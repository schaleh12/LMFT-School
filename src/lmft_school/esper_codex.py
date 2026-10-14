"""Electro-Gravitational Alphabet of Espers (A to Z) Codex.

Provides the foundational 26-letter conceptual alphabet for LMFT-School,
grounded across 4 quaternion facets (Weather, Relational, Structural, Contemplative)
and continuous coordinates across the 24 canonical leaves in birth.py (Rule D001).
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Final, Mapping


@dataclass(frozen=True)
class EsperRecord:
    """An archetypal letter in the Electro-Gravitational Alphabet."""

    letter: str
    name: str
    element: str
    polarity: str  # "White" (Radiance/Expansion) or "Black" (Gravity/Depth)
    core_spells: tuple[str, ...]
    horizon: str
    leaf_activations: Mapping[str, float]

    def __post_init__(self) -> None:
        if len(self.letter) != 1 or not self.letter.isalpha():
            raise ValueError(f"Esper letter must be a single alphabetic character, got {self.letter!r}")
        if self.polarity not in ("White", "Black"):
            raise ValueError(f"Polarity must be 'White' or 'Black', got {self.polarity!r}")
        for leaf, val in self.leaf_activations.items():
            if not (0.0 <= val <= 1.0):
                raise ValueError(f"Leaf activation {leaf} = {val} out of bounds [0.0, 1.0]")


# Canonical 26-Letter Electro-Gravitational Esper Codex
# All leaf activations map strictly to the 24 canonical leaves in birth.py (Rule D001).
ESPER_CODEX: Final[dict[str, EsperRecord]] = {
    "A": EsperRecord(
        letter="A",
        name="Atomos",
        element="Gravity & Void",
        polarity="Black",
        core_spells=("Warp", "Gravitas"),
        horizon="The appetite of singularities, surrendering control to mystery.",
        leaf_activations={
            "philosophical/structure/chaos": 0.70,
            "philosophical/being/existence": 0.65,
            "experiential/reflection/salience": 0.80,
            "experiential/phase/arousal": 0.50,
            "experiential/phase/valence": 0.40,
            "psychological/contemplation/clarity": 0.45,
            "cultural/justice/honor": 0.55,
        },
    ),
    "B": EsperRecord(
        letter="B",
        name="Bahamut",
        element="Stellar Fire",
        polarity="White",
        core_spells=("Flare", "Radiance"),
        horizon="Sovereignty, righteous awe, leadership without tyranny.",
        leaf_activations={
            "cultural/justice/honor": 0.85,
            "cultural/justice/fairness": 0.80,
            "cultural/efficiency/power": 0.80,
            "philosophical/being/agency": 0.85,
            "experiential/phase/valence": 0.75,
            "psychological/contemplation/confidence": 0.85,
            "philosophical/persistence/continuity": 0.75,
        },
    ),
    "C": EsperRecord(
        letter="C",
        name="Carbuncle",
        element="Prism & Gemlight",
        polarity="White",
        core_spells=("Reflect", "Glitterdust"),
        horizon="Mirror-wisdom: learning by echo rather than impulse.",
        leaf_activations={
            "psychological/contemplation/clarity": 0.85,
            "psychological/truth/fact": 0.80,
            "experiential/synchronization/resonance": 0.85,
            "cultural/justice/fairness": 0.75,
            "philosophical/structure/order": 0.70,
        },
    ),
    "D": EsperRecord(
        letter="D",
        name="Diabolos",
        element="Dream & Midnight",
        polarity="Black",
        core_spells=("Nightmare", "Gravity Well"),
        horizon="Lucid descent into shadow to retrieve forgotten selves.",
        leaf_activations={
            "experiential/reflection/salience": 0.75,
            "experiential/reflection/novelty": 0.70,
            "philosophical/structure/chaos": 0.65,
            "psychological/contemplation/clarity": 0.50,
            "cultural/freedom/self-sufficiency": 0.65,
        },
    ),
    "E": EsperRecord(
        letter="E",
        name="Eden",
        element="Genesis Field",
        polarity="Black",
        core_spells=("Paradise Lost", "Seed"),
        horizon="The terror of pure potential—creation before morality.",
        leaf_activations={
            "philosophical/being/existence": 0.85,
            "experiential/reflection/novelty": 0.85,
            "philosophical/structure/chaos": 0.65,
            "psychological/will/intention": 0.75,
            "cultural/freedom/needlessness": 0.70,
        },
    ),
    "F": EsperRecord(
        letter="F",
        name="Fenrir",
        element="Tempest & Hunger",
        polarity="Black",
        core_spells=("Howl", "Devour"),
        horizon="Wild instinct, teeth of inevitability, endings that liberate.",
        leaf_activations={
            "philosophical/being/agency": 0.85,
            "philosophical/structure/chaos": 0.80,
            "experiential/phase/arousal": 0.80,
            "cultural/freedom/self-sufficiency": 0.75,
            "experiential/reflection/salience": 0.75,
        },
    ),
    "G": EsperRecord(
        letter="G",
        name="Golem",
        element="Stone & Resonance",
        polarity="White",
        core_spells=("Protect", "Tectonic Ward"),
        horizon="Endurance through stillness; the body as cathedral.",
        leaf_activations={
            "philosophical/persistence/discreteness": 0.85,
            "philosophical/structure/order": 0.80,
            "cultural/justice/fairness": 0.80,
            "experiential/synchronization/resonance": 0.75,
            "psychological/contemplation/confidence": 0.75,
        },
    ),
    "H": EsperRecord(
        letter="H",
        name="Hecate",
        element="Crossroads Flame",
        polarity="Black",
        core_spells=("Gate", "Hex"),
        horizon="Liminal choice, the triple path, sorcery of thresholds.",
        leaf_activations={
            "psychological/will/intention": 0.80,
            "philosophical/structure/chaos": 0.65,
            "experiential/reflection/novelty": 0.75,
            "cultural/freedom/self-sufficiency": 0.70,
            "psychological/contemplation/clarity": 0.60,
        },
    ),
    "I": EsperRecord(
        letter="I",
        name="Ifrit",
        element="Volcanic Blaze",
        polarity="Black",
        core_spells=("Hellfire", "Burn"),
        horizon="Purification by ordeal—passion as crucible.",
        leaf_activations={
            "philosophical/being/agency": 0.85,
            "experiential/phase/arousal": 0.85,
            "philosophical/persistence/continuity": 0.75,
            "psychological/will/execution": 0.80,
            "cultural/justice/honor": 0.70,
        },
    ),
    "J": EsperRecord(
        letter="J",
        name="Jinn",
        element="Desert Wind",
        polarity="White",
        core_spells=("Zephyr", "Mirage"),
        horizon="Freedom, trickster insight, the grace of impermanence.",
        leaf_activations={
            "cultural/freedom/needlessness": 0.85,
            "philosophical/structure/chaos": 0.65,
            "experiential/reflection/novelty": 0.75,
            "psychological/contemplation/clarity": 0.70,
            "experiential/reflection/salience": 0.70,
        },
    ),
    "K": EsperRecord(
        letter="K",
        name="Kirin",
        element="Spring-Rain Vitality",
        polarity="White",
        core_spells=("Regen", "Benediction"),
        horizon="Compassion that mends by simply existing.",
        leaf_activations={
            "cultural/justice/fairness": 0.90,
            "experiential/phase/valence": 0.85,
            "experiential/phase/arousal": 0.25,
            "philosophical/being/existence": 0.80,
            "psychological/contemplation/clarity": 0.80,
        },
    ),
    "L": EsperRecord(
        letter="L",
        name="Leviathan",
        element="Tidal Memory",
        polarity="White",
        core_spells=("Deluge", "Tsunami"),
        horizon="Deep emotion, ancestral recall, the oceanic subconscious.",
        leaf_activations={
            "philosophical/persistence/continuity": 0.85,
            "philosophical/being/existence": 0.80,
            "experiential/synchronization/resonance": 0.85,
            "experiential/phase/valence": 0.60,
            "psychological/truth/fact": 0.75,
        },
    ),
    "M": EsperRecord(
        letter="M",
        name="Maduin",
        element="Empathic Pulse",
        polarity="White",
        core_spells=("Embrace", "Sync"),
        horizon="Fusion of hearts; diplomacy between planes.",
        leaf_activations={
            "cultural/justice/fairness": 0.85,
            "experiential/synchronization/resonance": 0.90,
            "cultural/freedom/self-sufficiency": 0.75,
            "experiential/phase/valence": 0.75,
            "psychological/contemplation/clarity": 0.75,
        },
    ),
    "N": EsperRecord(
        letter="N",
        name="Nidhogg",
        element="Venom & Rot",
        polarity="Black",
        core_spells=("Corrode", "Dark Swarm"),
        horizon="The necessary decay that feeds new roots.",
        leaf_activations={
            "philosophical/persistence/continuity": 0.75,
            "philosophical/structure/chaos": 0.70,
            "experiential/phase/valence": 0.35,
            "cultural/efficiency/wastelessness": 0.65,
            "psychological/truth/fact": 0.65,
        },
    ),
    "O": EsperRecord(
        letter="O",
        name="Odin",
        element="Steel & Lightning",
        polarity="Black",
        core_spells=("Zantetsuken", "Cavalry Charge"),
        horizon="Swiftness that decides fate in a single stroke.",
        leaf_activations={
            "philosophical/being/agency": 0.90,
            "psychological/will/execution": 0.90,
            "philosophical/persistence/discreteness": 0.85,
            "cultural/justice/honor": 0.80,
            "experiential/phase/arousal": 0.75,
        },
    ),
    "P": EsperRecord(
        letter="P",
        name="Phoenix",
        element="Resurrection Fire",
        polarity="White",
        core_spells=("Life", "White-Wind"),
        horizon="Rebirth, covenant, the immortality of promise.",
        leaf_activations={
            "philosophical/persistence/continuity": 0.95,
            "cultural/justice/honor": 0.85,
            "experiential/phase/valence": 0.85,
            "psychological/will/intention": 0.80,
            "experiential/reflection/novelty": 0.75,
        },
    ),
    "Q": EsperRecord(
        letter="Q",
        name="Quetzalcoatl",
        element="Sky-Storm & Feather",
        polarity="White",
        core_spells=("Thunder", "Volt-Dance"),
        horizon="Enlightenment delivered as sudden revelation.",
        leaf_activations={
            "philosophical/being/agency": 0.85,
            "experiential/reflection/novelty": 0.85,
            "psychological/contemplation/clarity": 0.85,
            "experiential/phase/arousal": 0.75,
            "cultural/freedom/self-sufficiency": 0.75,
        },
    ),
    "R": EsperRecord(
        letter="R",
        name="Ragnarok",
        element="Cosmic Cataclysm",
        polarity="Black",
        core_spells=("End-of-Days", "Reset"),
        horizon="Closure that prunes timelines, mercy through completion.",
        leaf_activations={
            "philosophical/structure/chaos": 0.85,
            "philosophical/persistence/discreteness": 0.85,
            "psychological/will/execution": 0.80,
            "cultural/efficiency/wastelessness": 0.70,
            "experiential/reflection/salience": 0.80,
        },
    ),
    "S": EsperRecord(
        letter="S",
        name="Siren",
        element="Song & Mind-Tide",
        polarity="White",
        core_spells=("Silence", "Charm"),
        horizon="The ethics of influence, lullabies that disarm violence.",
        leaf_activations={
            "cultural/justice/fairness": 0.85,
            "experiential/synchronization/resonance": 0.90,
            "experiential/phase/arousal": 0.20,
            "cultural/freedom/self-sufficiency": 0.75,
            "psychological/contemplation/clarity": 0.80,
        },
    ),
    "T": EsperRecord(
        letter="T",
        name="Titan",
        element="Continental Strength",
        polarity="White",
        core_spells=("Quake", "Rampart"),
        horizon="Responsibility, bearing weight so others may move.",
        leaf_activations={
            "cultural/justice/fairness": 0.90,
            "cultural/efficiency/power": 0.85,
            "philosophical/persistence/continuity": 0.85,
            "philosophical/persistence/discreteness": 0.85,
            "experiential/synchronization/resonance": 0.80,
        },
    ),
    "U": EsperRecord(
        letter="U",
        name="Ultima",
        element="Pure Mana",
        polarity="White",
        core_spells=("Holy", "Omega Burst"),
        horizon="Essence beyond element—logic of the Logos.",
        leaf_activations={
            "psychological/truth/theory": 0.95,
            "psychological/contemplation/clarity": 0.90,
            "philosophical/structure/order": 0.85,
            "philosophical/being/existence": 0.85,
            "cultural/justice/honor": 0.80,
        },
    ),
    "V": EsperRecord(
        letter="V",
        name="Vajra",
        element="Diamond-Thunder",
        polarity="Black",
        core_spells=("Indra's Wrath", "Static Field"),
        horizon="Authority of shock-truth, the blade of sudden insight.",
        leaf_activations={
            "psychological/truth/fact": 0.90,
            "philosophical/being/agency": 0.85,
            "experiential/phase/arousal": 0.80,
            "cultural/justice/honor": 0.80,
            "philosophical/persistence/discreteness": 0.80,
        },
    ),
    "W": EsperRecord(
        letter="W",
        name="Wendigo",
        element="Frost & Hunger",
        polarity="Black",
        core_spells=("Glacial Bite", "Curse"),
        horizon="The void of obsession, cautionary appetite.",
        leaf_activations={
            "philosophical/structure/chaos": 0.75,
            "experiential/phase/valence": 0.30,
            "experiential/phase/arousal": 0.70,
            "philosophical/persistence/discreteness": 0.75,
            "psychological/contemplation/clarity": 0.50,
        },
    ),
    "X": EsperRecord(
        letter="X",
        name="Xolotl",
        element="Dusk & Afterlife",
        polarity="Black",
        core_spells=("Cross-River", "Eclipse"),
        horizon="Psychopomp wisdom: guiding what must pass.",
        leaf_activations={
            "cultural/justice/honor": 0.75,
            "philosophical/persistence/continuity": 0.80,
            "psychological/contemplation/clarity": 0.70,
            "experiential/synchronization/resonance": 0.75,
            "cultural/justice/fairness": 0.70,
        },
    ),
    "Y": EsperRecord(
        letter="Y",
        name="Yggdrasil",
        element="Root-Cosmos",
        polarity="White",
        core_spells=("Lifewood", "Re-Sprout"),
        horizon="Interconnection, cycles of seasons and selves.",
        leaf_activations={
            "philosophical/persistence/continuity": 0.95,
            "philosophical/being/existence": 0.90,
            "cultural/justice/fairness": 0.85,
            "experiential/synchronization/resonance": 0.85,
            "psychological/contemplation/clarity": 0.80,
        },
    ),
    "Z": EsperRecord(
        letter="Z",
        name="Zodiark",
        element="Star-Archive",
        polarity="Black",
        core_spells=("Fate-Bind", "Astral Seal"),
        horizon="The script of destinies, reading the code inside constellations.",
        leaf_activations={
            "psychological/truth/theory": 0.85,
            "psychological/contemplation/clarity": 0.75,
            "philosophical/structure/order": 0.80,
            "philosophical/persistence/continuity": 0.85,
            "cultural/efficiency/wastelessness": 0.75,
        },
    ),
}


def get_esper_by_letter(char: str) -> EsperRecord:
    """Retrieve an Esper record by single character (case-insensitive)."""
    key = char.strip().upper()
    if key not in ESPER_CODEX:
        raise KeyError(f"No Esper defined for letter {char!r}")
    return ESPER_CODEX[key]


def get_esper_by_name(name: str) -> EsperRecord:
    """Retrieve an Esper record by name (case-insensitive)."""
    target = name.strip().lower()
    for record in ESPER_CODEX.values():
        if record.name.lower() == target:
            return record
    raise KeyError(f"No Esper found with name {name!r}")


def get_word_esper_chord(word: str) -> list[EsperRecord]:
    """Break any word into its sequential sequence of archetypal Espers."""
    chord: list[EsperRecord] = []
    for char in word:
        if char.isalpha():
            chord.append(get_esper_by_letter(char))
    return chord
