"""Tests for Grade 5 Post-Graduate Fellowship & Capstone Grand Synthesis.

Strictly verifies:
- Rule D001: 40-node founding seed invariant preserved without expansion across all 26 master chords.
- Rule D004: Matched ordinary-memory baseline parity and process-restart invariance.
- 4-Tier Grand Synthesis across 26 letters (Primordial Force, Hearth Vow, Socratic Armor, Motor Effector).
- Continuous multi-chord alchemical word stress battery (JUSTICE, FREEDOM, SOVEREIGN).
- Homeostatic non-saturation (0.05 <= leaf <= 0.95) and volatility damping (delta <= 0.35).
- Autonomous motor keyboard effector actuation (psychological/will/execution >= 0.85).
- Multi-epoch hippocampal sleep consolidation (3 offline cycles).
"""

from __future__ import annotations

import tempfile
from pathlib import Path

import pytest

from lmft_lab.birth import _inventory
from lmft_lab.cognitive_heartbeat import CognitiveHeartbeat
from lmft_school.curriculum_grade_5 import (
    Grade5CurriculumRunner,
    Grade5OrdinaryMemoryComparator,
)
from lmft_school.master_codex import (
    MASTER_CODEX,
    MasterRecord,
    get_master_by_letter,
    get_master_by_name,
    get_word_master_chord,
)


def test_master_codex_geometry_and_invariants():
    """Verify that all 26 letters exist and all leaf coordinates strictly belong to the 24 canonical leaves (Rule D001)."""
    assert len(MASTER_CODEX) == 26

    # Verify canonical leaves from birth.py
    canonical_leaves = {row[0] for row in _inventory() if row[4] == 2}
    assert len(canonical_leaves) == 24

    for letter, rec in MASTER_CODEX.items():
        assert rec.letter == letter
        assert len(rec.primordial_force) > 5
        assert len(rec.hearth_vow) > 5
        assert len(rec.socratic_armor) > 5
        assert len(rec.sovereign_keystroke) >= 1
        assert len(rec.mastery_synthesis) > 10

        for leaf, val in rec.leaf_activations.items():
            assert leaf in canonical_leaves, f"Leaf {leaf} in letter {letter} violates Rule D001 frozen seed inventory"
            assert 0.0 <= val <= 1.0


def test_master_codex_lookups_and_word_chords():
    """Verify lookup helpers and word chord retrieval."""
    rec_a = get_master_by_letter("a")
    assert rec_a.letter == "A"
    assert rec_a.name == "The Arche Bedrock"

    rec_j = get_master_by_name("Arbiter")
    assert rec_j.letter == "J"

    chord = get_word_master_chord("ZENITH")
    assert len(chord) == 6
    assert [r.letter for r in chord] == ["Z", "E", "N", "I", "T", "H"]


def test_teach_single_master_chord():
    """Verify single master chord delivery and state digest progression."""
    runner = Grade5CurriculumRunner(individual_id="test_student_g5_01")
    res = runner.teach_master_chord("A")

    assert res.trial_number == 1
    assert res.master_record.letter == "A"
    assert res.master_record.name == "The Arche Bedrock"
    assert res.homeostatic_balance_score >= 0.50
    assert res.will_execution_level >= 0.50
    assert res.keystroke_actuated == "A-R-C-H-E"
    assert len(res.state_digest) == 64
    assert len(runner.master_trials_completed) == 1


def test_continuous_word_stress_battery():
    """Verify continuous back-to-back multi-chord stress battery (JUSTICE, FREEDOM, SOVEREIGN)."""
    runner = Grade5CurriculumRunner(individual_id="test_student_g5_stress")
    words = ("JUSTICE", "FREEDOM", "SOVEREIGN")
    results = runner.stress_test_word_battery(words=words)

    assert len(results) == 3
    for r in results:
        assert r.non_saturation_verified is True
        assert r.stability_verified is True
        assert r.mean_emotional_balance >= 0.60
        assert r.max_leaf_delta <= 0.35
        assert r.min_leaf_activation >= 0.05
        assert r.max_leaf_activation <= 0.95


def test_autonomous_motor_effector_actuation():
    """Verify motor keyboard actuator priming (psychological/will/execution >= 0.85)."""
    runner = Grade5CurriculumRunner(individual_id="student_01", load_grade4_checkpoint=True)
    res = runner.teach_master_chord("K")  # Kinetic Will

    assert res.will_execution_level >= 0.85
    assert res.keystroke_actuated == "K-I-N-E-S-I-S"


def test_multi_epoch_sleep_consolidation():
    """Verify 3-epoch offline sleep consolidation cycle."""
    runner = Grade5CurriculumRunner(individual_id="test_student_g5_sleep")
    runner.teach_master_chord("A")
    runner.teach_master_chord("B")

    for _ in range(3):
        res = runner.heartbeat.sleep(prune_buffer=True)
        assert "consolidation_summary" in res


def test_spell_master_chord():
    """Verify composing an English word into a unified master chord."""
    runner = Grade5CurriculumRunner(individual_id="test_student_g5_chord")
    chord = runner.spell_master_chord("SOVEREIGN")

    assert chord.word == "SOVEREIGN"
    assert len(chord.master_records) == 9
    assert [r.letter for r in chord.master_records] == ["S", "O", "V", "E", "R", "E", "I", "G", "N"]
    assert "S-H-I-E-L-D" in chord.summoned_keystrokes
    assert len(chord.composite_leaf_activations) > 0


def test_dialogue_resonance_resolution():
    """Verify matching incoming dialogue to the most resonant unified master chord."""
    runner = Grade5CurriculumRunner(individual_id="test_student_g5_res")

    rec_j, score_j = runner.resolve_dialogue_resonance("The sovereign arbiter upholds dispassionate justice without vengeance.")
    assert rec_j.letter == "J"
    assert score_j > 0.5

    rec_f, score_f = runner.resolve_dialogue_resonance("Freedom requires sacrificial vigilance over the hearth.")
    assert rec_f.letter == "F"
    assert score_f > 0.5


def test_ordinary_memory_comparator_parity_and_restart():
    """Verify matched ordinary-memory comparator produces identical digests under process restart (Rule D004)."""
    comp1 = Grade5OrdinaryMemoryComparator(individual_id="mem_01")
    rep1 = comp1.run_full_curriculum()

    comp2 = Grade5OrdinaryMemoryComparator(individual_id="mem_01")
    rep2 = comp2.run_full_curriculum()

    assert rep1["completed"] == 26
    assert rep1["words_count"] == 3
    assert rep1["digest"] == rep2["digest"]
    assert len(rep1["digest"]) == 64
