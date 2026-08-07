# Task 4: Official Submission Form Answers

> **Candidate**: Rohit  
> **Track**: GTM / Growth Engineer (Round 2)  
> **Philosophy**: *Blunt, actionable, highly specific criticism scores in our favor.*

---

## Question 1: What Broke (Bugs, Rough Edges & Confusing Moments)

1. **Cold-Start Session Warmup Latency on Web UI (`use.superdocs.app`)**:
   - *Symptom*: On initiating a fresh document session, the first AST indexing and prompt turn occasionally stalls for 20–35 seconds before returning the initial diff stream.
   - *Impact*: In self-serve user onboarding, a 30-second cold-start creates immediate funnel drop-off.
   - *Recommended Fix*: Keep a pre-warmed worker pool for new session initialization and display an explicit "Indexing chunk hierarchy..." progress state instead of an ambiguous spinning loader.
2. **Chunk Boundary Splitting in Multi-Section Contiguous Edits**:
   - *Symptom*: When requesting synchronized edits across two adjacent sub-headings (e.g. Section 2.1 and Section 2.2), the diff generator occasionally consolidates both into a single `proposed_change_batch` rather than exposing granular per-chunk accept/reject toggles.
   - *Recommended Fix*: Preserve distinct AST node IDs at the paragraph/subheading level in the review card so users can accept Section 2.1 while rejecting Section 2.2.
3. **Citation Anchor Key Drops During Aggressive Condensation**:
   - *Symptom*: When prompting the AI to "condense by 40%", LaTeX/BibTeX citation keys (e.g. `[@vaswani2017attention]`) are occasionally dropped if the parent clause is restructured.
   - *Recommended Fix*: Add a post-generation citation preservation assertion on the server that rejects the draft turn and retries if source citation tokens are omitted.
4. **Table Cell Formatting on Complex Multi-Column PDF Export**:
   - *Symptom*: Wide markdown/HTML comparison tables with multi-line cell text occasionally wrap awkwardly or clip margin borders on strict PDF rendering.
   - *Recommended Fix*: Introduce an automatic column-width calculation heuristic in the PDF print CSS stylesheet with responsive font scaling.

---

## Question 2: The One Morning Number

### **Weekly Active Document Edit Loops (WADEL)**
- **Definition**: The count of document sessions per week where a user:
  1. Opens or uploads an existing multi-section document (`.docx`, `.tex`, `.md`, PDF).
  2. Executes an in-document AI edit prompt across $\ge 1$ targeted chunks.
  3. Inspects the diff in Review Mode and **Accepts** the modification (`approval_mode='ask_every_time'` or in-editor accept).
- **Why this specific number**:
  - In an AI document application, top-of-funnel prompt counts are dangerous vanity metrics. A user can run 20 prompts in a chat window and leave frustrated.
  - **WADEL** measures the closed loop: *Did the AI actually save the user from manual editing in their core document?*
  - If WADEL is growing week-over-week, SuperDocs is becoming an indispensable daily tool. If WADEL drops while prompt volume rises, users are rejecting edits and hitting UX friction.

---

## Question 3: Five Features to Build Next, One to Drop & Immediate Fixes

### Five Features to Build Next (In Priority Order):
1. **Bidirectional Git / GitHub Sync for `.tex` and `.md` Documents**:
   - Allow technical teams to link a GitHub repository so document edits sync cleanly via Git branches and PRs, unifying developers, researchers, and technical writers.
2. **Granular Sub-Chunk Diff Review (Accept/Reject by Paragraph/Sentence)**:
   - Enhance the HITL review interface so users can cherry-pick specific paragraph modifications within a larger section update.
3. **Citation & Cross-Reference Graph Engine**:
   - A dedicated inspection panel that maps all cross-references (equations, figures, tables, bibliography keys) and alerts users when a section edit breaks a downstream reference.
4. **Custom Organization Style Guide Linters**:
   - Allow enterprise organizations to upload house style guides (e.g. Nature style, company tone guidelines) that act as strict constraints on every AI turn.
5. **SuperDocs MCP CLI & 1-Click Agent Plugin Expansion**:
   - Package the 38 production MCP tools into an instant 1-command installer (`npx @superdocs/mcp-setup`) for Claude Code, Cursor, and VS Code.

### The One Thing to Drop:
- **Drop Standalone Presentation / Slide Generation**:
  - Slide creation dilutes product focus and competes with specialized tools (Gamma, Tome). SuperDocs' superpower is deep, structured, high-stakes text documents. Stay relentlessly focused on being the *"Cursor for documents"*.

### Immediate Frictions to Fix:
- Pre-warm backend workers to eliminate first-turn session latency.
- Add an explicit visual highlight on the document canvas indicating which chunk IDs are actively being modified during an SSE streaming run.

---

## Question 4: Autonomous GTM Operation at 20-to-100 Person Scale

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
   - Agents monitor public registries (arXiv preprints, NIH/NSF awards, GitHub RFCs, SEC filings) to extract target document structures and parameter complexities.
2. **Artifact Synthesis & Quality Gate Loop**:
   - Multi-stage LLM agents synthesize high-value structural audit memos and domain-specific templates.
   - Deterministic Python validators check tone, guardrails, and markdown syntax against strict scoring rules.
3. **Human-in-the-Loop Steering Cockpit**:
   - A single growth engineer reviews flagged edge cases in a 15-minute morning dashboard, approving or adjusting prompt parameters.
4. **What Breaks First at Scale**:
   - *Nuance hallucination in niche sub-fields* (e.g. misinterpreting biological assay units).
   - *Mitigation*: Partition agent prompts with curated few-shot domain databases and automated citation assertions.

---

## Question 5: Growth Audit of `superdocs.app` & `docs.superdocs.app`

### 1. `superdocs.app` (Landing Page Critique):
- **Current Weakness**: The landing page is visually clean but leans on abstract claims. A first-time visitor takes 15–20 seconds to realize SuperDocs is an *in-document editor with diff review*, not another ChatGPT wrapper.
- **Specific Recommendations**:
  1. **Above-the-Fold Interactive Diff Hero**: Replace static hero text with an interactive widget where visitors can click a prompt and watch 3 sections edit in-place with red/green diffs.
  2. **Sharpen the "Cursor for Documents" Positioning**: Make the core headline explicit: *"ChatGPT gives you text to copy-paste. SuperDocs edits the document you already have."*
  3. **Feature Comparison Matrix**: Add a side-by-side table comparing *ChatGPT Web* vs *Google Docs* vs *SuperDocs* across chunk-level editing, diff reviews, and citation retention.

### 2. `docs.superdocs.app` (Developer & Integration Docs):
- **Current Strength**: Exhaustive capability catalog with 38 MCP tools, async job polling, and SSE streaming.
- **Specific Recommendations**:
  1. **Promote the 1-Line MCP Setup Command**: Move the Claude Code & Cursor MCP installation command to the top banner of the docs home page.
  2. **Interactive API Playground**: Add an in-browser request tester where developers can test `/v1/chat` with `response_mode='compact'` on sample `.docx` files.

---

## 🎁 Bonus: Brand & Naming Exploration

1. **`Contextra` (`contextra.app` / `contextra.dev`)**:
   - *Rationale*: Blends "Context" and "Structure"—emphasizing full-document contextual intelligence over isolated chat boxes.
2. **`Docsmith` (`docsmith.ai` / `docsmith.io`)**:
   - *Rationale*: Evokes craftsmanship, precision, and surgical editing for high-stakes documents.
3. **`RefactorDoc` (`refactordoc.com`)**:
   - *Rationale*: Instantly resonates with developers and technical authors who love refactoring code and want that exact superpower for documents.
