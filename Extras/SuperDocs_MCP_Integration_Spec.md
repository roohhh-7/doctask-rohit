# Extras: SuperDocs Model Context Protocol (MCP) Integration Spec

> **Overview**: Comprehensive specification for integrating SuperDocs via its production Model Context Protocol (MCP) server (`https://api.superdocs.app/mcp/`) across coding agents (Claude Code, Cursor, VS Code, Claude Desktop, and autonomous custom agents).

---

## 1. Official MCP Server Architecture

SuperDocs exposes a unified Streamable HTTP MCP endpoint:
- **Endpoint**: `https://api.superdocs.app/mcp/`
- **Authentication**: `Bearer sk_...` (User Key) or `Bearer lce_...` (Organization Key)
- **Tool Catalog**: **38 Production MCP Tools** + **4 User-Invocable Workflow Prompts** (e.g. `/superdocs:edit_styled_docx`, `/superdocs:convert_format`).

```text
┌────────────────────────┐         Streamable HTTP          ┌───────────────────────────┐
│  AI Coding Agent       │ ───────────────────────────────> │  SuperDocs MCP Server     │
│  (Claude Code, Cursor, │ <─────────────────────────────── │  (https://api.superdocs.app│
│   VS Code, Custom Bot) │          SSE Stream              │   /mcp/ - 38 Tools)       │
└────────────────────────┘                                  └─────────────┬─────────────┘
                                                                          │
                                                                          ▼
                                                            ┌───────────────────────────┐
                                                            │ Chunk-ID Structural Engine│
                                                            │ • AST Par-level IDs       │
                                                            │ • HITL Diff Approvals     │
                                                            │ • Lossless LaTeX/Docx IO  │
                                                            └───────────────────────────┘
```

---

## 2. Key MCP Tools for Autonomous Document Refactoring

### Core Document Editing & HITL Tools:
1. `edit_document`: Natural language structural edits targeting exact chunk IDs, preserving tables and formatting.
2. `chat_async` / `approve_proposed_changes`: Enables Human-in-the-Loop (`approval_mode='ask_every_time'`), returning structured `proposed_change_batch` diffs.
3. `revert_session_to_message`: Snaps conversation and document state back to any prior turn.
4. `agent_signup` & `agent_adopt`: Fully autonomous AI agents can sign up, pass a proof-of-work challenge, obtain an API key, and hand off ownership to their human sponsor.

---

## 3. Production MCP Client Integration (Python)

```python
import json
import requests

class SuperDocsProductionClient:
    def __init__(self, api_key: str, base_url: str = "https://api.superdocs.app/v1"):
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        self.base_url = base_url

    def submit_targeted_edit(self, session_id: str, prompt: str, approval_mode: str = "ask_every_time"):
        """
        Executes a targeted structural edit using SuperDocs compact response mode
        and chunk-ID precision.
        """
        payload = {
            "message": prompt,
            "response_mode": "compact",      # Emits only chunk_diffs (500-2,000 tokens vs 130k)
            "approval_mode": approval_mode   # HITL approval mode for high-stakes revisions
        }
        response = requests.post(f"{self.base_url}/chat/{session_id}", json=payload, headers=self.headers)
        return response.json()

    def get_session_diffs(self, session_id: str, job_id: str):
        """Polls async job status and returns granular per-section before/after HTML diffs."""
        response = requests.get(f"{self.base_url}/jobs/{job_id}", headers=self.headers)
        return response.json()

# Example Autonomous Agent Execution:
if __name__ == "__main__":
    client = SuperDocsProductionClient(api_key="sk_live_sample_token")
    print("SuperDocs Production MCP Client Initialized.")
```
