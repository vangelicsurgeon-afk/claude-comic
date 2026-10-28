import sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT)); sys.path.insert(0, str(ROOT / "tools"))
from comic import Strip
from art.characters import margo, pip
from art import props
from art.palette import *

s = Strip(width=1000, height=860, cols=2, rows=2, margin=20, gutter=16, title="0005 Please Handle")
P = s.panels
W, H = P[0].rect.w, P[0].rect.h
FY = H * 0.78


def stage(p):
    p.add(props.office_bg(W, H, FY, night=True))


# 1  FWUMP: note sticks out of the tube, Margo flinches
p = P[0]; stage(p)
p.add(props.tube_station(), x=70, y=FY - 90)
p.add(props.note(), x=70, y=FY - 90 - 18, rotate=8)
p.add(margo.draw("arms_up", "surprised", "left"), x=W - 110, y=FY - 10, scale=0.85)
p.add(props.desk(190), x=W - 110, y=FY - 70)
p.add(props.mug(False), x=W - 180, y=FY - 120)
p.add(pip.draw("stand", "flustered", "right"), x=190, y=FY + 40, scale=0.9)
p.sfx("FWUMP", 110, 90, size=46)

# 2  close-up of the note
p = P[1]
p.add(f'<rect x="0" y="0" width="{W}" height="{H}" fill="{WALL_DARK}"/>')
p.add(props.note(big=True), x=W / 2, y=H / 2 + 100, rotate=-3)
fam = s.font_family
p.add(f'<text x="-95" y="-95" font-family="{fam}" font-size="38" font-weight="700" fill="{INK}">Please handle.</text>',
      x=W / 2, y=H / 2 + 100, rotate=-3)
p.add(f'<text x="35" y="-25" font-family="{fam}" font-size="34" fill="{INK}">-H.</text>',
      x=W / 2, y=H / 2 + 100, rotate=-3)

# 3  side by side (Pip left, Margo right)
p = P[2]; stage(p)
p.add(margo.draw("stand", "deadpan", "left"), x=W / 2 + 90, y=FY - 10, scale=0.85)
p.add(props.desk(300), x=W / 2 + 40, y=FY - 70)
p.add(props.note(), x=W / 2 - 20, y=FY - 70)
p.add(pip.draw("stand", "worried", "right"), x=90, y=FY + 40, scale=0.95)
p.balloon("Handle what?", 30, 30, tail=(92, 232), max_width=160)
p.balloon("He doesn't say.", 240, 30, tail=(W / 2 + 90, 100), max_width=200)

# 4  stamp and file
p = P[3]; stage(p)
p.add(margo.draw("stand", "neutral", "right"), x=W / 2 - 80, y=FY - 10, scale=0.85)
p.add(props.desk(300), x=W / 2 - 20, y=FY - 70)
# open drawer: dark opening with a tall stack of identical notes
p.add(f'<rect x="{W/2-20-150+30}" y="{FY-70+30}" width="90" height="56" fill="#3a2f2a" stroke="{INK}" stroke-width="3"/>')
for i in range(7):
    p.add(props.note(), x=W / 2 - 20 - 150 + 75 + (i % 2) * 6, y=FY - 70 + 84 - i * 6)
p.add(props.note(), x=W / 2 + 40, y=FY - 70)
p.add(props.stamp(), x=W / 2 + 60, y=FY - 80)
p.add(pip.draw("stand", "worried", "left"), x=W / 2 + 160, y=FY + 40, scale=0.9)
p.balloon("It's handled.", 40, 20, tail=(W / 2 - 80, 100), max_width=170)
p.sfx("CHUNK", W - 150, 80, size=40)

s.save(pathlib.Path(__file__).parent / "comic.svg")
