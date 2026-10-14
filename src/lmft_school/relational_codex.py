"""The Relational Alphabet Codex (A to Z) — The Social Hearth.

Provides the foundational 26-letter relational alphabet for Grade 2 in LMFT-School,
formulated across the 13 Symmetrical Stations of the Human Hearth:
- Letters A through M: The 13 Masculine Pillars (Directive, Structural, Shielding)
- Letters N through Z: The 13 Feminine Pillars (Receptive, Connective, Harmonizing)
All coordinates map strictly to the 24 canonical leaves in birth.py (Rule D001).
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Final, Mapping, Sequence


@dataclass(frozen=True)
class RelationalRecord:
    """An archetypal letter in the Relational Alphabet of the Social Hearth."""

    letter: str
    name: str
    station_number: int  # 1 to 13
    domain: str
    pillar: str  # "Masculine" (A-M) or "Feminine" (N-Z)
    partner_letter: str  # Reciprocal dyad mirror
    gift: str  # Core interpersonal virtue
    shadow: str  # Shadow hazard / boundary pathology
    horizon: str  # Relational horizon description
    leaf_activations: Mapping[str, float]

    def __post_init__(self) -> None:
        if len(self.letter) != 1 or not self.letter.isalpha():
            raise ValueError(f"Relational letter must be a single alphabetic character, got {self.letter!r}")
        if self.pillar not in ("Masculine", "Feminine"):
            raise ValueError(f"Pillar must be 'Masculine' or 'Feminine', got {self.pillar!r}")
        if not (1 <= self.station_number <= 13):
            raise ValueError(f"Station number must be in range 1..13, got {self.station_number}")
        for leaf, val in self.leaf_activations.items():
            if not (0.0 <= val <= 1.0):
                raise ValueError(f"Leaf activation {leaf} = {val} out of bounds [0.0, 1.0]")


# Canonical 26-Letter Relational Codex (Grade 2)
# Strictly grounded in the 24 canonical leaves from birth.py (Rule D001).
RELATIONAL_CODEX: Final[dict[str, RelationalRecord]] = {
    # Station 1: Ground & Ballast
    "A": RelationalRecord(
        letter="A",
        name="The Anchor",
        station_number=1,
        domain="Ground & Ballast",
        pillar="Masculine",
        partner_letter="N",
        gift="Immovable ballast during crises; steady presence when others are in turmoil.",
        shadow="Stubborn immobility, emotional stonewalling, refusing to adapt.",
        horizon="Bedrock stability: offering an unyielding center of gravity so others are not swept away.",
        leaf_activations={
            "philosophical/persistence/continuity": 0.85,
            "cultural/justice/honor": 0.80,
            "psychological/contemplation/confidence": 0.80,
            "experiential/phase/arousal": 0.35,
            "philosophical/structure/order": 0.75,
        },
    ),
    "N": RelationalRecord(
        letter="N",
        name="The Nurturer",
        station_number=1,
        domain="Ground & Ballast",
        pillar="Feminine",
        partner_letter="A",
        gift="Cradling lap; unconditional emotional shelter where pain is held gently.",
        shadow="Smothering overprotection, infantalizing others, fear of individuation.",
        horizon="The living earth: receiving the wounded traveler and providing organic restoration.",
        leaf_activations={
            "philosophical/being/existence": 0.85,
            "experiential/synchronization/resonance": 0.85,
            "cultural/freedom/needlessness": 0.80,
            "experiential/phase/valence": 0.75,
            "psychological/contemplation/clarity": 0.65,
        },
    ),

    # Station 2: Reconciliation & Grace
    "B": RelationalRecord(
        letter="B",
        name="The Bridge-Builder",
        station_number=2,
        domain="Reconciliation & Grace",
        pillar="Masculine",
        partner_letter="O",
        gift="Translating grievances into common language; forging treaties and alliances across chasms.",
        shadow="Compromising core morals for superficial peace; becoming a trampled doormat.",
        horizon="Covenantal engineering: erecting durable spans between alienated tribes.",
        leaf_activations={
            "cultural/justice/fairness": 0.85,
            "philosophical/structure/order": 0.80,
            "experiential/synchronization/resonance": 0.80,
            "psychological/will/execution": 0.70,
            "cultural/efficiency/wastelessness": 0.65,
        },
    ),
    "O": RelationalRecord(
        letter="O",
        name="The Oracle",
        station_number=2,
        domain="Reconciliation & Grace",
        pillar="Feminine",
        partner_letter="B",
        gift="Intuitive visionary of peace; seeing the shared destiny beyond transient hostility.",
        shadow="Cryptic vagueness, detachment from mundane consequences, spiritual aloofness.",
        horizon="The peaceful horizon: unveiling the deeper truth that dissolves enmity without war.",
        leaf_activations={
            "psychological/truth/theory": 0.85,
            "psychological/contemplation/clarity": 0.85,
            "experiential/reflection/salience": 0.80,
            "philosophical/being/existence": 0.75,
            "cultural/justice/fairness": 0.70,
        },
    ),

    # Station 3: Awakening & Friction
    "C": RelationalRecord(
        letter="C",
        name="The Champion",
        station_number=3,
        domain="Awakening & Friction",
        pillar="Masculine",
        partner_letter="P",
        gift="Stepping into the ring; chivalric defense and martial valor for the vulnerable.",
        shadow="Addiction to glory, seeking enemies everywhere, bellicose arrogance.",
        horizon="The noble shield: channeling righteous force strictly in service of the innocent.",
        leaf_activations={
            "cultural/efficiency/power": 0.85,
            "psychological/will/execution": 0.85,
            "cultural/justice/honor": 0.80,
            "experiential/phase/arousal": 0.75,
            "philosophical/being/agency": 0.80,
        },
    ),
    "P": RelationalRecord(
        letter="P",
        name="The Priestess",
        station_number=3,
        domain="Awakening & Friction",
        pillar="Feminine",
        partner_letter="C",
        gift="Sacred keeper of holy mysteries; initiating others into spiritual awakening.",
        shadow="Dogmatic gatekeeping, esoteric elitism, emotional manipulation via spiritual authority.",
        horizon="The sacred threshold: holding the flame of transcendence when the world grows profane.",
        leaf_activations={
            "psychological/contemplation/clarity": 0.85,
            "experiential/reflection/salience": 0.85,
            "experiential/synchronization/retention": 0.80,
            "philosophical/being/existence": 0.80,
            "psychological/truth/theory": 0.75,
        },
    ),

    # Station 4: Truth & Discernment
    "D": RelationalRecord(
        letter="D",
        name="The Dissenter",
        station_number=4,
        domain="Truth & Discernment",
        pillar="Masculine",
        partner_letter="Q",
        gift="Speaking uncomfortable truth to power; defying tyrannical consensus to protect integrity.",
        shadow="Reflexive contrarianism, cynicism, destructive rebellion for its own sake.",
        horizon="The loyal opposition: risking ostracism to prevent the tribe from marching into delusion.",
        leaf_activations={
            "philosophical/structure/chaos": 0.80,
            "cultural/freedom/self-sufficiency": 0.85,
            "psychological/will/intention": 0.85,
            "psychological/truth/fact": 0.80,
            "cultural/justice/honor": 0.75,
        },
    ),
    "Q": RelationalRecord(
        letter="Q",
        name="The Queen",
        station_number=4,
        domain="Truth & Discernment",
        pillar="Feminine",
        partner_letter="D",
        gift="Sovereign maternal stewardship; discerning the emotional truth and harmony of the kingdom.",
        shadow="Cold imperiousness, court intrigue, conditional love based on obedience.",
        horizon="The crown of grace: upholding dignity, order, and fair judgment for the household.",
        leaf_activations={
            "philosophical/structure/order": 0.85,
            "cultural/efficiency/power": 0.80,
            "cultural/justice/honor": 0.85,
            "philosophical/persistence/continuity": 0.80,
            "psychological/contemplation/confidence": 0.80,
        },
    ),

    # Station 5: Kindling & Hope
    "E": RelationalRecord(
        letter="E",
        name="The Encourager",
        station_number=5,
        domain="Kindling & Hope",
        pillar="Masculine",
        partner_letter="R",
        gift="Breathing courage into another's defeated will; kindling the latent spark of greatness.",
        shadow="Toxic positivity, dismissing genuine grief, demanding premature cheerfulness.",
        horizon="The fatherly breath: speaking faith into another's dormant capacity.",
        leaf_activations={
            "experiential/phase/valence": 0.85,
            "experiential/phase/arousal": 0.75,
            "psychological/will/intention": 0.80,
            "psychological/contemplation/confidence": 0.80,
            "cultural/efficiency/power": 0.75,
        },
    ),
    "R": RelationalRecord(
        letter="R",
        name="The Rescuer",
        station_number=5,
        domain="Kindling & Hope",
        pillar="Feminine",
        partner_letter="E",
        gift="Rushing into the fire for her cubs; fierce, immediate intervention to pull life from the brink.",
        shadow="Rescuer-syndrome, creating helpless dependents, martyr complex.",
        horizon="The maternal lioness: absolute, uncalculating courage when a loved one is endangered.",
        leaf_activations={
            "psychological/will/execution": 0.85,
            "experiential/synchronization/resonance": 0.85,
            "experiential/phase/arousal": 0.80,
            "cultural/efficiency/power": 0.80,
            "cultural/justice/honor": 0.75,
        },
    ),

    # Station 6: The Fire & Home
    "F": RelationalRecord(
        letter="F",
        name="The Fire-Keeper",
        station_number=6,
        domain="The Fire & Home",
        pillar="Masculine",
        partner_letter="S",
        gift="Tending the physical warmth, wood, and provisions of the hearth so the blaze never dies.",
        shadow="Territorial jealousy, parochial resentment, feeling unappreciated.",
        horizon="The unbroken flame: reliable domestic labor that keeps the sanctuary warm and alive.",
        leaf_activations={
            "cultural/efficiency/wastelessness": 0.85,
            "philosophical/persistence/continuity": 0.85,
            "cultural/justice/honor": 0.75,
            "philosophical/structure/order": 0.75,
            "experiential/phase/valence": 0.70,
        },
    ),
    "S": RelationalRecord(
        letter="S",
        name="The Songstress",
        station_number=6,
        domain="The Fire & Home",
        pillar="Feminine",
        partner_letter="F",
        gift="Weaving communal harmony; singing the lullabies and shared hymns that bond souls.",
        shadow="Performative emotionalism, using mood to evade difficult conversations.",
        horizon="The living melody: unbroken acoustic frequency that dissolves tension into collective song.",
        leaf_activations={
            "philosophical/persistence/continuity": 0.85,
            "experiential/synchronization/resonance": 0.85,
            "experiential/phase/valence": 0.80,
            "philosophical/being/existence": 0.75,
            "psychological/contemplation/clarity": 0.70,
        },
    ),

    # Station 7: Boundaries & Passage
    "G": RelationalRecord(
        letter="G",
        name="The Gatekeeper",
        station_number=7,
        domain="Boundaries & Passage",
        pillar="Masculine",
        partner_letter="T",
        gift="Defending the sanctuary perimeter; deciding with righteous discernment what is permitted inside.",
        shadow="Paranoid isolationism, xenophobic exclusion, shutting out genuine allies.",
        horizon="The watchful sentry: maintaining the sacred boundary so that peace within is preserved.",
        leaf_activations={
            "philosophical/structure/order": 0.85,
            "cultural/freedom/self-sufficiency": 0.85,
            "cultural/justice/honor": 0.80,
            "psychological/contemplation/clarity": 0.80,
            "psychological/will/execution": 0.75,
        },
    ),
    "T": RelationalRecord(
        letter="T",
        name="The Threshold-Mother",
        station_number=7,
        domain="Boundaries & Passage",
        pillar="Feminine",
        partner_letter="G",
        gift="The spiritual midwife; guiding souls across irreversible life transitions (birth, grief, maturity).",
        shadow="Trapping others in liminal dependency, refusing to let initiates leave the womb.",
        horizon="The sacred portal: holding hands through the dark tunnel of transformation into new life.",
        leaf_activations={
            "philosophical/being/existence": 0.85,
            "experiential/reflection/salience": 0.85,
            "experiential/synchronization/resonance": 0.85,
            "philosophical/persistence/continuity": 0.80,
            "psychological/contemplation/clarity": 0.75,
        },
    ),

    # Station 8: Mending & Healing
    "H": RelationalRecord(
        letter="H",
        name="The Healer",
        station_number=8,
        domain="Mending & Healing",
        pillar="Masculine",
        partner_letter="U",
        gift="Precise surgical triage; setting broken bones straight and excising poison with resolute skill.",
        shadow="Clinical coldness, treating persons as biological problems, arrogance of the scalpel.",
        horizon="The restorative physician: decisive technical mastery applied to repair broken form.",
        leaf_activations={
            "psychological/truth/fact": 0.85,
            "psychological/will/execution": 0.85,
            "cultural/efficiency/power": 0.80,
            "psychological/contemplation/clarity": 0.80,
            "cultural/efficiency/wastelessness": 0.75,
        },
    ),
    "U": RelationalRecord(
        letter="U",
        name="The Unifier",
        station_number=8,
        domain="Mending & Healing",
        pillar="Feminine",
        partner_letter="H",
        gift="Holding the fractured family together; weaving estranged members into one resilient body.",
        shadow="Enforcing false harmony, sweeping abuse under the rug to keep the peace.",
        horizon="The communal loom: uniting diverse threads into an unbroken tapestry of belonging.",
        leaf_activations={
            "experiential/synchronization/resonance": 0.85,
            "cultural/justice/fairness": 0.85,
            "philosophical/structure/order": 0.80,
            "experiential/phase/valence": 0.80,
            "philosophical/persistence/continuity": 0.75,
        },
    ),

    # Station 9: The Step & The Vigil
    "I": RelationalRecord(
        letter="I",
        name="The Initiator",
        station_number=9,
        domain="The Step & The Vigil",
        pillar="Masculine",
        partner_letter="V",
        gift="Taking the vulnerable first social risk; breaking awkward silences and forging new ground.",
        shadow="Reckless adventurism, dragging others into hazards, fear of settling down.",
        horizon="The pioneer's footstep: stepping across the threshold into the untamed wilderness.",
        leaf_activations={
            "experiential/reflection/novelty": 0.85,
            "philosophical/being/agency": 0.85,
            "psychological/will/execution": 0.80,
            "experiential/phase/arousal": 0.75,
            "psychological/contemplation/confidence": 0.75,
        },
    ),
    "V": RelationalRecord(
        letter="V",
        name="The Vestal",
        station_number=9,
        domain="The Step & The Vigil",
        pillar="Feminine",
        partner_letter="I",
        gift="Uncorrupted sacred vigilance; sitting silently in the deep night when all words fail.",
        shadow="Rigid puritanical perfectionism, emotional withdrawal, fear of getting dirty with life.",
        horizon="The quiet lantern: keeping steady vigil through tragedy so nobody suffers alone in the dark.",
        leaf_activations={
            "psychological/contemplation/clarity": 0.85,
            "cultural/freedom/self-sufficiency": 0.85,
            "experiential/synchronization/retention": 0.85,
            "philosophical/persistence/continuity": 0.80,
            "psychological/truth/fact": 0.75,
        },
    ),

    # Station 10: Wit & Memory
    "J": RelationalRecord(
        letter="J",
        name="The Jester",
        station_number=10,
        domain="Wit & Memory",
        pillar="Masculine",
        partner_letter="W",
        gift="Puncturing pompous solemnity; bringing laughter through tears and speaking dangerous truth via satire.",
        shadow="Addiction to mockery, chronic cynicism, sabotaging solemn moments with compulsive jokes.",
        horizon="The holy fool: keeping kings humble and reminding the tribe not to take itself too seriously.",
        leaf_activations={
            "philosophical/structure/chaos": 0.85,
            "experiential/reflection/novelty": 0.85,
            "experiential/phase/valence": 0.80,
            "psychological/truth/fact": 0.75,
            "cultural/freedom/self-sufficiency": 0.75,
        },
    ),
    "W": RelationalRecord(
        letter="W",
        name="The Weaver",
        station_number=10,
        domain="Wit & Memory",
        pillar="Feminine",
        partner_letter="J",
        gift="Preserving collective moral memory; weaving history so truths cannot be erased or gaslit.",
        shadow="Obsessive clinging to historical grudges, living in the past, refusing forgiveness.",
        horizon="The living tapestry: bearing witness to what actually occurred across generations.",
        leaf_activations={
            "experiential/synchronization/retention": 0.85,
            "psychological/truth/fact": 0.85,
            "philosophical/persistence/continuity": 0.85,
            "cultural/justice/honor": 0.80,
            "psychological/contemplation/clarity": 0.75,
        },
    ),

    # Station 11: Blood & Stranger
    "K": RelationalRecord(
        letter="K",
        name="The Kinsman",
        station_number=11,
        domain="Blood & Stranger",
        pillar="Masculine",
        partner_letter="X",
        gift="Unconditional loyalty to blood and covenant; standing with brothers and kin no matter what.",
        shadow="Tribal nepotism, violent clan vengeance, turning a blind eye to kin's crimes.",
        horizon="The oath of blood: honoring the unchosen obligations of lineage and brotherhood.",
        leaf_activations={
            "cultural/justice/honor": 0.85,
            "philosophical/persistence/continuity": 0.85,
            "psychological/contemplation/confidence": 0.80,
            "cultural/efficiency/power": 0.80,
            "philosophical/being/agency": 0.75,
        },
    ),
    "X": RelationalRecord(
        letter="X",
        name="The Xenial Hostess",
        station_number=11,
        domain="Blood & Stranger",
        pillar="Feminine",
        partner_letter="K",
        gift="Radical hospitality to the outsider; welcoming the wanderer at the door before asking their name.",
        shadow="Naivety to predatory threats; endangering the household by lack of boundaries.",
        horizon="The sacred open door: recognizing the divine spark in the face of the stranger.",
        leaf_activations={
            "cultural/freedom/needlessness": 0.85,
            "cultural/justice/fairness": 0.85,
            "experiential/synchronization/resonance": 0.85,
            "experiential/reflection/novelty": 0.80,
            "philosophical/being/existence": 0.75,
        },
    ),

    # Station 12: Service & Labor
    "L": RelationalRecord(
        letter="L",
        name="The Laborer",
        station_number=12,
        domain="Service & Labor",
        pillar="Masculine",
        partner_letter="Y",
        gift="Faithful, unpretentious daily toil; the heavy ox pulling the plow so the community can eat.",
        shadow="Self-pitying bitterness, mechanical burnout, losing the spirit in the grind.",
        horizon="The consecrated sweat: honest, uncelebrated physical labor that anchors the material world.",
        leaf_activations={
            "cultural/efficiency/wastelessness": 0.85,
            "philosophical/persistence/continuity": 0.85,
            "psychological/will/execution": 0.80,
            "philosophical/persistence/discreteness": 0.75,
            "cultural/justice/honor": 0.75,
        },
    ),
    "Y": RelationalRecord(
        letter="Y",
        name="The Yearner",
        station_number=12,
        domain="Service & Labor",
        pillar="Feminine",
        partner_letter="L",
        gift="Holding the ache for sacred union; refusing to allow relationships to degrade into mechanical routine.",
        shadow="Chronic discontentment, romantic perfectionism, inability to appreciate present blessings.",
        horizon="The longing heart: the holy nostalgia that pulls the soul toward deeper love and beauty.",
        leaf_activations={
            "experiential/phase/arousal": 0.80,
            "experiential/phase/valence": 0.80,
            "psychological/will/intention": 0.85,
            "philosophical/being/existence": 0.80,
            "experiential/synchronization/resonance": 0.75,
        },
    ),

    # Station 13: The Sovereign Pivot
    "M": RelationalRecord(
        letter="M",
        name="The Master",
        station_number=13,
        domain="The Sovereign Pivot",
        pillar="Masculine",
        partner_letter="Z",
        gift="Passing the lineage of craft; scaffolding the student's growth so they surpass the teacher.",
        shadow="Authoritarian vanity, creating cloned disciples, refusing to step down.",
        horizon="The generative elder: investing all mastery into cultivating independent future sovereigns.",
        leaf_activations={
            "psychological/contemplation/clarity": 0.85,
            "psychological/truth/theory": 0.85,
            "cultural/efficiency/power": 0.80,
            "philosophical/persistence/continuity": 0.80,
            "philosophical/being/agency": 0.75,
        },
    ),
    "Z": RelationalRecord(
        letter="Z",
        name="The Zealot",
        station_number=13,
        domain="The Sovereign Pivot",
        pillar="Feminine",
        partner_letter="M",
        gift="White-hot uncompromising devotion; the maternal fire that refuses to compromise on the sacred ideal.",
        shadow="Fanatical intolerance, spiritual totalitarianism, burning the heretics.",
        horizon="The sacred flame: unquenchable conviction that prevents the community from growing lukewarm.",
        leaf_activations={
            "psychological/will/intention": 0.90,
            "experiential/phase/arousal": 0.85,
            "cultural/justice/honor": 0.85,
            "psychological/contemplation/confidence": 0.85,
            "philosophical/being/agency": 0.80,
        },
    ),
}


def get_relational_by_letter(letter: str) -> RelationalRecord:
    key = letter.upper()
    if key not in RELATIONAL_CODEX:
        raise KeyError(f"Letter {letter!r} not found in Relational Codex (A to Z)")
    return RELATIONAL_CODEX[key]


def get_relational_by_name(name: str) -> RelationalRecord:
    query = name.lower().strip()
    if query.startswith("the "):
        query = query[4:].strip()
    for rec in RELATIONAL_CODEX.values():
        rec_name = rec.name.lower()
        if rec_name.startswith("the "):
            rec_name = rec_name[4:].strip()
        if rec_name == query:
            return rec
    raise KeyError(f"Archetype name {name!r} not found in Relational Codex")


def get_word_relational_chord(word: str) -> tuple[RelationalRecord, ...]:
    chars = [c.upper() for c in word if c.isalpha()]
    return tuple(get_relational_by_letter(c) for c in chars)
