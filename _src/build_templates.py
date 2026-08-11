#!/usr/bin/env python3
"""Expand the font placeholders in *.template.html into the artifact pages.

The five oldest pages are kept as templates carrying ATKINSON_400-style
placeholders inside url(data:font/woff2;base64,...), so 1.5MB of base64 does
not sit in version control five times over. build_site.py strips those
@font-face rules and repoints them at real .woff2 files, so the inlined copy
only matters for previewing a page on its own -- but the expansion step still
has to exist, or the pages simply are not there to collect.

It previously did not exist as a script at all: the expanded .html files were
produced once, by hand, and every later build silently reused them. A fresh
clone of this repo could not rebuild those five pages. This is that step.
"""

import os
import sys

SRC = os.path.dirname(os.path.abspath(__file__))

# placeholder -> the .b64 file holding that face
FONTS = {
    'ATKINSON_400I': 'fonts/atkinson-italic-400.b64',
    'ATKINSON_400': 'fonts/atkinson-normal-400.b64',
    'ATKINSON_700': 'fonts/atkinson-normal-700.b64',
    'FRAUNCES_500I': 'fonts/fraunces-italic-500.b64',
    'FRAUNCES_700': 'fonts/fraunces-normal-700.b64',
}

TEMPLATES = [
    'second-half-guide', 'approaching-60', 'social-security-62',
    'bank-imposter-scam', 'wednesday-letters',
]


def main():
    data = {}
    for name, path in FONTS.items():
        full = os.path.join(SRC, path)
        if not os.path.exists(full):
            sys.exit(f'missing font data: {path}')
        data[name] = open(full).read().strip()

    # ATKINSON_400 is a prefix of ATKINSON_400I, so the longer names have to
    # be substituted first or the italic face gets half-replaced.
    order = sorted(data, key=len, reverse=True)

    for stem in TEMPLATES:
        tpl = os.path.join(SRC, f'{stem}.template.html')
        if not os.path.exists(tpl):
            sys.exit(f'missing template: {stem}.template.html')
        html = open(tpl).read()
        for name in order:
            html = html.replace(name, data[name])
        left = [n for n in data if n in html]
        assert not left, f'{stem}: unexpanded placeholders {left}'
        out = os.path.join(SRC, f'{stem}.html')
        open(out, 'w').write(html)
        print(f'{stem}.html {len(html)}')


if __name__ == '__main__':
    main()
