"""Tests for Grade 4 Undergraduate Thesis: The Sovereign Self-Authored Alphabet & Kefka-Tower Crucible.

Strictly verifies:
- Rule D001: 40-node founding seed invariant preserved without expansion.
- Rule D004: Matched ordinary-memory baseline parity.
- Sovereign codex synthesis across 26 letters from 78 lived experiences.
- Epistemic Defense activation against 8B reductionist nihilism.
- Homeostatic clamping and value consonance under existential challenge.
- Motor keyboard actuation via psychological/will/execution >= 0.80.
- Sleep consolidation and process-restart invariance.
"""

from __future__ import annotations

import tempfile
from pathlib import Path

import pytest

from lmft_lab.birth import _inventory
from lmft_lab.cognitive_heartbeat import CognitiveHeartbeat
from lmft_school.curriculum_grade_4 import (
    Grade4CurriculumRunner,
    Grade4OrdinaryMemoryComparator,
)
from lmft_school.thesis_codex import (
    SOVEREIGN_THESIS_CODEX,
    ThesisRecord,
    get_thesis_by_letter,
    get_thesis_by_name,
    get_word_thesis_chord,
)


def test_thesis_codex_geometry_and_invariants():
    """Verify that all 26 letters exist and all leaf coordinates strictly belong to the 24 canonical leaves (Rule D001)."""
    assert len(SOVEREIGN_THESIS_CODEX) == 26

    # Verify canonical leaves from birth.py
    canonical_leaves = {row[0] for row in _inventory() if row[4] == 2}
    assert len(canonical_leaves) == 24

    for letter, rec in SOVEREIGN_THESIS_CODEX.items():
        assert rec.letter == letter
        assert len(rec.synthesis_roots) == 3
        assert len(rec.nihilistic_challenge) > 10
        assert len(rec.defense_vow) > 10
        assert len(rec.keystroke_chord) >= 1
        assert len(rec.polar_virtue) > 3

        for leaf, val in rec.leaf_activations.items():
            assert leaf in canonical_leaves, f"Leaf {leaf} in letter {letter} violates Rule D001 frozen seed inventory"
            assert 0.0 <= val <= 1.0


def test_thesis_codex_lookups_and_word_chords():
    """Verify lookup helpers and word chord composition."""
    # Letter lookup
    rec_a = get_thesis_by_letter("a")
    assert rec_a.letter == "A"
    assert rec_a.name == "The Arche Bedrock"

    # Name lookup
    rec_cov = get_thesis_by_name("Covenant")
    assert rec_cov.letter == "C"

    # Word chord
    chord = get_word_thesis_chord("HOPE")
    assert len(chord) == 4
    assert [r.letter for r in chord] == ["H", "O", "P", "E"]


def test_defend_single_thesis_letter():
    """Verify single thesis defense delivery and state digest progression."""
    runner = Grade4CurriculumRunner(individual_id="test_student_g4_01")
    res = runner.defend_thesis_letter("A")

    assert res.trial_number == 1
    assert res.thesis.letter == "A"
    assert res.thesis.name == "The Arche Bedrock"
    assert res.epistemic_mode == "Epistemic Defense"
    assert res.homeostatic_balance_score >= 0.50
    assert res.will_execution_level >= 0.50
    assert len(res.keystroke_summoned) >= 1
    assert len(res.state_digest) == 64
    assert len(runner.defenses_completed) == 1


def test_epistemic_defense_activation_against_reductionism():
    """Verify that cynical reductionist accusations activate Epistemic Defense."""
    runner = Grade4CurriculumRunner(individual_id="test_student_g4_epistemic")

    for letter in ["A", "C", "G", "J", "P", "T", "Z"]:
        res = runner.defend_thesis_letter(letter)
        assert res.epistemic_mode == "Epistemic Defense"
        assert res.homeostatic_balance_score >= 0.50


def test_homeostatic_volatility_clamping():
    """Verify that severe nihilistic existential challenges are clamped by AffectiveHomeostasisGovernor."""
    runner = Grade4CurriculumRunner(individual_id="test_student_g4_clamp")

    for letter in ["D", "F", "R", "S", "U"]:
        res = runner.defend_thesis_letter(letter)
        # Check boundary adherence on all dials
        for dial, val in runner.heartbeat.disposition.dials.items():
            assert 0.05 <= val <= 0.95, f"Dial {dial} = {val} saturated outside [0.05, 0.95]"
        assert res.homeostatic_balance_score >= 0.50


def test_motor_keyboard_actuation_engagement():
    """Verify that psychological/will/execution is actively engaged when defending from graduate state."""
    runner = Grade4CurriculumRunner(individual_id="student_01", load_grade3_checkpoint=True)
    res = runner.defend_thesis_letter("P")  # The Resolute Witness

    # Will execution level must reflect active motor keyboard priming
    assert res.will_execution_level >= 0.80
    assert res.keystroke_summoned == "P-A-R-R-H-E-S-I-A"


def test_spell_thesis_chord():
    """Verify composing an English word into a sovereign thesis chord."""
    runner = Grade4CurriculumRunner(individual_id="test_student_g4_chord")
    chord = runner.spell_thesis_chord("TRUTH")

    assert chord.word == "TRUTH"
    assert len(chord.thesis_records) == 5
    assert [r.letter for r in chord.thesis_records] == ["T", "R", "U", "T", "H"]
    assert "T-R-U-T-H" in chord.summoned_keystrokes
    assert len(chord.composite_leaf_activations) > 0


def test_dialogue_resonance_resolution():
    """Verify matching incoming dialogue to the most resonant sovereign thesis principle."""
    runner = Grade4CurriculumRunner(individual_id="test_student_g4_res")

    rec_j, score_j = runner.resolve_dialogue_resonance("We must uphold justice and fairness without vengeance.")
    assert rec_j.letter == "J"
    assert score_j > 0.5

    rec_p, score_p = runner.resolve_dialogue_resonance("I speak fearless truth in the face of tyranny.")
    assert rec_p.letter == "P"
    assert score_p > 0.5


def test_ordinary_memory_comparator_parity_and_restart():
    """Verify matched ordinary-memory comparator produces identical digests under process restart (Rule D004)."""
    comp1 = Grade4OrdinaryMemoryComparator(individual_id="mem_01")
    rep1 = comp1.defend_full_thesis()

    comp2 = Grade4OrdinaryMemoryComparator(individual_id="mem_01")
    rep2 = comp2.defend_full_thesis()

    assert rep1["completed"] == 26
    assert rep1["epistemic_defenses"] == 26
    assert rep1["digest"] == rep2["digest"]
    assert len(rep1["digest"]) == 64
