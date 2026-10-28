"""Props and settings for the Department. Fragments use local origin as documented.

desk(w)            origin: top-centre of desktop surface; draws the front panel below it
folder(color)      origin: bottom-centre; a case folder standing/lying ~44 wide
mug(steam)         origin: bottom-centre; ~28 wide
tube_station()     origin: bottom-centre; wall pneumatic-tube mouth with brass hatch ~70 wide
clipboard()        origin: top-left of the board, ~52x66
stamp()            origin: bottom-centre; rubber stamp ~30 tall
paper_stack(n)     origin: bottom-centre; n sheets ~50 wide
window(night)      origin: top-left; 120x150 window
earring(scale)     origin: bottom-centre; silver hoop ~26 tall (draw it big for close-ups)
tin()              origin: bottom-centre; round button tin ~40 wide, lid slightly ajar
form(color)        origin: bottom-centre; one flat sheet ~44x56 (white, pink, yellow copies)
office_bg(w, h, ...) full-panel background: wall, floor line, optional window
"""
from .palette import *


def desk(w=300):
    top = rect(-w / 2, 0, w, 14, fill=WOOD, sw=4, r=3)
    body = rect(-w / 2 + 14, 14, w - 28, 90, fill="#b98355", sw=4)
    drawer = rect(-w / 2 + 30, 30, 90, 56, fill="#a87647", sw=3) + circle(-w / 2 + 75, 58, 4, fill=MUSTARD, w=2.5)
    return body + drawer + top


def folder(color=MUSTARD):
    return (rect(-22, -30, 44, 30, fill=color, sw=3.5, r=2)
            + path("M-22,-30 L-22,-36 L-6,-36 L0,-30", fill=color, w=3.5)
            + line(-14, -16, 14, -16, w=2.5))


def mug(steam=True):
    s = ""
    if steam:
        s = path("M-4,-30 Q-9,-38 -4,-44 M5,-30 Q0,-38 5,-44", stroke="#9aa0a6", w=2.5)
    return s + rect(-12, -24, 24, 24, fill="#fff", sw=3.5, r=4) + path("M12,-18 Q22,-18 22,-10 Q22,-4 12,-5", w=3.5)


def tube_station():
    return (rect(-36, -96, 72, 96, fill="#8a6a3b", sw=4, r=6)
            + ellipse(0, -52, 24, 24, fill="#1f1a24", w=4)
            + rect(-30, -96, 60, 12, fill=MUSTARD, sw=3.5, r=3)
            + path("M0,-130 L0,-96", stroke=INK, w=14) + path("M0,-130 L0,-96", stroke="#c9a24b", w=8))


def clipboard():
    return (rect(0, 0, 52, 66, fill=WOOD, sw=3.5, r=3) + rect(6, 8, 40, 52, fill="#fff", sw=2.5)
            + rect(16, -4, 20, 10, fill="#9aa0a6", sw=3, r=2)
            + line(12, 22, 40, 22, w=2.5) + line(12, 32, 40, 32, w=2.5) + line(12, 42, 32, 42, w=2.5))


def stamp():
    return (rect(-14, -12, 28, 12, fill=RUST, sw=3.5, r=2) + rect(-5, -30, 10, 18, fill="#c8956b", sw=3.5, r=3)
            + ellipse(0, -32, 9, 5, fill="#c8956b", w=3.5))


def paper_stack(n=4):
    out = ""
    for i in range(n):
        out += rect(-25, -6 * (i + 1), 50, 6, fill="#fff", sw=2.5)
    return out


def window(night=True):
    sky = NIGHT if night else "#aee0f5"
    out = rect(0, 0, 120, 150, fill=sky, sw=5)
    if night:
        for (x, y) in ((22, 22), (86, 36), (60, 70), (30, 100), (96, 108)):
            out += circle(x, y, 2.4, fill=FLAME_CORE, w=0)
        out += circle(88, 26, 11, fill=PAPER, w=0)
    out += line(60, 0, 60, 150, w=5) + line(0, 75, 120, 75, w=5)
    out += rect(-8, 150, 136, 10, fill=WOOD, sw=4, r=2)
    return out


def earring():
    return (circle(0, -14, 12, fill="none", stroke=INK, w=6) + circle(0, -14, 12, fill="none", stroke="#c9ced6", w=3)
            + circle(0, -29, 3.5, fill="#c9ced6", w=2.5))


def tin():
    return (rect(-20, -22, 40, 22, fill=RUST, sw=3.5, r=3) + rect(-22, -30, 44, 9, fill=MUSTARD, sw=3.5, r=3)
            + circle(-8, -10, 3, fill=PAPER, w=2) + circle(6, -12, 3, fill=PAPER, w=2))


def form(color="#ffffff"):
    return (rect(-22, -56, 44, 56, fill=color, sw=3, r=1)
            + line(-14, -42, 14, -42, w=2.5) + line(-14, -32, 14, -32, w=2.5) + line(-14, -22, 4, -22, w=2.5))


def office_bg(w, h, floor_y=None, window_at=None, night=False):
    """Back wall, wainscot stripe and floor for a panel of size w x h."""
    floor_y = floor_y if floor_y is not None else h * 0.78
    wall = WALL if not night else "#7ea9ae"
    out = f'<rect x="0" y="0" width="{w}" height="{h}" fill="{wall}"/>'
    out += f'<rect x="0" y="{floor_y - 70}" width="{w}" height="70" fill="{WALL_DARK}" opacity="0.28"/>'
    out += line(0, floor_y - 70, w, floor_y - 70, w=3, c=WALL_DARK)
    out += f'<rect x="0" y="{floor_y}" width="{w}" height="{h - floor_y}" fill="{FLOOR}"/>'
    out += line(0, floor_y, w, floor_y, w=4)
    if window_at:
        out += f'<g transform="translate({window_at[0]},{window_at[1]})">{window(night=True)}</g>'
    return out


def note(big=False):
    """Hollis's tube note. origin: bottom-centre; small folded slip ~34x24, or big=True a ~300x190 close-up slip with typed text."""
    if not big:
        return (rect(-17, -24, 34, 24, fill="#fffdf4", sw=3, r=1) + line(-17, -24, 0, -12, w=2.5) + line(17, -24, 0, -12, w=2.5))
    return (rect(-150, -190, 300, 190, fill="#fffdf4", sw=4, r=2)
            + line(-110, -60, 110, -60, w=2.5, c="#9aa0a6")
            + "")
