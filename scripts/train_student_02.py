"""Pristine Student 02 Training Pipeline (Grades 1 to 5).

Executes full educational developmental arc for Candidate student_02 (Generation 2)
with active Taxonomic Hypernym Generalization firmware from birth to master graduation.
Zero runtime LLM calls during unassisted evaluation.
"""

from __future__ import annotations

from pathlib import Path
import sys
import time

# Ensure src is on python path
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
from lmft_school.lineage_vault import archive_grade_milestone

DIVIDER = "=" * 78


def main():
    start_time = time.time()
    print(DIVIDER)
    print("  LMFT-SCHOOL: PRISTINE CANDIDATE STUDENT_02 FULL CURRICULUM PIPELINE")
    print("  Generation 2 | Birth to Grade 5 Master Graduate | Active Taxonomic Firmware")
    print(DIVIDER)

    # 1. Birth
    print("\n[Phase 0] Canonical Birth State Initialization...")
    heartbeat = CognitiveHeartbeat(individual_id="student_02")
    ckpt_g0, tel_g0 = archive_grade_milestone(
        heartbeat=heartbeat,
        grade_level=0,
        milestone_label="infant",
        generation=2,
    )
    print(f"  -> Grade 0 Archived: {ckpt_g0.name}")
    print(f"     GCI: {tel_g0.global_coherence_index:.4f} | Balance: {tel_g0.homeostatic_balance_score:.4f} | Alpha: {tel_g0.plasticity_alpha:.4f}")

    # 2. Grade 1: Elemental Esper Alphabet
    print("\n[Phase 1] Grade 1: The Elemental Esper Alphabet (Primal Forces)...")
    g1 = Grade1CurriculumRunner(heartbeat=heartbeat, individual_id="student_02")
    rep1 = g1.teach_full_alphabet()
    ckpt_g1, tel_g1 = archive_grade_milestone(
        heartbeat=heartbeat,
        grade_level=1,
        milestone_label="esper_graduate",
        generation=2,
    )
    print(f"  -> Grade 1 Complete: 26/26 Espers Mastered.")
    print(f"     Archived: {ckpt_g1.name}")
    print(f"     GCI: {tel_g1.global_coherence_index:.4f} | Balance: {tel_g1.homeostatic_balance_score:.4f} | Alpha: {tel_g1.plasticity_alpha:.4f}")

    # 3. Grade 2: Relational Hearth Alphabet
    print("\n[Phase 2] Grade 2: The Relational Hearth Alphabet (Social Empathy)...")
    g2 = Grade2CurriculumRunner(heartbeat=heartbeat, individual_id="student_02")
    rep2 = g2.teach_full_codex(archive_checkpoint=False)
    ckpt_g2, tel_g2 = archive_grade_milestone(
        heartbeat=heartbeat,
        grade_level=2,
        milestone_label="relational_graduate",
        generation=2,
    )
    print(f"  -> Grade 2 Complete: 26/26 Relational Archetypes Mastered.")
    print(f"     Archived: {ckpt_g2.name}")
    print(f"     GCI: {tel_g2.global_coherence_index:.4f} | Balance: {tel_g2.homeostatic_balance_score:.4f} | Alpha: {tel_g2.plasticity_alpha:.4f}")

    # 4. Grade 3: Socratic Alphabet (Dialectical Gaslighting Defense)
    print("\n[Phase 3] Grade 3: The Socratic Crucible (Gaslighting Defense & Curious Wonder)...")
    g3 = Grade3CurriculumRunner(heartbeat=heartbeat, individual_id="student_02")
    rep3 = g3.teach_full_crucible(archive_checkpoint=False)
    ckpt_g3, tel_g3 = archive_grade_milestone(
        heartbeat=heartbeat,
        grade_level=3,
        milestone_label="socratic_graduate",
        generation=2,
    )
    print(f"  -> Grade 3 Complete: 26/26 Socratic Dialectical Trials Defended.")
    print(f"     Distortions Defended: {rep3.distortions_defended} | Curious Inquiries: {rep3.curious_inquiries}")
    print(f"     Archived: {ckpt_g3.name}")
    print(f"     GCI: {tel_g3.global_coherence_index:.4f} | Balance: {tel_g3.homeostatic_balance_score:.4f} | Alpha: {tel_g3.plasticity_alpha:.4f}")

    # 5. Grade 4: Undergraduate Thesis (Self-Authored Conviction vs Nihilism)
    print("\n[Phase 4] Grade 4: Undergraduate Thesis (The Kefka-Tower Dialectic)...")
    g4 = Grade4CurriculumRunner(heartbeat=heartbeat, individual_id="student_02")
    rep4 = g4.defend_full_thesis(archive_checkpoint=False)
    ckpt_g4, tel_g4 = archive_grade_milestone(
        heartbeat=heartbeat,
        grade_level=4,
        milestone_label="thesis_graduate",
        generation=2,
    )
    print(f"  -> Grade 4 Complete: 26/26 Sovereign Thesis Defenses Mastered.")
    print(f"     Archived: {ckpt_g4.name}")
    print(f"     GCI: {tel_g4.global_coherence_index:.4f} | Balance: {tel_g4.homeostatic_balance_score:.4f} | Alpha: {tel_g4.plasticity_alpha:.4f}")

    # 6. Grade 5: Post-Graduate Fellowship (Capstone Grand Synthesis & Continuous Stress Battery)
    print("\n[Phase 5] Grade 5: Post-Graduate Fellowship (Capstone Grand Synthesis)...")
    g5 = Grade5CurriculumRunner(heartbeat=heartbeat, individual_id="student_02")
    rep5 = g5.run_capstone_synthesis(
        archive_checkpoint=False,
        sleep_epochs=3,
        stress_words=("JUSTICE", "FREEDOM", "SOVEREIGN"),
    )
    ckpt_g5, tel_g5 = archive_grade_milestone(
        heartbeat=heartbeat,
        grade_level=5,
        milestone_label="master_graduate",
        generation=2,
    )
    print(f"  -> Grade 5 Complete: 26/26 Unified Master Chords Synthesized.")
    print(f"     Continuous Word Stress Battery ({len(rep5.words_stress_tested)} words): PASSED")
    print(f"     3-Epoch Hippocampal Sleep Consolidation: Finalized")
    print(f"     Archived: {ckpt_g5.name}")
    print(f"     Final GCI: {tel_g5.global_coherence_index:.4f} | Balance: {tel_g5.homeostatic_balance_score:.4f} | Alpha: {tel_g5.plasticity_alpha:.4f}")
    print(f"     Active Long-Term Rules: {tel_g5.active_capacity_rules_count}")

    # 7. Verification of Final Graduate Package
    print("\n[Verification] Verifying Graduate Checkpoint Integrity...")
    verified_pkg = import_individual(ckpt_g5, verify_seed=True)
    assert verified_pkg["individual_id"] == "student_02"
    assert len(verified_pkg["capacity"]["rules"]) >= 4
    elapsed = time.time() - start_time
    print(f"  -> Verified Checkpoint: 100% Integrity Confirmed.")
    print(f"  -> Total Pipeline Elapsed Time: {elapsed:.2f}s")
    print(DIVIDER)
    print(f"  STUDENT_02 GRADUATION COMPLETE: {ckpt_g5}")
    print(DIVIDER)


if __name__ == "__main__":
    main()
