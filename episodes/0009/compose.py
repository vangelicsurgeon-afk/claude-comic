import sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT)); sys.path.insert(0, str(ROOT / "tools"))
from comic import Strip
from art.characters import margo, pip
from art import props
from art.palette import *

s = Strip(width=1000, height=860, cols=2, rows=2, margin=20, gutter=16, title="0009 Filed")
P = s.panels
W, H = P[0].rect.w, P[0].rect.h
FY = H * 0.78


def stage(p):
    p.add(props.office_bg(W, H, FY, night=True))


# 1  the empty spot
p = P[0]; stage(p)
p.add(margo.draw("stand", "deadpan", "left"), x=W - 120, y=FY + 25, scale=0.85)
p.add(props.desk(250), x=W - 140, y=FY - 70)
p.add(f'<ellipse cx="{W-190}" cy="{FY-72}" rx="22" ry="5" fill="{RUST}" opacity="0.35"/>')
p.add(props.mug(False), x=W - 90, y=FY - 74)
p.add(pip.draw("hold", "neutral", "right"), x=110, y=FY + 40, scale=1.1)
p.add(props.folder(MUSTARD), x=160, y=FY - 20, scale=0.8, rotate=-10)
p.balloon("The stamp is not here.", 130, 25, tail=(W - 150, 150), max_width=200)
p.balloon("Where is it?", 20, 120, tail=(100, 200), max_width=110)

# 2  rummaging
p = P[1]; stage(p)
p.add(margo.draw("arms_up", "worried", "left"), x=W - 150, y=FY - 10, scale=0.85)
p.add(props.desk(260), x=W - 150, y=FY - 70)
p.add(f'<rect x="{W-250}" y="{FY-70+30}" width="90" height="50" fill="#3a2f2a" stroke="{INK}" stroke-width="3"/>')
p.add(props.paper_stack(3), x=W - 215, y=FY - 70)
for (x, y, r) in [(W - 300, 150, -25), (W - 90, 90, 20), (W - 230, 70, 40)]:
    p.add(props.form(), x=x, y=y, rotate=r)
p.add(pip.draw("stand", "worried", "right"), x=110, y=FY + 40, scale=1.0)
p.balloon("Nobody panic.", W - 215, 18, tail=(W - 160, 100), max_width=150)
p.balloon("Without it, nothing is approved. Somewhere, a bus is not waiting.", 14, 70, tail=(100, 190), max_width=250)

# 3  FWUMP
p = P[2]; stage(p)
p.add(props.tube_station(), x=70, y=FY - 90)
p.add(props.note(), x=70, y=FY - 90 - 18, rotate=8)
p.add(margo.draw("arms_up", "surprised", "left"), x=W - 110, y=FY - 10, scale=0.85)
p.add(props.desk(190), x=W - 110, y=FY - 70)
p.add(pip.draw("stand", "flustered", "right"), x=210, y=FY + 40, scale=0.95)
p.sfx("FWUMP", 20, 70, size=44)
p.balloon("Do not read it.", 190, 130, tail=(W - 140, 205), max_width=140)

# 4  filed
p = P[3]
p.add(f'<rect x="0" y="0" width="{W}" height="{H}" fill="{WALL}"/>')
p.add(f'<rect x="0" y="{H*0.85}" width="{W}" height="{H*0.15}" fill="{FLOOR}"/>')
mx, my, ms = W * 0.62, H * 1.45, 1.9
p.add(margo.draw("stand", "deadpan", "left"), x=mx, y=my, scale=ms)
# stamp stuck in the bun (bun centre is head(0,-196) + (-14,-40), mirrored by facing left)
bx, by = mx + 14 * ms, my + (-196 - 40) * ms
p.add(props.stamp(), x=bx + 6, y=by - 10, scale=1.5, rotate=25)
p.add(pip.draw("point", "surprised", "right"), x=90, y=H * 1.02, scale=1.3)
p.balloon("It's in your hair.", 14, 14, tail=(100, 200), max_width=190)
p.balloon("It's filed.", 225, 20, tail=(mx - 40, 190), max_width=120)

s.save(pathlib.Path(__file__).parent / "comic.svg")
