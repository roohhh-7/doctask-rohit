#!/usr/bin/env python3
"""
CLI Batch Runner for SuperDocs Growth Engine
Usage:
    python run_machine.py --batch 1
    python run_machine.py --batch 2
"""

import os
import sys
import argparse
from growth_engine import GrowthEngine


def main():
    parser = argparse.ArgumentParser(description="Run SuperDocs Growth Machine on a specified batch.")
    parser.add_argument("--batch", type=str, required=True, help="Batch identifier ('1' or '2' or full path)")
    parser.add_argument("--config", type=str, default="config.json", help="Path to config.json")
    parser.add_argument("--outputs-dir", type=str, default="../Outputs", help="Path to outputs directory")

    args = parser.parse_args()

    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(script_dir, args.config)
    outputs_dir = os.path.join(script_dir, args.outputs_dir)
    os.makedirs(outputs_dir, exist_ok=True)

    if args.batch == "1":
        batch_path = os.path.join(script_dir, "synthetic_batch_1.json")
    elif args.batch == "2":
        batch_path = os.path.join(script_dir, "synthetic_batch_2.json")
    else:
        batch_path = args.batch

    if not os.path.exists(batch_path):
        print(f"[ERROR] Batch file not found: {batch_path}")
        sys.exit(1)

    print(f"================================================================")
    print(f"  SUPERDOCS GROWTH MACHINE — RUNNING BATCH: {args.batch}")
    print(f"  Input Source: {batch_path}")
    print(f"  Output Sink:  {outputs_dir}")
    print(f"================================================================")

    engine = GrowthEngine(config_path)
    result = engine.process_batch(batch_path, outputs_dir)

    print(f"\n[SUCCESS] Batch Completed!")
    print(f"  - Total Processed: {result['total_records_processed']}")
    print(f"  - Passed QA Gate:  {result['records_passed_gate']}")
    print(f"  - Quarantined:     {result['records_failed_gate']}")
    print(f"  - Pass Rate:       {result['pass_rate_percent']}%")
    print(f"  - Avg Latency:     {result['avg_latency_per_record_ms']} ms/record")
    print(f"  - Total Tokens:    {result['total_simulated_tokens']}")
    print(f"  - Total Est. Cost: ${result['estimated_total_cost_usd']}")
    print(f"  - Run Log Saved:   {os.path.join(outputs_dir, result['batch_name'] + '_run_log.json')}")
    print(f"================================================================\n")


if __name__ == "__main__":
    main()
