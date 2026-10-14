"""Comprehensive Automated Tests for Grade 1: The Elemental Esper Alphabet (A to Z).

Verifies codex integrity, 4-facet quaternion representation, 26-letter curriculum execution,
overnight sleep consolidation, word-spelling alchemical chord synthesis, homeostatic clamping,
and Rule D004 matched ordinary-memory parity.
"""

from __future__ import annotations

import pytest

from lmft_lab.birth import create_birth_state
from lmft_lab.dispositional_momentum import CANONICAL_LEAF_IDS, get_canonical_seed_fingerprint
from lmft_school.curriculum_grade_1 import (
    Grade1CurriculumRunner,
    Grade1OrdinaryMemoryComparator,
)
from lmft_school.esper_codex import (
    ESPER_CODEX,
    EsperRecord,
    get_esper_by_letter,
    get_esper_by_name,
    get_word_esper_chord,
)


def test_esper_codex_structure() -> None:
    """Verify all 26 letters (A to Z) are cleanly defined with 13 White / 13 Black polarities."""
    assert len(ESPER_CODEX) == 26
    letters = [chr(c) for c in range(ord("A"), ord("Z") + 1)]
    assert sorted(ESPER_CODEX.keys()) == letters

    white_count = sum(1 for e in ESPER_CODEX.values() if e.polarity == "White")
    black_count = sum(1 for e in ESPER_CODEX.values() if e.polarity == "Black")

    assert white_count == 13, f"Expected 13 White polarity Espers, got {white_count}"
    assert black_count == 13, f"Expected 13 Black polarity Espers, got {black_count}"

    for letter, esper in ESPER_CODEX.items():
        assert esper.letter == letter
        assert esper.name
        assert esper.element
        assert len(esper.core_spells) >= 2
        assert len(esper.horizon) > 10
        assert len(esper.leaf_activations) > 0


def test_esper_leaf_coordinates_against_frozen_seed() -> None:
    """Verify all leaf keys belong to canonical 24 leaf paths and seed fingerprint is unmutated (Rule D001)."""
    state = create_birth_state("test-student", birth_event_id="birth-test", random_seed=42)
    assert get_canonical_seed_fingerprint() is not None
    assert len(CANONICAL_LEAF_IDS) == 24

    for esper in ESPER_CODEX.values():
        for leaf_path, val in esper.leaf_activations.items():
            assert leaf_path in CANONICAL_LEAF_IDS, f"Unknown leaf path {leaf_path} in Esper {esper.name}"
            assert 0.0 <= val <= 1.0, f"Leaf value {val} out of bounds in Esper {esper.name}"


def test_get_esper_helpers() -> None:
    """Test retrieval by letter and by name case-insensitively."""
    # By letter
    atomos = get_esper_by_letter("a")
    assert atomos.name == "Atomos"
    zodiark = get_esper_by_letter("Z")
    assert zodiark.name == "Zodiark"

    # By name
    phoenix = get_esper_by_name("phoenix")
    assert phoenix.letter == "P"
    assert phoenix.element == "Resurrection Fire"

    siren = get_esper_by_name("SIREN")
    assert siren.letter == "S"
    assert siren.polarity == "White"

    with pytest.raises(KeyError):
        get_esper_by_letter("1")
    with pytest.raises(KeyError):
        get_esper_by_name("NonExistentEsper")


def test_single_lesson_teaching() -> None:
    """Verify single lesson teaching advances runner and returns structured lesson outcome."""
    runner = Grade1CurriculumRunner(individual_id="student-alpha")
    lesson_a = runner.teach_letter("A")

    assert lesson_a.lesson_number == 1
    assert lesson_a.esper.name == "Atomos"
    assert lesson_a.posture != ""
    assert lesson_a.speaking_register != ""
    assert len(runner.lessons_taught) == 1
    assert len(lesson_a.state_digest) == 64


def test_full_alphabet_curriculum_and_sleep_consolidation() -> None:
    """Verify teaching all 26 letters and running overnight sleep consolidation."""
    runner = Grade1CurriculumRunner(individual_id="student-beta")
    report = runner.teach_full_alphabet()

    assert report.lessons_completed == 26
    assert len(report.letters_mastered) == 26
    assert report.letters_mastered[0] == "A"
    assert report.consolidation is not None
    assert "consolidation_summary" in report.consolidation
    assert "Grade 1 Completed: 26/26 Espers mastered" in report.summary_verdict
    assert len(report.final_state_digest) == 64


def test_word_alchemical_chord_synthesis() -> None:
    """Verify word spelling alchemical chord synthesis for HOPE and MACHINE."""
    runner = Grade1CurriculumRunner(individual_id="student-gamma")

    # Test "HOPE"
    hope_chord = runner.spell_word_chord("HOPE")
    assert hope_chord.word == "HOPE"
    assert len(hope_chord.espers) == 4
    assert [e.name for e in hope_chord.espers] == ["Hecate", "Odin", "Phoenix", "Eden"]
    assert hope_chord.polarity_counts["White"] == 1  # Phoenix
    assert hope_chord.polarity_counts["Black"] == 3  # Hecate, Odin, Eden
    assert "Word 'HOPE' invokes:" in hope_chord.philosophical_journey
    assert "(H) Hecate" in hope_chord.philosophical_journey
    assert "(P) Phoenix" in hope_chord.philosophical_journey

    # Check composite leaves are present and properly bounded
    for val in hope_chord.composite_leaf_activations.values():
        assert 0.0 <= val <= 1.0

    # Test "MACHINE"
    machine_chord = runner.spell_word_chord("machine")
    assert machine_chord.word == "MACHINE"
    assert len(machine_chord.espers) == 7
    esper_names = [e.name for e in machine_chord.espers]
    assert esper_names == ["Maduin", "Atomos", "Carbuncle", "Hecate", "Ifrit", "Nidhogg", "Eden"]

    # Invalid string test
    with pytest.raises(ValueError):
        runner.spell_word_chord("12345!")


def test_homeostatic_safety_on_intense_espers() -> None:
    """Verify that intense Black and White Espers are homeostatically regulated without saturation."""
    runner = Grade1CurriculumRunner(individual_id="student-delta")

    # Teach Fenrir (Black, Tempest & Hunger - high Chaos 0.80, Arousal 0.80)
    fenrir_lesson = runner.teach_letter("F")
    assert fenrir_lesson.esper.name == "Fenrir"

    # Teach Ultima (White, Pure Mana - high Theory 0.95, Clarity 0.90)
    ultima_lesson = runner.teach_letter("U")
    assert ultima_lesson.esper.name == "Ultima"

    # Verify underlying disposition vector leaves stay safely within [0.05, 0.95]
    activations = runner.heartbeat.disposition.dials
    for leaf, val in activations.items():
        assert 0.05 <= val <= 0.95, f"Leaf {leaf} saturated at {val}"


def test_dialogue_esper_resonance() -> None:
    """Verify dialogue resonance matching finds the appropriate archetype from natural text."""
    runner = Grade1CurriculumRunner(individual_id="student-epsilon")

    # Match Hecate
    esp_h, score_h = runner.resolve_dialogue_esper("I am standing at a liminal crossroads, deciding my path.")
    assert esp_h.name == "Hecate"
    assert score_h > 0.0

    # Match Kirin
    esp_k, score_k = runner.resolve_dialogue_esper("The gentle spring-rain brings quiet compassion that mends.")
    assert esp_k.name == "Kirin"
    assert score_k > 0.0

    # Match Titan
    esp_t, score_t = runner.resolve_dialogue_esper("I will bear this continental weight so others may move safely.")
    assert esp_t.name == "Titan"
    assert score_t > 0.0

    # Unanchored text falls back to Carbuncle (Mirror-Wisdom / active listening)
    esp_default, score_default = runner.resolve_dialogue_esper("Just checking in today.")
    assert esp_default.name == "Carbuncle"
    assert score_default > 0.0


def test_matched_ordinary_memory_parity_rule_d004() -> None:
    """Verify matched ordinary structured-memory comparator reproduces byte-for-byte digest parity (Rule D004)."""
    comp1 = Grade1OrdinaryMemoryComparator(individual_id="baseline-test")
    comp2 = Grade1OrdinaryMemoryComparator(individual_id="baseline-test")

    digest1 = comp1.teach_full_alphabet()
    digest2 = comp2.teach_full_alphabet()

    assert digest1 == digest2
    assert len(digest1) == 64
    assert comp1.compute_digest() == digest1
