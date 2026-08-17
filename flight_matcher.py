# flight_matcher.py
import re
import json
import math
import time
import threading
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from airline_codes import IATA_TO_ICAO, OPERATING_TO_MARKETING
import config

# ── Shared state ───────────────────────────────────────────────────────────────

departure_table = {}
departure_lock = threading.Lock()

watch_zone = {}
watch_lock = threading.Lock()

# active_flights: flights currently in display zone, shown until they leave
# Structure: {callsign: {"callsign": str, "destination": str, "alt": any, "track": any}}
active_flights = {}
active_flights_lock = threading.Lock()


# ── Selenium browser ───────────────────────────────────────────────────────────

def make_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")
    options.add_argument("--blink-settings=imagesEnabled=false")
    options.binary_location = config.CHROMIUM_PATH
    service = Service(config.CHROMEDRIVER_PATH)
    return webdriver.Chrome(service=service, options=options)


# ── Callsign normalization ─────────────────────────────────────────────────────

def normalize_callsign(raw: str, translate_to_icao: bool = False) -> str:
    raw = raw.strip()

    match = re.search(r'([A-Z][A-Z0-9])\s+(\d+)$', raw.upper())
    if match:
        code = match.group(1)
        number = match.group(2)
        if translate_to_icao and len(code) == 2:
            code = IATA_TO_ICAO.get(code, code)
        return code + number

    match = re.search(r'([A-Z]{3})(\d+)', raw.upper())
    if match:
        return match.group(1) + match.group(2)

    return raw.upper().replace(" ", "")


# ── Departure table helpers ────────────────────────────────────────────────────

def load_cache():
    try:
        with open(config.DEPARTURE_CACHE_PATH, "r") as f:
            data = json.load(f)
        print(f"[CACHE] Loaded {len(data)} entries from disk")
        with departure_lock:
            departure_table.update(data)
    except FileNotFoundError:
        print("[CACHE] No cache file found, starting fresh")
    except Exception as e:
        print(f"[CACHE] Failed to load cache: {e}")


def save_cache():
    try:
        with departure_lock:
            snapshot = dict(departure_table)
        with open(config.DEPARTURE_CACHE_PATH, "w") as f:
            json.dump(snapshot, f)
    except Exception as e:
        print(f"[CACHE] Failed to save cache: {e}")


def lookup_departure(callsign: str, table_snapshot: dict) -> str:
    entry = table_snapshot.get(callsign)
    if entry:
        return entry.get("destination", "Unknown")

    match = re.match(r'([A-Z]{3})(\d+)', callsign)
    if match:
        operating_code = match.group(1)
        flight_number = match.group(2)
        marketing_code = OPERATING_TO_MARKETING.get(operating_code)
        if marketing_code:
            remapped = marketing_code + flight_number
            entry = table_snapshot.get(remapped)
            if entry:
                print(f"[MATCH] Remapped {callsign} -> {remapped}")
                return entry.get("destination", "Unknown")

    return "Unknown"


# ── Haversine ──────────────────────────────────────────────────────────────────

def haversine_miles(lat1, lon1, lat2, lon2):
    R = 3958.8
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlam = math.radians(lon2 - lon1)
    a = math.sin(dphi/2)**2 + math.cos(phi1)*math.cos(phi2)*math.sin(dlam/2)**2
    return R * 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))


# ── MSP scraper ────────────────────────────────────────────────────────────────

def fetch_msp_page(driver, page_number: int) -> str:
    if page_number == 1:
        url = config.MSP_URL
    else:
        url = f"{config.MSP_URL}&page={page_number}"

    try:
        driver.get(url)
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "table.flight-search-results tbody tr")
            )
        )
        return driver.page_source
    except Exception as e:
        print(f"[MSP] Page {page_number} fetch failed: {e}")
        return ""


def fetch_all_msp_html() -> list:
    pages_html = []
    driver = make_driver()

    try:
        print("[MSP] Fetching page 1...")
        html = fetch_msp_page(driver, 1)
        if not html:
            print("[MSP] Failed to fetch page 1")
            return []

        pages_html.append(html)

        for page_num in range(2, 4):
            print(f"[MSP] Fetching page {page_num}...")
            page_html = fetch_msp_page(driver, page_num)
            if not page_html:
                print(f"[MSP] Page {page_num} empty, stopping pagination")
                break

            soup = BeautifulSoup(page_html, "html.parser")
            table = soup.select_one("table.flight-search-results")
            if not table or not table.select("tbody tr"):
                print(f"[MSP] Page {page_num} has no rows, stopping")
                break

            pages_html.append(page_html)

    except Exception as e:
        print(f"[MSP] Scrape error: {e}")
    finally:
        driver.quit()

    return pages_html


def parse_departures(html: str) -> dict:
    soup = BeautifulSoup(html, "html.parser")
    table = soup.select_one("table.flight-search-results")
    if not table:
        print("[MSP] Could not find flight-search-results table")
        return {}

    results = {}
    for row in table.select("tbody tr"):
        cells = row.find_all("td")
        if len(cells) < 3:
            continue

        raw_flight = cells[2].get_text(strip=True)
        destination = cells[1].get_text(strip=True)

        callsign = normalize_callsign(raw_flight, translate_to_icao=True)
        if callsign and destination:
            results[callsign] = destination

    return results


def scrape_msp_departures():
    pages_html = fetch_all_msp_html()
    if not pages_html:
        print("[MSP] Scrape returned no pages")
        return

    all_flights = {}
    for i, html in enumerate(pages_html):
        page_flights = parse_departures(html)
        print(f"[MSP] Page {i+1}: {len(page_flights)} flights")
        all_flights.update(page_flights)

    if not all_flights:
        print("[MSP] No flights parsed")
        return

    now = time.time()
    with departure_lock:
        for callsign, destination in all_flights.items():
            departure_table[callsign] = {
                "destination": destination,
                "updated_at": now,
            }

        cutoff = now - config.DEPARTURE_MAX_AGE
        stale = [k for k, v in departure_table.items()
                 if v["updated_at"] < cutoff]
        for k in stale:
            del departure_table[k]

    print(f"[MSP] {len(all_flights)} fresh, "
          f"{len(stale)} evicted, "
          f"{len(departure_table)} total")

    save_cache()


def msp_scraper_thread():
    while True:
        scrape_msp_departures()
        jitter = random.uniform(-60, 60)
        time.sleep(config.MSP_POLL_INTERVAL + jitter)


# ── ADS-B poller ───────────────────────────────────────────────────────────────

def _hold_radius() -> float:
    """Return the radius used to determine when to stop showing a flight."""
    if config.DISPLAY_HOLD_ZONE == "watch":
        return config.WATCH_RADIUS_MILES
    return config.DISPLAY_RADIUS_MILES


def adsb_poller_thread():
    while True:
        try:
            with open(config.ADSB_PATH, "r") as f:
                data = json.load(f)

            aircraft_list = data.get("aircraft", [])

            with departure_lock:
                table_snapshot = dict(departure_table)

            current_callsigns = set()

            for ac in aircraft_list:
                lat = ac.get("lat")
                lon = ac.get("lon")
                seen_pos = ac.get("seen_pos", 999)
                flight = ac.get("flight", "").strip()
                alt = ac.get("alt_baro", "?")
                track = ac.get("track", "?")

                if not lat or not lon:
                    continue
                if seen_pos > config.MAX_SEEN_POS:
                    continue
                if not flight:
                    continue

                callsign = normalize_callsign(flight)
                dist = haversine_miles(
                    config.HOME_LAT, config.HOME_LON, lat, lon
                )

                if dist <= config.WATCH_RADIUS_MILES:
                    current_callsigns.add(callsign)

                    with watch_lock:
                        if callsign not in watch_zone:
                            destination = lookup_departure(
                                callsign, table_snapshot
                            )
                            watch_zone[callsign] = {
                                "callsign": callsign,
                                "destination": destination,
                                "alt": alt,
                                "track": track,
                                "min_dist": dist,
                            }
                            print(f"[WATCH] {callsign} entered watch zone "
                                  f"at {dist:.2f} mi | {alt} ft | "
                                  f"-> {destination}")
                        else:
                            watch_zone[callsign]["min_dist"] = min(
                                watch_zone[callsign]["min_dist"], dist
                            )

                    # Enter display zone — add to active_flights if not already there
                    if dist <= config.DISPLAY_RADIUS_MILES:
                        with active_flights_lock:
                            if callsign not in active_flights:
                                with watch_lock:
                                    flight_info = dict(
                                        watch_zone.get(callsign, {})
                                    )
                                active_flights[callsign] = flight_info
                                print(f"[DISPLAY] {callsign} | {dist:.2f} mi | "
                                      f"{alt} ft | "
                                      f"-> {flight_info.get('destination', 'Unknown')}")

            # ── Remove flights that have left the hold zone ──
            hold_radius = _hold_radius()

            # Build set of callsigns still within hold radius
            current_in_hold = set()
            for ac in aircraft_list:
                lat = ac.get("lat")
                lon = ac.get("lon")
                seen_pos = ac.get("seen_pos", 999)
                flight = ac.get("flight", "").strip()
                if not lat or not lon or seen_pos > config.MAX_SEEN_POS or not flight:
                    continue
                callsign = normalize_callsign(flight)
                dist = haversine_miles(
                    config.HOME_LAT, config.HOME_LON, lat, lon
                )
                if dist <= hold_radius:
                    current_in_hold.add(callsign)

            with active_flights_lock:
                exited_display = [c for c in active_flights
                                  if c not in current_in_hold]
                for callsign in exited_display:
                    entry = active_flights.pop(callsign)
                    print(f"[DISPLAY END] {callsign} left "
                          f"{config.DISPLAY_HOLD_ZONE} zone")

            # Clean up watch zone for flights that left watch radius entirely
            with watch_lock:
                exited_watch = [c for c in watch_zone
                                if c not in current_callsigns]
                for callsign in exited_watch:
                    entry = watch_zone.pop(callsign)
                    print(f"[EXIT] {callsign} left watch zone "
                          f"(closest: {entry['min_dist']:.2f} mi)")

        except Exception as e:
            print(f"[ADSB] Poll failed: {e}")

        time.sleep(config.ADSB_POLL_INTERVAL)


# ── Public API ─────────────────────────────────────────────────────────────────

def get_active_flights() -> list:
    """
    Returns list of flights currently in the display zone.
    led_display calls this to know what to show.
    Flights stay in this list until they leave the hold zone —
    no consume step needed.
    """
    with active_flights_lock:
        return list(active_flights.values())


def start():
    load_cache()
    threading.Thread(target=msp_scraper_thread, daemon=True).start()
    threading.Thread(target=adsb_poller_thread, daemon=True).start()
    print("[MATCHER] All threads started")