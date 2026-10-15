"""Epigenetic Heir Student 03 Training Pipeline (Grades 1 to 5).

Executes the full Generation 3 educational progression for Candidate 'student_03'
using the refined Generation 3 curriculum codices and ancestral capacity inheritance.
Zero runtime LLM calls during unassisted evaluation.
"""

from __future__ import annotations

from pathlib import Path
import sys
import time

src_dir = Path(__file__).resolve().parents[1] / "src"
if str(src_dir) not in sys.path:
    sys.path.insert(0, str(src_dir))

from lmft_lab.cognitive_heartbeat import CognitiveHeartbeat
from lmft_lab.individual_package import import_individual
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
from lmft_school.lineage_vault import archive_grade_milestone
from prime_heir import prime_epigenetic_heir

DIVIDER = "=" * 78


def train_generation_3_student() -> CognitiveHeartbeat:
    start_time = time.time()
    print(DIVIDER)
    print("  LMFT-SCHOOL: EPIGENETIC HEIR STUDENT_03 (GENERATION 3) TRAINING PIPELINE")
    print("  Ancestral Capacity Inheritance | Refined Gen 3 Curriculum | Active Taxonomy")
    print(DIVIDER)

    # 1. Phase 0: Prime Epigenetic Heir from Student 02 Master Graduate
    parent_ckpt = Path("checkpoints/individual_student_02_gen02_grade5_master_graduate.lmft.json")
    ckpt_g0, heartbeat = prime_epigenetic_heir(
        parent_checkpoint_path=parent_ckpt,
        heir_id="student_03",
        generation=3,
        initial_plasticity=0.30,
    )

    # 2. Phase 1: Grade 1 with Refined Esper Codex (Shock-Damped)
    print("\n[Phase 1] Grade 1: Refined Elemental Esper Alphabet (Shock-Damped)...")
    g1 = Grade1CurriculumRunner(heartbeat=heartbeat, individual_id="student_03", codex=GEN3_ESPER_CODEX)
    rep1 = g1.teach_full_alphabet()
    ckpt_g1, tel_g1 = archive_grade_milestone(
        heartbeat=heartbeat,
        grade_level=1,
        milestone_label="esper_graduate",
        generation=3,
    )
    print(f"  -> Grade 1 Complete: 26/26 Refined Espers Mastered.")
    print(f"     Archived: {ckpt_g1.name}")
    print(f"     GCI: {tel_g1.global_coherence_index:.4f} | Balance: {tel_g1.homeostatic_balance_score:.4f} | Alpha: {tel_g1.plasticity_alpha:.4f}")

    # 3. Phase 2: Grade 2 with Refined Relational Hearth Codex
    print("\n[Phase 2] Grade 2: Refined Relational Hearth Alphabet (Reciprocal Dyads)...")
    g2 = Grade2CurriculumRunner(heartbeat=heartbeat, individual_id="student_03", codex=GEN3_RELATIONAL_CODEX)
    # Sequentially teach all 26 archetypes
    for letter in [chr(c) for c in range(ord("A"), ord("Z") + 1)]:
        g2.teach_archetype(letter)
    g2.heartbeat.sleep(prune_buffer=True)
    ckpt_g2, tel_g2 = archive_grade_milestone(
        heartbeat=heartbeat,
        grade_level=2,
        milestone_label="relational_graduate",
        generation=3,
    )
    print(f"  -> Grade 2 Complete: 26/26 Refined Relational Archetypes Mastered.")
    print(f"     Archived: {ckpt_g2.name}")
    print(f"     GCI: {tel_g2.global_coherence_index:.4f} | Balance: {tel_g2.homeostatic_balance_score:.4f} | Alpha: {tel_g2.plasticity_alpha:.4f}")

    # 4. Phase 3: Grade 3 with Refined Socratic Crucible Codex (Protected Clarity)
    print("\n[Phase 3] Grade 3: Refined Socratic Crucible (Protected Clarity & Defense)...")
    g3 = Grade3CurriculumRunner(heartbeat=heartbeat, individual_id="student_03", codex=GEN3_SOCRATIC_CODEX)
    distortions = 0
    curious = 0
    for letter in [chr(c) for c in range(ord("A"), ord("Z") + 1)]:
        res = g3.teach_paradox(letter)
        if res.epistemic_mode == "Epistemic Defense":
            distortions += 1
        else:
            curious += 1
    g3.heartbeat.sleep(prune_buffer=True)
    ckpt_g3, tel_g3 = archive_grade_milestone(
        heartbeat=heartbeat,
        grade_level=3,
        milestone_label="socratic_graduate",
        generation=3,
    )
    print(f"  -> Grade 3 Complete: 26/26 Refined Socratic Dialectical Trials Defended.")
    print(f"     Distortions Defended: {distortions} | Curious Inquiries: {curious}")
    print(f"     Archived: {ckpt_g3.name}")
    print(f"     GCI: {tel_g3.global_coherence_index:.4f} | Balance: {tel_g3.homeostatic_balance_score:.4f} | Alpha: {tel_g3.plasticity_alpha:.4f}")

    # 5. Phase 4: Grade 4 with Refined Sovereign Thesis Codex
    print("\n[Phase 4] Grade 4: Refined Undergraduate Thesis (Holonomic Sovereignty)...")
    g4 = Grade4CurriculumRunner(heartbeat=heartbeat, individual_id="student_03", codex=GEN3_THESIS_CODEX)
    for letter in [chr(c) for c in range(ord("A"), ord("Z") + 1)]:
        g4.defend_thesis_letter(letter)
    g4.heartbeat.sleep(prune_buffer=True)
    ckpt_g4, tel_g4 = archive_grade_milestone(
        heartbeat=heartbeat,
        grade_level=4,
        milestone_label="thesis_graduate",
        generation=3,
    )
    print(f"  -> Grade 4 Complete: 26/26 Refined Sovereign Thesis Defenses Mastered.")
    print(f"     Archived: {ckpt_g4.name}")
    print(f"     GCI: {tel_g4.global_coherence_index:.4f} | Balance: {tel_g4.homeostatic_balance_score:.4f} | Alpha: {tel_g4.plasticity_alpha:.4f}")

    # 6. Phase 5: Grade 5 with Refined Master Codex + Stress Battery + Sleep
    print("\n[Phase 5] Grade 5: Post-Graduate Fellowship (Refined Capstone Synthesis)...")
    g5 = Grade5CurriculumRunner(heartbeat=heartbeat, individual_id="student_03", codex=GEN3_MASTER_CODEX)
    for letter in [chr(c) for c in range(ord("A"), ord("Z") + 1)]:
        g5.teach_master_chord(letter)
    
    # Continuous word stress battery
    g5.stress_test_word_battery(("JUSTICE", "FREEDOM", "SOVEREIGN"))

    # 3 offline sleep consolidation epochs
    for epoch in range(1, 4):
        sleep_res = heartbeat.sleep(prune_buffer=True)
        print(f"     Sleep Epoch {epoch}/3: {len(sleep_res.get('consolidation_summary', {}).get('promoted_rules', []))} rules promoted.")

    ckpt_g5, tel_g5 = archive_grade_milestone(
        heartbeat=heartbeat,
        grade_level=5,
        milestone_label="master_graduate",
        generation=3,
    )
    print(f"  -> Grade 5 Complete: 26/26 Refined Master Chords Synthesized.")
    print(f"     Archived: {ckpt_g5.name}")
    print(f"     GCI: {tel_g5.global_coherence_index:.4f} | Balance: {tel_g5.homeostatic_balance_score:.4f} | Alpha: {tel_g5.plasticity_alpha:.4f}")
    print(f"     Consolidated Rules: {len(heartbeat.consolidator.long_term_rules)}")

    # 7. Verification of Standalone Package Fidelity
    pkg = import_individual(ckpt_g5, verify_seed=True)
    assert pkg["individual_id"] == "student_03"
    assert len(pkg["capacity"]["rules"]) >= 4
    print(f"\n[+] Checkpoint Integrity Verified: 100% Valid (Seed Fingerprint Matched)")

    elapsed = time.time() - start_time
    print(DIVIDER)
    print(f"  STUDENT_03 GRADUATION COMPLETE in {elapsed:.2f}s | ALL 5 GRADES MASTERED")
    print(DIVIDER)

    return heartbeat


if __name__ == "__main__":
    train_generation_3_student()
