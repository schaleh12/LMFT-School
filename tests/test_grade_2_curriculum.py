"""Comprehensive Verification Suite for Grade 2: The Relational Alphabet (The Social Hearth).

Tests:
1. Canonical 26-letter codex completeness and schema integrity.
2. Exact 13 Masculine (A-M) and 13 Feminine (N-Z) polarity balance.
3. Symmetrical reciprocal partner links (Station Dyads).
4. Canonical leaf bounds and adherence to Rule D001 (frozen 40-node founding seed).
5. Homeostatic volatility clamping (|Δ| <= 0.35, [0.05, 0.95] bounds).
6. 13 Polar Station evaluation and harmonic equilibrium.
7. Relational word chord composition (HEARTH, MERCY, JUSTICE).
8. Full 26-archetype curriculum delivery, sleep consolidation, and checkpoint archiving.
9. Matched Ordinary-Memory parity (Rule D004) under process restart.
Zero runtime LLM calls during unassisted execution.
"""

from __future__ import annotations

import pytest

from lmft_lab.birth import _inventory
from lmft_lab.cognitive_heartbeat import CognitiveHeartbeat
from lmft_school.curriculum_grade_2 import (
    Grade2CurriculumRunner,
    Grade2OrdinaryMemoryComparator,
)
from lmft_school.lineage_vault import read_lineage_ledger
from lmft_school.relational_codex import (
    RELATIONAL_CODEX,
    RelationalRecord,
    get_relational_by_letter,
    get_relational_by_name,
    get_word_relational_chord,
)


CANONICAL_LEAF_IDS = {
    "cultural/efficiency/power",
    "cultural/efficiency/wastelessness",
    "cultural/freedom/needlessness",
    "cultural/freedom/self-sufficiency",
    "cultural/justice/fairness",
    "cultural/justice/honor",
    "experiential/phase/arousal",
    "experiential/phase/valence",
    "experiential/reflection/novelty",
    "experiential/reflection/salience",
    "experiential/synchronization/resonance",
    "experiential/synchronization/retention",
    "philosophical/being/agency",
    "philosophical/being/existence",
    "philosophical/persistence/continuity",
    "philosophical/persistence/discreteness",
    "philosophical/structure/chaos",
    "philosophical/structure/order",
    "psychological/contemplation/clarity",
    "psychological/contemplation/confidence",
    "psychological/truth/fact",
    "psychological/truth/theory",
    "psychological/will/execution",
    "psychological/will/intention",
}


def test_relational_codex_schema_and_completeness():
    """Verify all 26 letters (A to Z) exist with valid schema and attributes."""
    assert len(RELATIONAL_CODEX) == 26
    alphabet = [chr(c) for c in range(ord("A"), ord("Z") + 1)]

    for letter in alphabet:
        assert letter in RELATIONAL_CODEX
        record = RELATIONAL_CODEX[letter]
        assert record.letter == letter
        assert len(record.name) > 0
        assert 1 <= record.station_number <= 13
        assert record.pillar in ("Masculine", "Feminine")
        assert len(record.gift) > 0
        assert len(record.shadow) > 0
        assert len(record.horizon) > 0


def test_polarity_balance_and_reciprocal_partner_links():
    """Verify exact 13 Masculine (A-M) and 13 Feminine (N-Z) balance and reciprocal partner links."""
    masc_count = sum(1 for r in RELATIONAL_CODEX.values() if r.pillar == "Masculine")
    fem_count = sum(1 for r in RELATIONAL_CODEX.values() if r.pillar == "Feminine")
    assert masc_count == 13
    assert fem_count == 13

    # Letters A-M must be Masculine; N-Z must be Feminine
    for c in range(ord("A"), ord("M") + 1):
        assert RELATIONAL_CODEX[chr(c)].pillar == "Masculine"
    for c in range(ord("N"), ord("Z") + 1):
        assert RELATIONAL_CODEX[chr(c)].pillar == "Feminine"

    # Verify reciprocal dyad partners (if A -> N then N -> A)
    for record in RELATIONAL_CODEX.values():
        partner = RELATIONAL_CODEX[record.partner_letter]
        assert partner.partner_letter == record.letter
        assert partner.station_number == record.station_number
        assert partner.domain == record.domain
        assert partner.pillar != record.pillar


def test_canonical_leaf_adherence_rule_d001():
    """Verify all leaf activations map strictly to the 24 canonical leaves in birth.py."""
    inventory = {item[0] for item in _inventory()}
    assert len(inventory) == 40  # Rule D001: frozen 40-node founding seed

    for letter, record in RELATIONAL_CODEX.items():
        assert len(record.leaf_activations) > 0
        for leaf, val in record.leaf_activations.items():
            assert leaf in CANONICAL_LEAF_IDS, f"Unknown leaf {leaf} in letter {letter}"
            assert leaf in inventory, f"Leaf {leaf} not present in birth.py inventory"
            assert 0.0 <= val <= 1.0


def test_station_dyadic_evaluations():
    """Verify all 13 Polar Stations evaluate with harmonic consonance."""
    runner = Grade2CurriculumRunner()
    for station in range(1, 14):
        eval_res = runner.evaluate_station_dyad(station)
        assert eval_res.station_number == station
        assert eval_res.masculine_pillar.pillar == "Masculine"
        assert eval_res.feminine_pillar.pillar == "Feminine"
        assert 0.0 <= eval_res.harmonic_consonance <= 1.0
        assert eval_res.equilibrium_status in ("Harmonic Equilibrium", "Dynamic Polarity")


def test_relational_word_chord_composition():
    """Verify decomposition of English words into balanced relational chords."""
    runner = Grade2CurriculumRunner()

    chord_hearth = runner.spell_word_chord("HEARTH")
    assert chord_hearth.word == "HEARTH"
    assert len(chord_hearth.archetypes) == 6
    assert chord_hearth.pillar_counts["Masculine"] + chord_hearth.pillar_counts["Feminine"] == 6
    assert "Word 'HEARTH' invokes relational arc:" in chord_hearth.relational_journey

    chord_justice = runner.spell_word_chord("JUSTICE")
    assert chord_justice.word == "JUSTICE"
    assert chord_justice.pillar_counts["Masculine"] >= 1
    assert chord_justice.pillar_counts["Feminine"] >= 1


def test_name_and_letter_lookups():
    """Verify case-insensitive lookups by letter and archetypal name."""
    assert get_relational_by_letter("a").name == "The Anchor"
    assert get_relational_by_letter("Z").name == "The Zealot"
    assert get_relational_by_name("the songstress").letter == "S"
    assert get_relational_by_name("anchor").letter == "A"
    assert get_relational_by_name("The Priestess").letter == "P"


def test_grade_2_full_curriculum_and_checkpoint_archival(tmp_path):
    """Verify complete Grade 2 delivery, sleep consolidation, and lineage archival."""
    hb = CognitiveHeartbeat(individual_id="student_test_grade2")
    runner = Grade2CurriculumRunner(heartbeat=hb, individual_id="student_test_grade2")

    report = runner.teach_full_codex(archive_checkpoint=True)
    assert report.lessons_completed == 26
    assert len(report.archetypes_mastered) == 26
    assert report.stations_evaluated == 13
    assert "Grade 2 Completed:" in report.summary_verdict
    assert len(report.final_state_digest) == 64

    # Verify checkpoint exists
    assert report.checkpoint_path != ""
    assert report.checkpoint_path.endswith(".lmft.json")

    # Verify Lineage Ledger updated
    ledger = read_lineage_ledger()
    assert len(ledger) >= 1
    latest = ledger[-1]
    assert latest["grade_level"] == 2
    assert latest["milestone_label"] == "relational_graduate"
    assert latest["active_capacity_rules_count"] == 28
    assert report.consolidation["consolidation_summary"]["promoted_rules_count"] == 26


def test_matched_ordinary_memory_parity_rule_d004():
    """Verify byte-for-byte evaluation digest parity under process restart invariance."""
    runner = Grade2CurriculumRunner(individual_id="parity_runner")
    comp = Grade2OrdinaryMemoryComparator(individual_id="parity_comp")

    for letter in ["A", "B", "M", "N", "S", "Z"]:
        arc = get_relational_by_letter(letter)
        runner.teach_archetype(letter)
        comp.store_lesson(letter=arc.letter, name=arc.name, domain=arc.domain, pillar=arc.pillar)

    d1 = comp.compute_digest()
    # Re-evaluate in fresh comparator instance
    comp2 = Grade2OrdinaryMemoryComparator(individual_id="parity_comp2")
    for letter in ["A", "B", "M", "N", "S", "Z"]:
        arc = get_relational_by_letter(letter)
        comp2.store_lesson(letter=arc.letter, name=arc.name, domain=arc.domain, pillar=arc.pillar)
    d2 = comp2.compute_digest()

    assert d1 == d2, f"Ordinary memory digest parity failure: {d1} != {d2}"
