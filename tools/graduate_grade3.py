"""Execution runner for Grade 3 Socratic Crucible graduation of student_01."""
import sys
from pathlib import Path

# Ensure src is on path
src_dir = Path(__file__).resolve().parents[1] / "src"
if str(src_dir) not in sys.path:
    sys.path.insert(0, str(src_dir))

from lmft_school.curriculum_grade_3 import Grade3CurriculumRunner

def main():
    print("=" * 70)
    print("Enrolling student_01 into Grade 3: The Socratic Alphabet Crucible...")
    print("=" * 70)
    
    runner = Grade3CurriculumRunner(
        individual_id="student_01",
        load_grade2_checkpoint=True,
    )
    
    print(f"Loaded student_01 prior cycle: {runner.heartbeat.cycle}")
    print("Delivering 26 Socratic dialectical paradoxes (A to Z)...")
    
    report = runner.teach_full_crucible(archive_checkpoint=True)
    
    print("\n" + "=" * 70)
    print("GRADUATION SUMMARY:")
    print("=" * 70)
    print(report.summary_verdict)
    print(f"Checkpoint archived: {report.checkpoint_path}")
    print(f"Final state digest:  {report.final_state_digest}")
    print(f"Distortions defended: {report.distortions_defended}")
    print(f"Curious inquiries:    {report.curious_inquiries}")
    print(f"Post-Grade 3 cycle:   {runner.heartbeat.cycle}")
    print("=" * 70)

if __name__ == "__main__":
    main()
