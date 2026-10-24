try:
    import pytest
except ImportError:
    pytest = None

from src.pigouvian_tax_engine import (
    MacroeconomicParameters,
    compute_optimal_tax,
    simulate_macroeconomic_equilibrium
)
from src.task_automation_ledger import (
    AutomationActivity,
    evaluate_task_portfolio,
    STANDARD_ACTIVITY_LEDGER
)


def test_monopoly_zero_externality():
    """
    When N = 1 (monopoly), the single firm internalizes the entire macroeconomic
    purchasing power of consumers, so (1 - 1/N) = 0 and tau* = 0.
    """
    params = MacroeconomicParameters(num_competing_firms=1)
    tax = compute_optimal_tax(params)
    assert tax == 0.0


def test_atomistic_competition_convergence():
    """
    As N -> large (e.g. 1000), (1 - 1/N) approaches 1.0.
    tau* approaches MPC * (w_h - c_AI).
    """
    params = MacroeconomicParameters(
        mpc=0.8,
        human_wage_annual=100000.0,
        ai_compute_cost_annual=10000.0,
        num_competing_firms=1000
    )
    tax = compute_optimal_tax(params)
    expected_asymptotic = 0.8 * 90000.0 * (1 - 1/1000)
    assert abs(tax - expected_asymptotic) < 1.0


def test_zero_arbitrage_non_negative_tax():
    """
    If AI compute cost exceeds human wage, no tax is levied (arbitrage <= 0).
    """
    params = MacroeconomicParameters(
        human_wage_annual=50000.0,
        ai_compute_cost_annual=80000.0,
        num_competing_firms=50
    )
    tax = compute_optimal_tax(params)
    assert tax == 0.0


def test_simulation_equilibrium_results():
    """Verifies complete macroeconomic simulation run."""
    params = MacroeconomicParameters(
        mpc=0.75,
        human_wage_annual=120000.0,
        ai_compute_cost_annual=20000.0,
        num_competing_firms=100,
        unemployment_safety_net=30000.0,
        human_capital_retraining_efficiency=0.5
    )
    sim = simulate_macroeconomic_equilibrium(params)
    assert sim.labor_cost_arbitrage == 100000.0
    assert sim.firm_externality_share == 0.99
    assert sim.optimal_pigouvian_tax == 74250.0
    assert sim.effective_ai_cost == 94250.0
    assert sim.demand_destruction_unregulated > sim.demand_stabilized_regulated
    assert "Cooperate_Retain" in sim.corporate_dilemma_payoffs
    assert "Defect_Displace" in sim.corporate_dilemma_payoffs


def test_activity_ledger_evaluation():
    """Verifies granular task and activity risk calculations."""
    ledger = evaluate_task_portfolio(STANDARD_ACTIVITY_LEDGER)
    assert ledger["total_activities_evaluated"] >= 5
    assert ledger["high_displacement_count"] >= 3
    assert 0.0 < ledger["mean_displacement_risk_pct"] <= 100.0
    assert 0.0 < ledger["mean_pigouvian_tax_rate_pct"] <= 100.0
