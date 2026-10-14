# Preregistered Protocol: Grade 2 Curriculum — The Relational Alphabet (The Social Hearth)

## 1. Research Purpose & Hypotheses

Grade 2 in `LMFT-School` introduces **The Relational Alphabet (The Social Hearth)**. 
Following the elemental and physical grounding of Grade 1 (The Electro-Gravitational Esper Alphabet), Grade 2 cultivates social cognition, interpersonal ethics, and dyadic empathy across 26 archetypes structured around the **13 Symmetrical Stations of the Human Hearth** ($13 \times 2 = 26$).

### Hypotheses:
- **H1 (Full 26-Letter Relational Codex Mastery):** All 26 letters (A to Z) are formally specified in `src/lmft_school/relational_codex.py` with exact 13 Masculine (A–M) and 13 Feminine (N–Z) polarity balance, reciprocal dyad partner links ($A \leftrightarrow N$, $B \leftrightarrow O$, ... $M \leftrightarrow Z$), and continuous coordinates mapped across the 24 canonical leaves in `birth.py` without mutating the frozen 40-node founding seed (Rule D001).
- **H2 (Dyadic Station Harmonic Equilibrium):** All 13 Polar Stations demonstrate harmonic consonance ($\ge 0.70$) between their masculine (directive, structural, shielding) and feminine (receptive, connective, harmonizing) pillars.
- **H3 (Homeostatic Volatility Clamping):** Intense relational virtues (e.g., *The Zealot*, *The Rescuer*, *The Champion*) and shadow hazards are regulated by the `AffectiveHomeostasisGovernor`, strictly clamping $|\Delta| \le 0.35$ and preventing boundary saturation ($0.05 \le \text{leaf} \le 0.95$).
- **H4 (Matched Ordinary-Memory Parity, Rule D004):** The LMFT curriculum runner and `Grade2OrdinaryMemoryComparator` achieve byte-for-byte evaluation digest parity under separate process restart invariance.
- **H5 (Lineage Vault & Phenotypic Telemetry Harvesting):** Each graduation milestone is frozen into an immutable `.lmft.json` standalone individual package in `checkpoints/` and cataloged with rich phenotype telemetry in `checkpoints/LINEAGE_LEDGER.json`.
- **H6 (Relational Word Chords & Interactive REPL Actuation):** English words decompose into balanced relational chords (e.g., `HEARTH`, `MERCY`, `JUSTICE`) with live HUD readouts in `tools/talk_to_lmft.py` supporting `--grade 1` and `--grade 2` time travel.

## 2. Experimental Design & Methodology

1. **Codex Implementation:** `src/lmft_school/relational_codex.py` defines `RelationalRecord` and canonical 26-letter catalog across the 13 Stations.
2. **Curriculum Engine:** `src/lmft_school/curriculum_grade_2.py` delivers sequential lessons through the 10-faculty Cognitive Heartbeat, computes dyadic station equilibria, and performs overnight memory consolidation.
3. **Lineage Vault:** `src/lmft_school/lineage_vault.py` snapshots `.lmft.json` packages and logs phenotype telemetry across generations.
4. **Verification:** `tests/test_grade_2_curriculum.py` executes 8 comprehensive automated tests under strict offline zero-LLM reproducibility.

## 3. Success Criteria

- 100% test pass rate across `tests/test_grade_2_curriculum.py`.
- Exact 13 Masculine / 13 Feminine balance and symmetrical reciprocal partner links.
- 100% adherence to Rule D001 (frozen 40-node founding seed) and Rule D004 (matched ordinary-memory parity).
- Zero runtime LLM calls during unassisted evaluation.
