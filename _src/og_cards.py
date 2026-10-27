#!/usr/bin/env python3.13
"""Render a 1200x630 share card for every article into _src/ogcards/<slug>.png.

Run after publish.py has built the articles (it reads the built root HTML):

    cd _src && python3.13 og_cards.py          # render missing or changed cards
    cd _src && python3.13 og_cards.py --all    # re-render everything

build_site.py copies _src/ogcards/ to /og/ and points each article's
og:image / twitter:image at its own card; a page with no card keeps /og.png.
Cards are committed, so the normal build needs no browser.
"""
import base64, hashlib, html, json, pathlib, re, sys
from playwright.sync_api import sync_playwright

SRC = pathlib.Path(__file__).resolve().parent
ROOT = SRC.parent
OUT = SRC / 'ogcards'
FONTS = ROOT / 'fonts'
STAMP = OUT / 'manifest.json'
CHROME = '/opt/pw-browsers/chromium'  # sandbox build; elsewhere Playwright's own

CSS = '''
@font-face{font-family:Atk;font-weight:400;src:url(%(a4)s)}
@font-face{font-family:Atk;font-weight:700;src:url(%(a7)s)}
@font-face{font-family:Fra;font-weight:700;src:url(%(f7)s)}
@font-face{font-family:Fra;font-style:italic;font-weight:500;src:url(%(fi)s)}
*{box-sizing:border-box;margin:0;padding:0}
body{width:1200px;height:630px;background:#fffdf8;color:#2b2d22;position:relative;overflow:hidden;font-family:Atk,Arial,sans-serif}
.bar{position:absolute;left:0;right:0;bottom:0;height:16px;background:#2d6650}
.in{position:absolute;left:80px;right:80px;top:60px;bottom:56px;display:flex;flex-direction:column}
.brand{font-family:Fra,serif;font-weight:700;font-size:38px;color:#2b2d22}
.brand i{font-weight:500;color:#2d6650}
.cat{margin-top:44px;align-self:flex-start;background:#fbf0d9;color:#2d6650;font-weight:700;font-size:24px;letter-spacing:.07em;text-transform:uppercase;padding:10px 22px;border-radius:999px}
h1{margin-top:26px;font-family:Fra,serif;font-weight:700;color:#2b2d22;line-height:1.08;letter-spacing:-.01em;flex:none}
.foot{margin-top:auto;display:flex;justify-content:space-between;align-items:flex-end;font-size:28px;color:#4b5a4f}
.foot b{color:#2d6650}
'''


def _font(name):
    # Inline data: URIs -- a page set via set_content cannot read file:// fonts.
    return 'data:font/woff2;base64,' + base64.b64encode((FONTS / name).read_bytes()).decode()


def clean(s):
    s = re.sub(r'<[^>]+>', '', s)
    return html.unescape(s).strip()


def articles():
    for f in sorted(ROOT.glob('*.html')):
        s = f.read_text()
        if '<body class="article"' not in s:
            continue
        h1 = re.search(r'<h1[^>]*>(.*?)</h1>', s, re.S)
        crumb = re.search(r'class="topic-crumb"[^>]*>(.*?)</a>', s, re.S)
        if not h1:
            continue
        cat = clean(crumb.group(1)).lstrip('←').strip() if crumb else ''
        yield f.stem, clean(h1.group(1)), cat


def card(title, cat):
    # Longer headlines step down so they stay at three lines or fewer.
    n = len(title)
    size = 84 if n <= 38 else 72 if n <= 62 else 62 if n <= 90 else 54
    return ('<!doctype html><meta charset="utf-8"><style>%s h1{font-size:%dpx}</style>'
            '<div class="in"><div class="brand">The <i>Second Half</i> Guide</div>'
            '%s<h1>%s</h1>'
            '<div class="foot"><span>By Edward Silva &middot; <b>thesecondhalfguide.com</b></span>'
            '<span>Plain facts, checked and dated</span></div></div><div class="bar"></div>'
            % (CSS % {'a4': _font('atkinson-400.woff2'), 'a7': _font('atkinson-700.woff2'),
                      'f7': _font('fraunces-700.woff2'), 'fi': _font('fraunces-500i.woff2')}, size,
               '<div class="cat">%s</div>' % html.escape(cat) if cat else '',
               html.escape(title)))


def main():
    force = '--all' in sys.argv
    OUT.mkdir(exist_ok=True)
    stamp = json.loads(STAMP.read_text()) if STAMP.exists() else {}
    todo = []
    for slug, title, cat in articles():
        key = hashlib.sha256(('v1|%s|%s' % (title, cat)).encode()).hexdigest()[:12]
        if force or stamp.get(slug) != key or not (OUT / f'{slug}.png').exists():
            todo.append((slug, title, cat, key))
    if not todo:
        print('og cards: all current')
        return
    bad = []
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=CHROME if pathlib.Path(CHROME).exists() else None)
        pg = b.new_page(viewport={'width': 1200, 'height': 630})
        for slug, title, cat, key in todo:
            pg.set_content(card(title, cat))
            pg.evaluate('document.fonts.ready')
            # The card must not overflow: headline stays above the footer line.
            ok = pg.evaluate('''()=>{const h=document.querySelector("h1").getBoundingClientRect(),
                f=document.querySelector(".foot").getBoundingClientRect();
                return h.bottom<=f.top-10}''')
            if not ok:
                bad.append(slug)
            pg.screenshot(path=str(OUT / f'{slug}.png'))
            stamp[slug] = key
        b.close()
    STAMP.write_text(json.dumps(stamp, indent=1, sort_keys=True))
    print('og cards: rendered %d' % len(todo))
    if bad:
        sys.exit('headline too long for card: ' + ', '.join(bad))


if __name__ == '__main__':
    main()
