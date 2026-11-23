import sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT)); sys.path.insert(0, str(ROOT / "tools"))
from comic import Strip
from art.characters import margo, pip
from art import props
from art.palette import *

s = Strip(width=1000, height=860, cols=2, rows=2, margin=20, gutter=16, title="0016 Intent to Knock")
P = s.panels
W, H = P[0].rect.w, P[0].rect.h
FY = H * 0.78
F = s.font_family


def m_stack(p, x, y, k, facing):
    """forms tucked under Margo's back arm (hand at (-34,-94) when facing right)."""
    sx = -34 if facing == "right" else 34
    p.add(props.paper_stack(4), x=x + sx * k, y=y - 82 * k, scale=k * 0.9)


# 1  One flight.
p = P[0]
xt, yt = 262, 232
p.add(props.stairwell_bg(W, H, xt, yt))
p.add(props.door_5(font=F), x=400, y=yt)
px = 360
p.add(pip.draw("point", "happy", "left", look="side"), x=px, y=yt, scale=0.82)
mx, my = props.stair_step(4, xt, yt)
mx += 6
k = 0.72
p.add(margo.draw("stand", "deadpan", "right", look="up", pearl=True), x=mx, y=my, scale=k)
m_stack(p, mx, my, k, "right")
p.add(props.note(), x=mx + 34 * k, y=my - 82 * k, scale=0.9)
p.balloon("One flight. Only to show you there's nothing to see.", 22, 10, tail=(mx + 14, my - 228 * k), max_width=230)
p.balloon("There's a door.", 300, 30, tail=(px - 6, yt - 112), max_width=150)

# 2  Nobody knocks.
p = P[1]
xt = 96
p.add(props.stairwell_bg(W, H, xt, FY))
dx = 372
p.add(props.door_5(font=F), x=dx, y=FY)
px = 352
p.add(pip.draw("wave", "happy", "right", look="side"), x=px, y=FY, scale=0.95)
mx, k = 140, 0.85
p.add(margo.draw("offer", "deadpan", "right", look="side", pearl=True), x=mx, y=FY, scale=k)
m_stack(p, mx, FY, k, "right")
p.balloon("Nobody knocks. Form 12. Notice of Intent to Knock.", 24, 10, tail=(mx + 6, FY - 238 * k), max_width=250)

# 3  close-up, the fan
p = P[2]
p.add(f'<rect x="0" y="0" width="{W}" height="{H}" fill="{props.STAIR_WALL}"/>'
      f'<rect x="0" y="{H-70}" width="{W}" height="70" fill="{props.STAIR_DADO}"/>'
      + line(0, H - 70, W, H - 70, w=3, c="#6f8a80"))
mx, my, k = 150, 556, 1.6
p.add(margo.draw("offer", "deadpan", "right", look="front", pearl=True), x=mx, y=my, scale=k)
hx, hy = mx + 88 * k, my - 122 * k
p.add(props.form_fan(["12", "12-B", "12-C", "12-D"], font=F, spread=26), x=hx + 6, y=hy + 8, scale=1.3, rotate=14)
p.balloon("12-B, the knock. 12-C, being let in. 12-D, being let out again.", 22, 10,
          tail=(mx + 40, my - 196 * k - 62), max_width=250)

# 4  raining under the door
p = P[3]
xt = 96
p.add(props.stairwell_bg(W, H, xt, FY))
dx = 404
p.add(props.door_5(font=F), x=dx, y=FY)
p.add(props.puddle(3), x=dx - 6, y=FY + 6, scale=1.1)
px = 196
p.add(pip.draw("point", "worried", "right", look="down"), x=px, y=FY + 2, scale=0.9)
mx, my = props.stair_step(1, xt, FY)
mx += 8
k = 0.85
p.add(margo.draw("stand", "deadpan", "left", look="side", pearl=True), x=mx, y=my, scale=k)
m_stack(p, mx, my, k, "left")
p.balloon("Margo. It's raining under the door.", 214, 8, tail=(px + 20, FY - 118), max_width=210)
p.balloon("Then it's a Medium problem.", 20, 52, tail=(mx - 2, my - 240 * k), max_width=180)

s.save(pathlib.Path(__file__).parent / "comic.svg")
