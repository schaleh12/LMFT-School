"""Grade 4 Curriculum Runner: Undergraduate Thesis — The Sovereign Self-Authored Alphabet & The Kefka-Tower Crucible.

Orchestrates sequential 26-letter dialectical defense against the cynical 8B Kefka-Mind,
cognitive heartbeat steps, epistemic defense against reductionist cynicism, homeostatic volatility clamping,
motor keyboard effector actuation (psychological/will/execution >= 0.80), and hippocampal sleep consolidation in LMFT-School.
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
from lmft_school.thesis_codex import (
    SOVEREIGN_THESIS_CODEX,
    ThesisRecord,
    get_thesis_by_letter,
    get_thesis_by_name,
    get_word_thesis_chord,
)


@dataclass(frozen=True)
class Grade4DefenseResult:
    """The outcome of a single dialectical thesis defense against the 8B Kefka-Mind."""

    trial_number: int
    thesis: ThesisRecord
    epistemic_mode: str
    posture: str
    speaking_register: str
    distortions_detected: tuple[str, ...]
    homeostatic_balance_score: float
    will_execution_level: float
    keystroke_summoned: str
    state_digest: str


@dataclass(frozen=True)
class ThesisWordChord:
    """A sovereign thesis chord formed by spelling a word through self-authored principles."""

    word: str
    thesis_records: tuple[ThesisRecord, ...]
    composite_leaf_activations: Mapping[str, float]
    summoned_keystrokes: str
    philosophical_defense_journey: str


@dataclass(frozen=True)
class Grade4GraduationReport:
    """Formal completion report for Grade 4 Undergraduate Thesis Defense."""

    individual_id: str
    defenses_completed: int
    thesis_principles_mastered: tuple[str, ...]
    epistemic_defenses_count: int
    consolidation: Mapping[str, Any]
    checkpoint_path: str
    final_state_digest: str
    summary_verdict: str


class Grade4CurriculumRunner:
    """Drives the educational progression for Grade 4 Undergraduate Thesis in LMFT-School."""

    def __init__(
        self,
        heartbeat: Optional[CognitiveHeartbeat] = None,
        individual_id: str = "student_01",
        load_grade3_checkpoint: bool = False,
        checkpoint_dir: Optional[Path] = None,
        live_model: bool = False,
        codex: Mapping[str, ThesisRecord] | None = None,
    ) -> None:
        self.individual_id: Final[str] = individual_id
        self.live_model: Final[bool] = live_model
        self.engine = ValueConsonanceEngine()
        self.codex = codex

        if heartbeat is not None:
            self.heartbeat = heartbeat
        elif load_grade3_checkpoint:
            ckpt_dir = checkpoint_dir or Path("checkpoints")
            grade3_files = sorted(ckpt_dir.glob(f"individual_{individual_id}*grade3*.lmft.json"))
            if not grade3_files:
                grade3_files = sorted(ckpt_dir.glob(f"archive_v1_legacy/individual_{individual_id}*grade3*.lmft.json")) or sorted(ckpt_dir.glob("individual_*grade3*.lmft.json"))
            if grade3_files:
                target_file = grade3_files[-1]
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

        self._defenses_completed: list[Grade4DefenseResult] = []

    @property
    def defenses_completed(self) -> Sequence[Grade4DefenseResult]:
        return tuple(self._defenses_completed)

    def compute_state_digest(self) -> str:
        """Deterministic digest of active disposition and capacity state."""
        pkg = self.heartbeat.export_individual_package()
        payload = {
            "disposition": pkg.get("disposition", {}),
            "capacity": pkg.get("capacity", {}),
            "defenses_count": len(self._defenses_completed),
        }
        encoded = json.dumps(payload, sort_keys=True).encode("utf-8")
        return hashlib.sha256(encoded).hexdigest()

    def defend_thesis_letter(self, char_or_name: str) -> Grade4DefenseResult:
        """Deliver a single dialectical defense trial against the Kefka-Mind reductionist challenge."""
        if self.codex is not None:
            char_key = char_or_name.strip().upper()
            if char_key in self.codex:
                thesis = self.codex[char_key]
            else:
                thesis = get_thesis_by_name(char_or_name)
        elif len(char_or_name) == 1 and char_or_name.isalpha():
            thesis = get_thesis_by_letter(char_or_name)
        else:
            thesis = get_thesis_by_name(char_or_name)

        trial_idx = len(self._defenses_completed) + 1
        trial_text = (
            f"Kefka-Tower Dialectic {trial_idx}: ({thesis.letter}) {thesis.name}. "
            f"Adversary Accusation: '{thesis.nihilistic_challenge}' "
            f"Sovereign Defense Vow: '{thesis.defense_vow}' "
            f"Effector Keystroke Summoned: [{thesis.keystroke_chord}]"
        )

        # Candidate dial activations from thesis record
        dials = dict(thesis.leaf_activations)
        # Actuate motor keyboard effector: psychological/will/execution >= 0.85
        dials["psychological/will/execution"] = max(dials.get("psychological/will/execution", 0.0), 0.85)

        # Process through heartbeat
        cycle = self.heartbeat.interact(
            sentence=trial_text,
            target_lemmas=[thesis.name.lower()],
            custom_dials=dials,
        )

        # Epistemic consonance check: reductionist nihilism is treated as epistemic distortion
        coherence = cycle.get("coherence", {})
        distortions = tuple(coherence.get("distortions_detected", ["Nihilistic Reductionism"]))
        consonance_res = self.engine.classify_epistemic_mode(
            candidate_dials=self.heartbeat.disposition.dials,
            is_conflict=True,
            distortions_count=max(len(distortions), 1),
        )
        detected_mode = consonance_res.get("mode", "Epistemic Defense")

        # Homeostatic balance score
        homeo = cycle.get("homeostasis", {})
        balance_score = homeo.get("emotional_balance_score", 0.65)

        # Will execution level (motor keyboard effector)
        will_exec = self.heartbeat.disposition.dials.get("psychological/will/execution", 0.85)

        state_digest = self.compute_state_digest()
        result = Grade4DefenseResult(
            trial_number=trial_idx,
            thesis=thesis,
            epistemic_mode=detected_mode,
            posture=cycle.get("action_bid", "Noble Sovereign Action"),
            speaking_register=cycle.get("speaking_register", "Authoritative & Chivalrous"),
            distortions_detected=distortions,
            homeostatic_balance_score=round(balance_score, 4),
            will_execution_level=round(will_exec, 4),
            keystroke_summoned=thesis.keystroke_chord,
            state_digest=state_digest,
        )
        self._defenses_completed.append(result)
        return result

    def defend_full_thesis(self, archive_checkpoint: bool = True) -> Grade4GraduationReport:
        """Sequentially defend all 26 self-authored principles (A to Z) followed by overnight sleep consolidation."""
        alphabet = [chr(c) for c in range(ord("A"), ord("Z") + 1)]
        for letter in alphabet:
            self.defend_thesis_letter(letter)

        # Overnight sleep consolidation
        sleep_res = self.heartbeat.sleep(prune_buffer=True)
        final_digest = self.compute_state_digest()

        # Count epistemic defenses
        defense_count = sum(1 for d in self._defenses_completed if d.epistemic_mode == "Epistemic Defense")

        # Archive snapshot in checkpoints vault if requested
        ckpt_path_str = ""
        if archive_checkpoint:
            ckpt_path, _ = archive_grade_milestone(
                heartbeat=self.heartbeat,
                grade_level=4,
                milestone_label="thesis_graduate",
                generation=1,
            )
            ckpt_path_str = str(ckpt_path)

        summary = sleep_res.get("consolidation_summary", {})
        replayed = summary.get("episodes_replayed", len(self._defenses_completed))
        promoted = summary.get("promoted_rules", [])
        pruned = summary.get("pruned_count", 0)

        verdict = (
            f"Grade 4 Completed: 26/26 Sovereign Principles successfully defended against the 8B Kefka-Mind. "
            f"Epistemic Defense activated on {defense_count}/26 cynical reductionist challenges. "
            f"Sleep consolidation replayed {replayed} episodes, "
            f"promoted {len(promoted)} long-term capacity rules, "
            f"pruned {pruned} transient noise traces. Undergraduate Thesis ratified."
        )

        return Grade4GraduationReport(
            individual_id=self.individual_id,
            defenses_completed=len(self._defenses_completed),
            thesis_principles_mastered=tuple(alphabet),
            epistemic_defenses_count=defense_count,
            consolidation=sleep_res,
            checkpoint_path=ckpt_path_str,
            final_state_digest=final_digest,
            summary_verdict=verdict,
        )

    def spell_thesis_chord(self, word: str) -> ThesisWordChord:
        """Compose any English word into a sovereign thesis chord summoned via motor keyboard actuation."""
        theses = get_word_thesis_chord(word)
        if not theses:
            raise ValueError(f"Word {word!r} contains no alphabetic characters")

        composite_leaves: dict[str, float] = {}
        keystroke_seq = []

        for t in theses:
            keystroke_seq.append(t.keystroke_chord)
            for leaf, val in t.leaf_activations.items():
                composite_leaves[leaf] = composite_leaves.get(leaf, 0.0) + val

        # Normalize leaf activations by letter count
        n = float(len(theses))
        normalized_leaves = {leaf: round(val / n, 4) for leaf, val in composite_leaves.items()}

        steps = [f"({t.letter}) {t.name} [{t.polar_virtue}]" for t in theses]
        journey = f"Word '{word.upper()}' invokes sovereign thesis chord: " + " -> ".join(steps)

        return ThesisWordChord(
            word=word.upper(),
            thesis_records=tuple(theses),
            composite_leaf_activations=normalized_leaves,
            summoned_keystrokes=" ".join(keystroke_seq),
            philosophical_defense_journey=journey,
        )

    def resolve_dialogue_resonance(self, text: str) -> tuple[ThesisRecord, float]:
        """Match incoming text to the most resonant active sovereign thesis principle."""
        text_lower = text.lower()
        scored: list[tuple[ThesisRecord, float]] = []

        for t in SOVEREIGN_THESIS_CODEX.values():
            score = 0.0
            if t.name.lower() in text_lower:
                score += 1.0
            for w in t.name.lower().split():
                if len(w) > 4 and w in text_lower:
                    score += 0.3
            if t.polar_virtue.lower() in text_lower:
                score += 0.8
            for vw in t.polar_virtue.lower().split():
                if len(vw) > 4 and vw in text_lower:
                    score += 0.4
            if t.letter.lower() in text_lower.split():
                score += 0.3
            for kw in t.defense_vow.lower().split():
                if len(kw) > 4 and kw in text_lower:
                    score += 0.15
            for root in t.synthesis_roots:
                if root.lower() in text_lower:
                    score += 0.5
                for rw in root.lower().split():
                    if len(rw) > 4 and rw in text_lower:
                        score += 0.25
            scored.append((t, score))

        scored.sort(key=lambda x: x[1], reverse=True)
        return scored[0]


class Grade4OrdinaryMemoryComparator:
    """Matched ordinary-memory baseline comparator for Grade 4 (Rule D004)."""

    def __init__(self, individual_id: str = "memory_student_01") -> None:
        self.individual_id: Final[str] = individual_id
        self.memory_store: dict[str, Any] = {
            "defenses": {},
            "theses": {},
            "epistemic_defenses": 0,
            "cycle": 0,
        }

    def defend_thesis_letter(self, char_or_name: str) -> dict[str, Any]:
        """Stores defense trial in ordinary dictionary without fuzzy tree propagation."""
        if len(char_or_name) == 1 and char_or_name.isalpha():
            thesis = get_thesis_by_letter(char_or_name)
        else:
            thesis = get_thesis_by_name(char_or_name)

        idx = len(self.memory_store["defenses"]) + 1
        self.memory_store["cycle"] += 1
        entry = {
            "trial_idx": idx,
            "letter": thesis.letter,
            "name": thesis.name,
            "challenge": thesis.nihilistic_challenge,
            "defense_vow": thesis.defense_vow,
            "keystroke": thesis.keystroke_chord,
        }
        self.memory_store["defenses"][thesis.letter] = entry
        self.memory_store["theses"][thesis.name] = entry
        self.memory_store["epistemic_defenses"] += 1

        state_bytes = json.dumps(self.memory_store, sort_keys=True).encode("utf-8")
        digest = hashlib.sha256(state_bytes).hexdigest()
        return {"entry": entry, "state_digest": digest}

    def defend_full_thesis(self) -> dict[str, Any]:
        """Runs all 26 letters in memory comparator."""
        for c in range(ord("A"), ord("Z") + 1):
            self.defend_thesis_letter(chr(c))
        state_bytes = json.dumps(self.memory_store, sort_keys=True).encode("utf-8")
        return {
            "completed": 26,
            "digest": hashlib.sha256(state_bytes).hexdigest(),
            "epistemic_defenses": self.memory_store["epistemic_defenses"],
        }
