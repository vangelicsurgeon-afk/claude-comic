# Art kit

Import from the repo root: `sys.path.insert(0, ROOT)`; `from art.characters import margo, pip`;
`from art import props`; `from art.palette import *`.

## Characters (`art/characters/`)
`draw(pose, expression, facing="right")` returns an SVG fragment, origin at the feet.
- **margo.py** (~235 tall): `draw(pose, expression, facing, look="side", pearl=False)`. Poses `stand, point, shrug, hold (carries a folder), arms_up, touch (right hand at top button)`.
  `look`: side/front/up/down (pupils). `pearl=True` draws her mismatched pearly top button (use it from 0011 on)
  (for desk scenes, stand her behind `props.desk`).
  Expressions `neutral, deadpan, happy, worried, surprised, smug, annoyed`.
- **pip.py** (~120 tall): `draw(pose, expression, facing, look="side")`, look = side/front/up/down. Poses `stand, point, wave, hold, arms_up, slump` (slump forces a sad face and squashes the body).
  Expressions `neutral, happy, worried, surprised, proud, sad, flustered`.
  Flame height reflects mood.

## Props (`art/props.py`)
`old_file()` (tied bundle of lavender folders), `request_slip()` (child's wobbly slip), `review_form(handwritten, name, font)` (380x250 PROBATIONARY REVIEW form, top-left origin, blue handwritten line; scale ~1.1 for an insert, ~0.2 when held), `pen()` (rust pen in a hand, origin at the nib), `big_form(extra, font)` (260x150 form, top-left origin; `extra` adds a ticked hand-drawn box with that label; skew/scale it to lie on a desk, see episodes/0011/compose.py). `sky_bg(w,h)` (morning sky, sun, skyline), `roof_bg(w,h)` (rooftop + parapet over sky), `water_tank()`, `roof_door()` (door with ROOF sign). Also: `desk(w)`, `folder(color)`, `mug(steam)`, `tube_station()`, `clipboard()`, `stamp()`,
`paper_stack(n)`, `note(big)`, `earring()`, `note(big)`, `tin()`, `form(color)`, `window(night)`, `street_bg(w,h)` (rainy night street), `bus()` (mustard bus, side view), `runner()` (commuter with umbrella), `office_bg(w, h, floor_y, window_at, night)`.
Origins are documented in the module docstring.

## Palette (`art/palette.py`)
Colour constants and small helpers `line, path, circle, ellipse, rect, flip_group`.

## Model sheets
`python3 art/make_model_sheets.py` then `python3 tools/render.py art/model-sheets/<name>.svg`.

## Layout variants
Custom panel rects: `Strip(width, height, panels=[Rect(x, y, w, h), ...])`; see episodes/0011/compose.py for 2+2+1 wide.
