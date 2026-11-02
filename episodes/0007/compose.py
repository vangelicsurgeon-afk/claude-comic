import sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT)); sys.path.insert(0, str(ROOT / "tools"))
from comic import Strip
from art.characters import margo, pip
from art import props
from art.palette import *

s = Strip(width=1000, height=860, cols=2, rows=2, margin=20, gutter=16, title="0007 Form 9")
P = s.panels
W, H = P[0].rect.w, P[0].rect.h
FY = H * 0.78
fam = s.font_family


def stage(p):
    p.add(props.office_bg(W, H, FY, night=True))


# 1  the folder comes back
p = P[0]; stage(p)
p.add(props.tube_station(), x=70, y=FY - 120)
p.add(margo.draw("stand", "deadpan", "left"), x=W - 100, y=FY - 10, scale=0.85)
p.add(props.desk(240), x=W - 120, y=FY - 70)
p.add(pip.draw("hold", "worried", "right"), x=170, y=FY + 40, scale=1.2)
p.balloon("It came back.", 100, 40, tail=(165, 175), max_width=170)

# 2  flame out
p = P[1]
p.add(f'<rect x="0" y="0" width="{W}" height="{H}" fill="{WALL}"/>')
p.add(f'<rect x="0" y="{H*0.8}" width="{W}" height="{H*0.2}" fill="{FLOOR}"/>')
p.add(pip.draw("slump", "sad", "right"), x=W / 2, y=H * 0.9, scale=1.7)
p.add(props.folder(LAVENDER), x=W / 2 + 170, y=H * 0.9, scale=1.1, rotate=-8)

p.caption("Case 4790. Returned: \"Exceeds Small.\"", "top-left", max_width=280)

# 3  Form 9
p = P[2]
p.add(f'<rect x="0" y="0" width="{W}" height="{H}" fill="{WOOD}"/>')
p.add(f'<rect x="{W/2-190}" y="40" width="380" height="330" fill="#fffdf4" stroke="{INK}" stroke-width="4"/>')
lines = [("FORM 9", 34, 700, 95), ("REQUEST FOR RECESS", 22, 700, 130),
         ("Employee: Pip", 22, 400, 190), ("Duration: as long as needed", 22, 400, 235),
         ("Approved: M. Voss", 26, 700, 310)]
for t, sz, wt, y in lines:
    p.add(f'<text x="{W/2-165}" y="{y}" font-family="{fam}" font-size="{sz}" font-weight="{wt}" fill="{INK}">{t}</text>')
p.add(f'<line x1="{W/2-165}" y1="322" x2="{W/2+60}" y2="322" stroke="#9aa0a6" stroke-width="2.5"/>')
p.add(f'<line x1="{W/2-165}" y1="248" x2="{W/2+150}" y2="248" stroke="#9aa0a6" stroke-width="2.5"/>')
# pen
p.add(f'<g transform="rotate(-35 {W/2+110} 300)"><rect x="{W/2+100}" y="270" width="14" height="110" rx="4" fill="{RUST}" stroke="{INK}" stroke-width="3.5"/>'
      f'<polygon points="{W/2+100},270 {W/2+114},270 {W/2+107},248" fill="{INK}"/></g>')
p.sfx("scratch scratch", W / 2 - 60, H - 25, size=30, rotate=-3)

# 4  mug and form
p = P[3]; stage(p)
p.add(props.desk(260), x=W - 120, y=FY - 70)
p.add(margo.draw("hold", "deadpan", "left"), x=W / 2 + 90, y=FY + 40, scale=0.95)
p.add(pip.draw("stand", "neutral", "right"), x=110, y=FY + 40, scale=1.0)
p.add(props.mug(True), x=190, y=FY + 40)
p.balloon("Is it in triplicate?", 20, 30, tail=(110, 150), max_width=190)
p.balloon("Obviously. Pink copy's mine.", 230, 20, tail=(W / 2 + 80, 100), max_width=210)

s.save(pathlib.Path(__file__).parent / "comic.svg")
