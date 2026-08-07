# doctask-rohit — SuperDocs Growth Engineer Round 2 Submission

> **Candidate**: Rohit  
> **Repository Name**: `doctask-rohit`  
> **Collaborator Added**: `o-kadam` (Omkar Kadam, Founder @ SuperDocs)  
> **Role Track**: GTM / Growth Engineer (Round 2)  
> **Credit Line**: *Built by Rohit for the SuperDocs Growth Engineer evaluation.*

---

## 🎯 Executive Overview

This repository contains the complete, production-grade deliverables for the **SuperDocs GTM / Growth Engineer Round 2 evaluation**. It demonstrates autonomous growth systems engineering, rigorous target research, high-taste practitioner distribution, and honest data-backed measurement.

---

## 📁 Repository Map

```text
doctask-rohit/
├── TASK-1-Growth-Machine/
│   ├── Audience.md                     # Deep audience profile: Deep-Tech / AI Labs & Consultancies
│   ├── Growth Strategy.md              # Research Artifact Gifting engine & inbound conversion economics
│   ├── Architecture.md                 # Full system architecture and execution flow diagrams
│   ├── Machine/                        # Working Python automation pipeline
│   │   ├── growth_engine.py            # Core 4-stage pipeline (Ingestion -> Analysis -> Generation -> Delivery)
│   │   ├── config.json                 # Model prompts, quality grading rules, synthetic config
│   │   ├── synthetic_batch_1.json      # Batch 1 (5 synthetic target profiles)
│   │   ├── synthetic_batch_2.json      # Batch 2 (5 new synthetic profiles for autonomous Run 2)
│   │   └── run_machine.py              # CLI batch runner and telemetry logger
│   ├── Outputs/                        # Autonomous execution logs and produced deliverables
│   │   ├── batch_1_run_log.json        # Run 1 execution trace, token counters, latency & delivery sink
│   │   ├── batch_1_produced_assets/    # 5 tailored technical audit memos from Run 1
│   │   ├── batch_2_run_log.json        # Run 2 execution trace (zero manual patching)
│   │   ├── batch_2_produced_assets/    # 5 tailored technical audit memos from Run 2
│   │   └── Sample_Produced_Asset.md    # Highlight showcase asset
│   ├── Measurements.md                 # Unit economics, drop-offs, 10x bottleneck breakdown, human-in-the-loop gates
│   └── Notes.md                        # Assumptions, engineering trade-offs, and technical rationale
│
├── TASK-2-Assigned-Build/              # Assigned: "Resource-first launch into a practitioner community"
│   ├── Resource/                       # "The Pre-Submission Grant & Peer-Review Audit Dossier"
│   │   ├── Dossier_Template.md         # Full text of the practitioner resource
│   │   ├── Section_Audit_Checklists.md # Review checklists & citation integrity trackers
│   │   └── Sample_Rendered_Pack.md     # Fully formatted markdown artifact
│   ├── Launch Plan.md                  # Community selection, written rules audit, intro copy, disclosure, follow-up playbook
│   ├── Exported_Resource_Preview.html  # Exportable HTML/PDF-styled print preview
│   └── README.md                       # Summary of the resource build and distribution mechanics
│
├── TASK-3-Use-Cases/                   # 10 Real Enterprise & Mid-Market Document Friction Use Cases
│   ├── Use Cases.md                    # 10 detailed use cases with honest product fit evaluations
│   ├── Companies.md                    # Real researched companies & why document friction bites them
│   └── Buyers.md                       # Target internal buyer roles, current tool failure modes, door-openers
│
├── TASK-4/                             # Demo Scripts, Video Plan, 1-Page Write-Up & Questions
│   ├── Clip_Script.md                  # 15–30 sec voiceover script & storyboard for "File to finished file, timed"
│   ├── Demo_Video_Script.md            # 3–5 min comprehensive demo walkthrough recording guide
│   ├── Write-up.md                     # 1-page executive summary (what was built, strategic calls, cuts, real numbers)
│   ├── Metrics.md                      # North Star metric dashboard & conversion funnel
│   └── Submission_Questions.md         # Answers to all 5 official submission questions + brand/naming bonus
│
├── Extras/                             # Extra Credit & Extended Engineering
│   ├── SuperDocs_MCP_Integration_Spec.md # MCP integration architecture & code sample
│   └── GTM_Autonomous_System_Design.md  # 20-to-100 person autonomous GTM architecture blueprint
│
├── TASK.md                             # Operational guide on working with this repository
├── PROGRESS.md                         # Log of assumptions, key milestones, and decisions
└── README.md                           # This index file
```

---

## ⚡ Quickstart: Running the Growth Machine

To run the Growth Machine locally and generate fresh runs:
```powershell
# Navigate to the machine directory
cd TASK-1-Growth-Machine/Machine

# Run Batch 1
python run_machine.py --batch 1

# Run Batch 2 (runs autonomously with zero code changes)
python run_machine.py --batch 2
```

Logs, JSON traces, and generated technical assets are written directly to `TASK-1-Growth-Machine/Outputs/`.
