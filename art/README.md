# Art kit

Import from the repo root: `sys.path.insert(0, ROOT)`; `from art.characters import margo, pip`;
`from art import props`; `from art.palette import *`.

## Characters (`art/characters/`)
`draw(pose, expression, facing="right")` returns an SVG fragment, origin at the feet.
- **margo.py** (~235 tall): `draw(pose, expression, facing, look="side", pearl=False)`. Poses `stand, point, shrug, hold (carries a folder), arms_up, touch (right hand at top button), offer (right arm out at chest height, e.g. handing over a stamp), write (both hands at desk height in front)`.
  `look`: side/front/up/down (pupils). `pearl=True` draws her mismatched pearly top button (use it from 0011 on)
  (for desk scenes, stand her behind `props.desk`).
  Expressions `neutral, deadpan, happy, worried, surprised, smug, annoyed`.
  Pose `cup`: right hand at chest height for a mug (see `margo_mug` in episodes/0014/compose.py).
- **pip.py** (~120 tall): `draw(pose, expression, facing, look="side")`, look = side/front/up/down. Poses `stand, point, wave, hold, arms_up, slump` (slump forces a sad face and squashes the body).
  Expressions `neutral, happy, worried, surprised, proud, sad, flustered`.
  Flame height reflects mood.
- **fen.py** (~140 tall incl. float, cloud ~140 wide): `draw(pose, expression, facing, look="side", drizzle=None)`. Grey raincloud in a teal tie, floats ~10 above a soft floor shadow (origin on the floor beneath). Poses `stand, point, wave, hold (clipboard gripped in both hands, right of the tie), tie (right hand at the knot: Fen's tell), arms_up`. Expressions `neutral, polite, proud, worried, surprised, sad, flustered`. `drizzle` None = from expression (worried/surprised 1, sad/flustered 2) or force 0-3. At scale ~0.8 Fen's cloud top is about Pip's flame height.

## Props (`art/props.py`)
`old_file()` (tied bundle of lavender folders), `request_slip()` (child's wobbly slip), `review_form(handwritten, name, font)` (380x250 PROBATIONARY REVIEW form, top-left origin, blue handwritten line; scale ~1.1 for an insert, ~0.2 when held), `scribble(dry)` (grey scratch marks when dry=True, a blue ink line otherwise; ~70 wide), `pen()` (rust pen in a hand, origin at the nib), `big_form(extra, font)` (260x150 form, top-left origin; `extra` adds a ticked hand-drawn box with that label; skew/scale it to lie on a desk, see episodes/0011/compose.py). `sky_bg(w,h)` (morning sky, sun, skyline), `roof_bg(w,h)` (rooftop + parapet over sky), `water_tank()`, `roof_door()` (door with ROOF sign). Also: `desk(w)` (narrow widths like 120-190 work for Pip's small desk), `folder(color)`, `mug(steam)`, `tube_station()`, `clipboard()`, `stamp()`,
`paper_stack(n)`, `note(big)`, `earring()`, `note(big)`, `tin()`, `form(color)`, `window(night)`, `street_bg(w,h)` (rainy night street), `bus()` (mustard bus, side view), `runner()` (commuter with umbrella), `office_bg(w, h, floor_y, window_at, night)`.
Origins are documented in the module docstring.

`supply_closet(open_)` (doorway 150x250 with impossibly deep shelves, SUPPLIES sign, door swung out on the right; origin bottom-centre), `ream(banded)` (~80x44 ream of forms with a paper band), `closure_form(font, ticked)` (380x260 close-up of FORM 1 · CASE CLOSURE with STAMPED / EXCEEDS SMALL (REFER UP) / FOUND BY REQUESTER and "Approved: H."; top-left origin), `folded_sheet()` (~34x24 folded form with teal header; draw before Margo to tuck behind her bun, see episodes/0014/compose.py).

## Palette (`art/palette.py`)
Colour constants and small helpers `line, path, circle, ellipse, rect, flip_group`.

## Model sheets
`python3 art/make_model_sheets.py` then `python3 tools/render.py art/model-sheets/<name>.svg`.

## Layout variants
Custom panel rects: `Strip(width, height, panels=[Rect(x, y, w, h), ...])`; see episodes/0011/compose.py for 2+2+1 wide.

## Episode helpers worth reusing
episodes/0013/compose.py has `held_stamp` (a stamp gripped by Margo's hand), `pen_on_paper` (a pen on its nib for two-shots) and `paper` (a sheet lying flat on a desk, skewed).

`note_card(lines, font, handled=False, size=17, crease=False)` (legible ~170-wide Hollis note, top-left origin; `handled=True` adds a rotated rust HANDLED stamp impression; skew it to lie on a desk, see `flat_card` in episodes/0015/compose.py).

## Stairwell (ep 0016)
`stairwell_bg(w, h, x_top, y_top, run=56, rise=26)`: full-panel stairwell with pale putty wall, green dado band, and a concrete flight descending to the LEFT from a landing edge at (x_top, y_top), plus a handrail. `stair_step(k, x_top, y_top)` returns (x, y) for feet on step k (k=0 is the landing). `door_5(number, font, ajar=False)`: grey-green fire door ~116x198 with a big teal painted number to its left (origin bottom-centre of the door). `puddle(drops)`: ~90-wide grey rain puddle with up to 3 drops (origin centre; reuse for Fen's drizzle). `form_fan(labels, font, hand, spread)`: forms fanned like cards with left-aligned header numbers and a Margo hand at the grip (origin grip). For a close-up, use Margo at scale 1.6 with pose `offer` and put the fan at her hand (see episodes/0016/compose.py). Constants: STAIR_WALL, STAIR_DADO, CONCRETE, RAIN.

`door_5(ajar=True)` (ep 0017): the door swung open on its left hinge, warm late-afternoon light in the gap and a big rust rubber doorstop wedge at the bottom right. Keep Fen or anyone else left of the gap so the wedge reads.
