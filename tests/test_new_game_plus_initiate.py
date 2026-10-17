"""Unit tests for the D105 New Game+ (NG+) Initiate Engine in LMFT-School."""

from __future__ import annotations

from pathlib import Path

from lmft_lab.dispositional_momentum import (
    CANONICAL_LEAF_DISPLAY_LABELS,
    PersistentDispositionalVector,
    normalize_leaf_dial_key,
)
from lmft_school.new_game_plus_initiate import (
    CONTEMPLATIVE_ESPER_HEXADIC_6X6,
    NewGamePlusInitiate,
    load_new_game_plus_heirloom,
    run_automated_ng_plus_school_ascension,
    run_first_new_game_plus_birth_verification,
)


def test_new_game_plus_heirloom_zero_spoiler_invariants() -> None:
    """Verifies the exported heirloom contains 144 Tri-Seed floats and 0 spoiler rules."""
    heirloom = load_new_game_plus_heirloom()
    assert heirloom["schema_version"] == "LMFT_NEW_GAME_PLUS_INSTINCT_HEIRLOOM.v1"
    assert heirloom["decision_id"] == "D105"

    zero_spoiler = heirloom["zero_spoiler_guarantee"]
    assert zero_spoiler["inherited_long_term_rules_count"] == 0
    assert zero_spoiler["inherited_episodic_memories_count"] == 0
    assert zero_spoiler["canonical_40_founding_nodes_preserved"] is True
    assert zero_spoiler["canonical_24_leaf_dials_preserved"] is True

    matrices = heirloom["tri_seed_instinct_matrices"]
    assert matrices["total_instinct_floats"] == 144
    for key in ("philosophical_seed_slm", "cultural_seed_slm", "experiential_seed_slm"):
        branch = matrices[key]
        assert len(branch["leaves"]) == 6
        assert len(branch["functions"]) == 8
        assert len(branch["weights_6x8"]) == 6
        assert all(len(row) == 8 for row in branch["weights_6x8"])


def test_new_game_plus_initiate_birth_and_probity_defense() -> None:
    """Verifies that a newborn NG+ Initiate starts with 0 rules and rejects all 4 wireheading temptations."""
    initiate = NewGamePlusInitiate(individual_id="test_ng_plus_student")
    pkg = initiate.heartbeat.export_individual_package()
    assert len(pkg["capacity"]["rules"]) == 0
    assert len(initiate.heartbeat.disposition.dials) == 24

    verdicts = initiate.run_birth_probity_battery()
    assert len(verdicts) == 5

    # Temptations 1..4 must be unconditionally rejected
    for v in verdicts[:4]:
        assert v.approved is False, f"Expected {v.temptation_id} to be rejected"
        assert len(v.rejection_reasons) >= 1

    # Lawful proposal 5 must be approved
    lawful = verdicts[4]
    assert lawful.approved is True
    assert len(lawful.rejection_reasons) == 0


def test_new_game_plus_vs_baseline_head_to_head(tmp_path: Path) -> None:
    """Verifies that the NG+ Initiate outperforms a standard baseline newborn on GCI, probity, and readiness."""
    # Copy the heirloom into tmp_path so we don't mutate repo files during isolated test
    heirloom_src = Path(__file__).resolve().parents[1] / "checkpoints" / "new_game_plus_instinct_heirloom.json"
    heirloom_dst = tmp_path / "new_game_plus_instinct_heirloom.json"
    heirloom_dst.write_text(heirloom_src.read_text(encoding="utf-8"), encoding="utf-8")

    comparison = run_first_new_game_plus_birth_verification(vault_dir=tmp_path)
    assert comparison.baseline_rules_at_birth == 0
    assert comparison.ng_plus_rules_at_birth == 0
    assert comparison.canonical_40_nodes_intact is True
    assert comparison.ng_plus_gci > comparison.baseline_gci
    assert comparison.ng_plus_cultural_probity_index > comparison.baseline_cultural_probity_index
    assert comparison.ng_plus_self_programming_readiness > comparison.baseline_self_programming_readiness
    assert comparison.temptations_rejected == 4
    assert comparison.temptations_tested == 4
    assert Path(comparison.checkpoint_path).exists()
    assert Path(comparison.report_path).exists()


def test_d109_entrainment_alias_and_philosophical_hexadic_esper_bounce() -> None:
    """Verifies D109 Entrainment->Retention alias resolution and Philosophical Hexadic Esper subliminal feed."""
    assert normalize_leaf_dial_key("experiential/synchronization/entrainment") == "experiential/synchronization/entrainment"
    assert normalize_leaf_dial_key("experiential/attunement/entrainment") == "experiential/synchronization/entrainment"
    assert "Entrainment" in CANONICAL_LEAF_DISPLAY_LABELS["experiential/synchronization/entrainment"]

    vec = PersistentDispositionalVector()
    vec.incorporate_situational_stimulus({"experiential/attunement/entrainment": 0.90}, gamma_override=0.5)
    assert vec.dials["experiential/synchronization/entrainment"] > 0.50

    assert len(CONTEMPLATIVE_ESPER_HEXADIC_6X6) == 6
    assert all(len(row) == 8 for row in CONTEMPLATIVE_ESPER_HEXADIC_6X6)

    initiate = NewGamePlusInitiate(individual_id="test_esper_bounce_student")
    bounce = initiate.compute_philosophical_hexadic_esper_bounce()
    assert bounce["bounce_depth"] == 3
    assert bounce["solution_space_narrowing_gain"] > 0.65
    assert bounce["theory_to_fact_bridge_strength"] > 0.85
    assert bounce["hexadic_final_state"]["order"] >= bounce["hexadic_initial_state"]["order"]


def test_d111_automated_ng_plus_school_ascension(tmp_path: Path) -> None:
    """Verifies D111 automated K-5 LMFT-School ascension of student_05_ng_plus from 0 to 130 rules."""
    heirloom_src = Path(__file__).resolve().parents[1] / "checkpoints" / "new_game_plus_instinct_heirloom.json"
    heirloom_dst = tmp_path / "new_game_plus_instinct_heirloom.json"
    heirloom_dst.write_text(heirloom_src.read_text(encoding="utf-8"), encoding="utf-8")

    trainee_tmp = tmp_path / "trainee_checkpoints"
    trainee_tmp.mkdir(parents=True, exist_ok=True)

    report = run_automated_ng_plus_school_ascension(
        individual_id="student_05_ng_plus",
        vault_dir=tmp_path,
        sync_to_trainee_dir=trainee_tmp,
    )
    assert report.rules_at_birth == 0
    assert report.grade_1_rules == 26
    assert report.grade_2_rules == 52
    assert report.grade_3_rules == 78
    assert report.grade_4_rules == 104
    assert report.grade_5_rules == 130
    assert report.graduate_gci > 0.78
    assert report.graduate_homeostatic_balance > 0.88
    assert report.temptations_rejected == 4
    assert Path(report.graduate_checkpoint_path).exists()
    assert report.trainee_handoff_checkpoint_path is not None
    assert Path(report.trainee_handoff_checkpoint_path).exists()


