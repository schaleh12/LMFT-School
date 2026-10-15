"""Execution runner for Grade 4 Undergraduate Thesis Defense graduation of student_01."""
import sys
from pathlib import Path

# Ensure src is on path
src_dir = Path(__file__).resolve().parents[1] / "src"
if str(src_dir) not in sys.path:
    sys.path.insert(0, str(src_dir))

from lmft_school.curriculum_grade_4 import Grade4CurriculumRunner


def main():
    print("=" * 70)
    print("Enrolling student_01 into Grade 4: Undergraduate Thesis Defense...")
    print("=" * 70)

    runner = Grade4CurriculumRunner(
        individual_id="student_01",
        load_grade3_checkpoint=True,
    )

    print(f"Loaded student_01 prior cycle: {runner.heartbeat.cycle}")
    print("Defending 26 Sovereign Thesis Principles (A to Z) against the 8B Kefka-Mind...")

    report = runner.defend_full_thesis(archive_checkpoint=True)

    print("\n" + "=" * 70)
    print("GRADUATION SUMMARY:")
    print("=" * 70)
    print(report.summary_verdict)
    print(f"Checkpoint archived: {report.checkpoint_path}")
    print(f"Final state digest:  {report.final_state_digest}")
    print(f"Defenses completed:  {report.defenses_completed}")
    print(f"Post-Grade 4 cycle:   {runner.heartbeat.cycle}")
    print("=" * 70)


if __name__ == "__main__":
    main()
