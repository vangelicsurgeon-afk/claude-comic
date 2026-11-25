import sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT)); sys.path.insert(0, str(ROOT / "tools"))
from comic import Strip
from art.characters import margo, pip, fen
from art import props
from art.palette import *

s = Strip(width=1000, height=860, cols=2, rows=2, margin=20, gutter=16, title="0017 Light Mist")
P = s.panels
W, H = P[0].rect.w, P[0].rect.h
FY = H * 0.78
DT = FY - 70  # desk top
F = s.font_family


def stage(p, window_at=None):
    p.add(props.office_bg(W, H, FY, window_at=window_at, night=True))


def fen_puddle(p, x, k=0.8):
    p.add(props.puddle(0), x=x, y=FY + 4, scale=k)


# 1  Quick ask.
p = P[0]; stage(p, window_at=(22, 40))
mx = 100
p.add(margo.draw("write", "deadpan", "right", look="side", pearl=True), x=mx, y=FY + 25, scale=0.8)
p.add(props.desk(170), x=mx + 6, y=DT)
p.add(props.mug(True), x=mx - 46, y=DT)
p.add(props.paper_stack(2), x=mx + 40, y=DT)
fx = 262
fen_puddle(p, fx, 0.9)
p.add(fen.draw("hold", "polite", "left", look="side", drizzle=1), x=fx, y=FY, scale=0.85)
px = 418
p.add(pip.draw("arms_up", "happy", "left", look="up"), x=px, y=FY - 50, scale=0.78)
p.add(props.desk(110), x=px, y=DT)
p.balloon("Hi. Fen, Medium. Quick ask. Super small.", 120, 8, tail=(fx - 6, FY - 128), max_width=200)
p.balloon("You're raining.", W - 136, 12, tail=(px - 4, FY - 140), max_width=120)
p.balloon("Light mist.", 268, 132, tail=(fx - 14, FY - 126), max_width=110)

# 2  close on Fen
p = P[1]; stage(p)
fx, k = 186, 1.45
p.add(fen.draw("tie", "flustered", "right", look="side", drizzle=2), x=fx, y=FY + 50, scale=k)
px = 420
p.add(pip.draw("stand", "flustered", "left", look="up"), x=px, y=FY + 40, scale=0.95)
p.balloon("I'm auditing the stairwell door. The one that shuts behind you.", 12, 8, tail=(fx - 20, FY + 50 - 145 * k), max_width=240)
p.balloon("You're locked out.", W - 136, 24, tail=(px - 2, FY - 80), max_width=120)
p.balloon("Locked in. To the outside.", 262, 150, tail=(fx + 92, FY + 50 - 118 * k), max_width=125)

# 3  KA-CHUNK (reverse angle: Pip's desk on the left, Margo's on the right)
p = P[2]; stage(p)
px = 96
DT3 = FY - 70
p.add(pip.draw("point", "proud", "right", look="down"), x=px - 2, y=DT3 + 11, scale=1.0)
p.add(props.desk(150), x=px + 5, y=DT3)
p.add(props.request_slip(), x=px + 62, y=DT3, scale=0.9)
p.add(props.stamp(), x=px + 60, y=DT3 - 26, scale=1.6)
p.add(circle(px + 59.6, DT3 - 62, 6.2, fill=LAVENDER, w=3.3))
p.add(path(f"M{px+24},{DT3-30} l-14,-6 M{px+96},{DT3-30} l14,-6", w=3))
p.sfx("KA-CHUNK", 176, 376, size=28, rotate=-8)
fx = 250
p.add(fen.draw("tie", "polite", "left", look="side", drizzle=1), x=fx, y=FY - 6, scale=0.72)
fen_puddle(p, fx, 0.7)
mx = W - 92
p.add(margo.draw("write", "deadpan", "left", look="down", pearl=True), x=mx, y=FY + 10, scale=0.85)
p.add(props.desk(160), x=mx - 6, y=DT)
p.add(props.scribble(dry=False), x=mx - 10, y=DT - 6, scale=0.7)
p.balloon("Requester?", 16, 10, tail=(px + 10, DT3 - 110), max_width=120)
p.balloon("Anonymous.", 150, 50, tail=(fx - 6, FY - 112), max_width=120)
p.balloon("Good choice.", W - 140, 40, tail=(mx - 6, FY + 10 - 235 * 0.85), max_width=120)

# 4  the landing
p = P[3]
xt = 96
p.add(props.stairwell_bg(W, H, xt, FY))
dx = 372
p.add(props.door_5(font=F, ajar=True), x=dx, y=FY)
fx = dx - 74
p.add(fen.draw("stand", "polite", "left", look="side", drizzle=0), x=fx, y=FY, scale=0.78)
sx, sy = props.stair_step(1, xt, FY)
p.add(pip.draw("wave", "happy", "right", look="up"), x=sx + 6, y=sy, scale=0.85)
p.balloon("Great outcome. Let's circle back.", 120, 10, tail=(fx - 20, FY - 116), max_width=200)
p.balloon("...What luck.", 330, 92, tail=(fx + 26, FY - 112), max_width=100, size=16)

s.save(pathlib.Path(__file__).parent / "comic.svg")
