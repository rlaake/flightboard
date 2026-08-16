# debug_receiver.py
# Standalone receiver test — no scraping, no display, just ADS-B detection
import json
import math
import time
import config


def haversine_miles(lat1, lon1, lat2, lon2):
    R = 3958.8
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlam = math.radians(lon2 - lon1)
    a = math.sin(dphi/2)**2 + math.cos(phi1)*math.cos(phi2)*math.sin(dlam/2)**2
    return R * 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))


def poll():
    try:
        with open(config.ADSB_PATH, "r") as f:
            data = json.load(f)
    except Exception as e:
        print(f"[ERROR] Could not read {config.ADSB_PATH}: {e}")
        return

    aircraft_list = data.get("aircraft", [])
    with_position = [
        a for a in aircraft_list
        if a.get("lat") and a.get("lon")
        and a.get("seen_pos", 999) <= config.MAX_SEEN_POS
    ]

    distances = []
    for ac in with_position:
        dist = haversine_miles(
            config.HOME_LAT, config.HOME_LON,
            ac["lat"], ac["lon"]
        )
        distances.append((dist, ac))
    distances.sort(key=lambda x: x[0])

    print(f"\n[{time.strftime('%H:%M:%S')}] "
          f"{len(aircraft_list)} total, "
          f"{len(with_position)} with fresh position")

    print("  Closest 5:")
    for dist, ac in distances[:5]:
        flight = ac.get("flight", "").strip() or "(no callsign)"
        alt = ac.get("alt_baro", "?")
        track = ac.get("track", "?")
        print(f"    {flight:10s} | {dist:.2f} mi | {alt} ft | hdg {track}")

    watch = [(d, a) for d, a in distances if d <= config.WATCH_RADIUS_MILES]
    display = [(d, a) for d, a in distances if d <= config.DISPLAY_RADIUS_MILES]

    if watch:
        print(f"\n  *** {len(watch)} in WATCH zone ({config.WATCH_RADIUS_MILES} mi):")
        for dist, ac in watch:
            flight = ac.get("flight", "").strip() or "(no callsign)"
            print(f"    {flight:10s} | {dist:.2f} mi | {ac.get('alt_baro', '?')} ft")

    if display:
        print(f"\n  *** {len(display)} in DISPLAY zone ({config.DISPLAY_RADIUS_MILES} mi):")
        for dist, ac in display:
            flight = ac.get("flight", "").strip() or "(no callsign)"
            print(f"    {flight:10s} | {dist:.2f} mi | {ac.get('alt_baro', '?')} ft")

    if not watch:
        print(f"  Nothing within {config.WATCH_RADIUS_MILES} miles")


if __name__ == "__main__":
    print("=== Receiver Debug ===")
    print(f"Home: {config.HOME_LAT}, {config.HOME_LON}")
    print(f"Watch radius:   {config.WATCH_RADIUS_MILES} mi")
    print(f"Display radius: {config.DISPLAY_RADIUS_MILES} mi")
    print(f"ADSB path: {config.ADSB_PATH}")
    print("Ctrl-C to stop\n")

    while True:
        poll()
        time.sleep(config.ADSB_POLL_INTERVAL)