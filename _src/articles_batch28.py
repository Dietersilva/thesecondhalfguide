#!/usr/bin/env python3
"""Twenty-eighth batch: the two IRS announcements of early November 2026 --
Revenue Procedure 2026-35 (2027 income-tax inflation adjustments, released
5 November, IR-2026-133) and Notice 2026-66 (2027 retirement-plan and IRA limits,
released 12 November).

irs.gov was not read directly: verified per CLAUDE.md section 2 by agreement
across independent write-ups that cite the IRS release. Deliberately omitted
because only one source gave it, or sources conflicted: the Saver's Credit
thresholds (one outlet says a new Saver's Match replaces the credit for 401(k)
and IRA contributions; others do not), the 2027 overall plan limit of $75,000,
the 2027 annual gift-tax exclusion, head-of-household bracket thresholds (rounded
differently across sources), and the 32% and 35% bracket thresholds below the 24%
line."""

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
           '$1,000 for couples, the senior deduction does not move, and none of it touches the return '
           'you file this spring.',
    'meta': '6 minute read &middot; Checked against the IRS announcement and independent write-ups that '
            'cite it',
    'checked': CHECKED28,
    'body': """      <p>On 5 November the IRS published the inflation adjustments for tax year 2027 in Revenue
      Procedure 2026-35, with a companion news release. The first thing to get straight is what they apply
      to. These are the amounts for income earned in <strong>2027</strong>, on returns filed in 2028. The
      return due in April is a 2026 return, and it uses the 2026 numbers, which are on
      <a href="/standard-deduction-65">the standard deduction page</a>.</p>

      <p>Most of the announcement is arithmetic. The seven rates stay where they are, and the dollar
      thresholds move up by about 3.2%. Here is what that does, and what it does not do for readers 65
      and older.</p>

""" + facts('The 2027 tax numbers, in dollars', [
        ('$33,200', 'Standard deduction, married filing jointly. Up $1,000 from 2026.'),
        ('$16,600', 'Standard deduction, single or married filing separately. Up $500.'),
        ('$24,925', 'Standard deduction, head of household. Up $775.'),
        ('$1,700 or $2,100', 'The extra standard deduction for being 65 or older (or blind): $1,700 for '
                             'each qualifying spouse if married, $2,100 if single or head of household. '
                             'Up $50 each, as reported.'),
        ('$6,000', 'The senior deduction for people 65 and older, for 2025 through 2028. Set in law, not '
                   'indexed, and it phases out above $75,000 of income single or $150,000 joint.'),
        ('$51,050 / $102,100', 'The top of the 0% long-term capital gains rate, single and joint, as '
                               'reported.'),
    ]) + """
      <h2>The standard deduction</h2>

      <p>For 2027 the base standard deduction is $33,200 for married couples filing jointly, $16,600 for
      single filers and married people filing separately, and $24,925 for heads of household. The last
      figure was projected at $24,950 by some forecasters, and the IRS number is $24,925.</p>

      <p>The age add-on is the part specific to readers of this site. An extra amount is added to the
      standard deduction for a taxpayer who is 65 or older, and again for one who is blind. Reporting on
      the revenue procedure gives $1,700 per qualifying condition for married filers and $2,100 for
      unmarried filers who are not surviving spouses, each $50 more than in 2026. Separately,
      the $6,000 senior deduction created in 2025 sits outside the standard deduction and does not change
      in 2027. It runs through 2028 and phases out above $75,000 of income
      for a single filer or $150,000 for a joint return. Both are on
      <a href="/senior-deduction">the senior deduction page</a>, and the phase-out is on
      <a href="/senior-deduction-phaseout">its own page</a>.</p>

      <p>Put together, using 2027 amounts: a single filer who is 66 with income under the senior-deduction
      phase-out line has $16,600 plus $2,100 plus $6,000, which is $24,700 of income that is not taxed.
      A married couple who are both 67 and are under the joint line have $33,200 plus $1,700 twice plus
      $6,000 twice, which is $48,600. Both sums are arithmetic on the published amounts, not a
      statement about anyone&rsquo;s tax bill.</p>

      <blockquote class="pull">
        <p>The brackets moved about 3.2%. The $6,000 senior deduction did not move at all. It is set in
        law, not indexed.</p>
      </blockquote>

""" + AD_INLINE + """
      <h2>The brackets</h2>

      <p>The rates are 10%, 12%, 22%, 24%, 32%, 35% and 37%. The thresholds, reported from the revenue
      procedure, are below. Each figure is the taxable income above which a rate begins.</p>

""" + facts('Where each rate begins, 2027 (taxable income above)', [
        ('12%', '$12,800 single. $25,600 married filing jointly.'),
        ('22%', '$52,025 single. $104,050 married filing jointly.'),
        ('24%', '$109,125 single. $218,250 married filing jointly.'),
        ('37%', '$661,375 single. $793,650 married filing jointly.'),
    ]) + """
      <p>Those are taxable income, which is what is left after the deductions above. A couple whose
      income is a pension and Social Security, for example, may land well inside the 12% bracket after
      the standard and senior deductions, which is why the deduction amounts matter more to many
      readers than the bracket edges. How benefits are counted is on
      <a href="/no-tax-on-social-security">the Social Security taxation page</a>, and the thresholds
      that decide how much of a benefit is taxable are not indexed at all.</p>

      <h2>The capital gains line</h2>

      <p>Long-term capital gains have their own rates of 0%, 15% and 20%. For 2027 the 0% rate is reported
      to apply to taxable income up to $51,050 for a single filer and $102,100 for a joint return. That
      is the number that comes up for people selling a house or taking gains in the years between work and
      required distributions, and the reporting on it is consistent across several tax sites, though
      this page did not read the revenue procedure&rsquo;s table directly.</p>

      <h2>What this does not change</h2>

      <p>It does not change the 2026 return, the senior deduction&rsquo;s dollar amount or its phase-out,
      the amounts that make Social Security taxable, or Medicare premiums. The Part B premium and the
      income thresholds for the Medicare surcharge, which look back two years, are announced separately,
      and as of this writing they have not been. The surcharge is on
      <a href="/irmaa">the IRMAA page</a>. Required withdrawals, which push income up in the
      early seventies, are on <a href="/rmd-deadline">the RMD page</a>.</p>

      <p>The retirement-account limits that the IRS announced a week later, on 12 November, are on
      <a href="/retirement-limits-2027">their own page</a>.</p>

      <h2>What&rsquo;s worth keeping in mind</h2>

""" + check([
        'The IRS announced the 2027 amounts on <strong>5 November 2026</strong>. They apply to income earned '
        'in 2027, on returns filed in 2028, not to the return due this spring.',
        'Standard deduction: <strong>$33,200</strong> joint, <strong>$16,600</strong> single, '
        '<strong>$24,925</strong> head of household.',
        'The age-65 add-on is reported at <strong>$1,700</strong> per qualifying spouse if married and '
        '<strong>$2,100</strong> if unmarried. The <strong>$6,000</strong> senior deduction is unchanged.',
        'The seven rates are unchanged; thresholds rose about <strong>3.2%</strong>. The 0% capital gains rate '
        'reaches <strong>$51,050</strong> single and <strong>$102,100</strong> joint, as reported.',
        'The Medicare Part B premium and surcharge thresholds for 2027 have not been announced.',
    ]) + """
      <p>The announcement is a set of numbers for next year. What a particular household owes depends on
      its income and its other deductions, and this page leaves that to the forms.</p>
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
        ('Lewis Group CPAs &mdash; The 2027 federal tax brackets are out',
         'https://lewisgroupcpas.com/the-2027-federal-tax-brackets-are-out-what-changed-and-how-to-use-it/'),
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
    'meta': '6 minute read &middot; Checked against IRS Notice 2026-66 as reported by several '
            'retirement-plan and tax outlets',
    'checked': CHECKED28,
    'body': """      <p>The IRS announced next year&rsquo;s retirement-plan limits on 12 November, in Notice 2026-66.
      Most of the changes are small, and one of them is a number that was an estimate until this week:
      the wage threshold that decides whether a worker&rsquo;s catch-up contributions have to go in as
      Roth. These limits take effect on 1 January 2027 and apply to contributions for that year.</p>

      <p>Everything below is the published limit, not a recommendation about how much anyone should save.</p>

""" + facts('The 2027 limits, with 2026 for comparison', [
        ('$25,500', '401(k), 403(b), most 457 plans and the federal Thrift Savings Plan. Was $24,500.'),
        ('$8,500', 'Catch-up for age 50 and older. Total $34,000. Was $8,000.'),
        ('$11,750', 'Catch-up for ages 60 to 63, in place of the standard one. Total $37,250. Was $11,250.'),
        ('$7,500', 'Traditional and Roth IRA contribution limit. Unchanged.'),
        ('$1,100', 'IRA catch-up for age 50 and older. Unchanged, so $8,600 in all.'),
        ('$155,000', 'The prior-year FICA wage level above which catch-up contributions must be Roth. Was '
                     '$150,000.'),
    ]) + """
      <h2>The workplace-plan limits</h2>

      <p>The employee deferral limit for a 401(k), 403(b), most 457(b) plans and the Thrift Savings Plan
      goes from $24,500 in 2026 to $25,500. Workers 50 and older can add the standard catch-up, which
      rises from $8,000 to $8,500, for a total of $34,000. The larger catch-up for people who are 60, 61,
      62 or 63 during the year rises from $11,250 to $11,750, for a total of $37,250. It replaces the
      standard catch-up for those four years and is available only if the plan allows it, as covered on
      <a href="/catch-up-60-63">the ages 60 to 63 page</a>. Turn 64 and the amount returns to the standard
      figure.</p>

      <h2>What the maximum comes to, by age</h2>

      <p>The three tiers are simple to add up. A worker under 50 can defer up to $25,500 in 2027. One who is
      50 to 59, or 64 and older, can defer up to $34,000, which is $25,500 plus the $8,500 catch-up. One who
      turns 60, 61, 62 or 63 during 2027, which means a birth year from 1964 through 1967, can defer up to
      $37,250, which is $25,500 plus $11,750. These are the ceilings the IRS allows. Whether a particular
      plan permits the full amount, or the larger catch-up at all, is the plan&rsquo;s own choice. Employer
      matching and other contributions are separate and are not counted in these figures.</p>

      <h2>The IRA limits</h2>

      <p>The IRA limit does not change. It stays at $7,500 for 2027, and the catch-up for people 50 and
      older stays at $1,100, which makes $8,600 for an eligible saver. Reporting explains why: IRA limits move
      in $500 steps, and this year&rsquo;s inflation did not carry the underlying figure far enough to
      cross the next one.</p>

      <p>The income ranges that decide who can contribute to a Roth IRA, or deduct a traditional IRA
      contribution, do move. For a single filer or head of household the Roth range is $158,000 to
      $173,000, up from $153,000 to $168,000. For married couples filing jointly it is $250,000 to
      $260,000, up from $242,000 to $252,000. The range for deducting a traditional IRA contribution
      when the contributor is covered by a workplace plan, for a joint return, is $133,000 to $153,000,
      up from $129,000 to $149,000.</p>

      <blockquote class="pull">
        <p>The 401(k) limit went up $1,000. The IRA limit did not move at all.</p>
      </blockquote>

""" + AD_INLINE + """
      <h2>The Roth catch-up threshold</h2>

      <p>For 2027, workers whose FICA wages from the employer sponsoring the plan were more than $155,000
      in 2026 generally have to make their catch-up contributions to that plan as Roth contributions,
      after tax. For 2026 the line was $150,000 of 2025 wages. Until this week the 2027 figure was an
      outside estimate, which is why <a href="/roth-catch-up">the Roth catch-up page</a> called it
      unconfirmed. The IRS notice settles it. The rule counts wages from the plan sponsor, not
      self-employment income, and a plan that offers no Roth option cannot take catch-up contributions
      from the workers it covers, which is the part that surprises people.</p>

      <h2>Where the 2027 numbers came from</h2>

      <p>These limits are indexed to inflation under rules set in law, and the IRS publishes them in a fall
      notice. The 2026 limits came out in November of last year, so the timing is normal. Outlets reporting
      on the notice, including the plan-sponsor trade group PSCA, a tax-accounting publication and CNBC,
      give the same figures for the 401(k), the catch-ups and the IRA. A few calculator sites published
      projections earlier in the fall, some of which differed on the IRA limit, and those are superseded by
      the notice.</p>

      <h2>What this does not cover</h2>

      <p>It does not cover the health savings account limits, which were announced in the spring and are on
      <a href="/hsa-medicare-timing">the HSA page</a>. It does not include the Saver&rsquo;s Credit
      thresholds, because one outlet describes a change to that credit in 2027 that the others do not
      mention, and the notice is the place to check. And it does not cover the required minimum
      distributions, whose age is set in law and is on
      <a href="/rmd-deadline">the RMD page</a>. The income-tax numbers announced a week earlier are on
      <a href="/tax-numbers-2027">their own page</a>, and the rule that lets someone 55 or older leave
      an employer and draw on its plan is on <a href="/rule-of-55">the rule of 55 page</a>.</p>

      <h2>What&rsquo;s worth keeping in mind</h2>

""" + check([
        'The 2027 401(k), 403(b), 457(b) and TSP limit is <strong>$25,500</strong>. The age-50 catch-up is '
        '<strong>$8,500</strong>; ages 60 to 63 get <strong>$11,750</strong> instead.',
        'The IRA limit is <strong>$7,500</strong> and the IRA catch-up <strong>$1,100</strong>. Both are '
        'unchanged.',
        'The Roth IRA range rises to <strong>$158,000&ndash;$173,000</strong> single and '
        '<strong>$250,000&ndash;$260,000</strong> joint.',
        'The catch-up Roth threshold for 2027 is <strong>$155,000</strong> of 2026 FICA wages from the plan '
        'sponsor.',
        'These are limits, not targets. Whether a plan offers the higher catch-up, or any Roth option, is '
        'the plan&rsquo;s decision.',
    ]) + """
      <p>The notice sets the ceilings. What a worker can do beneath them is up to the plan and the
      worker&rsquo;s own income and age.</p>
""",
    'sources': [
        ('IRS &mdash; Notice 2026-66: 2027 amounts relating to retirement plans and IRAs',
         'https://www.irs.gov/pub/irs-drop/n-26-66.pdf'),
        ('CNBC &mdash; IRS announces 2027 401(k) contribution limits (12 November 2026)',
         'https://www.cnbc.com/2026/11/12/401k-contribution-limits-2027.html'),
        ('PSCA &mdash; IRS releases 2027 401(k), IRA limits',
         'https://www.psca.org/news/psca-news/2026/11/breaking-irs-announces-2027-401k-contribution-limits'),
        ('The Tax Adviser &mdash; Inflation adjustments to retirement account limits issued for 2027',
         'https://www.thetaxadviser.com/news/2026/nov/inflation-adjustments-to-retirement-account-limits-issued-for-2027/'),
        ('Current Federal Tax Developments &mdash; Technical analysis of IRS Notice 2026-66',
         'https://www.currentfederaltaxdevelopments.com/blog/2026/11/12/technical-analysis-of-irs-notice-2026-66-statutory-mechanics-and-practice-implications-of-the-2027-cost-of-living-adjustments-for-qualified-plans-and-iras'),
        ('401kSpecialist &mdash; IRS makes it official: 2027 401(k) contribution limit rises to $25,500',
         'https://401kspecialistmag.com/irs-makes-it-official-2027-401k-contribution-limit-rises-to-25500/'),
    ],
    'next': {'slug': 'catch-up-60-63',
             'title': 'The catch-up window that closes at 64',
             'blurb': 'The larger 401(k) catch-up for ages 60 to 63, and the plan rule that decides whether '
                      'you can use it.'},
}
