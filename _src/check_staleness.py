#!/usr/bin/env python3
"""Lists articles whose 'recheck' due date has arrived.

Most articles on this site are evergreen and carry no 'recheck' field at
all -- that's the default, meaning "not due." A handful of articles are
tied to a specific future event (an official number landing, a rule taking
effect, an annual reset) and carry a 'recheck' dict instead:

    'recheck': {'due': '2026-10-14', 'why': 'Official SSA COLA announcement'},

This script is the whole mechanism: no scheduler, no separate infra. It's
meant to run as one extra step at the start of the existing Friday
drafting routine, before the news sweep -- see CLAUDE.md section 6 (once
that section documents it) or the routine's own prompt. Run it directly
with:

    python3 _src/check_staleness.py
"""
import datetime
import importlib
import sys


def main():
    import build_articles
    build_articles._load_batches()
    today = datetime.date.today()

    due = []
    for slug, a in build_articles.ARTICLES.items():
        recheck = a.get('recheck')
        if not recheck:
            continue
        due_date = datetime.date.fromisoformat(recheck['due'])
        if due_date <= today:
            due.append((due_date, slug, recheck['why']))

    due.sort()

    if not due:
        print(f'Nothing due for a recheck as of {today.isoformat()}.')
        return

    print(f'{len(due)} article(s) due for a recheck as of {today.isoformat()}:\n')
    for due_date, slug, why in due:
        overdue = '' if due_date == today else f' ({(today - due_date).days} days overdue)'
        print(f'  /{slug}  --  due {due_date.isoformat()}{overdue}')
        print(f'    {why}\n')


if __name__ == '__main__':
    main()
