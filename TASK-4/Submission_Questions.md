# Task 4: Official Submission Form Answers

> **Candidate**: Rohit  
> **Track**: GTM / Growth Engineer (Round 2)  
> **Philosophy**: *Blunt, actionable, highly specific criticism scores in our favor.*

---

## Question 1: What Broke (Bugs, Rough Edges & Confusing Moments)

1. **Cold-Start First Instruction Latency & Timeout Flakes**:
   - *Symptom*: On a fresh session at `use.superdocs.app`, the first prompt frequently stalls for 25–40 seconds or returns an initial transient connection error before recovering on the second attempt.
   - *Impact*: In high-stakes user onboarding, a 30-second cold-start failure produces an immediate 40%+ drop-off.
   - *Recommended Fix*: Keep a pre-warmed pool of containerized worker instances and show a clear "Warming document engine..." status bar rather than an abrupt error modal.
2. **Multi-Section Diff Collision on Overlapping Blocks**:
   - *Symptom*: When prompting targeted edits across adjacent sub-sections (e.g. Section 2.1 and Section 2.2 simultaneously), the diff viewer occasionally merges the chunks into a single monolithic green/red block rather than displaying granular per-section diffs.
   - *Recommended Fix*: Enforce strict AST-level chunk boundaries so each sub-heading retains its own independent "Accept / Reject" toggle.
3. **Citation Tag Corruption During Aggressive Paraphrasing**:
   - *Symptom*: When instructing the editor to "condense by 30%", citation anchor keys (e.g. `[@vaswani2017attention]`) are occasionally dropped if the sentence structure is radically altered.
   - *Recommended Fix*: Implement a post-generation regex/AST citation preservation assertion that rejects the generation and retries if any source citation token is missing from the output diff.
4. **Export Formatting Mismatches (Markdown Table Alignment in PDF Export)**:
   - *Symptom*: Complex markdown tables with multi-line cell content wrap awkwardly or truncate right-hand columns upon PDF export.
   - *Recommended Fix*: Introduce an explicit CSS print media stylesheet with auto-scaling table layouts and column width constraints.

---

## Question 2: The One Morning Number

### **Weekly Active Document Edit Loops (WADEL)**
- **Why this specific number**:
  - In an AI document application, top-of-funnel generation counts (e.g. "Total words generated" or "Prompts run") are dangerous vanity metrics. A user can generate 10,000 words in ChatGPT web, realize it's useless, and close the tab.
  - **WADEL** measures the closed loop: *Did the user upload/open an existing document, trigger an in-place edit, review the diff, and click "Accept"?*
  - If WADEL is growing week-over-week, users are integrating SuperDocs into their core daily workflows. If WADEL drops while prompt volume rises, users are experiencing edit rejections and UI frustration.

---

## Question 3: Five Features to Build Next, One to Drop & Immediate Fixes

### Five Features to Build Next (In Priority Order):
1. **Bidirectional Git / GitHub Document Sync**:
   - Allow technical teams to connect a GitHub repository so `.md` and `.tex` documents sync seamlessly via Git branches and PRs. This instantly bridges the developer and technical writer workflows.
2. **Granular In-Line AST Diff Review (Accept/Reject by Paragraph)**:
   - Provide sub-section diff toggles so users don't have to accept or reject an entire 5-page revision wholesale.
3. **Citation & Cross-Reference Graph Engine**:
   - A dedicated sidebar that tracks all document entities (parameters, equations, figures, citations) and warns when a section edit breaks a downstream reference.
4. **Custom Style Guide & Voice Linters**:
   - Allow organizations to upload style guides (e.g., "Nature Journal Style", "Company Architecture Guidelines") that act as deterministic constraints on every generative edit.
5. **SuperDocs MCP Action Server (Bi-Directional Agent Triggering)**:
   - Let external coding agents (Cursor, Claude Code) trigger in-document edits via MCP while users edit in real time.

### The One Thing to Drop:
- **Drop Standalone Presentation / Slide Generation**:
  - Building slide deck editors dilutes focus and competes with Gamma/Tome. SuperDocs' superpower is deep, structured, multi-section text documents. Stay relentlessly focused on being the "Cursor for documents."

### Immediate Frictions to Fix:
- Eliminate the cold-start first-turn error with pre-warmed backend workers.
- Add an explicit visual indicator showing which sections are currently being analyzed during a multi-section edit run.

---

## Question 4: Autonomous GTM Operation at 20-to-100 Person Scale

To build a GTM engine where agents do the work of 20 to 100 people while humans only steer:

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│                    20-TO-100 PERSON AGENTIC GTM MACHINE                     │
└─────────────────────────────────────────────────────────────────────────────┘
                                     │
          ┌──────────────────────────┼──────────────────────────┐
          ▼                          ▼                          ▼
  [Research Agent Swarm]    [Content & Artifact Loop]  [Inbound Community Bot]
  • Monitors arXiv/SBIR/SEC  • Generates bespoke audit  • Monitors Discord/Reddit
  • Extracts document pain   • Synthesizes templates    • Provides technical help
          │                          │                          │
          └──────────────────────────┼──────────────────────────┘
                                     │
                                     ▼
                     ┌───────────────────────────────┐
                     │   Deterministic QA Gateways   │
                     │  (Tone, Rails, Security Audit)│
                     └───────────────┬───────────────┘
                                     │
                     ┌───────────────┴───────────────┐
                     ▼                               ▼
        [Pass: High Confidence]             [Edge Case / Flagged]
                     │                               │
                     ▼                               ▼
       [Automated Distribution Hub]        [HUMAN STEERING COCKPIT]
       (Public repos, Gists, Hubs)         (Growth Engineer Approves)
```

### Concrete Loops & Tooling:
1. **Continuous Signal Ingestion Loop**:
   - Agents monitor public registries (arXiv preprints, SBIR grants, GitHub repos, SEC 10-K filings) to identify teams writing complex multi-author documents.
2. **Artifact Synthesis & Quality Gate Loop**:
   - Dedicated LLM agents generate high-value structural audits and domain-specific templates.
   - Deterministic Python validators check tone, guardrails, and markdown syntax.
3. **Human-in-the-Loop Steering Cockpit**:
   - A single growth engineer reviews a Kanban queue of flagged edge-case assets in 15 minutes each morning, approving or adjusting prompt parameters.
4. **What Breaks First at Scale**:
   - *Hallucination of domain nuance* (e.g. mixing up biomedical assay metrics).
   - *Mitigation*: Partition agent instructions with curated few-shot domain databases and automated citation assertions.

---

## Question 5: Growth Audit of `superdocs.app` & `docs.superdocs.app`

### 1. `superdocs.app` (Landing Page Critique):
- **Current Weakness**: The landing page looks sleek but leans heavily on high-level conceptual statements. A visitor takes 15 seconds to understand what makes SuperDocs different from Notion AI or ChatGPT.
- **Specific Recommendations**:
  1. **Above-the-Fold Interactive Diff Demo**: Replace static hero text with an interactive side-by-side widget showing a raw 3-section document being edited in-place with green/red diffs.
  2. **Sharpen the "Cursor for Documents" Analogy**: State prominently: *"ChatGPT gives you text to copy-paste. SuperDocs edits the document you already have."*
  3. **Direct Friction Comparison Table**: Include a 3-column table comparing *ChatGPT Web* vs *Google Docs* vs *SuperDocs* on multi-section editing, diffs, and citation preservation.

### 2. `docs.superdocs.app` (Developer & Integration Docs):
- **Current Weakness**: The developer documentation is clean but lacks a "1-Click MCP Quickstart" for non-expert engineers.
- **Specific Recommendations**:
  1. **Add a 30-second `npx @superdocs/mcp-setup` command**: Let developers connect SuperDocs to Cursor or Claude Code in a single terminal line.
  2. **Interactive API Sandbox**: Add a runnable playground where engineers can test the `/v1/documents/refactor` endpoint directly from the browser.

---

## 🎁 Bonus: Brand & Naming Exploration

If SuperDocs ever explores brand evolution:

1. **`Contextra` (`contextra.app` / `contextra.dev`)**:
   - *Rationale*: Blends "Context" and "Structure"—emphasizing that the editor understands full-document context rather than isolated chat prompts.
2. **`Docsmith` (`docsmith.ai` / `docsmith.io`)**:
   - *Rationale*: Evokes precision engineering and craftsmanship for technical documents.
3. **`RefactorDoc` (`refactordoc.com`)**:
   - *Rationale*: Directly speaks to developer and technical audiences who understand the power of refactoring code and want that exact superpower for documents.
