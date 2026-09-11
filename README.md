# The Second Half Guide

Static site source and generated output for TheSecondHalfGuide.com.

## Retirement Strategy Model

The feature branch `feature/retirement-strategy-model` contains the privacy-first browser calculator at `/retirement-strategy-model`.

Its main public comparison is Social Security claiming at ages 62, 65, and 67. The model includes single/couple inputs, SSA-style benefit estimation, retirement-account growth and withdrawals, earnings-test effects, Medicare timing, and optional detailed assumptions.

Protected Vercel previews preserve the `_vercel_share` token across same-origin navigation so the header, search, home, and category links continue to work inside a shared preview. Production navigation is unchanged.

For the calculator, canonical source lives under `_src/`; the published root copies are kept in sync on the feature branch.
