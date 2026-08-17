# main.py
import flight_matcher
import led_display
import weather

if __name__ == "__main__":
    print("=== Flight Board Starting ===")
    weather.start()
    flight_matcher.start()
    led_display.run(
        get_active_flights=flight_matcher.get_active_flights,
    )