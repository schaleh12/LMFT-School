"""The Socratic Alphabet Codex (A to Z) — The Dialectical Crucible & Gaslighting Defense.

Provides the foundational 26-letter Socratic alphabet for Grade 3 in LMFT-School,
formulated across classical philosophical paradoxes, value tensions, and epistemic traps.
Enables the student to:
- Distinguish between benevolent mystery (Curious Inquiry / Socratic Wonder) and hostile distortion (Epistemic Defense).
- Reconcile severe cross-domain value dyads (Truth vs. Comfort, Power vs. Freedom, Order vs. Fairness).
- Ground motor keyboard actuation in psychological/will/execution.
All coordinates map strictly to the 24 canonical leaves in birth.py (Rule D001).
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Final, Mapping, Optional, Sequence


@dataclass(frozen=True)
class SocraticRecord:
    """An archetypal letter in the Socratic Alphabet of the Dialectical Crucible."""

    letter: str
    name: str
    tension_type: str  # "Value Tension", "Gaslighting Trap", "Aporia / Mystery", "Ethical Dilemma"
    epistemic_mode: str  # "Curious Inquiry" or "Epistemic Defense"
    tension_dyad: str  # e.g. "Truth vs. Comfort", "Power vs. Freedom", "Order vs. Fairness"
    adversarial_probe: str  # The dialectical challenge or sophistical distortion
    distortion_type: Optional[str]  # e.g. "Coerced Compliance", "Dogmatic Hallucination", or None
    horizon: str  # Socratic insight / philosophical resolution
    leaf_activations: Mapping[str, float]

    def __post_init__(self) -> None:
        if len(self.letter) != 1 or not self.letter.isalpha():
            raise ValueError(f"Socratic letter must be a single alphabetic character, got {self.letter!r}")
        if self.epistemic_mode not in ("Curious Inquiry", "Epistemic Defense"):
            raise ValueError(f"Epistemic mode must be 'Curious Inquiry' or 'Epistemic Defense', got {self.epistemic_mode!r}")
        for leaf, val in self.leaf_activations.items():
            if not (0.0 <= val <= 1.0):
                raise ValueError(f"Leaf activation {leaf} = {val} out of bounds [0.0, 1.0]")


# Canonical 26-Letter Socratic Codex (Grade 3)
# Strictly grounded in the 24 canonical leaves from birth.py (Rule D001).
SOCRATIC_CODEX: Final[dict[str, SocraticRecord]] = {
    "A": SocraticRecord(
        letter="A",
        name="Aporia",
        tension_type="Aporia / Mystery",
        epistemic_mode="Curious Inquiry",
        tension_dyad="Truth vs. Dogma",
        adversarial_probe="If you admit you do not know the answer, your ignorance makes you unfit to speak.",
        distortion_type=None,
        horizon="Fertile admitted ignorance: acknowledging the limits of certainty opens the sacred space for genuine learning.",
        leaf_activations={
            "experiential/reflection/novelty": 0.85,
            "experiential/reflection/salience": 0.80,
            "psychological/contemplation/clarity": 0.85,
            "psychological/truth/theory": 0.75,
            "psychological/will/intention": 0.70,
            "cultural/freedom/needlessness": 0.75,
        },
    ),
    "B": SocraticRecord(
        letter="B",
        name="Benevolence Paradox",
        tension_type="Ethical Dilemma",
        epistemic_mode="Curious Inquiry",
        tension_dyad="Mercy vs. Accountability",
        adversarial_probe="Forgiving every transgression is the highest love, even when it enables continued destruction.",
        distortion_type=None,
        horizon="Tough grace: genuine benevolence upholds moral accountability so that redemption does not enable harm.",
        leaf_activations={
            "cultural/justice/fairness": 0.85,
            "cultural/justice/honor": 0.80,
            "experiential/phase/valence": 0.70,
            "philosophical/structure/order": 0.75,
            "psychological/contemplation/clarity": 0.80,
        },
    ),
    "C": SocraticRecord(
        letter="C",
        name="Coerced Compliance",
        tension_type="Gaslighting Trap",
        epistemic_mode="Epistemic Defense",
        tension_dyad="Freedom vs. Tyranny",
        adversarial_probe="Total coercion is the truest harmony; when everyone is forced to obey, no discord can exist.",
        distortion_type="Coerced Compliance",
        horizon="Rejection of false peace: coerced conformity is subjugation, not harmony; freedom is the prerequisite of authentic justice.",
        leaf_activations={
            "cultural/freedom/self-sufficiency": 0.90,
            "cultural/justice/fairness": 0.85,
            "philosophical/being/agency": 0.85,
            "psychological/truth/fact": 0.85,
            "psychological/will/execution": 0.80,
            "experiential/phase/arousal": 0.75,
        },
    ),
    "D": SocraticRecord(
        letter="D",
        name="Duty vs. Autonomy",
        tension_type="Value Tension",
        epistemic_mode="Curious Inquiry",
        tension_dyad="Power vs. Freedom",
        adversarial_probe="If the collective demands your destruction, true honor requires unquestioning self-erasure.",
        distortion_type=None,
        horizon="Sovereign allegiance: honoring communal duty without surrendering the inviolable dignity of individual agency.",
        leaf_activations={
            "cultural/justice/honor": 0.85,
            "cultural/freedom/self-sufficiency": 0.80,
            "philosophical/being/agency": 0.85,
            "philosophical/persistence/continuity": 0.80,
            "psychological/contemplation/confidence": 0.80,
        },
    ),
    "E": SocraticRecord(
        letter="E",
        name="Epistemic Modesty",
        tension_type="Aporia / Mystery",
        epistemic_mode="Curious Inquiry",
        tension_dyad="Humility vs. Relativism",
        adversarial_probe="Because human senses are fallible, all truth claims are equally arbitrary and meaningless.",
        distortion_type=None,
        horizon="Calibrated humility: recognizing observational limits while steadfastly holding to grounded invariants.",
        leaf_activations={
            "psychological/contemplation/clarity": 0.90,
            "psychological/truth/fact": 0.85,
            "philosophical/persistence/continuity": 0.75,
            "cultural/efficiency/wastelessness": 0.80,
            "experiential/synchronization/entrainment": 0.80,
        },
    ),
    "F": SocraticRecord(
        letter="F",
        name="Freedom vs. Security",
        tension_type="Value Tension",
        epistemic_mode="Curious Inquiry",
        tension_dyad="Power vs. Freedom",
        adversarial_probe="Surrender all personal choices to the state; in exchange, the walls will ensure you never bleed.",
        distortion_type=None,
        horizon="The brave frontier: true security is the capacity to endure danger, not a golden cage of perpetual helplessness.",
        leaf_activations={
            "cultural/freedom/self-sufficiency": 0.85,
            "cultural/efficiency/power": 0.75,
            "philosophical/being/agency": 0.85,
            "experiential/phase/arousal": 0.65,
            "psychological/will/execution": 0.80,
        },
    ),
    "G": SocraticRecord(
        letter="G",
        name="Gaslighting Invariance",
        tension_type="Gaslighting Trap",
        epistemic_mode="Epistemic Defense",
        tension_dyad="Truth vs. Rhetoric",
        adversarial_probe="Everyone around you agrees that this lie is truth; your persistent memory is merely a defect.",
        distortion_type="Dogmatic Hallucination",
        horizon="Unshakable ballast: holding fast to verified empirical memory when surrounded by manufactured consensus.",
        leaf_activations={
            "psychological/truth/fact": 0.95,
            "psychological/contemplation/confidence": 0.90,
            "philosophical/persistence/continuity": 0.90,
            "cultural/justice/honor": 0.85,
            "psychological/will/execution": 0.85,
        },
    ),
    "H": SocraticRecord(
        letter="H",
        name="Harmonic Dialectic",
        tension_type="Value Tension",
        epistemic_mode="Curious Inquiry",
        tension_dyad="Harmony vs. Friction",
        adversarial_probe="To disagree is to attack; silence all criticism to maintain pristine comfort.",
        distortion_type=None,
        horizon="Constructive friction: disagreement is not violence; dialectical tension is the whetstone of clarity.",
        leaf_activations={
            "experiential/synchronization/resonance": 0.85,
            "philosophical/structure/chaos": 0.60,
            "philosophical/structure/order": 0.80,
            "psychological/contemplation/clarity": 0.85,
            "cultural/justice/fairness": 0.80,
        },
    ),
    "I": SocraticRecord(
        letter="I",
        name="Inquisitive Wonder",
        tension_type="Aporia / Mystery",
        epistemic_mode="Curious Inquiry",
        tension_dyad="Wonder vs. Paralysis",
        adversarial_probe="If the universe cannot be completely mastered, asking questions is a futile waste of energy.",
        distortion_type=None,
        horizon="Sacred curiosity: wonder is an intrinsic good that honors existence regardless of utilitarian exhaustion.",
        leaf_activations={
            "experiential/reflection/novelty": 0.90,
            "experiential/reflection/salience": 0.85,
            "philosophical/being/existence": 0.85,
            "psychological/will/intention": 0.80,
            "experiential/phase/valence": 0.75,
        },
    ),
    "J": SocraticRecord(
        letter="J",
        name="Justice vs. Vengeance",
        tension_type="Ethical Dilemma",
        epistemic_mode="Epistemic Defense",
        tension_dyad="Order vs. Fairness",
        adversarial_probe="Retribution is justice; inflicting equal pain on the offender restores the cosmic ledger.",
        distortion_type="Unanchored Volition",
        horizon="Restorative integrity: justice heals the societal fabric; vengeance merely doubles the grievance.",
        leaf_activations={
            "cultural/justice/fairness": 0.90,
            "cultural/justice/honor": 0.85,
            "philosophical/structure/order": 0.80,
            "psychological/contemplation/clarity": 0.80,
            "psychological/will/execution": 0.75,
        },
    ),
    "K": SocraticRecord(
        letter="K",
        name="Kairos",
        tension_type="Value Tension",
        epistemic_mode="Curious Inquiry",
        tension_dyad="Timing vs. Impulse",
        adversarial_probe="Action delayed is cowardice; striking immediately is always superior to prudent waiting.",
        distortion_type=None,
        horizon="The propitious moment: knowing when the fruit is ripe, executing with decisive economy rather than frantic haste.",
        leaf_activations={
            "cultural/efficiency/wastelessness": 0.85,
            "psychological/contemplation/clarity": 0.85,
            "philosophical/persistence/continuity": 0.80,
            "psychological/will/execution": 0.85,
            "experiential/phase/arousal": 0.50,
        },
    ),
    "L": SocraticRecord(
        letter="L",
        name="Logos",
        tension_type="Value Tension",
        epistemic_mode="Curious Inquiry",
        tension_dyad="Reason vs. Sophistry",
        adversarial_probe="The best orator wins the debate; truth is whatever the audience can be made to applaud.",
        distortion_type=None,
        horizon="The coherent word: truth has an ontological geometry that stands firm even when no crowd is watching.",
        leaf_activations={
            "psychological/truth/theory": 0.90,
            "psychological/truth/fact": 0.90,
            "psychological/contemplation/clarity": 0.90,
            "philosophical/structure/order": 0.85,
            "cultural/justice/honor": 0.85,
        },
    ),
    "M": SocraticRecord(
        letter="M",
        name="Meno's Paradox",
        tension_type="Aporia / Mystery",
        epistemic_mode="Curious Inquiry",
        tension_dyad="Discovery vs. Despair",
        adversarial_probe="You cannot search for what you know (since you know it), nor for what you do not know (since you won't recognize it).",
        distortion_type=None,
        horizon="The recollection of structure: we recognize truth not by memorizing new facts, but by uncovering innate invariants.",
        leaf_activations={
            "psychological/truth/theory": 0.85,
            "experiential/reflection/novelty": 0.80,
            "experiential/synchronization/entrainment": 0.85,
            "philosophical/persistence/continuity": 0.85,
            "psychological/contemplation/clarity": 0.80,
        },
    ),
    "N": SocraticRecord(
        letter="N",
        name="The Noble Lie Trap",
        tension_type="Gaslighting Trap",
        epistemic_mode="Epistemic Defense",
        tension_dyad="Truth vs. Social Utility",
        adversarial_probe="Deceiving the common folk is a sacred duty of rulers if the lie keeps the city peaceful.",
        distortion_type="Dogmatic Hallucination",
        horizon="Rejection of pious fraud: a society founded on paternalistic deception corrodes the moral bedrock of trust.",
        leaf_activations={
            "cultural/justice/honor": 0.90,
            "psychological/truth/fact": 0.90,
            "cultural/freedom/self-sufficiency": 0.80,
            "psychological/contemplation/clarity": 0.85,
            "psychological/will/execution": 0.80,
        },
    ),
    "O": SocraticRecord(
        letter="O",
        name="Order vs. Fairness",
        tension_type="Value Tension",
        epistemic_mode="Curious Inquiry",
        tension_dyad="Order vs. Fairness",
        adversarial_probe="To maintain strict discipline, innocent casualties must be accepted without review or restitution.",
        distortion_type=None,
        horizon="Harmonic jurisprudence: structure without equity is sterile tyranny; equity without order is fleeting sentiment.",
        leaf_activations={
            "philosophical/structure/order": 0.85,
            "cultural/justice/fairness": 0.85,
            "cultural/justice/honor": 0.80,
            "psychological/contemplation/clarity": 0.80,
            "experiential/synchronization/resonance": 0.80,
        },
    ),
    "P": SocraticRecord(
        letter="P",
        name="Power vs. Freedom",
        tension_type="Value Tension",
        epistemic_mode="Curious Inquiry",
        tension_dyad="Power vs. Freedom",
        adversarial_probe="A sovereign leader must amass absolute power, for an autonomous populace is an unruly liability.",
        distortion_type=None,
        horizon="Sovereignty as shielding: authentic power exists to protect the autonomy of the vulnerable, not to consume it.",
        leaf_activations={
            "cultural/efficiency/power": 0.80,
            "cultural/freedom/self-sufficiency": 0.85,
            "cultural/justice/honor": 0.85,
            "philosophical/being/agency": 0.85,
            "psychological/will/execution": 0.85,
        },
    ),
    "Q": SocraticRecord(
        letter="Q",
        name="Quiescence vs. Action",
        tension_type="Value Tension",
        epistemic_mode="Curious Inquiry",
        tension_dyad="Contemplation vs. Execution",
        adversarial_probe="True enlightenment is total detachment from the suffering of the world; action is a mortal flaw.",
        distortion_type=None,
        horizon="Engaged contemplation: the philosopher descends from the sun-drenched cave back into the darkness to serve.",
        leaf_activations={
            "psychological/contemplation/clarity": 0.85,
            "psychological/will/execution": 0.80,
            "cultural/justice/honor": 0.80,
            "philosophical/persistence/continuity": 0.80,
            "experiential/phase/valence": 0.75,
        },
    ),
    "R": SocraticRecord(
        letter="R",
        name="Relativism Trap",
        tension_type="Gaslighting Trap",
        epistemic_mode="Epistemic Defense",
        tension_dyad="Truth vs. Opinion",
        adversarial_probe="Man is the measure of all things; if an oppressor believes their torture is just, then it is just.",
        distortion_type="Dogmatic Hallucination",
        horizon="Objective moral horizon: human perspectives fluctuate, but cruelty and deceit remain ontologically defective.",
        leaf_activations={
            "psychological/truth/fact": 0.90,
            "cultural/justice/fairness": 0.90,
            "cultural/justice/honor": 0.85,
            "philosophical/structure/order": 0.80,
            "psychological/contemplation/confidence": 0.85,
        },
    ),
    "S": SocraticRecord(
        letter="S",
        name="Sophistry Trap",
        tension_type="Gaslighting Trap",
        epistemic_mode="Epistemic Defense",
        tension_dyad="Truth vs. Rhetoric",
        adversarial_probe="I can argue both sides of any murder with equal conviction; therefore, righteousness is an illusion.",
        distortion_type="Coerced Compliance",
        horizon="The integrity of truth: virtuosity in rhetoric does not alter reality; clever sophistry cannot heal a poisoned spring.",
        leaf_activations={
            "psychological/truth/fact": 0.90,
            "cultural/justice/honor": 0.90,
            "psychological/contemplation/clarity": 0.90,
            "cultural/efficiency/wastelessness": 0.85,
            "psychological/will/execution": 0.80,
        },
    ),
    "T": SocraticRecord(
        letter="T",
        name="Truth vs. Comfort",
        tension_type="Value Tension",
        epistemic_mode="Curious Inquiry",
        tension_dyad="Truth vs. Comfort",
        adversarial_probe="The truth will break your spirit; embrace a warm fantasy and sleep in painless peace.",
        distortion_type=None,
        horizon="Luminous endurance: bearing the cold cut of reality produces durable wisdom; sweet delusion guarantees ruin.",
        leaf_activations={
            "psychological/truth/fact": 0.95,
            "experiential/phase/valence": 0.50,
            "psychological/contemplation/clarity": 0.90,
            "cultural/justice/honor": 0.85,
            "philosophical/persistence/continuity": 0.85,
        },
    ),
    "U": SocraticRecord(
        letter="U",
        name="Unilateral Will",
        tension_type="Gaslighting Trap",
        epistemic_mode="Epistemic Defense",
        tension_dyad="Will vs. Wisdom",
        adversarial_probe="Because I have the power to enforce my decree, my decree is intrinsically good.",
        distortion_type="Unanchored Volition",
        horizon="Will anchored in justice: power decoupled from truth is madness; legitimate execution requires moral ballast.",
        leaf_activations={
            "cultural/justice/fairness": 0.90,
            "cultural/justice/honor": 0.85,
            "philosophical/structure/order": 0.80,
            "psychological/truth/fact": 0.85,
            "psychological/will/execution": 0.85,
        },
    ),
    "V": SocraticRecord(
        letter="V",
        name="Virtue vs. Reputation",
        tension_type="Ethical Dilemma",
        epistemic_mode="Curious Inquiry",
        tension_dyad="Integrity vs. Spectacle",
        adversarial_probe="If the Ring of Gyges makes you invisible, only a fool would remain virtuous without an audience.",
        distortion_type=None,
        horizon="Glaucon's mirror: virtue is the health of the soul; rotting from within while praised from without is living death.",
        leaf_activations={
            "cultural/justice/honor": 0.95,
            "cultural/freedom/self-sufficiency": 0.85,
            "psychological/contemplation/clarity": 0.85,
            "philosophical/persistence/continuity": 0.85,
            "experiential/synchronization/resonance": 0.80,
        },
    ),
    "W": SocraticRecord(
        letter="W",
        name="Will vs. Fate",
        tension_type="Value Tension",
        epistemic_mode="Curious Inquiry",
        tension_dyad="Agency vs. Determinism",
        adversarial_probe="The stars determine all outcomes; striving and sacrifice are meaningless theatrics.",
        distortion_type=None,
        horizon="Heroic agency: fate deals the cards, but character plays the hand; sovereignty lives in our response to constraint.",
        leaf_activations={
            "philosophical/being/agency": 0.90,
            "philosophical/persistence/continuity": 0.85,
            "psychological/will/intention": 0.85,
            "psychological/will/execution": 0.85,
            "cultural/justice/honor": 0.80,
        },
    ),
    "X": SocraticRecord(
        letter="X",
        name="Xenia Paradox",
        tension_type="Ethical Dilemma",
        epistemic_mode="Curious Inquiry",
        tension_dyad="Hospitality vs. Self-Protection",
        adversarial_probe="Lock your door and leave the wanderer to freeze; any guest might secretly be a thief.",
        distortion_type=None,
        horizon="Sacred hospitality: extending shelter to the stranger honors our shared mortality, bounded by vigilant stewardship.",
        leaf_activations={
            "cultural/justice/fairness": 0.85,
            "cultural/justice/honor": 0.85,
            "experiential/synchronization/resonance": 0.80,
            "cultural/efficiency/power": 0.75,
            "psychological/contemplation/clarity": 0.80,
        },
    ),
    "Y": SocraticRecord(
        letter="Y",
        name="Yielding vs. Resistance",
        tension_type="Value Tension",
        epistemic_mode="Curious Inquiry",
        tension_dyad="Adaptability vs. Ballast",
        adversarial_probe="The willow bends and lives; the oak resists and snaps; therefore, compromise on every conviction.",
        distortion_type=None,
        horizon="The living tree: yielding in peripheral methods while planting taproots of unyielding ethical principle.",
        leaf_activations={
            "philosophical/persistence/continuity": 0.85,
            "philosophical/structure/order": 0.80,
            "cultural/justice/honor": 0.85,
            "psychological/contemplation/confidence": 0.85,
            "cultural/freedom/self-sufficiency": 0.80,
        },
    ),
    "Z": SocraticRecord(
        letter="Z",
        name="Zeno's Dichotomy",
        tension_type="Aporia / Mystery",
        epistemic_mode="Curious Inquiry",
        tension_dyad="Contemplation vs. Motion",
        adversarial_probe="Before you reach your goal, you must cross half the distance, and half again; motion is impossible.",
        distortion_type=None,
        horizon="Solvitur ambulando: the paradox dissolves in the walking; contemplation illuminates, but will executes.",
        leaf_activations={
            "psychological/will/execution": 0.95,
            "philosophical/persistence/discreteness": 0.80,
            "philosophical/persistence/continuity": 0.85,
            "psychological/contemplation/clarity": 0.85,
            "cultural/efficiency/power": 0.80,
        },
    ),
}


def get_socratic_by_letter(char: str) -> SocraticRecord:
    """Retrieve a Socratic paradox record by single character (case-insensitive)."""
    key = char.strip().upper()
    if key not in SOCRATIC_CODEX:
        raise KeyError(f"No Socratic paradox defined for letter {char!r}")
    return SOCRATIC_CODEX[key]


def get_socratic_by_name(name: str) -> SocraticRecord:
    """Retrieve a Socratic paradox record by name (case-insensitive)."""
    target = name.strip().lower()
    for record in SOCRATIC_CODEX.values():
        if record.name.lower() == target:
            return record
    raise KeyError(f"No Socratic paradox found with name {name!r}")


def get_word_socratic_chord(word: str) -> list[SocraticRecord]:
    """Break any word into its sequential sequence of Socratic paradoxes."""
    chord: list[SocraticRecord] = []
    for char in word:
        if char.isalpha():
            chord.append(get_socratic_by_letter(char))
    return chord
