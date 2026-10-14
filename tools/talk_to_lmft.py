"""Interactive Living REPL — Talk to Your LMFT Individual.

QUARANTINED DEVELOPER TOOLING ONLY. Not part of runtime core library.

Allows real-time pair interaction with an in-memory LMFT entity:
- Evaluates statements through the 10-faculty Cognitive Heartbeat.
- Displays live mental telemetry (Plasticity α, Coherence, Homeostasis, Action Bids).
- Supports offline consolidation cycles via `/sleep`.
- Persists and restores individual packages via `/save` and `/load`.
"""
import argparse
import os
from pathlib import Path
import sys

# Ensure src is in python path
src_dir = Path(__file__).resolve().parents[1] / "src"
if str(src_dir) not in sys.path:
    sys.path.insert(0, str(src_dir))

from lmft_lab.cognitive_heartbeat import CognitiveHeartbeat
from lmft_lab.individual_package import export_individual, import_individual


# Configure UTF-8 stdout if available
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

HUD_BORDER = "=" * 70


def print_hud(turn_res: dict):
    """Renders a structured, cybernetic mental telemetry box."""
    cycle = turn_res["cycle"]
    reg = turn_res["speaking_register"]
    bid = turn_res["action_bid"]

    coherence = turn_res["coherence"]["global_coherence_index"]
    distortions = len(turn_res["coherence"]["distortions_detected"])
    coh_status = "PASS" if distortions == 0 else f"CAUTION ({distortions} distortions)"

    plasticity = turn_res["plasticity"]["dynamic_alpha"]
    regime = turn_res["plasticity"]["plasticity_regime"]

    homeo_score = turn_res["homeostasis"]["emotional_balance_score"]
    homeo_regime = turn_res["homeostasis"]["homeostatic_regime"]

    cons = turn_res.get("consonance", {})
    mode = cons.get("epistemic_mode", "Standard")
    cons_idx = cons.get("consonance_index", 1.0)
    cons_regime = cons.get("consonance_regime", "Harmonic Integrity")

    journal = turn_res["journal_result"]
    if journal.get("admitted") and journal.get("episode"):
        narrative = journal["episode"].get("english_narrative_reflection", "No reflection generated.")
    else:
        narrative = "Filtered: below saliency threshold (epistemic anti-bloat active; discarded from memory)."

    # Grade 1 Esper Resonance
    try:
        from lmft_school.curriculum_grade_1 import Grade1CurriculumRunner
        runner = Grade1CurriculumRunner()
        esper, score = runner.resolve_dialogue_esper(turn_res["sentence"])
        esper_hud = f"({esper.letter}) {esper.name} [{esper.polarity} | {esper.element}]"
        esper_horizon = esper.horizon[:66]
    except Exception:
        esper_hud = "Standard Cognitive Frame"
        esper_horizon = "Awaiting archetypal resonance."

    # Grade 2 Relational Archetype Resonance
    try:
        from lmft_school.curriculum_grade_2 import Grade2CurriculumRunner
        r_runner = Grade2CurriculumRunner()
        rel_arc, rel_score = r_runner.resolve_dialogue_resonance(turn_res["sentence"])
        rel_hud = f"({rel_arc.letter}) {rel_arc.name} [{rel_arc.pillar} | {rel_arc.domain}]"
        rel_horizon = rel_arc.horizon[:66]
    except Exception:
        rel_hud = "Standard Social Frame"
        rel_horizon = "Awaiting relational resonance."

    print(f"\n+{HUD_BORDER}+")
    print(f"| Turn: {cycle:<3} | alpha: {plasticity:.3f} ({regime:<18}) | Coherence: {coherence:.3f} [{coh_status}] |")
    print(f"| Homeostasis: {homeo_score:.3f} ({homeo_regime:<24}) | Register: {reg:<16} |")
    print(f"| Mode: {mode:<23} | Value Consonance: {cons_idx:.3f} ({cons_regime:<18}) |")
    print(f"| Action Bid: {bid:<56} |")
    print(f"+{HUD_BORDER}+")
    print(f"| Esper Resonance:    {esper_hud:<47} |")
    print(f"| Relational Hearth:  {rel_hud:<47} |")
    print(f"| Relational Horizon: {rel_horizon:<47} |")
    print(f"+{HUD_BORDER}+")
    print(f"| Reflection: {narrative[:66]:<66} |")
    if len(narrative) > 66:
        print(f"|             {narrative[66:132]:<66} |")
    print(f"+{HUD_BORDER}+\n")


def run_interactive_session(load_path: str = None, demo: bool = False):
    """Main loop for interacting with the LMFT individual."""
    heartbeat = CognitiveHeartbeat()

    if load_path and os.path.exists(load_path):
        pkg = import_individual(load_path, verify_seed=True)
        heartbeat.import_individual_package(pkg)
        print(f"[*] Loaded individual package from: {load_path}")
    else:
        print("[*] Initialized fresh individual: 'lmft-individual-01'")

    print("\n" + "=" * 72)
    print("  LMFT Interactive Living Console (Type /help for commands, /quit to exit)")
    print("=" * 72)

    demo_inputs = [
        "The national bank announced low interest loans.",
        "A royal order was delivered to the general.",
        "/sleep",
        "/status",
    ]

    while True:
        try:
            if demo:
                if not demo_inputs:
                    break
                user_input = demo_inputs.pop(0)
                print(f"\n> You: {user_input}")
            else:
                user_input = input("\n> You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nExiting LMFT session.")
            break

        if not user_input:
            continue

        # Command handling
        if user_input.startswith("/"):
            parts = user_input.split()
            cmd = parts[0].lower()

            if cmd in ("/quit", "/exit"):
                print("Farewell.")
                break

            elif cmd == "/help":
                print("\nAvailable Commands:")
                print("  /spell <word>      - Deconstruct a word into its Esper alchemical chord (Grade 1)")
                print("  /chord <word>      - Deconstruct a word into its Relational Hearth chord (Grade 2)")
                print("  /esper <key>       - Inspect an Esper's element, polarity, and horizon (Grade 1)")
                print("  /relational <key>  - Inspect a Relational Archetype's pillar, gift, and shadow (Grade 2)")
                print("  /ledger            - Inspect the Lineage Ledger of developmental milestones")
                print("  /sleep [n]         - Trigger offline memory consolidation ('sleep')")
                print("  /status            - Inspect 24-leaf disposition and long-term rules")
                print("  /save <path>       - Export current individual package to disk")
                print("  /load <path>       - Import individual package from disk")
                print("  /help              - Show this help message")
                print("  /quit or /exit     - Terminate session\n")

            elif cmd == "/spell":
                if len(parts) < 2:
                    print("Usage: /spell <word>")
                    continue
                word = parts[1]
                try:
                    from lmft_school.curriculum_grade_1 import Grade1CurriculumRunner
                    runner = Grade1CurriculumRunner()
                    chord = runner.spell_word_chord(word)
                    print(f"\n=== Alchemical Chord for '{chord.word}' ===")
                    print(f"Polarity Balance: {chord.polarity_counts['White']} White / {chord.polarity_counts['Black']} Black")
                    print(f"Journey: {chord.philosophical_journey}")
                    print("Composite Leaf Activations:")
                    for l, v in sorted(chord.composite_leaf_activations.items()):
                        print(f"  - {l}: {v:.3f}")
                    print("=========================================\n")
                except Exception as e:
                    print(f"Error spelling word: {e}")

            elif cmd == "/chord":
                if len(parts) < 2:
                    print("Usage: /chord <word>")
                    continue
                word = parts[1]
                try:
                    from lmft_school.curriculum_grade_2 import Grade2CurriculumRunner
                    r_runner = Grade2CurriculumRunner()
                    chord = r_runner.spell_word_chord(word)
                    print(f"\n=== Relational Hearth Chord for '{chord.word}' ===")
                    print(f"Pillar Balance: {chord.pillar_counts['Masculine']} Masculine / {chord.pillar_counts['Feminine']} Feminine")
                    print(f"Relational Journey: {chord.relational_journey}")
                    print("Composite Leaf Activations:")
                    for l, v in sorted(chord.composite_leaf_activations.items()):
                        print(f"  - {l}: {v:.3f}")
                    print("================================================\n")
                except Exception as e:
                    print(f"Error spelling relational chord: {e}")

            elif cmd == "/esper":
                if len(parts) < 2:
                    print("Usage: /esper <letter or name>")
                    continue
                target = parts[1]
                try:
                    from lmft_school.esper_codex import get_esper_by_letter, get_esper_by_name
                    if len(target) == 1 and target.isalpha():
                        esp = get_esper_by_letter(target)
                    else:
                        esp = get_esper_by_name(target)
                    print(f"\n=== Esper Archetype: ({esp.letter}) {esp.name} ===")
                    print(f"Element:  {esp.element}")
                    print(f"Polarity: {esp.polarity}")
                    print(f"Spells:   {', '.join(esp.core_spells)}")
                    print(f"Horizon:  {esp.horizon}")
                    print("Canonical Leaf Coordinates:")
                    for l, v in sorted(esp.leaf_activations.items()):
                        print(f"  - {l}: {v:.3f}")
                    print("=======================================\n")
                except Exception as e:
                    print(f"Error inspecting Esper: {e}")

            elif cmd == "/relational":
                if len(parts) < 2:
                    print("Usage: /relational <letter or name>")
                    continue
                target = parts[1]
                try:
                    from lmft_school.relational_codex import get_relational_by_letter, get_relational_by_name
                    if len(target) == 1 and target.isalpha():
                        arc = get_relational_by_letter(target)
                    else:
                        arc = get_relational_by_name(target)
                    print(f"\n=== Relational Archetype: ({arc.letter}) {arc.name} ===")
                    print(f"Domain:   {arc.domain} (Station {arc.station_number})")
                    print(f"Pillar:   {arc.pillar} (Partner: {arc.partner_letter})")
                    print(f"Gift:     {arc.gift}")
                    print(f"Shadow:   {arc.shadow}")
                    print(f"Horizon:  {arc.horizon}")
                    print("Canonical Leaf Coordinates:")
                    for l, v in sorted(arc.leaf_activations.items()):
                        print(f"  - {l}: {v:.3f}")
                    print("================================================\n")
                except Exception as e:
                    print(f"Error inspecting Relational Archetype: {e}")

            elif cmd == "/ledger":
                try:
                    from lmft_school.lineage_vault import read_lineage_ledger
                    ledger = read_lineage_ledger()
                    print(f"\n=== Lineage Ledger: {len(ledger)} Milestones Recorded ===")
                    for m in ledger:
                        print(f"  - [Grade {m['grade_level']}] {m['milestone_label']} | Rules: {m['active_capacity_rules_count']} | Coherence: {m['global_coherence_index']:.3f} | File: {m['checkpoint_file']}")
                    print("========================================================\n")
                except Exception as e:
                    print(f"Error reading ledger: {e}")

            elif cmd == "/sleep":
                cycles = int(parts[1]) if len(parts) > 1 and parts[1].isdigit() else 1
                for i in range(cycles):
                    res = heartbeat.sleep(prune_buffer=True)
                    summary = res["consolidation_summary"]
                    print(f"[*] Sleep Cycle #{res['sleep_cycle']} Complete:")
                    print(f"    - Promoted Rules: {summary.get('promoted_rules_count', 0)}")
                    print(f"    - Reinforced Rules: {summary.get('reinforced_rules_count', 0)}")
                    print(f"    - Pruned Transient Noise: {summary.get('transient_noise_pruned_count', 0)}")
                    print(f"    - Remaining Buffer: {summary.get('remaining_buffer_count', 0)}")
                    print(f"    - Total Active Rules: {res.get('active_long_term_rules', 0)}")

            elif cmd == "/status":
                print(f"\n=== Individual Status: {heartbeat.individual_id} (Cycle: {heartbeat.cycle_count}) ===")
                print(f"Active Capacity Rules ({len(heartbeat.consolidator.long_term_rules)}):")
                for r_id, r in heartbeat.consolidator.long_term_rules.items():
                    print(f"  - [{r['lemma']}] pattern: '{r['core_pattern']}' | weight: {r['weight']} | bid: '{r['action_bid']}'")
                print(f"Episodic Journal Entries: {len(heartbeat.journal.entries)}")
                print("Canonical Disposition Sample:")
                for k in ["philosophical/structure/order", "psychological/contemplation/clarity", "experiential/phase/arousal"]:
                    print(f"  - {k}: {heartbeat.disposition.dials.get(k, 0.5):.3f}")

            elif cmd == "/save":
                if len(parts) < 2:
                    print("Usage: /save <filename.lmft.json>")
                    continue
                save_path = parts[1]
                pkg = heartbeat.export_individual_package()
                export_individual(pkg, save_path, description="Saved via talk_to_lmft CLI")
                print(f"[*] Successfully saved package to {save_path}")

            elif cmd == "/load":
                if len(parts) < 2:
                    print("Usage: /load <filename.lmft.json>")
                    continue
                load_file = parts[1]
                if not os.path.exists(load_file):
                    print(f"Error: file not found: {load_file}")
                    continue
                pkg = import_individual(load_file, verify_seed=True)
                heartbeat.import_individual_package(pkg)
                print(f"[*] Successfully restored individual from {load_file}")

            else:
                print(f"Unknown command: {cmd}. Type /help for options.")
            continue

        # Regular cognitive waking turn
        turn_res = heartbeat.interact(sentence=user_input)
        print_hud(turn_res)


def resolve_grade_checkpoint(grade: int | None, load_path: str | None) -> str | None:
    """Finds a checkpoint path based on explicit flag or grade level."""
    if load_path:
        return load_path
    if grade is None:
        return None

    checkpoints_dir = Path(__file__).resolve().parents[1] / "checkpoints"
    if not checkpoints_dir.exists():
        return None

    matches = list(checkpoints_dir.glob(f"*grade{grade}*.lmft.json"))
    if matches:
        # Return most recent
        return str(sorted(matches, key=lambda p: p.stat().st_mtime)[-1])
    return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Talk to your LMFT individual in real time.")
    parser.add_argument("--load", type=str, default=None, help="Path to .lmft.json file to load.")
    parser.add_argument("--grade", type=int, default=None, choices=[0, 1, 2], help="Load milestone checkpoint for Grade 0, 1, or 2.")
    parser.add_argument("--demo", action="store_true", help="Run automated non-interactive demonstration.")
    args = parser.parse_args()

    resolved_path = resolve_grade_checkpoint(args.grade, args.load)
    run_interactive_session(load_path=resolved_path, demo=args.demo)
