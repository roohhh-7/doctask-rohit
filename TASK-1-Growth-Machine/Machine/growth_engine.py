"""
SuperDocs Autonomous Growth Engine
----------------------------------
A multi-stage pipeline that automates:
1. Target profile ingestion and schema validation (Public Milestones: arXiv / NIH / GitHub)
2. Proposal friction and cross-section dependency analysis
3. High-taste personalized milestone outreach + SuperDocs template kit synthesis
4. Multi-dimension quality scoring and rail compliance gating
5. Telemetry logging, cost estimation, and delivery simulation
"""

import os
import json
import time
import datetime
from typing import Dict, Any, List, Tuple


class GrowthEngine:
    def __init__(self, config_path: str):
        with open(config_path, "r", encoding="utf-8") as f:
            self.config = json.load(f)
        self.min_score = self.config.get("min_quality_score_threshold", 85.0)

    def process_batch(self, batch_file_path: str, output_base_dir: str) -> Dict[str, Any]:
        with open(batch_file_path, "r", encoding="utf-8") as f:
            targets = json.load(f)

        batch_name = os.path.splitext(os.path.basename(batch_file_path))[0]
        batch_assets_dir = os.path.join(output_base_dir, f"{batch_name}_produced_assets")
        os.makedirs(batch_assets_dir, exist_ok=True)

        batch_start_time = time.time()
        processed_records = []
        passed_count = 0
        failed_count = 0
        total_tokens = 0

        for target in targets:
            record_start = time.time()
            
            # Stage 1: Ingestion & Validation
            is_valid, validation_msg = self._validate_target(target)
            if not is_valid:
                processed_records.append({
                    "target_id": target.get("target_id", "UNKNOWN"),
                    "status": "ERROR_VALIDATION",
                    "message": validation_msg
                })
                failed_count += 1
                continue

            # Stage 2: Proposal Friction & Milestone Analysis
            friction_profile = self._analyze_friction(target)

            # Stage 3: SuperDocs Outreach & Template Kit Synthesis
            asset_markdown, token_count = self._synthesize_asset(target, friction_profile)
            total_tokens += token_count

            # Stage 4: Automated Quality Gate
            quality_score, score_breakdown, passes_gate = self._evaluate_quality(target, asset_markdown)
            
            record_latency_ms = round((time.time() - record_start) * 1000, 2)

            if passes_gate:
                passed_count += 1
                status = "PASSED_GATE"
                # Save generated asset
                asset_filename = f"{target['target_id']}_{target['organization_name'].replace(' ', '_')}_Outreach_Pack.md"
                asset_path = os.path.join(batch_assets_dir, asset_filename)
                with open(asset_path, "w", encoding="utf-8") as af:
                    af.write(asset_markdown)
            else:
                failed_count += 1
                status = "QUARANTINED"
                asset_filename = None

            # Calculate cost estimate
            prompt_tokens = int(token_count * 0.4)
            comp_tokens = int(token_count * 0.6)
            cost_usd = (prompt_tokens / 1000.0 * self.config["cost_per_1k_prompt_tokens_usd"]) + \
                       (comp_tokens / 1000.0 * self.config["cost_per_1k_completion_tokens_usd"])

            processed_records.append({
                "target_id": target["target_id"],
                "organization_name": target["organization_name"],
                "recipient_role": target["recipient_role"],
                "synthetic_inbox": target["synthetic_inbox"],
                "status": status,
                "quality_score": quality_score,
                "score_breakdown": score_breakdown,
                "simulated_tokens": token_count,
                "estimated_cost_usd": round(cost_usd, 5),
                "latency_ms": record_latency_ms,
                "produced_asset_file": asset_filename
            })

        total_batch_latency_ms = round((time.time() - batch_start_time) * 1000, 2)
        total_prompt_tokens = int(total_tokens * 0.4)
        total_comp_tokens = int(total_tokens * 0.6)
        total_batch_cost_usd = (total_prompt_tokens / 1000.0 * self.config["cost_per_1k_prompt_tokens_usd"]) + \
                               (total_comp_tokens / 1000.0 * self.config["cost_per_1k_completion_tokens_usd"])

        batch_log = {
            "batch_name": batch_name,
            "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "total_records_processed": len(targets),
            "records_passed_gate": passed_count,
            "records_failed_gate": failed_count,
            "pass_rate_percent": round((passed_count / len(targets)) * 100.0, 1) if targets else 0,
            "avg_latency_per_record_ms": round(total_batch_latency_ms / len(targets), 2) if targets else 0,
            "total_simulated_tokens": total_tokens,
            "estimated_total_cost_usd": round(total_batch_cost_usd, 4),
            "records": processed_records
        }

        # Save run log
        log_path = os.path.join(output_base_dir, f"{batch_name}_run_log.json")
        with open(log_path, "w", encoding="utf-8") as lf:
            json.dump(batch_log, lf, indent=2)

        return batch_log

    def _validate_target(self, target: Dict[str, Any]) -> Tuple[bool, str]:
        required_keys = ["target_id", "organization_name", "domain", "active_document_type", "recipient_role", "synthetic_inbox"]
        for key in required_keys:
            if key not in target or not target[key]:
                return False, f"Missing required key: {key}"
        # Guardrail check: Ensure synthetic inbox pattern
        if not ("internal-test-sink.local" in target["synthetic_inbox"] or "test" in target["synthetic_inbox"]):
            return False, "Target violates synthetic inbox guardrail"
        return True, "Valid"

    def _analyze_friction(self, target: Dict[str, Any]) -> Dict[str, Any]:
        pages = target.get("document_page_count", 40)
        contributors = target.get("contributor_count", 4)
        friction_risk = "HIGH" if pages > 50 or contributors > 5 else "MEDIUM"
        return {
            "friction_risk_level": friction_risk,
            "sync_complexity_index": round((pages * 0.1) + (contributors * 0.5), 1),
            "primary_bottleneck": target.get("primary_technical_friction", "Cross-section parameter divergence")
        }

    def _synthesize_asset(self, target: Dict[str, Any], friction: Dict[str, Any]) -> Tuple[str, int]:
        org = target["organization_name"]
        doc_type = target["active_document_type"]
        role = target["recipient_role"]
        params = target.get("core_parameters", {})
        model_type = params.get("model_type", "Domain Neural Pipeline")
        benchmark = params.get("eval_benchmark", "High-fidelity target precision")
        grant_val = f"${params.get('grant_amount_usd', 1000000):,}"

        markdown = f"""# Milestone Intelligence & Proposal Outreach Pack
**Recipient**: {role}, {org}  
**Trigger Milestone**: Public Publication / Award of *{doc_type}*  
**Research Stack**: {model_type} | Target Metric: {benchmark} | Scope: {grant_val}  

---

## 1. Personalized Outbound Email (Respectful & Non-Intrusive)

**Subject**: {doc_type} & multi-author proposal drafting  
**To**: {role} at {org}

```text
Hi there,

Congratulations to the team at {org} on the recent milestone with "{doc_type}"! Tracking your work on {model_type} has been really impressive.

When expanding technical breakthroughs into 50+ page grant proposals or follow-up RFCs, keeping 20+ sections, compute tables, and citation anchors in sync across multiple co-authors in Word or Google Docs quickly becomes a major headache.

We built a free Proposal & Manuscript Template Kit in SuperDocs (think "Cursor for documents"):
- Section-Precision Editing: Update parameters (e.g. compute allocations or dataset sizes) across multiple sections in one prompt without rewriting the whole document.
- In-Document Red/Green Diff Review: Inspect every proposed change highlighted on the page before accepting.
- Strict Privacy: Zero model training on user text, isolated private workspaces, and 100% US-hosted infrastructure.

Here is a 1-click sandbox link pre-loaded with a sample technical proposal to test the diff editor:
👉 https://use.superdocs.app/sandbox/{org.lower().replace(' ', '-')}-proposal-kit

No sales call or credit card required. Hope this saves your team hours on the next drafting cycle!

Best regards,
Rohit | Growth Engineer, SuperDocs
```

---

## 2. Parameter Alignment & Section Architecture Matrix

| Section Identifier | Target Parameter Spec | Multi-Section Dependency | Alignment Solution |
|---|---|---|---|
| **Section 2 / Executive Abstract** | Target Metric: `{benchmark}` | Section 5 Milestones | Synchronized in-document update |
| **Section 3.2 / Architecture Spec** | Architecture: `{model_type}` | Section 7 Compute Allocation | Synchronized budget table refactor |
| **Section 4.1 / Validation Protocols** | Empirical Baseline | Appendix Citation Index | Lossless BibTeX citation preservation |

---

## 3. SuperDocs In-Document Refactor Spec (1-Click Diff Execution)

```markdown
<!-- SUPERDOCS EXECUTION PROMPT -->
@document-target: [Section 2.1, Section 3.2, Section 7.4]
Instruction:
Reconcile all architecture parameter references to match "{model_type}".
Ensure benchmark targets strictly reflect "{benchmark}".
Update compute cluster allocation tables in Section 7 without breaking inline citation tags.
Preserve all mathematical formulas, LaTeX styling, and markdown table structures in-place.
```

### Native Diff Preview (What the Researcher Sees):
```diff
- Baseline throughput benchmark: uncalibrated legacy architecture
+ Synchronized throughput benchmark: {benchmark} ({model_type})
- Estimated cluster footprint: 32 x A100 SXM4 (obsolete allocation)
+ Estimated cluster footprint: Reconciled per Section 3.2 architectural parameters
```

---

## 4. Privacy & Ethical Guardrail Disclosure
*This campaign piece was synthesized by an automated growth intelligence engine using public milestone metadata. No private drafts were accessed, and zero emails were transmitted to real individuals during this evaluation.*
"""
        simulated_tokens = len(markdown.split()) * 4 + 450
        return markdown, simulated_tokens

    def _evaluate_quality(self, target: Dict[str, Any], markdown: str) -> Tuple[float, Dict[str, float], bool]:
        scores = {}
        
        # 1. Technical Specificity (0-25)
        has_model = target.get("core_parameters", {}).get("model_type", "") in markdown
        has_org = target["organization_name"] in markdown
        scores["technical_specificity"] = 25.0 if has_model and has_org else 15.0

        # 2. Taste & Tone (0-25)
        has_sales_fluff = any(w in markdown.lower() for w in ["best-in-class", "revolutionary", "game-changing", "act now"])
        scores["taste_and_tone"] = 15.0 if has_sales_fluff else 25.0

        # 3. Guardrail & Rail Compliance (0-25)
        has_privacy_notice = "Privacy & Ethical Guardrail Disclosure" in markdown
        has_no_spreadsheet_promise = "spreadsheet output" not in markdown.lower()
        scores["rails_compliance"] = 25.0 if has_privacy_notice and has_no_spreadsheet_promise else 10.0

        # 4. Formatting & Syntax Integrity (0-25)
        has_tables = "|" in markdown and "---" in markdown
        has_diff = "```diff" in markdown
        scores["syntax_integrity"] = 25.0 if has_tables and has_diff else 15.0

        total_score = sum(scores.values())
        passes_gate = total_score >= self.min_score

        return total_score, scores, passes_gate
