# config.py

# Home location
HOME_LAT = 44.93088
HOME_LON = -93.23491

# Geofence
WATCH_RADIUS_MILES = 2.5
DISPLAY_RADIUS_MILES = 1.5

# Display hold zone
DISPLAY_HOLD_ZONE = "display"

# ADS-B
ADSB_PATH = "/run/readsb/aircraft.json"
ADSB_POLL_INTERVAL = 3
MAX_SEEN_POS = 15

# MSP scraper
MSP_URL = "https://www.mspairport.com/flights-and-airlines/flights?flight_type=departure"
MSP_POLL_INTERVAL = 600
BROWSER = "chromium"
CHROMIUM_PATH = "/usr/bin/chromium-browser"
CHROMEDRIVER_PATH = "/usr/bin/chromedriver"

# Departure table
DEPARTURE_CACHE_PATH = "/home/pi/flightboard/departure_cache.json"
DEPARTURE_MAX_AGE = 7200

# LED display
PANEL_ROWS = 32
PANEL_COLS = 64
CHAIN_LENGTH = 1
SCROLL_SPEED = 0.05
IDLE_PAUSE = 3.0
FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"
FONT_SIZE = 16
LED_RGB_SEQUENCE = "RBG"

# Colors (R, G, B)
COLOR_FLIGHT = (255, 200, 50)   # amber
COLOR_IDLE = (100, 100, 255)    # soft blue

# Weather display
WEATHER_FETCH_INTERVAL = 600    # fetch every 10 minutes
WEATHER_DISPLAY_INTERVAL = 300  # show weather every 5 minutes during idle
WEATHER_DISPLAY_SECONDS = 8     # how long to show the weather card