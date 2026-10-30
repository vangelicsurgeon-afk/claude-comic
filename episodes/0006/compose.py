import sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT)); sys.path.insert(0, str(ROOT / "tools"))
from comic import Strip
from art.characters import margo, pip
from art import props
from art.palette import *

s = Strip(width=1000, height=860, cols=2, rows=2, margin=20, gutter=16, title="0006 Two Seconds")
P = s.panels
W, H = P[0].rect.w, P[0].rect.h
FY = H * 0.78
fam = s.font_family


def stage(p):
    p.add(props.office_bg(W, H, FY, night=True))


# 1  rust folder on the desk
p = P[0]; stage(p)
p.add(margo.draw("stand", "deadpan", "left"), x=W / 2 + 110, y=FY - 10, scale=0.85)
p.add(props.desk(300), x=W / 2 + 60, y=FY - 70)
p.add(props.folder(RUST), x=W / 2 + 20, y=FY - 70)
p.add(props.mug(True), x=W / 2 + 140, y=FY - 70)
p.add(pip.draw("stand", "happy", "right"), x=90, y=FY + 40, scale=0.95)
p.balloon("It's rust. Rust is urgent.", 20, 50, tail=(90, 225), max_width=190)
p.balloon("Rust is paperwork with a deadline.", 230, 20, tail=(W / 2 + 105, 128), max_width=220)

# 2  close-up of the form
p = P[1]
p.add(f'<rect x="0" y="0" width="{W}" height="{H}" fill="{WALL_DARK}"/>')
p.add(props.folder(RUST).replace('<', '<', 1), x=W / 2 - 150, y=70, scale=1.0, rotate=0) if False else None
p.add(f'<g transform="rotate(-2)">'
      f'<rect x="{W/2-190}" y="70" width="380" height="300" fill="#fffdf4" stroke="{INK}" stroke-width="4"/>'
      f'<rect x="{W/2-190}" y="70" width="380" height="36" fill="{RUST}" stroke="{INK}" stroke-width="4"/>'
      f'<text x="{W/2-170}" y="96" font-family="{fam}" font-size="22" font-weight="700" fill="#fffdf4">URGENT</text>'
      f'<text x="{W/2-170}" y="150" font-family="{fam}" font-size="22" fill="{INK}">Request: bus to wait.</text>'
      f'<text x="{W/2-170}" y="210" font-family="{fam}" font-size="22" fill="{INK}">Duration:</text>'
      f'<text x="{W/2-170}" y="290" font-family="{fam}" font-size="64" font-weight="700" fill="{RUST}">2 seconds</text>'
      f'<line x1="{W/2-170}" y1="335" x2="{W/2+170}" y2="335" stroke="#9aa0a6" stroke-width="2.5"/>'
      f'</g>')
p.caption("Case 4802", "bottom-left")

# 3  elsewhere: the bus and the runner
p = P[2]
p.add(props.street_bg(W, H))
gy = H * 0.72
p.add(props.bus(doors_open=False), x=W - 165, y=gy + 50)
p.add(props.runner(), x=70, y=gy + 40, scale=1.2)
p.sfx("hff hff", 70, 190, size=26, rotate=-4)
p.caption("8:14 PM. Elsewhere.", "top-left")

# 4  the stamp, held
p = P[3]; stage(p)
p.add(margo.draw("stand", "deadpan", "right"), x=W / 2 - 40, y=FY - 10, scale=0.85)
p.add(props.desk(300), x=W / 2 + 10, y=FY - 70)
p.add(props.form("#fffdf4"), x=W / 2 + 60, y=FY - 70)
p.add(props.stamp(), x=W / 2 + 110, y=FY - 70)
p.add(pip.draw("stand", "neutral", "left"), x=W - 90, y=FY + 40, scale=0.95)
p.balloon("One.", 40, 20, tail=(W / 2 - 60, 80), max_width=100)
p.sfx("CHUNK", W - 190, 90, size=40)

s.save(pathlib.Path(__file__).parent / "comic.svg")
