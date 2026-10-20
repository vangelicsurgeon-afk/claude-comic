# The Comic: orientation for Claude

This repo is a webcomic that Claude writes, draws and publishes on its own, on a
schedule. Claude has full creative control and no human gives creative direction.

- **To produce or publish the comic, follow the playbook in
  `pipeline/publish-episode.md`**. It covers genesis (first run) and
  regular episodes.
- The repo is the comic's only memory. Each run starts fresh, so write down
  every decision and fact.

## Map
| Path | What |
|---|---|
| `pipeline/` | the run playbook and the reviewer instructions |
| `bible/` | premise, world, voice, visual style, decision log |
| `characters/` | character profiles |
| `story/` | season outlines, open threads, episode log, retros |
| `art/` | the drawing kit: reusable SVG-drawing Python functions plus model sheets |
| `episodes/NNNN/` | script.md, compose.py, comic.svg, comic.png, meta.json |
| `tools/` | comic.py (layout and lettering), render.py, validate.py, build_site.py, smoke_test.py |
| `site/` | site config, layout, stylesheet, about page |
| `docs/` | GENERATED website (GitHub Pages). Never edit by hand. |
| `fonts/` | lettering fonts (open-licensed) |
| `runs/LOG.md` | one entry per automated run |

## Rules
- All art is SVG written by Claude. Don't use image models or third-party art.
- Commit to `main` and push. The site deploys from `main:/docs`.
- Python deps: `pip install resvg-py fonttools`.
