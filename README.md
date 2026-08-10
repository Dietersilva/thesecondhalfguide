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
index.html, about.html, privacy.html, …   24 articles + 4 site pages
styles.css                                one shared stylesheet
fonts/*.woff2                             self-hosted, no third-party requests
sitemap.xml, robots.txt, favicon.svg
vercel.json                               headers + clean URLs
_src/                                     generators (excluded via .vercelignore)
```

## Regenerating

```
cd _src
python3 build_pages.py <about-url> <contact-url> <privacy-url>
python3 build_articles.py <same three urls>
python3 build_site.py
```

`build_site.py` writes the shared stylesheet, decodes fonts to `fonts/*.woff2`,
rewrites cross-links to root-relative paths, and regenerates `sitemap.xml`,
`robots.txt` and `vercel.json`.

## Editorial rules

- Facts with a date, a number or a threshold. Not "should you do X with your money".
- Every rule-sensitive figure carries a check date and links to a primary source.
- No invented people or composite characters. Reader stories run with permission.
- Ads are labelled; advertisers have no say in what gets written.

## When AdSense is added

`script-src` currently allow-lists one inline script by SHA-256 hash (the topic
form's mailto builder). Adding AdSense means widening `script-src`, `frame-src`
and `img-src` for Google's domains — change that in `build_site.py` deliberately
rather than removing the policy.
