# Task 1: Engineering Notes, Trade-Offs & Stated Assumptions

> **Author**: Rohit  
> **Module**: `TASK-1-Growth-Machine`  

---

## 1. Explicit Architectural Decisions & Trade-Offs

### Decision 1: Python CLI & Modular Object Pipeline vs. No-Code (n8n/Zapier)
- **Choice**: Built a clean, object-oriented Python pipeline (`growth_engine.py` + `run_machine.py`) with declarative JSON configuration.
- **Why**:
  - No-code tools (Zapier/Make) obscure validation logic and make git diff review cumbersome for engineering teams.
  - Python scripts are fully deterministic, version-controlled, testable in CI/CD, and allow programmatic evaluation gates with exact token/cost logging.

### Decision 2: Focus on Grant & Technical Proposal PIs vs. Generic SaaS Marketers
- **Choice**: Narrowed audience strictly to technical proposal writers and applied research PIs.
- **Why**:
  - Generic SaaS marketing content (blog posts, LinkedIn copy) is low-stakes and already saturated by basic chat windows.
  - Multi-section technical grants and RFCs represent maximum document pain: strict page limits, cross-section dependency constraints, mathematical notation, and high monetary stakes ($500k–$5M grants). If SuperDocs solves this, the willingness to pay is nearly inelastic.

### Decision 3: Synthetic Persona Sinks vs. Mock External API Requests
- **Choice**: All pipeline outputs are routed directly to local structured files and synthetic inbox sinks (`*.local`).
- **Why**:
  - Complies 100% with the fundamental rule of the evaluation: *Zero outbound contact to real humans or companies*.
  - Enables instant local evaluation of runs without network dependency flakes.

---

## 2. What We Explicitly Cut (And Why)

1. **Cut Live Web Scraping inside the Pipeline**:
   - *Rationale*: Scraping live websites introduces flaky DOM changes, rate blocks, and unpredictable latency. Using structured public metadata schemas ensures deterministic runs.
2. **Cut Automated Multi-Step Email Cadence Logic**:
   - *Rationale*: SuperDocs' growth moat is not annoying email spam sequences; it is providing high-taste technical artifacts that convert on product value. We focused all engineering on deliverable quality and structural integrity.
3. **Cut PDF Layout Rendering Engine**:
   - *Rationale*: SuperDocs is a live document editing environment, not an Adobe InDesign clone. Delivering clean Markdown + Diff blocks respects the product's true identity.

---

## 3. Product Rails Verification Checklist

- [x] Zero real outbound / zero cold emails sent.
- [x] No spreadsheet editing or spreadsheet output promises.
- [x] No claim of live web browsing within the core editor.
- [x] No claim of unearned compliance certifications.
- [x] All redactions and data privacy claims framed with explicit human-in-the-loop requirements.
- [x] Repeatable double batch execution logged with zero manual code changes between runs.
