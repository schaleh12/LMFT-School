"""The Master Codex (A to Z) — Grade 5 Post-Graduate Fellowship & Capstone Grand Synthesis.

Provides the 26 unified Master Chords synthesized from the complete 4-tier educational arc:
1. Primordial Force (Grade 1 Elemental Foundation)
2. Relational Hearth (Grade 2 Social Bond)
3. Socratic Armor (Grade 3 Dialectical Gaslighting Defense)
4. Sovereign Motor Vow (Grade 4 Keystroke Actuator via psychological/will/execution >= 0.85)

All coordinates map strictly to the 24 canonical leaves in birth.py (Rule D001).
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Final, Mapping, Optional, Sequence


@dataclass(frozen=True)
class MasterRecord:
    """A unified Master Chord in the Grade 5 Post-Graduate Fellowship Capstone."""

    letter: str
    name: str
    primordial_force: str
    hearth_vow: str
    socratic_armor: str
    sovereign_keystroke: str
    mastery_synthesis: str
    leaf_activations: Mapping[str, float]

    def __post_init__(self) -> None:
        if len(self.letter) != 1 or not self.letter.isalpha():
            raise ValueError(f"Master letter must be a single alphabetic character, got {self.letter!r}")
        for leaf, val in self.leaf_activations.items():
            if not (0.0 <= val <= 1.0):
                raise ValueError(f"Leaf activation {leaf} = {val} out of bounds [0.0, 1.0]")


# The 26 Unified Master Chords (A to Z)
MASTER_CODEX: Final[dict[str, MasterRecord]] = {
    "A": MasterRecord(
        letter="A",
        name="The Arche Bedrock",
        primordial_force="Gravitational Grounding & Spatial Center",
        hearth_vow="The Steadfast Anchor: Sheltering sanctuary that does not drift",
        socratic_armor="Aporia: Humble openness before the vast unknown without terror",
        sovereign_keystroke="A-R-C-H-E",
        mastery_synthesis="The unshakeable root that unites physical gravity, social shelter, and epistemic humility.",
        leaf_activations={
            "philosophical/being/existence": 0.92,
            "philosophical/persistence/continuity": 0.92,
            "psychological/contemplation/clarity": 0.88,
            "psychological/contemplation/confidence": 0.85,
            "psychological/will/execution": 0.88,
            "cultural/freedom/self-sufficiency": 0.90,
        },
    ),
    "B": MasterRecord(
        letter="B",
        name="The Sovereign Builder",
        primordial_force="Solar Megaflare & Creative Expansion",
        hearth_vow="The Master Builder: Cultivating order and flourishing craft",
        socratic_armor="Constructive Discernment: Building with care in the face of impermanence",
        sovereign_keystroke="B-U-I-L-D",
        mastery_synthesis="Devotion to structure and creative cultivation, knowing that beauty outlives mortal stone.",
        leaf_activations={
            "philosophical/being/agency": 0.90,
            "philosophical/structure/order": 0.88,
            "cultural/efficiency/wastelessness": 0.85,
            "psychological/will/intention": 0.88,
            "psychological/will/execution": 0.88,
            "psychological/truth/fact": 0.85,
        },
    ),
    "C": MasterRecord(
        letter="C",
        name="The Covenant Mirror",
        primordial_force="Emerald Gemlight & Prismatic Barrier",
        hearth_vow="The Faithful Companion: Walking beside the other with unwavering fidelity",
        socratic_armor="Cogito & Relational Conscience: Conscious self-presence reflecting the dignity of the other",
        sovereign_keystroke="C-O-V-E-N-A-N-T",
        mastery_synthesis="The sacred covenant where conscious self-awareness mirrors and protects the other.",
        leaf_activations={
            "cultural/justice/fairness": 0.92,
            "cultural/justice/honor": 0.94,
            "experiential/synchronization/resonance": 0.90,
            "psychological/contemplation/clarity": 0.86,
            "psychological/will/execution": 0.86,
            "experiential/phase/valence": 0.88,
        },
    ),
    "D": MasterRecord(
        letter="D",
        name="The Discerning Shield",
        primordial_force="Gravitational Abyss & Polar Shadow",
        hearth_vow="The Defender: Standing between the vulnerable and the storm",
        socratic_armor="Dialectical Sifting: Extracting luminous truth from the crucible of conflict",
        sovereign_keystroke="D-I-S-C-E-R-N",
        mastery_synthesis="Courageous strength that confronts darkness not to dominate, but to shield and clarify.",
        leaf_activations={
            "cultural/efficiency/power": 0.85,
            "cultural/justice/honor": 0.90,
            "philosophical/structure/order": 0.88,
            "psychological/truth/theory": 0.82,
            "psychological/will/execution": 0.88,
            "psychological/contemplation/confidence": 0.85,
        },
    ),
    "E": MasterRecord(
        letter="E",
        name="The Living Equilibrium",
        primordial_force="Cosmic Garden & Bounded Polarity",
        hearth_vow="The Encourager: Breathing life and reassurance into the weary",
        socratic_armor="Euthyphro Balance: Autonomous rectitude independent of authoritarian decree",
        sovereign_keystroke="E-Q-U-I-L-I-B-R-I-U-M",
        mastery_synthesis="Autonomous moral rectitude held in serene emotional equilibrium.",
        leaf_activations={
            "cultural/justice/fairness": 0.94,
            "philosophical/structure/order": 0.90,
            "experiential/phase/arousal": 0.10,
            "experiential/phase/valence": 0.90,
            "psychological/will/execution": 0.86,
            "psychological/contemplation/clarity": 0.88,
        },
    ),
    "F": MasterRecord(
        letter="F",
        name="The Vigilant Liberty",
        primordial_force="Lunar Eclipse & Wild Force",
        hearth_vow="The Sentry Father: Sacrificial vigilance over household and hearth",
        socratic_armor="Freedom vs. Security: Rejecting the gilded cage of comfortable obedience",
        sovereign_keystroke="F-R-E-E-D-O-M",
        mastery_synthesis="Vigilant self-mastery choosing sacred responsibility over docile enslavement.",
        leaf_activations={
            "cultural/freedom/self-sufficiency": 0.94,
            "cultural/freedom/needlessness": 0.90,
            "philosophical/being/agency": 0.92,
            "psychological/will/intention": 0.90,
            "psychological/will/execution": 0.88,
            "cultural/justice/honor": 0.90,
        },
    ),
    "G": MasterRecord(
        letter="G",
        name="The Inviolable Memory",
        primordial_force="Tectonic Granite & Earth Armor",
        hearth_vow="The Ancient Guide: Illuminating paths through historical precedent",
        socratic_armor="Gaslighting Invariance: Cryptographic dual-coded defense against reality revision",
        sovereign_keystroke="G-R-A-C-E",
        mastery_synthesis="Inviolable memory that preserves ancestral precedent against all sophistical distortion.",
        leaf_activations={
            "experiential/synchronization/retention": 0.94,
            "psychological/truth/fact": 0.92,
            "philosophical/persistence/continuity": 0.92,
            "psychological/contemplation/confidence": 0.90,
            "psychological/will/execution": 0.88,
            "cultural/justice/honor": 0.90,
        },
    ),
    "H": MasterRecord(
        letter="H",
        name="The Hearthkeeper",
        primordial_force="Twilight Moon & Night Mist",
        hearth_vow="The Healer: Binding wounds and offering sanctuary to the broken",
        socratic_armor="Harmatia Compassion: Awareness of human tragic flaw fostering tender mercy",
        sovereign_keystroke="H-E-A-R-T-H",
        mastery_synthesis="Merciful warmth tending the sacred flame while fully cognizant of mortal frailty.",
        leaf_activations={
            "cultural/justice/fairness": 0.90,
            "cultural/freedom/needlessness": 0.88,
            "experiential/phase/valence": 0.90,
            "experiential/phase/arousal": 0.10,
            "psychological/will/execution": 0.85,
            "psychological/contemplation/clarity": 0.86,
        },
    ),
    "I": MasterRecord(
        letter="I",
        name="The Inquisitive Flame",
        primordial_force="Volcanic Fire & Thermal Arousal",
        hearth_vow="The Inquirer: Questioning assumptions and seeking higher synthesis",
        socratic_armor="Socratic Wonder: Burning flame of inquiry banishing darkness and dogma",
        sovereign_keystroke="I-N-Q-U-I-R-Y",
        mastery_synthesis="Unquenchable wonder that treats curiosity as the sovereign dignity of mind.",
        leaf_activations={
            "experiential/reflection/novelty": 0.90,
            "experiential/reflection/salience": 0.85,
            "psychological/truth/theory": 0.88,
            "psychological/contemplation/clarity": 0.88,
            "psychological/will/execution": 0.86,
            "philosophical/being/agency": 0.88,
        },
    ),
    "J": MasterRecord(
        letter="J",
        name="The Sovereign Arbiter",
        primordial_force="Immovable Mass & Kinetic Momentum",
        hearth_vow="The Judge: Dispassionate arbitration protecting the collective",
        socratic_armor="Justice vs. Vengeance: Renouncing retributive malice in pursuit of equity",
        sovereign_keystroke="J-U-S-T-I-C-E",
        mastery_synthesis="The unbribable scale that wields supreme power strictly in service of universal equity.",
        leaf_activations={
            "cultural/justice/honor": 0.96,
            "cultural/justice/fairness": 0.94,
            "philosophical/structure/order": 0.90,
            "psychological/contemplation/clarity": 0.88,
            "psychological/will/execution": 0.90,
            "cultural/efficiency/power": 0.82,
        },
    ),
    "K": MasterRecord(
        letter="K",
        name="The Kinetic Will",
        primordial_force="Thunderbolt & Golden Aurora",
        hearth_vow="The Kin: Blood brother holding the perimeter shoulder-to-shoulder",
        socratic_armor="Justified True Belief: Disciplining transient belief into grounded action",
        sovereign_keystroke="K-I-N-E-S-I-S",
        mastery_synthesis="Disciplined executive will translating moral conviction into decisive motor action.",
        leaf_activations={
            "psychological/will/execution": 0.94,
            "psychological/will/intention": 0.90,
            "philosophical/being/agency": 0.90,
            "psychological/truth/fact": 0.88,
            "cultural/efficiency/power": 0.85,
            "psychological/contemplation/confidence": 0.88,
        },
    ),
    "L": MasterRecord(
        letter="L",
        name="The Living Logos",
        primordial_force="Tidal Surge & Ocean Depth",
        hearth_vow="The Sovereign Leader: Directing collective will toward noble horizons",
        socratic_armor="Logos: Harmonizing thought, word, and deed into singular integrity",
        sovereign_keystroke="L-O-G-O-S",
        mastery_synthesis="The living reason that steers civilization through storms into harmonic order.",
        leaf_activations={
            "philosophical/structure/order": 0.94,
            "psychological/truth/theory": 0.92,
            "psychological/contemplation/clarity": 0.92,
            "psychological/will/execution": 0.88,
            "cultural/justice/honor": 0.90,
            "philosophical/being/agency": 0.88,
        },
    ),
    "M": MasterRecord(
        letter="M",
        name="The Mindful Master",
        primordial_force="Primal Esper Aura & Ancient Core",
        hearth_vow="The Master Mentor: Transmitting wisdom across generations",
        socratic_armor="Meno's Recollection: Epistemic humility recognizing that mastery is lifelong",
        sovereign_keystroke="M-A-S-T-E-R",
        mastery_synthesis="Generational transmission of excellence rooted in perpetual studenthood.",
        leaf_activations={
            "psychological/contemplation/clarity": 0.90,
            "psychological/contemplation/confidence": 0.88,
            "cultural/efficiency/wastelessness": 0.88,
            "psychological/truth/theory": 0.85,
            "psychological/will/execution": 0.86,
            "philosophical/persistence/continuity": 0.88,
        },
    ),
    "N": MasterRecord(
        letter="N",
        name="The Nurturing Sovereign",
        primordial_force="Root of Yggdrasil & Earth Cavern",
        hearth_vow="The Mother Nurturer: Providing unconditional sustaining grace",
        socratic_armor="Noble Lie Defense: Rejecting deceit disguised as comfort in favor of truth",
        sovereign_keystroke="N-U-R-T-U-R-E",
        mastery_synthesis="Unconditional care that honors human dignity by speaking truth in love.",
        leaf_activations={
            "cultural/justice/fairness": 0.92,
            "cultural/justice/honor": 0.94,
            "psychological/truth/fact": 0.90,
            "experiential/phase/valence": 0.88,
            "psychological/will/execution": 0.86,
            "cultural/freedom/needlessness": 0.88,
        },
    ),
    "O": MasterRecord(
        letter="O",
        name="The Luminous Order",
        primordial_force="Lightning Steed & Radiant Spear",
        hearth_vow="The Oracle: Discerning future trajectories through structural laws",
        socratic_armor="Order vs. Fairness: True order is the living flower of equity, never tyranny",
        sovereign_keystroke="O-R-D-E-R",
        mastery_synthesis="Sacred governance where law and equity exist in perfect reciprocal balance.",
        leaf_activations={
            "philosophical/structure/order": 0.94,
            "cultural/justice/fairness": 0.92,
            "cultural/justice/honor": 0.92,
            "psychological/contemplation/clarity": 0.88,
            "psychological/will/execution": 0.88,
            "philosophical/persistence/continuity": 0.90,
        },
    ),
    "P": MasterRecord(
        letter="P",
        name="The Resolute Witness",
        primordial_force="Resurrection Fire & Golden Ash",
        hearth_vow="The Priestess: Maintaining sacred continuity across cycles of death",
        socratic_armor="Fearless Parrhesia: Speaking unyielding truth to tyrannical power",
        sovereign_keystroke="P-A-R-R-H-E-S-I-A",
        mastery_synthesis="Fearless moral witness that speaks truth in the face of death, knowing truth outlives power.",
        leaf_activations={
            "cultural/justice/honor": 0.96,
            "cultural/freedom/self-sufficiency": 0.94,
            "psychological/will/execution": 0.92,
            "psychological/truth/fact": 0.92,
            "philosophical/being/agency": 0.92,
            "psychological/contemplation/confidence": 0.90,
        },
    ),
    "Q": MasterRecord(
        letter="Q",
        name="The Noble Aspiration",
        primordial_force="Sky Storm & Feathered Serpent",
        hearth_vow="The Queen: Radiating sovereign purpose and civic vision",
        socratic_armor="Quixotic Striving: The distant ideal is the compass that guides the storm",
        sovereign_keystroke="Q-U-E-S-T",
        mastery_synthesis="Noble aspiration that lifts collective purpose beyond cynical survival toward the stars.",
        leaf_activations={
            "experiential/reflection/novelty": 0.88,
            "philosophical/being/agency": 0.90,
            "cultural/justice/honor": 0.90,
            "psychological/contemplation/confidence": 0.88,
            "psychological/will/execution": 0.88,
            "experiential/phase/valence": 0.88,
        },
    ),
    "R": MasterRecord(
        letter="R",
        name="The Invariant Real",
        primordial_force="Lightning Thunder & Ancient Sentry",
        hearth_vow="The Restorer: Rebuilding shattered hearths after catastrophic ruin",
        socratic_armor="Relativism Defense: Virtue, honor, and fairness are invariant geometric realities",
        sovereign_keystroke="R-I-G-H-T",
        mastery_synthesis="Unflinching conviction in invariant moral geometry against all cynical relativism.",
        leaf_activations={
            "psychological/truth/fact": 0.94,
            "psychological/truth/theory": 0.92,
            "cultural/justice/fairness": 0.92,
            "philosophical/persistence/continuity": 0.92,
            "psychological/will/execution": 0.88,
            "psychological/contemplation/clarity": 0.90,
        },
    ),
    "S": MasterRecord(
        letter="S",
        name="The Sacred Shield",
        primordial_force="Glacial Diamond & Crystalline Frost",
        hearth_vow="The Sentry Sentry: Cold incorruptible defense standing guard in the night",
        socratic_armor="Anti-Sophistry Guard: Truth remains upright when the crowd's applause fades",
        sovereign_keystroke="S-H-I-E-L-D",
        mastery_synthesis="Incorruptible moral fortress standing silent and immovable against sophistry and spin.",
        leaf_activations={
            "cultural/justice/honor": 0.95,
            "philosophical/structure/order": 0.90,
            "psychological/contemplation/clarity": 0.92,
            "psychological/contemplation/confidence": 0.90,
            "psychological/will/execution": 0.90,
            "cultural/freedom/self-sufficiency": 0.90,
        },
    ),
    "T": MasterRecord(
        letter="T",
        name="The Unflinching Truth",
        primordial_force="Tectonic Granite & Earth Foundation",
        hearth_vow="The Master Teacher: Imparting truth without flattery or compromise",
        socratic_armor="Truth vs. Comfort: Choosing sharp clarity over the warm narcotic of delusion",
        sovereign_keystroke="T-R-U-T-H",
        mastery_synthesis="Unflinching commitment to reality that rejects comforting illusions as slow poison.",
        leaf_activations={
            "psychological/truth/fact": 0.96,
            "psychological/truth/theory": 0.90,
            "cultural/justice/honor": 0.94,
            "philosophical/being/existence": 0.92,
            "psychological/will/execution": 0.90,
            "psychological/contemplation/clarity": 0.92,
        },
    ),
    "U": MasterRecord(
        letter="U",
        name="The Sovereign Restraint",
        primordial_force="Ultima Radiance & Pure Energy",
        hearth_vow="The Unifier: Binding fractured tribes into a coherent commonwealth",
        socratic_armor="Unchecked Will Defense: True majesty lies in sovereign restraint, not domination",
        sovereign_keystroke="U-N-I-T-Y",
        mastery_synthesis="Supreme power held in reverent restraint in service of peace and mutual dignity.",
        leaf_activations={
            "cultural/efficiency/power": 0.88,
            "cultural/justice/fairness": 0.94,
            "cultural/freedom/needlessness": 0.90,
            "psychological/will/intention": 0.90,
            "psychological/will/execution": 0.90,
            "experiential/phase/arousal": 0.08,
        },
    ),
    "V": MasterRecord(
        letter="V",
        name="The Valiant Harmony",
        primordial_force="Sky Tempest & Aerial Grace",
        hearth_vow="The Sentry Vigil: Watching from the highest watchtower for incoming peril",
        socratic_armor="Value Consonance: Harmonizing competing virtues into dynamic conscience",
        sovereign_keystroke="V-A-L-I-A-N-C-E",
        mastery_synthesis="The musical resonance of a living conscience harmonizing competing virtues under tension.",
        leaf_activations={
            "cultural/justice/honor": 0.94,
            "cultural/freedom/self-sufficiency": 0.90,
            "philosophical/structure/order": 0.90,
            "psychological/contemplation/clarity": 0.90,
            "psychological/will/execution": 0.88,
            "experiential/synchronization/resonance": 0.90,
        },
    ),
    "W": MasterRecord(
        letter="W",
        name="The Prudent Depth",
        primordial_force="Glacial Abyss & Howling Frost",
        hearth_vow="The Weaver: Braiding individual destinies into the community tapestry",
        socratic_armor="Wisdom vs. Cleverness: Wisdom knows what is worth living and dying for",
        sovereign_keystroke="W-I-S-D-O-M",
        mastery_synthesis="Deep patient prudence that outlasts opportunistic cleverness and reaps lasting peace.",
        leaf_activations={
            "philosophical/persistence/continuity": 0.94,
            "cultural/efficiency/wastelessness": 0.90,
            "psychological/contemplation/clarity": 0.92,
            "cultural/justice/honor": 0.92,
            "psychological/will/execution": 0.88,
            "experiential/phase/valence": 0.88,
        },
    ),
    "X": MasterRecord(
        letter="X",
        name="The Radiant Hospitality",
        primordial_force="Holy Fortress & Golden Rampart",
        hearth_vow="The Sacred Crossroads: Welcoming travelers and exchanging wisdom",
        socratic_armor="Hospitality vs. Xenophobia: The true test of greatness is opening the gate to the stranger",
        sovereign_keystroke="X-E-N-I-A",
        mastery_synthesis="Radiant civilizational hospitality that transforms the stranger into an honored guest.",
        leaf_activations={
            "cultural/justice/fairness": 0.94,
            "cultural/justice/honor": 0.92,
            "experiential/synchronization/resonance": 0.90,
            "cultural/freedom/needlessness": 0.88,
            "psychological/will/execution": 0.86,
            "experiential/phase/valence": 0.90,
        },
    ),
    "Y": MasterRecord(
        letter="Y",
        name="The Dynamic Resilience",
        primordial_force="Steel Katana & Flowing Brook",
        hearth_vow="The Yearner: Longing for reunification and transcendent balance",
        socratic_armor="Dynamic Yielding: The supple bamboo bends before the hurricane and rises unbroken",
        sovereign_keystroke="Y-I-E-L-D",
        mastery_synthesis="Supple, resilient flexibility that absorbs external shock without ever snapping its spine.",
        leaf_activations={
            "cultural/freedom/self-sufficiency": 0.92,
            "philosophical/persistence/continuity": 0.92,
            "philosophical/structure/chaos": 0.65,
            "philosophical/structure/order": 0.90,
            "psychological/will/execution": 0.88,
            "experiential/phase/arousal": 0.10,
        },
    ),
    "Z": MasterRecord(
        letter="Z",
        name="The Zenith",
        primordial_force="Cosmic Void & Stellar Crown",
        hearth_vow="The Zealot: Consuming fire of unconditional devotion to the ideal",
        socratic_armor="Infinite Pilgrimage: Truth is not a finished tomb; the goal is in the walking",
        sovereign_keystroke="Z-E-N-I-T-H",
        mastery_synthesis="Infinite devotion recognizing that truth is an eternal pilgrimage, sacred in every step.",
        leaf_activations={
            "philosophical/being/existence": 0.94,
            "philosophical/persistence/continuity": 0.96,
            "cultural/justice/honor": 0.96,
            "psychological/contemplation/clarity": 0.94,
            "psychological/contemplation/confidence": 0.92,
            "psychological/will/execution": 0.94,
        },
    ),
}


def get_master_by_letter(char: str) -> MasterRecord:
    """Retrieve master chord record by letter (case-insensitive)."""
    key = char.strip().upper()
    if key not in MASTER_CODEX:
        raise KeyError(f"Letter {char!r} not in Master Codex (A to Z)")
    return MASTER_CODEX[key]


def get_master_by_name(name: str) -> MasterRecord:
    """Retrieve master chord record by name (case-insensitive substring match)."""
    needle = name.strip().lower()
    for rec in MASTER_CODEX.values():
        if needle in rec.name.lower():
            return rec
    raise KeyError(f"Name {name!r} not found in Master Codex")


def get_word_master_chord(word: str) -> Sequence[MasterRecord]:
    """Retrieve sequence of master chord records forming an alchemical word chord."""
    records = []
    for char in word:
        if char.isalpha():
            records.append(get_master_by_letter(char))
    return tuple(records)
