import sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT)); sys.path.insert(0, str(ROOT / "tools"))
from comic import Strip
from art.characters import margo, pip
from art import props
from art.palette import *

s = Strip(width=1000, height=860, cols=2, rows=2, margin=20, gutter=16, title="0013 What Luck")
P = s.panels
W, H = P[0].rect.w, P[0].rect.h
FY = H * 0.78


def stage(p, window_at=None):
    p.add(props.office_bg(W, H, FY, window_at=window_at, night=True))


def held_stamp(p, hx, hy, k=1.0):
    """Stamp gripped at the handle by a hand at (hx, hy)."""
    p.add(props.stamp(), x=hx, y=hy + 22 * k, scale=k)
    p.add(circle(hx, hy, 8 * k, fill=SKIN_MARGO, w=3.5))


def pen_on_paper(p, nx, ny, k=1.0):
    """A rust pen standing on its nib at (nx, ny), leaning back toward the writer."""
    p.add(f'<g transform="translate({nx},{ny}) rotate(-30) scale({k})">'
          + path("M0,0 L-4,-10 L4,-10 Z", fill=INK, w=2)
          + rect(-5, -52, 10, 42, fill=RUST, sw=3, r=4) + '</g>')


def paper(p, x, y, w=90):
    p.add(f'<g transform="translate({x},{y}) skewX(-20) scale(1,0.4)">'
          + rect(0, -60, w, 60, fill="#ffffff", sw=3) + '</g>')


# 1  the new desk
p = P[0]; stage(p, window_at=(22, 52))
p.add(margo.draw("point", "deadpan", "right", look="side", pearl=True), x=150, y=FY + 25, scale=0.85)
p.add(props.desk(190), x=150, y=FY - 70)
p.add(props.mug(True), x=90, y=FY - 70)
p.add(props.desk(124), x=322, y=FY - 70)
p.add(pip.draw("arms_up", "surprised", "left", look="side"), x=405, y=FY + 18, scale=0.85)
p.balloon("Your desk. Same distance from the tube as mine.", 150, 12, tail=(150, 118), max_width=200)
p.balloon("It has a drawer!", W - 140, 70, tail=(W - 70, 190), max_width=125)

# 2  the stamp
p = P[1]; stage(p)
p.add(margo.draw("offer", "deadpan", "right", look="side", pearl=True), x=150, y=FY + 70, scale=1.0)
held_stamp(p, 150 + 88, FY + 70 - 122, k=1.2)
p.add(pip.draw("arms_up", "happy", "left", look="up"), x=350, y=FY + 50, scale=1.1)
p.balloon("Your stamp. Don't file it anywhere I would.", 14, 14, tail=(140, 118), max_width=230)

# 3  first solo case
p = P[2]; stage(p)
p.add(props.tube_station(), x=40, y=FY - 50)
mx = 165
p.add(margo.draw("write", "annoyed", "right", look="down", pearl=True), x=mx, y=FY + 25, scale=0.8)
p.add(props.desk(190), x=mx + 5, y=FY - 70)
paper(p, mx + 20, FY - 66, 80)
pen_on_paper(p, mx + 46, FY - 76, k=0.9)
p.add(props.scribble(dry=True), x=mx + 4, y=FY - 82, scale=0.85)
px = 370
p.add(pip.draw("hold", "neutral", "left", look="down"), x=px + 6, y=FY - 66, scale=1.0)
p.add(props.desk(150), x=px, y=FY - 70)
# open folder with the request slip
p.add(rect(px - 58, FY - 82, 50, 12, fill=MUSTARD, sw=3, r=2) + rect(px - 8, FY - 82, 50, 12, fill=MUSTARD, sw=3, r=2))
p.add(props.request_slip(), x=px - 32, y=FY - 74, scale=0.7)
p.add(props.form("#ffd6e0"), x=px + 58, y=FY - 70, scale=0.55)
p.add(props.form("#fff3b0"), x=px + 54, y=FY - 74, scale=0.55)
p.add(props.form("#ffffff"), x=px + 50, y=FY - 78, scale=0.55)
p.add(props.stamp(), x=px + 20, y=FY - 70, scale=0.8)
p.balloon("Case 4831. “Find a pen that works.” Requester: anonymous.", 120, 8, tail=(px - 40, 190), max_width=240)

# 4  KA-CHUNK / what luck
p = P[3]; stage(p)
DT = FY - 84
mx = 125
p.add(margo.draw("write", "deadpan", "right", look="down", pearl=True), x=mx, y=DT + 88, scale=1.0)
p.add(props.desk(230), x=mx + 10, y=DT)
paper(p, mx + 10, DT + 5, 110)
p.add(props.scribble(dry=False), x=mx + 6, y=DT - 6, scale=0.9)
pen_on_paper(p, mx + 58, DT - 6, k=1.1)
px = 372
p.add(pip.draw("point", "proud", "left", look="side"), x=px + 2, y=DT + 11, scale=1.1)
p.add(props.desk(190), x=px - 5, y=DT)
p.add(props.folder(MUSTARD), x=px - 70, y=DT, scale=1.3)
p.add(props.stamp(), x=px - 71, y=DT - 26, scale=1.8)
p.add(circle(px - 70.6, DT - 66, 6.6, fill=LAVENDER, w=3.3))
p.add(path(f"M{px-108},{DT-34} l-14,-6 M{px-110},{DT-20} l-16,0 M{px-34},{DT-34} l14,-6", w=3))
p.sfx("KA-CHUNK", 180, 135, size=34, rotate=-6)
p.balloon("What luck.", 16, 20, tail=(mx - 4, 110), max_width=130)

s.save(pathlib.Path(__file__).parent / "comic.svg")
