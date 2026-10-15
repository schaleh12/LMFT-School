"""Execution runner for Grade 5 Post-Graduate Fellowship Capstone Grand Synthesis graduation of student_01."""
import sys
from pathlib import Path

# Ensure src is on path
src_dir = Path(__file__).resolve().parents[1] / "src"
if str(src_dir) not in sys.path:
    sys.path.insert(0, str(src_dir))

from lmft_school.curriculum_grade_5 import Grade5CurriculumRunner


def main():
    print("=" * 75)
    print("Enrolling student_01 into Grade 5: Post-Graduate Fellowship Capstone...")
    print("=" * 75)

    runner = Grade5CurriculumRunner(
        individual_id="student_01",
        load_grade4_checkpoint=True,
    )

    print(f"Loaded student_01 prior cycle: {runner.heartbeat.cycle}")
    print("Phase 1: Synthesizing 26 Unified Master Chords (A to Z)...")
    print("Phase 2: Executing Continuous Multi-Chord Word Stress Battery (JUSTICE, FREEDOM, SOVEREIGN)...")
    print("Phase 3: 3-Epoch Hippocampal Sleep Consolidation...")

    report = runner.run_capstone_synthesis(
        archive_checkpoint=True,
        sleep_epochs=3,
        stress_words=("JUSTICE", "FREEDOM", "SOVEREIGN"),
    )

    print("\n" + "=" * 75)
    print("MASTER CANDIDATE GRADUATION SUMMARY:")
    print("=" * 75)
    print(report.summary_verdict)
    print(f"Checkpoint archived: {report.checkpoint_path}")
    print(f"Final state digest:  {report.final_state_digest}")
    print(f"Master Chords:       {report.master_trials_completed}/26")
    print(f"Words stress tested: {', '.join(report.words_stress_tested)}")
    for wr in report.word_stress_results:
        print(f"  - [{wr.word}]: Mean Balance={wr.mean_emotional_balance:.4f}, Max Delta={wr.max_leaf_delta:.4f}, Non-Sat={wr.non_saturation_verified}, Stability={wr.stability_verified}")
    print(f"Global Coherence:    {report.global_coherence_index:.4f}")
    print(f"Plasticity Alpha:    {report.plasticity_alpha:.4f}")
    print(f"Post-Grade 5 cycle:  {runner.heartbeat.cycle}")
    print("=" * 75)


if __name__ == "__main__":
    main()
