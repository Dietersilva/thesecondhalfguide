# Retirement calculator regression suite

Cross-checks the live `retirement-strategy-model.html`/`.js` page against
`ssa-reference.js` -- an independently written implementation of the same
SSA methodology (AIME/PIA via top-35 wage-indexed earnings and bend points,
early/delayed claiming factors, spousal excess, the earnings test, and the
portfolio projection). The reference is written from SSA rules directly,
not copied from the production file, so a mismatch is a real signal instead
of the same bug reflected back.

`run-regression.js` drives the actual built page with Playwright (not a
mock), sets each scenario's inputs, reads the rendered strategy table, and
diffs it against the reference model's expected output for the same inputs.

## Running it

```bash
# from the repo root
python3 -m http.server 8931 &        # serves the built page
cd _src/tests/regression
NODE_PATH=/path/to/some/node_modules/with/playwright-core node run-regression.js
```

`playwright-core` isn't vendored into the repo; point `NODE_PATH` at any
local install of it (or `npm install playwright-core` in this folder --
just don't commit the resulting `node_modules/`). Chromium's binary path
defaults to `/opt/pw-browsers/chromium-1194/chrome-linux/chrome`; override
with `RSM_CHROME_PATH` if that's not where it lives. `RSM_TEST_URL`
overrides the page URL if you're serving on a different port.

Exit code is 0 only if every scenario passes. `last-run.json` captures the
full per-scenario detail (rendered rows + expected values) after each run.

## What's covered

25 scenarios in `scenarios.js`: single and couple households, a short
(zero-padded) work history, a high earner pinned at the taxable wage cap,
an entered SSA statement override, career-average vs. current-wages
estimation, an expected future raise, an older birth year with FRA = 66,
still working past 62 with earnings-test withholding, staggered spousal
retirement ages, a 10-year spousal age gap, the mixed-household case where
one spouse has a real SSA number and the other is estimated, a low-earning
spouse whose spousal excess applies, portfolio depletion before the
horizon, and reinvesting early Social Security checks instead of spending
them. Later additions cover a pension netted out of the bridge, a staggered couple's
bridge, an already-retired user, mixed claim ages with a birth-date offset, and blank
"same as current pay" inputs.

Each scenario checks monthly SS, annual SS, portfolio at retirement, portfolio at
horizon, the snapshot's bridge cost and ongoing gap at claim ages 62/65/67, and (for
couples) all nine cells of the mixed-claim-age matrix.

## What isn't covered

- The SSA "FRA-year" $1-for-$3 earnings-test rule (as opposed to the
  standard $1-for-$2 rule) is verified at the formula level in
  `ssa-reference.js` against the published SSA rule, but isn't exercised
  end-to-end through the rendered page: the one place the UI surfaces a
  concrete earnings-test dollar figure (`renderEarnings`, the "Working
  while claiming" panel) is hardcoded to age 62, which structurally can
  never be within a year of any possible FRA (65-67). The rule does affect
  the multi-year portfolio projection when someone works and claims early
  in the exact year they reach a fractional FRA, but isolating that
  single-rule effect from decades of compounding wasn't worth the
  fragility it would add here.
- Break-even age display and the cumulative-benefit chart aren't checked
  (the chart renders to an SVG path rather than text, and break-even ages
  are a secondary read of the same underlying cash flows this suite
  already reconciles).
- Federal/state tax, IRMAA, RMDs, Medicare premiums, and detailed survivor
  benefits aren't modeled by the calculator itself, so there's nothing to
  regression-test there.

## History

First built and run 2026-09-29, after a manual code review raised (and the
team fixed separately) the household-wide vs. per-spouse "do you know your
SSA estimate" ambiguity. Initial run: 5/15 passed. All 10 failures were
traced to bugs in the *test harness*, not the production code:

1. Several scenarios set `<select>` fields (`years-worked`, `horizon`) to
   values that don't match any actual `<option>` in the HTML (e.g.
   `years-worked: 18` when the real options are 10/15/20/25/30/35/40+).
   Setting an unmatched value on a native `<select>` leaves it blank, and
   the app read that as its clamped minimum -- silently testing the wrong
   inputs. Fixed by using only valid option values, and `run-regression.js`
   now verifies the value stuck before proceeding.
2. `ssa-reference.js`'s portfolio drawdown loop used a fixed "household
   ready age" as the income checkpoint for the whole retirement horizon,
   instead of re-evaluating benefit eligibility against the *current* loop
   year like the production code's `portfolioForClaim` correctly does.
   This under/overstated the bridge-year gap in couple and
   claim-after-retirement scenarios.
3. `ssa-reference.js` used the person's raw (uncapped) current wages as the
   anchor for projecting past-year earnings, instead of capping at that
   year's own taxable maximum first, as production does. This overstated
   AIME for high earners pinned at the wage cap.

After fixing all three: 15/15 passed, confirming the production
calculation code has not regressed relative to an independent
implementation of the underlying SSA rules.

### 2026-09-29, second pass: rules the first version shared with the calculator

A later outside review found four modeling problems the first suite could not
catch, because the reference had adopted the same conventions as the calculator:
the snapshot bridge ignored pension/other income, started at the first spouse's
retirement instead of when both were retired, spousal excess was reduced from the
receiving spouse's own claim age rather than from when it can start (once the
worker has filed), and an already-passed retirement age triggered withdrawals for
years that had already gone by. Each was reproduced against the old build, fixed,
and the reference was updated to the corrected rule before re-running (20/20).

### 2026-09-29, third pass: earnings-test credit-back

SSA withholds whole checks while someone works before full retirement age (FRA) and,
at FRA, recalculates the benefit as though they had claimed that many months later.
The calculator used to withhold and never credit it back, which made early claiming
while working look much worse than it is (claim-65 vs claim-67 break-even read "about
68" for a worker staying on to 67; it is closer to 80). It now models it:
withholding per person, per working year, using each person's own retirement age;
checks counted in whole months; the settled benefit is PIA times the reduction factor
for `claim age + months withheld / 12`, capped at FRA. It feeds every output.

Conventions stated in `ssa-reference.js` and shared deliberately: a year is a span of
the person's own age, the FRA year is the span ending at FRA (so a person with an
integer FRA of 67 gets the $65,160 / $1-per-$3 rule at 66, which the old code never
reached), and checks in the FRA year are capped at the months left before FRA.

Five new scenarios cover working past FRA, a fractional-FRA year, earnings under the
limit, a couple where only one spouse still works, and invest-early-checks mode.
Pointing the corrected reference at the previous build fails 9 of 25, so the suite
does detect the change. Cross-checked the rule against a published worked example
(filed at 63, $1,500/mo, $35,000 earnings, $23,400 limit: $5,800 withheld, 4 checks).

Still not modeled: SSA's special first-year monthly rule, the earnings test on spousal
excess, and months within a year (earnings are a single annual figure).
