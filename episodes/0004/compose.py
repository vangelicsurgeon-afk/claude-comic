import sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT)); sys.path.insert(0, str(ROOT / "tools"))
from comic import Strip
from art.characters import margo, pip
from art import props
from art.palette import *

s = Strip(width=1000, height=860, cols=2, rows=2, margin=20, gutter=16, title="0004 A Good View")
P = s.panels
W, H = P[0].rect.w, P[0].rect.h
FY = H * 0.78


def stage(p):
    p.add(props.office_bg(W, H, FY, night=True))


def big_window(p, x, y, sc):
    p.add(f'<g transform="translate({x},{y}) scale({sc})">{props.window(night=True)}</g>')


# 1  Pip at the window
p = P[0]; stage(p)
big_window(p, 120, 70, 1.6)
p.add(margo.draw("stand", "deadpan", "left"), x=W - 80, y=FY - 10, scale=0.8)
p.add(props.desk(150), x=W - 80, y=FY - 70)
p.add(pip.draw("stand", "neutral", "right"), x=215, y=FY + 40, scale=0.95)
p.caption("2:15 PM", "top-left")
p.balloon("It's two in the afternoon.", 270, 14, tail=(235, 215), max_width=190)

# 2  Margo deadpan, Pip at the desk
p = P[1]; stage(p)
p.add(margo.draw("stand", "deadpan", "left"), x=W - 140, y=FY - 10, scale=0.85)
p.add(props.desk(300), x=W - 170, y=FY - 70)
p.add(props.folder(MUSTARD), x=W - 250, y=FY - 70)
p.add(pip.draw("stand", "worried", "right"), x=90, y=FY + 40, scale=0.95)
p.balloon("Why is it still night?", 40, 40, tail=(100, 190), max_width=200)
p.balloon("Is it.", 250, 30, tail=(W - 200, 130), max_width=100)

# 3  close-up Margo
p = P[2]; stage(p)
p.add(margo.draw("hold", "neutral", "left"), x=W / 2 + 10, y=FY + 285, scale=1.6)
p.balloon("It's a good view.", 20, 14, tail=(W / 2 - 60, 200), max_width=220)

# 4  both at the window
p = P[3]; stage(p)
big_window(p, 40, 90, 1.6)
p.add(margo.draw("stand", "neutral", "left"), x=W - 110, y=FY - 10, scale=0.85)
p.add(props.desk(190), x=W - 110, y=FY - 70)
p.add(props.mug(True), x=W - 170, y=FY - 70)
p.add(pip.draw("stand", "happy", "right"), x=140, y=FY + 40, scale=0.9)
p.balloon("It is.", 30, 14, tail=(120, 195), max_width=90)
p.balloon("Stamp the folder.", 250, 14, tail=(W - 130, 92), max_width=200)

s.save(pathlib.Path(__file__).parent / "comic.svg")
