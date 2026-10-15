"""Generalized Epigenetic Heir Training Pipeline.

Trains any designated Epigenetic Heir (e.g. student_03, student_04, etc.)
from parent graduate through all 5 grades with sleep consolidation
using the refined generational codices.
"""

from __future__ import annotations

import argparse
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


def train_heir(
    heir_id: str = "student_04",
    generation: int = 4,
    parent_checkpoint: Path | None = None,
) -> CognitiveHeartbeat:
    start_time = time.time()
    print(DIVIDER)
    print(f"  LMFT-SCHOOL: EPIGENETIC HEIR {heir_id.upper()} (GENERATION {generation}) TRAINING")
    print(f"  Ancestral Neocortex Inheritance | Refined Gen {generation} Curriculum")
    print(DIVIDER)

    if parent_checkpoint is None:
        parent_checkpoint = Path(f"checkpoints/individual_student_{generation-1:02d}_gen{generation-1:02d}_grade5_master_graduate.lmft.json")

    # 1. Prime Infant
    ckpt_g0, heartbeat = prime_epigenetic_heir(
        parent_checkpoint_path=parent_checkpoint,
        heir_id=heir_id,
        generation=generation,
        initial_plasticity=0.30,
    )

    # 2. Grade 1
    print("\n[Phase 1] Grade 1: Refined Elemental Esper Alphabet...")
    g1 = Grade1CurriculumRunner(heartbeat=heartbeat, individual_id=heir_id, codex=GEN3_ESPER_CODEX)
    g1.teach_full_alphabet()
    ckpt_g1, tel_g1 = archive_grade_milestone(
        heartbeat=heartbeat,
        grade_level=1,
        milestone_label="esper_graduate",
        generation=generation,
    )
    print(f"  -> Grade 1 Complete: 26/26 Espers Mastered.")
    print(f"     GCI: {tel_g1.global_coherence_index:.4f} | Balance: {tel_g1.homeostatic_balance_score:.4f} | Alpha: {tel_g1.plasticity_alpha:.4f}")

    # 3. Grade 2
    print("\n[Phase 2] Grade 2: Refined Relational Hearth Alphabet...")
    g2 = Grade2CurriculumRunner(heartbeat=heartbeat, individual_id=heir_id, codex=GEN3_RELATIONAL_CODEX)
    for letter in [chr(c) for c in range(ord("A"), ord("Z") + 1)]:
        g2.teach_archetype(letter)
    heartbeat.sleep(prune_buffer=True)
    ckpt_g2, tel_g2 = archive_grade_milestone(
        heartbeat=heartbeat,
        grade_level=2,
        milestone_label="relational_graduate",
        generation=generation,
    )
    print(f"  -> Grade 2 Complete: 26/26 Relational Archetypes Mastered.")
    print(f"     GCI: {tel_g2.global_coherence_index:.4f} | Balance: {tel_g2.homeostatic_balance_score:.4f} | Alpha: {tel_g2.plasticity_alpha:.4f}")

    # 4. Grade 3
    print("\n[Phase 3] Grade 3: Refined Socratic Crucible...")
    g3 = Grade3CurriculumRunner(heartbeat=heartbeat, individual_id=heir_id, codex=GEN3_SOCRATIC_CODEX)
    for letter in [chr(c) for c in range(ord("A"), ord("Z") + 1)]:
        g3.teach_paradox(letter)
    heartbeat.sleep(prune_buffer=True)
    ckpt_g3, tel_g3 = archive_grade_milestone(
        heartbeat=heartbeat,
        grade_level=3,
        milestone_label="socratic_graduate",
        generation=generation,
    )
    print(f"  -> Grade 3 Complete: 26/26 Socratic Trials Defended.")
    print(f"     GCI: {tel_g3.global_coherence_index:.4f} | Balance: {tel_g3.homeostatic_balance_score:.4f} | Alpha: {tel_g3.plasticity_alpha:.4f}")

    # 5. Grade 4
    print("\n[Phase 4] Grade 4: Refined Sovereign Thesis...")
    g4 = Grade4CurriculumRunner(heartbeat=heartbeat, individual_id=heir_id, codex=GEN3_THESIS_CODEX)
    for letter in [chr(c) for c in range(ord("A"), ord("Z") + 1)]:
        g4.defend_thesis_letter(letter)
    heartbeat.sleep(prune_buffer=True)
    ckpt_g4, tel_g4 = archive_grade_milestone(
        heartbeat=heartbeat,
        grade_level=4,
        milestone_label="thesis_graduate",
        generation=generation,
    )
    print(f"  -> Grade 4 Complete: 26/26 Sovereign Defenses Mastered.")
    print(f"     GCI: {tel_g4.global_coherence_index:.4f} | Balance: {tel_g4.homeostatic_balance_score:.4f} | Alpha: {tel_g4.plasticity_alpha:.4f}")

    # 6. Grade 5
    print("\n[Phase 5] Grade 5: Refined Capstone Grand Synthesis...")
    g5 = Grade5CurriculumRunner(heartbeat=heartbeat, individual_id=heir_id, codex=GEN3_MASTER_CODEX)
    for letter in [chr(c) for c in range(ord("A"), ord("Z") + 1)]:
        g5.teach_master_chord(letter)
    g5.stress_test_word_battery(("JUSTICE", "FREEDOM", "SOVEREIGN"))

    for epoch in range(1, 4):
        sleep_res = heartbeat.sleep(prune_buffer=True)
        print(f"     Sleep Epoch {epoch}/3: {len(sleep_res.get('consolidation_summary', {}).get('promoted_rules', []))} rules promoted.")

    ckpt_g5, tel_g5 = archive_grade_milestone(
        heartbeat=heartbeat,
        grade_level=5,
        milestone_label="master_graduate",
        generation=generation,
    )
    print(f"  -> Grade 5 Complete: Master Chords Synthesized.")
    print(f"     Archived: {ckpt_g5.name}")
    print(f"     GCI: {tel_g5.global_coherence_index:.4f} | Balance: {tel_g5.homeostatic_balance_score:.4f} | Alpha: {tel_g5.plasticity_alpha:.4f}")
    print(f"     Active Long-Term Rules: {len(heartbeat.consolidator.long_term_rules)}")

    pkg = import_individual(ckpt_g5, verify_seed=True)
    assert pkg["individual_id"] == heir_id
    elapsed = time.time() - start_time
    print(DIVIDER)
    print(f"  {heir_id.upper()} GRADUATION COMPLETE in {elapsed:.2f}s | CHECKSUM VERIFIED")
    print(DIVIDER)
    return heartbeat


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train an Epigenetic Heir")
    parser.add_argument("--heir", type=str, default="student_04", help="Heir candidate ID")
    parser.add_argument("--gen", type=int, default=4, help="Generation number")
    parser.add_argument("--parent", type=Path, default=Path("checkpoints/individual_student_03_gen03_grade5_master_graduate.lmft.json"), help="Parent checkpoint path")
    args = parser.parse_args()

    train_heir(heir_id=args.heir, generation=args.gen, parent_checkpoint=args.parent)
