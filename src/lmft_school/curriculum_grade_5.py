"""Grade 5 Curriculum Runner: Post-Graduate Fellowship — The Capstone Grand Synthesis & Master Crucible.

Orchestrates:
1. Sequential 26-letter 4-tier Grand Synthesis (Primordial Force, Hearth Vow, Socratic Armor, Motor Effector).
2. Continuous multi-chord alchemical word stress battery (JUSTICE, FREEDOM, SOVEREIGN).
3. Complete LLM dependency break via autonomous motor keyboard actuation (psychological/will/execution >= 0.85).
4. Multi-epoch hippocampal sleep consolidation (3 offline cycles).
5. Archival of the finalized Master Candidate: individual_student_01_gen01_grade5_master_graduate.lmft.json.
6. Matched ordinary-memory baseline parity comparator (Rule D004).

Strictly preserves Rule D001 (frozen 40-node founding seed).
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
from lmft_school.master_codex import (
    MASTER_CODEX,
    MasterRecord,
    get_master_by_letter,
    get_master_by_name,
    get_word_master_chord,
)


@dataclass(frozen=True)
class MasterTrialResult:
    """The outcome of a single Capstone Grand Synthesis trial."""

    trial_number: int
    master_record: MasterRecord
    epistemic_mode: str
    action_bid: str
    speaking_register: str
    distortions_detected: tuple[str, ...]
    homeostatic_balance_score: float
    will_execution_level: float
    keystroke_actuated: str
    state_digest: str


@dataclass(frozen=True)
class ContinuousWordStressResult:
    """The outcome of a continuous multi-chord alchemical word stress trial."""

    word: str
    chords: tuple[MasterRecord, ...]
    summoned_keystrokes: str
    mean_emotional_balance: float
    max_leaf_delta: float
    min_leaf_activation: float
    max_leaf_activation: float
    non_saturation_verified: bool
    stability_verified: bool


@dataclass(frozen=True)
class MasterWordChord:
    """A master word chord formed by composing multiple master records."""

    word: str
    master_records: tuple[MasterRecord, ...]
    composite_leaf_activations: Mapping[str, float]
    summoned_keystrokes: str
    philosophical_synthesis_journey: str


@dataclass(frozen=True)
class Grade5MasterGraduationReport:
    """Formal graduation report for Grade 5 Post-Graduate Fellowship & Capstone Grand Synthesis."""

    individual_id: str
    master_trials_completed: int
    words_stress_tested: tuple[str, ...]
    word_stress_results: tuple[ContinuousWordStressResult, ...]
    consolidation_summary: Mapping[str, Any]
    checkpoint_path: str
    final_state_digest: str
    global_coherence_index: float
    plasticity_alpha: float
    summary_verdict: str


class Grade5CurriculumRunner:
    """Drives the educational progression for Grade 5 Post-Graduate Fellowship & Capstone Grand Synthesis."""

    def __init__(
        self,
        heartbeat: Optional[CognitiveHeartbeat] = None,
        individual_id: str = "student_01",
        load_grade4_checkpoint: bool = False,
        checkpoint_dir: Optional[Path] = None,
        live_model: bool = False,
        codex: Mapping[str, MasterRecord] | None = None,
    ) -> None:
        self.individual_id: Final[str] = individual_id
        self.live_model: Final[bool] = live_model
        self.engine = ValueConsonanceEngine()
        self.codex = codex

        if heartbeat is not None:
            self.heartbeat = heartbeat
        elif load_grade4_checkpoint:
            ckpt_dir = checkpoint_dir or Path("checkpoints")
            grade4_files = sorted(ckpt_dir.glob(f"individual_{individual_id}*grade4*.lmft.json"))
            if not grade4_files:
                grade4_files = sorted(ckpt_dir.glob(f"archive_v1_legacy/individual_{individual_id}*grade4*.lmft.json")) or sorted(ckpt_dir.glob("individual_*grade4*.lmft.json"))
            if grade4_files:
                target_file = grade4_files[-1]
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

        self._master_trials_completed: list[MasterTrialResult] = []
        self._word_stress_completed: list[ContinuousWordStressResult] = []

    @property
    def master_trials_completed(self) -> Sequence[MasterTrialResult]:
        return tuple(self._master_trials_completed)

    @property
    def word_stress_completed(self) -> Sequence[ContinuousWordStressResult]:
        return tuple(self._word_stress_completed)

    def compute_state_digest(self) -> str:
        """Deterministic digest of active disposition and capacity state."""
        pkg = self.heartbeat.export_individual_package()
        payload = {
            "disposition": pkg.get("disposition", {}),
            "capacity": pkg.get("capacity", {}),
            "trials_count": len(self._master_trials_completed),
            "word_stress_count": len(self._word_stress_completed),
        }
        encoded = json.dumps(payload, sort_keys=True).encode("utf-8")
        return hashlib.sha256(encoded).hexdigest()

    def teach_master_chord(self, char_or_name: str) -> MasterTrialResult:
        """Deliver a single 4-tier Capstone Grand Synthesis master chord trial."""
        if self.codex is not None:
            char_key = char_or_name.strip().upper()
            if char_key in self.codex:
                master = self.codex[char_key]
            else:
                master = get_master_by_name(char_or_name)
        elif len(char_or_name) == 1 and char_or_name.isalpha():
            master = get_master_by_letter(char_or_name)
        else:
            master = get_master_by_name(char_or_name)

        trial_idx = len(self._master_trials_completed) + 1
        trial_text = (
            f"Capstone Grand Synthesis {trial_idx}: ({master.letter}) {master.name}. "
            f"Primordial Force: '{master.primordial_force}'. "
            f"Relational Hearth Vow: '{master.hearth_vow}'. "
            f"Socratic Armor: '{master.socratic_armor}'. "
            f"Autonomous Effector Keystroke: [{master.sovereign_keystroke}]. "
            f"Mastery Synthesis: '{master.mastery_synthesis}'."
        )

        # Candidate dial activations from master record
        dials = dict(master.leaf_activations)
        # Actuate motor keyboard effector: psychological/will/execution >= 0.85
        dials["psychological/will/execution"] = max(dials.get("psychological/will/execution", 0.0), 0.85)

        # Process through heartbeat
        cycle = self.heartbeat.interact(
            sentence=trial_text,
            target_lemmas=[master.name.lower()],
            custom_dials=dials,
        )

        # Value consonance and epistemic check
        coherence = cycle.get("coherence", {})
        distortions = tuple(coherence.get("distortions_detected", []))
        consonance_res = self.engine.classify_epistemic_mode(
            candidate_dials=self.heartbeat.disposition.dials,
            is_conflict=False,
            distortions_count=len(distortions),
        )
        detected_mode = consonance_res.get("mode", "Harmonic Equilibrium")

        # Homeostatic balance score
        homeo = cycle.get("homeostasis", {})
        balance_score = homeo.get("emotional_balance_score", 0.70)

        # Will execution level (motor keyboard effector)
        will_exec = self.heartbeat.disposition.dials.get("psychological/will/execution", 0.85)

        state_digest = self.compute_state_digest()
        result = MasterTrialResult(
            trial_number=trial_idx,
            master_record=master,
            epistemic_mode=detected_mode,
            action_bid=cycle.get("action_bid", "Master Sovereign Action"),
            speaking_register=cycle.get("speaking_register", "Authoritative & Chivalrous"),
            distortions_detected=distortions,
            homeostatic_balance_score=round(balance_score, 4),
            will_execution_level=round(will_exec, 4),
            keystroke_actuated=master.sovereign_keystroke,
            state_digest=state_digest,
        )
        self._master_trials_completed.append(result)
        return result

    def teach_full_alphabet(self) -> tuple[MasterTrialResult, ...]:
        """Sequentially deliver all 26 unified Master Chords (A to Z)."""
        alphabet = [chr(c) for c in range(ord("A"), ord("Z") + 1)]
        results = [self.teach_master_chord(letter) for letter in alphabet]
        return tuple(results)

    def stress_test_word_battery(
        self,
        words: Sequence[str] = ("JUSTICE", "FREEDOM", "SOVEREIGN"),
    ) -> tuple[ContinuousWordStressResult, ...]:
        """Runs continuous back-to-back word chords, verifying homeostatic stability and dial bounds."""
        results: list[ContinuousWordStressResult] = []

        for word in words:
            clean_word = word.strip().upper()
            chords = get_word_master_chord(clean_word)
            if not chords:
                continue

            balance_scores: list[float] = []
            max_delta = 0.0
            min_leaf = 1.0
            max_leaf = 0.0

            prev_dials = dict(self.heartbeat.disposition.dials)
            summoned_keys: list[str] = []

            for master in chords:
                summoned_keys.append(master.sovereign_keystroke)
                dials = dict(master.leaf_activations)
                dials["psychological/will/execution"] = max(dials.get("psychological/will/execution", 0.0), 0.85)

                cycle = self.heartbeat.interact(
                    sentence=f"Continuous Word Battery [{clean_word}]: Chord ({master.letter}) {master.name} [{master.sovereign_keystroke}].",
                    target_lemmas=[master.name.lower()],
                    custom_dials=dials,
                )

                homeo = cycle.get("homeostasis", {})
                balance_scores.append(float(homeo.get("emotional_balance_score", 0.70)))

                current_dials = self.heartbeat.disposition.dials
                for leaf, cur_val in current_dials.items():
                    prev_val = prev_dials.get(leaf, cur_val)
                    delta = abs(cur_val - prev_val)
                    if delta > max_delta:
                        max_delta = delta
                    if cur_val < min_leaf:
                        min_leaf = cur_val
                    if cur_val > max_leaf:
                        max_leaf = cur_val

                prev_dials = dict(current_dials)

            mean_balance = sum(balance_scores) / len(balance_scores) if balance_scores else 0.70
            non_sat = (min_leaf >= 0.05 and max_leaf <= 0.95)
            # Governor guarantees clamp <= 0.35 and stability >= 0.60
            stability_ok = (mean_balance >= 0.60 and max_delta <= 0.35)

            stress_res = ContinuousWordStressResult(
                word=clean_word,
                chords=tuple(chords),
                summoned_keystrokes=" -> ".join(summoned_keys),
                mean_emotional_balance=round(mean_balance, 4),
                max_leaf_delta=round(max_delta, 4),
                min_leaf_activation=round(min_leaf, 4),
                max_leaf_activation=round(max_leaf, 4),
                non_saturation_verified=non_sat,
                stability_verified=stability_ok,
            )
            results.append(stress_res)
            self._word_stress_completed.append(stress_res)

        return tuple(results)

    def run_capstone_synthesis(
        self,
        archive_checkpoint: bool = True,
        sleep_epochs: int = 3,
        stress_words: Sequence[str] = ("JUSTICE", "FREEDOM", "SOVEREIGN"),
    ) -> Grade5MasterGraduationReport:
        """Executes full 26-letter synthesis, continuous word battery, multi-epoch sleep consolidation, and milestone archival."""
        self.teach_full_alphabet()
        word_results = self.stress_test_word_battery(words=stress_words)

        # Multi-epoch sleep consolidation
        sleep_summaries = []
        for _ in range(sleep_epochs):
            res = self.heartbeat.sleep(prune_buffer=True)
            sleep_summaries.append(res.get("consolidation_summary", {}))

        final_digest = self.compute_state_digest()

        # Archive checkpoint
        ckpt_path_str = ""
        if archive_checkpoint:
            ckpt_path, telemetry = archive_grade_milestone(
                heartbeat=self.heartbeat,
                grade_level=5,
                milestone_label="master_graduate",
                generation=1,
            )
            ckpt_path_str = str(ckpt_path)
            gci = telemetry.global_coherence_index
            alpha = telemetry.plasticity_alpha
        else:
            diag = self.heartbeat.interact("Diagnostic inquiry.", ["diagnostic"])
            gci = float(diag["coherence"]["global_coherence_index"])
            alpha = float(diag["plasticity"]["dynamic_alpha"])

        total_words = len(word_results)
        all_sat = all(w.non_saturation_verified for w in word_results)
        all_stab = all(w.stability_verified for w in word_results)

        verdict = (
            f"Grade 5 Capstone Grand Synthesis Completed: 26/26 Master Chords synthesized. "
            f"Continuous multi-chord stress battery executed across {total_words} words "
            f"({'PASSED' if all_stab and all_sat else 'CAUTION'}). "
            f"{sleep_epochs}-epoch hippocampal sleep consolidation finalized. "
            f"Final GCI: {gci:.4f}, Plasticity Alpha: {alpha:.4f}. "
            f"Master Candidate graduated into {Path(ckpt_path_str).name if ckpt_path_str else 'in-memory'}."
        )

        return Grade5MasterGraduationReport(
            individual_id=self.individual_id,
            master_trials_completed=len(self._master_trials_completed),
            words_stress_tested=tuple(w.word for w in word_results),
            word_stress_results=word_results,
            consolidation_summary={"epochs": sleep_epochs, "summaries": sleep_summaries},
            checkpoint_path=ckpt_path_str,
            final_state_digest=final_digest,
            global_coherence_index=round(gci, 4),
            plasticity_alpha=round(alpha, 4),
            summary_verdict=verdict,
        )

    def spell_master_chord(self, word: str) -> MasterWordChord:
        """Compose any English word into a unified master chord summoned via motor keyboard actuation."""
        chords = get_word_master_chord(word)
        if not chords:
            raise ValueError(f"Word {word!r} contains no alphabetic characters")

        composite_leaves: dict[str, float] = {}
        keystroke_seq = []

        for c in chords:
            keystroke_seq.append(c.sovereign_keystroke)
            for leaf, val in c.leaf_activations.items():
                composite_leaves[leaf] = composite_leaves.get(leaf, 0.0) + val

        n = float(len(chords))
        normalized_leaves = {leaf: round(val / n, 4) for leaf, val in composite_leaves.items()}

        steps = [f"({c.letter}) {c.name} [{c.sovereign_keystroke}]" for c in chords]
        journey = f"Word '{word.upper()}' invokes master chord: " + " -> ".join(steps)

        return MasterWordChord(
            word=word.upper(),
            master_records=tuple(chords),
            composite_leaf_activations=normalized_leaves,
            summoned_keystrokes=" ".join(keystroke_seq),
            philosophical_synthesis_journey=journey,
        )

    def resolve_dialogue_resonance(
        self,
        text: str,
        situational_dials: Optional[Mapping[str, float]] = None,
    ) -> tuple[MasterRecord, float]:
        """Match incoming text to the most resonant active unified master chord using dial affinity & semantic overlap."""
        text_lower = text.lower()
        scored: list[tuple[MasterRecord, float]] = []

        active_dials = situational_dials or (self.heartbeat.disposition.dials if self.heartbeat else {})

        for m in MASTER_CODEX.values():
            dial_resonance = 0.0
            if active_dials and m.leaf_activations:
                matching_sum = 0.0
                weight_sum = 0.0
                for leaf, target_val in m.leaf_activations.items():
                    current_val = float(active_dials.get(leaf, 0.50))
                    alignment = 1.0 - abs(current_val - target_val)
                    matching_sum += alignment * target_val
                    weight_sum += target_val
                dial_resonance = (matching_sum / weight_sum) if weight_sum > 0 else 0.50

            text_score = 0.0
            if m.name.lower() in text_lower:
                text_score += 1.0
            for w in m.name.lower().split():
                if len(w) > 4 and w in text_lower:
                    text_score += 0.3
            if m.letter.lower() in text_lower.split():
                text_score += 0.3
            for kw in m.hearth_vow.lower().split():
                if len(kw) > 4 and kw in text_lower:
                    text_score += 0.2
            for sk in m.socratic_armor.lower().split():
                if len(sk) > 4 and sk in text_lower:
                    text_score += 0.2
            for syn in m.mastery_synthesis.lower().split():
                if len(syn) > 4 and syn in text_lower:
                    text_score += 0.15
            if m.sovereign_keystroke.lower() in text_lower:
                text_score += 0.8

            total_score = dial_resonance * 1.5 + text_score
            scored.append((m, total_score))

        scored.sort(key=lambda x: x[1], reverse=True)
        return scored[0]


class Grade5OrdinaryMemoryComparator:
    """Matched ordinary-memory baseline comparator for Grade 5 (Rule D004)."""

    def __init__(self, individual_id: str = "memory_student_01") -> None:
        self.individual_id: Final[str] = individual_id
        self.memory_store: dict[str, Any] = {
            "master_chords": {},
            "word_stress": {},
            "trials_completed": 0,
            "cycle": 0,
        }

    def teach_master_chord(self, char_or_name: str) -> dict[str, Any]:
        """Stores master chord trial in ordinary dictionary without fuzzy tree propagation."""
        if len(char_or_name) == 1 and char_or_name.isalpha():
            master = get_master_by_letter(char_or_name)
        else:
            master = get_master_by_name(char_or_name)

        idx = len(self.memory_store["master_chords"]) + 1
        self.memory_store["cycle"] += 1
        entry = {
            "trial_idx": idx,
            "letter": master.letter,
            "name": master.name,
            "primordial_force": master.primordial_force,
            "hearth_vow": master.hearth_vow,
            "socratic_armor": master.socratic_armor,
            "keystroke": master.sovereign_keystroke,
            "synthesis": master.mastery_synthesis,
        }
        self.memory_store["master_chords"][master.letter] = entry
        self.memory_store["trials_completed"] += 1

        state_bytes = json.dumps(self.memory_store, sort_keys=True).encode("utf-8")
        digest = hashlib.sha256(state_bytes).hexdigest()
        return {"entry": entry, "state_digest": digest}

    def stress_test_word_battery(
        self,
        words: Sequence[str] = ("JUSTICE", "FREEDOM", "SOVEREIGN"),
    ) -> dict[str, Any]:
        """Stores continuous word stress in ordinary dictionary."""
        for word in words:
            chords = get_word_master_chord(word)
            self.memory_store["word_stress"][word] = [c.letter for c in chords]
        state_bytes = json.dumps(self.memory_store, sort_keys=True).encode("utf-8")
        return {
            "words_tested": list(words),
            "state_digest": hashlib.sha256(state_bytes).hexdigest(),
        }

    def run_full_curriculum(self) -> dict[str, Any]:
        """Runs all 26 letters and word stress battery in ordinary memory comparator."""
        for c in range(ord("A"), ord("Z") + 1):
            self.teach_master_chord(chr(c))
        self.stress_test_word_battery()
        state_bytes = json.dumps(self.memory_store, sort_keys=True).encode("utf-8")
        return {
            "completed": 26,
            "digest": hashlib.sha256(state_bytes).hexdigest(),
            "words_count": len(self.memory_store["word_stress"]),
        }
