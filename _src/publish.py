#!/usr/bin/env python3
"""Build the site from _src and sync it into the repo root for deployment."""
import os
import shutil
import subprocess
import sys

SRC = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(SRC)
SITE = os.path.join(SRC, 'site')

STATIC_TOOLS = (
    'retirement-strategy-model.html',
    'retirement-strategy-model.css',
    'retirement-strategy-model-header.css',
    'retirement-strategy-model-launch.css',
    'retirement-strategy-model.js',
    'retirement-strategy-model-modes.js',
    'retirement-strategy-model-launch.js',
    'retirement-planner-launch.html',
)
KEEP = {'.git', '.gitignore', '.vercelignore', 'README.md', 'CLAUDE.md', '_src', 'promotion'}

RETIREMENT_ARTICLE_CTAS = {
    'social-security-62.html': ('Run your own 62 vs. 65 vs. 67 numbers', 'Compare the monthly benefit, break-even age, retirement savings and spending gap using your own assumptions.'),
    'delayed-retirement-credit.html': ('See what waiting does to the rest of your retirement', 'Model Social Security timing together with retirement savings, spending and work income.'),
    'spousal-benefits.html': ('Compare claiming ages as a household', 'Use the couple mode to compare 62, 65 and 67 together, then explore mixed claiming ages.'),
    'widows-penalty.html': ('Stress-test the household Social Security decision', 'Compare claiming ages and see why survivor income belongs in the conversation.'),
    'irmaa.html': ('Put Social Security timing into the larger retirement picture', 'Compare claiming ages, retirement income and Medicare timing in one private browser-based model.'),
    'hsa-medicare-timing.html': ('See Social Security and Medicare timing on one screen', 'Use the planner to compare claiming ages while keeping HSA and Part B timing visible.'),
    'medicare-enrollment.html': ('Medicare at 65 does not mean Social Security at 65', 'Compare 62, 65 and 67 while keeping the Medicare timeline separate.'),
    'rmd-deadline.html': ('See how Social Security changes the savings drawdown', 'Compare claiming ages against your retirement spending target and portfolio horizon.'),
    'no-tax-on-social-security.html': ('Run the gross-income tradeoffs first', 'Compare claiming ages and savings drawdown, then use the tax article to interpret the result.'),
    'rule-of-55.html': ('Model the bridge between work and Social Security', 'See what happens if retirement begins before the Social Security age you choose.'),
    'catch-up-60-63.html': ('See what extra contributions can change', 'Advanced mode includes annual contributions and employer match before retirement.'),
}


def run(script):
    r = subprocess.run([sys.executable, script], cwd=SRC, capture_output=True, text=True)
    if r.returncode:
        sys.exit(f'{script} failed:\n{r.stdout}\n{r.stderr}')
    return r.stdout.strip()


def read(path):
    with open(path, encoding='utf-8') as f:
        return f.read()


def write(path, text):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)


def install_static_tools():
    for name in STATIC_TOOLS:
        src = os.path.join(SRC, name)
        if not os.path.exists(src):
            sys.exit(f'missing standalone tool source: {src}')
        shutil.copy2(src, os.path.join(SITE, name))

    vercel = os.path.join(SITE, 'vercel.json')
    cfg = read(vercel)
    if "script-src 'self'" not in cfg:
        cfg = cfg.replace("script-src ", "script-src 'self' ", 1)
    write(vercel, cfg)


def inject_homepage_promotion():
    home = os.path.join(SITE, 'index.html')
    html = read(home)

    feature = '''\n  <div class="wrap">\n    <a class="house" href="/retirement-strategy-model">\n      <span class="house-label">New interactive tool</span>\n      <span class="house-title">The Second Half Retirement Planner: 62 vs. 65 vs. 67</span>\n      <span class="house-blurb">Not just a Social Security check calculator. See what claiming age can do to your monthly income, retirement savings, spending gap, work earnings test and Medicare timeline.</span>\n      <span class="house-more">Run your numbers &rarr;</span>\n    </a>\n  </div>\n'''
    hero_end = '  </section>\n\n  <div class="wrap">\n      <a class="house" href="/airport-help">'
    if 'The Second Half Retirement Planner: 62 vs. 65 vs. 67' not in html and hero_end in html:
        html = html.replace(hero_end, '  </section>\n' + feature + '\n  <div class="wrap">\n      <a class="house" href="/airport-help">', 1)

    latest_marker = '      <div class="latest-grid">\n'
    latest_card = '''        <a class="latest-card" href="/retirement-planner-launch">\n          <span class="latest-kicker">New tool</span>\n          <h3>We built the retirement calculator we wanted to exist</h3>\n          <p>Most calculators stop at the Social Security check. Ours follows the decision into savings, spending, work, couples and Medicare timing.</p>\n        </a>\n'''
    if '/retirement-planner-launch' not in html and latest_marker in html:
        html = html.replace(latest_marker, latest_marker + latest_card, 1)

    money_marker = '<a class="tag-live" href="/delayed-retirement-credit">'
    tool_link = ('<a class="tag-live" href="/retirement-strategy-model">'
                 'Try: The Second Half Retirement Planner &mdash; compare 62, 65 and 67 &rarr;</a>\n            ')
    if 'Try: The Second Half Retirement Planner' not in html and money_marker in html:
        html = html.replace(money_marker, tool_link + money_marker, 1)

    write(home, html)


def inject_article_ctas():
    for filename, (title, blurb) in RETIREMENT_ARTICLE_CTAS.items():
        path = os.path.join(SITE, filename)
        if not os.path.exists(path):
            continue
        html = read(path)
        if 'Run your numbers in The Second Half Retirement Planner' in html:
            continue
        marker = '    <div class="next-up">'
        if marker not in html:
            continue
        cta = f'''    <a class="house" href="/retirement-strategy-model">\n      <span class="house-label">Run your numbers</span>\n      <span class="house-title">{title}</span>\n      <span class="house-blurb">{blurb}</span>\n      <span class="house-more">Run your numbers in The Second Half Retirement Planner &rarr;</span>\n    </a>\n\n'''
        html = html.replace(marker, cta + marker, 1)
        write(path, html)


def inject_persistent_planner_link():
    for filename in os.listdir(SITE):
        if not filename.endswith('.html'):
            continue
        path = os.path.join(SITE, filename)
        html = read(path)
        if 'href="/retirement-strategy-model">Retirement Planner</a>' in html:
            continue
        marker = '<a href="/numbers">Useful numbers</a>'
        if marker in html:
            html = html.replace(marker, '<a href="/retirement-strategy-model">Retirement Planner</a>\n      ' + marker, 1)
            write(path, html)


def inject_discovery():
    sitemap = os.path.join(SITE, 'sitemap.xml')
    xml = read(sitemap)
    nodes = []
    if '/retirement-strategy-model</loc>' not in xml:
        nodes.append('  <url><loc>https://thesecondhalfguide.com/retirement-strategy-model</loc><lastmod>2026-09-10</lastmod><changefreq>monthly</changefreq><priority>0.9</priority></url>\n')
    if '/retirement-planner-launch</loc>' not in xml:
        nodes.append('  <url><loc>https://thesecondhalfguide.com/retirement-planner-launch</loc><lastmod>2026-09-10</lastmod><changefreq>yearly</changefreq><priority>0.7</priority></url>\n')
    if nodes:
        xml = xml.replace('</urlset>', ''.join(nodes) + '</urlset>')
        write(sitemap, xml)

    llms = os.path.join(SITE, 'llms.txt')
    if os.path.exists(llms):
        text = read(llms)
        line = ('\n## Interactive tools\n'
                '- [The Second Half Retirement Planner: Social Security 62 vs. 65 vs. 67]'
                '(https://thesecondhalfguide.com/retirement-strategy-model): '
                'Privacy-first browser calculator comparing claiming ages, retirement savings, spending gaps, work earnings-test effects, couple combinations and Medicare timing.\n')
        if '## Interactive tools' not in text:
            text += line
        write(llms, text)


def install_promotions():
    inject_homepage_promotion()
    inject_article_ctas()
    inject_persistent_planner_link()
    inject_discovery()


def main():
    check = '--check' in sys.argv
    for script in ('build_templates.py', 'build_pages.py', 'build_articles.py', 'build_site.py'):
        out = run(script)
        print(f'  {script}: {out.splitlines()[-1] if out else "ok"}')
    install_static_tools()
    install_promotions()

    built = set()
    for root, _, files in os.walk(SITE):
        for f in files:
            built.add(os.path.relpath(os.path.join(root, f), SITE))

    existing = set()
    for root, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if os.path.join(os.path.relpath(root, ROOT), d).lstrip('./') not in KEEP and d not in KEEP]
        for f in files:
            rel = os.path.relpath(os.path.join(root, f), ROOT)
            if rel.split(os.sep)[0] not in KEEP:
                existing.add(rel)

    added = sorted(built - existing)
    removed = sorted(existing - built)
    print(f'\n{len(built)} files built | +{len(added)} new | -{len(removed)} stale')
    for f in added[:10]:
        print(f'  + {f}')
    for f in removed[:10]:
        print(f'  - {f}')
    if check:
        print('\n--check: nothing written')
        return

    for rel in sorted(built):
        dst = os.path.join(ROOT, rel)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(os.path.join(SITE, rel), dst)
    for rel in removed:
        os.remove(os.path.join(ROOT, rel))
    print('\nsynced to repo root -- commit and push to deploy')


if __name__ == '__main__':
    main()
