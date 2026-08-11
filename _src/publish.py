#!/usr/bin/env python3
"""Build the site from _src and sync it into the repo root for deployment.

Vercel serves this repo's root directly, so publishing means: run the three
builders in order, then copy _src/site/ over the root. Doing that by hand was
how a stale styles.css and a half-copied build got shipped before, so it lives
in one command instead.

    python3 _src/publish.py          # build and sync
    python3 _src/publish.py --check  # build only, report what would change

Run it from anywhere; paths resolve relative to this file.
"""

import os
import shutil
import subprocess
import sys

SRC = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(SRC)
SITE = os.path.join(SRC, 'site')

# Everything the build owns. Anything in the repo root that is not one of
# these (and not in KEEP) is a file the build no longer produces, so it is
# removed -- otherwise a renamed page lingers as a ghost URL that Google keeps.
KEEP = {'.git', '.gitignore', '.vercelignore', 'README.md', 'CLAUDE.md', '_src'}


def run(script):
    r = subprocess.run([sys.executable, script], cwd=SRC,
                       capture_output=True, text=True)
    if r.returncode:
        sys.exit(f'{script} failed:\n{r.stdout}\n{r.stderr}')
    return r.stdout.strip()


def main():
    check = '--check' in sys.argv
    for script in ('build_templates.py', 'build_pages.py',
                   'build_articles.py', 'build_site.py'):
        out = run(script)
        print(f'  {script}: {out.splitlines()[-1] if out else "ok"}')

    built = set()
    for root, _, files in os.walk(SITE):
        for f in files:
            built.add(os.path.relpath(os.path.join(root, f), SITE))

    existing = set()
    for root, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if os.path.join(
            os.path.relpath(root, ROOT), d).lstrip('./') not in KEEP
            and d not in KEEP]
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
