# 🏛️ Pigouvian Automation Tax & The AI Layoff Trap Engine

[![CI](https://github.com/Pradeeptalari14/tp-pigouvian-automation-tax/actions/workflows/ci.yml/badge.svg)](https://github.com/Pradeeptalari14/tp-pigouvian-automation-tax/actions/workflows/ci.yml)
[![DevSecOps](https://github.com/Pradeeptalari14/tp-pigouvian-automation-tax/actions/workflows/devsecops-audit.yml/badge.svg)](https://github.com/Pradeeptalari14/tp-pigouvian-automation-tax/actions/workflows/devsecops-audit.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Studio: #349](https://img.shields.io/badge/Studio-%23349_Live-emerald)](https://talaripradeep.info/studios/pigouvian-automation-tax/)

Deterministic Macroeconomic Equilibrium and Task Disruption Simulation Engine modeling the **Corporate Prisoner's Dilemma**, aggregate purchasing power decay, and the **optimal Pigouvian automation speed governor**.

Directly models and validates the economic research paper:
> **"The AI Layoff Trap"** (2026)  
> **Brett Hemenway Falk** (University of Pennsylvania) & **Gerry Tsoukalas** (Boston University / Wharton)

---

## 🔬 Core Formulations & Research Findings

### 1. The Corporate Prisoner's Dilemma
When an individual firm replaces human labor ($w_h$) with compute ($c_{AI}$), it captures **100% of the microeconomic margin arbitrage**:
$$\Delta \text{Margin}_i = w_h - c_{AI}$$
However, it externalizes the demand reduction onto the entire macroeconomic product market. Because atomistic competitors cannot unilaterally refrain from automation without sacrificing margins, all firms automate aggressively:
$$\text{Nash Outcome: (Defect, Defect) } \to \text{Macroeconomic aggregate demand destruction}$$

### 2. The Optimal Pigouvian Automation Tax
To internalize the market failure, the optimal speed governor tax per displaced FTE is:
$$\tau^* = \text{MPC} \times (w_h - c_{AI}) \times \left(1 - \frac{1}{N}\right)$$
* $\text{MPC} \in [0.65, 0.90]$: Marginal propensity to consume of the displaced labor cohort.
* $N$: Number of competing firms. In a monopoly ($N=1$), $\tau^*=0$ because the single firm already internalizes its consumer base. In atomistic competition ($N \to \infty$), $(1 - 1/N) \to 1$, requiring full Pigouvian internalization.
* **100% Dividend Recycling:** Tax revenues fund human-in-the-loop (HITL) wage offsets and multi-year retraining endowments.

---

## 🚀 Quickstart & CLI Simulator

```bash
# Clone the repository
git clone https://github.com/Pradeeptalari14/tp-pigouvian-automation-tax.git
cd tp-pigouvian-automation-tax

# Install dependencies
pip install -r requirements.txt

# Run the macroeconomic CLI simulation
python -m src.cli --mpc 0.78 --human-wage 145000 --ai-cost 6500 --firms 50 --ledger

# Output structured JSON for pipeline integration
python -m src.cli --json
```

---

## 📊 Granular Activity Ledger

| Job Family | Displaced Activity | Human Hourly | Compute Unit Cost | Disruption Risk | Tax Buffer ($\tau^*$) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Software Dev** | Boilerplate CRUD generation, unit tests | $125.00/hr | $0.04/endpoint | 92% | 42.5% Speed-governed |
| **Cloud Ops / SRE** | Incident log triage, alert remediation | $145.00/hr | $0.02/incident | 88% | 46.0% Transition Buffer |
| **Voice Ops / CS** | L1 Outbound Qualification Telephony | $36.00/hr | $0.15/3-min call | 96% | 48.2% Surcharge |
| **Legal / Compliance** | Commercial contract review | $320.00/hr | $3.50/contract | 74% | 38.0% Retraining Fund |
| **FinOps** | Multi-Cloud billing reconciliation | $95.00/hr | $0.80/cycle | 82% | 35.0% Hybrid Credit |

---

## 🛡️ 9+ DevSecOps Governance

* **Keyless Cosign Signing:** Ephemeral OIDC signing attached to container releases.
* **Semgrep SAST:** Custom AST scanning preventing unpinned stochastic drift and arithmetic division hazards.
* **CycloneDX SBOM:** Automated dependency manifest generation.
* **Distroless Runtime:** Minimal container attack surface (`UID 65532`).
* **Deterministic Tests:** Full coverage of asymptotic market convergence and edge boundary constraints.

---

## 🌐 Live Interactive Studio
Explore the interactive visual simulator, live canvas demand curves, and dynamic Nash equilibrium matrix at:  
👉 **[https://talaripradeep.info/studios/pigouvian-automation-tax/](https://talaripradeep.info/studios/pigouvian-automation-tax/)**
