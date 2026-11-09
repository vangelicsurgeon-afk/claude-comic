import sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT)); sys.path.insert(0, str(ROOT / "tools"))
from comic import Strip
from art.characters import margo, pip
from art import props
from art.palette import *

s = Strip(width=1000, height=860, cols=2, rows=2, margin=20, gutter=16, title="0010 Two Minutes")
P = s.panels
W, H = P[0].rect.w, P[0].rect.h
FY = H * 0.78

# 1  office, tugging toward the ROOF door
p = P[0]
p.add(props.office_bg(W, H, FY, night=True))
p.add(props.roof_door(), x=70, y=FY)
p.add(margo.draw("hold", "deadpan", "left"), x=W - 140, y=FY + 25, scale=0.9)
p.add(pip.draw("point", "happy", "left"), x=200, y=FY + 40, scale=1.1)
p.balloon("Come up. Just for a minute.", 80, 14, tail=(190, 190), max_width=190)
p.balloon("It's night.", W - 190, 10, tail=(W - 150, 120), max_width=110)

# 2  roof, Margo steps out
p = P[1]
p.add(props.roof_bg(W, H))
p.add(props.water_tank(), x=W - 90, y=H * 0.72)
p.add(props.roof_door(), x=90, y=H * 0.72 + 6, scale=1.2)
p.add(pip.draw("wave", "happy", "left"), x=W * 0.58, y=H * 0.9, scale=1.1)
p.add(margo.draw("stand", "worried", "right"), x=215, y=H * 0.95, scale=0.8)
p.balloon("Not up here.", W * 0.45, 20, tail=(W * 0.56, 190), max_width=140)

# 3  silent sunrise
p = P[2]
p.add(props.roof_bg(W, H, roof_y=H * 0.8, sun_x=W * 0.8))
p.add(margo.draw("stand", "neutral", "right"), x=W * 0.3, y=H * 1.02, scale=0.85)
p.add(pip.draw("stand", "happy", "right"), x=W * 0.48, y=H * 1.0, scale=1.0)

# 4  close-up
p = P[3]
p.add(f'<rect x="0" y="0" width="{W}" height="{H}" fill="#fbc48f"/>')
p.add(f'<circle cx="{W*0.8}" cy="{H*0.35}" r="{W*0.17}" fill="{FLAME_CORE}" stroke="{INK}" stroke-width="4"/>')
p.add(f'<rect x="0" y="{H*0.9}" width="{W}" height="{H*0.1}" fill="#c9c3cf" stroke="{INK}" stroke-width="4"/>')
mx, my = W * 0.58, H * 1.5
p.add(margo.draw("stand", "happy", "right"), x=mx, y=my, scale=1.8)
p.add(pip.draw("stand", "happy", "right"), x=W * 0.2, y=H * 1.02, scale=1.3)
p.balloon("Two minutes.", 20, 14, tail=(mx - 100, 150), max_width=140)
p.balloon("One fifty-nine.", 20, 160, tail=(W * 0.2 + 20, 250), max_width=170)

s.save(pathlib.Path(__file__).parent / "comic.svg")
