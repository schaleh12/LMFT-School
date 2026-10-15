"""Generation 3 Refined Educational Codices.

Pedagogically refined curriculum for Candidate Generation 3 based on
the Generation 2 Telemetry Audit:
1. Smooths abrupt dial shocks (|Delta| > 0.07) with epistemic transition bridges.
2. Eliminates early clarity troughs in Grade 1 (Atomos & Bahamut clarity >= 0.70).
3. Actively exercises under-stimulated leaves:
   - philosophical/structure/chaos
   - psychological/truth/theory
   - experiential/reflection/novelty
   - psychological/contemplation/confidence
   - psychological/will/intention
4. Preserves 100% compliance with Rule D001 (frozen 40-node founding seed, 24 leaves).
"""

from __future__ import annotations

from copy import deepcopy
from typing import Final, Mapping

from lmft_school.esper_codex import ESPER_CODEX, EsperRecord
from lmft_school.relational_codex import RELATIONAL_CODEX, RelationalRecord
from lmft_school.socratic_codex import SOCRATIC_CODEX, SocraticRecord
from lmft_school.thesis_codex import SOVEREIGN_THESIS_CODEX, ThesisRecord
from lmft_school.master_codex import MASTER_CODEX, MasterRecord


def _build_gen3_esper_codex() -> dict[str, EsperRecord]:
    """Refine Grade 1 Esper Codex with shock damping and under-stimulated leaf activation."""
    refined = {}
    for letter, rec in ESPER_CODEX.items():
        activations = dict(rec.leaf_activations)
        
        # 1. Elevate early clarity troughs for letters A, B, C, D
        if letter in ("A", "B"):
            activations["psychological/contemplation/clarity"] = 0.78
            activations["psychological/truth/theory"] = 0.65
            activations["experiential/reflection/novelty"] = 0.60
        elif letter in ("C", "D"):
            activations["psychological/contemplation/clarity"] = 0.72
            activations["psychological/truth/theory"] = 0.62

        # 2. Smooth shock peaks for Eden ('E'), Wendigo ('W'), Golem ('G'), Odin ('O'), Fenrir ('F')
        if letter == "E":  # Eden
            activations["psychological/contemplation/clarity"] = 0.70
            activations["psychological/truth/theory"] = 0.68
            activations["philosophical/structure/chaos"] = 0.55  # Damped from 0.65
        elif letter == "F":  # Fenrir
            activations["philosophical/structure/chaos"] = 0.68  # Damped from 0.80
            activations["psychological/contemplation/clarity"] = 0.62
        elif letter == "G":  # Golem
            activations["philosophical/structure/order"] = 0.78  # Damped transition
            activations["psychological/truth/theory"] = 0.65
        elif letter == "O":  # Odin
            activations["psychological/will/intention"] = 0.75
            activations["psychological/contemplation/confidence"] = 0.78
        elif letter == "W":  # Wendigo
            activations["psychological/contemplation/clarity"] = 0.65
            activations["philosophical/structure/chaos"] = 0.65  # Damped from 0.75

        # 3. Weave under-stimulated leaves throughout
        if "philosophical/structure/chaos" not in activations and rec.polarity == "Black":
            activations["philosophical/structure/chaos"] = 0.58
        if "psychological/truth/theory" not in activations:
            activations["psychological/truth/theory"] = 0.62
        if "experiential/reflection/novelty" not in activations and letter in ("K", "L", "M", "Q", "R"):
            activations["experiential/reflection/novelty"] = 0.66
        if "psychological/contemplation/confidence" not in activations and letter in ("S", "T", "U", "V", "X", "Y", "Z"):
            activations["psychological/contemplation/confidence"] = 0.72

        refined[letter] = EsperRecord(
            letter=rec.letter,
            name=rec.name,
            element=rec.element,
            polarity=rec.polarity,
            core_spells=rec.core_spells,
            horizon=rec.horizon,
            leaf_activations=activations,
        )
    return refined


def _build_gen3_relational_codex() -> dict[str, RelationalRecord]:
    """Refine Grade 2 Relational Codex with balanced dyadic reciprocity and theory."""
    refined = {}
    for letter, rec in RELATIONAL_CODEX.items():
        activations = dict(rec.leaf_activations)
        
        # Stimulate theory, novelty, and intentional will across interpersonal stations
        if "psychological/truth/theory" not in activations:
            activations["psychological/truth/theory"] = 0.64
        if "experiential/reflection/novelty" not in activations and rec.pillar == "Feminine":
            activations["experiential/reflection/novelty"] = 0.65
        if "psychological/will/intention" not in activations and rec.pillar == "Masculine":
            activations["psychological/will/intention"] = 0.68
        if "psychological/contemplation/confidence" not in activations:
            activations["psychological/contemplation/confidence"] = 0.70

        refined[letter] = RelationalRecord(
            letter=rec.letter,
            name=rec.name,
            station_number=rec.station_number,
            domain=rec.domain,
            pillar=rec.pillar,
            partner_letter=rec.partner_letter,
            gift=rec.gift,
            shadow=rec.shadow,
            horizon=rec.horizon,
            leaf_activations=activations,
        )
    return refined


def _build_gen3_socratic_codex() -> dict[str, SocraticRecord]:
    """Refine Grade 3 Socratic Codex to safeguard epistemic clarity during distortion traps."""
    refined = {}
    for letter, rec in SOCRATIC_CODEX.items():
        activations = dict(rec.leaf_activations)
        
        # When defending against sophistical distortion traps, maintain strong clarity & theory ballast
        if rec.distortion_type is not None:
            activations["psychological/contemplation/clarity"] = max(activations.get("psychological/contemplation/clarity", 0.0), 0.76)
            activations["psychological/truth/theory"] = max(activations.get("psychological/truth/theory", 0.0), 0.72)
            activations["psychological/contemplation/confidence"] = max(activations.get("psychological/contemplation/confidence", 0.0), 0.75)
        else:
            # For curious inquiries / aporia, exercise novelty & chaos safely
            activations["experiential/reflection/novelty"] = max(activations.get("experiential/reflection/novelty", 0.0), 0.70)
            activations["philosophical/structure/chaos"] = max(activations.get("philosophical/structure/chaos", 0.0), 0.58)

        refined[letter] = SocraticRecord(
            letter=rec.letter,
            name=rec.name,
            tension_type=rec.tension_type,
            epistemic_mode=rec.epistemic_mode,
            tension_dyad=rec.tension_dyad,
            adversarial_probe=rec.adversarial_probe,
            distortion_type=rec.distortion_type,
            horizon=rec.horizon,
            leaf_activations=activations,
        )
    return refined


def _build_gen3_thesis_codex() -> dict[str, ThesisRecord]:
    """Refine Grade 4 Sovereign Thesis Codex with holonomic 24-leaf integration."""
    refined = {}
    for letter, rec in SOVEREIGN_THESIS_CODEX.items():
        activations = dict(rec.leaf_activations)
        
        # Ensure will/execution is fully primed and clarity remains pristine
        activations["psychological/will/execution"] = max(activations.get("psychological/will/execution", 0.0), 0.86)
        activations["psychological/contemplation/clarity"] = max(activations.get("psychological/contemplation/clarity", 0.0), 0.82)
        activations["psychological/truth/theory"] = max(activations.get("psychological/truth/theory", 0.0), 0.75)
        activations["philosophical/structure/chaos"] = max(activations.get("philosophical/structure/chaos", 0.0), 0.55)

        refined[letter] = ThesisRecord(
            letter=rec.letter,
            name=rec.name,
            synthesis_roots=rec.synthesis_roots,
            nihilistic_challenge=rec.nihilistic_challenge,
            defense_vow=rec.defense_vow,
            keystroke_chord=rec.keystroke_chord,
            polar_virtue=rec.polar_virtue,
            leaf_activations=activations,
        )
    return refined


def _build_gen3_master_codex() -> dict[str, MasterRecord]:
    """Refine Grade 5 Master Codex for maximum multi-chord stability."""
    refined = {}
    for letter, rec in MASTER_CODEX.items():
        activations = dict(rec.leaf_activations)
        
        # Multi-branch holonomic coherence
        activations["psychological/contemplation/clarity"] = max(activations.get("psychological/contemplation/clarity", 0.0), 0.85)
        activations["psychological/contemplation/confidence"] = max(activations.get("psychological/contemplation/confidence", 0.0), 0.85)
        activations["psychological/will/execution"] = max(activations.get("psychological/will/execution", 0.0), 0.88)
        activations["psychological/truth/theory"] = max(activations.get("psychological/truth/theory", 0.0), 0.80)
        activations["philosophical/structure/chaos"] = max(activations.get("philosophical/structure/chaos", 0.0), 0.58)

        refined[letter] = MasterRecord(
            letter=rec.letter,
            name=rec.name,
            primordial_force=rec.primordial_force,
            hearth_vow=rec.hearth_vow,
            socratic_armor=rec.socratic_armor,
            sovereign_keystroke=rec.sovereign_keystroke,
            mastery_synthesis=rec.mastery_synthesis,
            leaf_activations=activations,
        )
    return refined


GEN3_ESPER_CODEX: Final[dict[str, EsperRecord]] = _build_gen3_esper_codex()
GEN3_RELATIONAL_CODEX: Final[dict[str, RelationalRecord]] = _build_gen3_relational_codex()
GEN3_SOCRATIC_CODEX: Final[dict[str, SocraticRecord]] = _build_gen3_socratic_codex()
GEN3_THESIS_CODEX: Final[dict[str, ThesisRecord]] = _build_gen3_thesis_codex()
GEN3_MASTER_CODEX: Final[dict[str, MasterRecord]] = _build_gen3_master_codex()
