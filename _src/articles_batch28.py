#!/usr/bin/env python3
"""Twenty-eighth batch: the two IRS announcements of early November 2026 --
Revenue Procedure 2026-35 (2027 income-tax inflation adjustments, released
5 November, IR-2026-133) and Notice 2026-66 (2027 retirement-plan and IRA limits,
released 12 November).

irs.gov was not read directly: verified per CLAUDE.md section 2 by agreement
across independent write-ups that cite the IRS release, and an outside audit of
13 November that read Rev. Proc. 2026-35 and Notice 2026-66. Revised on that
audit: MAGI and eligibility wording on the senior deduction, capital-gain
stacking, calendar wording, governmental-457(b) catch-ups, shared IRA limit, the
narrower no-Roth statement, and the Saver's Match, which the IRS and CRS confirm
replaces the Saver's Credit for retirement contributions from 2027. Deliberately
omitted: the 2027 overall plan limit of $75,000, the annual gift-tax exclusion,
and head-of-household bracket thresholds."""

from build_articles import facts, check, AD_INLINE

ARTICLES28 = {}

CHECKED28 = '13 November 2026'

# ------------------------------------------------------------- 2027 tax numbers
ARTICLES28['tax-numbers-2027'] = {
    'title': 'The 2027 Tax Numbers: Standard Deduction, Brackets, 65-Plus Add-On '
             '&mdash; The Second Half Guide',
    'eyebrow': 'Facts &amp; thresholds',
    'h1': 'The 2027 tax numbers: the standard deduction, the brackets and the 65-plus add-on',
    'dek': 'The IRS has set next year&rsquo;s inflation-adjusted amounts. The standard deduction rises '
           '$1,000 for couples and the senior deduction does not move. These amounts apply to tax year '
           '2027, generally on returns filed in 2028.',
    'meta': '6 minute read &middot; Checked against the IRS announcement and Revenue Procedure 2026-35 '
            'as summarized by tax publications',
    'checked': CHECKED28,
    'body': """      <p>On 5 November 2026 the IRS published the inflation adjustments for tax year 2027 in Revenue
      Procedure 2026-35, with a companion news release. They apply to income earned in 2027,
      generally on returns filed in 2028. A 2026 return, generally filed in 2027, uses the 2026 amounts,
      which are on <a href="/standard-deduction-65">the standard deduction page</a>.</p>

      <p>Most of the announcement is arithmetic. The seven rates stay where they are, and the dollar
      thresholds move up by about 3.2%. Here is what that does, and what it does not do for readers 65
      and older.</p>

""" + facts('The 2027 tax numbers, in dollars', [
        ('$33,200', 'Standard deduction, married filing jointly. Up $1,000 from 2026.'),
        ('$16,600', 'Standard deduction, single or married filing separately. Up $500.'),
        ('$24,925', 'Standard deduction, head of household. Up $775.'),
        ('$1,700 or $2,100', 'The extra standard deduction for being 65 or older (or blind): $1,700 per '
                             'qualifying condition if married, $2,100 if unmarried and not a surviving '
                             'spouse. Each is $50 more than in 2026.'),
        ('$6,000', 'The senior deduction, per eligible person 65 or older, for 2025 through 2028. Set in '
                   'law, not indexed. It phases out above modified adjusted gross income of $75,000, or '
                   '$150,000 on a joint return.'),
        ('$51,050 / $102,100', 'The taxable income at which the 0% long-term capital gains rate ends, '
                               'single and joint.'),
    ]) + """
      <h2>The standard deduction</h2>

      <p>For 2027 the base standard deduction is $33,200 for married couples filing jointly, $16,600 for
      single filers and married people filing separately, and $24,925 for heads of household.</p>

      <p>The age add-on is the part specific to readers of this site. An extra amount is added to the
      standard deduction for a taxpayer who is 65 or older, and again for one who is blind. For 2027 it is
      $1,700 per qualifying condition for married filers and $2,100 for unmarried filers who are not
      surviving spouses, each $50 more than in 2026.</p>

      <p>Measured against 2026, the three base amounts rose by about 3.1% for joint filers and single
      filers and about 3.2% for heads of household, which is the same pace as the brackets. The age add-on
      is part of the standard deduction, so it is available only to people who take the standard
      deduction. The senior deduction below is not, which is the difference that most coverage skips.</p>

      <h2>The senior deduction does not move</h2>

      <p>The $6,000 senior deduction created in 2025 is a separate provision. It is up to $6,000 per
      eligible person 65 or older, runs through 2028, and phases out for modified adjusted gross income
      (MAGI) above $75,000, or $150,000 on a joint return. Eligibility also requires a qualifying Social
      Security number, and married taxpayers must file jointly. An eligible taxpayer can claim it whether
      they itemize or take the standard deduction. It is not indexed, so it is the same in 2027 as in 2026.
      It is covered on <a href="/senior-deduction">the senior deduction page</a>, and the phase-out is on
      <a href="/senior-deduction-phaseout">its own page</a>.</p>

      <p>An example, using 2027 amounts. For an eligible single filer age 66 who takes the standard
      deduction and has MAGI of $75,000 or less, these deductions total $24,700: $16,600 plus $2,100 plus
      $6,000. For an eligible joint-filing couple, both age 67, with MAGI of $150,000 or less, the total is
      $48,600: $33,200 plus $3,400 plus $12,000. These are deductions used in calculating federal taxable
      income. They are not tax credits, and they are not a blanket exemption for that amount of household
      receipts.</p>

      <blockquote class="pull">
        <p>The brackets moved about 3.2%. The $6,000 senior deduction did not move at all. It is set in
        law, not indexed.</p>
      </blockquote>

""" + AD_INLINE + """
      <h2>The brackets</h2>

      <p>The ordinary-income rates are 10%, 12%, 22%, 24%, 32%, 35% and 37%. Each rate applies only to the
      portion of ordinary taxable income within that bracket. The thresholds below, from the IRS
      announcement, are the taxable income above which each rate begins. Taxable income is income after
      applicable adjustments and deductions.</p>

""" + facts('Selected ordinary-income bracket thresholds, 2027 (taxable income above)', [
        ('12%', '$12,800 single. $25,600 married filing jointly.'),
        ('22%', '$52,025 single. $104,050 married filing jointly.'),
        ('24%', '$109,125 single. $218,250 married filing jointly.'),
        ('32%', '$208,325 single. $416,650 married filing jointly.'),
        ('35%', '$264,550 single. $529,100 married filing jointly.'),
        ('37%', '$661,375 single. $793,650 married filing jointly.'),
    ]) + """
      <p>How Social Security benefits are counted is on
      <a href="/no-tax-on-social-security">the Social Security taxation page</a>. The thresholds that decide
      how much of a benefit is taxable are set in law and are not indexed.</p>

      <h2>The capital gains line</h2>

      <p>For 2027, the 0% rate on most net long-term capital gains and qualified dividends reaches taxable
      income of $51,050 for single filers and $102,100 for joint filers. Ordinary taxable income uses up
      the lower portion of that range first, and only gains that fit below the ceiling receive the 0%
      rate. The ceiling is not an allowance for sale proceeds. A main-home sale may qualify for a separate
      exclusion under different rules. In practice that means wages, a pension or withdrawals from a
      traditional account fill the 0% range first, and a gain is taxed at 0% only to the extent it fits
      in what is left. Head-of-household thresholds are set separately in the IRS tables and are not
      reproduced here.</p>

      <h2>What this does not change</h2>

      <p>It does not change the 2026 return, the senior deduction&rsquo;s dollar amount or its phase-out, or
      the amounts that make Social Security taxable. The IRS tax inflation release does not set Medicare
      Part B premiums or the income brackets for the Medicare surcharge, which CMS announces separately.
      The surcharge, which looks back two years, is on <a href="/irmaa">the IRMAA page</a>. Required
      minimum distributions can increase taxable income; the starting age depends on birth year and the
      account, and is on <a href="/rmd-deadline">the RMD page</a>.</p>

      <p>The retirement-account limits that the IRS announced a week later, on 12 November, are on
      <a href="/retirement-limits-2027">their own page</a>.</p>

      <h2>What&rsquo;s worth keeping in mind</h2>

""" + check([
        'These amounts apply to <strong>tax year 2027</strong>, generally on returns filed in 2028. A 2026 '
        'return uses the 2026 amounts.',
        'Standard deduction: <strong>$33,200</strong> joint, <strong>$16,600</strong> single, '
        '<strong>$24,925</strong> head of household. The age-65 add-on is <strong>$1,700</strong> per '
        'qualifying condition if married and <strong>$2,100</strong> if unmarried.',
        'The <strong>$6,000</strong> senior deduction is unchanged. It phases out above MAGI of $75,000 '
        '($150,000 joint).',
        'The 0% capital gains rate reaches taxable income of <strong>$51,050</strong> single and '
        '<strong>$102,100</strong> joint.',
    ]) + """
      <p>The announcement is a set of numbers for next year. What a particular household owes depends on
      its income and its deductions, and the forms decide that.</p>
""",
    'sources': [
        ('IRS &mdash; IR-2026-133: IRS releases tax inflation adjustments for tax year 2027',
         'https://www.irs.gov/newsroom/irs-releases-tax-inflation-adjustments-for-tax-year-2027-taxpayers-continue-to-benefit-from-the-working-families-tax-cuts'),
        ('KPMG &mdash; Rev. Proc. 2026-35: Inflation adjustments for tax year 2027',
         'https://kpmg.com/us/en/taxnewsflash/news/2026/11/rev-proc-2026-35-inflation-adjustments-2027.html'),
        ('Taxgirl &mdash; 2027 tax brackets: IRS announces tax rates, deductions and more (10 November 2026)',
         'https://www.taxgirl.com/2026/11/10/2027-tax-brackets-standard-deduction/'),
        ('Budget Seniors &mdash; 2027 federal tax brackets: official IRS rates and standard deduction',
         'https://www.budgetseniors.com/benefits-finance/2027-federal-tax-brackets/'),
        ('Visaverge &mdash; 2027 capital gains tax brackets',
         'https://www.visaverge.com/taxes/2027-capital-gains-tax-brackets/'),
    ],
    'next': {'slug': 'senior-deduction',
             'title': 'The new $6,000 senior deduction',
             'blurb': 'Who qualifies, how it stacks with the standard deduction, and where it phases out.'},
}

# ------------------------------------------------------------- 2027 retirement limits
ARTICLES28['retirement-limits-2027'] = {
    'title': 'The 2027 Retirement Account Limits: 401(k), IRA, Catch-Ups &mdash; The Second Half Guide',
    'eyebrow': 'Facts &amp; thresholds',
    'h1': 'The 2027 retirement account limits: the 401(k), the IRA and the catch-ups',
    'dek': 'The 401(k) limit rises $1,000 to $25,500, the catch-up for ages 60 to 63 goes to $11,750, and '
           'the IRA limit stays at $7,500. The IRS announced the 2027 amounts on 12 November.',
    'meta': '6 minute read &middot; Checked against IRS Notice 2026-66 as summarized by retirement-plan '
            'and tax publications',
    'checked': CHECKED28,
    'body': """      <p>The IRS announced next year&rsquo;s retirement-plan limits on 12 November 2026, in Notice
      2026-66. Most of the changes are small, and one is a number that was an estimate until this month:
      the wage threshold that decides whether a worker&rsquo;s catch-up contributions have to go in as
      Roth. The limits take effect on 1 January 2027 and apply to contributions for that year.</p>

      <p>Everything below is the published limit, not a recommendation about how much anyone should save.</p>

""" + facts('The 2027 limits (2026 in parentheses)', [
        ('$25,500 ($24,500)', 'Employee deferral limit: 401(k), 403(b), eligible 457(b) plans and the '
                              'Thrift Savings Plan.'),
        ('$8,500 ($8,000)', 'Catch-up for age 50 and older. Total $34,000.'),
        ('$11,750 ($11,250)', 'Catch-up for ages 60 to 63, in place of the standard one. Total $37,250.'),
        ('$7,500 ($7,500)', 'Traditional and Roth IRA contribution limit, shared across both. Unchanged.'),
        ('$1,100 ($1,100)', 'IRA catch-up for age 50 and older. Unchanged, so $8,600 in all.'),
        ('$155,000 ($150,000)', 'The prior-year FICA wage level above which workplace-plan catch-up '
                                'contributions must be Roth.'),
    ]) + """
      <h2>The workplace-plan limits</h2>

      <p>The employee deferral limit goes from $24,500 in 2026 to $25,500. It applies to 401(k) and 403(b)
      plans, to eligible 457(b) plans, which include governmental and tax-exempt-employer plans, and to the
      federal Thrift Savings Plan. The age-based catch-ups below apply to 401(k), 403(b) and governmental
      457(b) plans and the Thrift Savings Plan. Nongovernmental 457(b) plans have different special
      catch-up rules, and these age tiers should not be assumed to apply to them.</p>

      <p>A worker under 50 can defer up to $25,500 in 2027. One who is 50 to 59, or 64 and older, can defer
      up to $34,000, which is $25,500 plus the $8,500 catch-up. One who turns 60, 61, 62 or 63 during 2027,
      which means a birth year from 1964 through 1967, can defer up to $37,250, which is $25,500 plus
      $11,750. The larger catch-up is available only if the plan allows it, as covered on
      <a href="/catch-up-60-63">the ages 60 to 63 page</a>. Turn 64 and the amount returns to the standard
      catch-up. Employer matching and other contributions are separate and are not counted in these
      figures.</p>

      <h2>What changed, and by how much</h2>

      <p>Against 2026, the deferral limit rose by $1,000, about 4.1%. The standard catch-up rose by $500,
      about 6.3%, and the ages 60 to 63 catch-up by $500, about 4.4%. The Roth IRA income range for single
      filers moved up by $5,000 at both ends, and the joint range by $8,000. The Roth catch-up wage
      threshold rose by $5,000. The IRA limit and its catch-up did not move. The percentages are
      arithmetic on the published figures.</p>

      <h2>The IRA limits</h2>

      <p>The IRS left both IRA dollar limits unchanged for 2027: $7,500, and a $1,100 catch-up for people
      50 and older, which makes $8,600 for an eligible saver. The limit is shared across a person&rsquo;s
      traditional and Roth IRAs; it is not a separate allowance for each account. Contributions also
      require sufficient eligible compensation, including the spousal-IRA rules where applicable. Direct
      Roth IRA eligibility and traditional IRA deductibility depend on additional income and filing-status
      rules.</p>

      <p>The income ranges, measured by modified adjusted gross income (MAGI), do move. For a single filer
      or head of household the Roth IRA range is $158,000 to $173,000, up from $153,000 to $168,000. For
      married couples filing jointly it is $250,000 to $260,000, up from $242,000 to $252,000. The range for
      deducting a traditional IRA contribution on a joint return, when the contributor is covered by a
      workplace plan, is $133,000 to $153,000, up from $129,000 to $149,000. When the contributor is not covered by a workplace plan but a spouse
      is, the joint range is $250,000 to $260,000, up from $242,000 to $252,000. For married people
      filing separately, the Roth range is not adjusted for inflation and stays at $0 to $10,000.</p>

      <blockquote class="pull">
        <p>The 401(k) limit went up $1,000. The IRA limit did not move at all.</p>
      </blockquote>

""" + AD_INLINE + """
      <h2>The Roth catch-up threshold</h2>

      <p>For 2027, workers whose FICA wages from the employer sponsoring the plan were more than $155,000
      in 2026 generally have to make their catch-up contributions to that plan as Roth contributions,
      after tax. For 2026 the line was $150,000 of 2025 wages. Until this month the 2027 figure was an
      outside estimate, which is why <a href="/roth-catch-up">the Roth catch-up page</a> called it
      unconfirmed. The IRS notice settles it. The test counts wages from the plan sponsor, not
      self-employment income, and specified aggregation rules and later applicability dates exist for
      some plans.</p>

      <p>A plan without a Roth feature generally cannot accept catch-up contributions from participants
      subject to the Roth catch-up requirement. It may still permit catch-ups for participants who are not
      subject to that requirement. This wage test concerns workplace-plan catch-ups. It does not determine
      eligibility to contribute to a Roth IRA.</p>

      <h2>The Saver&rsquo;s Match replaces the Saver&rsquo;s Credit</h2>

      <p>Starting with 2027 retirement contributions, the Saver&rsquo;s Match replaces the Saver&rsquo;s
      Credit for eligible retirement savers. Eligible individuals can receive a federal matching
      contribution of up to $1,000 to a designated retirement account, claimed on the 2027 return filed in
      2028. The Saver&rsquo;s Credit continues for eligible ABLE-account contributions. The two programs
      have separate eligibility rules, and the IRS page describes the income limits.</p>

      <h2>What this does not cover</h2>

      <p>It does not cover the health savings account limits, which were announced in the spring and are on
      <a href="/hsa-medicare-timing">the HSA page</a>, or required minimum distributions, whose starting age
      depends on birth year and is on <a href="/rmd-deadline">the RMD page</a>. The income-tax numbers
      announced a week earlier are on <a href="/tax-numbers-2027">their own page</a>, and the rule that
      lets someone 55 or older leave an employer and draw on its plan is on
      <a href="/rule-of-55">the rule of 55 page</a>.</p>

      <h2>What&rsquo;s worth keeping in mind</h2>

""" + check([
        'The 2027 deferral limit is <strong>$25,500</strong>; the age-50 catch-up is <strong>$8,500</strong>; '
        'ages 60 to 63 get <strong>$11,750</strong> instead. The age catch-ups apply to governmental 457(b) '
        'plans, not all 457 plans.',
        'The IRA limit is <strong>$7,500</strong>, shared across traditional and Roth IRAs, plus a '
        '<strong>$1,100</strong> catch-up. Both are unchanged.',
        'The Roth catch-up threshold for 2027 is <strong>$155,000</strong> of 2026 FICA wages from the plan '
        'sponsor.',
        'The <strong>Saver&rsquo;s Match</strong> replaces the Saver&rsquo;s Credit for retirement '
        'contributions starting in 2027.',
    ]) + """
      <p>These are limits, not targets. Compensation, tax rules and eligibility also constrain what any
      one person can contribute.</p>
""",
    'sources': [
        ('IRS &mdash; Notice 2026-66: 2027 amounts relating to retirement plans and IRAs',
         'https://www.irs.gov/pub/irs-drop/n-26-66.pdf'),
        ('CNBC &mdash; IRS announces 2027 401(k) contribution limits (12 November 2026)',
         'https://www.cnbc.com/2026/11/12/401k-contribution-limits-2027.html'),
        ('The Tax Adviser &mdash; Inflation adjustments to retirement account limits issued for 2027',
         'https://www.thetaxadviser.com/news/2026/nov/inflation-adjustments-to-retirement-account-limits-issued-for-2027/'),
        ('IRS &mdash; Saver&rsquo;s Match', 'https://www.irs.gov/credits-deductions/savers-match'),
        ('Congressional Research Service &mdash; The Retirement Savings Contribution Credit and the '
         'Saver&rsquo;s Match', 'https://www.congress.gov/crs-product/IF11159'),
    ],
    'next': {'slug': 'catch-up-60-63',
             'title': 'The catch-up window that closes at 64',
             'blurb': 'The larger 401(k) catch-up for ages 60 to 63, and the plan rule that decides whether '
                      'you can use it.'},
}
