import sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT)); sys.path.insert(0, str(ROOT / "tools"))
from comic import Strip
from art.characters import margo, pip
from art import props
from art.palette import *

s = Strip(width=1000, height=860, cols=2, rows=2, margin=20, gutter=16, title="0003 Triplicate")
P = s.panels
W, H = P[0].rect.w, P[0].rect.h
FY = H * 0.78


def stage(p, window=None):
    p.add(props.office_bg(W, H, FY, window_at=window, night=True))


# 1  Margo at desk, Pip in front, earring on the desk
p = P[0]; stage(p)
p.add(margo.draw("stand", "deadpan", "right"), x=170, y=FY - 10, scale=0.85)
p.add(props.desk(260), x=170, y=FY - 70)
p.add(props.folder(MUSTARD), x=100, y=FY - 70, scale=1.0)
p.add(props.earring(), x=235, y=FY - 70, scale=1.6)
p.add(pip.draw("stand", "happy", "left"), x=400, y=FY + 40, scale=0.95)
p.balloon("Case 4471. One earring, silver. Last seen Tuesday.", 10, 12, tail=(170, 125), max_width=220)
p.balloon("It's in her coat. We could just put it there.", 250, 100, tail=(400, 195), max_width=210)

# 2  close-up Margo, Pip's three forms
p = P[1]; stage(p)
p.add(margo.draw("hold", "deadpan", "right"), x=190, y=FY + 285, scale=1.6)
for i, c in enumerate(("#ffffff", "#fff2a8", "#ffd6dc")):
    p.add(props.form(c), x=W - 110 + i * 24, y=FY - 10 - i * 6, scale=1.5)
p.balloon("We could. Is the form done?", 20, 10, tail=(190, 215), max_width=250)
p.balloon("Signed. Dated. Triplicate.", 270, 110, tail=(W - 10, 240), max_width=190)

# 3  Pip stamps
p = P[2]; stage(p)
p.add(props.desk(340), x=W / 2, y=FY - 70)
p.add(props.paper_stack(3), x=W / 2 + 110, y=FY - 70)
p.add(props.form("#ffffff"), x=W / 2 - 100, y=FY - 70, scale=1.0)
p.add(props.stamp(), x=W / 2 - 100, y=FY - 70 - 30, scale=1.0)
p.add(pip.draw("stand", "neutral", "right"), x=W / 2 + 10, y=FY - 20, scale=1.2)
p.balloon("Who keeps the third one?", 20, 14, tail=(W / 2 - 10, 170), max_width=230)
p.sfx("CHUNK", 300, 200, size=40, rotate=-6)

# 4  drawer
p = P[3]; stage(p)
p.add(props.desk(300), x=W - 170, y=FY - 70)
p.add(props.tin(), x=W - 110, y=FY - 70, scale=1.2)
p.add(props.form("#ffd6dc"), x=W - 220, y=FY - 70, scale=0.9)
p.add(pip.draw("stand", "neutral", "right"), x=70, y=FY + 40, scale=0.95)
p.add(margo.draw("stand", "deadpan", "left"), x=W - 170, y=FY - 10, scale=0.85)
p.balloon("Someone who might come looking.", 100, 14, tail=(W - 170, 95), max_width=240)

s.save(pathlib.Path(__file__).parent / "comic.svg")
