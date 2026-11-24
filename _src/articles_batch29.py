#!/usr/bin/env python3
"""Twenty-ninth batch: the CMS announcement of 17 November 2026 -- the 2027 Medicare
Part B premium and deductible, the Part A deductible and premiums (CMS fact sheet
and the 19 November Federal Register notice, 91 FR 74556), and the 2027 IRMAA
brackets for Parts B and D.

cms.gov, ssa.gov and federalregister.gov were not read directly: verified per
CLAUDE.md section 2 by agreement across independent results that cite the CMS fact
sheet or the Federal Register notice (AARP, Kiplinger, a legal-news summary of the
notice, several benefits sites). The hospital coinsurance amounts are stated by
statute as fractions of the Part A deductible and were checked by arithmetic.
Deliberately omitted because only one source gave it: the share of enrollees who
pay an income-related surcharge, the married-filing-separately brackets, and the
2027 base Part D premium."""

from build_articles import facts, check, AD_INLINE
from charts import irmaa_tiers

ARTICLES29 = {}

CHECKED29 = '20 November 2026'

# ------------------------------------------------------------- Part B and Part A 2027
ARTICLES29['part-b-premium-2027'] = {
    'title': 'Medicare Part B Costs $209.40 in 2027: Premium, Deductible, Part A &mdash; The Second Half Guide',
    'eyebrow': 'Facts &amp; thresholds',
    'h1': 'Medicare Part B costs $209.40 a month in 2027',
    'dek': 'CMS announced the 2027 amounts on 17 November: a $6.50 rise in the Part B premium, a $9 rise '
           'in the deductible, and a $1,776 hospital deductible. What it takes out of the 3.6% raise.',
    'meta': '6 minute read &middot; Checked against the CMS fact sheet, the Federal Register notice and '
            'independent reporting that cites them',
    'checked': CHECKED29,
    'body': """      <p>On 17 November 2026 CMS announced the 2027 Medicare Part A and Part B amounts. They take effect
      on <strong>1 January 2027</strong>. Until then the 2026 amounts apply. The headline numbers are a
      standard Part B premium of <strong>$209.40</strong> a month and a Part B deductible of
      <strong>$292</strong>.</p>

      <p>This is the number that was missing from the Social Security raise. The 2027 COLA is 3.6%, and for
      most people the Part B premium is taken out of the payment before it arrives. Now both figures are
      official.</p>

""" + facts('The 2027 Medicare amounts, announced 17 November 2026', [
        ('$209.40', 'The standard monthly Part B premium. Up $6.50, or 3.2%, from $202.90 in 2026.'),
        ('$292', 'The annual Part B deductible. Up $9 from $283 in 2026.'),
        ('$1,776', 'The Part A inpatient hospital deductible for each benefit period. Up $40 from $1,736.'),
        ('$0', 'The Part A premium for most people, who have at least 40 quarters of Medicare-covered work.'),
        ('$328', 'The reduced Part A premium, for people with 30 to 39 quarters. It was $311 in 2026.'),
        ('$597', 'The full Part A premium, for people with fewer than 30 quarters. It was $565 in 2026.'),
        ('1 January 2027', 'When the new amounts take effect.'),
    ]) + """
      <h2>How the premium is set</h2>

      <p>The Part B premium is not a negotiated price. By law it is set to cover about a quarter of the
      average expected cost of Part B for people on Medicare, with the rest paid from general revenue.
      CMS attributed this year&rsquo;s increase mainly to projected growth in health care spending. The
      figure landed ten cents below the $209.50 that the 2026 Medicare Trustees Report had projected,
      which is the number <a href="/medicare-2027-costs">the page on 2027 Medicare costs</a> carried
      while the official amount was pending.</p>

      <p>For scale: the 2026 premium rose almost 10%, from $185.00 to $202.90. The 2027 increase is about
      a third of that.</p>

      <h2>What it takes out of the raise</h2>

      <p>The Social Security Administration puts the average retired-worker benefit at $2,095 before the
      3.6% COLA and $2,170 after, an increase of about $75 a month. The premium increase is $6.50.
      Subtracting one from the other gives about <strong>$68.50 a month</strong> left of the average
      raise for a person whose Part B premium is withheld from the benefit. That is the site&rsquo;s own
      arithmetic on two published figures, not a number either agency reported. The premium increase
      absorbs roughly 9% of the average raise.</p>

      <p>A $1,500 benefit rises by about $54, so $47.50 remains. A $3,000 benefit rises by about $108, so
      $101.50 remains. The premium is the same flat amount for both people, which is why it takes a
      larger share of a smaller raise.</p>

      <blockquote class="pull">
        <p>The premium is a flat dollar amount. The COLA is a percentage. The two meet in the same
        deposit, and the flat amount comes out first.</p>
      </blockquote>

""" + AD_INLINE + """
      <h2>The hold-harmless rule, and who it does not protect</h2>

      <p>A hold-harmless provision in the law limits how much of a Part B increase can reduce a
      person&rsquo;s net Social Security payment, for people who have the premium deducted from their
      benefit. It matters when the premium increase is bigger than the dollar COLA. This year the
      premium rises $6.50, so a 3.6% raise is smaller than the increase only for a benefit under about
      $181 a month. For most people the provision does not limit anything in 2027.</p>

      <p>It also does not cover everyone. People newly enrolled in Medicare, people who pay the
      <a href="/irmaa-2027">income-related surcharge</a>, people who do not have the premium taken from a
      Social Security payment, and people whose premium is paid by Medicaid are among those outside it.
      The mechanics are on <a href="/cola">the COLA page</a>.</p>

      <h2>Part A: the deductible and the premium</h2>

      <p>Part A pays for inpatient hospital care, and most people do not pay a premium for it. The
      <strong>$1,776</strong> deductible applies to each benefit period, which begins when you are
      admitted as an inpatient and ends after 60 days without inpatient care. It is not a yearly
      deductible, so a person admitted twice in a year, with 60 clear days between, can meet it twice.
      Whether a stay counts at all depends on being admitted rather than held for observation, which is
      covered on <a href="/observation-status">the observation status page</a>.</p>

      <p>After the deductible, hospital days 1 to 60 cost nothing. Days 61 to 90 carry a daily
      coinsurance of <strong>$444</strong>, which is by law one quarter of the deductible. Lifetime reserve
      days, of which a person has 60 over a lifetime, cost <strong>$888</strong> a day, one half of it.
      Skilled nursing facility days 21 to 100 cost <strong>$222</strong> a day, one eighth. Those three
      figures follow from the deductible and were checked by arithmetic. The rest of what Medicare does
      not pay is on <a href="/medicare-gaps">the gaps page</a>.</p>

      <p>The Part A premium figures appear in a Federal Register notice published on 19 November. The
      $597 full premium is about 5.7% above 2026, and the $328 reduced premium is the full amount less
      45%.</p>

      <h2>When you will see it</h2>

      <p>Social Security sends each beneficiary a notice of the new benefit amount, and the Part B
      premium for people who have it withheld is expected to show in that notice. People with a <em>my
      Social Security</em> account can read it online beginning in late November. Mailed notices follow
      in December. People who pay Medicare directly, rather than through Social Security, are billed on
      their own schedule.</p>

      <p>None of this changes what a Medicare Advantage plan or a Medigap policy charges. Those premiums
      are set by the plan. Part B is still owed on top of them, because both are layered on Original
      Medicare, as <a href="/advantage-vs-original">the Advantage or Original page</a> sets out.</p>

      <h2>What&rsquo;s worth keeping in mind</h2>

""" + check([
        'The 2027 standard Part B premium is <strong>$209.40</strong> and the deductible is '
        '<strong>$292</strong>, both effective <strong>1 January 2027</strong>. The 2026 amounts, '
        '$202.90 and $283, apply until then.',
        'The premium rose <strong>$6.50</strong>. Against the average $75 raise, about '
        '<strong>$68.50</strong> remains for someone whose premium is withheld. That is arithmetic on '
        'published figures.',
        'The Part A hospital deductible is <strong>$1,776</strong> per benefit period. Most people pay '
        'no Part A premium; the reduced premium is $328 and the full premium is $597.',
        'People who pay the income-related surcharge, are newly enrolled, or have no premium withheld '
        'are outside the hold-harmless rule.',
        'Plan and Medigap premiums are set separately and are not part of this announcement.',
    ]) + """
      <p>The raise and the deposit are still different numbers, and this year the gap between them is
      small. The figure to check is the one on the notice that arrives with your own name on it.</p>
""",
    'sources': [
        ('CMS &mdash; 2027 Medicare Parts A &amp; B premiums and deductibles (fact sheet)',
         'https://www.cms.gov/newsroom/fact-sheets/2027-medicare-parts-b-premiums-deductibles'),
        ('Federal Register &mdash; Medicare Program; CY 2027 Part A premiums for the uninsured aged and '
         'for certain disabled individuals who have exhausted other entitlement (19 November 2026)',
         'https://www.federalregister.gov/documents/2026/11/19/2026-23604/medicare-program-cy-2027-part-a-premiums-for-the-uninsured-aged-and-for-certain-disabled-individuals'),
        ('AARP &mdash; Medicare&rsquo;s Part B premium increases slightly for 2027',
         'https://www.aarp.org/medicare/medicare-part-b-premium-2027/'),
        ('Social Security Administration &mdash; 2027 Cost-of-Living Adjustment fact sheet',
         'https://www.ssa.gov/news/en/cola/factsheets/2027.html'),
        ('Kiplinger &mdash; Medicare premiums 2027: IRMAA brackets and surcharges for Parts B and D',
         'https://www.kiplinger.com/retirement/medicare/medicare-premiums-irmaa-brackets-and-surcharges-part-b-and-d-2027'),
    ],
    'next': {'slug': 'irmaa-2027',
             'title': 'The 2027 Medicare income surcharge',
             'blurb': 'The 2027 brackets for the surcharge on top of the $209.40: where it starts and '
                      'what each step adds.'},
}

# ------------------------------------------------------------------- IRMAA 2027
ARTICLES29['irmaa-2027'] = {
    'title': 'The 2027 IRMAA Brackets: Medicare Surcharge Starts at $112,000 &mdash; The Second Half Guide',
    'eyebrow': 'Facts &amp; thresholds',
    'h1': 'The 2027 Medicare income surcharge starts at $112,000 single, $224,000 joint',
    'dek': 'CMS published the 2027 IRMAA brackets on 17 November. The surcharge is based on your 2025 tax '
           'return, and each step is a cliff, not a slope.',
    'meta': '6 minute read &middot; Checked against the CMS fact sheet and independent reporting that '
            'cites it',
    'checked': CHECKED29,
    'body': """      <p>Medicare charges some people more than the standard premium, based on income. The surcharge
      is called IRMAA, for income-related monthly adjustment amount, and it applies to both Part B and
      Part D. On 17 November 2026 CMS published the 2027 brackets, which take effect on
      <strong>1 January 2027</strong> and are based on the income reported on a <strong>2025</strong> tax
      return.</p>

      <p>The standard Part B premium for 2027 is $209.40. The surcharge starts for a single filer whose
      modified adjusted gross income is above <strong>$112,000</strong>, and for a married couple filing
      jointly above <strong>$224,000</strong>. Those thresholds were $109,000 and $218,000 for 2026.</p>

""" + facts('The 2027 IRMAA tiers, by 2025 modified adjusted gross income', [
        ('$112,000 or less single; $224,000 or less joint',
         'No surcharge. Part B is the standard $209.40. Part D has no surcharge.'),
        ('$112,001 to $141,000 single; $224,001 to $282,000 joint',
         'Part B total $293.10 a month, which is $83.70 more. Part D surcharge $15.40.'),
        ('$141,001 to $177,000 single; $282,001 to $354,000 joint',
         'Part B total $418.80, which is $209.40 more. Part D surcharge $39.70.'),
        ('$177,001 to $212,000 single; $354,001 to $424,000 joint',
         'Part B total $544.40, which is $335.00 more. Part D surcharge $64.00.'),
        ('$212,001 to $499,999 single; $424,001 to $749,999 joint',
         'Part B total $670.00, which is $460.60 more. Part D surcharge $88.30.'),
        ('$500,000 or more single; $750,000 or more joint',
         'Part B total $711.80, which is $502.40 more. Part D surcharge $96.40.'),
    ]) + """
""" + irmaa_tiers() + """
      <h2>Where the 2025 income comes in</h2>

      <p>IRMAA looks back two years. The 2027 amounts are set from the 2025 return, which Social Security
      receives from the IRS. If the 2025 return is not available, the agency uses the most recent one it
      has. The income measure is modified adjusted gross income, which is the adjusted gross income on the
      return plus tax-exempt interest.</p>

      <p>That means the figure includes taxable withdrawals from traditional accounts, Roth conversions,
      capital gains, interest, dividends and the taxable part of Social Security. It does not include
      qualified withdrawals from a Roth account. A qualified charitable distribution from an IRA never
      enters adjusted gross income, which is why it comes up on
      <a href="/rmd-deadline">the required withdrawals page</a>. The rest of the rules, including how a
      person asks Social Security to use a more recent year after a life-changing event, are on
      <a href="/irmaa">the IRMAA page</a>.</p>

      <blockquote class="pull">
        <p>The surcharge is a cliff. One dollar over a threshold moves the whole premium to the next
        tier for the year.</p>
      </blockquote>

""" + AD_INLINE + """
      <h2>The rule behind the table</h2>

      <p>The tiers are not arbitrary dollar amounts. By law the standard Part B premium covers about 25%
      of average Part B costs, and each IRMAA tier raises the total to a larger share of those costs:
      35%, 50%, 65%, 80% and 85%. Divide each total by the standard premium and the pattern shows. The
      first tier is 1.4 times $209.40, and the top tier is 3.4 times it. Because the table is built from
      the standard premium, it moves every time that premium moves.</p>

      <p>The Part D amounts follow a similar structure, but they are set from the national average base
      premium for drug coverage and are paid on top of whatever plan a person chose.</p>

      <h2>What one step costs</h2>

      <p>A single filer with 2025 income of $112,001 pays $83.70 a month more for Part B than a filer at
      $112,000, and $15.40 more for Part D. That is $99.10 a month, or about <strong>$1,189</strong> over
      2027. The two filers differ by one dollar of income. The same logic repeats at each threshold in
      the table.</p>

      <p>Compared with 2026, the first-tier Part B surcharge rises from about $81 to $83.70, and the
      thresholds move up about $3,000 for a single filer and $6,000 for a joint return. The top tier
      total goes from $689.90 to $711.80.</p>

      <p>The thresholds are adjusted each year for inflation and rounded to the nearest $1,000, which is
      why $109,000 became $112,000 for a single filer and $218,000 became $224,000 for a joint return.
      The top tier begins at $500,000 single and $750,000 joint. The income tax numbers that moved on a
      similar schedule are on
      <a href="/tax-numbers-2027">the 2027 tax numbers page</a>.</p>

      <p>The 2027 premium reads the 2025 return, so the 2026 return that people file in the spring will
      set the 2028 amounts. A year in which income spikes is the one that is read two years later, and
      that is the sentence the <a href="/irmaa">IRMAA page</a> spends most of its length on.</p>

      <h2>How the Part D surcharge is paid</h2>

      <p>The Part D amount is paid to Medicare, not to the drug plan. It is deducted from a Social
      Security benefit or billed directly, regardless of how the plan premium is paid, and it applies
      to a Medicare Advantage plan that includes drug coverage as well. The Part B surcharge is added to
      the Part B premium. People who do not have the premium withheld from a benefit receive a bill.</p>

      <h2>Who is not in this table</h2>

      <p>The table above covers single filers and joint filers. Married people who file separately and
      lived with their spouse during the year are measured against a much narrower set of brackets, and the
      amounts for 2027 were not confirmed in enough sources to print here. Social Security&rsquo;s own
      notice lists the tier that applies to a given person.</p>

      <p>The Part A premium, the Part B deductible and the way the standard premium is set are on
      <a href="/part-b-premium-2027">the page on 2027 Part B costs</a>. The earnings that the same
      2025 return reports for Social Security purposes are a separate matter, covered on
      <a href="/earnings-test">the earnings test page</a>.</p>

      <h2>What to check</h2>

""" + check([
        'The 2027 surcharge starts above <strong>$112,000</strong> single or <strong>$224,000</strong> '
        'joint, measured on the <strong>2025</strong> return.',
        'There are five tiers. Part B totals run from <strong>$293.10</strong> to <strong>$711.80</strong> '
        'a month, and the Part D surcharge from <strong>$15.40</strong> to <strong>$96.40</strong>.',
        'Each step is a cliff: going over a threshold by a dollar moves the whole premium.',
        'The Part D surcharge goes to Medicare, not to your drug plan, and applies to Medicare Advantage '
        'plans with drug coverage too.',
        'The amount that applies to you is on the notice Social Security sends, not in a table.',
    ]) + """
      <p>The table is the rule. The notice is the decision, and it is made from a tax return that was
      filed more than a year before the premium takes effect.</p>
""",
    'sources': [
        ('CMS &mdash; 2027 Medicare Parts A &amp; B premiums and deductibles (fact sheet)',
         'https://www.cms.gov/newsroom/fact-sheets/2027-medicare-parts-b-premiums-deductibles'),
        ('Kiplinger &mdash; Medicare premiums 2027: IRMAA brackets and surcharges for Parts B and D',
         'https://www.kiplinger.com/retirement/medicare/medicare-premiums-irmaa-brackets-and-surcharges-part-b-and-d-2027'),
        ('AARP &mdash; Medicare&rsquo;s Part B premium increases slightly for 2027',
         'https://www.aarp.org/medicare/medicare-part-b-premium-2027/'),
        ('Social Security Administration &mdash; Medicare premiums: rules for higher-income beneficiaries',
         'https://www.ssa.gov/medicare/lower-irmaa'),
        ('CMS &mdash; 2026 Medicare Parts A &amp; B premiums and deductibles (IRMAA table, for comparison)',
         'https://www.cms.gov/newsroom/fact-sheets/2026-medicare-parts-b-premiums-deductibles'),
    ],
    'next': {'slug': 'irmaa',
             'title': 'The Medicare surcharge based on what you earned two years ago',
             'blurb': 'How the look-back works, why it is a cliff, and the form that asks for a more '
                      'recent year.'},
}
