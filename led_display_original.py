# led_display.py
import time
import threading

try:
    from rgbmatrix import RGBMatrix, RGBMatrixOptions
    from PIL import Image, ImageDraw, ImageFont
    HARDWARE_AVAILABLE = True
except ImportError:
    HARDWARE_AVAILABLE = False
    print("[DISPLAY] rgbmatrix not available — running in mock mode")

import config

FONT_SIZE_SMALL = 12
FLIGHT_DISPLAY_SECONDS = 10
DOT_CYCLE_SPEED = 0.5  # seconds per dot step


def make_matrix():
    options = RGBMatrixOptions()
    options.rows = config.PANEL_ROWS
    options.cols = config.PANEL_COLS
    options.chain_length = config.CHAIN_LENGTH
    options.parallel = 1
    options.hardware_mapping = "adafruit-hat"
    options.led_rgb_sequence = config.LED_RGB_SEQUENCE
    options.pwm_bits = 11
    options.pwm_lsb_nanoseconds = 130
    options.scan_mode = 0
    options.drop_privileges = False
    return RGBMatrix(options=options)


def load_font(size):
    from PIL import ImageFont
    try:
        return ImageFont.truetype(config.FONT_PATH, size)
    except Exception:
        return ImageFont.load_default()


def render_flight_static(matrix, flight, font):
    """
    Display flight info statically — callsign on top line, destination on bottom.
    Holds for FLIGHT_DISPLAY_SECONDS then returns.
    """
    from PIL import Image, ImageDraw

    panel_w = config.PANEL_COLS * config.CHAIN_LENGTH
    panel_h = config.PANEL_ROWS

    image = Image.new("RGB", (panel_w, panel_h))
    draw = ImageDraw.Draw(image)

    callsign = flight.get("callsign", "")
    destination = flight.get("destination", "Unknown")

    # Top line — callsign
    draw.text((2, 2), callsign, font=font, fill=config.COLOR_FLIGHT)
    # Bottom line — destination
    draw.text((2, panel_h // 2), destination, font=font, fill=config.COLOR_FLIGHT)

    matrix.SetImage(image.convert("RGB"))
    time.sleep(FLIGHT_DISPLAY_SECONDS)


def render_idle(matrix, font, stop_event):
    """
    Idle animation — plane scrolls across top half, 
    'Scanning' with animated dots on bottom half.
    Runs until stop_event is set.
    """
    from PIL import Image, ImageDraw

    panel_w = config.PANEL_COLS * config.CHAIN_LENGTH
    panel_h = config.PANEL_ROWS
    half_h = panel_h // 2

    # Pixel art plane — simple arrow shape
    plane_pixels = [
        (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
        (3, 1), (4, 0),
        (3, 3), (4, 4),
        (0, 1), (0, 3),
    ]

    plane_x = 0
    dot_count = 0
    last_dot_time = time.time()
    last_frame_time = time.time()
    PLANE_SPEED = 0.05  # seconds per pixel

    while not stop_event.is_set():
        now = time.time()

        # Update dot count every DOT_CYCLE_SPEED seconds
        if now - last_dot_time >= DOT_CYCLE_SPEED:
            dot_count = (dot_count + 1) % 4
            last_dot_time = now

        # Update plane position every PLANE_SPEED seconds
        if now - last_frame_time >= PLANE_SPEED:
            plane_x = (plane_x + 1) % (panel_w + 10)
            last_frame_time = now

        # Build frame
        image = Image.new("RGB", (panel_w, panel_h))
        draw = ImageDraw.Draw(image)

        # Draw plane on top half
        for px, py in plane_pixels:
            x = plane_x + px - 5  # offset so it starts off screen
            if 0 <= x < panel_w and 0 <= py < half_h:
                draw.point((x, py), fill=(255, 255, 255))

        # Draw scanning text on bottom half
        dots = "." * dot_count
        scanning_text = f"Scanning{dots}"
        draw.text((2, half_h + 2), scanning_text,
                  font=font, fill=config.COLOR_IDLE)

        matrix.SetImage(image.convert("RGB"))
        time.sleep(0.01)  # ~100fps refresh, actual speed controlled above


# ── Mock mode ──────────────────────────────────────────────────────────────────

def mock_display_flight(flight):
    callsign = flight.get("callsign", "")
    destination = flight.get("destination", "Unknown")
    print(f"\n[DISPLAY]")
    print(f"  {callsign}")
    print(f"  {destination}")
    print(f"  (holding {FLIGHT_DISPLAY_SECONDS}s...)")
    time.sleep(FLIGHT_DISPLAY_SECONDS)


def mock_display_idle():
    for dots in range(4):
        print(f"\r[IDLE] ✈  Scanning{'.' * dots}   ", end="", flush=True)
        time.sleep(DOT_CYCLE_SPEED)


# ── Main display loop ──────────────────────────────────────────────────────────

def run(get_display_flights, consume_display_flight=None):
    font = load_font(FONT_SIZE_SMALL) if HARDWARE_AVAILABLE else None
    matrix = make_matrix() if HARDWARE_AVAILABLE else None

    print("[DISPLAY] Starting display loop")

    # Stop event for idle animation thread
    idle_stop = threading.Event()
    idle_thread = None

    def start_idle():
        nonlocal idle_thread
        idle_stop.clear()
        if HARDWARE_AVAILABLE:
            idle_thread = threading.Thread(
                target=render_idle,
                args=(matrix, font, idle_stop),
                daemon=True
            )
            idle_thread.start()

    def stop_idle():
        idle_stop.set()
        if idle_thread:
            idle_thread.join(timeout=1)

    # Start idle animation initially
    start_idle()

    while True:
        flights = get_display_flights()

        if flights:
            # Stop idle animation
            stop_idle()

            if len(flights) == 1:
                # Single flight — show statically
                if HARDWARE_AVAILABLE:
                    render_flight_static(matrix, flights[0], font)
                else:
                    mock_display_flight(flights[0])

                if consume_display_flight:
                    consume_display_flight(flights[0]["callsign"])

            else:
                # Multiple flights — alternate
                for flight in flights:
                    if HARDWARE_AVAILABLE:
                        render_flight_static(matrix, flight, font)
                    else:
                        mock_display_flight(flight)

                    if consume_display_flight:
                        consume_display_flight(flight["callsign"])

            # Resume idle after showing flights
            if HARDWARE_AVAILABLE:
                matrix.Clear()
            start_idle()

        else:
            if not HARDWARE_AVAILABLE:
                mock_display_idle()

        time.sleep(0.1)