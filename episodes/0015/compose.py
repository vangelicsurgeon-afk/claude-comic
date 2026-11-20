import sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT)); sys.path.insert(0, str(ROOT / "tools"))
from comic import Strip
from art.characters import margo, pip
from art import props
from art.palette import *

s = Strip(width=1000, height=860, cols=2, rows=2, margin=20, gutter=16, title="0015 Come Up")
P = s.panels
W, H = P[0].rect.w, P[0].rect.h
FY = H * 0.78
DT = FY - 70  # desk top
F = s.font_family


def stage(p, window_at=None):
    p.add(props.office_bg(W, H, FY, window_at=window_at, night=True))


def card(p, x, y, lines, k=1.0, rot=0, handled=False, size=17):
    p.add(f'<g transform="translate({x},{y}) rotate({rot}) scale({k})">{props.note_card(lines, F, handled, size)}</g>')


def flat_card(p, x, y, lines, k=1.0, handled=False):
    """note card lying flat on a desk (top edge at y)."""
    p.add(f'<g transform="translate({x},{y}) skewX(-14) scale({k},{k*0.62})">{props.note_card(lines, F, handled)}</g>')


# 1  FWUMP, the note
p = P[0]; stage(p)
p.add(props.tube_station(), x=48, y=FY - 50)
p.sfx("FWUMP", 20, 120, size=34, rotate=-10)
mx = 330
p.add(margo.draw("write", "surprised", "left", look="down", pearl=True), x=mx, y=FY + 25, scale=0.85)
p.add(props.desk(200), x=mx - 5, y=DT)
p.add(props.mug(True), x=mx + 60, y=DT)
p.add(props.paper_stack(3), x=mx - 40, y=DT)
p.add(props.desk(124), x=W + 20, y=DT)
px = 150
p.add(pip.draw("hold", "worried", "right", look="down"), x=px, y=FY + 40, scale=1.0)
p.add(props.note(), x=px + 2, y=FY + 2, scale=1.3)
p.balloon("“Please come up. -H.” Up where?", 110, 14, tail=(px + 8, FY - 90), max_width=180)
p.balloon("He doesn't say.", W - 150, 70, tail=(mx - 6, 150), max_width=130)

# 2  Up.
p = P[1]; stage(p, window_at=(26, 46))
dx = 290
p.add(props.desk(210), x=dx, y=DT)
p.add(props.mug(False), x=dx + 72, y=DT)
p.add(props.paper_stack(2), x=dx - 70, y=DT)
p.add(margo.draw("stand", "deadpan", "left", look="front", pearl=True), x=dx, y=DT + 2, scale=0.72)
p.add(props.note(), x=dx - 24, y=DT - 56, scale=0.9, rotate=8)
p.add(pip.draw("arms_up", "flustered", "right", look="up"), x=120, y=FY + 40, scale=1.0)
p.balloon("Up.", W - 110, 22, tail=(dx + 20, 92), max_width=70)

# 3  KA-CHUNK
p = P[2]; stage(p)
p.add(props.tube_station(), x=40, y=FY - 50)
mx = W - 70
p.add(margo.draw("offer", "deadpan", "left", look="down", pearl=True), x=mx, y=FY - 12, scale=0.9)
p.add(props.desk(300), x=W - 150, y=DT)
p.add(props.mug(False), x=W - 40, y=DT)
k = 0.9
hx, hy = mx - 88 * k, FY - 12 - 122 * k  # Margo's "offer" hand, facing left
flat_card(p, hx - 162, DT - 40, ["Please come up.", "-H."], k=0.9, handled=True)
p.add(props.stamp(), x=hx, y=hy + 36, scale=1.4)
p.add(circle(hx, hy, 8, fill=SKIN_MARGO, w=3.5))
p.add(path(f"M{hx-28},{hy+44} l-12,6 M{hx+28},{hy+44} l12,6", w=3))
p.sfx("KA-CHUNK", 150, 190, size=28, rotate=-6)
px = 110
p.add(pip.draw("stand", "worried", "right", look="side"), x=px, y=FY + 40, scale=1.0)
p.balloon("I think he meant the fifth floor.", 14, 14, tail=(px + 4, FY - 90), max_width=170)
p.balloon("Then he'd have said “floor.”", W - 228, 36, tail=(mx - 52, 165), max_width=180)

# 4  further
p = P[3]; stage(p)
p.add(props.tube_station(), x=40, y=FY - 50)
p.sfx("FWUMP", 14, 118, size=30, rotate=-10)
mx = W - 62
p.add(margo.draw("stand", "deadpan", "left", look="up", pearl=True), x=mx, y=FY + 25, scale=0.9)
p.add(props.desk(220), x=mx - 10, y=DT)
p.add(props.mug(False), x=mx + 30, y=DT)
px = 140
p.add(pip.draw("wave", "proud", "right", look="side"), x=px, y=FY + 40, scale=1.05)
hx, hy = px + 58 * 1.05, FY + 40 - 96 * 1.05
card(p, hx - 12, hy - 96, ["Please come up", "further.", "-H."], k=0.95, rot=-4, size=19)
p.add(circle(hx, hy, 9, fill=LAVENDER, w=3.3))
p.balloon("He says “further.”", 150, 12, tail=(px - 22, FY - 74), max_width=150)

s.save(pathlib.Path(__file__).parent / "comic.svg")
