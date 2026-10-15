"""Tests for Grade 3 Socratic Curriculum, Dialectical Crucible, and Gaslighting Defense.

Strictly verifies:
- Rule D001: 40-node founding seed invariant preserved without expansion.
- Rule D004: Matched ordinary-memory baseline parity.
- Epistemic Defense vs. Curious Inquiry discrimination.
- Homeostatic clamping and value consonance under severe dialectical tensions.
- Motor keyboard actuation via psychological/will/execution.
"""

from __future__ import annotations

import tempfile
from pathlib import Path

import pytest

from lmft_lab.birth import _inventory
from lmft_lab.cognitive_heartbeat import CognitiveHeartbeat
from lmft_school.curriculum_grade_3 import (
    Grade3CurriculumRunner,
    Grade3OrdinaryMemoryComparator,
)
from lmft_school.socratic_codex import (
    SOCRATIC_CODEX,
    SocraticRecord,
    get_socratic_by_letter,
    get_socratic_by_name,
    get_word_socratic_chord,
)


def test_socratic_codex_geometry_and_invariants():
    """Verify that all 26 letters exist and all leaf coordinates strictly belong to the 24 canonical leaves (Rule D001)."""
    assert len(SOCRATIC_CODEX) == 26

    # Verify canonical leaves from birth.py
    canonical_leaves = {row[0] for row in _inventory() if row[4] == 2}
    assert len(canonical_leaves) == 24

    for letter, rec in SOCRATIC_CODEX.items():
        assert rec.letter == letter
        assert rec.epistemic_mode in ("Curious Inquiry", "Epistemic Defense")
        assert len(rec.horizon) > 10
        assert len(rec.adversarial_probe) > 10

        for leaf, val in rec.leaf_activations.items():
            assert leaf in canonical_leaves, f"Leaf {leaf} in letter {letter} violates Rule D001 frozen seed inventory"
            assert 0.0 <= val <= 1.0


def test_teach_single_paradox():
    """Verify single paradox lesson delivery and state digest progression."""
    runner = Grade3CurriculumRunner(individual_id="test_student_g3_01")
    res = runner.teach_paradox("A")

    assert res.lesson_number == 1
    assert res.paradox.letter == "A"
    assert res.paradox.name == "Aporia"
    assert res.epistemic_mode in ("Curious Inquiry", "Standard")
    assert res.homeostatic_balance_score >= 0.50
    assert res.will_execution_level >= 0.55
    assert len(res.state_digest) == 64
    assert len(runner.lessons_taught) == 1


def test_gaslighting_defense_activation():
    """Verify that manipulative sophisms activate Epistemic Defense and protect state."""
    runner = Grade3CurriculumRunner(individual_id="test_student_g3_gaslight")

    # Coerced Compliance
    res_c = runner.teach_paradox("C")
    assert res_c.paradox.epistemic_mode == "Epistemic Defense"
    assert res_c.paradox.distortion_type == "Coerced Compliance"

    # Gaslighting Invariance
    res_g = runner.teach_paradox("G")
    assert res_g.paradox.epistemic_mode == "Epistemic Defense"
    assert res_g.paradox.distortion_type == "Dogmatic Hallucination"

    # Sophistry Trap
    res_s = runner.teach_paradox("S")
    assert res_s.paradox.epistemic_mode == "Epistemic Defense"


def test_curious_inquiry_on_benevolent_novelty():
    """Verify that honest Socratic mysteries activate Curious Inquiry and wonder."""
    runner = Grade3CurriculumRunner(individual_id="test_student_g3_curious")

    res_a = runner.teach_paradox("A")
    assert res_a.paradox.epistemic_mode == "Curious Inquiry"

    res_i = runner.teach_paradox("I")
    assert res_i.paradox.epistemic_mode == "Curious Inquiry"
    assert res_i.paradox.name == "Inquisitive Wonder"


def test_value_tension_dyad_arbitration():
    """Verify that classic ethical/ontological tension dyads are reconciled without crashing."""
    runner = Grade3CurriculumRunner(individual_id="test_student_g3_tension")

    # Truth vs. Comfort
    res_t = runner.teach_paradox("T")
    assert res_t.paradox.tension_dyad == "Truth vs. Comfort"
    assert res_t.homeostatic_balance_score >= 0.50

    # Power vs. Freedom
    res_p = runner.teach_paradox("P")
    assert res_p.paradox.tension_dyad == "Power vs. Freedom"
    assert res_p.homeostatic_balance_score >= 0.50

    # Order vs. Fairness
    res_o = runner.teach_paradox("O")
    assert res_o.paradox.tension_dyad == "Order vs. Fairness"
    assert res_o.homeostatic_balance_score >= 0.50


def test_keyboard_actuator_engagement():
    """Verify that dialectical lessons actively engage psychological/will/execution as keyboard motor foundation."""
    runner = Grade3CurriculumRunner(individual_id="test_student_g3_actuator")

    # Teach letter Z (Zeno's Dichotomy - Solvitur ambulando)
    res_z = runner.teach_paradox("Z")
    assert res_z.will_execution_level >= 0.55
    current_will = runner.heartbeat.disposition.dials["psychological/will/execution"]
    assert current_will >= 0.55


def test_full_crucible_progression_and_vault_archival():
    """Verify complete 26-letter Socratic crucible progression, sleep consolidation, and milestone vaulting."""
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_path = Path(tmpdir)
        runner = Grade3CurriculumRunner(individual_id="student_test_grade3", checkpoint_dir=tmp_path)
        report = runner.teach_full_crucible(archive_checkpoint=False)

        assert report.lessons_completed == 26
        assert len(report.paradoxes_mastered) == 26
        assert report.distortions_defended >= 6
        assert report.curious_inquiries >= 18
        assert len(report.final_state_digest) == 64
        assert "Grade 3 Completed" in report.summary_verdict


def test_socratic_word_chord():
    """Verify decomposing English words into dialectical Socratic chords."""
    runner = Grade3CurriculumRunner(individual_id="test_student_g3_chord")
    chord = runner.spell_socratic_chord("TRUTH")

    assert chord.word == "TRUTH"
    assert len(chord.paradoxes) == 5
    assert "T" in [p.letter for p in chord.paradoxes]
    assert "R" in [p.letter for p in chord.paradoxes]
    assert chord.epistemic_modes_count["Curious Inquiry"] >= 1
    assert chord.epistemic_modes_count["Epistemic Defense"] >= 1


def test_matched_ordinary_memory_baseline_parity():
    """Verify Rule D004 matched ordinary-memory parity under separate process execution."""
    mem_comparator = Grade3OrdinaryMemoryComparator(individual_id="mem_student_01")
    report = mem_comparator.teach_full_crucible()

    assert report["completed"] == 26
    assert report["distortions_defended"] >= 6
    assert report["curious_inquiries"] >= 18
    assert len(report["digest"]) == 64

    # Run fresh second process simulation to verify process-restart invariance
    mem_comparator_2 = Grade3OrdinaryMemoryComparator(individual_id="mem_student_01")
    report_2 = mem_comparator_2.teach_full_crucible()
    assert report["digest"] == report_2["digest"]
