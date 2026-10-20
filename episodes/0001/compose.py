import sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT)); sys.path.insert(0, str(ROOT / "tools"))
from comic import Strip
from art.characters import margo, pip
from art import props
from art.palette import *

s = Strip(width=1000, height=860, cols=2, rows=2, margin=20, gutter=16, title="0001 The Paperwork Is the Miracle")
P = s.panels
W, H = P[0].rect.w, P[0].rect.h
FY = H * 0.78


def stage(p, window=True):
    p.add(props.office_bg(W, H, FY, window_at=(W - 150, 40) if window else None, night=True))


# 1
p = P[0]; stage(p)
p.add(props.desk(190), x=W - 100, y=FY - 70)
p.add(props.stamp(), x=W - 70, y=FY - 70)
p.add(margo.draw("hold", "deadpan", "right"), x=130, y=FY + 30, scale=0.85)
p.add(pip.draw("stand", "happy", "left"), x=300, y=FY + 30)
p.caption("Pip's first day.", corner="bottom-left")
p.balloon("Rule one. The paperwork is the miracle.", 30, 18, tail=(135, 110), max_width=250)

# 2
p = P[1]; stage(p, window=False)
p.add(margo.draw("point", "deadpan", "left"), x=350, y=FY + 40, scale=0.95)
p.add(pip.draw("hold", "worried", "right"), x=110, y=FY + 40, scale=1.2)
p.balloon("I thought the miracle was the part where somebody gets lucky.", 10, 12, tail=(100, 150), max_width=240)
p.balloon("That's the side effect.", 285, 20, tail=(340, 150), max_width=170)

# 3
p = P[2]; stage(p)
p.add(pip.draw("arms_up", "proud", "right"), x=190, y=FY + 20, scale=1.3)
p.add(props.desk(300), x=190, y=FY - 56)
p.add(props.paper_stack(3), x=100, y=FY - 56)
p.add(props.stamp(), x=265, y=FY - 56)
p.add(margo.draw("stand", "surprised", "left"), x=410, y=FY + 30, scale=0.85)
p.balloon("Signed. Dated. Triplicate.", 20, 14, tail=(190, 100), max_width=230)
p.sfx("KA-CHUNK", 232, 222, size=30, rotate=-10)

# 4
p = P[3]; p.add(props.office_bg(W, H, FY, window_at=(185, 150), night=True))
p.add('<rect x="14" y="165" width="60" height="38" fill="#f2d98a" stroke="#2a2433" stroke-width="3"/>'
      '<rect x="30" y="150" width="28" height="16" fill="#f2d98a" stroke="#2a2433" stroke-width="3"/>', x=W - 160, y=-40, scale=0.0001)
p.add(pip.draw("stand", "surprised", "right"), x=130, y=FY + 30, scale=1.1)
p.add(margo.draw("stand", "smug", "left"), x=370, y=FY + 30, scale=0.85)
p.balloon("Did it work?", 20, 20, tail=(130, 130), max_width=170)
p.balloon("Someone just found a parking space. Good. Now do it again, slower.", 190, 14, tail=(362, 160), max_width=270)

s.save(pathlib.Path(__file__).parent / "comic.svg")
