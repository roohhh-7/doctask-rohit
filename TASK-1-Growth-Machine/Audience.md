# Task 1: Target Audience Definition & Problem Space

> **Selected Audience**: **Principal Investigators (PIs) and Technical Directors at Applied AI & Bio-Tech Research Labs / Boutique AI Consultancies**  
> **Specific Cohort**: Small to mid-sized research teams (5–35 researchers/engineers) writing high-stakes, multi-section documents (DARPA/NSF/Horizon grant proposals, technical RFCs, multi-tenant AI system architecture briefs, and client technical audit deliverables).

---

## 1. Who They Are

This audience consists of technical leaders and senior researchers who bridge scientific research, technical architecture, and external funding/procurement.

- **Titles**: Principal Investigator, Lead Research Scientist, Director of Applied AI, Technical Partner.
- **Organization Types**:
  - Independent AI research institutes (e.g., applied labs spinning out of universities, open-source AI consortia).
  - Boutique AI engineering consultancies (e.g., specialized teams deploying custom foundation models or drug discovery pipelines).
  - High-tier GovTech / defense AI contractors.
- **Document Output**:
  - 30–70 page grant proposals (NSF, ARPA-H, SBIR Phase II).
  - 15–40 page client technical architecture dossiers and safety/alignment evaluation packs.
  - Multi-contributor technical RFCs with complex math formulas, citation graphs, and architecture diagrams.

---

## 2. What They Do Today (The Existing Workflow & Friction)

### Current Stack
- **Drafting & Collaboration**: Google Docs (for real-time typing), Overleaf/LaTeX (for scientific papers), or Notion/Markdown files (for internal specs).
- **AI "Assistance"**: Claude Web, ChatGPT Plus, or Cursor (for code only).

### The Exact Point of Failure (The "Copy-Paste Loop")
1. A 45-page proposal has 8 distinct sections written by 4 different researchers.
2. The PI wants to update Section 3.2 ("Evaluation Methodology") to reflect newly benchmarked inference latency data without breaking references in Section 5 ("Budget Justification") and Section 1 ("Executive Abstract").
3. **The Chat Window Trap**:
   - The PI copies 4 pages of text into Claude/ChatGPT web.
   - Claude generates a rewritten 4-page block in a separate chat panel.
   - The PI must manually copy it back, reformat headers, fix broken markdown/latex tables, and verify whether inline citations survived.
   - *Result*: The PI spends 45 minutes doing manual formatting triage for a 2-minute AI edit.
4. **Context Drift**:
   - Web chatbots cannot see the remaining 40 pages of the proposal, so the generated section uses conflicting terminology and obsolete parameter names.

---

## 3. What Would Genuinely Make Them Switch to SuperDocs

The switch is driven by three specific SuperDocs capabilities that directly eliminate their biggest pain points:

1. **In-Document Targeted Multi-Section Editing**:
   - The AI acts directly inside the document hierarchy (like Cursor's `composer` or `Cmd+K` for code).
   - The user can highlight 3 disjoint sections across a 50-page document and instruct: *"Update all parameter references from llama-3-70b to mistral-large across Sections 2, 4, and Appendix B, and reconcile citations."* The changes land directly in place.
2. **Review Mode with Diff Inspection**:
   - Researchers cannot blindly accept AI rewrites. SuperDocs' native diff review lets the PI step through green/red additions and deletions section by section before accepting.
3. **Citation & Cross-Reference Integrity**:
   - SuperDocs preserves citation keys and reference IDs during generative section rewrites, preventing the catastrophic "hallucinated bibliography" problem that plagues web LLMs.

---

## 4. How to Find the First 10 Target Companies

We do not scrape private individuals or send unsolicited generic spam. Instead, we identify 10 active organizations through public technical publication registries and grant award portals:

### Discovery Channels & Public Registries
1. **SBIR/STTR Grant Award Database (`sbir.gov/awards`)**: Filter by Phase I / Phase II awards in Artificial Intelligence, Biotechnology, and Quantum Computing from the last 6 months.
2. **arXiv / OpenReview Preprint Submissions**: Target labs actively publishing high-velocity research preprints with industry co-authors (e.g., NeurIPS / ICML / ICLR workshop tracks).
3. **GitHub Foundation Model Repositories**: Identify boutique consultancies maintaining open-source model forks and technical whitepapers.

### First 10 Target Companies (Publicly Researched Profiles)

| # | Researched Company | Focus Domain | Document Friction Point |
|---|---|---|---|
| 1 | **Latent Space Bio** | AI-driven protein design & wet-lab validation | 50+ page NIH/ARPA-H grant applications requiring strict cross-referencing between experimental assay protocols and compute budgeting. |
| 2 | **Cortex Systems Group** | Edge AI & defense autonomous robotics | SBIR Phase II technical proposals requiring precise MIL-STD specification compliance across 6 sub-contractor teams. |
| 3 | **Synthea Dynamics** | Synthetic data generation for clinical trials | FDA technical briefing documents with dense statistical tables and regulatory citation cross-checks. |
| 4 | **Vectorial AI Labs** | Enterprise LLM fine-tuning & evaluation | 40-page bespoke client architecture audit reports comparing latency, throughput, and GPU cluster topologies. |
| 5 | **NeuroPath Research** | Computational neuroscience & neural interfaces | DARPA multi-site collaborative grant deliverables with strict versioning and mathematical nomenclature. |
| 6 | **Foundry Quantum** | Quantum algorithm simulation & hybrid compute | DOE research proposals requiring exact mathematical notation preservation across multi-author drafts. |
| 7 | **Helios Energy Compute** | Grid-scale AI optimization for renewables | Commercial utility RFP responses (100+ pages) requiring multi-team section synchronization under tight 48h deadlines. |
| 8 | **Axiom Security Systems** | Automated formal verification for AI agents | ISO/IEC 42001 and EU AI Act compliance dossiers requiring precise audit-trail diffing. |
| 9 | **Epistemic Technologies** | Automated literature synthesis & drug repurposing | Systematic review protocols with hundreds of structured citations that break in standard web chat interfaces. |
| 10 | **Polymathic Labs** | Physics-informed neural networks (PINNs) | NSF multidisciplinary proposals bridging fluid dynamics and deep learning with heavy mathematical appendices. |
