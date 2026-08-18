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
import html as html_mod
import hashlib
import json
import os
import re
import shutil

SITE = 'site'
SRC_DIR = os.path.dirname(os.path.abspath(__file__))
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
    # Written for the result page, not the article: 120-158 characters, with
    # the words a reader would actually type near the front. Anything not
    # listed here falls back to the page dek, which is usually too long.
    '/': 'Smart, practical information for people roughly 55–70 — the dates, thresholds and dollar figures of the ten years surrounding retirement, checked and dated.',
    '/medigap-window': 'The one-time six-month Medigap window: when it starts, what guaranteed issue means, and what insurers may ask about your health once it closes.',
    '/numbers': 'The real phone numbers for Medicare, Social Security, fraud reporting and local help — checked, with hours, and printable for the kitchen drawer.',
    '/rmd-deadline': 'Required minimum distributions in 2026: the age by birth year, the first-year trap, the 25% penalty, and the charitable route that skips the tax.',
    '/subscribed': 'Confirm your subscription to Wednesday Letters from The Second Half Guide — and what to do if the confirmation email has not arrived yet.',
    '/about': 'Who writes The Second Half Guide, how it is funded, how the facts are checked, and the standards it holds itself to. Published by Edward Silva.',
    '/advantage-vs-original': 'Medicare Advantage or Original Medicare: what each one is, how the money works, and the one decision that gets much harder to reverse later on.',
    '/airport-security': 'TSA ended the shoes-off rule for everyone in July 2025, deleting the one screening benefit of turning 75. What PreCheck and Global Entry still buy you.',
    '/airport-help': 'Wheelchairs, escorts through the terminal, help through security — all free and yours by law. Almost entirely unused, because nobody tells you.',
    '/approaching-60': 'What actually changes as you approach 60: the deadlines worth a calendar entry, the thresholds that matter, and the many that are only marketing.',
    '/bank-imposter-scam': 'How the bank impostor call works, why it defeats careful people, and the one sentence that stops it — plus what to do if one has already reached you.',
    '/cola': 'Social Security rose 2.8% for 2026. For an average retired worker on the standard Part B premium, Medicare took back about a third before it arrived.',
    '/contact': 'Reach The Second Half Guide: corrections, topic suggestions and reader stories. A real person reads everything, and corrections are especially welcome.',
    '/cruise-medical': 'There is a doctor on board, they bill you, and Medicare almost certainly does not apply. What shipboard care costs, and what evacuation can run to.',
    '/digital-estate': 'Photographs, bills and password resets now live behind a login — and a password is not the same as permission. What an executor can actually reach.',
    '/downsizing-math': 'Selling a big house and buying a small one may free up less than you think. The costs that decide it are the ones nobody puts in the spreadsheet.',
    '/driving': 'Age alone is a poor predictor of who should stop driving. The specific, checkable things that are better ones — and the road in between the two.',
    '/drug-cap': 'Part D prescription costs now have a hard annual ceiling of $2,100. A genuinely big change — and “out-of-pocket cap” is doing a lot of work.',
    '/enrollment-scams': 'Open enrollment is the one season when unsolicited Medicare contact feels normal. That is what makes it the most profitable weeks of the fraud year.',
    '/falls': 'More than one in four older adults falls each year and fall deaths are up 51% in a decade. The best-supported prevention costs nothing at all.',
    '/free-college': 'Most states let older residents take public-college courses free or cheaply. Rules vary by state, campus, age, and whether you audit or take credit.',
    '/gold-courier-scam': 'The FBI logged about 725 gold-courier frauds in 2025, with $311.8 million lost and 98% of it by people over 60. It ends with a stranger at your door.',
    '/irmaa': 'IRMAA 2026: the Medicare surcharge set by your income from two years ago. The thresholds, why it is a cliff not a slope, and the form that appeals it.',
    '/long-distance': 'Living far from grandchildren changes the mechanics of closeness, not the closeness itself. What has to be built rather than simply absorbed.',
    '/long-term-care': 'What long-term care actually costs in 2026, who pays for it, and what insurance does and does not do. One of the largest risks in retirement.',
    '/medicare-enrollment': 'Miss your Medicare enrollment window without the right coverage and you pay a surcharge every month for life. The seven months that decide it.',
    '/medicare-gaps': 'What Medicare does not cover: teeth, eyes, ears, and the very large one most people do not discover until a parent needs it. Worth knowing early.',
    '/medicare-savings': 'Four Medicare Savings Programs help with premiums and deductibles, plus Extra Help for drug costs. The 2026 income limits are higher than most assume.',
    '/observation-status': 'Observation is a billing status, not a place. Why three hospital nights may not count toward Medicare\'s three-day rule, and the appeal opened in 2025.',
    '/privacy': 'Privacy Policy and Terms for The Second Half Guide: what we collect, the newsletter, advertising cookies, your rights, and the editorial disclaimers.',
    '/property-tax': 'Most states reduce, freeze or defer property taxes at a certain age. Almost none apply it automatically, and the age is lower than people assume.',
    '/senior-age': 'There is no senior birthday. About a dozen unrelated clocks — 50, 55, 59½, 62, 65, 67 — set by different institutions, and only some of them matter.',
    '/no-tax-on-social-security': 'The 2025 law created a $6,000 deduction for people over 65. It did not change how Social Security is taxed — those thresholds are frozen since 1984.',
    '/senior-deduction-phaseout': 'The $6,000 senior deduction shrinks by six cents per dollar above $75,000 single or $150,000 joint, and reaches zero at $175,000. The arithmetic.',
    '/senior-deduction-sunset': 'The $6,000 senior deduction applies to tax years 2025 through 2028 and then ends. What that means for timing a conversion or a sale.',
    '/standard-deduction-65': 'Three separate deductions stack for someone over 65 in 2026: the base, the age-65 addition, and the new $6,000. Together, more than most expect.',
    '/senior-deduction': 'The new $6,000 senior deduction for people 65 and over — temporary, income-limited, and widely misdescribed as “no tax on Social Security.”',
    '/social-security-62': 'Filing for Social Security at 62 cuts your benefit permanently. The arithmetic — the reduction, the break-even, and when filing early still wins.',
    '/social-security-login': 'Your old Social Security username and password no longer work. Nothing went wrong — the sign-in system changed, and getting back in takes 20 minutes.',
    '/voice-cloning': 'The grandparent scam had one reliable flaw: the caller never sounded right. Voice cloning removed it. What still works has nothing to do with the voice.',
    '/wednesday-letters': 'Fiction from The Second Half Guide: twenty-one years of Wednesday mornings at a small-town post office, and the letters that kept on arriving.',
    '/wep-gpo-repeal': 'WEP and GPO cut the Social Security of teachers, firefighters and public employees for decades. Both were repealed, and many affected still don\'t know.',
    '/widows-penalty': 'When one spouse dies, income falls and the tax brackets narrow at the same time. One of the harshest bits of arithmetic in retirement, rarely explained.',
}

PAGE_FILES = {
    'second-half-guide.html': '/',
    'numbers.html': '/numbers',
    'subscribed.html': '/subscribed',
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


def house_promo(target, title, blurb, container):
    """container: the width class the ad slot sat in, or '' if already inside one.

    The promo used to replace the whole slot div, wrapper and all, which left
    the full-width variant with nothing constraining it -- it ran edge to edge
    while every other block on the page was inset. Keep the wrapper.
    """
    open_, close = (f'  <div class="{container}">\n', '  </div>\n') if container else ('', '')
    return (open_
            + f'      <a class="house" href="{target}">\n'
            + f'        <span class="house-label">Also on The Second Half Guide</span>\n'
            + f'        <span class="house-title">{title}</span>\n'
            + f'        <span class="house-blurb">{blurb}</span>\n'
            + f'        <span class="house-more">Read it &rarr;</span>\n'
            + f'      </a>\n' + close)


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
    '/senior-deduction-sunset', '/standard-deduction-65',
    '/no-tax-on-social-security', '/senior-deduction-phaseout',
    '/rmd-deadline', '/medigap-window', '/observation-status', '/irmaa', '/medicare-savings', '/widows-penalty', '/falls', '/wellness-visit',
    '/downsizing-math', '/driving',
    '/gold-courier-scam', '/wep-gpo-repeal', '/social-security-login',
    '/airport-help', '/airport-security', '/passport-traps',
    '/travel-medications', '/cruise-medical', '/the-big-trip',
    '/hearing-aids', '/long-term-care', '/cola',
]
LATEST_SHOWN = 6

# Kit's plain-HTML endpoint, so the form is a normal POST rather than a
# third-party script. The CSP forbids external scripts, and a signup that
# only works with JavaScript enabled is the wrong bet for this audience.
#
# Set this to the numeric form ID from Kit (Grow -> Landing Pages & Forms ->
# your form -> Embed -> HTML). Until it is set the block is left out of the
# build entirely: shipping a form that posts nowhere would collect addresses
# into a void, which is worse than having no form at all.
KIT_FORM_ID = '9792077'
# Kit now serves this on app.kit.com; app.convertkit.com is the older host and
# stays in the CSP so an older form URL would not silently break.
KIT_ENDPOINT = 'https://app.kit.com/forms/%s/subscriptions'

SUBSCRIBE_CSS = """
.signup { border-top: 1px solid var(--line); margin-top: 8px; padding: 40px 0 8px; }
.signup-card {
  background: var(--bg); border: 1px solid var(--line); border-radius: var(--radius);
  padding: 30px 28px;
}
.signup-card h2 { font-size: 1.45rem; margin: 0 0 6px; }
.signup-card p.why { margin: 0 0 20px; color: var(--ink-soft); max-width: 54ch; }
.signup-form { display: flex; flex-wrap: wrap; gap: 12px; align-items: flex-end; }
.signup-field { display: flex; flex-direction: column; gap: 6px; flex: 1 1 260px; }
.signup-field label { font-weight: 700; font-size: 1rem; }
.signup-field input {
  font: inherit; font-size: 1.05rem; padding: 13px 14px; min-height: 52px;
  border: 2px solid var(--line); border-radius: 9px; background: var(--surface);
  color: var(--ink); width: 100%;
}
.signup-field input:focus-visible { outline: 3px solid var(--focus); outline-offset: 1px; }
.signup-form button {
  font: inherit; font-weight: 700; font-size: 1.05rem; min-height: 52px;
  padding: 13px 22px; border: 0; border-radius: 9px; cursor: pointer;
  background: var(--pine-strong); color: #fff; flex: 0 0 auto;
}
.signup-form button:hover { filter: brightness(1.08); }
.signup-form button:focus-visible { outline: 3px solid var(--ink); outline-offset: 2px; }
.signup-fine { margin: 16px 0 0; font-size: 0.95rem; color: var(--ink-soft); }
@media (max-width: 520px) {
  .signup-form button { width: 100%; }
}
@media print { .signup { display: none; } }
"""


def subscribe_block(wide):
    """The Wednesday Letters signup. Returns '' until KIT_FORM_ID is set."""
    if not KIT_FORM_ID:
        return ''
    wrap = 'wrap-wide' if wide else 'wrap'
    return (
        '  <section class="signup" id="letters">\n'
        f'    <div class="{wrap}">\n'
        '      <div class="signup-card">\n'
        '        <h2>Wednesday Letters</h2>\n'
        '        <p class="why">One email, Wednesday mornings: the few things that '
        'changed this week for people in their late fifties and sixties, and what '
        'the numbers actually are. No advice, no hype, no selling your address.</p>\n'
        f'        <form class="signup-form" action="{KIT_ENDPOINT % KIT_FORM_ID}" '
        'method="post">\n'
        '          <div class="signup-field">\n'
        '            <label for="letters-email">Your email address</label>\n'
        '            <input id="letters-email" type="email" name="email_address" '
        'autocomplete="email" required>\n'
        '          </div>\n'
        '          <button type="submit">Send me Wednesday Letters</button>\n'
        '        </form>\n'
        '        <p class="signup-fine">Free. Unsubscribe in one click, any time. '
        'We never sell, rent, or share your address &mdash; see the '
        '<a href="/privacy">privacy policy</a>.</p>\n'
        '      </div>\n'
        '    </div>\n'
        '  </section>\n')


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
            '      <div class="section-head">\n        <h2>Just published</h2>\n'
            '        <p>The newest pieces. Everything stays filed under its topic below &mdash; this is '
            'simply what went up most recently.</p>\n      </div>\n'
            '      <div class="latest-grid">\n' + '\n'.join(cards)
            + '\n      </div>\n    </div>\n  </section>\n')

# The four oldest templates still carried a "Privacy Policy & Terms — coming
# soon" span from before those pages existed, so About/Contact/Privacy were
# unreachable from them. Rather than patch each source, the footer is rebuilt
# here for every page, which also keeps a new link (like /numbers) from having
# to be added in four places.
FOOTER_RE = re.compile(r'<footer>.*?</footer>', re.S)
FOOTER_LINKS = (('/about', 'About'), ('/contact', 'Contact'),
                ('/numbers', 'Useful numbers'), ('/privacy', 'Privacy &amp; Terms'))


def footer_block(cls):
    wrap = 'wrap' if cls == 'hub' else 'wrap-wide'
    links = '\n'.join(f'      <a href="{h}">{t}</a>' for h, t in FOOTER_LINKS)
    return ('<footer>\n'
            f'  <div class="{wrap} foot-grid">\n'
            '    <span>&copy; 2026 The Second Half Guide</span>\n'
            '    <span class="foot-links">\n' + links + '\n    </span>\n'
            '  </div>\n</footer>')


# Search engines have no way to tell that these pages are reported facts with
# a named author and a checked date rather than anonymous filler, which is the
# whole distinction a YMYL site lives or dies on. JSON-LD says it outright.
#
# datePublished is deliberately absent: the builder knows when a page was last
# checked but not when it first went up, and a guessed publication date on a
# site whose selling point is verified numbers would be the one lie on it.
def git_dates():
    """slug path -> first-committed date, so datePublished is a fact not a guess.

    datePublished was deliberately left out when the structured data went in,
    because guessing a date on a site whose selling point is verified numbers
    would have been the one lie on it. The repository knows when each page
    first shipped, so the guess is no longer necessary.
    """
    import subprocess
    root = os.path.dirname(os.path.abspath(SRC_DIR))
    out = {}
    try:
        files = subprocess.run(['git', 'ls-files', '*.html'], cwd=root,
                               capture_output=True, text=True, timeout=30)
        for fn in files.stdout.split():
            r = subprocess.run(['git', 'log', '--diff-filter=A', '--format=%ad',
                                '--date=short', '--', fn],
                               cwd=root, capture_output=True, text=True, timeout=30)
            lines = [l for l in r.stdout.split() if l]
            if lines:
                path = '/' if fn == 'index.html' else '/' + fn[:-5]
                out[path] = lines[-1]
    except Exception:
        pass
    return out


MONTHS = {m: i for i, m in enumerate(
    'January February March April May June July August September October '
    'November December'.split(), 1)}
CHECKED_RE = re.compile(r'Checked against primary sources on (\d{1,2}) (\w+) (\d{4})')

PERSON = {
    '@type': 'Person',
    'name': 'Edward Silva',
    'url': ORIGIN + '/about',
    'image': ORIGIN + '/images/edward.png',
}
PUBLISHER = {
    '@type': 'Organization',
    'name': 'The Second Half Guide',
    'url': ORIGIN + '/',
    'logo': {'@type': 'ImageObject', 'url': ORIGIN + '/og.png',
             'width': 1200, 'height': 630},
}


def json_ld(path, title, desc, canonical, headline, body, published=None):
    cls = layout_class(path)
    if cls == 'hub':
        node = {'@type': 'WebSite', 'name': 'The Second Half Guide',
                'url': ORIGIN + '/', 'description': desc, 'publisher': PUBLISHER,
                'inLanguage': 'en-US'}
    elif cls == 'doc':
        node = {'@type': 'ProfilePage' if path == '/about' else 'WebPage',
                'name': headline, 'url': canonical, 'description': desc,
                'publisher': PUBLISHER, 'inLanguage': 'en-US'}
        if path == '/about':
            node['mainEntity'] = PERSON
    else:
        node = {'@type': 'Article', 'headline': headline[:110], 'url': canonical,
                'description': desc, 'author': PERSON, 'publisher': PUBLISHER,
                'image': ORIGIN + '/og.png', 'inLanguage': 'en-US',
                'isAccessibleForFree': True,
                'mainEntityOfPage': {'@type': 'WebPage', '@id': canonical}}
        if published:
            node['datePublished'] = published
        m = CHECKED_RE.search(re.sub(r'<[^>]+>', ' ', body))
        if m and m.group(2) in MONTHS:
            node['dateModified'] = '%s-%02d-%02d' % (
                m.group(3), MONTHS[m.group(2)], int(m.group(1)))
        node.setdefault('dateModified', published or '')
        if not node['dateModified']:
            del node['dateModified']
    node['@context'] = 'https://schema.org'
    return json.dumps(node, indent=None, separators=(',', ':'), sort_keys=True)


# Utility pages: real destinations for a reader mid-flow, but nothing a
# search engine should index or a sitemap should advertise.
NOINDEX = {'/subscribed'}
ROBOTS = {False: 'index, follow, max-image-preview:large',
          True: 'noindex, follow'}


# The homepage used to state the article count in words, by hand, and it went
# stale the moment anything was published. It is derived from the build now.
ONES = ('zero one two three four five six seven eight nine ten eleven twelve '
        'thirteen fourteen fifteen sixteen seventeen eighteen nineteen').split()
TENS = ('', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy',
        'eighty', 'ninety')


def spell(n):
    """Small integers in words, since the sentence reads better that way."""
    if n < 20:
        w = ONES[n]
    elif n < 100:
        w = TENS[n // 10] + ('-' + ONES[n % 10] if n % 10 else '')
    else:
        return str(n)
    return w[0].upper() + w[1:]


def layout_class(path):
    if path == '/': return 'hub'
    if path in ('/about', '/contact', '/privacy', '/numbers', '/subscribed'): return 'doc'
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
    published = git_dates()

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
        if path != '/':
            title = re.sub(r'\s*(?:&mdash;|\u2014|\|)\s*The Second Half Guide\s*$', '', title)

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

        body, n_foot = FOOTER_RE.subn(footer_block(cls), body)
        assert n_foot == 1, f'{path}: expected one footer, found {n_foot}'

        # The letter is the point of the site's email, so it goes at the end of
        # anything worth reading. Not on the reference pages, where a signup
        # would interrupt someone mid-task looking up a phone number.
        if cls in ('hub', 'article'):
            block = subscribe_block(wide=(cls != 'hub'))
            if block:
                body = body.replace('<footer>', block + '\n<footer>', 1)

        # Allow-list each inline script by hash instead of relaxing script-src.
        for s in re.findall(r'<script(?![^>]*\ssrc=)[^>]*>(.*?)</script>', body, re.S):
            digest = base64.b64encode(hashlib.sha256(s.encode()).digest()).decode()
            script_hashes.add(f"'sha256-{digest}'")

        desc = DESCRIPTIONS.get(path)
        if not desc:
            d = re.search(r'<p class="dek">(.*?)</p>', body, re.S)
            desc = re.sub(r'<[^>]+>', '', d.group(1)).strip() if d else DESCRIPTIONS['/']
        desc = re.sub(r'\s+', ' ', desc)[:300]
        canonical = ORIGIN + path  # '/' keeps its slash, matching the sitemap

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
        n_articles = sum(1 for p_ in rendered if layout_class(p_) == 'article')
        body = body.replace('{{ARTICLE_COUNT}}', spell(n_articles))
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
                slot = m.group(1)
                container = ('wrap-wide' if 'wrap-wide' in slot
                             else 'wrap' if 'wrap' in slot else '')
                return house_promo(target, headline, blurb, container)

            rendered[path] = (title, desc, canonical, AD_SLOT_RE.sub(swap, body))

    styles = (NEW_FONT_FACES + '\n'.join(global_rules) + '\n'
              + '\n'.join(css_blocks) + NORMALIZE + LATEST_CSS + SUBSCRIBE_CSS
              + (HOUSE_CSS if not ADS_LIVE else ''))
    # The stylesheet used to be served as a plain /styles.css. Because the
    # name never changed, a reader whose browser had cached an older copy kept
    # it -- and new markup (the house promos) rendered against old CSS as bare
    # underlined links. Hashing the content into the filename makes a changed
    # stylesheet a different URL, so a stale copy can never be reused.
    css_name = 'styles.%s.css' % hashlib.sha256(
        styles.encode()).hexdigest()[:10]
    open(f'{SITE}/{css_name}', 'w').write(styles)
    # Anyone whose browser cached a page from before the hash existed will
    # still request /styles.css. Serving it keeps those readers styled
    # instead of handing them a 404 and an unstyled page.
    open(f'{SITE}/styles.css', 'w').write(styles)
    open(f'{SITE}/favicon.svg', 'w').write(FAVICON)
    if os.path.exists('ogcard/og.png'):
        shutil.copy('ogcard/og.png', f'{SITE}/og.png')
    if os.path.isdir('images'):
        shutil.copytree('images', f'{SITE}/images')

    for path, (title, desc, canonical, body) in rendered.items():
        ld = json_ld(path, title, desc, canonical, meta[path][0], body,
                     published.get(path))
        # A ld+json data block is not executed, so script-src does not gate it,
        # but hashing it costs nothing and survives a stricter policy later.
        script_hashes.add("'sha256-%s'" % base64.b64encode(
            hashlib.sha256(ld.encode()).digest()).decode())
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
<meta name="robots" content="{ROBOTS[path in NOINDEX]}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preload" href="/fonts/atkinson-400.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/{css_name}">
<script type="application/ld+json">{ld}</script>
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
        # The homepage entry used to be a bare https://host with no path at
        # all. Google tolerates it; the sitemap protocol and stricter
        # validators want a complete URL, so the root keeps its slash.
        f'  <url><loc>{ORIGIN}{p}</loc>'
        + (f'<lastmod>{published[p]}</lastmod>' if p in published else '')
        + f'<changefreq>{"weekly" if p == "/" else "monthly"}</changefreq>'
        f'<priority>{"1.0" if p == "/" else "0.8"}</priority></url>\n'
        for p in sorted(rendered) if p not in NOINDEX)
    open(f'{SITE}/sitemap.xml', 'w').write(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + '</urlset>\n')

    # The wildcard already permits these, but naming them states the intent
    # rather than leaving it to a default: this site wants to be read, quoted
    # and cited by assistants. Being cited as the source of a Medicare figure
    # is worth more to a small publisher than the pageview it might displace.
    AI_AGENTS = [
        'GPTBot', 'OAI-SearchBot', 'ChatGPT-User',           # OpenAI
        'ClaudeBot', 'Claude-Web', 'anthropic-ai',           # Anthropic
        'PerplexityBot', 'Perplexity-User',                  # Perplexity
        'Google-Extended',                                   # Gemini grounding
        'Applebot-Extended', 'Bingbot', 'CCBot', 'Meta-ExternalAgent',
    ]
    robots = ['User-agent: *', 'Allow: /', '',
              '# Assistants and their crawlers are welcome. Every figure here',
              '# is sourced at the foot of the article it appears in.']
    for agent in AI_AGENTS:
        robots += [f'User-agent: {agent}', 'Allow: /', '']
    robots += [f'Sitemap: {ORIGIN}/sitemap.xml', '']
    open(f'{SITE}/robots.txt', 'w').write('\n'.join(robots))

    # llms.txt: an emerging convention pointing a model at the parts of a site
    # worth reading, in the order worth reading them. Cheap, and this site is
    # exactly the shape it was proposed for -- factual reference, plain prose.
    llms = [f'# The Second Half Guide', '',
            '> Smart, practical information for people roughly 55-70 navigating the '
            'financial and lifestyle transition into retirement. Every dollar amount, '
            'age threshold and deadline is checked against the agency that publishes '
            'it, and the sources are listed at the foot of each article.', '',
            'Published by Edward Silva. Not financial, legal, medical or tax advice; '
            'this is a publisher, not an advisor. Figures are stated for the year '
            'named on the page and change annually.', '']
    groups = [
        ('Medicare', ['/medicare-enrollment', '/open-enrollment', '/advantage-vs-original',
                      '/medicare-gaps', '/medicare-savings', '/irmaa', '/observation-status',
                      '/medigap-window', '/drug-cap', '/wellness-visit', '/vaccine-ages']),
        ('Social Security and taxes', ['/social-security-62', '/cola', '/wep-gpo-repeal',
                                       '/widows-penalty', '/senior-deduction', '/rmd-deadline',
                                       '/property-tax', '/social-security-login']),
        ('Fraud and safety', ['/bank-imposter-scam', '/five-minute-rule', '/romance-scams',
                              '/gold-courier-scam', '/voice-cloning', '/enrollment-scams',
                              '/numbers']),
        ('Reference', ['/about', '/senior-age', '/approaching-60']),
    ]
    for name, paths in groups:
        llms.append(f'## {name}')
        for p_ in paths:
            if p_ in meta:
                # llms.txt is plain markdown, so the HTML entities the site
                # stores have to be resolved and the summary cut at a word
                # boundary rather than mid-word at a fixed offset.
                head_ = html_mod.unescape(meta[p_][0])
                sum_ = html_mod.unescape(meta[p_][1])
                if len(sum_) > 160:
                    sum_ = sum_[:160].rsplit(' ', 1)[0] + '…'
                llms.append(f'- [{head_}]({ORIGIN}{p_}): {sum_}')
        llms.append('')
    open(f'{SITE}/llms.txt', 'w').write('\n'.join(llms))

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
           # The signup posts to Kit, so the policy has to name it. Kept to
           # the one host rather than relaxed, so a form injected anywhere on
           # the site still cannot exfiltrate to an attacker's endpoint.
           "form-action 'self'"
           + (' https://app.convertkit.com https://app.kit.com' if KIT_FORM_ID else ''))
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
                # HTML must revalidate or a deploy never reaches anyone who has
                # already visited. Listed here, before the long-cache rules, so
                # those override it for the assets rather than the reverse.
                {"key": "Cache-Control", "value": "public, max-age=0, must-revalidate"},
            ]},
            {"source": "/fonts/(.*)", "headers": [
                {"key": "Cache-Control", "value": "public, max-age=31536000, immutable"}]},
            # Safe to cache forever now that the name carries a content hash:
            # a changed stylesheet is a different URL. The old /styles.css was
            # cached for a week under a fixed name, so readers kept stale CSS.
            {"source": "/styles.(.*).css", "headers": [
                {"key": "Cache-Control", "value": "public, max-age=31536000, immutable"}]},
            {"source": "/images/(.*)", "headers": [
                {"key": "Cache-Control", "value": "public, max-age=86400"}]},
            # The unhashed legacy copy: short cache, since its contents change.
            {"source": "/styles.css", "headers": [
                {"key": "Cache-Control", "value": "public, max-age=300"}]},
        ],
    }
    open(f'{SITE}/vercel.json', 'w').write(json.dumps(vercel, indent=2) + '\n')

    total = sum(os.path.getsize(os.path.join(r, f))
                for r, _, fs in os.walk(SITE) for f in fs)
    print(f'{len(rendered)} pages, {css_name} {len(styles) // 1024}KB, total {total // 1024}KB')
    leftover = [p for p, (_, _, _, b) in rendered.items() if 'claude.ai/code/artifact' in b]
    print('pages still linking to claude.ai:', leftover or 'none')


if __name__ == '__main__':
    main()
