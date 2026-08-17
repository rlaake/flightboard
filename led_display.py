# led_display.py
from planes import get_random_airline, build_plane_pixels
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

FONT_SIZE_SMALL = 8
FLIGHT_DISPLAY_SECONDS = 15
DOT_CYCLE_SPEED = 0.5  # seconds per dot step
PLANE_Y_OFFSET = 1
PLANE_SPEED = 0.08  # seconds per pixel
PLANE_WIDTH = 18
PLANE_PAUSE_SECONDS = 2


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
    from PIL import Image, ImageDraw
    from planes import (get_random_airline, build_plane_pixels,
                        should_show_ufo, build_ufo_frame,
                        UFO_WIDTH)

    panel_w = config.PANEL_COLS * config.CHAIN_LENGTH
    panel_h = config.PANEL_ROWS

    # Sprite state
    sprite_x = -PLANE_WIDTH
    pause_until_plane = None
    last_plane_time = time.monotonic()
    is_ufo = False
    frame_count = 0

    # Initial sprite
    current_scheme = get_random_airline()
    current_pixels = build_plane_pixels(current_scheme)
    current_width = PLANE_WIDTH
    print(f"[IDLE] Initial livery: {current_scheme['name']}")

    # Scroll state
    scroll_text = "Scanning the sky"
    dummy = Image.new("RGB", (1, 1))
    dummy_draw = ImageDraw.Draw(dummy)
    bbox = dummy_draw.textbbox((0, 0), scroll_text, font=font)
    text_width = bbox[2] - bbox[0]

    scroll_x = panel_w
    pause_until_scroll = None
    last_scroll_time = time.monotonic()
    SCROLL_SPEED_TEXT = 0.06
    TEXT_PAUSE_SECONDS = 1.5

    image = Image.new("RGB", (panel_w, panel_h))
    draw = ImageDraw.Draw(image)

    while not stop_event.is_set():
        now = time.monotonic()
        frame_count += 1

        draw.rectangle((0, 0, panel_w - 1, panel_h - 1), fill=(0, 0, 0))

        # ── Sprite movement ──
        if pause_until_plane is not None:
            if now >= pause_until_plane:
                # Decide: UFO or plane?
                if should_show_ufo():
                    is_ufo = True
                    current_pixels = build_ufo_frame(0)
                    current_width = UFO_WIDTH
                    print("[IDLE] 👽 UFO incoming!")
                else:
                    is_ufo = False
                    current_scheme = get_random_airline()
                    current_pixels = build_plane_pixels(current_scheme)
                    current_width = PLANE_WIDTH
                    print(f"[IDLE] Next livery: {current_scheme['name']}")

                sprite_x = -current_width
                pause_until_plane = None
                last_plane_time = now

        elif now - last_plane_time >= PLANE_SPEED:
            sprite_x += 1
            last_plane_time = now
            if sprite_x >= panel_w:
                pause_until_plane = now + PLANE_PAUSE_SECONDS

        # ── Text scroll ──
        if pause_until_scroll is not None:
            if now >= pause_until_scroll:
                scroll_x = panel_w
                pause_until_scroll = None
                last_scroll_time = now
        elif now - last_scroll_time >= SCROLL_SPEED_TEXT:
            scroll_x -= 1
            last_scroll_time = now
            if scroll_x < -text_width:
                pause_until_scroll = now + TEXT_PAUSE_SECONDS

        # ── Draw sprite ──
        if is_ufo:
            # Update rotating lights each frame
            current_pixels = build_ufo_frame(frame_count // 3)
            # Sine wave wobble — ±2 pixels vertical
            wobble_y = int(math.sin(sprite_x * 0.3) * 2)
        else:
            wobble_y = 0

        for px, py, color in current_pixels:
            x = sprite_x + px
            y = py + PLANE_Y_OFFSET + wobble_y
            if 0 <= x < panel_w and 0 <= y < panel_h:
                draw.point((x, y), fill=color)

        # ── Draw scrolling text ──
        draw.text((scroll_x, 20), scroll_text,
                  font=font, fill=config.COLOR_IDLE)

        matrix.SetImage(image, unsafe=False)
        time.sleep(0.01)


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
