# Task 1: Growth Machine Architecture & Data Flow

This document details the modular software architecture of the **SuperDocs Autonomous Growth Machine** (`TASK-1-Growth-Machine/Machine/`).

---

## 1. System Topology & Pipeline Diagram

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│                    SUPERDOCS AUTONOMOUS GROWTH ENGINE                       │
└─────────────────────────────────────────────────────────────────────────────┘
                                     │
                                     ▼
                     ┌───────────────────────────────┐
                     │   Stage 1: Target Ingestion   │
                     │  (synthetic_batch_1/2.json)   │
                     └───────────────┬───────────────┘
                                     │ Normalized Account Schema
                                     ▼
                     ┌───────────────────────────────┐
                     │  Stage 2: Friction & Context  │
                     │       Analyzer Engine         │
                     └───────────────┬───────────────┘
                                     │ Extraction of Document Vulnerabilities
                                     ▼
                     ┌───────────────────────────────┐
                     │ Stage 3: SuperDocs Asset Gen  │
                     │ (Bespoke Technical Audit Pack)│
                     └───────────────┬───────────────┘
                                     │ Formatted Markdown & Prompt Specs
                                     ▼
                     ┌───────────────────────────────┐
                     │  Stage 4: Automated QA & Gate │
                     │  (Tone, Rails & Syntax Check) │
                     └───────────────┬───────────────┘
                                     │
                     ┌───────────────┴───────────────┐
                     ▼                               ▼
      [Pass: Score >= 85%]             [Fail: Score < 85%]
                     │                               │
                     ▼                               ▼
      ┌─────────────────────────────┐ ┌─────────────────────────────┐
      │   Outputs/ Batch Asset      │ │ Quarantined / Logged in     │
      │  & Structured JSON Telemetry│ │ Run Log for Human Review    │
      └─────────────────────────────┘ └─────────────────────────────┘
```

---

## 2. Core Modules in `Machine/`

### 1. `growth_engine.py` (Core Engine)
- **`TargetIngestionModule`**: Reads raw batch inputs (JSON format), validates schema completeness, and computes baseline document complexity indicators.
- **`DocumentFrictionAnalyzer`**: Identifies specific cross-section synchronization risks (e.g. parameter drift between Abstract, Methodology, and Budget; citation staleness; multi-author style divergence).
- **`SuperDocsAssetGenerator`**: Synthesizes a high-taste, 4-section Technical Audit Memo containing actionable structural recommendations, citation graphs, and exact SuperDocs multi-section refactor instructions.
- **`QualityGateVerifier`**: Automatically scores the generated deliverable across 4 strict dimensions (Technical Specificity, Tone & Taste, Guardrail Compliance, Formatting Integrity). If the score is below 85%, the record is flagged for human review.
- **`TelemetryLogger`**: Collects runtime statistics (latency per stage, simulated token usage, estimated cost, gate pass rate, and delivery timestamps).

### 2. `run_machine.py` (CLI Runner)
- Provides standard command-line flags (`--batch 1`, `--batch 2`, `--output-dir`).
- Executes end-to-end processing without requiring manual file edits or runtime patches between batches.

### 3. `Automations/` (n8n & Apollo Orchestration Suite)
- **`n8n_growth_workflow.json`**: An importable, valid n8n JSON workflow file connecting arXiv signal ingestion, Apollo REST enrichment, complexity scoring, AI synthesis, and automated QA gating.
- **`Apollo_API_Spec.json`**: Complete REST API endpoint schemas (`/v1/organizations/enrich` and `/v1/people/match`) and target filter queries.
- **`n8n_Setup_Guide.md`**: Complete step-by-step visual deployment and configuration guide.
- **`n8n_runner.py`**: Runnable CLI testing harness simulating the full n8n node execution graph.

### 4. `Dashboard/` (GTM Operations Cockpit)
- **`index.html`**: A dark-mode, responsive GTM command center allowing growth operators to inspect enriched accounts, review 3-touch campaigns, execute **Human Gate 1** approvals, and monitor real-time pipeline telemetry.

### 5. `Landing_Page/` (Dynamic Programmatic Landing Page)
- **`index.html`**: A high-converting programmatic landing page featuring a live ICP segment switcher (Bio-AI Labs, Engineering RFCs, Open Research Communities, and custom company personalization).

---

## 3. Data Flow & Schemas

### Input Schema (`synthetic_batch_X.json`)
```json
{
  "target_id": "SYNTH-001",
  "organization_name": "Latent Space Bio",
  "domain": "AI-Driven Protein Engineering & Wet-Lab Assays",
  "active_document_type": "ARPA-H Technical Milestone Proposal",
  "document_page_count": 52,
  "contributor_count": 5,
  "current_primary_tool": "Google Docs + Overleaf + Claude Web",
  "primary_technical_friction": "Experimental assay parameters in Section 4 drift from compute allocation in Section 7",
  "recipient_role": "Lead Principal Investigator",
  "synthetic_inbox": "pi-eval-sink@test-lab.internal"
}
```

### Output Schema (`batch_X_run_log.json`)
```json
{
  "batch_id": "batch_1",
  "timestamp": "2026-08-07T17:26:00Z",
  "total_records_processed": 5,
  "records_passed_gate": 5,
  "records_failed_gate": 0,
  "avg_processing_latency_ms": 142.5,
  "total_simulated_tokens": 14250,
  "estimated_total_cost_usd": 0.057,
  "records": [ ... ]
}
```
