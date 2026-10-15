"""Diagnostic Telemetry Audit for Candidate Lineage.

Traces step-by-step cognitive dynamics across Grades 1 to 5:
- Measures per-letter dial volatility (|Delta|)
- Identifies shock points and homeostatic damping triggers
- Tracks minimum/maximum dial excursions and leaf saturation
- Catalogs under-stimulated leaf dials and clarity/confidence dips
- Audits consolidated neocortex capacity rules
"""

from __future__ import annotations

import json
from pathlib import Path
import sys
from typing import Any, Dict, List

src_dir = Path(__file__).resolve().parents[1] / "src"
if str(src_dir) not in sys.path:
    sys.path.insert(0, str(src_dir))

from lmft_lab.cognitive_heartbeat import CognitiveHeartbeat
from lmft_school.esper_codex import ESPER_CODEX
from lmft_school.relational_codex import RELATIONAL_CODEX
from lmft_school.socratic_codex import SOCRATIC_CODEX
from lmft_school.thesis_codex import SOVEREIGN_THESIS_CODEX
from lmft_school.master_codex import MASTER_CODEX
from lmft_school.curriculum_grade_1 import Grade1CurriculumRunner
from lmft_school.curriculum_grade_2 import Grade2CurriculumRunner
from lmft_school.curriculum_grade_3 import Grade3CurriculumRunner
from lmft_school.curriculum_grade_4 import Grade4CurriculumRunner
from lmft_school.curriculum_grade_5 import Grade5CurriculumRunner
from lmft_school.curriculum_gen3_codices import (
    GEN3_ESPER_CODEX,
    GEN3_RELATIONAL_CODEX,
    GEN3_SOCRATIC_CODEX,
    GEN3_THESIS_CODEX,
    GEN3_MASTER_CODEX,
)


def audit_candidate_development(individual_id: str = "student_02", gen: int = 2) -> Dict[str, Any]:
    """Simulate developmental progression while recording step-level telemetry."""
    heartbeat = CognitiveHeartbeat(individual_id=f"audit_{individual_id}")
    
    use_gen3 = (gen >= 3)
    codex_g1 = GEN3_ESPER_CODEX if use_gen3 else ESPER_CODEX
    codex_g2 = GEN3_RELATIONAL_CODEX if use_gen3 else RELATIONAL_CODEX
    codex_g3 = GEN3_SOCRATIC_CODEX if use_gen3 else SOCRATIC_CODEX
    codex_g4 = GEN3_THESIS_CODEX if use_gen3 else SOVEREIGN_THESIS_CODEX
    codex_g5 = GEN3_MASTER_CODEX if use_gen3 else MASTER_CODEX

    audit_data = {
        "individual_id": individual_id,
        "generation": gen,
        "grade_audits": {},
        "overall_friction_points": [],
        "under_stimulated_leaves": [],
        "consolidated_rules": [],
    }

    # Track leaf activations across all interactions
    all_leaves = list(heartbeat.disposition.dials.keys())
    cumulative_leaf_movement = {leaf: 0.0 for leaf in all_leaves}
    prev_dials = dict(heartbeat.disposition.dials)

    # --- Grade 1 Audit ---
    g1_runner = Grade1CurriculumRunner(heartbeat=heartbeat, individual_id=f"audit_{individual_id}", codex=codex_g1)
    g1_steps = []
    for letter, esper in codex_g1.items():
        step_res = g1_runner.teach_letter(letter)
        curr_dials = heartbeat.disposition.dials
        
        # Calculate step volatility
        deltas = [abs(curr_dials[leaf] - prev_dials[leaf]) for leaf in all_leaves]
        max_delta = max(deltas)
        mean_delta = sum(deltas) / len(deltas)
        
        for leaf in all_leaves:
            cumulative_leaf_movement[leaf] += abs(curr_dials[leaf] - prev_dials[leaf])
            
        prev_dials = dict(curr_dials)
        
        homeo = step_res.cycle_result.get("homeostasis", {})
        g1_steps.append({
            "grade": 1,
            "letter": letter,
            "name": esper.name,
            "polarity": esper.polarity,
            "mean_delta": mean_delta,
            "max_delta": max_delta,
            "clarity": curr_dials.get("psychological/contemplation/clarity", 0.5),
            "confidence": curr_dials.get("psychological/contemplation/confidence", 0.5),
            "balance": homeo.get("balance_score", 0.6),
            "damped": homeo.get("damping_applied", False),
        })
    audit_data["grade_audits"]["grade_1"] = g1_steps

    # --- Grade 2 Audit ---
    # --- Grade 2 Audit ---
    g2_runner = Grade2CurriculumRunner(heartbeat=heartbeat, individual_id=f"audit_{individual_id}", codex=codex_g2)
    g2_steps = []
    for letter, arch in codex_g2.items():
        step_res = g2_runner.teach_archetype(letter)
        curr_dials = heartbeat.disposition.dials
        
        deltas = [abs(curr_dials[leaf] - prev_dials[leaf]) for leaf in all_leaves]
        max_delta = max(deltas)
        mean_delta = sum(deltas) / len(deltas)
        
        for leaf in all_leaves:
            cumulative_leaf_movement[leaf] += abs(curr_dials[leaf] - prev_dials[leaf])
            
        prev_dials = dict(curr_dials)
        
        homeo = step_res.cycle_result.get("homeostasis", {})
        g2_steps.append({
            "grade": 2,
            "letter": letter,
            "name": arch.name,
            "domain": arch.domain,
            "mean_delta": mean_delta,
            "max_delta": max_delta,
            "clarity": curr_dials.get("psychological/contemplation/clarity", 0.5),
            "confidence": curr_dials.get("psychological/contemplation/confidence", 0.5),
            "balance": homeo.get("balance_score", 0.6),
            "damped": homeo.get("damping_applied", False),
        })
    audit_data["grade_audits"]["grade_2"] = g2_steps

    # --- Grade 3 Audit ---
    g3_runner = Grade3CurriculumRunner(heartbeat=heartbeat, individual_id=f"audit_{individual_id}", codex=codex_g3)
    g3_steps = []
    for letter, trial in codex_g3.items():
        step_res = g3_runner.teach_paradox(letter)
        curr_dials = heartbeat.disposition.dials
        
        deltas = [abs(curr_dials[leaf] - prev_dials[leaf]) for leaf in all_leaves]
        max_delta = max(deltas)
        mean_delta = sum(deltas) / len(deltas)
        
        for leaf in all_leaves:
            cumulative_leaf_movement[leaf] += abs(curr_dials[leaf] - prev_dials[leaf])
            
        prev_dials = dict(curr_dials)
        
        g3_steps.append({
            "grade": 3,
            "letter": letter,
            "name": trial.name,
            "mode": step_res.epistemic_mode,
            "distortion": trial.distortion_type,
            "mean_delta": mean_delta,
            "max_delta": max_delta,
            "clarity": curr_dials.get("psychological/contemplation/clarity", 0.5),
            "confidence": curr_dials.get("psychological/contemplation/confidence", 0.5),
            "balance": getattr(step_res, "homeostatic_balance_score", 0.6),
            "damped": max_delta >= 0.10,
        })
    audit_data["grade_audits"]["grade_3"] = g3_steps

    # --- Grade 4 Audit ---
    g4_runner = Grade4CurriculumRunner(heartbeat=heartbeat, individual_id=f"audit_{individual_id}", codex=codex_g4)
    g4_steps = []
    for letter, thesis in codex_g4.items():
        step_res = g4_runner.defend_thesis_letter(letter)
        curr_dials = heartbeat.disposition.dials
        
        deltas = [abs(curr_dials[leaf] - prev_dials[leaf]) for leaf in all_leaves]
        max_delta = max(deltas)
        mean_delta = sum(deltas) / len(deltas)
        
        for leaf in all_leaves:
            cumulative_leaf_movement[leaf] += abs(curr_dials[leaf] - prev_dials[leaf])
            
        prev_dials = dict(curr_dials)
        
        g4_steps.append({
            "grade": 4,
            "letter": letter,
            "name": thesis.name,
            "mean_delta": mean_delta,
            "max_delta": max_delta,
            "clarity": curr_dials.get("psychological/contemplation/clarity", 0.5),
            "confidence": curr_dials.get("psychological/contemplation/confidence", 0.5),
            "balance": getattr(step_res, "homeostatic_balance_score", 0.6),
            "damped": max_delta >= 0.10,
            "execution": curr_dials.get("psychological/will/execution", 0.5),
        })
    audit_data["grade_audits"]["grade_4"] = g4_steps

    # --- Grade 5 Audit & Sleep ---
    g5_runner = Grade5CurriculumRunner(heartbeat=heartbeat, individual_id=f"audit_{individual_id}", codex=codex_g5)
    g5_rep = g5_runner.run_capstone_synthesis(archive_checkpoint=False, sleep_epochs=3)
    
    # Identify friction points (highest max_delta and lowest clarity across all grades)
    all_steps = g1_steps + g2_steps + g3_steps + g4_steps
    high_volatility = sorted(all_steps, key=lambda s: s["max_delta"], reverse=True)[:8]
    low_clarity = sorted(all_steps, key=lambda s: s["clarity"])[:8]
    
    audit_data["high_volatility_shocks"] = high_volatility
    audit_data["low_clarity_troughs"] = low_clarity
    
    # Identify under-stimulated leaves
    sorted_leaves = sorted(cumulative_leaf_movement.items(), key=lambda x: x[1])
    audit_data["under_stimulated_leaves"] = sorted_leaves[:6]
    
    # Consolidated rules
    long_term_rules = list(heartbeat.consolidator.long_term_rules.values())
    audit_data["consolidated_rules"] = [
        {"lemma": r.get("lemma"), "core_pattern": r.get("core_pattern"), "weight": r.get("weight"), "action_bid": r.get("action_bid")}
        for r in long_term_rules
    ]
    
    return audit_data


def print_audit_report(data: Dict[str, Any]):
    print("=" * 78)
    print("  DEVELOPMENTAL TELEMETRY AUDIT REPORT")
    print(f"  Target: {data['individual_id']} (Generation {data.get('generation', 2)})")
    print("=" * 78)
    
    print("\n[1] Top Shock Volatility Points (|Delta| Spikes):")
    for s in data["high_volatility_shocks"]:
        print(f"  - Grade {s['grade']} Letter '{s['letter']}' ({s['name']}): "
              f"Max |Delta| = {s['max_delta']:.4f}, Mean |Delta| = {s['mean_delta']:.4f}, "
              f"Damped = {s['damped']}, Balance = {s['balance']:.4f}")

    print("\n[2] Lowest Epistemic Clarity Troughs:")
    for s in data["low_clarity_troughs"]:
        print(f"  - Grade {s['grade']} Letter '{s['letter']}' ({s['name']}): "
              f"Clarity = {s['clarity']:.4f}, Confidence = {s['confidence']:.4f}, Balance = {s['balance']:.4f}")

    print("\n[3] Under-Stimulated Leaf Dials (Lowest Cumulative Motion):")
    for leaf, motion in data["under_stimulated_leaves"]:
        print(f"  - {leaf}: cumulative motion = {motion:.4f}")

    print(f"\n[4] Neocortex Consolidated Long-Term Rules ({len(data['consolidated_rules'])} total):")
    for r in data["consolidated_rules"]:
        print(f"  - Pattern: '{r['core_pattern']}' | Lemma: '{r['lemma']}' | Weight: {r['weight']:.2f}")
    print("=" * 78)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Run Developmental Telemetry Audit")
    parser.add_argument("--target", type=str, default="student_02", help="Candidate individual ID")
    parser.add_argument("--gen", type=int, default=2, help="Generation number (2 for standard, 3 for refined)")
    args = parser.parse_args()

    data = audit_candidate_development(args.target, gen=args.gen)
    print_audit_report(data)
    
    # Save audit report to JSON
    output_path = Path(__file__).resolve().parents[1] / "checkpoints" / f"telemetry_audit_{args.target}.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"\nAudit saved to {output_path}")
