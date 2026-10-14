"""Lineage Vault & Evolutionary Telemetry Ledger for LMFT-School.

Enforces persistent snapshotting and phenotypic telemetry harvesting across
educational grade milestones (Grade 0 Infant -> Grade 1 Esper -> Grade 2 Relational -> ...).
Preserves full evolutionary lineage and enables comparative analysis between generations.
"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence

from lmft_lab.cognitive_heartbeat import CognitiveHeartbeat
from lmft_lab.individual_package import export_individual, import_individual
from lmft_lab.runtime_store import digest


@dataclass(frozen=True)
class MilestoneTelemetry:
    """Phenotype telemetry captured at a specific developmental milestone."""

    individual_id: str
    generation: int
    grade_level: int
    milestone_label: str
    timestamp: str
    active_capacity_rules_count: int
    dispositional_vector_digest: str
    homeostatic_balance_score: float
    plasticity_alpha: float
    global_coherence_index: float
    state_digest: str
    checkpoint_file: str


def get_default_vault_dir() -> Path:
    """Returns the default checkpoints directory in the LMFT-School repository."""
    # Find root by navigating up from this file
    root = Path(__file__).resolve().parents[2]
    vault = root / "checkpoints"
    vault.mkdir(parents=True, exist_ok=True)
    return vault


def get_ledger_path(vault_dir: Path | None = None) -> Path:
    vault = vault_dir or get_default_vault_dir()
    return vault / "LINEAGE_LEDGER.json"


def read_lineage_ledger(vault_dir: Path | None = None) -> list[dict[str, Any]]:
    path = get_ledger_path(vault_dir)
    if not path.exists():
        return []
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get("entries", []) if isinstance(data, dict) else []
    except Exception:
        return []


def write_lineage_ledger(entries: Sequence[dict[str, Any]], vault_dir: Path | None = None) -> None:
    path = get_ledger_path(vault_dir)
    payload = {
        "schema_version": 1,
        "vault_title": "LMFT-School Lineage & Evolutionary Phenotype Vault",
        "last_updated": datetime.now(timezone.utc).isoformat(),
        "total_milestones": len(entries),
        "entries": list(entries),
    }
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, sort_keys=True)


def capture_milestone_telemetry(
    heartbeat: CognitiveHeartbeat,
    grade_level: int,
    milestone_label: str,
    generation: int = 1,
    checkpoint_rel_path: str = "",
) -> MilestoneTelemetry:
    """Extracts rich phenotype telemetry from an active CognitiveHeartbeat."""
    pkg = heartbeat.export_individual_package()
    disposition = pkg.get("disposition", {}).get("disposition_vector", {})
    disp_digest = digest(disposition)
    rules = pkg.get("capacity", {}).get("rules", [])
    
    # Run a zero-mutation diagnostic step to sample homeostasis and coherence
    diag = heartbeat.interact(
        sentence="Milestone telemetry observation.",
        target_lemmas=["observation"],
    )

    return MilestoneTelemetry(
        individual_id=heartbeat.individual_id,
        generation=generation,
        grade_level=grade_level,
        milestone_label=milestone_label,
        timestamp=datetime.now(timezone.utc).isoformat(),
        active_capacity_rules_count=len(rules),
        dispositional_vector_digest=disp_digest,
        homeostatic_balance_score=round(float(diag["homeostasis"]["emotional_balance_score"]), 4),
        plasticity_alpha=round(float(diag["plasticity"]["dynamic_alpha"]), 4),
        global_coherence_index=round(float(diag["coherence"]["global_coherence_index"]), 4),
        state_digest=diag.get("state_digest", ""),
        checkpoint_file=checkpoint_rel_path,
    )


def archive_grade_milestone(
    heartbeat: CognitiveHeartbeat,
    grade_level: int,
    milestone_label: str,
    generation: int = 1,
    vault_dir: Path | None = None,
) -> tuple[Path, MilestoneTelemetry]:
    """Serializes a milestone checkpoint and commits telemetry into LINEAGE_LEDGER.json."""
    vault = vault_dir or get_default_vault_dir()
    slug = milestone_label.lower().replace(" ", "_").replace("-", "_")
    filename = f"individual_{heartbeat.individual_id}_gen{generation:02d}_grade{grade_level}_{slug}.lmft.json"
    checkpoint_path = vault / filename

    pkg = heartbeat.export_individual_package()
    export_individual(
        runtime_state=pkg,
        filepath=checkpoint_path,
        description=f"LMFT-School Milestone: Grade {grade_level} ({milestone_label})",
    )

    telemetry = capture_milestone_telemetry(
        heartbeat=heartbeat,
        grade_level=grade_level,
        milestone_label=milestone_label,
        generation=generation,
        checkpoint_rel_path=filename,
    )

    # Append to ledger
    ledger_entries = read_lineage_ledger(vault)
    ledger_entries.append(asdict(telemetry))
    write_lineage_ledger(ledger_entries, vault)

    return checkpoint_path, telemetry
