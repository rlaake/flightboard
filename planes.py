# planes.py
import random

AIRLINE_SCHEMES = {
    "delta": {
        "name": "Delta",
        "tail":         (200, 0, 20),
        "fuselage":     (245, 245, 248),
        "fuselage_dark":(15, 25, 80),
        "window":       (15, 25, 80),
        "wing":         (185, 190, 200),
        "engine":       (60, 65, 75),
        "cockpit":      (110, 185, 255),
        "nav_light":    (255, 70, 70),
    },
    "american": {
        "name": "American",
        "tail":         (160, 165, 175),
        "fuselage":     (235, 235, 238),
        "fuselage_dark":(160, 165, 175),
        "window":       (180, 0, 30),
        "wing":         (175, 180, 190),
        "engine":       (55, 60, 70),
        "cockpit":      (110, 185, 255),
        "nav_light":    (255, 70, 70),
    },
    "southwest": {
        "name": "Southwest",
        "tail":         (210, 35, 25),
        "fuselage":     (30, 100, 200),
        "fuselage_dark":(20, 70, 150),
        "window":       (240, 185, 0),
        "wing":         (195, 200, 210),
        "engine":       (45, 50, 60),
        "cockpit":      (110, 185, 255),
        "nav_light":    (255, 220, 0),
    },
    "united": {
        "name": "United",
        "tail":         (0, 25, 100),
        "fuselage":     (240, 242, 245),
        "fuselage_dark":(0, 25, 100),
        "window":       (190, 155, 0),
        "wing":         (180, 185, 195),
        "engine":       (55, 60, 70),
        "cockpit":      (110, 185, 255),
        "nav_light":    (255, 70, 70),
    },
    "suncountry": {
        "name": "Sun Country",
        "tail":         (0, 60, 160),
        "fuselage":     (245, 245, 248),
        "fuselage_dark":(220, 100, 20),
        "window":       (220, 100, 20),
        "wing":         (180, 185, 195),
        "engine":       (55, 60, 70),
        "cockpit":      (110, 185, 255),
        "nav_light":    (220, 100, 20),
    },
    "skywest": {
        "name": "SkyWest",
        "tail":         (15, 40, 120),
        "fuselage":     (215, 218, 222),
        "fuselage_dark":(140, 145, 155),
        "window":       (30, 80, 190),
        "wing":         (170, 175, 185),
        "engine":       (55, 60, 70),
        "cockpit":      (110, 185, 255),
        "nav_light":    (255, 70, 70),
    },
    "endeavor": {
        "name": "Endeavor",
        "tail":         (90, 30, 150),
        "fuselage":     (225, 225, 228),
        "fuselage_dark":(150, 100, 190),
        "window":       (140, 80, 200),
        "wing":         (175, 178, 188),
        "engine":       (55, 60, 70),
        "cockpit":      (110, 185, 255),
        "nav_light":    (255, 70, 70),
    },
    "republic": {
        "name": "Republic",
        "tail":         (10, 35, 115),
        "fuselage":     (238, 240, 244),
        "fuselage_dark":(10, 35, 115),
        "window":       (50, 110, 210),
        "wing":         (175, 180, 190),
        "engine":       (55, 60, 70),
        "cockpit":      (110, 185, 255),
        "nav_light":    (255, 70, 70),
    },
    "aerlingus": {
        "name": "Aer Lingus",
        "tail":         (0, 145, 110),
        "fuselage":     (240, 242, 245),
        "fuselage_dark":(0, 100, 80),
        "window":       (0, 175, 135),
        "wing":         (175, 180, 190),
        "engine":       (55, 60, 70),
        "cockpit":      (110, 185, 255),
        "nav_light":    (0, 175, 135),
    },
}

_WEIGHTS = {
    "delta":      12,
    "american":   12,
    "southwest":  12,
    "united":     12,
    "suncountry": 12,
    "skywest":    12,
    "endeavor":   12,
    "republic":   12,
    "aerlingus":   4,
}

_AIRLINES = list(_WEIGHTS.keys())
_WEIGHT_VALUES = [_WEIGHTS[a] for a in _AIRLINES]


def get_random_airline() -> dict:
    key = random.choices(_AIRLINES, weights=_WEIGHT_VALUES, k=1)[0]
    return AIRLINE_SCHEMES[key]


def _fuselage_color(scheme: dict, x: int, y: int) -> tuple:
    """
    Returns the fuselage color for a given pixel position.
    Handles special cases like Sun Country's diagonal split.
    """
    if scheme["name"] == "Sun Country":
        # Diagonal split: orange forward-lower, white rear-upper
        # Split point at x=9, diagonal goes top-right to bottom-left
        # Forward (x < 9): orange below the diagonal, white above
        # Rear (x >= 9): always white
        if x >= 9:
            return scheme["fuselage"]
        else:
            # Diagonal threshold — as x decreases toward nose,
            # orange extends higher
            diagonal_y = 4 + (9 - x) // 2
            if y >= diagonal_y:
                return scheme["fuselage_dark"]  # orange
            else:
                return scheme["fuselage"]        # white
    else:
        # Standard: fuselage_dark on top and bottom rows, fuselage in middle
        if y in (4, 9):
            return scheme["fuselage_dark"]
        return scheme["fuselage"]


def build_plane_pixels(scheme: dict) -> list:
    """
    Build a list of (x, y, color) tuples for the plane sprite.
    Plane faces right, tail at x=0, nose at x=17.
    Sprite is 18px wide x 17px tall (y=0 to y=16).
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
        # ── Tail: vertical stabilizer (taller now) ──
        (0, 0, t),
        (0, 1, t),
        (0, 2, t),
        (0, 3, t),
        (1, 1, t),
        (1, 2, t),
        (1, 3, t),
        (1, 4, t),
        (2, 2, t),
        (2, 3, t),

        # ── Rear fuselage ──
        (2, 4, fd),
        (2, 5, f),
        (2, 6, f),
        (2, 7, f),
        (2, 8, f),
        (2, 9, fd),

        # ── Main fuselage body (4px tall: rows 4-9) ──
    ]

    # Build fuselage dynamically to handle Sun Country diagonal
    for x in range(3, 15):
        pixels.append((x, 4, _fuselage_color(scheme, x, 4)))
        pixels.append((x, 5, _fuselage_color(scheme, x, 5)))
        pixels.append((x, 6, _fuselage_color(scheme, x, 6)))
        pixels.append((x, 7, _fuselage_color(scheme, x, 7)))
        pixels.append((x, 8, _fuselage_color(scheme, x, 8)))
        pixels.append((x, 9, _fuselage_color(scheme, x, 9)))

    pixels += [
        # ── Cockpit and nose ──
        (15, 3, c),
        (15, 4, c),
        (15, 5, c),
        (15, 6, f),
        (15, 7, f),
        (15, 8, f),
        (15, 9, fd),
        (16, 4, c),
        (16, 5, c),
        (16, 6, f),
        (16, 7, f),
        (16, 8, fd),
        (17, 5, f),
        (17, 6, f),
        (17, 7, fd),

        # ── Passenger windows (two rows for taller fuselage) ──
        (5,  5, w), (5,  6, w),
        (6,  5, w), (6,  6, w),
        (7,  5, w), (7,  6, w),
        (8,  5, w), (8,  6, w),
        (9,  5, w), (9,  6, w),
        (10, 5, w), (10, 6, w),
        (11, 5, w), (11, 6, w),
        (12, 5, w), (12, 6, w),
        (13, 5, w), (13, 6, w),
        (14, 5, w), (14, 6, w),

        # ── Top wing (bigger) ──
        (6,  3, wg),
        (7,  2, wg),
        (7,  3, wg),
        (8,  1, wg),
        (8,  2, wg),
        (9,  1, wg),
        (9,  2, wg),
        (10, 1, wg),
        (10, 2, wg),

        # ── Lower wing (bigger) ──
        (6,  10, wg),
        (7,  10, wg),
        (7,  11, wg),
        (6,  11, wg),
        (5,  11, wg),
        (5,  12, wg),
        (4,  12, wg),
        (4,  13, wg),
        (3,  13, wg),
        (3,  14, wg_dark),
        (2,  14, wg_dark),

        # ── Engine (larger, under wing) ──
        (7,  12, e),
        (8,  12, e),
        (9,  12, e),
        (7,  13, wg),
        (8,  13, wg),
        (9,  13, wg),

        # ── Navigation light ──
        (2, 14, nl),
        (2, 15, nl),
    ]

    return pixels