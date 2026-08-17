# weather.py
import time
import threading
import requests
import config

# ── Shared state ───────────────────────────────────────────────────────────────

_weather_data = None
_weather_lock = threading.Lock()
_last_fetch = 0


# ── Open-Meteo WMO code -> condition mapping ───────────────────────────────────
# https://open-meteo.com/en/docs#weathervariables

WMO_CONDITIONS = {
    0:  ("Clear",        "clear"),
    1:  ("Mostly Clear", "clear"),
    2:  ("Partly Cloudy","partly_cloudy"),
    3:  ("Overcast",     "cloudy"),
    45: ("Foggy",        "fog"),
    48: ("Foggy",        "fog"),
    51: ("Light Drizzle","light_rain"),
    53: ("Drizzle",      "light_rain"),
    55: ("Heavy Drizzle","rain"),
    61: ("Light Rain",   "light_rain"),
    63: ("Rain",         "rain"),
    65: ("Heavy Rain",   "heavy_rain"),
    71: ("Light Snow",   "snow"),
    73: ("Snow",         "snow"),
    75: ("Heavy Snow",   "snow"),
    77: ("Snow Grains",  "snow"),
    80: ("Light Showers","light_rain"),
    81: ("Showers",      "rain"),
    82: ("Heavy Showers","heavy_rain"),
    85: ("Snow Showers", "snow"),
    86: ("Snow Showers", "snow"),
    95: ("Thunderstorm", "thunderstorm"),
    96: ("Thunderstorm", "thunderstorm"),
    99: ("Thunderstorm", "thunderstorm"),
}


def fetch_weather() -> dict | None:
    """Fetch current weather from Open-Meteo. Returns parsed dict or None."""
    try:
        url = (
            f"https://api.open-meteo.com/v1/forecast"
            f"?latitude={config.HOME_LAT}"
            f"&longitude={config.HOME_LON}"
            f"&current=temperature_2m,weathercode,windspeed_10m"
            f"&temperature_unit=fahrenheit"
            f"&windspeed_unit=mph"
            f"&timezone=auto"
        )
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        data = resp.json()

        current = data["current"]
        wmo = current["weathercode"]
        temp = round(current["temperature_2m"])
        condition_label, condition_key = WMO_CONDITIONS.get(
            wmo, ("Unknown", "cloudy")
        )

        return {
            "temp": temp,
            "condition": condition_label,
            "condition_key": condition_key,
            "wmo": wmo,
        }

    except Exception as e:
        print(f"[WEATHER] Fetch failed: {e}")
        return None


def get_weather() -> dict | None:
    """Return cached weather data, fetching if stale."""
    global _last_fetch, _weather_data

    now = time.time()
    if now - _last_fetch >= config.WEATHER_FETCH_INTERVAL or _weather_data is None:
        result = fetch_weather()
        if result:
            with _weather_lock:
                _weather_data = result
            _last_fetch = now
            print(f"[WEATHER] {result['temp']}°F {result['condition']} "
                  f"(WMO {result['wmo']})")

    with _weather_lock:
        return dict(_weather_data) if _weather_data else None


def weather_fetcher_thread():
    """Background thread to keep weather data fresh."""
    while True:
        get_weather()
        time.sleep(config.WEATHER_FETCH_INTERVAL)


def start():
    """Start the background weather fetcher."""
    # Do an immediate fetch so data is ready on first display
    get_weather()
    threading.Thread(target=weather_fetcher_thread, daemon=True).start()
    print("[WEATHER] Fetcher started")


# ── Pixel art weather icons (14x14, origin top-left) ──────────────────────────

def get_weather_pixels(condition_key: str) -> list:
    """Return list of (x, y, color) tuples for the given condition."""
    builders = {
        "clear":         _pixels_clear,
        "partly_cloudy": _pixels_partly_cloudy,
        "cloudy":        _pixels_cloudy,
        "fog":           _pixels_fog,
        "light_rain":    _pixels_light_rain,
        "rain":          _pixels_rain,
        "heavy_rain":    _pixels_heavy_rain,
        "snow":          _pixels_snow,
        "thunderstorm":  _pixels_thunderstorm,
    }
    builder = builders.get(condition_key, _pixels_cloudy)
    return builder()


# Colors
SUN       = (255, 210, 0)
SUN_RAY   = (255, 230, 80)
CLOUD     = (210, 215, 220)
CLOUD_DRK = (160, 165, 175)
RAIN_LT   = (100, 160, 255)
RAIN_HVY  = (50, 100, 220)
SNOW_CLR  = (200, 220, 255)
FOG_CLR   = (180, 185, 195)
LIGHTNING = (255, 230, 0)


def _pixels_clear() -> list:
    """Bright sun with rays."""
    pixels = []
    # Sun body — 5x5 circle centered at (7,7)
    for x, y in [
        (6,5),(7,5),(8,5),
        (5,6),(6,6),(7,6),(8,6),(9,6),
        (5,7),(6,7),(7,7),(8,7),(9,7),
        (5,8),(6,8),(7,8),(8,8),(9,8),
        (6,9),(7,9),(8,9),
    ]:
        pixels.append((x, y, SUN))

    # Rays
    for x, y in [
        (7,3),(7,4),          # top
        (7,10),(7,11),        # bottom
        (3,7),(4,7),          # left
        (10,7),(11,7),        # right
        (4,4),(5,5),          # top-left
        (10,4),(9,5),         # top-right
        (4,10),(5,9),         # bottom-left
        (10,10),(9,9),        # bottom-right
    ]:
        pixels.append((x, y, SUN_RAY))

    return pixels


def _pixels_partly_cloudy() -> list:
    """Small sun top-right, cloud bottom-left."""
    pixels = []

    # Small sun — top right
    for x, y in [
        (9,1),(10,1),(11,1),
        (8,2),(9,2),(10,2),(11,2),(12,2),
        (8,3),(9,3),(10,3),(11,3),(12,3),
        (9,4),(10,4),(11,4),
    ]:
        pixels.append((x, y, SUN))

    # Sun rays — small
    for x, y in [(10,0),(13,3),(7,3),(10,5)]:
        pixels.append((x, y, SUN_RAY))

    # Cloud — bottom left, overlapping sun slightly
    for x, y in [
        (4,6),(5,6),(6,6),(7,6),(8,6),
        (3,7),(4,7),(5,7),(6,7),(7,7),(8,7),(9,7),(10,7),
        (3,8),(4,8),(5,8),(6,8),(7,8),(8,8),(9,8),(10,8),
        (3,9),(4,9),(5,9),(6,9),(7,9),(8,9),(9,9),(10,9),
        (4,10),(5,10),(6,10),(7,10),(8,10),(9,10),
    ]:
        pixels.append((x, y, CLOUD))

    return pixels


def _pixels_cloudy() -> list:
    """Full overcast cloud."""
    pixels = []
    for x, y in [
        (5,3),(6,3),(7,3),(8,3),
        (4,4),(5,4),(6,4),(7,4),(8,4),(9,4),(10,4),
        (3,5),(4,5),(5,5),(6,5),(7,5),(8,5),(9,5),(10,5),(11,5),
        (3,6),(4,6),(5,6),(6,6),(7,6),(8,6),(9,6),(10,6),(11,6),
        (3,7),(4,7),(5,7),(6,7),(7,7),(8,7),(9,7),(10,7),(11,7),
        (3,8),(4,8),(5,8),(6,8),(7,8),(8,8),(9,8),(10,8),(11,8),
        (4,9),(5,9),(6,9),(7,9),(8,9),(9,9),(10,9),
    ]:
        pixels.append((x, y, CLOUD))

    return pixels


def _pixels_fog() -> list:
    """Horizontal fog lines."""
    pixels = []
    for y, x_start, x_end in [
        (3, 3, 11),
        (5, 2, 12),
        (7, 4, 10),
        (9, 2, 12),
        (11, 3, 11),
    ]:
        for x in range(x_start, x_end + 1):
            pixels.append((x, y, FOG_CLR))

    return pixels


def _pixels_light_rain() -> list:
    """Cloud with light rain drops."""
    pixels = list(_pixels_cloudy())
    # Light drops — 3 drops
    for x, y in [
        (5, 11), (5, 12),
        (8, 11), (8, 12),
        (11, 11),(11, 12),
    ]:
        pixels.append((x, y, RAIN_LT))
    return pixels


def _pixels_rain() -> list:
    """Cloud with moderate rain."""
    pixels = list(_pixels_cloudy())
    # 4 drops, slightly heavier
    for x, y in [
        (4, 11),(4, 12),(4, 13),
        (7, 11),(7, 12),(7, 13),
        (10,11),(10,12),(10,13),
        (6, 12),(6, 13),
        (9, 12),(9, 13),
    ]:
        pixels.append((x, y, RAIN_LT))
    return pixels


def _pixels_heavy_rain() -> list:
    """Cloud with heavy rain."""
    pixels = list(_pixels_cloudy())
    for x, y in [
        (4, 11),(4, 12),(4, 13),
        (6, 11),(6, 12),(6, 13),
        (8, 11),(8, 12),(8, 13),
        (10,11),(10,12),(10,13),
        (5, 12),(5, 13),
        (7, 12),(7, 13),
        (9, 12),(9, 13),
        (11,12),(11,13),
    ]:
        pixels.append((x, y, RAIN_HVY))
    return pixels


def _pixels_snow() -> list:
    """Cloud with snowflakes."""
    pixels = list(_pixels_cloudy())
    # Simple cross snowflakes
    for cx, cy in [(5, 12), (8, 12), (11, 12)]:
        for x, y in [
            (cx, cy),
            (cx-1, cy), (cx+1, cy),
            (cx, cy-1), (cx, cy+1),
        ]:
            pixels.append((x, y, SNOW_CLR))
    return pixels


def _pixels_thunderstorm() -> list:
    """Dark cloud with lightning bolt."""
    pixels = []
    # Darker cloud
    for x, y in [
        (5,3),(6,3),(7,3),(8,3),
        (4,4),(5,4),(6,4),(7,4),(8,4),(9,4),(10,4),
        (3,5),(4,5),(5,5),(6,5),(7,5),(8,5),(9,5),(10,5),(11,5),
        (3,6),(4,6),(5,6),(6,6),(7,6),(8,6),(9,6),(10,6),(11,6),
        (3,7),(4,7),(5,7),(6,7),(7,7),(8,7),(9,7),(10,7),(11,7),
        (3,8),(4,8),(5,8),(6,8),(7,8),(8,8),(9,8),(10,8),(11,8),
        (4,9),(5,9),(6,9),(7,9),(8,9),(9,9),(10,9),
    ]:
        pixels.append((x, y, CLOUD_DRK))

    # Lightning bolt
    for x, y in [
        (8,10),(7,10),
        (7,11),(6,11),
        (6,12),(5,12),(4,12),
        (5,13),(6,13),
    ]:
        pixels.append((x, y, LIGHTNING))

    return pixels