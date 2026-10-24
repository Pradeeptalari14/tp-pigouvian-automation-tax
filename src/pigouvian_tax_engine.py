"""
Pigouvian Automation Tax Engine
Implements the macroeconomic speed governor and Corporate Prisoner's Dilemma
models from 'The AI Layoff Trap' (Falk & Tsoukalas, 2026).
"""

from typing import Dict, Any, List
from pydantic import BaseModel, Field


class MacroeconomicParameters(BaseModel):
    """Macroeconomic parameters determining equilibrium tax rates."""
    mpc: float = Field(default=0.78, ge=0.0, le=1.0, description="Marginal Propensity to Consume")
    human_wage_annual: float = Field(default=145000.0, gt=0, description="Average annual human knowledge worker wage ($)")
    ai_compute_cost_annual: float = Field(default=6500.0, ge=0, description="Annual compute/token inference cost per FTE equivalent ($)")
    num_competing_firms: int = Field(default=50, ge=1, description="Number of competing firms in the macroeconomic market")
    unemployment_safety_net: float = Field(default=28000.0, ge=0, description="Annual public safety net / transfer payment per displaced worker ($)")
    human_capital_retraining_efficiency: float = Field(default=0.45, ge=0.0, le=1.0, description="Share of tax recycled into human-in-the-loop upskilling")


class SimulationResult(BaseModel):
    """Output metrics from the Pigouvian Automation Tax engine."""
    labor_cost_arbitrage: float
    firm_externality_share: float
    optimal_pigouvian_tax: float
    effective_ai_cost: float
    demand_destruction_unregulated: float
    demand_stabilized_regulated: float
    corporate_dilemma_payoffs: Dict[str, Dict[str, float]]
    equilibrium_description: str


def compute_optimal_tax(params: MacroeconomicParameters) -> float:
    """
    Computes the optimal Pigouvian Automation Tax per worker displaced:
    tau* = MPC * (w_h - c_AI) * (1 - 1/N)
    
    When N = 1 (monopoly), (1 - 1/N) = 0. A single monopoly firm already
    internalizes the complete macroeconomic purchasing power of its consumers.
    As N -> infinity (atomistic competition), (1 - 1/N) -> 1. Atomistic firms
    have zero individual incentive to preserve macro aggregate demand.
    """
    arbitrage = max(0.0, params.human_wage_annual - params.ai_compute_cost_annual)
    if params.num_competing_firms <= 1:
        firm_externality_share = 0.0
    else:
        firm_externality_share = 1.0 - (1.0 / params.num_competing_firms)
    optimal_tax = params.mpc * arbitrage * firm_externality_share
    return round(optimal_tax, 2)


def simulate_macroeconomic_equilibrium(params: MacroeconomicParameters) -> SimulationResult:
    """
    Simulates both unregulated Nash race and Pigouvian-regulated Social Optimum.
    """
    arbitrage = max(0.0, params.human_wage_annual - params.ai_compute_cost_annual)
    if params.num_competing_firms <= 1:
        firm_externality_share = 0.0
    else:
        firm_externality_share = 1.0 - (1.0 / params.num_competing_firms)
    optimal_tax = compute_optimal_tax(params)
    effective_ai_cost = params.ai_compute_cost_annual + optimal_tax

    # Macroeconomic aggregate demand delta per 1,000 workers displaced
    income_loss_per_worker = max(0.0, params.human_wage_annual - params.unemployment_safety_net)
    demand_destruction_per_1k = 1000 * params.mpc * income_loss_per_worker
    
    # Under optimal tax recycling, tax revenue offsets demand loss via HITL subsidies
    recycling_dividend = 1000 * (optimal_tax * params.human_capital_retraining_efficiency)
    net_demand_destruction_regulated = max(0.0, demand_destruction_per_1k - recycling_dividend)

    # 2x2 Game-Theoretic Corporate Prisoner's Dilemma Payoff Matrix
    # Options: [Retain_Hybrid, Displace_Aggressively]
    # Payoffs format: (Firm_i Profit Index, Competitor_j Profit Index)
    retain_hybrid_both = 100.0  # Stable demand, moderate margins
    displace_aggressive_both = 64.0  # Lower costs, but macro collapse shrinks total market
    unilateral_displace = 135.0  # Firm i steals margin share while market has not yet collapsed
    unilateral_victim = 45.0  # Firm j bears high cost structure in shrinking market

    payoffs = {
        "Cooperate_Retain": {
            "Cooperate_Retain": retain_hybrid_both,
            "Defect_Displace": unilateral_victim
        },
        "Defect_Displace": {
            "Cooperate_Retain": unilateral_displace,
            "Defect_Displace": displace_aggressive_both
        }
    }

    equilibrium_summary = (
        f"Without regulation, (Defect, Defect) is the unique Nash Equilibrium with payoff {displace_aggressive_both:.1f}. "
        f"The Pigouvian speed governor tau*=${optimal_tax:,.2f} internalizes the {firm_externality_share*100:.1f}% "
        f"market externality, aligning micro incentives with the Social Optimum."
    )

    return SimulationResult(
        labor_cost_arbitrage=round(arbitrage, 2),
        firm_externality_share=round(firm_externality_share, 4),
        optimal_pigouvian_tax=optimal_tax,
        effective_ai_cost=round(effective_ai_cost, 2),
        demand_destruction_unregulated=round(demand_destruction_per_1k, 2),
        demand_stabilized_regulated=round(net_demand_destruction_regulated, 2),
        corporate_dilemma_payoffs=payoffs,
        equilibrium_description=equilibrium_summary
    )
