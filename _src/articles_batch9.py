#!/usr/bin/env python3
"""Ninth batch: three facts for people leaving work before 65."""

from build_articles import facts, check, AD_INLINE

ARTICLES9 = {}

# Verified 18 August 2026, separately from the shared CHECKED constant used
# by earlier batches -- these three are newly researched, not carried
# forward, and the date should say so rather than borrow an older one.
CHECKED9 = '18 August 2026'

# ------------------------------------------------------------- ACA subsidy cliff
ARTICLES9['aca-subsidy-cliff'] = {
    'title': 'The ACA Subsidy Cliff Is Back in 2026 &mdash; The Second Half Guide',
    'eyebrow': 'Facts &amp; thresholds',
    'h1': 'The ACA subsidy cliff is back in 2026',
    'dek': 'The extra help that capped marketplace premiums at 8.5% of income expired at the end of '
           '2025. For anyone retiring before 65 and buying their own coverage, that changes the math.',
    'meta': '6 minute read &middot; Verified against KFF and Congress.gov figures',
    'checked': CHECKED9,
    'body': """      <p>If you plan to leave work before 65 and buy health coverage on the ACA marketplace to bridge
      the gap to Medicare, a rule that mattered to that plan changed at the start of this year — and it
      changed quietly enough that a lot of people who are already covered do not know about it yet.</p>

      <p>From 2021 through 2025, enhanced premium tax credits did two things: they made existing subsidies
      larger, and they extended subsidies for the first time to people earning <em>above</em> 400% of the
      federal poverty level, capping what anyone paid for a benchmark plan at 8.5% of income regardless of
      how high that income was. That second part is what eliminated the old "subsidy cliff," where
      crossing 400% of poverty meant losing help entirely, all at once.</p>

      <p>Those enhanced credits expired on schedule at the end of 2025. Congress did not extend them —
      competing proposals stalled in the Senate in December — and as of this writing several bills remain
      under discussion with nothing enacted. The cliff is back.</p>

""" + facts('What changed at the start of 2026', [
        ('The cliff, restored', 'Income above 400% of the federal poverty level now loses ACA premium '
                                'tax credits entirely, not gradually.'),
        ('Enrollees are paying more, on average', 'KFF found the average net premium payment across '
                                                  '<em>all</em> marketplace enrollees, subsidized or not, '
                                                  'rose about 58% &mdash; from $113 to $178 a month.'),
        ('The steeper estimate, for one group', 'For people who were receiving subsidies in 2025 and keep '
                                                'the identical plan in 2026, KFF estimates the increase '
                                                'at about 114% on average &mdash; roughly $888 a year to '
                                                'roughly $1,904. Many enrollees are instead switching to '
                                                'cheaper plans, which is part of why the increase across '
                                                'everyone is smaller than that figure.'),
        ('Who is affected most', 'People with incomes just above 400% of poverty, a group that made up '
                                 'a small share of 2025 enrollment but a large share of the drop in '
                                 'sign-ups this year.'),
        ('400% of poverty, in dollars', 'Roughly $62,600 for a single person and $84,600 for a couple in '
                                        'the 48 contiguous states. Marketplace eligibility for 2026 '
                                        'coverage is measured against the <strong>2025</strong> poverty '
                                        'guidelines, not the newer 2026 ones &mdash; using the wrong '
                                        'year’s table is an easy way to get this number wrong. Check your '
                                        'own household size on HealthCare.gov, and confirm which year’s '
                                        'guideline it is using.'),
        ('The repayment cap is also gone', 'Starting with the 2026 tax year, if you received more advance '
                                           'premium tax credit than you turned out to qualify for, there '
                                           'is <strong>no cap</strong> on what you repay at tax time. '
                                           'Through 2025 the repayment was capped at a few hundred to a '
                                           'few thousand dollars depending on income; that cap is gone for '
                                           '2026 returns, at every income level.'),
    ]) + """
      <h2>Why this lands on this site's readers specifically</h2>

      <p>Marketplace coverage is disproportionately used by people who have left a job before 65 and are
      not yet eligible for Medicare — retired early, laid off, self-employed, or covering the gap after a
      spouse's employer coverage ends. That is a specific, common situation in the years right before
      Medicare, and it is exactly the population this change affects.</p>

      <p>It also interacts with a decision a lot of people make deliberately: keeping reported income low
      in the years before Medicare, often by living off savings rather than taxable withdrawals, partly
      <em>because</em> it used to maximize ACA subsidies. That strategy still works below 400% of poverty —
      it is worth more now, not less, since the credit at that income level still exists and unsubsidized
      premiums have risen too. It is the plan to hold income <em>just over</em> the line, or to not think
      about the line at all, that got considerably more expensive this year.</p>

""" + AD_INLINE + """
      <h2>What to actually check</h2>

""" + check([
        'Find your <strong>household size and estimated 2026 income</strong> in dollars, then compare it '
        'to 400% of the federal poverty line for that household size &mdash; not last year’s income, '
        'this year’s estimate.',
        'If your household income for the year comes in <strong>above the applicable 400% threshold</strong>, '
        'the premium tax credit is not available for that year &mdash; it is a cliff, not a slope, the same '
        'shape as the Medicare IRMAA surcharge described elsewhere on this site.',
        'Income from <strong>IRA withdrawals, Roth conversions and realized capital gains</strong> all count '
        'toward the household income used to determine eligibility. Anyone considering one of these '
        'transactions specifically because of its effect on marketplace eligibility should check the full '
        'tax consequences with a qualified tax professional first &mdash; this page reports the rule, not '
        'the strategy.',
        'Because the <strong>repayment cap is gone for 2026</strong>, an income estimate that turns out too '
        'low is a bigger risk than in past years &mdash; there is no longer a ceiling on what you would owe '
        'back. If your income might come in higher than what you told the marketplace, update your '
        'application during the year rather than waiting for tax time.',
        'Re-check your plan during <strong>open enrollment</strong> even if nothing else about your life '
        'changed &mdash; the subsidy math changed under you, and the plan that made sense in 2025 may not '
        'be the best value in 2026.',
        'Watch for legislation. Proposals to restore some version of the enhanced credits have been '
        'introduced; none had passed as of this writing. If that changes, it changes the numbers on this '
        'page, and we will update it.',
    ]) + """
      <p>None of this is a reason to avoid marketplace coverage, and it is not advice about what your
      household should do — your income, your state, and your health all change the answer. It is a
      reason to run the actual numbers for your own household before you assume the plan you had last year
      still costs what it used to.</p>
""",
    'sources': [
        ('KFF &mdash; A Steep Subsidy Cliff Looms for Older Middle-Income Enrollees',
         'https://www.kff.org/quick-take/a-steep-subsidy-cliff-looms-for-older-middle-income-enrollees-if-aca-enhanced-tax-credits-expire/'),
        ('KFF &mdash; ACA Marketplace Premium Payments Would More than Double on Average',
         'https://www.kff.org/affordable-care-act/aca-marketplace-premium-payments-would-more-than-double-on-average-next-year-if-enhanced-premium-tax-credits-expire/'),
        ('Congressional Research Service &mdash; Enhanced Premium Tax Credit and 2026 Exchange Premiums',
         'https://www.congress.gov/crs-product/R48290'),
        ('HealthCare.gov &mdash; Federal poverty level (FPL)',
         'https://www.healthcare.gov/glossary/federal-poverty-level-fpl/'),
        ('IRS &mdash; Fact Sheet 2025-10, Premium Tax Credit questions and answers',
         'https://www.irs.gov/newsroom/irs-updates-frequently-asked-questions-on-the-premium-tax-credit'),
        ('KFF &mdash; What We Know So Far About 2026 ACA Marketplace Enrollment, Premiums, and Deductibles',
         'https://www.kff.org/affordable-care-act/what-we-know-so-far-about-2026-aca-marketplace-enrollment-premiums-and-deductibles/'),
    ],
    'next': {'slug': 'rule-of-55',
             'title': 'The Rule of 55: what it actually covers',
             'blurb': 'One way to fund the years between leaving work and Medicare without a 10% penalty.'},
}

# --------------------------------------------------------------------- Rule of 55
ARTICLES9['rule-of-55'] = {
    'title': 'The Rule of 55: What It Actually Covers &mdash; The Second Half Guide',
    'eyebrow': 'Facts &amp; thresholds',
    'h1': 'The Rule of 55: what it actually covers',
    'dek': 'Leave a job at 55 or later and you may be able to tap that employer’s 401(k) without the '
           'usual 10% penalty. The exceptions are where people get tripped up.',
    'meta': '5 minute read &middot; Verified against IRS guidance',
    'checked': CHECKED9,
    'body': """      <p>Withdraw from a 401(k) before 59&frac12; and the IRS normally adds a 10% penalty on top of the
      ordinary income tax. The Rule of 55 is a specific, named exception to that penalty — not a way
      around taxes, just around the extra 10%.</p>

      <p>It matters most to exactly the people this site is written for: someone who leaves a job at 55,
      58, or 62, years before Medicare and years before the standard penalty-free age, and needs a way to
      draw income from savings without a 10% haircut on every withdrawal.</p>

""" + facts('The rule, precisely', [
        ('Who qualifies', 'Anyone who separates from an employer in or after the calendar year they turn '
                          '55.'),
        ('What it applies to', 'Only the 401(k) or 403(b) of the employer <strong>you are leaving</strong>. '
                               'Not old employers’ plans, not IRAs, not a plan you already rolled '
                               'money into.'),
        ('Public safety exception', 'A specific list of &ldquo;qualified public safety employees&rdquo; '
                                    '&mdash; state and local police, firefighters and EMS workers, federal '
                                    'law enforcement and firefighters, air traffic controllers, and (since '
                                    'a 2022 law) private-sector firefighters and state/local corrections '
                                    'officers &mdash; qualify at 50, or at any age once they reach 25 years '
                                    'of service under the plan.'),
        ('Taxes still apply', 'Ordinary income tax is owed on every withdrawal, exactly as it would be '
                              'after 59&frac12;. Only the 10% early-withdrawal penalty is waived.'),
        ('The plan decides the mechanics', 'Employers are not required to allow flexible withdrawals. '
                                           'Some plans permit only a single lump-sum distribution, which '
                                           'can push you into a higher tax bracket for that year.'),
    ]) + """
      <h2>The mistake that cancels it</h2>

      <p>One way people lose access to this exception without meaning to: <strong>rolling the 401(k) into
      an IRA</strong> after leaving the job, often on the advice of someone focused on investment options
      rather than on this rule. The Rule of 55 itself does not apply to IRAs — it is specific to the
      employer plan. Once the money is in an IRA, the standard age-59&frac12; rule governs it instead, along
      with the IRA's own separate list of penalty exceptions, which is shorter and does not include simply
      &ldquo;you left a job after 55.&rdquo;</p>

      <p>If there is any chance you will need this money before 59&frac12;, that is a reason to leave it in
      the old employer's plan, at least for the amount you may need, before rolling the rest anywhere
      else.</p>

""" + AD_INLINE + """
      <h2>Worth checking before you rely on it</h2>

""" + check([
        'Confirm with your plan administrator, in writing, that your specific plan '
        '<strong>allows periodic or partial withdrawals</strong> rather than only a lump sum &mdash; this '
        'varies by employer and is not guaranteed by the rule itself.',
        'Check the <strong>exact separation date</strong> the rule uses: it is the calendar year you turn '
        '55, not your birthday. Leaving in January of that year still qualifies; leaving in December the '
        'year before does not.',
        'If you have <strong>multiple old 401(k)s</strong>, only the plan of the employer you are '
        'currently leaving qualifies. A 401(k) from a job you left at 50 does not get the exception now, '
        'even though you are over 55 today.',
        'Remember that <strong>state tax</strong> treatment of the withdrawal is separate from this '
        'federal rule and varies by state.',
        'Weigh it against other pre-59&frac12; options &mdash; Roth conversions, SEPP/72(t) schedules, '
        'taxable brokerage accounts &mdash; with an accountant, since which is cheapest depends on your '
        'specific tax picture.',
    ]) + """
      <p>The Rule of 55 will not appear on your account statement or in most plan summaries — it is a
      provision of the tax code, not a feature the plan advertises. Knowing it exists, and knowing the
      rollover trap that quietly cancels it, is usually the entire value of this page.</p>
""",
    'sources': [
        ('IRS &mdash; Retirement topics: Exceptions to tax on early distributions',
         'https://www.irs.gov/retirement-plans/plan-participant-employee/retirement-topics-tax-on-early-distributions'),
        ('IRS &mdash; Retirement plan and IRA required minimum distributions FAQs',
         'https://www.irs.gov/retirement-plans/retirement-plans-faqs-regarding-required-minimum-distributions'),
        ('IRS &mdash; Topic no. 558, Additional tax on early distributions',
         'https://www.irs.gov/taxtopics/tc558'),
        ('TSP.gov &mdash; SECURE Act 2.0, Section 329: Modification of eligible age for qualified public '
         'safety employees',
         'https://www.tsp.gov/bulletins/23-3/'),
    ],
    'next': {'slug': 'delayed-retirement-credit',
             'title': 'What delaying Social Security actually adds to your check',
             'blurb': 'The other side of the same years &mdash; what waiting to claim is actually worth.'},
}

# ---------------------------------------------------- delayed retirement credit
ARTICLES9['delayed-retirement-credit'] = {
    'title': 'What Delaying Social Security Actually Adds to Your Check &mdash; The Second Half Guide',
    'eyebrow': 'Facts &amp; thresholds',
    'h1': 'What delaying Social Security actually adds to your check',
    'dek': 'No secret, no trick &mdash; just a published rate. Waiting past full retirement age adds '
           '8% a year to your benefit, up to age 70, where it stops.',
    'meta': '4 minute read &middot; Verified against SSA rules',
    'checked': CHECKED9,
    'body': """      <p>You may have seen this dressed up as a hidden "bonus" or a "secret" a newsletter wants to sell
      you. It is neither. It is a published Social Security rule, sitting in plain text on ssa.gov, and it
      is worth knowing on its own terms rather than through an ad.</p>

""" + facts('The rule', [
        ('Full retirement age (FRA)', '67, for anyone born in 1960 or later.'),
        ('Delayed retirement credits', '8% added per year for each year you wait past FRA, up to age 70.'),
        ('Maximum total increase', '24% above your FRA benefit amount, reached at age 70.'),
        ('Where it stops', 'Delayed retirement credits stop accumulating at age 70. Waiting beyond 70 does '
                           'not increase the retirement benefit further.'),
        ('What it does not change', 'How your benefit was calculated in the first place, or whether '
                                    'benefits are taxed. The credit increases the benefit based on how '
                                    'long you wait past FRA, up to 70 &mdash; it does not change anything '
                                    'else about how the benefit works.'),
    ]) + """
      <p>In practical terms: someone whose FRA benefit is $2,000 a month gets about $2,480 a month by
      waiting until 70 instead — permanently, adjusted for cost-of-living increases every year after,
      same as any other benefit. That is the entire "secret." It is arithmetic SSA publishes, not
      information anyone is hiding.</p>

      <blockquote class="pull">
        <p>This is not advice to delay. Whether waiting makes sense depends on your health, your other
        income, and whether you have a spouse whose survivor benefit depends on yours &mdash; a genuinely
        personal calculation this page is not making for you.</p>
      </blockquote>

""" + AD_INLINE + """
      <h2>Where it connects to other decisions on this site</h2>

""" + check([
        'Leaving a job and claiming Social Security are <strong>two separate decisions</strong>. You can '
        'stop working at 60 or 62 and still delay claiming to 67 or 70, living on savings or '
        '<a href="/rule-of-55">Rule of 55 withdrawals</a> in between.',
        'If you are married, the <strong>higher earner delaying</strong> raises the benefit that becomes '
        'the survivor benefit later &mdash; the mechanic behind <a href="/widows-penalty">the widow’s '
        'penalty</a> piece on this site.',
        'Delaying Social Security does not automatically delay your <strong>Medicare</strong> enrollment. '
        'Most people still need to sign up for Part B on its own seven-month schedule at 65 no matter when '
        'they claim Social Security. The exception is active employer group health coverage — yours or a '
        'spouse’s current job — which can open a Special Enrollment Period instead; see '
        '<a href="/medicare-enrollment">the Medicare enrollment deadline piece</a> on this site for the '
        'specifics.',
        'The 8% figure is <strong>set in statute</strong>, not adjusted for inflation or market conditions '
        '&mdash; it is the same 8% every year, unlike COLA increases.',
    ]) + """
      <p>Nobody needs to sell you access to this. It is a public rate, publicly calculated, and the only
      thing separating "secret" marketing from a plain fact is whether someone is asking you to pay for
      it.</p>
""",
    'sources': [
        ('SSA &mdash; Delayed Retirement | Born in 1960', 'https://www.ssa.gov/benefits/retirement/planner/1960-delay.html'),
        ('Code of Federal Regulations &sect; 404.313', 'https://www.ssa.gov/OP_Home/cfr20/404/404-0313.htm'),
    ],
    'next': {'slug': 'social-security-62',
             'title': 'Should you file at 62?',
             'blurb': 'The other end of the same trade-off &mdash; what claiming early actually costs.'},
}
