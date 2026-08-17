# debug_display.py
# Tests led_display idle animation and flight display in isolation.
# No ADS-B polling, no MSP scraping.
import time
import led_display

# --- Config ---
# Set to None to only test idle animation
# Set to a list of flights to test flight display after a delay
TEST_FLIGHTS = [
    {"callsign": "DAL1519", "destination": "Detroit (DTW)"},
]
FLIGHT_TRIGGER_DELAY = 15  # seconds of idle before injecting a test flight

# --- State ---
flights_injected = False
start_time = time.time()
display_queue = []

def get_display_flights():
    global flights_injected

    if TEST_FLIGHTS and not flights_injected:
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
    # Reset so it can trigger again after the next delay
    if not display_queue:
        flights_injected = False

if __name__ == "__main__":
    print("=== Display Debug ===")
    print(f"Idle animation will run for {FLIGHT_TRIGGER_DELAY}s")
    print(f"Then inject: {[f['callsign'] for f in TEST_FLIGHTS] if TEST_FLIGHTS else 'nothing'}")
    print("Ctrl-C to stop\n")
    led_display.run(get_display_flights, consume_display_flight)