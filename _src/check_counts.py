#!/usr/bin/env python3
"""Fail the build if a displayed article count disagrees with what is actually linked.

Checks _src/site after build_site.py:
  * each topic hub's "N pieces" equals the number of article links on that hub;
  * the homepage "N pieces published so far" equals the number of article pages built;
  * every article link on a hub resolves to a built page.
"""
import glob, os, re, sys

SITE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'site')
HUBS = ('medicare', 'money', 'paperwork', 'fraud', 'aging', 'travel', 'family')
WORDS = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
         'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']


def read(p):
    with open(p, encoding='utf-8') as f:
        return f.read()


def number(text):
    text = text.strip().lower()
    if text.isdigit():
        return int(text)
    return WORDS.index(text) if text in WORDS else None


problems = []
for hub in HUBS:
    t = read(os.path.join(SITE, hub + '.html'))
    m = re.search(r'(\d+) pieces?\b', t)
    links = re.findall(r'<a class="topic-link" href="(/[a-z0-9-]+)"', t)
    if not m:
        problems.append(f'/{hub}: no "N pieces" count found')
        continue
    if int(m.group(1)) != len(links):
        problems.append(f'/{hub}: says {m.group(1)} pieces but links {len(links)}')
    for href in links:
        if not os.path.exists(os.path.join(SITE, href.lstrip('/') + '.html')):
            problems.append(f'/{hub}: links to {href}, which is not built')

# The planner's launch page is installed by publish.py, not built by build_site.py, so the
# homepage sentence has never counted it.
NOT_COUNTED = {'retirement-planner-launch'}
articles = [p for p in glob.glob(os.path.join(SITE, '*.html'))
            if os.path.basename(p)[:-5] not in NOT_COUNTED and re.search(r'<body[^>]*class="[^"]*\barticle\b', read(p))]
home = read(os.path.join(SITE, 'index.html'))
m = re.search(r'>\s*([A-Za-z0-9-]+) pieces published so far', home)
if not m:
    problems.append('homepage: no "pieces published so far" sentence found')
else:
    shown = m.group(1)
    shown_n = number(shown)
    if shown_n is None:  # tens/twenty-one style spelled numbers: compare to the spelled form
        TENS = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
        n = len(articles)
        spelled = (TENS[n // 10] + ('-' + WORDS[n % 10] if n % 10 else '')) if 20 <= n < 100 else str(n)
        if shown.lower() != spelled:
            problems.append(f'homepage: says "{shown}" pieces, {len(articles)} article pages built')
    elif shown_n != len(articles):
        problems.append(f'homepage: says {shown_n} pieces, {len(articles)} article pages built')

if problems:
    sys.exit('Count check failed:\n  ' + '\n  '.join(problems))
print(f'counts ok: {len(articles)} articles, {len(HUBS)} hubs')
