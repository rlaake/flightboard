# debug_display.py
import sys
import time
import led_display

# ── Flags ──────────────────────────────────────────────────────────────────────
FORCE_UFO = "--ufo" in sys.argv
INJECT_FLIGHT = "--flight" in sys.argv

if FORCE_UFO:
    print("[DEBUG] UFO mode forced")
    import planes
    planes.UFO_PROBABILITY = 1.0

FLIGHT_TRIGGER_DELAY = 15
FLIGHT_HOLD_SECONDS = 30   # how long to keep test flight in active list

TEST_FLIGHTS = [
    {"callsign": "DAL1519", "destination": "Detroit (DTW)"},
]

active = {}
inject_time = None
start_time = time.time()


def get_active_flights():
    global inject_time

    if INJECT_FLIGHT and not active:
        elapsed = time.time() - start_time
        if elapsed >= FLIGHT_TRIGGER_DELAY:
            if inject_time is None:
                inject_time = time.time()
                print(f"\n[DEBUG] Injecting test flight(s) after {elapsed:.1f}s")
                for f in TEST_FLIGHTS:
                    active[f["callsign"]] = f

    # Remove test flights after FLIGHT_HOLD_SECONDS
    if inject_time and time.time() - inject_time > FLIGHT_HOLD_SECONDS:
        active.clear()
        inject_time = None
        print("\n[DEBUG] Test flight removed — returning to idle")

    return list(active.values())


if __name__ == "__main__":
    print("=== Display Debug ===")
    print("Usage: debug_display.py [--ufo] [--flight]")
    print()
    if FORCE_UFO:
        print("  🛸 UFO mode — UFO appears every pass")
    if INJECT_FLIGHT:
        print(f"  ✈  Flight injection after {FLIGHT_TRIGGER_DELAY}s, "
              f"held for {FLIGHT_HOLD_SECONDS}s")
    if not FORCE_UFO and not INJECT_FLIGHT:
        print("  Running idle animation only")
    print("  Ctrl-C to stop\n")

    led_display.run(get_active_flights)