# planes.py
import random

# ── Airline color schemes ──────────────────────────────────────────────────────

AIRLINE_SCHEMES = {
    "delta": {
        "name": "Delta",
        "tail":     (0, 30, 100),      # deep navy
        "fuselage": (220, 225, 230),   # light gray
        "window":   (180, 0, 30),      # red
        "wing":     (180, 185, 195),   # gray
        "engine":   (60, 65, 75),      # dark gray
        "cockpit":  (100, 180, 255),   # blue tint
    },
    "american": {
        "name": "American",
        "tail":     (180, 185, 195),   # silver/gray
        "fuselage": (240, 240, 240),   # near white
        "window":   (180, 0, 30),      # red
        "wing":     (180, 185, 195),   # silver
        "engine":   (60, 65, 75),      # dark gray
        "cockpit":  (100, 180, 255),   # blue tint
    },
    "southwest": {
        "name": "Southwest",
        "tail":     (220, 50, 30),     # red
        "fuselage": (30, 100, 200),    # blue
        "window":   (240, 180, 0),     # yellow
        "wing":     (200, 205, 210),   # gray
        "engine":   (50, 55, 65),      # dark gray
        "cockpit":  (100, 180, 255),   # blue tint
    },
    "united": {
        "name": "United",
        "tail":     (0, 30, 100),      # navy
        "fuselage": (235, 238, 240),   # white/gray
        "window":   (180, 150, 0),     # gold
        "wing":     (180, 185, 195),   # gray
        "engine":   (60, 65, 75),      # dark gray
        "cockpit":  (100, 180, 255),   # blue tint
    },
    "suncountry": {
        "name": "Sun Country",
        "tail":     (0, 40, 120),      # navy
        "fuselage": (235, 238, 240),   # white
        "window":   (220, 180, 0),     # yellow
        "wing":     (180, 185, 195),   # gray
        "engine":   (60, 65, 75),      # dark gray
        "cockpit":  (100, 180, 255),   # blue tint
    },
    "skywest": {
        "name": "SkyWest",
        "tail":     (20, 50, 130),     # dark blue
        "fuselage": (210, 215, 220),   # light gray
        "window":   (100, 130, 200),   # muted blue
        "wing":     (170, 175, 185),   # gray
        "engine":   (55, 60, 70),      # dark gray
        "cockpit":  (100, 180, 255),   # blue tint
    },
    "endeavor": {
        "name": "Endeavor",
        "tail":     (80, 40, 140),     # purple
        "fuselage": (220, 222, 225),   # light gray
        "window":   (160, 120, 210),   # light purple
        "wing":     (175, 180, 190),   # gray
        "engine":   (55, 60, 70),      # dark gray
        "cockpit":  (100, 180, 255),   # blue tint
    },
    "republic": {
        "name": "Republic",
        "tail":     (10, 40, 110),     # dark blue
        "fuselage": (225, 228, 232),   # white/gray
        "window":   (50, 100, 200),    # blue
        "wing":     (175, 180, 190),   # gray
        "engine":   (55, 60, 70),      # dark gray
        "cockpit":  (100, 180, 255),   # blue tint
    },
    "aerlingus": {
        "name": "Aer Lingus",
        "tail":     (0, 130, 100),     # teal green
        "fuselage": (235, 238, 240),   # white
        "window":   (0, 160, 120),     # bright teal
        "wing":     (175, 180, 190),   # gray
        "engine":   (55, 60, 70),      # dark gray
        "cockpit":  (100, 180, 255),   # blue tint
    },
}

# ── Weighted random selection ──────────────────────────────────────────────────

# All carriers equal weight except Aer Lingus at ~3%
_WEIGHTS = {
    "delta":      12,
    "american":   12,
    "southwest":  12,
    "united":     12,
    "suncountry": 12,
    "skywest":    12,
    "endeavor":   12,
    "republic":   12,
    "aerlingus":   4,   # ~3.2% — easter egg
}

_AIRLINES = list(_WEIGHTS.keys())
_WEIGHT_VALUES = [_WEIGHTS[a] for a in _AIRLINES]


def get_random_airline() -> dict:
    """Return a random airline color scheme with weighted probability."""
    key = random.choices(_AIRLINES, weights=_WEIGHT_VALUES, k=1)[0]
    return AIRLINE_SCHEMES[key]


# ── Plane pixel builder ────────────────────────────────────────────────────────

def build_plane_pixels(scheme: dict) -> list:
    """
    Build a list of (x, y, color) tuples for the plane sprite
    using the given airline color scheme.

    Plane faces right, tail at x=0, nose at x=17.
    """
    t = scheme["tail"]
    f = scheme["fuselage"]
    w = scheme["window"]
    wg = scheme["wing"]
    e = scheme["engine"]
    c = scheme["cockpit"]

    # Light/dark fuselage shading variants
    f_dark = tuple(max(0, v - 45) for v in f)
    wg_dark = tuple(max(0, v - 45) for v in wg)

    pixels = [
        # Tail: vertical stabilizer
        (0, 1, t),
        (0, 2, t),
        (0, 3, t),
        (1, 2, t),
        (1, 3, t),
        (1, 4, t),

        # Rear fuselage
        (2, 3, f_dark),
        (2, 4, f),
        (2, 5, f),
        (2, 6, f),
        (2, 7, f_dark),

        # Main fuselage body
        (3,  4, f_dark), (3,  5, f), (3,  6, f), (3,  7, f_dark),
        (4,  4, f_dark), (4,  5, f), (4,  6, f), (4,  7, f_dark),
        (5,  4, f_dark), (5,  5, f), (5,  6, f), (5,  7, f_dark),
        (6,  4, f_dark), (6,  5, f), (6,  6, f), (6,  7, f_dark),
        (7,  4, f_dark), (7,  5, f), (7,  6, f), (7,  7, f_dark),
        (8,  4, f_dark), (8,  5, f), (8,  6, f), (8,  7, f_dark),
        (9,  4, f_dark), (9,  5, f), (9,  6, f), (9,  7, f_dark),
        (10, 4, f_dark), (10, 5, f), (10, 6, f), (10, 7, f_dark),
        (11, 4, f_dark), (11, 5, f), (11, 6, f), (11, 7, f_dark),
        (12, 4, f_dark), (12, 5, f), (12, 6, f), (12, 7, f_dark),
        (13, 4, f_dark), (13, 5, f), (13, 6, f), (13, 7, f_dark),
        (14, 4, f_dark), (14, 5, f), (14, 6, f), (14, 7, f_dark),

        # Cockpit and nose
        (15, 3, c),
        (15, 4, c),
        (15, 5, f),
        (15, 6, f),
        (15, 7, f_dark),
        (16, 4, c),
        (16, 5, f),
        (16, 6, f_dark),
        (17, 5, f),

        # Passenger windows
        (5,  5, w),
        (6,  5, w),
        (7,  5, w),
        (8,  5, w),
        (9,  5, w),
        (10, 5, w),
        (11, 5, w),
        (12, 5, w),
        (13, 5, w),
        (14, 5, w),

        # Top wing
        (6,  3, wg),
        (7,  2, wg),
        (8,  2, wg),
        (7,  1, wg),
        (8,  1, wg),

        # Lower wing
        (7,  8, wg),
        (8,  8, wg),
        (6,  9, wg),
        (7,  9, wg),
        (5,  10, wg),
        (6,  10, wg),
        (4,  11, wg),
        (5,  11, wg),
        (4,  12, wg_dark),

        # Engine
        (8,  9,  e),
        (9,  9,  e),
        (8,  10, wg),
        (9,  10, wg),

        # Navigation light — always red
        (4, 12, (255, 70, 70)),
    ]

    return pixels