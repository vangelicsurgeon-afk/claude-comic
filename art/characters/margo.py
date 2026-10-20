"""Margo Voss, senior caseworker. Origin at the feet, ~235 units tall, drawn facing right.

draw(pose, expression, facing) -> SVG fragment string.
poses: stand, point, shrug, hold, arms_up, sit_desk (torso only, for behind a desk)
expressions: neutral, deadpan, happy, worried, surprised, smug, annoyed
"""
from ..palette import *

SHOULDERS = {"L": (-26, -146), "R": (26, -146)}

POSES = {  # hand targets (L, R) and elbow bend offsets
    "stand":   {"L": (-34, -94), "R": (34, -94)},
    "point":   {"L": (-32, -96), "R": (86, -156)},
    "shrug":   {"L": (-58, -128), "R": (58, -128)},
    "hold":    {"L": (-8, -104), "R": (40, -116)},
    "arms_up": {"L": (-52, -206), "R": (52, -206)},
}


def _arm(side, hand):
    sx, sy = SHOULDERS[side]
    hx, hy = hand
    out = 1 if side == "R" else -1
    cx, cy = (sx + hx) / 2 + out * 8, (sy + hy) / 2 + 12
    d = f"M{sx},{sy} Q{cx:.1f},{cy:.1f} {hx},{hy}"
    return (path(d, stroke=INK, w=17) + path(d, stroke=MUSTARD, w=10)
            + circle(hx, hy, 8, fill=SKIN_MARGO, w=3.5))


def _face(expression):
    """Face drawn centered at (0,0) in head space; head radius 34."""
    px = 3  # pupils look toward the facing direction
    brow, mouth, eyes = "", "", ""
    # eye openness / shape
    def eye(x, open_=1.0, pupil=True):
        lens = ellipse(x, 0, 11, 11, fill="#fff", w=3)
        pup = circle(x + px, 1, 4.2 * (1 if open_ >= 0.6 else 1), fill=INK, w=0) if pupil else ""
        lid = ""
        if open_ < 1.0:  # half-lid drawn as a flat chord over the top
            h = 11 * (1 - open_) * 2
            lid = (f'<path d="M{x-11},0 A11 11 0 0 1 {x+11},0 L{x+11},{-11+h:.1f} '
                   f'L{x-11},{-11+h:.1f} Z" fill="{SKIN_MARGO}" stroke="none"/>'
                   f'<line x1="{x-11}" y1="{-11+h:.1f}" x2="{x+11}" y2="{-11+h:.1f}" '
                   f'stroke="{INK}" stroke-width="3"/>')
        return lens + pup + lid
    E = {
        "neutral":  dict(o=1.0, b=((-20, -20, -6, -22), (6, -22, 20, -20)), m="M-7,18 L7,18"),
        "deadpan":  dict(o=0.55, b=((-20, -19, -6, -19), (6, -19, 20, -19)), m="M-7,19 L7,19"),
        "happy":    dict(o=1.0, b=((-20, -22, -6, -26), (6, -26, 20, -22)), m="M-10,14 Q0,26 10,14"),
        "worried":  dict(o=1.0, b=((-20, -16, -6, -24), (6, -24, 20, -16)), m="M-9,21 Q0,12 9,21"),
        "surprised":dict(o=1.0, b=((-20, -28, -6, -29), (6, -29, 20, -28)), m=None),
        "smug":     dict(o=0.6, b=((-20, -20, -6, -22), (6, -26, 20, -22)), m="M-9,18 Q4,22 11,13"),
        "annoyed":  dict(o=0.7, b=((-20, -22, -6, -16), (6, -16, 20, -22)), m="M-8,20 Q0,16 8,20"),
    }[expression]
    o = E["o"]
    eyes = eye(-14, o) + eye(14, o)
    glasses = (circle(-14, 0, 14, fill="none", w=3.2) + circle(14, 0, 14, fill="none", w=3.2)
               + line(-1, -1, 1, -1, w=3.2))
    for (x1, y1, x2, y2) in E["b"]:
        brow += line(x1, y1 - 6, x2, y2 - 6, w=3.6)
    if E["m"]:
        mouth = path(E["m"], w=3.6)
    else:
        mouth = ellipse(0, 20, 5, 6.5, fill="#6b2f2f", w=3)
    return eyes + glasses + brow + mouth


def draw(pose="stand", expression="neutral", facing="right"):
    parts = []
    if pose != "sit_desk":
        # legs + shoes
        for x in (-12, 12):
            parts.append(line(x, -62, x, -8, w=14, c=INK))
            parts.append(line(x, -62, x, -8, w=7, c=RUST))
            parts.append(ellipse(x + 5, -3, 13, 7, fill=INK, w=3))
        # skirt / cardigan body
        parts.append(path("M-34,-62 L-28,-152 Q0,-164 28,-152 L34,-62 Q0,-52 -34,-62 Z", fill=MUSTARD))
        parts.append(line(0, -156, 0, -58, w=3))
        for y in (-132, -108, -84):
            parts.append(circle(7, y, 3.2, fill=INK, w=0))
        parts.append(path("M-34,-62 Q0,-52 34,-62", stroke=INK, w=3))
    else:
        parts.append(path("M-34,0 L-28,-152 Q0,-164 28,-152 L34,0 Z", fill=MUSTARD))
        parts.append(line(0, -156, 0, 0, w=3))
        for y in (-132, -108, -84):
            parts.append(circle(7, y, 3.2, fill=INK, w=0))
    # collar + neck
    parts.append(rect(-8, -166, 16, 16, fill=SKIN_MARGO, sw=3.5))
    parts.append(path("M-18,-152 L0,-140 L18,-152", stroke=INK, w=3.5, fill=PAPER))
    # arms (far arm first so the near arm overlaps)
    hands = POSES["stand" if pose == "sit_desk" else pose]
    if pose == "sit_desk":
        hands = {"L": (-36, -70), "R": (40, -66)}
    parts.append(_arm("L", hands["L"]))
    parts.append(_arm("R", hands["R"]))
    # head
    hx, hy = 0, -196
    parts.append(f'<g transform="translate({hx},{hy})">')
    parts.append(circle(-24, -22, 15, fill=HAIR_GREY))  # bun, back of head
    parts.append(circle(0, 0, 36, fill=SKIN_MARGO))
    parts.append(path("M-36,-4 Q-36,-40 0,-40 Q34,-40 36,-8 Q18,-36 -6,-31 Q-26,-30 -36,-4 Z",
                      fill=HAIR_GREY, w=3.5))
    parts.append(f'<g transform="translate(0,4)">{_face(expression)}</g>')
    parts.append("</g>")
    return flip_group("".join(parts), facing)
