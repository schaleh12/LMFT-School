"""Unit tests for the D105 New Game+ (NG+) Initiate Engine in LMFT-School."""

from __future__ import annotations

from pathlib import Path

from lmft_school.new_game_plus_initiate import (
    NewGamePlusInitiate,
    load_new_game_plus_heirloom,
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
