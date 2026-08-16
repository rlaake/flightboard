# planes.py
import random

# ── Airline color schemes ──────────────────────────────────────────────────────

AIRLINE_SCHEMES = {
    "delta": {
        "name": "Delta",
        "tail":         (200, 0, 20),      # red widget tail
        "fuselage":     (245, 245, 248),   # white
        "fuselage_dark":(15, 25, 80),      # navy belly stripe
        "window":       (15, 25, 80),      # navy blue windows
        "wing":         (185, 190, 200),   # gray
        "engine":       (60, 65, 75),      # dark gray
        "cockpit":      (110, 185, 255),   # blue tint
        "nav_light":    (255, 70, 70),     # red
    },
    "american": {
        "name": "American",
        "tail":         (160, 165, 175),   # silver gray tail
        "fuselage":     (235, 235, 238),   # near white
        "fuselage_dark":(160, 165, 175),   # silver belly
        "window":       (180, 0, 30),      # red stripe windows
        "wing":         (175, 180, 190),   # silver
        "engine":       (55, 60, 70),      # dark gray
        "cockpit":      (110, 185, 255),   # blue tint
        "nav_light":    (255, 70, 70),     # red
    },
    "southwest": {
        "name": "Southwest",
        "tail":         (210, 35, 25),     # red tail
        "fuselage":     (30, 100, 200),    # blue fuselage
        "fuselage_dark":(20, 70, 150),     # darker blue belly
        "window":       (240, 185, 0),     # yellow windows
        "wing":         (195, 200, 210),   # gray
        "engine":       (45, 50, 60),      # dark gray
        "cockpit":      (110, 185, 255),   # blue tint
        "nav_light":    (255, 220, 0),     # yellow
    },
    "united": {
        "name": "United",
        "tail":         (0, 25, 100),      # deep navy tail
        "fuselage":     (240, 242, 245),   # white
        "fuselage_dark":(0, 25, 100),      # navy belly
        "window":       (190, 155, 0),     # gold windows
        "wing":         (180, 185, 195),   # gray
        "engine":       (55, 60, 70),      # dark gray
        "cockpit":      (110, 185, 255),   # blue tint
        "nav_light":    (255, 70, 70),     # red
    },
    "suncountry": {
        "name": "Sun Country",
        "tail":         (0, 60, 160),      # blue half of tail
        "fuselage":     (245, 245, 248),   # white upper fuselage
        "fuselage_dark":(220, 100, 20),    # orange lower fuselage
        "window":       (220, 100, 20),    # orange windows
        "wing":         (180, 185, 195),   # gray
        "engine":       (55, 60, 70),      # dark gray
        "cockpit":      (110, 185, 255),   # blue tint
        "nav_light":    (220, 100, 20),    # orange
    },
    "skywest": {
        "name": "SkyWest",
        "tail":         (15, 40, 120),     # dark blue tail
        "fuselage":     (215, 218, 222),   # light gray
        "fuselage_dark":(140, 145, 155),   # darker gray belly
        "window":       (30, 80, 190),     # blue windows
        "wing":         (170, 175, 185),   # gray
        "engine":       (55, 60, 70),      # dark gray
        "cockpit":      (110, 185, 255),   # blue tint
        "nav_light":    (255, 70, 70),     # red
    },
    "endeavor": {
        "name": "Endeavor",
        "tail":         (90, 30, 150),     # purple tail
        "fuselage":     (225, 225, 228),   # light gray
        "fuselage_dark":(150, 100, 190),   # purple belly
        "window":       (140, 80, 200),    # purple windows
        "wing":         (175, 178, 188),   # gray
        "engine":       (55, 60, 70),      # dark gray
        "cockpit":      (110, 185, 255),   # blue tint
        "nav_light":    (255, 70, 70),     # red
    },
    "republic": {
        "name": "Republic",
        "tail":         (10, 35, 115),     # dark blue tail
        "fuselage":     (238, 240, 244),   # white
        "fuselage_dark":(10, 35, 115),     # navy belly
        "window":       (50, 110, 210),    # blue windows
        "wing":         (175, 180, 190),   # gray
        "engine":       (55, 60, 70),      # dark gray
        "cockpit":      (110, 185, 255),   # blue tint
        "nav_light":    (255, 70, 70),     # red
    },
    "aerlingus": {
        "name": "Aer Lingus",
        "tail":         (0, 145, 110),     # bright teal tail
        "fuselage":     (240, 242, 245),   # white
        "fuselage_dark":(0, 100, 80),      # dark teal belly
        "window":       (0, 175, 135),     # teal windows
        "wing":         (175, 180, 190),   # gray
        "engine":       (55, 60, 70),      # dark gray
        "cockpit":      (110, 185, 255),   # blue tint
        "nav_light":    (0, 175, 135),     # teal nav light
    },
}

# ── Weighted random selection ──────────────────────────────────────────────────

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
    t  = scheme["tail"]
    f  = scheme["fuselage"]
    fd = scheme["fuselage_dark"]
    w  = scheme["window"]
    wg = scheme["wing"]
    e  = scheme["engine"]
    c  = scheme["cockpit"]
    nl = scheme["nav_light"]

    wg_dark = tuple(max(0, v - 40) for v in wg)

    pixels = [
        # Tail: vertical stabilizer
        (0, 1, t),
        (0, 2, t),
        (0, 3, t),
        (1, 2, t),
        (1, 3, t),
        (1, 4, t),

        # Rear fuselage — dark belly bottom, white top
        (2, 3, fd),
        (2, 4, f),
        (2, 5, f),
        (2, 6, f),
        (2, 7, fd),

        # Main fuselage — top row white, bottom row dark (belly stripe)
        (3,  4, fd), (3,  5, f), (3,  6, f), (3,  7, fd),
        (4,  4, fd), (4,  5, f), (4,  6, f), (4,  7, fd),
        (5,  4, fd), (5,  5, f), (5,  6, f), (5,  7, fd),
        (6,  4, fd), (6,  5, f), (6,  6, f), (6,  7, fd),
        (7,  4, fd), (7,  5, f), (7,  6, f), (7,  7, fd),
        (8,  4, fd), (8,  5, f), (8,  6, f), (8,  7, fd),
        (9,  4, fd), (9,  5, f), (9,  6, f), (9,  7, fd),
        (10, 4, fd), (10, 5, f), (10, 6, f), (10, 7, fd),
        (11, 4, fd), (11, 5, f), (11, 6, f), (11, 7, fd),
        (12, 4, fd), (12, 5, f), (12, 6, f), (12, 7, fd),
        (13, 4, fd), (13, 5, f), (13, 6, f), (13, 7, fd),
        (14, 4, fd), (14, 5, f), (14, 6, f), (14, 7, fd),

        # Cockpit and nose
        (15, 3, c),
        (15, 4, c),
        (15, 5, f),
        (15, 6, f),
        (15, 7, fd),
        (16, 4, c),
        (16, 5, f),
        (16, 6, fd),
        (17, 5, f),

        # Passenger windows — window color as stripe
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

        # Navigation light
        (4, 12, nl),
    ]

    return pixels