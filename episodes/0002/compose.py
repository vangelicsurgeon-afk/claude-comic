import sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT)); sys.path.insert(0, str(ROOT / "tools"))
from comic import Strip
from art.characters import margo, pip
from art import props
from art.palette import *

s = Strip(width=1000, height=860, cols=2, rows=2, margin=20, gutter=16, title="0002 Fwump")
P = s.panels
W, H = P[0].rect.w, P[0].rect.h
FY = H * 0.78


def stage(p, window=None):
    p.add(props.office_bg(W, H, FY, window_at=window, night=True))


# 1  wide: tube on the right, Pip hiding left
p = P[0]; stage(p)
p.add(props.tube_station(), x=W - 60, y=FY - 10, scale=1.3)
p.add(props.desk(150), x=60, y=FY - 70)
p.add(pip.draw("stand", "worried", "right"), x=140, y=FY + 30, scale=0.95)
p.add(margo.draw("point", "deadpan", "right"), x=300, y=FY + 30, scale=0.85)
p.balloon("Cases arrive by tube. Someone takes them out.", 20, 16, tail=(285, 120), max_width=240)
p.balloon("Someone.", 140, 120, tail=(140, 210), max_width=110)

# 2  close-up Pip
p = P[1]; stage(p)
p.add(pip.draw("stand", "worried", "right"), x=190, y=FY + 150, scale=1.9)
p.balloon("What if it's a big one?", 26, 14, tail=(150, 140), max_width=220)
p.balloon("It's a folder.", 300, 40, tail=(W - 20, 110), max_width=150)

# 3  fwump
p = P[2]; stage(p)
p.add(props.tube_station(), x=170, y=FY - 10, scale=1.7)
p.add(pip.draw("arms_up", "flustered", "left"), x=310, y=FY - 30, scale=1.0)
p.add(margo.draw("stand", "surprised", "left"), x=W - 40, y=FY + 30, scale=0.85)
p.add(props.folder(MUSTARD), x=170, y=FY - 150, scale=1.1)
p.sfx("FWUMP", 40, 60, size=52, rotate=-8)

# 4  button
p = P[3]; stage(p, window=(W - 150, 40))
p.add(props.desk(130), x=W - 70, y=FY - 70)
p.add(line(-20, 0, 20, -6, w=6, c="#c8553d") , x=W - 90, y=FY - 74)
p.add(pip.draw("hold", "happy", "right"), x=120, y=FY + 30, scale=1.2)
p.add(props.folder(MUSTARD), x=165, y=FY - 15, scale=1.3)
p.add(margo.draw("stand", "deadpan", "left"), x=290, y=FY + 30, scale=0.85)
p.balloon("You jumped.", 10, 14, tail=(120, 120), max_width=150)
p.balloon("I was reaching for a pen.", 220, 20, tail=(285, 105), max_width=220)

s.save(pathlib.Path(__file__).parent / "comic.svg")
