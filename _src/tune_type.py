import re, glob

FILES = ['second-half-guide.template.html', 'build_pages.py', 'build_articles.py',
         'approaching-60.template.html', 'social-security-62.template.html',
         'bank-imposter-scam.template.html', 'wednesday-letters.template.html']

def set_prop(css, selector, prop, value):
    """Change one property inside one selector block."""
    m = re.search(re.escape(selector) + r'\s*\{', css)
    if not m: return css, 0
    start = m.end(); depth = 1; i = start
    while i < len(css) and depth:
        if css[i] == '{': depth += 1
        elif css[i] == '}': depth -= 1
        i += 1
    block = css[start:i]
    new, n = re.subn(rf'{prop}\s*:\s*[^;]+;', f'{prop}: {value};', block, count=1)
    return css[:start] + new + css[i:], n

# Display type comes down; reading text stays generous.
EDITS = [
    ('body', 'line-height', '1.6'),
    ('h1', 'font-size', 'clamp(34px, 4.6vw, 48px)'),      # hub hero
    ('.hero-sub', 'font-size', '20px'),
    ('.dek', 'font-size', '20px'),
    ('.note p', 'font-size', '21px'),
    ('blockquote.pull p', 'font-size', '20px'),
    ('.section-head h2', 'font-size', 'clamp(26px, 3vw, 32px)'),
]

for fn in FILES:
    try: s = open(fn).read()
    except FileNotFoundError: continue
    total = 0
    for sel, prop, val in EDITS:
        s, n = set_prop(s, sel, prop, val); total += n
    # article h1 uses its own clamp; hub h1 already handled above
    s2, n = re.subn(r'clamp\(34px, 5vw, 48px\)', 'clamp(30px, 4.2vw, 42px)', s)
    s = s2; total += n
    open(fn, 'w').write(s)
    print(f'{fn:38} {total} edits')
