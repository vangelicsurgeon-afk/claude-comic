import sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT)); sys.path.insert(0, str(ROOT / "tools"))
from comic import Strip
from art.characters import margo, pip
from art import props
from art.palette import *

s = Strip(width=1000, height=860, cols=2, rows=2, margin=20, gutter=16, title="0012 Not Slower")
P = s.panels
W, H = P[0].rect.w, P[0].rect.h
FY = H * 0.78


def stage(p, window_at=None):
    p.add(props.office_bg(W, H, FY, window_at=window_at, night=True))


def open_drawer(p, dx, w):
    p.add(f'<rect x="{dx - w/2 + 30}" y="{FY-70+30}" width="90" height="56" fill="#3a2f2a" stroke="{INK}" stroke-width="3"/>')


# 1  the note still in the tube
p = P[0]; stage(p)
p.add(props.tube_station(), x=80, y=FY - 40)
p.add(props.note(), x=80, y=FY - 40 - 40)
p.add(margo.draw("stand", "neutral", "left", look="side", pearl=True), x=W - 105, y=FY + 25, scale=0.85)
p.add(props.desk(210), x=W - 115, y=FY - 70)
p.add(props.mug(True), x=W - 60, y=FY - 74)
p.add(pip.draw("stand", "worried", "left", look="side"), x=205, y=FY + 40, scale=1.0)
p.balloon("Your note from last week is still in the tube.", 14, 14, tail=(195, 215), max_width=220)
p.balloon("Read it.", W - 150, 60, tail=(W - 115, 140), max_width=110)

# 2  "Review what?"  "You."
p = P[1]; stage(p)
dx = W - 140
p.add(margo.draw("hold", "deadpan", "left", look="down", pearl=True), x=W - 120, y=FY + 25, scale=0.85)
p.add(props.desk(250), x=dx, y=FY - 70)
open_drawer(p, dx, 250)
p.add(props.form(), x=W - 175, y=FY - 70, rotate=-6)
p.add(props.mug(False), x=W - 50, y=FY - 74)
p.add(pip.draw("hold", "flustered", "right", look="side"), x=120, y=FY + 40, scale=1.05)
p.add(props.note(big=False), x=124, y=FY + 32, scale=1.3, rotate=-8)
p.balloon("“Please review. -H.” Review what?", 14, 14, tail=(120, 200), max_width=210)
p.balloon("You.", W - 150, 70, tail=(W - 130, 140), max_width=90)

# 3  insert: the one line
p = P[2]
p.add(f'<rect x="0" y="0" width="{W}" height="{H}" fill="{WOOD}"/>')
for y in (70, 160, 250, 340):
    p.add(line(0, y, W, y + 6, w=2, c="#86592f"))
fs = 1.12
fx, fy = (W - 380 * fs) / 2 - 16, (H - 250 * fs) / 2 + 6
p.add(f'<g transform="translate({fx:.1f},{fy:.1f}) rotate(-3) scale({fs})">'
      f'{props.review_form("Good. Now do it again.", "PIP", s.font_family)}</g>')
p.add(props.pen(), x=fx + 335 * fs, y=fy + 148 * fs, scale=1.2)

# 4  "No 'slower'?"  "Not anymore."
p = P[3]; stage(p, window_at=(W - 140, 70))
mx = W - 215
p.add(margo.draw("stand", "deadpan", "right", look="side", pearl=True), x=mx, y=FY + 25, scale=0.85)
p.add(props.desk(220), x=mx + 10, y=FY - 70)
p.add(props.mug(True), x=mx + 60, y=FY - 74)
p.add(pip.draw("hold", "proud", "right", look="up"), x=95, y=FY + 40, scale=1.1)
p.add(f'<g transform="translate({95 - 40},{FY - 12}) rotate(-6) scale(0.21)">'
      f'{props.review_form("Good. Now do it again.", "PIP", s.font_family)}</g>')
p.balloon("No “slower”?", 14, 40, tail=(95, 170), max_width=150)
p.balloon("Not anymore.", 190, 10, tail=(mx - 10, 125), max_width=140)

s.save(pathlib.Path(__file__).parent / "comic.svg")
