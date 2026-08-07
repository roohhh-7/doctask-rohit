# TASK.md — Working Protocol & Operations Guide

> **Candidate**: Rohit  
> **Repository**: `doctask-rohit`  
> **Submission Track**: SuperDocs Round 2 — GTM / Growth Engineer  
> **Collaborator**: `o-kadam` (Omkar Kadam)  

---

## 1. Operating Philosophy

This repository is organized to demonstrate end-to-end agency, taste, technical execution, and rigorous measurement.

### Core Working Rules
1. **Zero Outbound to Real Persons/Companies**:
   - Outbound engines and pipelines run exclusively against synthetic prospect profiles and verified self-owned test sinks.
   - Researched company entities are real, public organizations; all prospect names, emails, and contact handles are strictly synthetic.
2. **Honest Capabilities & Clear Boundaries**:
   - SuperDocs is accurately modeled as the "Cursor for documents" — focused on closing the loop between AI text generation and in-document structural editing.
   - We do not market or design around capabilities outside the spec (no spreadsheet output engines, no live web scraping from within the editor, no unearned compliance claims).
3. **Resumable & Deterministic Pipelines**:
   - Every script, automation step, and batch execution logs full telemetry (run status, latency, input tokens, output tokens, cost estimates, and error captures).
   - Scripts are stateless across batches and can be rerun on arbitrary new input sets without patching.
4. **Transparent Verification**:
   - All claims, funnel numbers, and unit economics are derived from explicit conversion models and stated assumptions.

---

## 2. Workspace Navigation

- **[`TASK-1-Growth-Machine/`](file:///c:/Users/rohit/OneDrive/Desktop/superdocs/TASK-1-Growth-Machine/)**: Complete growth machine for Technical Proposal & Grant Writing PIs. Includes audience research, strategy, architecture, Python automation engine, two autonomous batch execution runs with logs, sample deliverables, and honest measurement analysis.
- **[`TASK-2-Assigned-Build/`](file:///c:/Users/rohit/OneDrive/Desktop/superdocs/TASK-2-Assigned-Build/)**: Resource-first practitioner launch into academic and deep-tech research communities ("The Pre-Submission Grant & Peer-Review Audit Dossier").
- **[`TASK-3-Use-Cases/`](file:///c:/Users/rohit/OneDrive/Desktop/superdocs/TASK-3-Use-Cases/)**: 10 researched enterprise and mid-market use cases, mapped companies, internal buyer titles, and conversation door-openers.
- **[`TASK-4/`](file:///c:/Users/rohit/OneDrive/Desktop/superdocs/TASK-4/)**: Feature clip storyboard ("File to finished file, timed"), 3.5-minute demo video script, 1-page executive write-up, metrics dashboard, and answers to all 5 official submission questions.
- **[`Extras/`](file:///c:/Users/rohit/OneDrive/Desktop/superdocs/Extras/)**: MCP server integration specifications and 20-to-100 person autonomous GTM architecture blueprint.

---

## 3. How to Execute the Growth Machine

To run the pipeline locally:
```powershell
# From the repository root:
cd TASK-1-Growth-Machine/Machine
python run_machine.py --batch 1
python run_machine.py --batch 2
```
All outputs and execution logs are automatically written to `TASK-1-Growth-Machine/Outputs/`.
