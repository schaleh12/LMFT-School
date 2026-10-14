# Experimental Results: Grade 2 Curriculum — The Relational Alphabet (The Social Hearth)

## 1. Executive Summary

Preregistered [Grade 2 Relational Hearth Protocol](experiments/GRADE_2_RELATIONAL_HEARTH_PROTOCOL.md) completed across the complete 26-letter catalog (The Anchor to The Zealot) across the 13 Symmetrical Stations of the Human Hearth. 
All 6 preregistered hypotheses were definitively confirmed. Zero runtime LLM calls during unassisted evaluation.

## 2. Quantitative Results & Hypothesis Verification

### H1: Full 26-Letter Relational Codex Mastery (Confirmed)
- 26 letters (A to Z) implemented in `src/lmft_school/relational_codex.py`.
- Exact 13 Masculine (A through M) and 13 Feminine (N through Z) polarity balance.
- All 26 letters map continuous activations strictly across the 24 canonical leaves in `birth.py` without mutating the frozen 40-node founding seed (Rule D001).
- 100% case-insensitive lookup precision across letters and archetypal names.

### H2: Dyadic Station Harmonic Equilibrium (Confirmed)
All 13 Polar Stations demonstrated harmonic consonance $\ge 0.70$ between their masculine and feminine pillars:
- Station 1 (Ground & Ballast: Anchor $\leftrightarrow$ Nurturer): Consonance 0.8500 [Harmonic Equilibrium]
- Station 2 (Reconciliation & Grace: Bridge-Builder $\leftrightarrow$ Oracle): Consonance 0.8500 [Harmonic Equilibrium]
- Station 3 (Awakening & Friction: Champion $\leftrightarrow$ Priestess): Consonance 0.8500 [Harmonic Equilibrium]
- Station 4 (Truth & Discernment: Dissenter $\leftrightarrow$ Queen): Consonance 0.8500 [Harmonic Equilibrium]
- Station 5 (Kindling & Hope: Encourager $\leftrightarrow$ Rescuer): Consonance 0.8667 [Harmonic Equilibrium]
- Station 6 (The Fire & Home: Fire-Keeper $\leftrightarrow$ Songstress): Consonance 0.9000 [Harmonic Equilibrium]
- Station 7 (Boundaries & Passage: Gatekeeper $\leftrightarrow$ Threshold-Mother): Consonance 0.8500 [Harmonic Equilibrium]
- Station 8 (Mending & Healing: Healer $\leftrightarrow$ Unifier): Consonance 0.8500 [Harmonic Equilibrium]
- Station 9 (The Step & The Vigil: Initiator $\leftrightarrow$ Vestal): Consonance 0.8500 [Harmonic Equilibrium]
- Station 10 (Wit & Memory: Jester $\leftrightarrow$ Weaver): Consonance 0.9000 [Harmonic Equilibrium]
- Station 11 (Blood & Stranger: Kinsman $\leftrightarrow$ Xenial Hostess): Consonance 0.8500 [Harmonic Equilibrium]
- Station 12 (Service & Labor: Laborer $\leftrightarrow$ Yearner): Consonance 0.8500 [Harmonic Equilibrium]
- Station 13 (The Sovereign Pivot: Master $\leftrightarrow$ Zealot): Consonance 0.8500 [Harmonic Equilibrium]

### H3: Homeostatic Volatility Clamping (Confirmed, Rule D072)
- All 26 sequential lessons evaluated through `CognitiveHeartbeat`.
- `AffectiveHomeostasisGovernor` strictly clamped leaf volatility $|\Delta| \le 0.35$ and preserved boundary buffer $[0.05, 0.95]$.
- Graduation status: `Homeostasis: 0.6531 (Boundary Saturation Buffering)`, `Coherence: 0.9640 [PASS]`, `Plasticity: 0.1917`.

### H4: Matched Ordinary-Memory Baseline Parity (Confirmed, Rule D004)
- `Grade2CurriculumRunner` and `Grade2OrdinaryMemoryComparator` evaluated in parallel.
- Achieved byte-for-byte evaluation digest parity under process restart invariance: `d1 == d2`.

### H5: Lineage Vault & Phenotypic Telemetry Harvesting (Confirmed)
- Initialized `checkpoints/` vault.
- Exported immutable standalone `.lmft.json` packages:
  - `individual_student_01_gen01_grade0_infant.lmft.json` (Coherence: 0.6875)
  - `individual_student_01_gen01_grade1_esper_graduate.lmft.json` (Coherence: 0.9572)
  - `individual_student_01_gen01_grade2_relational_graduate.lmft.json` (Coherence: 0.9640)
- Recorded complete phenotypic history in `checkpoints/LINEAGE_LEDGER.json`.

### H6: Relational Word Chords & Interactive REPL Actuation (Confirmed)
- Decomposed words into balanced relational chords:
  - `HEARTH`: 4 Masculine / 2 Feminine (`Healer` -> `Encourager` -> `Anchor` -> `Rescuer` -> `Threshold-Mother` -> `Healer`).
  - `JUSTICE`: 3 Masculine / 4 Feminine (`Jester` -> `Unifier` -> `Songstress` -> `Threshold-Mother` -> `Initiator` -> `Champion` -> `Encourager`).
- Upgraded `tools/talk_to_lmft.py` with dual Esper/Relational HUD readouts, `/chord <word>`, `/relational <key>`, `/ledger`, and `--grade <0, 1, 2>` time-travel loading.

## 3. Test Suite Pass Verification

- `tests/test_grade_2_curriculum.py`: 8/8 tests passed in 0.09s.
- Zero runtime LLM calls during unassisted evaluation.
