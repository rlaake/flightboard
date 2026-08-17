# led_display.py
from planes import get_random_airline, build_plane_pixels
import time
import threading
import math

try:
    from rgbmatrix import RGBMatrix, RGBMatrixOptions
    from PIL import Image, ImageDraw, ImageFont
    HARDWARE_AVAILABLE = True
except ImportError:
    HARDWARE_AVAILABLE = False
    print("[DISPLAY] rgbmatrix not available — running in mock mode")

import config

FONT_SIZE_SMALL = 10
DOT_CYCLE_SPEED = 0.5
PLANE_Y_OFFSET = 1
PLANE_SPEED = 0.08
PLANE_WIDTH = 18
PLANE_PAUSE_SECONDS = 2
SCROLL_SPEED_TEXT = 0.06
TEXT_PAUSE_SECONDS = 1
DEST_SCROLL_SPEED = 0.08


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


def measure_text(text, font):
    from PIL import Image, ImageDraw
    dummy = Image.new("RGB", (1, 1))
    draw = ImageDraw.Draw(dummy)
    bbox = draw.textbbox((0, 0), text, font=font)
    return bbox[2] - bbox[0]


# ── Weather display ────────────────────────────────────────────────────────────

def render_weather(matrix, font, weather_data):
    """
    Show weather card for WEATHER_DISPLAY_SECONDS.
    Layout: pixel art left (14x14), temp/condition/time right.
    """
    from PIL import Image, ImageDraw
    from weather import get_weather_pixels

    panel_w = config.PANEL_COLS * config.CHAIN_LENGTH
    panel_h = config.PANEL_ROWS

    image = Image.new("RGB", (panel_w, panel_h))
    draw = ImageDraw.Draw(image)

    # ── Pixel art — left side, vertically centered ──
    art_pixels = get_weather_pixels(weather_data["condition_key"])
    art_y_offset = (panel_h - 14) // 2  # center 14px art in 32px height

    for px, py, color in art_pixels:
        x = px
        y = py + art_y_offset
        if 0 <= x < 16 and 0 <= y < panel_h:
            draw.point((x, y), fill=color)

    # ── Text — right side ──
    text_x = 17  # just right of the 14px art + 2px gap

    # Temperature
    temp_str = f"{weather_data['temp']}\u00b0F"
    draw.text((text_x, 1), temp_str, font=font, fill=(255, 200, 50))

    # Condition — may be long, truncate if needed
    condition = weather_data["condition"]
    if measure_text(condition, font) > panel_w - text_x:
        # Truncate to fit
        while condition and measure_text(condition + "..", font) > panel_w - text_x:
            condition = condition[:-1]
        condition = condition + ".."
    draw.text((text_x, 12), condition, font=font, fill=(180, 220, 255))

    # Time and date
    now = time.localtime()
    time_str = time.strftime("%-I:%M%p", now).lower()  # e.g. 3:42pm
    date_str = time.strftime("%a %-d", now)             # e.g. Mon 3
    datetime_str = f"{date_str} {time_str}"
    draw.text((text_x, 22), datetime_str, font=font, fill=(150, 150, 150))

    matrix.SetImage(image.convert("RGB"))
    time.sleep(config.WEATHER_DISPLAY_SECONDS)
    matrix.Clear()


def mock_render_weather(weather_data):
    now = time.localtime()
    print(f"\n[WEATHER] {weather_data['temp']}°F | "
          f"{weather_data['condition']} | "
          f"{time.strftime('%a %-d %-I:%M%p', now).lower()}")
    time.sleep(config.WEATHER_DISPLAY_SECONDS)


# ── Flight display ─────────────────────────────────────────────────────────────

def render_flight(matrix, font, get_active_flights, stop_event):
    from PIL import Image, ImageDraw

    panel_w = config.PANEL_COLS * config.CHAIN_LENGTH
    panel_h = config.PANEL_ROWS

    image = Image.new("RGB", (panel_w, panel_h))
    draw = ImageDraw.Draw(image)

    current_callsign = None
    dest_scroll_x = panel_w
    last_scroll_time = time.monotonic()

    while not stop_event.is_set():
        flights = get_active_flights()

        if not flights:
            break

        flight = flights[0]
        callsign = flight.get("callsign", "")
        destination = flight.get("destination", "Unknown")

        if callsign != current_callsign:
            current_callsign = callsign
            dest_scroll_x = panel_w
            last_scroll_time = time.monotonic()
            print(f"[DISPLAY] Now showing: {callsign} -> {destination}")

        now = time.monotonic()

        if now - last_scroll_time >= DEST_SCROLL_SPEED:
            dest_scroll_x -= 1
            last_scroll_time = now

        dest_width = measure_text(destination, font)
        if dest_scroll_x < -dest_width:
            dest_scroll_x = panel_w

        draw.rectangle((0, 0, panel_w - 1, panel_h - 1), fill=(0, 0, 0))
        draw.text((2, 2), callsign, font=font, fill=config.COLOR_FLIGHT)
        draw.text((dest_scroll_x, panel_h // 2), destination,
                  font=font, fill=config.COLOR_FLIGHT)

        matrix.SetImage(image, unsafe=False)
        time.sleep(0.01)


# ── Idle display ───────────────────────────────────────────────────────────────

def render_idle(matrix, font, stop_event):
    from PIL import Image, ImageDraw
    from planes import (get_random_airline, build_plane_pixels,
                        should_show_ufo, build_ufo_frame, UFO_WIDTH)
    import weather

    panel_w = config.PANEL_COLS * config.CHAIN_LENGTH
    panel_h = config.PANEL_ROWS

    sprite_x = -PLANE_WIDTH
    pause_until_plane = None
    last_plane_time = time.monotonic()
    is_ufo = False
    frame_count = 0

    current_scheme = get_random_airline()
    current_pixels = build_plane_pixels(current_scheme)
    current_width = PLANE_WIDTH
    print(f"[IDLE] Initial livery: {current_scheme['name']}")

    scroll_text = "Scanning the sky"
    dummy = Image.new("RGB", (1, 1))
    dummy_draw = ImageDraw.Draw(dummy)
    bbox = dummy_draw.textbbox((0, 0), scroll_text, font=font)
    text_width = bbox[2] - bbox[0]

    scroll_x = panel_w
    pause_until_scroll = None
    last_scroll_time = time.monotonic()

    # Weather trigger
    last_weather_display = time.monotonic()

    image = Image.new("RGB", (panel_w, panel_h))
    draw = ImageDraw.Draw(image)

    while not stop_event.is_set():
        now = time.monotonic()
        frame_count += 1

        # ── Weather display trigger ──
        if now - last_weather_display >= config.WEATHER_DISPLAY_INTERVAL:
            weather_data = weather.get_weather()
            if weather_data:
                print(f"[IDLE] Showing weather: "
                      f"{weather_data['temp']}°F {weather_data['condition']}")
                if HARDWARE_AVAILABLE:
                    render_weather(matrix, font, weather_data)
                else:
                    mock_render_weather(weather_data)
                # Reset timing after weather display
                last_weather_display = time.monotonic()
                last_plane_time = time.monotonic()
                last_scroll_time = time.monotonic()
                # Clear and redraw
                image = Image.new("RGB", (panel_w, panel_h))
                draw = ImageDraw.Draw(image)
            else:
                # No weather data yet — reset timer and try again in 60s
                last_weather_display = now - config.WEATHER_DISPLAY_INTERVAL + 60
            continue

        draw.rectangle((0, 0, panel_w - 1, panel_h - 1), fill=(0, 0, 0))

        # ── Sprite movement ──
        if pause_until_plane is not None:
            if now >= pause_until_plane:
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
            current_pixels = build_ufo_frame(frame_count // 3)
            wobble_y = int(math.sin(sprite_x * 0.3) * 2)
        else:
            wobble_y = 0

        for px, py, color in current_pixels:
            x = sprite_x + px
            y = py + PLANE_Y_OFFSET + wobble_y
            if 0 <= x < panel_w and 0 <= y < panel_h:
                draw.point((x, y), fill=color)

        draw.text((scroll_x, 20), scroll_text,
                  font=font, fill=config.COLOR_IDLE)

        matrix.SetImage(image, unsafe=False)
        time.sleep(0.01)


# ── Mock mode ──────────────────────────────────────────────────────────────────

def mock_display_flight(flight):
    callsign = flight.get("callsign", "")
    destination = flight.get("destination", "Unknown")
    print(f"\r[DISPLAY] {callsign:10s} | {destination}", end="", flush=True)


def mock_display_idle():
    for dots in range(4):
        print(f"\r[IDLE] ✈  Scanning the sky{'.' * dots}   ",
              end="", flush=True)
        time.sleep(DOT_CYCLE_SPEED)


# ── Main display loop ──────────────────────────────────────────────────────────

def run(get_active_flights):
    font = load_font(FONT_SIZE_SMALL) if HARDWARE_AVAILABLE else None
    matrix = make_matrix() if HARDWARE_AVAILABLE else None

    print("[DISPLAY] Starting display loop")

    idle_stop = threading.Event()
    flight_stop = threading.Event()
    idle_thread = None
    flight_thread = None

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
        if HARDWARE_AVAILABLE:
            matrix.Clear()

    def start_flight():
        nonlocal flight_thread
        flight_stop.clear()
        if HARDWARE_AVAILABLE:
            flight_thread = threading.Thread(
                target=render_flight,
                args=(matrix, font, get_active_flights, flight_stop),
                daemon=True
            )
            flight_thread.start()

    def stop_flight():
        flight_stop.set()
        if flight_thread:
            flight_thread.join(timeout=1)
        if HARDWARE_AVAILABLE:
            matrix.Clear()

    start_idle()
    in_flight_mode = False

    while True:
        flights = get_active_flights()

        if flights and not in_flight_mode:
            stop_idle()
            start_flight()
            in_flight_mode = True
            print(f"[DISPLAY] Entering flight mode: "
                  f"{flights[0].get('callsign')}")

        elif not flights and in_flight_mode:
            stop_flight()
            start_idle()
            in_flight_mode = False
            print("[DISPLAY] Returning to idle")

        time.sleep(0.2)