"""Fen, Medium Miracles caseworker (5th floor): a small grey raincloud in a neat tie. They.
Origin on the floor directly beneath Fen (Fen floats; a soft shadow marks the floor). ~140 tall, cloud ~140 wide.

draw(pose, expression, facing, look, drizzle) -> SVG fragment string.
poses: stand, point, wave, hold (clipboard in front), tie (right hand straightening the tie knot), arms_up
expressions: neutral, polite (small professional smile), proud, worried, surprised, sad, flustered
look: side (default), front, up, down.
drizzle: None = from the expression (worried 1, surprised 1, sad 2, flustered 2, else 0), or 0/1/2/3 to force it.
Drizzle is Fen's mood gauge, like Pip's flame. Never explained in dialogue.
"""
from ..palette import *

CLOUD = "#aeb4bf"
CLOUD_HI = "#cdd2da"
TIE = WALL_DARK
RAIN = "#6f8fb3"

BODY = ("M-58,-62 Q-76,-64 -70,-84 Q-82,-106 -56,-112 Q-52,-138 -24,-134 Q-10,-154 12,-142 "
        "Q36,-152 44,-128 Q72,-128 66,-104 Q82,-86 64,-70 Q66,-56 48,-60 Q0,-54 -58,-62 Z")

POSES = {  # hand targets (L, R); shoulders at the cloud's lower sides (-56,-74), (56,-74); arms drawn behind the body
    "stand":   {"L": (-76, -44), "R": (76, -44)},
    "point":   {"L": (-76, -44), "R": (110, -92)},
    "wave":    {"L": (-76, -44), "R": (96, -134)},
    "hold":    {"L": (18, -40), "R": (68, -40)},
    "tie":     {"L": (-76, -44), "R": (10, -56)},
    "arms_up": {"L": (-92, -140), "R": (92, -140)},
}
AUTO_DRIZZLE = {"worried": 1, "surprised": 1, "sad": 2, "flustered": 2}
LOOK = {"side": (2.2, 0.5), "front": (0, 0.5), "up": (0.5, -3), "down": (0.5, 3.5)}


def _arm(side, hand):
    sx, sy = (-56, -74) if side == "L" else (56, -74)
    hx, hy = hand
    d = f"M{sx},{sy} Q{(sx + hx) / 2:.1f},{(sy + hy) / 2 + 10:.1f} {hx},{hy}"
    return path(d, stroke=INK, w=11) + path(d, stroke=CLOUD, w=5.5) + circle(hx, hy, 6, fill=CLOUD, w=3)


def _face(expression, look="side"):
    cy = -100
    lx, ly = LOOK[look]
    def eye(x, r=6.5, lid=0.0):
        out = ellipse(x, cy, r, r * 1.2, fill="#fff", w=2.8) + circle(x + lx, cy + ly, r * 0.55, fill=INK, w=0)
        if lid:  # businesslike upper lid
            out += path(f"M{x - r - 1},{cy - r * 1.2 + lid} L{x + r + 1},{cy - r * 1.2 + lid}", w=3)
            out += f'<rect x="{x - r:.1f}" y="{cy - r * 1.25:.1f}" width="{2 * r:.1f}" height="{lid:.1f}" fill="{CLOUD}"/>'
        return out
    brows, mouth, extra = "", "", ""
    eyes = eye(-14, lid=3) + eye(14, lid=3)
    if expression == "neutral":
        mouth = line(-6, -82, 6, -82, w=3)
    elif expression == "polite":
        eyes = eye(-14) + eye(14)
        brows = line(-21, cy - 15, -8, cy - 17, w=3) + line(8, cy - 17, 21, cy - 15, w=3)
        mouth = path("M-10,-84 Q0,-74 10,-84", w=3)
    elif expression == "proud":
        eyes = eye(-14, lid=6) + eye(14, lid=6)
        brows = line(-22, cy - 18, -7, cy - 14, w=3) + line(7, cy - 14, 22, cy - 18, w=3)
        mouth = path("M-10,-84 Q3,-74 12,-88", w=3.2)
    elif expression == "worried":
        eyes = eye(-14) + eye(14)
        brows = line(-21, cy - 10, -8, cy - 16, w=3) + line(8, cy - 16, 21, cy - 10, w=3)
        mouth = path("M-6,-79 Q0,-85 6,-79", w=3)
    elif expression == "surprised":
        eyes = eye(-14, r=7.5) + eye(14, r=7.5)
        brows = line(-21, cy - 18, -8, cy - 21, w=3) + line(8, cy - 21, 21, cy - 18, w=3)
        mouth = ellipse(0, -79, 4.5, 6, fill="#4a3a4f", w=2.8)
    elif expression == "sad":
        eyes = eye(-14, lid=4) + eye(14, lid=4)
        brows = line(-22, cy - 6, -8, cy - 15, w=3) + line(8, cy - 15, 22, cy - 6, w=3)
        mouth = path("M-7,-77 Q0,-85 7,-77", w=3)
    elif expression == "flustered":
        eyes = eye(-14, r=5.5) + eye(14, r=7.5)
        brows = line(-21, cy - 12, -8, cy - 16, w=3) + line(8, cy - 15, 21, cy - 10, w=3)
        mouth = path("M-8,-81 Q-4,-85 0,-81 Q4,-77 8,-81", w=3)
        extra = path("M34,-120 Q28,-108 34,-102 Q40,-108 34,-120 Z", fill="#bcd3ea", w=2.5)
    return eyes + brows + mouth + extra


def _drizzle(level):
    if not level:
        return ""
    xs = {1: (-30, 6, 36), 2: (-42, -18, 6, 30, 50), 3: (-50, -34, -18, -2, 14, 30, 46, 58)}[min(level, 3)]
    ln = {1: 12, 2: 16, 3: 20}[min(level, 3)]
    out = ""
    for i, x in enumerate(xs):
        y0 = -54 + (i % 2) * 14
        out += line(x, y0, x - 3, y0 + ln, w=3, c=RAIN)
        out += line(x - 5, y0 + ln + 12, x - 7, y0 + ln + 12 + ln * 0.6, w=3, c=RAIN)
    return out


def draw(pose="stand", expression="neutral", facing="right", look="side", drizzle=None):
    level = AUTO_DRIZZLE.get(expression, 0) if drizzle is None else drizzle
    parts = [f'<ellipse cx="0" cy="-2" rx="34" ry="6" fill="{INK}" opacity="0.15"/>']
    parts.append(_drizzle(level))
    hands = POSES[pose]
    parts.append(_arm("L", hands["L"]))
    if pose != "tie":
        parts.append(_arm("R", hands["R"]))
    # tie hangs below the cloud from a white collar
    parts.append(path("M-6,-60 L6,-60 L10,-22 L0,-10 L-10,-22 Z", fill=TIE, w=3))
    parts.append(path("M-14,-64 L0,-52 L14,-64", fill="#ffffff", w=3))
    parts.append(path("M-5,-60 L5,-60 L3,-52 L-3,-52 Z", fill=TIE, w=2.5))
    parts.append(path(BODY, fill=CLOUD))
    parts.append(path("M-44,-112 Q-40,-128 -22,-126 M0,-138 Q14,-142 26,-134", stroke=CLOUD_HI, w=5))
    parts.append(f'<g transform="translate(4,0)">{_face(expression, look)}</g>')
    if pose == "hold":
        parts.append(rect(18, -66, 50, 56, fill="#c9a571", sw=3.5, r=3) + rect(25, -59, 36, 42, fill="#ffffff", sw=2.5)
                     + line(30, -48, 56, -48, w=2) + line(30, -38, 56, -38, w=2) + rect(35, -70, 16, 8, fill="#8d9aa3", sw=2.5))
        parts.append(circle(18, -40, 6, fill=CLOUD, w=3) + circle(68, -40, 6, fill=CLOUD, w=3))
        return flip_group("".join(parts), facing)
    if pose == "tie":  # the hand at the knot crosses in front of the body
        parts.append(_arm("R", hands["R"]))
    return flip_group("".join(parts), facing)
