# debug_display.py
import sys
import time
import led_display
import weather

# ── Flags ──────────────────────────────────────────────────────────────────────
FORCE_UFO = "--ufo" in sys.argv
INJECT_FLIGHT = "--flight" in sys.argv
FORCE_WEATHER = "--weather" in sys.argv

if FORCE_UFO:
    print("[DEBUG] UFO mode forced")
    import planes
    planes.UFO_PROBABILITY = 1.0

if FORCE_WEATHER:
    print("[DEBUG] Weather mode forced — triggering immediately")
    import config
    config.WEATHER_DISPLAY_INTERVAL = 5  # show after 5 seconds

FLIGHT_TRIGGER_DELAY = 15
FLIGHT_HOLD_SECONDS = 30

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

    if inject_time and time.time() - inject_time > FLIGHT_HOLD_SECONDS:
        active.clear()
        inject_time = None
        print("\n[DEBUG] Test flight removed — returning to idle")

    return list(active.values())


if __name__ == "__main__":
    print("=== Display Debug ===")
    print("Usage: debug_display.py [--ufo] [--flight] [--weather]")
    print()
    if FORCE_UFO:
        print("  🛸 UFO mode — UFO appears every pass")
    if INJECT_FLIGHT:
        print(f"  ✈  Flight injection after {FLIGHT_TRIGGER_DELAY}s, "
              f"held for {FLIGHT_HOLD_SECONDS}s")
    if FORCE_WEATHER:
        print("  🌤  Weather forced — displays after 5s")
    if not any([FORCE_UFO, INJECT_FLIGHT, FORCE_WEATHER]):
        print("  Running idle animation only")
    print("  Ctrl-C to stop\n")

    weather.start()
    led_display.run(get_active_flights)