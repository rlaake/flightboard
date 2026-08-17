# config.py

# Home location
HOME_LAT = 44.93088
HOME_LON = -93.23491

# Geofence
WATCH_RADIUS_MILES = 2.5
DISPLAY_RADIUS_MILES = 1.5

# ADS-B
ADSB_PATH = "/run/readsb/aircraft.json"
ADSB_POLL_INTERVAL = 3
MAX_SEEN_POS = 15  # ignore positions older than 15 seconds

# MSP scraper
MSP_URL = "https://www.mspairport.com/flights-and-airlines/flights?flight_type=departure"
MSP_POLL_INTERVAL = 600  # 10 minutes
BROWSER = "chromium"
CHROMIUM_PATH = "/usr/bin/chromium-browser"
CHROMEDRIVER_PATH = "/usr/bin/chromedriver"

# Departure table
DEPARTURE_CACHE_PATH = "/home/pi/flightboard/departure_cache.json"
DEPARTURE_MAX_AGE = 7200  # evict entries older than 2 hours

# LED display
PANEL_ROWS = 32
PANEL_COLS = 64
CHAIN_LENGTH = 1          # set to 2 when second panel added
SCROLL_SPEED = 0.05       # seconds per pixel
IDLE_PAUSE = 3.0          # seconds dark between idle loops
FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"
FONT_SIZE = 16
LED_RGB_SEQUENCE = "RBG"

# Colors (R, G, B)
COLOR_FLIGHT = (255, 200, 50)   # amber
COLOR_IDLE = (100, 100, 255)    # soft blue

# Display hold zone — how long to keep showing a flight after it enters the display zone
# "display" = show until flight leaves DISPLAY_RADIUS_MILES
# "watch"   = show until flight leaves WATCH_RADIUS_MILES (longer)
DISPLAY_HOLD_ZONE = "display"
