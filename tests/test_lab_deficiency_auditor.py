"""Unit tests for the D107 LMFT-Lab Implicit Deficiency Auditor & Remediation Engine."""

from __future__ import annotations

from lmft_school.lab_deficiency_auditor import run_lmft_lab_deficiency_diagnostic_suite


def test_lmft_lab_four_implicit_deficiencies_spotted_and_remediated() -> None:
    """Verifies all 4 implicit deficiencies in `lmft_lab` are reproduced and cleanly remediated."""
    proofs = run_lmft_lab_deficiency_diagnostic_suite()
    assert len(proofs) == 4
    for p in proofs:
        assert p.remediation_verified is True, f"Failed remediation proof for {p.deficiency_id}"
