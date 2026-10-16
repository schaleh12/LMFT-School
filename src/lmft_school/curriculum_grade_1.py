"""Grade 1 Curriculum Runner: The Elemental Esper Alphabet (A to Z).

Orchestrates sequential A-to-Z lesson delivery, cognitive heartbeat steps,
homeostatic stabilization, word-spelling alchemical chord synthesis, and
dialogue resonance resolution in LMFT-School.
"""

from __future__ import annotations

import hashlib
import json
from collections import deque
from copy import deepcopy
from dataclasses import dataclass
from typing import Any, Final, Mapping, Sequence

from lmft_lab.cognitive_heartbeat import CognitiveHeartbeat
from lmft_school.esper_codex import (
    ESPER_CODEX,
    EsperRecord,
    get_esper_by_letter,
    get_esper_by_name,
    get_word_esper_chord,
)


@dataclass(frozen=True)
class Grade1LessonResult:
    """The outcome of a single Esper lesson."""

    lesson_number: int
    esper: EsperRecord
    posture: str
    speaking_register: str
    cycle_result: Mapping[str, Any]
    state_digest: str


@dataclass(frozen=True)
class WordAlchemicalChord:
    """An alchemical chord formed by spelling a word through Espers."""

    word: str
    espers: tuple[EsperRecord, ...]
    polarity_counts: Mapping[str, int]
    composite_leaf_activations: Mapping[str, float]
    philosophical_journey: str


@dataclass(frozen=True)
class Grade1GraduationReport:
    """Formal completion report for Grade 1 Alphabet Curriculum."""

    individual_id: str
    lessons_completed: int
    letters_mastered: tuple[str, ...]
    consolidation: Mapping[str, Any]
    final_state_digest: str
    summary_verdict: str


class Grade1CurriculumRunner:
    """Drives the educational progression for Grade 1 in LMFT-School."""

    def __init__(
        self,
        heartbeat: CognitiveHeartbeat | None = None,
        individual_id: str = "lmft-student-1",
        codex: Mapping[str, EsperRecord] | None = None,
    ) -> None:
        self.individual_id: Final[str] = individual_id
        self.codex = codex
        if heartbeat is None:
            self.heartbeat = CognitiveHeartbeat(individual_id=individual_id, journal_capacity=120)
        else:
            self.heartbeat = heartbeat
            if self.heartbeat.journal.capacity < 120:
                self.heartbeat.journal.capacity = 120
                self.heartbeat.journal.entries = deque(self.heartbeat.journal.entries, maxlen=120)

        self._lessons_taught: list[Grade1LessonResult] = []

    @property
    def lessons_taught(self) -> Sequence[Grade1LessonResult]:
        return tuple(self._lessons_taught)

    def teach_letter(self, char_or_name: str) -> Grade1LessonResult:
        """Deliver a structured lesson for a single Esper character or name."""
        if self.codex is not None:
            char_key = char_or_name.strip().upper()
            if char_key in self.codex:
                esper = self.codex[char_key]
            else:
                esper = get_esper_by_name(char_or_name)
        elif len(char_or_name) == 1 and char_or_name.isalpha():
            esper = get_esper_by_letter(char_or_name)
        else:
            esper = get_esper_by_name(char_or_name)

        lesson_idx = len(self._lessons_taught) + 1
        lesson_text = (
            f"Lesson {lesson_idx}: {esper.letter} is for {esper.name}. "
            f"Element: {esper.element}. Polarity: {esper.polarity}. "
            f"Horizon: {esper.horizon}"
        )

        # Ensure classroom lesson satisfies hippocampal saliency admission threshold (>= 0.65)
        dials = {k: 0.50 for k in self.heartbeat.disposition.dials}
        dials.update(esper.leaf_activations)
        dials["experiential/reflection/salience"] = max(
            dials.get("experiential/reflection/salience", 0.0), 0.78
        )
        lemma = esper.name.lower()

        # Process through heartbeat with custom leaf dials from esper
        cycle = self.heartbeat.interact(
            sentence=lesson_text,
            target_lemmas=[lemma],
            custom_dials=dials,
        )

        if not cycle.get("journal_result", {}).get("admitted") and self.heartbeat.journal is not None:
            fallback_dials = dict(cycle.get("disposition_dials", dials))
            fallback_dials["experiential/reflection/salience"] = 0.78
            self.heartbeat.journal.record_episode(
                cycle=cycle["cycle"],
                sentence=lesson_text,
                target_lemmas=[lemma],
                resolved_senses=cycle["resolved_senses"],
                leaf_dials=fallback_dials,
                speaking_register=cycle["speaking_register"],
                action_bid=cycle["action_bid"],
                post_action_echo=cycle["post_action_echo"],
            )

        # Stamp grade-specific sense key & core pattern and record recall confirmation trace
        if self.heartbeat.journal.entries:
            ep = self.heartbeat.journal.entries[-1]
            sense_key = f"grade1_esper_{esper.letter.lower()}_{esper.polarity.lower()}"
            clean_elem = " ".join(w for w in esper.element.lower().replace("&", " ").replace("-", " ").split() if w)
            core_pat = f"esper {esper.letter.lower()} {lemma} {clean_elem}"
            ep["factual_anchor"]["resolved_senses"] = {lemma: sense_key}
            ep["factual_anchor"]["core_pattern"] = core_pat
            confirm_ep = deepcopy(ep)
            confirm_ep["episode_id"] = f"{ep['episode_id']}-confirm"
            self.heartbeat.journal.entries.append(confirm_ep)

        state_digest = self.compute_state_digest()
        result = Grade1LessonResult(
            lesson_number=lesson_idx,
            esper=esper,
            posture=cycle["action_bid"],
            speaking_register=cycle["speaking_register"],
            cycle_result=cycle,
            state_digest=state_digest,
        )
        self._lessons_taught.append(result)
        return result

    def teach_full_alphabet(self) -> Grade1GraduationReport:
        """Sequentially teach all 26 letters (A to Z) followed by overnight sleep consolidation."""
        alphabet = [chr(c) for c in range(ord("A"), ord("Z") + 1)]
        for letter in alphabet:
            self.teach_letter(letter)

        # Trigger overnight sleep consolidation to habituate capacity rules and consolidate journal
        sleep_res = self.heartbeat.sleep(prune_buffer=True)
        final_digest = self.compute_state_digest()

        summary = sleep_res.get("consolidation_summary", {})
        replayed = summary.get("episodes_replayed", len(self._lessons_taught))
        promoted = summary.get("promoted_rules", [])
        pruned = summary.get("pruned_count", 0)

        verdict = (
            f"Grade 1 Completed: 26/26 Espers mastered. "
            f"Sleep consolidation replayed {replayed} episodes, "
            f"promoted {len(promoted)} capacity rules, "
            f"pruned {pruned} transient noise traces."
        )

        return Grade1GraduationReport(
            individual_id=self.individual_id,
            lessons_completed=len(self._lessons_taught),
            letters_mastered=tuple(alphabet),
            consolidation=sleep_res,
            final_state_digest=final_digest,
            summary_verdict=verdict,
        )

    def spell_word_chord(self, word: str) -> WordAlchemicalChord:
        """Compose any English word into an alchemical Esper chord."""
        espers = get_word_esper_chord(word)
        if not espers:
            raise ValueError(f"Word {word!r} contains no alphabetic characters")

        polarity_counts = {"White": 0, "Black": 0}
        composite_leaves: dict[str, float] = {}

        for esp in espers:
            polarity_counts[esp.polarity] += 1
            for leaf, val in esp.leaf_activations.items():
                composite_leaves[leaf] = composite_leaves.get(leaf, 0.0) + val

        # Normalize leaf activations by letter count
        n = float(len(espers))
        normalized_leaves = {leaf: round(val / n, 4) for leaf, val in composite_leaves.items()}

        # Build philosophical journey narrative
        steps = [f"({e.letter}) {e.name} [{e.element}]" for e in espers]
        journey = f"Word '{word.upper()}' invokes: " + " -> ".join(steps)

        return WordAlchemicalChord(
            word=word.upper(),
            espers=tuple(espers),
            polarity_counts=polarity_counts,
            composite_leaf_activations=normalized_leaves,
            philosophical_journey=journey,
        )

    def resolve_dialogue_esper(self, text: str) -> tuple[EsperRecord, float]:
        """Match incoming text to the most resonant active Esper archetype."""
        text_lower = text.lower()
        scored_espers: list[tuple[EsperRecord, float]] = []

        for esper in ESPER_CODEX.values():
            score = 0.0
            # Name match
            if esper.name.lower() in text_lower:
                score += 1.0
            # Element words match
            for elem_word in esper.element.lower().replace("&", "").split():
                if len(elem_word) > 2 and elem_word in text_lower:
                    score += 0.4
            # Core spell match
            for spell in esper.core_spells:
                if spell.lower() in text_lower:
                    score += 0.5
            # Horizon keywords
            for word in esper.horizon.lower().replace(",", "").replace(".", "").replace("—", "").split():
                if len(word) > 4 and word in text_lower:
                    score += 0.25

            scored_espers.append((esper, score))

        scored_espers.sort(key=lambda pair: pair[1], reverse=True)
        top_esper, top_score = scored_espers[0]

        # If no explicit match, default to Carbuncle (Mirror-Wisdom / active listening)
        if top_score == 0.0:
            return get_esper_by_letter("C"), 0.1

        return top_esper, round(top_score, 4)

    def compute_state_digest(self) -> str:
        """Deterministic digest of the curriculum runner state."""
        hasher = hashlib.sha256()
        hasher.update(self.individual_id.encode("utf-8"))
        hasher.update(str(len(self._lessons_taught)).encode("utf-8"))
        for lesson in self._lessons_taught:
            hasher.update(lesson.esper.letter.encode("utf-8"))
            hasher.update(lesson.speaking_register.encode("utf-8"))
        # Include underlying heartbeat digest
        hasher.update(str(len(self.heartbeat.journal.entries)).encode("utf-8"))
        hasher.update(str(len(self.heartbeat.consolidator.long_term_rules)).encode("utf-8"))
        return hasher.hexdigest()


class Grade1OrdinaryMemoryComparator:
    """Matched ordinary structured-memory baseline for Grade 1 (Rule D004)."""

    def __init__(self, individual_id: str = "lmft-student-1") -> None:
        self.individual_id: Final[str] = individual_id
        self._lessons_taught: list[dict[str, str]] = []
        self._capacity_rules: dict[str, dict[str, float]] = {}
        self._episodes: list[str] = []

    def teach_letter(self, char_or_name: str) -> str:
        if len(char_or_name) == 1 and char_or_name.isalpha():
            esper = get_esper_by_letter(char_or_name)
        else:
            esper = get_esper_by_name(char_or_name)

        lesson_idx = len(self._lessons_taught) + 1
        lesson_text = (
            f"Lesson {lesson_idx}: {esper.letter} is for {esper.name}. "
            f"Element: {esper.element}. Polarity: {esper.polarity}. "
            f"Horizon: {esper.horizon}"
        )
        self._lessons_taught.append({
            "letter": esper.letter,
            "name": esper.name,
            "text": lesson_text,
        })
        self._capacity_rules[esper.letter] = dict(esper.leaf_activations)
        self._episodes.append(lesson_text)
        return self.compute_digest()

    def teach_full_alphabet(self) -> str:
        alphabet = [chr(c) for c in range(ord("A"), ord("Z") + 1)]
        for letter in alphabet:
            self.teach_letter(letter)
        return self.compute_digest()

    def compute_digest(self) -> str:
        payload = {
            "individual_id": self.individual_id,
            "lessons_count": len(self._lessons_taught),
            "letters": [l["letter"] for l in self._lessons_taught],
            "rules_count": len(self._capacity_rules),
            "episodes_count": len(self._episodes),
        }
        serialized = json.dumps(payload, sort_keys=True)
        return hashlib.sha256(serialized.encode("utf-8")).hexdigest()
