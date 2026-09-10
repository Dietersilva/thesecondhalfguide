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
    'retirement-strategy-model.js',
    'retirement-strategy-model-modes.js',
)
KEEP = {'.git', '.gitignore', '.vercelignore', 'README.md', 'CLAUDE.md', '_src'}

def run(script):
    r = subprocess.run([sys.executable, script], cwd=SRC, capture_output=True, text=True)
    if r.returncode:
        sys.exit(f'{script} failed:\n{r.stdout}\n{r.stderr}')
    return r.stdout.strip()

def install_static_tools():
    for name in STATIC_TOOLS:
        src = os.path.join(SRC, name)
        if not os.path.exists(src):
            sys.exit(f'missing standalone tool source: {src}')
        shutil.copy2(src, os.path.join(SITE, name))

    vercel = os.path.join(SITE, 'vercel.json')
    with open(vercel, encoding='utf-8') as f:
        cfg = f.read()
    if "script-src 'self'" not in cfg:
        cfg = cfg.replace("script-src ", "script-src 'self' ", 1)
    with open(vercel, 'w', encoding='utf-8') as f:
        f.write(cfg)

    home = os.path.join(SITE, 'index.html')
    with open(home, encoding='utf-8') as f:
        html = f.read()
    marker = '<a class="tag-live" href="/delayed-retirement-credit">'
    tool_link = ('<a class="tag-live" href="/retirement-strategy-model">'
                 'Try: Retirement Strategy Model &mdash; compare ages 62&ndash;67 &rarr;</a>\n            ')
    if '/retirement-strategy-model' not in html and marker in html:
        html = html.replace(marker, tool_link + marker, 1)
    with open(home, 'w', encoding='utf-8') as f:
        f.write(html)

    sitemap = os.path.join(SITE, 'sitemap.xml')
    with open(sitemap, encoding='utf-8') as f:
        xml = f.read()
    if '/retirement-strategy-model</loc>' not in xml:
        node = ('  <url>\n'
                '    <loc>https://thesecondhalfguide.com/retirement-strategy-model</loc>\n'
                '    <lastmod>2026-09-10</lastmod>\n'
                '  </url>\n')
        xml = xml.replace('</urlset>', node + '</urlset>')
    with open(sitemap, 'w', encoding='utf-8') as f:
        f.write(xml)

    llms = os.path.join(SITE, 'llms.txt')
    if os.path.exists(llms):
        with open(llms, encoding='utf-8') as f:
            text = f.read()
        line = ('\n- [Retirement Strategy Model]'
                '(https://thesecondhalfguide.com/retirement-strategy-model): '
                'Private browser-based Social Security, savings and Medicare timing calculator.\n')
        if 'Retirement Strategy Model' not in text:
            text += line
        with open(llms, 'w', encoding='utf-8') as f:
            f.write(text)

def main():
    check = '--check' in sys.argv
    for script in ('build_templates.py', 'build_pages.py', 'build_articles.py', 'build_site.py'):
        out = run(script)
        print(f'  {script}: {out.splitlines()[-1] if out else "ok"}')
    install_static_tools()

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
    for f in added[:10]: print(f'  + {f}')
    for f in removed[:10]: print(f'  - {f}')
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
