# Art kit

Import from the repo root: `sys.path.insert(0, ROOT)`; `from art.characters import margo, pip`;
`from art import props`; `from art.palette import *`.

## Characters (`art/characters/`)
`draw(pose, expression, facing="right")` returns an SVG fragment, origin at the feet.
- **margo.py** (~235 tall): poses `stand, point, shrug, hold (carries a folder), arms_up`
  (for desk scenes, stand her behind `props.desk`).
  Expressions `neutral, deadpan, happy, worried, surprised, smug, annoyed`.
- **pip.py** (~120 tall): poses `stand, point, wave, hold, arms_up, slump` (slump forces a sad face and squashes the body).
  Expressions `neutral, happy, worried, surprised, proud, sad, flustered`.
  Flame height reflects mood.

## Props (`art/props.py`)
`desk(w)`, `folder(color)`, `mug(steam)`, `tube_station()`, `clipboard()`, `stamp()`,
`paper_stack(n)`, `note(big)`, `earring()`, `note(big)`, `tin()`, `form(color)`, `window(night)`, `office_bg(w, h, floor_y, window_at, night)`.
Origins are documented in the module docstring.

## Palette (`art/palette.py`)
Colour constants and small helpers `line, path, circle, ellipse, rect, flip_group`.

## Model sheets
`python3 art/make_model_sheets.py` then `python3 tools/render.py art/model-sheets/<name>.svg`.
