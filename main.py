# main.py
import flight_matcher
import led_display

if __name__ == "__main__":
    print("=== Flight Board Starting ===")
    flight_matcher.start()
    led_display.run(
        get_display_flights=flight_matcher.get_display_flights,
        consume_display_flight=flight_matcher.consume_display_flight,
    )