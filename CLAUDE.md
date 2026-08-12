# The Second Half Guide — operating notes

Read this before touching anything. It is the accumulated result of a lot of
decisions that are not obvious from the code, and several that were made by
getting them wrong first.

**thesecondhalfguide.com** — a static site for readers roughly 55–70.
Author and owner: **Edward Silva**. Deployed on Vercel from `main`; every push
to `main` goes live within a minute or two.

---

## 1. The editorial rule, which decides most arguments

> **A 55+ lifestyle page. Not an advice page. Facts people need to know as
> they near 60.**

This is the owner's own framing and it is the single most useful test:

- **Keep** a piece that states a fact with a **date, a number, or a
  threshold**. "The 2026 Part D out-of-pocket cap is $2,100." "You get seven
  months around your 65th birthday and missing it costs you permanently."
- **Cut** a piece that weighs "should you do X with your money." Those are
  advisor essays. They need credentials the site does not have, they age badly,
  and they are the exact genre this site exists as an alternative to.

A useful phrasing of the difference: *report the rule, not the decision.*
`/social-security-62` is the edge case — it survives because it is
overwhelmingly arithmetic, not counsel.

Related and load-bearing: **the site is a publisher, not an advisor.** Edward
is a computer professional of 40+ years, not a CFP, attorney, or licensed
agent. Never write anything that reads as personalized advice. The disclaimers
on `/about` and `/privacy` say this explicitly; do not undercut them.

### Why this matters more than it looks

Every topic here is **YMYL** (Your Money or Your Life) — Medicare, Social
Security, taxes, fraud. Google holds these to its highest quality bar and the
author has no professional credential to lean on. Verifiable facts with cited
sources are the entire defense. Give that up and there is no site.

---

## 2. Verification — the part that is actually the product

Every load-bearing number gets checked against the issuing agency before it is
written. Not "it sounds right," not "another site says so."

**Known limitation:** in this sandbox, outbound requests to `medicare.gov`,
`ssa.gov`, `irs.gov`, `cdc.gov` and similar are blocked at the proxy, so you
cannot fetch a primary source directly. `WebSearch` works. So verification in
practice means: search, and require **agreement across independent results
that trace back to the agency**. Where results conflict or are thin, say so in
the copy or leave the number out. Do not split the difference.

Two rules learned the hard way:

- **Never "correct" a URL by pattern.** A CMS link reading
  `2026-medicare-parts-b-premiums-deductibles` was "normalized" to
  `...premiums-and-deductibles` because that matched their historical scheme.
  The new form was a 404 and it broke a working link across three articles.
  **If you did not verify the replacement resolves, do not change the link.**
- **Never bulk find-and-replace across text without masking URLs and `href`
  values.** A "corrected" word inside a link is a dead link. When the British
  spellings were fixed, all 171 external URLs were diffed before and after to
  prove none moved.

If a number cannot be confirmed, **omit it**. `/numbers` deliberately has no
FTC phone number for exactly this reason and points at `reportfraud.ftc.gov`
instead. On a page whose promise is "this is safe to call," an unverified
entry is worse than a missing one.

Every article carries **"Checked against primary sources on <date>"**. That
line has to stay true.

---

## 3. Voice

Written for a smart adult who is not stupid and is not a child. Specifically:

- Plain, declarative, unhurried. Short sentences do the heavy lifting.
- **Never** patronize. No "as we age," no "seniors should remember to," no
  cheerleading about how sixty is the new forty.
- Lead with the fact. The reader's time is the scarcest thing in the exchange.
- Concrete beats abstract every time: `$2,100`, `15 October`, `seven months`.
- A dry, humane aside is welcome. Jokes at the reader's expense are not.
- Second person is fine. Hedging stacked three deep is not.
- **American English.** This matters and has bitten before: 189 British
  spellings had to be removed, including *enrolment* 41 times on a site about
  Medicare **enrollment**. Watch for: enrollment, program, curb, license,
  center, judgment, aging, traveling, gray, skeptical, specialty, fall (not
  autumn), line (not queue), elevator (not lift).

Two lines of the site's own copy that set the register:

> "Smart, practical information for people roughly 55–70."
> "What nobody tells you about the 10 years surrounding retirement."

**Length:** 1,050–1,350 words. Below ~900 it reads thin; above ~1,500 it stops
being the thing this site is.

**Structure that works:** hook → what actually changes → a fact table → the
part nobody mentions → what to do about it. Most articles carry a
`facts()` table and several carry a `check()` list; see `_src/build_articles.py`.

---

## 4. How the site is built

The repo root **is** the deployed site. Vercel serves it statically. Sources
live in `_src/`, which `.vercelignore` keeps out of the deployment.

```bash
python3 _src/publish.py --check   # build, report what would change
python3 _src/publish.py           # build and sync into the repo root
git add -A && git commit && git push   # deploy
```

`publish.py` runs four builders in order:

| script | produces |
|---|---|
| `build_templates.py` | expands font placeholders in the five `*.template.html` pages |
| `build_pages.py` | About, Contact, Privacy, Numbers, Subscribed |
| `build_articles.py` | every article, from `articles_batch2..8.py` |
| `build_site.py` | assembles `_src/site/`: one stylesheet, heads, sitemap, headers |

**Adding an article:** append a dict to the newest `articles_batch*.py`, then
run `publish.py`. Add a `DESCRIPTIONS` entry in `build_site.py`, and add the
slug to `LATEST` (newest first) so it appears under "Just published". Add to
`PROMO_POOL` only if it has broad appeal.

### Things in the build that will bite you

- **CSS is scoped by body class.** Every page brought its own `<style>`, and
  several defined `.wrap` at different widths; concatenating them let the last
  definition win everywhere and silently broke the homepage layout. Rules are
  now scoped under `body.hub` / `body.doc` / `body.article`. Only `:root`,
  `*`, `html` and `@font-face` stay global. Do not add unscoped rules.
- **The stylesheet filename carries a content hash.** It used to be a fixed
  `/styles.css` cached for a week, so returning readers kept stale CSS and new
  markup rendered unstyled. The hashed name is what pages link to. A copy is
  also written to the old `/styles.css` path on a five-minute cache, purely so
  browsers still holding pre-hash HTML get a working stylesheet instead of a
  404 — do not remove it, and do not link pages at it.
- **The footer is generated for every page** in `build_site.py`. Do not hand-
  edit footers; four pages once drifted to "Privacy Policy — coming soon" and
  lost their links to About, Contact and Privacy entirely.
- **CSP allow-lists inline scripts by SHA-256 hash.** No external scripts, no
  `unsafe-inline`. `form-action` names Kit's endpoint only. If you add an
  inline script it is hashed automatically; if you add an external one it will
  be blocked, and that is deliberate.
- **Cache headers are order-sensitive.** Vercel applies later matching header
  rules over earlier ones, so the catch-all `Cache-Control` must stay listed
  before the long-cache rules for fonts, the hashed stylesheet and images —
  otherwise it overrides them and every asset revalidates on every visit.
- **`ADS_LIVE = False`.** Ad slots currently render house promos for other
  articles. Flip to `True` only once AdSense is approved.
- **`KIT_FORM_ID` is set** and the Wednesday Letters signup is live on the
  homepage and every article. It posts to Kit's plain-HTML endpoint, not their
  JavaScript embed, because the CSP forbids external scripts. Leave the value
  alone; setting it to None silently removes the signup everywhere.

---

## 5. What is already covered

Do not duplicate these. Check the list before proposing a topic.

- `/advantage-vs-original` — Advantage or Original: what actually differs
- `/aging-in-place` — Aging in place: staying home is a goal, not a plan
- `/airport-help` — The airport help you're entitled to
- `/airport-security` — Airport security after 75, and PreCheck
- `/approaching-60` — What actually changes approaching 60
- `/bank-imposter-scam` — The call that empties bank accounts
- `/beneficiary-form` — Your beneficiary form may outrank your will
- `/cola` — The COLA: why a raise doesn't feel like one
- `/cruise-medical` — Getting sick on a cruise
- `/digital-estate` — Who gets your digital life
- `/downsizing-math` — Downsizing: the arithmetic people skip
- `/driving` — The driving conversation
- `/drug-cap` — The $2,100 drug cap
- `/enrollment-scams` — Why your phone rings more in October
- `/falls` — Falls: the numbers, and what reduces them
- `/five-minute-rule` — Why scammers need you to act right now
- `/free-college` — Free college classes after 60
- `/go-go-years` — The "go-go years" are real, not a deadline
- `/gold-courier-scam` — When the scammer sends someone to your door
- `/hearing-aids` — What the over-the-counter rule changed
- `/irmaa` — The Medicare surcharge set by your income from two years ago
- `/observation-status` — Observation vs. admitted, and the three-day rule
- `/long-distance` — The new long-distance grandparent
- `/long-term-care` — Long-term care: the numbers
- `/medicare-enrollment` — The deadline that never forgives you
- `/medicare-gaps` — What Medicare doesn't cover
- `/medicare-savings` — The help millions qualify for and never claim
- `/numbers` — The numbers worth keeping by the phone (printable)
- `/on-call` — Being available without being on call
- `/open-enrollment` — What the 15 October window is for
- `/parks-pass` — The National Parks Senior Pass
- `/passport-traps` — Passport rules that turn people away
- `/power-of-attorney` — For while you're still here
- `/property-tax` — The break you might already qualify for
- `/romance-scams` — Intelligence was never the issue
- `/senior-age` — When does "senior" actually start?
- `/senior-deduction` — The new $6,000 senior deduction
- `/social-security-62` — Filing at 62, by the arithmetic
- `/social-security-login` — Locked out of your SSA account
- `/the-big-trip` — The big trip, done right
- `/travel-insurance` — What are you actually buying?
- `/travel-medications` — Flying with medications and equipment
- `/vaccine-ages` — The vaccine schedule nobody hands you
- `/voice-cloning` — When the voice sounds like your grandchild
- `/wellness-visit` — The free Medicare visit almost nobody uses
- `/wep-gpo-repeal` — The pension rule that cut your benefit is gone
- `/widows-penalty` — The widow's penalty
- `/wednesday-letters` — Reader correspondence

### Known gaps, roughly in priority order

1. **The Medigap 6-month window** — one-time guaranteed issue; after it
   closes, insurers may underwrite or refuse.
2. **RMDs and QCDs** — 31 December deadline, age 73 or 75 by birth year, and
   the QCD route at 70½.

**Seasonality:** Medicare Annual Enrollment runs **15 October – 7 December**.
That is when this vertical's advertising money exists. Anything meant to earn
that traffic must be published and indexed *well before* mid-October.

---

## 6. House rules for automated runs

The Friday routine **drafts; it does not publish.** Work goes to a branch and
a pull request, never to `main`. Reasons, in order:

1. **Google's scaled-content-abuse policy** targets mass-produced content
   published without meaningful human review. The penalty is not a weak
   article, it is deindexing the domain.
2. **YMYL.** One wrong threshold published unreviewed discredits the other
   forty-six pages.
3. **AdSense is not approved yet.** Unreviewed volume arriving during review
   is a rejection risk.
4. **Primary sources are unreachable from here** (see §2). Human review is
   what keeps the "checked against primary sources" line honest.

So: **2–3 pieces per run**, each one fully built and verified, pushed to a
branch. Vercel builds a preview URL for the branch automatically, so the
owner can read them as they will actually look before merging.

Do not merge to `main`. Do not flip `ADS_LIVE`. Do not change prices,
thresholds, or the privacy policy without saying so prominently in the PR
description — the privacy policy is with an attorney.
