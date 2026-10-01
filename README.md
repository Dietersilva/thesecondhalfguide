# thesecondhalfguide.com

Plain-language facts for the years after 55. Static site — no framework, no
build step, no server-side code. Vercel serves these files directly.

## Vercel project settings

- **Root Directory:** *(leave blank — the site is at the repo root)*
- **Framework Preset:** Other
- **Build Command / Output Directory:** *(none)*

`vercel.json` sets `cleanUrls` (so `/about` serves `about.html`) and the
security headers: HSTS, a strict Content-Security-Policy, `nosniff`,
`Referrer-Policy`, `Permissions-Policy` and frame denial.

## Layout

```
index.html, about.html, etias.html, …      built pages: articles, category hubs, site pages
styles.<hash>.css                          the one shared stylesheet (content-hashed filename);
                                           styles.css is a short-cache legacy copy -- leave it
fonts/*.woff2                              self-hosted, no third-party requests
retirement-strategy-model.*                hand-authored calculator, copied verbatim by publish.py
sitemap.xml, robots.txt, llms.txt          generated
vercel.json                                generated: headers, CSP script hashes, clean URLs
_src/                                      sources, generators and tests (excluded via .vercelignore)
```

## Regenerating

```
python3 _src/publish.py --check    # build, report what would change, write nothing
python3 _src/publish.py            # build and sync into the repo root
```

`publish.py` runs the four builders in order (templates, pages, articles, site),
then installs the hand-authored calculator files. `build_site.py` writes the shared
stylesheet, decodes fonts, rewrites cross-links, and regenerates the sitemap,
`robots.txt`, `llms.txt` and `vercel.json`. `CLAUDE.md` has the full operating notes.

The calculator has an independent regression suite: `_src/tests/regression/README.md`.

## Editorial rules

- Facts with a date, a number or a threshold. Not "should you do X with your money".
- Every rule-sensitive figure carries a check date and links to a primary source.
- No invented people or composite characters. Reader stories run with permission.
- Ads are labelled; advertisers have no say in what gets written.

## Content Security Policy

`script-src` allow-lists each inline script by SHA-256 hash; `build_site.py`
computes the hashes and writes them into `vercel.json`. There are no external
scripts beyond the analytics hosts it names, and no `unsafe-inline`. Adding AdSense
(see `ADS_LIVE` in `build_site.py`) means widening `script-src`, `frame-src` and
`img-src` for Google's domains -- do that deliberately rather than loosening the policy.
