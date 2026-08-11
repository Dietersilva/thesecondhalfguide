#!/usr/bin/env python3
"""Assemble the deployable static site from the artifact pages.

The artifact builders inline fonts and link to claude.ai URLs, which is right
for previewing but wrong for a real site. This turns that output into:
  - one shared styles.css and real .woff2 files instead of 24 copies of base64
  - clean root-relative paths (/about, /medicare-enrollment)
  - a proper <head> per page: description, canonical, Open Graph, favicon
  - sitemap.xml, robots.txt, vercel.json security headers
"""

import base64
import hashlib
import json
import os
import re
import shutil

SITE = 'site'
ORIGIN = 'https://thesecondhalfguide.com'

# artifact uuid -> site path
ROUTES = {
    'd7289b2f-07da-4008-b5cf-6c2547f70169': '/',
    '9547133b-a75a-4f81-b112-6ed4d1034a63': '/about',
    'bde95ba2-582b-4a77-af16-559d0beb862c': '/contact',
    '01d12169-239a-4780-afc1-244fead8ddd6': '/privacy',
    # original four
    '7ccf5206-2e2c-42c9-a49c-cbb27d5f88b5': '/approaching-60',
    'c1ae0269-8005-42bc-aa20-4bf4c8d1a177': '/social-security-62',
    'c9bd23f5-82bb-469a-aaf8-592026422822': '/bank-imposter-scam',
    '88860eb8-0dc4-4cad-a053-b4b17afa6fc8': '/wednesday-letters',
}

DESCRIPTIONS = {
    '/': 'Smart, practical information for people roughly 55–70 navigating the financial and '
         'lifestyle transition into retirement — what nobody tells you about the 10 years '
         'surrounding it.',
    '/about': 'Who writes The Second Half Guide, how it is funded, and the editorial standards it '
              'holds itself to.',
    '/contact': 'How to reach The Second Half Guide — corrections, topic suggestions and reader stories.',
    '/privacy': 'Privacy Policy and Terms of Use for The Second Half Guide, including advertising '
                'cookies and editorial disclaimers.',
    '/approaching-60': 'What genuinely changes as you approach 60, what does not, and the handful of '
                       'deadlines worth putting on a calendar.',
    '/social-security-62': 'The maths behind claiming Social Security at 62 — when filing early pays '
                           'off and when it does not.',
    '/bank-imposter-scam': 'How the bank impostor call works, why it is so effective, and exactly what '
                           'to do if one reaches you.',
    '/wednesday-letters': 'The Wednesday Letters — reader correspondence from The Second Half Guide.',
}

PAGE_FILES = {
    'second-half-guide.html': '/',
    'about.html': '/about',
    'contact.html': '/contact',
    'privacy.html': '/privacy',
    'approaching-60.html': '/approaching-60',
    'social-security-62.html': '/social-security-62',
    'bank-imposter-scam.html': '/bank-imposter-scam',
    'wednesday-letters.html': '/wednesday-letters',
}

FONT_FILES = {
    'fonts/atkinson-normal-400.b64': 'atkinson-400.woff2',
    'fonts/atkinson-normal-700.b64': 'atkinson-700.woff2',
    'fonts/atkinson-italic-400.b64': 'atkinson-400i.woff2',
    'fonts/fraunces-normal-700.b64': 'fraunces-700.woff2',
    'fonts/fraunces-italic-500.b64': 'fraunces-500i.woff2',
}

FAVICON = (
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">'
    '<rect width="64" height="64" rx="12" fill="#2C6650"/>'
    '<circle cx="32" cy="32" r="19" fill="none" stroke="#FBF3DD" stroke-width="4"/>'
    '<path d="M32 13v19l12 8" fill="none" stroke="#E08E2B" stroke-width="4" '
    'stroke-linecap="round" stroke-linejoin="round"/></svg>'
)


def collect_pages():
    """slug path -> raw artifact html"""
    pages = {}
    for fn, path in PAGE_FILES.items():
        if os.path.exists(fn):
            pages[path] = open(fn).read()
    for fn in sorted(os.listdir('articles')):
        if fn.endswith('.html'):
            pages['/' + fn[:-5]] = open(f'articles/{fn}').read()
    return pages


FONT_FACE_RE = re.compile(r'@font-face\s*\{[^}]*\}', re.S)

# Every page carried its own <style> block, and several define the same
# selectors with different values (.wrap is 1040px on the hub, 760px on an
# article, 680px on a letter). Concatenating them into one stylesheet let the
# last definition win everywhere. Each layout's rules are scoped under a body
# class instead; genuinely global bits (:root, *, html, @font-face) stay shared.
GLOBAL_SELECTORS = {':root', '*', 'html'}


def split_rules(css):
    """Yield top-level (prelude, body_or_None) pairs."""
    i, n, start = 0, len(css), 0
    while i < n:
        c = css[i]
        if c == '{':
            prelude = css[start:i].strip()
            depth, j = 1, i + 1
            while j < n and depth:
                if css[j] == '{': depth += 1
                elif css[j] == '}': depth -= 1
                j += 1
            yield prelude, css[i + 1:j - 1]
            i = start = j
        elif c == ';' and css[start:i].strip().startswith('@'):
            yield css[start:i].strip(), None
            i += 1; start = i
        else:
            i += 1


def scope_css(css, cls):
    """Prefix rules with body.<cls>; return (scoped, global_rules)."""
    scoped, globals_ = [], []
    for prelude, block in split_rules(css):
        if block is None:
            globals_.append(prelude + ';'); continue
        if prelude.startswith('@media') or prelude.startswith('@supports'):
            inner, inner_globals = scope_css(block, cls)
            globals_.extend(inner_globals)
            if inner.strip():
                scoped.append(f'{prelude} {{{inner}}}')
            continue
        if prelude.startswith('@'):
            globals_.append(f'{prelude} {{{block}}}'); continue
        out = []
        for sel in (p.strip() for p in prelude.split(',')):
            if not sel: continue
            if sel in GLOBAL_SELECTORS:
                globals_.append(f'{sel} {{{block}}}'); continue
            if sel == 'body' or sel.startswith('body.') or sel.startswith('body '):
                out.append(sel.replace('body', f'body.{cls}', 1))
            else:
                out.append(f'body.{cls} {sel}')
        if out:
            scoped.append(f'{", ".join(out)} {{{block}}}')
    return '\n'.join(scoped), globals_



# --- House promos -----------------------------------------------------------
# Until advertising is live, the ad slots carry promos for other articles
# rather than dashed placeholders. Unsold inventory becomes internal linking,
# which is worth more to a new site than an empty box announcing it has no ads.
# Flip ADS_LIVE to True when AdSense is approved and the slots come back.
ADS_LIVE = False

# Broadly appealing pieces — the ones worth putting in front of any reader.
PROMO_POOL = [
    '/airport-help', '/five-minute-rule', '/senior-age', '/medicare-enrollment',
    '/beneficiary-form', '/free-college', '/parks-pass', '/voice-cloning',
    '/medicare-gaps', '/long-term-care', '/property-tax', '/the-big-trip',
]

AD_SLOT_RE = re.compile(
    r'[ \t]*<div class="((?:wrap-wide |wrap )?ad-slot)">.*?</div>\s*</div>\n?',
    re.S)


def house_promo(target, title, blurb, wide):
    cls = 'house house-wide' if wide else 'house'
    return (f'      <a class="{cls}" href="{target}">\n'
            f'        <span class="house-label">Also on The Second Half Guide</span>\n'
            f'        <span class="house-title">{title}</span>\n'
            f'        <span class="house-blurb">{blurb}</span>\n'
            f'        <span class="house-more">Read it &rarr;</span>\n'
            f'      </a>\n')


HOUSE_CSS = """
body.hub .house, body.article .house, body.doc .house {
  display: block; margin: 44px 0; padding: 24px 28px; text-decoration: none;
  background: var(--surface-2); border-radius: var(--radius);
  border-left: 4px solid var(--pine);
}
body.hub .house:hover, body.article .house:hover, body.doc .house:hover {
  background: color-mix(in srgb, var(--gold-soft) 40%, var(--surface-2));
}
body.hub .house-label, body.article .house-label, body.doc .house-label {
  display: block; font-size: 12.5px; font-weight: 700; letter-spacing: 0.07em;
  text-transform: uppercase; color: var(--pine-strong); margin-bottom: 8px;
}
body.hub .house-title, body.article .house-title, body.doc .house-title {
  display: block; font-family: 'Fraunces', serif; font-weight: 700; font-size: 21px;
  line-height: 1.25; color: var(--ink); margin-bottom: 6px; text-wrap: balance;
}
body.hub .house-blurb, body.article .house-blurb, body.doc .house-blurb {
  display: block; font-size: 16.5px; color: var(--ink-soft); max-width: 62ch;
}
body.hub .house-more, body.article .house-more, body.doc .house-more {
  display: inline-block; margin-top: 12px; font-size: 15.5px; font-weight: 700;
  color: var(--pine-strong);
}
"""


# --- Latest ------------------------------------------------------------------
# Newest first. An article's topic card is its permanent home; this is a
# time-ordered view of the same pages, not a separate place things live in for a
# week. Add new slugs to the top as they publish.
LATEST = [
    '/medicare-savings', '/widows-penalty', '/falls', '/wellness-visit',
    '/downsizing-math', '/driving',
    '/gold-courier-scam', '/wep-gpo-repeal', '/social-security-login',
    '/airport-help', '/airport-security', '/passport-traps',
    '/travel-medications', '/cruise-medical', '/the-big-trip',
    '/hearing-aids', '/long-term-care', '/cola',
]
LATEST_SHOWN = 6

LATEST_CSS = """
body.hub .latest { padding: 8px 0 56px; }
body.hub .latest-grid {
  display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 18px;
}
body.hub .latest-card {
  display: block; text-decoration: none; background: var(--surface);
  border: 1px solid var(--line); border-radius: var(--radius); padding: 22px 24px;
  box-shadow: var(--shadow);
}
body.hub .latest-card:hover { border-color: var(--pine); }
body.hub .latest-kicker {
  display: block; font-size: 12.5px; font-weight: 700; letter-spacing: 0.06em;
  text-transform: uppercase; color: var(--pine-strong); margin-bottom: 8px;
}
body.hub .latest-card h3 {
  font-family: 'Fraunces', serif; font-weight: 700; font-size: 19px; line-height: 1.25;
  margin: 0 0 8px; color: var(--ink); text-wrap: balance;
}
body.hub .latest-card p { margin: 0; font-size: 16px; color: var(--ink-soft); }
"""


def latest_section(meta):
    cards = []
    for path in LATEST[:LATEST_SHOWN]:
        if path not in meta:
            continue
        headline, blurb = meta[path]
        if len(blurb) > 150:
            blurb = blurb[:147].rsplit(' ', 1)[0] + '&hellip;'
        cards.append(
            f'        <a class="latest-card" href="{path}">\n'
            f'          <span class="latest-kicker">New</span>\n'
            f'          <h3>{headline}</h3>\n'
            f'          <p>{blurb}</p>\n'
            f'        </a>')
    if not cards:
        return ''
    return ('  <section class="latest" id="latest">\n    <div class="wrap">\n'
            '      <div class="section-head">\n        <h2>Latest</h2>\n'
            '        <p>The most recent pieces. Everything stays filed under its topic below &mdash; '
            'this is just what went up most recently.</p>\n      </div>\n'
            '      <div class="latest-grid">\n' + '\n'.join(cards)
            + '\n      </div>\n    </div>\n  </section>\n')

def layout_class(path):
    if path == '/': return 'hub'
    if path in ('/about', '/contact', '/privacy'): return 'doc'
    return 'article'


NEW_FONT_FACES = """
@font-face{font-family:'Atkinson Hyperlegible';font-style:normal;font-weight:400;font-display:swap;src:url(/fonts/atkinson-400.woff2) format('woff2')}
@font-face{font-family:'Atkinson Hyperlegible';font-style:normal;font-weight:700;font-display:swap;src:url(/fonts/atkinson-700.woff2) format('woff2')}
@font-face{font-family:'Atkinson Hyperlegible';font-style:italic;font-weight:400;font-display:swap;src:url(/fonts/atkinson-400i.woff2) format('woff2')}
@font-face{font-family:'Fraunces';font-style:normal;font-weight:600 700;font-display:swap;src:url(/fonts/fraunces-700.woff2) format('woff2')}
@font-face{font-family:'Fraunces';font-style:italic;font-weight:500;font-display:swap;src:url(/fonts/fraunces-500i.woff2) format('woff2')}
"""


def main():
    if os.path.exists(SITE):
        shutil.rmtree(SITE)
    os.makedirs(f'{SITE}/fonts')

    for src, dest in FONT_FILES.items():
        with open(f'{SITE}/fonts/{dest}', 'wb') as f:
            f.write(base64.b64decode(open(src).read().strip()))

    pages = collect_pages()

    # article slug -> path, so cross-links resolve locally
    routes = dict(ROUTES)
    if os.path.exists('article_urls.json'):
        for slug, url in json.load(open('article_urls.json')).items():
            uuid = url.rstrip('/').split('/')[-1]
            routes[uuid] = '/' + slug
    for uuid in ('9aa6d645-f0f3-4db2-8c71-535ebb5fb551', 'b36f1473-2201-4354-ad3d-9f12fc5e11e6',
                 '1f79fa4b-7886-4d6d-b812-2e2142c030e6', 'f18cc53c-1c7b-473a-bafc-bac54df82623',
                 '8463d7bb-bd49-4b97-a8f4-1319bf03ff35'):
        pass  # covered by article_urls.json below if present

    css_blocks, seen = [], set()
    global_rules, seen_scoped = [], set()
    meta = {}
    script_hashes = set()
    rendered = {}

    for path, html in sorted(pages.items()):
        title_m = re.search(r'<title>(.*?)</title>', html, re.S)
        title = title_m.group(1).strip() if title_m else 'The Second Half Guide'

        style_m = re.search(r'<style>(.*?)</style>', html, re.S)
        css = style_m.group(1) if style_m else ''
        css = FONT_FACE_RE.sub('', css)
        cls = layout_class(path)
        scoped, page_globals = scope_css(css, cls)
        for g in page_globals:
            if g not in seen:
                seen.add(g); global_rules.append(g)
        if (cls, scoped) not in seen_scoped:
            seen_scoped.add((cls, scoped))
            css_blocks.append(scoped)

        body = html[style_m.end():] if style_m else html
        body = re.sub(r'^\s*', '', body)

        # rewrite artifact links to local routes
        def swap(m):
            return routes.get(m.group(1), '/')
        body = re.sub(r'https://claude\.ai/code/artifact/([a-f0-9-]{36})', swap, body)

        # Allow-list each inline script by hash instead of relaxing script-src.
        for s in re.findall(r'<script(?![^>]*\ssrc=)[^>]*>(.*?)</script>', body, re.S):
            digest = base64.b64encode(hashlib.sha256(s.encode()).digest()).decode()
            script_hashes.add(f"'sha256-{digest}'")

        desc = DESCRIPTIONS.get(path)
        if not desc:
            d = re.search(r'<p class="dek">(.*?)</p>', body, re.S)
            desc = re.sub(r'<[^>]+>', '', d.group(1)).strip() if d else DESCRIPTIONS['/']
        desc = re.sub(r'\s+', ' ', desc)[:300]
        canonical = ORIGIN + ('' if path == '/' else path)

        h1m = re.search(r'<h1[^>]*>(.*?)</h1>', body, re.S)
        headline = re.sub(r'\s+', ' ', h1m.group(1)).strip() if h1m else title
        meta[path] = (headline, desc)

        rendered[path] = (title, desc, canonical, body)

    # The article-layout pages came from templates with three different
    # measures (680/740/760). Settle on one so every article reads the same
    # and the fact tables have room.
    NORMALIZE = '\nbody.article .wrap { max-width: 760px; }\n'
    if '/' in rendered:
        title, desc, canonical, body = rendered['/']
        marker = '  <section class="topics" id="topics">'
        if marker in body:
            body = body.replace(marker, latest_section(meta) + '\n' + marker, 1)
            rendered['/'] = (title, desc, canonical, body)

    if not ADS_LIVE:
        pool = [p for p in PROMO_POOL if p in rendered]
        for i, path in enumerate(sorted(rendered)):
            title, desc, canonical, body = rendered[path]
            picks = [p for p in pool if p != path]
            if not picks:
                continue
            n = [0]

            def swap(m, path=path, picks=picks, n=n):
                target = picks[(i + n[0]) % len(picks)]
                n[0] += 1
                headline, blurb = meta[target]
                return house_promo(target, headline, blurb, 'wrap-wide' in m.group(1))

            rendered[path] = (title, desc, canonical, AD_SLOT_RE.sub(swap, body))

    styles = (NEW_FONT_FACES + '\n'.join(global_rules) + '\n'
              + '\n'.join(css_blocks) + NORMALIZE + LATEST_CSS + (HOUSE_CSS if not ADS_LIVE else ''))
    open(f'{SITE}/styles.css', 'w').write(styles)
    open(f'{SITE}/favicon.svg', 'w').write(FAVICON)
    if os.path.exists('ogcard/og.png'):
        shutil.copy('ogcard/og.png', f'{SITE}/og.png')
    if os.path.isdir('images'):
        shutil.copytree('images', f'{SITE}/images')

    for path, (title, desc, canonical, body) in rendered.items():
        head = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="{'website' if path == '/' else 'article'}">
<meta property="og:site_name" content="The Second Half Guide">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{ORIGIN}/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="The Second Half Guide — what nobody tells you about the 10 years surrounding retirement.">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{ORIGIN}/og.png">
<meta name="author" content="Edward Silva">
<meta name="robots" content="index, follow, max-image-preview:large">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preload" href="/fonts/atkinson-400.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/styles.css">
</head>
<body class=\"{layout_class(path)}\">
"""
        out = head + body.rstrip() + '\n</body>\n</html>\n'
        fn = 'index.html' if path == '/' else f'{path.lstrip("/")}.html'
        dest = os.path.join(SITE, fn)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        open(dest, 'w').write(out)

    # sitemap
    urls = ''.join(
        f'  <url><loc>{ORIGIN}{"" if p == "/" else p}</loc>'
        f'<changefreq>{"weekly" if p == "/" else "monthly"}</changefreq>'
        f'<priority>{"1.0" if p == "/" else "0.8"}</priority></url>\n'
        for p in sorted(rendered))
    open(f'{SITE}/sitemap.xml', 'w').write(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + '</urlset>\n')

    open(f'{SITE}/robots.txt', 'w').write(
        f'User-agent: *\nAllow: /\n\nSitemap: {ORIGIN}/sitemap.xml\n')

    # Strict CSP: the site ships no scripts and no third-party assets today.
    # AdSense will require loosening script-src/frame-src — do that deliberately.
    csp = (f"default-src 'self'; "
           "img-src 'self' data:; "
           "style-src 'self'; "
           "font-src 'self'; "
           f"script-src {' '.join(sorted(script_hashes)) or chr(39)+'none'+chr(39)}; "
           "object-src 'none'; "
           "frame-ancestors 'none'; "
           "base-uri 'self'; "
           "form-action 'self'")
    vercel = {
        "$schema": "https://openapi.vercel.sh/vercel.json",
        "cleanUrls": True,
        "trailingSlash": False,
        "headers": [
            {"source": "/(.*)", "headers": [
                {"key": "Strict-Transport-Security",
                 "value": "max-age=63072000; includeSubDomains; preload"},
                {"key": "Content-Security-Policy", "value": csp},
                {"key": "X-Content-Type-Options", "value": "nosniff"},
                {"key": "Referrer-Policy", "value": "strict-origin-when-cross-origin"},
                {"key": "Permissions-Policy",
                 "value": "camera=(), microphone=(), geolocation=(), interest-cohort=()"},
                {"key": "X-Frame-Options", "value": "DENY"},
                {"key": "Cross-Origin-Opener-Policy", "value": "same-origin"},
            ]},
            {"source": "/fonts/(.*)", "headers": [
                {"key": "Cache-Control", "value": "public, max-age=31536000, immutable"}]},
            {"source": "/styles.css", "headers": [
                {"key": "Cache-Control", "value": "public, max-age=604800"}]},
        ],
    }
    open(f'{SITE}/vercel.json', 'w').write(json.dumps(vercel, indent=2) + '\n')

    total = sum(os.path.getsize(os.path.join(r, f))
                for r, _, fs in os.walk(SITE) for f in fs)
    print(f'{len(rendered)} pages, styles.css {len(styles) // 1024}KB, total {total // 1024}KB')
    leftover = [p for p, (_, _, _, b) in rendered.items() if 'claude.ai/code/artifact' in b]
    print('pages still linking to claude.ai:', leftover or 'none')


if __name__ == '__main__':
    main()
