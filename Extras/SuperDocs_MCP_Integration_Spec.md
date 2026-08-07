# Extras: SuperDocs Model Context Protocol (MCP) Integration Spec

> **Overview**: How to seamlessly integrate SuperDocs as a native Model Context Protocol (MCP) server for coding agents like Claude Code, Cursor, and custom agentic frameworks.

---

## 1. MCP Tool Architecture

The SuperDocs MCP server exposes 4 atomic tools to external coding agents:

```json
{
  "name": "superdocs_edit_document",
  "description": "Applies targeted, in-place multi-section edits to a SuperDocs document with diff review tracking.",
  "parameters": {
    "type": "object",
    "properties": {
      "document_id": { "type": "string", "description": "Unique identifier of the target document" },
      "target_sections": { 
        "type": "array", 
        "items": { "type": "string" },
        "description": "List of section headers or AST node IDs to modify" 
      },
      "edit_instructions": { "type": "string", "description": "Natural language editing directive" },
      "preserve_citations": { "type": "boolean", "default": true }
    },
    "required": ["document_id", "target_sections", "edit_instructions"]
  }
}
```

---

## 2. Example MCP Agent Call (Python)

```python
import json
import requests

class SuperDocsMCPClient:
    def __init__(self, api_key: str, base_url: str = "https://api.superdocs.app/v1"):
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        self.base_url = base_url

    def refactor_sections(self, document_id: str, sections: list, instruction: str):
        payload = {
            "document_id": document_id,
            "target_sections": sections,
            "instruction": instruction,
            "mode": "review_diff"
        }
        response = requests.post(f"{self.base_url}/documents/refactor", json=payload, headers=self.headers)
        return response.json()

# Example Agent Execution:
if __name__ == "__main__":
    client = SuperDocsMCPClient(api_key="SUPERDOCS_TEST_KEY")
    result = client.refactor_sections(
        document_id="doc_grant_2026",
        sections=["Section 3.1", "Section 6.4"],
        instruction="Align compute budget numbers to 8x H100 GPU cluster."
    )
    print("SuperDocs In-Document Edit Triggered:", result)
```
