"""Pip, the new hire: a small lavender wisp with a flame on its head. Origin at the feet, ~120 tall.

draw(pose, expression, facing) -> SVG fragment string.
poses: stand, point, wave, hold, arms_up, slump
expressions: neutral, happy, worried, surprised, proud, sad, flustered
The flame is Pip's mood ring: tall when happy/proud, tiny when sad, jittery when flustered.
"""
from ..palette import *

POSES = {
    "stand":   {"L": (-42, -44), "R": (42, -44)},
    "point":   {"L": (-40, -42), "R": (66, -70)},
    "wave":    {"L": (-40, -44), "R": (58, -96)},
    "hold":    {"L": (-24, -38), "R": (28, -40)},
    "arms_up": {"L": (-46, -100), "R": (46, -100)},
    "slump":   {"L": (-36, -22), "R": (36, -22)},
}


def _flame(expression):
    k = {"happy": 1.25, "proud": 1.4, "neutral": 1.0, "surprised": 1.35, "worried": 0.8,
         "sad": 0.5, "flustered": 1.1}[expression]
    lean = {"flustered": 10, "worried": -4}.get(expression, 0)
    h = 30 * k
    base = -104
    outer = (f"M-11,{base} Q-14,{base - h * 0.5:.1f} {lean * 0.5:.1f},{base - h:.1f} "
             f"Q{14 + lean * 0.3:.1f},{base - h * 0.5:.1f} 11,{base} Z")
    inner = (f"M-5.5,{base} Q-7,{base - h * 0.3:.1f} {lean * 0.3:.1f},{base - h * 0.62:.1f} "
             f"Q7,{base - h * 0.3:.1f} 5.5,{base} Z")
    return path(outer, fill=FLAME, w=3.5) + path(inner, fill=FLAME_CORE, stroke="none", w=0)


def _face(expression):
    cy = -66
    def eye(x, r=9, look=2.5, h=1.0):
        return (ellipse(x, cy, r, r * 1.15 * h, fill="#fff", w=3)
                + circle(x + look, cy + 1.5, r * 0.5, fill=INK, w=0))
    cheeks = ellipse(-24, cy + 14, 6, 4, fill=CHEEK, stroke="none", w=0) + \
             ellipse(24, cy + 14, 6, 4, fill=CHEEK, stroke="none", w=0)
    brows, mouth = "", ""
    eyes = eye(-13) + eye(13)
    if expression == "neutral":
        mouth = path("M-5,-46 Q0,-43 5,-46", w=3.2)
    elif expression == "happy":
        mouth = path("M-8,-48 Q0,-36 8,-48 Z", fill="#6b2f2f", w=3)
    elif expression == "proud":
        mouth = path("M-8,-47 Q0,-38 8,-47", w=3.2)
        brows = line(-21, cy - 16, -6, cy - 17, w=3) + line(6, cy - 17, 21, cy - 16, w=3)
    elif expression == "worried":
        brows = line(-21, cy - 12, -7, cy - 19, w=3) + line(7, cy - 19, 21, cy - 12, w=3)
        mouth = path("M-6,-42 Q0,-48 6,-42", w=3.2)
    elif expression == "sad":
        eyes = eye(-13, h=0.8, look=0) + eye(13, h=0.8, look=0)
        brows = line(-21, cy - 10, -7, cy - 18, w=3) + line(7, cy - 18, 21, cy - 10, w=3)
        mouth = path("M-6,-41 Q0,-49 6,-41", w=3.2)
        cheeks += path("M-13,-52 Q-15,-44 -13,-40", stroke="#7fb7e8", w=3)
    elif expression == "surprised":
        eyes = eye(-13, r=10, look=0) + eye(13, r=10, look=0)
        brows = line(-21, cy - 18, -6, cy - 20, w=3) + line(6, cy - 20, 21, cy - 18, w=3)
        mouth = ellipse(0, -44, 4.5, 6, fill="#6b2f2f", w=3)
    elif expression == "flustered":
        eyes = eye(-13, r=8, look=-3) + eye(13, r=10, look=-3)
        brows = line(-21, cy - 14, -7, cy - 18, w=3) + line(7, cy - 16, 21, cy - 12, w=3)
        mouth = path("M-7,-44 Q-3,-48 0,-44 Q3,-40 7,-44", w=3.2)
        cheeks += path("M26,-84 L30,-90 M31,-82 L35,-88", stroke="#7fb7e8", w=3)
    return cheeks + eyes + brows + mouth


def _arm(side, hand):
    sx = -34 if side == "L" else 34
    sy = -52
    hx, hy = hand
    d = f"M{sx},{sy} Q{(sx + hx) / 2:.1f},{(sy + hy) / 2 + 10:.1f} {hx},{hy}"
    return path(d, stroke=INK, w=13) + path(d, stroke=LAVENDER, w=7) + circle(hx, hy, 6, fill=LAVENDER, w=3)


def draw(pose="stand", expression="neutral", facing="right"):
    parts = []
    squash = 4 if pose == "slump" else 0
    parts.append(ellipse(-14, -3, 12, 6, fill=INK, w=3) + ellipse(14, -3, 12, 6, fill=INK, w=3))
    parts.append(_flame(expression))
    body = (f"M-38,-10 Q-46,-60 -30,-92 Q0,-120 30,-92 Q46,-60 38,-10 Q0,{2 - squash} -38,-10 Z")
    parts.append(path(body, fill=LAVENDER))
    parts.append(path("M-26,-30 Q0,-24 26,-30", stroke="#cdbff0", w=3))  # belly crease
    hands = POSES[pose]
    parts.append(_arm("L", hands["L"]))
    parts.append(_arm("R", hands["R"]))
    parts.append(_face(expression))
    return flip_group("".join(parts), facing)
