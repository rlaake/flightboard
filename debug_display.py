# debug_display.py
import sys
import time
import led_display

# ── Flags ──────────────────────────────────────────────────────────────────────
FORCE_UFO = "--ufo" in sys.argv
INJECT_FLIGHT = "--flight" in sys.argv

if FORCE_UFO:
    print("[DEBUG] UFO mode forced — overriding probability")
    import planes
    planes.UFO_PROBABILITY = 1.0

# ── Display queue ──────────────────────────────────────────────────────────────
FLIGHT_TRIGGER_DELAY = 15  # seconds before injecting test flight

TEST_FLIGHTS = [
    {"callsign": "DAL1519", "destination": "Detroit (DTW)"},
]

flights_injected = False
start_time = time.time()
display_queue = []


def get_display_flights():
    global flights_injected

    if INJECT_FLIGHT and not flights_injected:
        elapsed = time.time() - start_time
        if elapsed >= FLIGHT_TRIGGER_DELAY:
            print(f"\n[DEBUG] Injecting test flight(s) after {elapsed:.1f}s")
            display_queue.extend(TEST_FLIGHTS)
            flights_injected = True

    return list(display_queue)


def consume_display_flight(callsign):
    global flights_injected
    for i, f in enumerate(display_queue):
        if f["callsign"] == callsign:
            display_queue.pop(i)
            print(f"[DEBUG] Consumed {callsign} from display queue")
            break
    if not display_queue:
        flights_injected = False


if __name__ == "__main__":
    print("=== Display Debug ===")
    print("Usage: debug_display.py [--ufo] [--flight]")
    print()
    if FORCE_UFO:
        print("  🛸 UFO mode — UFO appears every pass")
    if INJECT_FLIGHT:
        print(f"  ✈  Flight injection — test flight after {FLIGHT_TRIGGER_DELAY}s")
    if not FORCE_UFO and not INJECT_FLIGHT:
        print("  Running idle animation only")
    print("  Ctrl-C to stop\n")

    led_display.run(get_display_flights, consume_display_flight)