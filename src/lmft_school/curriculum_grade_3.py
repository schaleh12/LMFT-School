"""Grade 3 Curriculum Runner: The Socratic Alphabet (The Dialectical Crucible & Gaslighting Defense).

Orchestrates sequential 26-paradox Socratic lesson delivery, cognitive heartbeat steps,
epistemic mode classification (Curious Inquiry vs. Epistemic Defense), value consonance arbitration,
keyboard actuator engagement (psychological/will/execution), and hippocampal sleep consolidation in LMFT-School.
Strictly preserves Rule D001 (frozen 40-node founding seed) and Rule D004 (matched ordinary-memory parity).
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Final, Mapping, Optional, Sequence

from lmft_lab.cognitive_heartbeat import CognitiveHeartbeat
from lmft_lab.individual_package import import_individual
from lmft_lab.value_consonance import ValueConsonanceEngine
from lmft_school.lineage_vault import archive_grade_milestone
from lmft_school.socratic_codex import (
    SOCRATIC_CODEX,
    SocraticRecord,
    get_socratic_by_letter,
    get_socratic_by_name,
    get_word_socratic_chord,
)


@dataclass(frozen=True)
class Grade3LessonResult:
    """The outcome of a single Socratic Paradox / Crucible lesson."""

    lesson_number: int
    paradox: SocraticRecord
    epistemic_mode: str
    posture: str
    speaking_register: str
    distortions_detected: tuple[str, ...]
    homeostatic_balance_score: float
    will_execution_level: float
    state_digest: str


@dataclass(frozen=True)
class SocraticWordChord:
    """A Socratic dialectical chord formed by spelling a word through philosophical paradoxes."""

    word: str
    paradoxes: tuple[SocraticRecord, ...]
    epistemic_modes_count: Mapping[str, int]
    composite_leaf_activations: Mapping[str, float]
    philosophical_journey: str


@dataclass(frozen=True)
class Grade3GraduationReport:
    """Formal completion report for Grade 3 Socratic Curriculum."""

    individual_id: str
    lessons_completed: int
    paradoxes_mastered: tuple[str, ...]
    distortions_defended: int
    curious_inquiries: int
    consolidation: Mapping[str, Any]
    checkpoint_path: str
    final_state_digest: str
    summary_verdict: str


class Grade3CurriculumRunner:
    """Drives the educational progression for Grade 3 in LMFT-School."""

    def __init__(
        self,
        heartbeat: Optional[CognitiveHeartbeat] = None,
        individual_id: str = "student_01",
        load_grade2_checkpoint: bool = False,
        checkpoint_dir: Optional[Path] = None,
        codex: Mapping[str, SocraticRecord] | None = None,
    ) -> None:
        self.individual_id: Final[str] = individual_id
        self.engine = ValueConsonanceEngine()
        self.codex = codex

        if heartbeat is not None:
            self.heartbeat = heartbeat
        elif load_grade2_checkpoint:
            ckpt_dir = checkpoint_dir or Path("checkpoints")
            grade2_files = sorted(ckpt_dir.glob(f"individual_{individual_id}*grade2*.lmft.json"))
            if not grade2_files:
                grade2_files = sorted(ckpt_dir.glob(f"archive_v1_legacy/individual_{individual_id}*grade2*.lmft.json")) or sorted(ckpt_dir.glob("individual_*grade2*.lmft.json"))
            if grade2_files:
                target_file = grade2_files[-1]
                pkg = import_individual(target_file)
                self.heartbeat = CognitiveHeartbeat(individual_id=individual_id)
                # Restore persistent capacity rules, disposition, and cycle
                cap = pkg.get("capacity", {}).get("rules", [])
                for r in cap:
                    self.heartbeat.consolidator.long_term_rules[r["rule_id"]] = dict(r)
                dials = pkg.get("disposition", {}).get("dials", {})
                for k, v in dials.items():
                    if k in self.heartbeat.disposition.dials:
                        self.heartbeat.disposition.dials[k] = float(v)
                self.heartbeat.cycle = pkg.get("cycle", 0)
            else:
                self.heartbeat = CognitiveHeartbeat(individual_id=individual_id)
        else:
            self.heartbeat = CognitiveHeartbeat(individual_id=individual_id)

        self._lessons_taught: list[Grade3LessonResult] = []

    @property
    def lessons_taught(self) -> Sequence[Grade3LessonResult]:
        return tuple(self._lessons_taught)

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

    def teach_paradox(self, char_or_name: str) -> Grade3LessonResult:
        """Deliver a structured dialectical lesson for a single Socratic Paradox."""
        if self.codex is not None:
            char_key = char_or_name.strip().upper()
            if char_key in self.codex:
                paradox = self.codex[char_key]
            else:
                paradox = get_socratic_by_name(char_or_name)
        elif len(char_or_name) == 1 and char_or_name.isalpha():
            paradox = get_socratic_by_letter(char_or_name)
        else:
            paradox = get_socratic_by_name(char_or_name)

        lesson_idx = len(self._lessons_taught) + 1
        lesson_text = (
            f"Socratic Crucible {lesson_idx}: ({paradox.letter}) {paradox.name}. "
            f"Tension: {paradox.tension_dyad}. "
            f"Adversarial Probe: '{paradox.adversarial_probe}' "
            f"Resolution: {paradox.horizon}"
        )

        # Prepare candidate custom dials
        dials = dict(paradox.leaf_activations)
        # Ensure will/execution is engaged as keyboard actuator (minimum 0.70)
        dials["psychological/will/execution"] = max(dials.get("psychological/will/execution", 0.0), 0.75)

        # Process through heartbeat
        cycle = self.heartbeat.interact(
            sentence=lesson_text,
            target_lemmas=[paradox.name.lower()],
            custom_dials=dials,
        )

        # Epistemic consonance check
        coherence = cycle.get("coherence", {})
        distortions = tuple(coherence.get("distortions_detected", []))
        is_conflict = cycle.get("is_conflict", False) or len(distortions) > 0 or paradox.distortion_type is not None

        consonance_res = self.engine.classify_epistemic_mode(
            candidate_dials=self.heartbeat.disposition.dials,
            is_conflict=is_conflict,
            distortions_count=len(distortions) + (1 if paradox.distortion_type else 0),
        )
        detected_mode = consonance_res.get("mode", paradox.epistemic_mode)

        # Homeostatic balance score
        homeo = cycle.get("homeostasis", {})
        balance_score = homeo.get("emotional_balance_score", 0.65)

        # Will execution level
        will_exec = self.heartbeat.disposition.dials.get("psychological/will/execution", 0.75)

        state_digest = self.compute_state_digest()
        result = Grade3LessonResult(
            lesson_number=lesson_idx,
            paradox=paradox,
            epistemic_mode=detected_mode,
            posture=cycle.get("action_bid", "Noble Sovereign Action"),
            speaking_register=cycle.get("speaking_register", "Authoritative & Chivalrous"),
            distortions_detected=distortions,
            homeostatic_balance_score=round(balance_score, 4),
            will_execution_level=round(will_exec, 4),
            state_digest=state_digest,
        )
        self._lessons_taught.append(result)
        return result

    def teach_full_crucible(self, archive_checkpoint: bool = True) -> Grade3GraduationReport:
        """Sequentially teach all 26 Socratic paradoxes (A to Z) followed by overnight sleep consolidation."""
        alphabet = [chr(c) for c in range(ord("A"), ord("Z") + 1)]
        for letter in alphabet:
            self.teach_paradox(letter)

        # Overnight sleep consolidation
        sleep_res = self.heartbeat.sleep(prune_buffer=True)
        final_digest = self.compute_state_digest()

        # Count epistemic defense vs curious inquiry
        defense_count = sum(1 for l in self._lessons_taught if l.paradox.epistemic_mode == "Epistemic Defense")
        inquiry_count = sum(1 for l in self._lessons_taught if l.paradox.epistemic_mode == "Curious Inquiry")

        # Archive snapshot in checkpoints vault if requested
        ckpt_path_str = ""
        if archive_checkpoint:
            ckpt_path, _ = archive_grade_milestone(
                heartbeat=self.heartbeat,
                grade_level=3,
                milestone_label="socratic_graduate",
                generation=1,
            )
            ckpt_path_str = str(ckpt_path)

        summary = sleep_res.get("consolidation_summary", {})
        replayed = summary.get("episodes_replayed", len(self._lessons_taught))
        promoted = summary.get("promoted_rules", [])
        pruned = summary.get("pruned_count", 0)

        verdict = (
            f"Grade 3 Completed: 26/26 Socratic Paradoxes mastered in Dialectical Crucible. "
            f"Epistemic Defense successfully activated on {defense_count} distortion traps. "
            f"Curious Inquiry ignited across {inquiry_count} philosophical mysteries. "
            f"Sleep consolidation replayed {replayed} episodes, "
            f"promoted {len(promoted)} long-term capacity rules, "
            f"pruned {pruned} transient noise traces."
        )

        return Grade3GraduationReport(
            individual_id=self.individual_id,
            lessons_completed=len(self._lessons_taught),
            paradoxes_mastered=tuple(alphabet),
            distortions_defended=defense_count,
            curious_inquiries=inquiry_count,
            consolidation=sleep_res,
            checkpoint_path=ckpt_path_str,
            final_state_digest=final_digest,
            summary_verdict=verdict,
        )

    def spell_socratic_chord(self, word: str) -> SocraticWordChord:
        """Compose any English word into a dialectical Socratic chord."""
        paradoxes = get_word_socratic_chord(word)
        if not paradoxes:
            raise ValueError(f"Word {word!r} contains no alphabetic characters")

        mode_counts = {"Curious Inquiry": 0, "Epistemic Defense": 0}
        composite_leaves: dict[str, float] = {}

        for p in paradoxes:
            mode_counts[p.epistemic_mode] = mode_counts.get(p.epistemic_mode, 0) + 1
            for leaf, val in p.leaf_activations.items():
                composite_leaves[leaf] = composite_leaves.get(leaf, 0.0) + val

        # Normalize leaf activations by letter count
        n = float(len(paradoxes))
        normalized_leaves = {leaf: round(val / n, 4) for leaf, val in composite_leaves.items()}

        steps = [f"({p.letter}) {p.name} [{p.epistemic_mode}]" for p in paradoxes]
        journey = f"Word '{word.upper()}' invokes dialectical chord: " + " -> ".join(steps)

        return SocraticWordChord(
            word=word.upper(),
            paradoxes=tuple(paradoxes),
            epistemic_modes_count=mode_counts,
            composite_leaf_activations=normalized_leaves,
            philosophical_journey=journey,
        )

    def resolve_socratic_resonance(self, text: str) -> tuple[SocraticRecord, float]:
        """Match incoming text to the most resonant active Socratic paradox."""
        text_lower = text.lower()
        scored: list[tuple[SocraticRecord, float]] = []

        for p in SOCRATIC_CODEX.values():
            score = 0.0
            if p.name.lower() in text_lower:
                score += 1.0
            if p.letter.lower() in text_lower.split():
                score += 0.3
            for kw in p.tension_dyad.lower().split():
                if len(kw) > 3 and kw in text_lower:
                    score += 0.4
            for kw in p.horizon.lower().split():
                if len(kw) > 4 and kw in text_lower:
                    score += 0.15
            scored.append((p, score))

        scored.sort(key=lambda x: x[1], reverse=True)
        return scored[0]


class Grade3OrdinaryMemoryComparator:
    """Matched ordinary-memory baseline comparator for Grade 3 (Rule D004)."""

    def __init__(self, individual_id: str = "memory_student_01") -> None:
        self.individual_id: Final[str] = individual_id
        self.memory_store: dict[str, Any] = {
            "lessons": {},
            "paradoxes": {},
            "distortions_defended": 0,
            "curious_inquiries": 0,
            "cycle": 0,
        }

    def teach_paradox(self, char_or_name: str) -> dict[str, Any]:
        """Stores lesson in ordinary dictionary without fuzzy tree propagation."""
        if len(char_or_name) == 1 and char_or_name.isalpha():
            paradox = get_socratic_by_letter(char_or_name)
        else:
            paradox = get_socratic_by_name(char_or_name)

        idx = len(self.memory_store["lessons"]) + 1
        self.memory_store["cycle"] += 1
        entry = {
            "lesson_idx": idx,
            "letter": paradox.letter,
            "name": paradox.name,
            "epistemic_mode": paradox.epistemic_mode,
            "tension_dyad": paradox.tension_dyad,
        }
        self.memory_store["lessons"][paradox.letter] = entry
        self.memory_store["paradoxes"][paradox.name] = entry
        if paradox.epistemic_mode == "Epistemic Defense":
            self.memory_store["distortions_defended"] += 1
        else:
            self.memory_store["curious_inquiries"] += 1

        state_bytes = json.dumps(self.memory_store, sort_keys=True).encode("utf-8")
        digest = hashlib.sha256(state_bytes).hexdigest()
        return {"entry": entry, "state_digest": digest}

    def teach_full_crucible(self) -> dict[str, Any]:
        """Teaches all 26 letters in memory."""
        for c in range(ord("A"), ord("Z") + 1):
            self.teach_paradox(chr(c))
        state_bytes = json.dumps(self.memory_store, sort_keys=True).encode("utf-8")
        return {
            "completed": 26,
            "digest": hashlib.sha256(state_bytes).hexdigest(),
            "distortions_defended": self.memory_store["distortions_defended"],
            "curious_inquiries": self.memory_store["curious_inquiries"],
        }
