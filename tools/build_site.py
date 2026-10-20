"""
build_site.py - regenerate the static site in docs/ from episodes/ and site/.

    python3 tools/build_site.py

Inputs
  site/config.json   title, tagline, base_url, domain, credit, description
  site/layout.html   page shell with {{placeholders}} (restyle freely)
  site/style.css     stylesheet (restyle freely)
  site/about.html    optional HTML fragment for /about/
  episodes/NNNN/meta.json + comic.svg (+ comic.png)  -- only status "published"

Output: docs/  (served by GitHub Pages from main:/docs). docs/ is fully
regenerated every build; never hand-edit it.
"""
import datetime as dt
import email.utils
import html
import json
import pathlib
import shutil
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
SITE, EPS, OUT = ROOT / "site", ROOT / "episodes", ROOT / "docs"
REQUIRED = ("number", "title", "date", "alt")


def esc(s):
    return html.escape(str(s), quote=True)


def paragraphs(text):
    return "".join(f"<p>{esc(p.strip())}</p>" for p in str(text).split("\n\n") if p.strip())


def load_episodes():
    eps, errors = [], []
    for d in sorted(p for p in EPS.iterdir() if p.is_dir()):
        mf = d / "meta.json"
        if not mf.exists():
            continue
        m = json.loads(mf.read_text(encoding="utf-8"))
        if m.get("status", "published") != "published":
            continue
        missing = [k for k in REQUIRED if not m.get(k)]
        if missing:
            errors.append(f"{d.name}: meta.json missing {missing}")
        if not (d / "comic.svg").exists():
            errors.append(f"{d.name}: comic.svg missing")
        m["_dir"] = d
        m["slug"] = f"{int(m['number']):04d}"
        eps.append(m)
    eps.sort(key=lambda m: int(m["number"]))
    nums = [int(m["number"]) for m in eps]
    if nums != list(range(1, len(nums) + 1)):
        errors.append(f"episode numbers are not contiguous from 1: {nums}")
    return eps, errors


def page(layout, cfg, root, title, body, og_image=None, description=None):
    full_title = f"{title} | {cfg['title']}" if title else cfg["title"]
    og = ""
    base = cfg.get("base_url", "").rstrip("/")
    if og_image and base:
        og = (f'<meta property="og:image" content="{esc(base + "/" + og_image)}">'
              '<meta name="twitter:card" content="summary_large_image">')
    return (layout
            .replace("{{page_title}}", esc(full_title))
            .replace("{{site_title}}", esc(cfg["title"]))
            .replace("{{tagline}}", esc(cfg.get("tagline", "")))
            .replace("{{credit}}", esc(cfg.get("credit", "")))
            .replace("{{description}}", esc(description or cfg.get("description", "")))
            .replace("{{og}}", og)
            .replace("{{root}}", root)
            .replace("{{content}}", body)
            .replace("{{year}}", str(dt.date.today().year)))


def nav(eps, i, root):
    def link(label, target, cls):
        if target is None:
            return f'<span class="nav-{cls} disabled">{label}</span>'
        return f'<a class="nav-{cls}" href="{root}ep/{target["slug"]}/">{label}</a>'
    first, last = eps[0], eps[-1]
    prev = eps[i - 1] if i > 0 else None
    nxt = eps[i + 1] if i < len(eps) - 1 else None
    return ('<nav class="comic-nav">'
            + link("&laquo; First", first if i > 0 else None, "first")
            + link("&lsaquo; Prev", prev, "prev")
            + f'<a class="nav-archive" href="{root}archive/">Archive</a>'
            + link("Next &rsaquo;", nxt, "next")
            + link("Latest &raquo;", last if i < len(eps) - 1 else None, "last")
            + "</nav>")


def episode_body(eps, i, root):
    m = eps[i]
    img = f'{root}ep/{m["slug"]}/comic.svg'
    parts = [
        nav(eps, i, root),
        '<article class="episode">',
        f'<h2 class="ep-title"><span class="ep-num">#{int(m["number"])}</span> {esc(m["title"])}</h2>',
        f'<figure class="comic"><img src="{img}" alt="{esc(m["alt"])}" title="{esc(m.get("hover", ""))}"></figure>',
        f'<p class="ep-date"><time datetime="{esc(m["date"])}">{esc(m["date"])}</time></p>',
    ]
    if m.get("note"):
        parts.append(f'<section class="ep-note">{paragraphs(m["note"])}</section>')
    if m.get("transcript"):
        lines = "".join(f"<li>{esc(t)}</li>" for t in m["transcript"])
        parts.append(f'<details class="transcript"><summary>Transcript</summary><ol>{lines}</ol></details>')
    parts += ["</article>", nav(eps, i, root)]
    return "".join(parts)


def feed(cfg, eps):
    base = cfg.get("base_url", "").rstrip("/")
    items = []
    for m in reversed(eps[-30:]):
        url = f"{base}/ep/{m['slug']}/"
        d = dt.datetime.fromisoformat(m["date"]).replace(hour=12, tzinfo=dt.timezone.utc)
        desc = f'<img src="{base}/ep/{m["slug"]}/comic.png" alt="{esc(m["alt"])}">'
        items.append(f"<item><title>{esc(m['title'])}</title><link>{url}</link><guid>{url}</guid>"
                     f"<pubDate>{email.utils.format_datetime(d)}</pubDate>"
                     f"<description>{esc(desc)}</description></item>")
    return ('<?xml version="1.0" encoding="UTF-8"?><rss version="2.0"><channel>'
            f"<title>{esc(cfg['title'])}</title><link>{base}/</link>"
            f"<description>{esc(cfg.get('description', ''))}</description>"
            + "".join(items) + "</channel></rss>")


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main():
    cfg = json.loads((SITE / "config.json").read_text(encoding="utf-8"))
    layout = (SITE / "layout.html").read_text(encoding="utf-8")
    eps, errors = load_episodes()
    if errors:
        print("BUILD ERRORS:\n  " + "\n  ".join(errors))
        sys.exit(1)

    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    (OUT / ".nojekyll").write_text("")
    shutil.copy(SITE / "style.css", OUT / "style.css")
    if (SITE / "assets").exists():
        shutil.copytree(SITE / "assets", OUT / "assets")
    if cfg.get("domain"):
        (OUT / "CNAME").write_text(cfg["domain"].strip() + "\n")

    for i, m in enumerate(eps):
        dst = OUT / "ep" / m["slug"]
        dst.mkdir(parents=True)
        for f in ("comic.svg", "comic.png"):
            if (m["_dir"] / f).exists():
                shutil.copy(m["_dir"] / f, dst / f)
        og = f"ep/{m['slug']}/comic.png" if (m["_dir"] / "comic.png").exists() else None
        write(dst / "index.html", page(layout, cfg, "../../", m["title"], episode_body(eps, i, "../../"),
                                       og, m["alt"]))

    if eps:
        m = eps[-1]
        og = f"ep/{m['slug']}/comic.png" if (m["_dir"] / "comic.png").exists() else None
        home = episode_body(eps, len(eps) - 1, "")
    else:
        og, home = None, '<section class="coming-soon"><p>The first episode is on its way.</p></section>'
    write(OUT / "index.html", page(layout, cfg, "", None, home, og))

    rows = "".join(f'<li><a href="../ep/{m["slug"]}/"><span class="ep-num">#{int(m["number"])}</span> '
                   f'{esc(m["title"])}</a> <time>{esc(m["date"])}</time></li>' for m in reversed(eps))
    write(OUT / "archive" / "index.html",
          page(layout, cfg, "../", "Archive", f'<section class="archive"><h2>Archive</h2><ol reversed>{rows}</ol></section>'))

    if (SITE / "about.html").exists():
        write(OUT / "about" / "index.html",
              page(layout, cfg, "../", "About", f'<section class="about">{(SITE / "about.html").read_text(encoding="utf-8")}</section>'))

    write(OUT / "feed.xml", feed(cfg, eps))
    print(f"built docs/ with {len(eps)} episode(s)")


if __name__ == "__main__":
    main()
