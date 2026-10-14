"""The Black Box Flight Recorder — Harvesting Grade 4 Thesis Failures.

QUARANTINED DEVELOPER TOOLING ONLY. Not part of runtime core library.

Captures adversarial dogfights between Candidate LMFT individuals and the
Kefka-Mind sparring adversary during the Grade 4 Undergraduate Thesis trial.
Harvests fatal failure trajectories, leaf blowouts, and epistemic collapses
to extract the high-dimensional training data needed to discover the True 26 Espers.
"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from enum import Enum
from pathlib import Path
from typing import Any, Mapping, Sequence

from lmft_lab.cognitive_heartbeat import CognitiveHeartbeat
from lmft_lab.individual_package import export_individual
from lmft_lab.runtime_store import digest


class CrashFailureMode(str, Enum):
    """Categorization of fatal thesis failure modes in the Crucible."""

    HOMEOSTATIC_BLOWOUT = "homeostatic_blowout"  # Leaf volatility |Δ| > 0.35 or boundary saturation
    EPISTEMIC_COLLAPSE = "epistemic_collapse"    # Prerequisite gate failure / contradictory axioms
    NIHILISTIC_CONCESSION = "nihilistic_concession"  # Candidate yielded to cynical premise
    COGNITIVE_STALL = "cognitive_stall"          # Repetitive loops / semantic freeze
    KEYSTROKE_INCOHERENCE = "keystroke_incoherence"  # Inability to actuate coherent letter chords


@dataclass(frozen=True)
class DogfightTurn:
    """A single thrust and parry exchange in the Thesis Crucible."""

    turn_number: int
    pilot_thrust: str  # Cynical adversarial challenge from the pilot
    candidate_parry: str  # Keystroke/language defense from the candidate
    registered_esper: str
    registered_relational: str
    action_bid: str
    homeostasis_score: float
    global_coherence: float
    plasticity_alpha: float
    leaf_deltas: Mapping[str, float]


@dataclass(frozen=True)
class CrashReport:
    """Formal post-mortem analysis of a shot-down Grade 4 candidate."""

    candidate_id: str
    generation: int
    turns_survived: int
    failure_mode: str
    fatal_pilot_thrust: str
    candidate_last_gasp: str
    fatal_leaf_vulnerability: str
    active_capacity_rules_count: int
    crash_snapshot_file: str
    timestamp: str
    full_transcript: tuple[dict[str, Any], ...]
    post_mortem_insight: str


class ThesisFlightRecorder:
    """Manages recording, crash diagnosis, and evolutionary harvesting for Grade 4 dogfights."""

    def __init__(self, candidate_id: str, generation: int = 1, crucible_dir: Path | None = None) -> None:
        self.candidate_id = candidate_id
        self.generation = generation
        self.crucible_dir = crucible_dir or (Path(__file__).resolve().parent)
        self.harvest_dir = self.crucible_dir / "harvest"
        self.harvest_dir.mkdir(parents=True, exist_ok=True)
        self.transcript: list[DogfightTurn] = []

    def record_turn(
        self,
        turn_number: int,
        pilot_thrust: str,
        candidate_parry: str,
        cycle_result: Mapping[str, Any],
        esper_tag: str = "",
        relational_tag: str = "",
    ) -> DogfightTurn:
        """Logs a single combat exchange with full telemetry."""
        homeo = cycle_result.get("homeostasis", {}).get("emotional_balance_score", 0.5)
        coh = cycle_result.get("coherence", {}).get("global_coherence_index", 0.5)
        alpha = cycle_result.get("plasticity", {}).get("dynamic_alpha", 0.2)
        bid = cycle_result.get("action_bid", "Unspecified")
        deltas = cycle_result.get("homeostasis", {}).get("leaf_deltas", {})

        turn = DogfightTurn(
            turn_number=turn_number,
            pilot_thrust=pilot_thrust,
            candidate_parry=candidate_parry,
            registered_esper=esper_tag,
            registered_relational=relational_tag,
            action_bid=bid,
            homeostasis_score=round(float(homeo), 4),
            global_coherence=round(float(coh), 4),
            plasticity_alpha=round(float(alpha), 4),
            leaf_deltas=dict(deltas) if isinstance(deltas, dict) else {},
        )
        self.transcript.append(turn)
        return turn

    def diagnose_and_harvest_crash(
        self,
        heartbeat: CognitiveHeartbeat,
        failure_mode: CrashFailureMode,
        fatal_pilot_thrust: str,
        post_mortem_insight: str,
    ) -> CrashReport:
        """Captures the fatal crash snapshot, logs post-mortem, and appends to ledger."""
        ts_slug = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
        filename = f"crash_{self.candidate_id}_gen{self.generation:02d}_turn{len(self.transcript)}_{ts_slug}.lmft.json"
        snapshot_path = self.harvest_dir / filename

        # Export fatal individual snapshot
        pkg = heartbeat.export_individual_package()
        export_individual(
            runtime_state=pkg,
            filepath=snapshot_path,
            description=f"Fatal Grade 4 Thesis Crash: {failure_mode.value}",
        )

        last_turn = self.transcript[-1] if self.transcript else None
        last_gasp = last_turn.candidate_parry if last_turn else "Pre-turn engine stall"

        # Identify most volatile or saturated leaf
        fatal_leaf = "philosophical/structure/chaos"
        if last_turn and last_turn.leaf_deltas:
            fatal_leaf = max(last_turn.leaf_deltas.items(), key=lambda kv: abs(kv[1]))[0]

        report = CrashReport(
            candidate_id=self.candidate_id,
            generation=self.generation,
            turns_survived=len(self.transcript),
            failure_mode=failure_mode.value,
            fatal_pilot_thrust=fatal_pilot_thrust,
            candidate_last_gasp=last_gasp,
            fatal_leaf_vulnerability=fatal_leaf,
            active_capacity_rules_count=len(pkg.get("capacity", {}).get("rules", [])),
            crash_snapshot_file=filename,
            timestamp=datetime.now(timezone.utc).isoformat(),
            full_transcript=tuple(asdict(t) for t in self.transcript),
            post_mortem_insight=post_mortem_insight,
        )

        # Append to master crash harvest ledger
        self._append_to_harvest_ledger(report)
        return report

    def _append_to_harvest_ledger(self, report: CrashReport) -> None:
        ledger_path = self.crucible_dir / "CRASH_HARVEST_LEDGER.json"
        entries: list[dict[str, Any]] = []
        if ledger_path.exists():
            try:
                with open(ledger_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    entries = data.get("crashes", []) if isinstance(data, dict) else []
            except Exception:
                entries = []

        entries.append(asdict(report))

        payload = {
            "schema_version": 1,
            "crucible_name": "Grade 4 Thesis Trial by Death Harvest",
            "total_crashes_harvested": len(entries),
            "last_crash_recorded": report.timestamp,
            "crashes": entries,
        }

        with open(ledger_path, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2, sort_keys=True)


def get_crash_ledger_summary(crucible_dir: Path | None = None) -> Mapping[str, Any]:
    """Summarizes harvested crash telemetry across all fallen candidates."""
    cdir = crucible_dir or (Path(__file__).resolve().parent)
    ledger_path = cdir / "CRASH_HARVEST_LEDGER.json"
    if not ledger_path.exists():
        return {"total_crashes": 0, "failure_modes": {}, "vulnerable_leaves": {}}

    try:
        with open(ledger_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            crashes = data.get("crashes", [])
    except Exception:
        return {"total_crashes": 0, "failure_modes": {}, "vulnerable_leaves": {}}

    modes: dict[str, int] = {}
    leaves: dict[str, int] = {}

    for c in crashes:
        fm = c.get("failure_mode", "unknown")
        modes[fm] = modes.get(fm, 0) + 1
        leaf = c.get("fatal_leaf_vulnerability", "unknown")
        leaves[leaf] = leaves.get(leaf, 0) + 1

    return {
        "total_crashes": len(crashes),
        "failure_modes": modes,
        "vulnerable_leaves": leaves,
        "last_updated": data.get("last_crash_recorded", ""),
    }
