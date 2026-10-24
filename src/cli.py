"""
CLI Interface for Pigouvian Automation Tax Engine.
"""

import argparse
import json
import sys
from .pigouvian_tax_engine import MacroeconomicParameters, simulate_macroeconomic_equilibrium
from .task_automation_ledger import evaluate_task_portfolio


def main():
    parser = argparse.ArgumentParser(
        description="Pigouvian Automation Tax & AI Layoff Trap Simulator (Falk & Tsoukalas, 2026)"
    )
    parser.add_argument("--mpc", type=float, default=0.78, help="Marginal Propensity to Consume (default: 0.78)")
    parser.add_argument("--human-wage", type=float, default=145000.0, help="Human annual loaded wage (default: 145000.0)")
    parser.add_argument("--ai-cost", type=float, default=6500.0, help="AI compute annual cost (default: 6500.0)")
    parser.add_argument("--firms", type=int, default=50, help="Number of competing firms (default: 50)")
    parser.add_argument("--json", action="store_true", help="Output pure JSON format")
    parser.add_argument("--ledger", action="store_true", help="Print granular activity ledger")

    args = parser.parse_args()

    params = MacroeconomicParameters(
        mpc=args.mpc,
        human_wage_annual=args.human_wage,
        ai_compute_cost_annual=args.ai_cost,
        num_competing_firms=args.firms
    )

    sim = simulate_macroeconomic_equilibrium(params)

    if args.json:
        output = sim.model_dump()
        if args.ledger:
            output["ledger"] = evaluate_task_portfolio()
        print(json.dumps(output, indent=2))
        return

    print("================================================================================")
    print(" [*] PIGOUVIAN AUTOMATION TAX ENGINE & AI LAYOFF TRAP SIMULATOR")
    print("     Reference: Brett Hemenway Falk (UPenn) & Gerry Tsoukalas (BU / Wharton)")
    print("================================================================================")
    print(f" Human Wage (w_h):             ${params.human_wage_annual:,.2f} / yr")
    print(f" AI Compute Cost (c_AI):       ${params.ai_compute_cost_annual:,.2f} / yr")
    print(f" Microeconomic Arbitrage:      ${sim.labor_cost_arbitrage:,.2f} / worker")
    print(f" Market Firm Count (N):        {params.num_competing_firms} firms")
    print(f" Externalized Share (1 - 1/N): {sim.firm_externality_share * 100:.2f}%")
    print(f" Marginal Propensity to Consume: {params.mpc:.2f}")
    print("--------------------------------------------------------------------------------")
    print(f" [+] Optimal Pigouvian Tax (tau*):  ${sim.optimal_pigouvian_tax:,.2f} / FTE displaced")
    print(f" [~] Effective AI Cost (c + tau):  ${sim.effective_ai_cost:,.2f} / yr")
    print("--------------------------------------------------------------------------------")
    print(f" Unregulated Demand Loss (1k FTE): ${sim.demand_destruction_unregulated:,.2f}")
    print(f" Regulated Demand Loss (With HITL): ${sim.demand_stabilized_regulated:,.2f}")
    print("================================================================================")
    print(sim.equilibrium_description)

    if args.ledger:
        print("\n--- TASK & ACTIVITY AUTOMATION LEDGER ---")
        ledger = evaluate_task_portfolio()
        for act in ledger["activities"]:
            print(f"[{act['activity_id']}] {act['job_family']} - {act['task_name']}")
            print(f"      Risk: {act['displacement_risk_pct']}% | Tax Rate: {act['pigouvian_tax_rate_pct']}% | Policy: {act['policy_action']}")


if __name__ == "__main__":
    main()
