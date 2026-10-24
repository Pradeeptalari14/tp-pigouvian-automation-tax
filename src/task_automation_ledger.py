"""
Task and Activity Automation Ledger
Granular micro-economic activity breakdown across tech, engineering, and operations roles.
"""

from typing import List, Dict
from pydantic import BaseModel, Field


class AutomationActivity(BaseModel):
    activity_id: str
    job_family: str
    task_name: str
    human_hourly_cost: float = Field(gt=0, description="Loaded human hourly wage ($/hr)")
    compute_task_cost: float = Field(ge=0, description="Equivalent AI agent inference cost ($/unit)")
    unit_basis: str
    displacement_risk_pct: float = Field(ge=0, le=100)
    pigouvian_tax_rate_pct: float = Field(ge=0, le=100)
    policy_action: str


STANDARD_ACTIVITY_LEDGER: List[AutomationActivity] = [
    AutomationActivity(
        activity_id="SWE-01",
        job_family="Software Engineering",
        task_name="Boilerplate CRUD & Unit Test Generation",
        human_hourly_cost=125.0,
        compute_task_cost=0.04,
        unit_basis="per endpoint",
        displacement_risk_pct=92.0,
        pigouvian_tax_rate_pct=42.5,
        policy_action="Taxed Speed Governor"
    ),
    AutomationActivity(
        activity_id="SWE-02",
        job_family="Software Engineering",
        task_name="Distributed System Architecture Design",
        human_hourly_cost=195.0,
        compute_task_cost=12.50,
        unit_basis="per design doc",
        displacement_risk_pct=18.0,
        pigouvian_tax_rate_pct=0.0,
        policy_action="Exempt Augmented HITL"
    ),
    AutomationActivity(
        activity_id="SRE-01",
        job_family="Cloud Ops / SRE",
        task_name="Alert Triage & Log Anomaly Parsing",
        human_hourly_cost=145.0,
        compute_task_cost=0.02,
        unit_basis="per incident runbook",
        displacement_risk_pct=88.0,
        pigouvian_tax_rate_pct=46.0,
        policy_action="Automated Transition Buffer"
    ),
    AutomationActivity(
        activity_id="VOX-01",
        job_family="Customer Success / Voice Ops",
        task_name="L1 Outbound Qualification Telephony",
        human_hourly_cost=36.0,
        compute_task_cost=0.15,
        unit_basis="per 3-min call",
        displacement_risk_pct=96.0,
        pigouvian_tax_rate_pct=48.2,
        policy_action="High Displacement Surcharge"
    ),
    AutomationActivity(
        activity_id="LEG-01",
        job_family="Legal & Compliance",
        task_name="Commercial Contract Redlining & Review",
        human_hourly_cost=320.0,
        compute_task_cost=3.50,
        unit_basis="per contract",
        displacement_risk_pct=74.0,
        pigouvian_tax_rate_pct=38.0,
        policy_action="Retraining Offset Fund"
    ),
    AutomationActivity(
        activity_id="FIN-01",
        job_family="FinOps & Accounting",
        task_name="Multi-Cloud Invoice Reconciliation & Ingestion",
        human_hourly_cost=95.0,
        compute_task_cost=0.80,
        unit_basis="per monthly billing cycle",
        displacement_risk_pct=82.0,
        pigouvian_tax_rate_pct=35.0,
        policy_action="Balanced Hybrid Credit"
    )
]


def evaluate_task_portfolio(activities: List[AutomationActivity] = None) -> Dict[str, Any]:
    """Evaluates aggregate displacement exposure and tax proceeds across activities."""
    if activities is None:
        activities = STANDARD_ACTIVITY_LEDGER

    total_activities = len(activities)
    avg_displacement_risk = sum(a.displacement_risk_pct for a in activities) / total_activities
    avg_tax_rate = sum(a.pigouvian_tax_rate_pct for a in activities) / total_activities

    high_risk_activities = [a for a in activities if a.displacement_risk_pct >= 70.0]

    return {
        "total_activities_evaluated": total_activities,
        "high_displacement_count": len(high_risk_activities),
        "mean_displacement_risk_pct": round(avg_displacement_risk, 2),
        "mean_pigouvian_tax_rate_pct": round(avg_tax_rate, 2),
        "activities": [a.model_dump() for a in activities]
    }
