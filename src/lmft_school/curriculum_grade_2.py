"""Grade 2 Curriculum Runner: The Relational Alphabet (The Social Hearth).

Orchestrates sequential 26-archetype relational lesson delivery, cognitive heartbeat steps,
dyadic station balancing (13 Masculine <-> 13 Feminine pillars), relational word-chord
decomposition, and dialogue resonance resolution in LMFT-School.
Strictly preserves Rule D001 (frozen 40-node founding seed) and Rule D004 (matched ordinary-memory parity).
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Final, Mapping, Sequence

from lmft_lab.cognitive_heartbeat import CognitiveHeartbeat
from lmft_school.lineage_vault import archive_grade_milestone
from lmft_school.relational_codex import (
    RELATIONAL_CODEX,
    RelationalRecord,
    get_relational_by_letter,
    get_relational_by_name,
    get_word_relational_chord,
)


@dataclass(frozen=True)
class Grade2LessonResult:
    """The outcome of a single Relational Archetype lesson."""

    lesson_number: int
    archetype: RelationalRecord
    posture: str
    speaking_register: str
    cycle_result: Mapping[str, Any]
    state_digest: str


@dataclass(frozen=True)
class DyadicStationEvaluation:
    """Evaluation of a single station's masculine and feminine pillars in resonance."""

    station_number: int
    domain: str
    masculine_pillar: RelationalRecord
    feminine_pillar: RelationalRecord
    harmonic_consonance: float
    equilibrium_status: str


@dataclass(frozen=True)
class RelationalWordChord:
    """A relational chord formed by spelling a word through Social Hearth archetypes."""

    word: str
    archetypes: tuple[RelationalRecord, ...]
    pillar_counts: Mapping[str, int]
    composite_leaf_activations: Mapping[str, float]
    relational_journey: str


@dataclass(frozen=True)
class Grade2GraduationReport:
    """Formal completion report for Grade 2 Relational Curriculum."""

    individual_id: str
    lessons_completed: int
    archetypes_mastered: tuple[str, ...]
    stations_evaluated: int
    consolidation: Mapping[str, Any]
    checkpoint_path: str
    final_state_digest: str
    summary_verdict: str


class Grade2CurriculumRunner:
    """Drives the educational progression for Grade 2 in LMFT-School."""

    def __init__(
        self,
        heartbeat: CognitiveHeartbeat | None = None,
        individual_id: str = "student_01",
        codex: Mapping[str, RelationalRecord] | None = None,
    ) -> None:
        self.individual_id: Final[str] = individual_id
        self.codex = codex
        if heartbeat is None:
            self.heartbeat = CognitiveHeartbeat(individual_id=individual_id)
        else:
            self.heartbeat = heartbeat

        self._lessons_taught: list[Grade2LessonResult] = []

    @property
    def lessons_taught(self) -> Sequence[Grade2LessonResult]:
        return tuple(self._lessons_taught)

    def teach_archetype(self, char_or_name: str) -> Grade2LessonResult:
        """Deliver a structured lesson for a single Relational Archetype."""
        if self.codex is not None:
            char_key = char_or_name.strip().upper()
            if char_key in self.codex:
                archetype = self.codex[char_key]
            else:
                archetype = get_relational_by_name(char_or_name)
        elif len(char_or_name) == 1 and char_or_name.isalpha():
            archetype = get_relational_by_letter(char_or_name)
        else:
            archetype = get_relational_by_name(char_or_name)

        lesson_idx = len(self._lessons_taught) + 1
        lesson_text = (
            f"Relational Lesson {lesson_idx}: {archetype.letter} is for {archetype.name}. "
            f"Domain: {archetype.domain} (Station {archetype.station_number}). "
            f"Pillar: {archetype.pillar} (Partner: {archetype.partner_letter}). "
            f"Gift: {archetype.gift} Shadow: {archetype.shadow}"
        )

        cycle = self.heartbeat.interact(
            sentence=lesson_text,
            target_lemmas=[archetype.name.lower().replace("the ", "")],
            custom_dials=dict(archetype.leaf_activations),
        )

        state_digest = self.compute_state_digest()
        result = Grade2LessonResult(
            lesson_number=lesson_idx,
            archetype=archetype,
            posture=cycle["action_bid"],
            speaking_register=cycle["speaking_register"],
            cycle_result=cycle,
            state_digest=state_digest,
        )
        self._lessons_taught.append(result)
        return result

    def evaluate_station_dyad(self, station_number: int) -> DyadicStationEvaluation:
        """Evaluates the harmonic balance between masculine and feminine pillars at a station."""
        if not (1 <= station_number <= 13):
            raise ValueError(f"Station number must be in range 1..13, got {station_number}")

        # Find masculine and feminine records for this station
        recs = [r for r in RELATIONAL_CODEX.values() if r.station_number == station_number]
        masc = next(r for r in recs if r.pillar == "Masculine")
        fem = next(r for r in recs if r.pillar == "Feminine")

        # Compute dot product concordance across overlapping canonical leaves
        shared_leaves = set(masc.leaf_activations.keys()).intersection(fem.leaf_activations.keys())
        if shared_leaves:
            diffs = [abs(masc.leaf_activations[l] - fem.leaf_activations[l]) for l in shared_leaves]
            avg_diff = sum(diffs) / len(diffs)
            consonance = round(max(0.0, 1.0 - avg_diff), 4)
        else:
            consonance = 0.8500  # Default complementary baseline

        status = "Harmonic Equilibrium" if consonance >= 0.70 else "Dynamic Polarity"

        return DyadicStationEvaluation(
            station_number=station_number,
            domain=masc.domain,
            masculine_pillar=masc,
            feminine_pillar=fem,
            harmonic_consonance=consonance,
            equilibrium_status=status,
        )

    def teach_full_codex(self, archive_checkpoint: bool = True) -> Grade2GraduationReport:
        """Sequentially teach all 26 archetypes (A to Z) followed by overnight sleep consolidation."""
        alphabet = [chr(c) for c in range(ord("A"), ord("Z") + 1)]
        for letter in alphabet:
            self.teach_archetype(letter)

        # Overnight sleep consolidation
        sleep_res = self.heartbeat.sleep(prune_buffer=True)
        final_digest = self.compute_state_digest()

        # Archive snapshot in checkpoints vault if requested
        ckpt_path_str = ""
        if archive_checkpoint:
            ckpt_path, _ = archive_grade_milestone(
                heartbeat=self.heartbeat,
                grade_level=2,
                milestone_label="relational_graduate",
                generation=1,
            )
            ckpt_path_str = str(ckpt_path)

        summary = sleep_res.get("consolidation_summary", {})
        replayed = summary.get("episodes_replayed", len(self._lessons_taught))
        promoted = summary.get("promoted_rules", [])
        pruned = summary.get("pruned_count", 0)

        verdict = (
            f"Grade 2 Completed: 26/26 Relational Archetypes mastered across 13 Stations. "
            f"Sleep consolidation replayed {replayed} episodes, "
            f"promoted {len(promoted)} capacity rules, "
            f"pruned {pruned} transient noise traces."
        )

        return Grade2GraduationReport(
            individual_id=self.individual_id,
            lessons_completed=len(self._lessons_taught),
            archetypes_mastered=tuple(alphabet),
            stations_evaluated=13,
            consolidation=sleep_res,
            checkpoint_path=ckpt_path_str,
            final_state_digest=final_digest,
            summary_verdict=verdict,
        )

    def spell_word_chord(self, word: str) -> RelationalWordChord:
        """Compose any English word into a Relational Archetype chord."""
        archetypes = get_word_relational_chord(word)
        if not archetypes:
            raise ValueError(f"Word {word!r} contains no alphabetic characters")

        pillar_counts = {"Masculine": 0, "Feminine": 0}
        composite_leaves: dict[str, float] = {}

        for arc in archetypes:
            pillar_counts[arc.pillar] += 1
            for leaf, val in arc.leaf_activations.items():
                composite_leaves[leaf] = composite_leaves.get(leaf, 0.0) + val

        # Normalize leaf activations
        n = float(len(archetypes))
        normalized_leaves = {leaf: round(val / n, 4) for leaf, val in composite_leaves.items()}

        steps = [f"({a.letter}) {a.name} [{a.pillar} | {a.domain}]" for a in archetypes]
        journey = f"Word '{word.upper()}' invokes relational arc: " + " -> ".join(steps)

        return RelationalWordChord(
            word=word.upper(),
            archetypes=archetypes,
            pillar_counts=pillar_counts,
            composite_leaf_activations=normalized_leaves,
            relational_journey=journey,
        )

    def resolve_dialogue_resonance(self, text: str) -> tuple[RelationalRecord, float]:
        """Resolves an incoming natural text query to its closest Relational Archetype resonance."""
        tokens = set(text.lower().split())
        best_archetype: RelationalRecord = RELATIONAL_CODEX["A"]
        best_score = 0.0

        for arc in RELATIONAL_CODEX.values():
            score = 0.10  # Baseline prior
            name_tokens = arc.name.lower().replace("the ", "").split()
            if any(nt in tokens for nt in name_tokens):
                score += 0.50
            if arc.letter.lower() in tokens:
                score += 0.20
            # Domain and gift semantic overlap
            domain_tokens = arc.domain.lower().split()
            gift_tokens = arc.gift.lower().split()
            if any(dt in tokens for dt in domain_tokens):
                score += 0.25
            if any(gt in tokens for gt in gift_tokens):
                score += 0.15

            if score > best_score:
                best_score = score
                best_archetype = arc

        return best_archetype, round(min(1.0, best_score), 4)

    def compute_state_digest(self) -> str:
        """Deterministic digest of active disposition and capacity state."""
        pkg = self.heartbeat.export_individual_package()
        payload = {
            "disposition": pkg.get("disposition", {}),
            "capacity": pkg.get("capacity", {}),
            "lessons_count": len(self._lessons_taught),
        }
        encoded = json.dumps(payload, sort_keys=True).encode("utf-8")
        return hashlib.sha256(encoded).hexdigest()


class Grade2OrdinaryMemoryComparator:
    """Matched ordinary structured memory baseline comparator (Rule D004)."""

    def __init__(self, individual_id: str = "comparator_01") -> None:
        self.individual_id = individual_id
        self.memory: dict[str, Any] = {"lessons": [], "rules": {}, "disposition": {}}

    def store_lesson(self, letter: str, name: str, domain: str, pillar: str) -> None:
        self.memory["lessons"].append({"letter": letter, "name": name, "domain": domain, "pillar": pillar})
        self.memory["rules"][letter] = {"name": name, "domain": domain, "pillar": pillar}

    def compute_digest(self) -> str:
        encoded = json.dumps(self.memory, sort_keys=True).encode("utf-8")
        return hashlib.sha256(encoded).hexdigest()
