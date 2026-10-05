#!/usr/bin/env python3
"""Twenty-first batch: two pieces from the first days of October 2026 --
the FTC's pre-Open-Enrollment warning about paid search ads that imitate
Medicare.gov and HealthCare.gov (consumer alert dated 28 September 2026), and the
mandatory Roth catch-up rule for workers 50+ who earned over the indexed
threshold in the prior year (final regulations; strict enforcement from 2027).

consumer.ftc.gov, irs.gov and cms.gov are proxy-blocked here, so no primary
source was read directly. Verified per CLAUDE.md section 2 by agreement across
independent results that trace to the agency. Where sources split -- the 2027
wage threshold, which the IRS had not announced at checking time and which only
projections put at $155,000 -- the copy says so instead of picking a number."""

from build_articles import facts, check, AD_INLINE

ARTICLES21 = {}

CHECKED21 = '3 October 2026'

# ------------------------------------------------------- paid search ad scam
ARTICLES21['search-ad-scam'] = {
    'title': 'The Medicare Website That Is Really an Ad &mdash; The Second Half Guide',
    'eyebrow': 'Facts &amp; thresholds',
    'h1': 'The Medicare website that is really an ad',
    'dek': 'The FTC&rsquo;s open-enrollment warning is about a scam that starts with a search, not a '
           'phone call: paid ads that sit above the real Medicare.gov and look official. Here is how '
           'to tell the difference in about two seconds.',
    'meta': '5 minute read &middot; Checked against the FTC&rsquo;s September 2026 consumer alert and '
            'independent reporting that cites it',
    'checked': CHECKED21,
    'recheck': {'due': '2026-11-02', 'why': 'Open enrollment is under way -- check for a newer FTC alert '
                'or enforcement action on paid-search impersonation.'},
    'body': """      <p>Most open-enrollment scam warnings are about the phone. The Federal Trade Commission&rsquo;s
      alert, published on September 28 ahead of Medicare and Marketplace open enrollment, is about
      something quieter: the search results page. Its point is simple. Scammers pay to appear at the top
      of search results, and a paid result can look a great deal like the real thing.</p>

      <p>Someone searching for &ldquo;Medicare plans&rdquo; in October is exactly who the ad is built for.
      The link goes to a page that borrows official-looking logos and keywords, or to a number that rings
      a call center. The FTC says a person who uses that link or number can end up paying for something
      that is not health insurance, or exposing personal information to medical identity theft.</p>

""" + facts('What the FTC alert says, at a glance', [
        ('Where it starts', 'A <strong>paid ad</strong> at the top of search results, not a call or a '
                            'letter.'),
        ('What it imitates', 'Medicare.gov and HealthCare.gov, using similar web addresses, official-'
                             'looking logos and the keywords you searched for.'),
        ('What it can cost you', 'Payment for a plan that is <strong>not health insurance</strong>, or '
                                 'medical identity theft.'),
        ('Official addresses', '<strong>Medicare.gov</strong> and <strong>HealthCare.gov</strong>. '
                               'Government sites end in .gov.'),
        ('Official phone', '<strong>1-800-633-4227</strong> (1-800-MEDICARE) for Medicare.'),
        ('Medicare open enrollment', '<strong>15 October &ndash; 7 December</strong>. The window '
                                     'when this traffic peaks.'),
        ('Where to report', 'ReportFraud.ftc.gov and your state attorney general; Medicare-related '
                            'scams also to Medicare at the number above.'),
    ]) + """
      <h2>What a paid result looks like</h2>

      <p>The surest route skips the results altogether. Typing <strong>medicare.gov</strong> into the
      browser&rsquo;s address bar yourself, or calling 1-800-MEDICARE, means no one has paid to put
      anything in front of you. Then check the address that actually loads: it should end in
      <strong>.gov</strong>.</p>

      <p>If you do search, a search engine labels paid placements, usually with a small &ldquo;Ad&rdquo;
      or &ldquo;Sponsored&rdquo; tag near the result. The tag is easy to miss and the page it leads to
      can be built to look like a government site. The FTC&rsquo;s practical advice is to scroll past
      anything marked that way and look for a result whose address ends in <strong>.gov</strong>.</p>

      <p>Not every ad is a scam. Plenty of paid results come from legitimate private businesses, such
      as brokers and insurers, that are simply unrelated to the government. The point is narrower: a
      paid result is not Medicare, and the official Plan Finder is free. Browsing plans and enrolling
      in one are different stages, and personal details, including a Medicare number, belong at the
      enrollment stage with a company or agent you chose, not on the first page a search ad
      sends you to.</p>

      <blockquote class="pull">
        <p>A paid result is not a government result. The only thing a search ad proves is that someone
        paid for the position.</p>
      </blockquote>

""" + AD_INLINE + """
      <h2>Why the ad works</h2>

      <p>An ad does not have to be a convincing forgery. It only has to be there at the moment a person
      is looking, with a headline that echoes the search, and a logo or a web address close enough to
      pass at a glance. People searching for plan information in the fall are doing something
      unfamiliar and a little stressful, and the first plausible result is the one most of them click.
      Search engines carry the ads because advertisers pay for the position, and the FTC&rsquo;s alert
      treats that as a fact about how the system works, not a defect in the reader.</p>

      <p>It is also not a new concern for the agency. FTC staff sent warning letters to 21 healthcare plan
      marketers and lead generators in December 2024, which the agency said did not allege that the
      recipients had broken the law, and the agency has run consumer alerts on
      open-enrollment scams in earlier years. It held a public roundtable on healthcare scams around
      open enrollment on September 29. The paid-search version is the part that has grown, because the
      ad can be placed in front of exactly the person searching.</p>

      <h2>Why October</h2>

      <p>Medicare open enrollment runs from 15 October to 7 December, and shopping for 2027 coverage
      sends millions of people to search engines at once. Marketplace open enrollment follows. The FTC
      has issued warnings of this kind in earlier years, and this year&rsquo;s adds the
      search-advertising angle plainly. The scheme depends on timing: the ad is waiting when a person
      who is already looking types in the query.</p>

      <p>It also pairs with the phone problem. A web form that collects a name and number is how a call
      center gets the list it dials later. That is one reason the sensible response is the same as for a
      cold call: be careful with a Medicare number, Social Security number or bank details: give them
      only to a company or agent you chose, reached through an address or number you verified yourself. The older piece on
      <a href="/enrollment-scams">why the phone rings more in October</a> covers the calling side.</p>

      <h2>If you already clicked</h2>

      <p>Clicking an ad is not the harm. The harm comes from what happens next: a payment, a Medicare
      or Social Security number typed into a form, a call to the number on the page. If you stopped
      before that point, there is nothing to undo. If you did not, the FTC&rsquo;s guidance is to report
      it at ReportFraud.ftc.gov and to your state attorney general, and to Medicare at 1-800-633-4227
      when Medicare is involved. A free State Health Insurance Assistance Program (SHIP) counselor can
      help sort out which coverage you actually have.</p>

      <p>If you gave out a Medicare or Social Security number, review your Medicare claims for services
      you did not receive, which is how medical identity theft usually shows up. If you think your
      identity has been misused, the FTC&rsquo;s IdentityTheft.gov walks through recovery steps, and the
      FTC has separate guidance on medical identity theft. Seeing an ad is not a reason to go there.</p>

      <h2>What to check</h2>

""" + check([
        'Go to <strong>Medicare.gov</strong> by typing the address, or by using a bookmark made once '
        'from a source you trust.',
        'If you do use a search engine, skip results marked <strong>Ad</strong> or '
        '<strong>Sponsored</strong> and check that the address ends in <strong>.gov</strong> before '
        'clicking.',
        'Be wary of a page that asks for payment, or for a Medicare number, before it shows you '
        'plans. The official Plan Finder is free.',
        'A free <strong>SHIP counselor</strong> or Senior Medicare Patrol volunteer can help with '
        'plan comparisons without selling you anything.',
        'If you were taken in, report it at <strong>ReportFraud.ftc.gov</strong> and to your state '
        'attorney general, and to Medicare at <strong>1-800-633-4227</strong> if Medicare is involved.',
    ]) + """
      <p>None of this requires technical skill. It requires noticing that the first result is not
      always the official one, a habit that costs two seconds and protects a number that cannot be
      reissued.</p>
""",
    'sources': [
        ('FTC &mdash; What to know ahead of Open Enrollment to avoid health insurance scams '
         '(Consumer Alert, September 2026)',
         'https://consumer.ftc.gov/consumer-alerts/2026/09/what-know-ahead-open-enrollment-avoid-health-insurance-scams'),
        ('FTC &mdash; Medicare Impersonators',
         'https://consumer.ftc.gov/medicare-impersonators'),
        ('FTC &mdash; How to avoid Medicare Open Enrollment scams (Consumer Alert, October 2023)',
         'https://consumer.ftc.gov/consumer-alerts/2023/10/how-avoid-medicare-open-enrollment-scams'),
        ('Bitdefender &mdash; FTC Warns of Fake Health Insurance Ads Online',
         'https://www.bitdefender.com/en-us/blog/hotforsecurity/fake-health-insurance-ads-ftc-warning'),
    ],
    'next': {'slug': 'enrollment-scams',
             'title': 'Why your phone rings more in October',
             'blurb': 'The calling side of the same season: what real Medicare agents can and cannot do.'},
}

# ------------------------------------------------------------- Roth catch-up
ARTICLES21['roth-catch-up'] = {
    'title': 'When Your 401(k) Catch-Up Must Go Into Roth &mdash; The Second Half Guide',
    'eyebrow': 'Facts &amp; thresholds',
    'h1': 'When your 401(k) catch-up must go into Roth, and what changes in 2027',
    'dek': 'The rule began in 2026: for workers 50 and older who earned more than a set amount from '
           'their employer the year before, catch-up contributions must go in as Roth. The detailed '
           'regulations apply from 2027, and some plans will not take catch-ups at all.',
    'meta': '6 minute read &middot; Checked against the IRS final regulations as reported by several '
            'plan administrators and law firms',
    'checked': CHECKED21,
    'recheck': {'due': '2026-11-15', 'why': 'The IRS normally announces next year\'s indexed limits in '
                'the fall -- replace the unconfirmed 2027 wage threshold with the official figure.'},
    'body': """      <p>A rule from the SECURE 2.0 Act changes how a certain group of older workers saves in a
      workplace plan. If you are 50 or older and earned more than a threshold in wages from your
      employer the previous year, any catch-up contribution you make must be a
      <strong>Roth</strong> contribution: after-tax, with no deduction up front.</p>

      <p>The requirement generally began on <strong>1 January 2026</strong>. The IRS&rsquo;s earlier
      administrative transition relief ended on 31 December 2025, and for 2026 plans are expected to
      follow a reasonable, good-faith reading of the statute. That is a standard for how plans
      comply, not a year in which the rule was optional. The final regulations, which spell out the
      details, generally apply beginning in 2027, with later dates for certain governmental and
      collectively bargained plans.</p>

""" + facts('The rule, at a glance', [
        ('Who', 'Participants <strong>50 or older</strong> in a 401(k), 403(b) or 457(b) '
                'plan whose prior-year wages from <em>that employer</em> exceeded the threshold.'),
        ('2026 threshold', '<strong>$150,000</strong> of prior-year (2025) wages, indexed from '
                           '$145,000 in the law.'),
        ('2027 threshold', 'Indexed again, and based on 2026 wages. At checking time the IRS had not '
                           'published it; some outside estimates say $155,000. Treat that as '
                           'unconfirmed.'),
        ('Which wages', 'Social Security (FICA) wages, <strong>Box 3 of the W-2</strong>, from the '
                        'employer sponsoring the plan. Generally not combined across employers; the '
                        'final regulations allow aggregation in specified cases, such as related '
                        'employers or a common paymaster.'),
        ('Self-employment income', 'Does not count. A sole proprietor or partner with no W-2 wages '
                                   'from the plan is outside the Roth-only rule.'),
        ('What changes', 'Catch-up contributions must be Roth. Regular contributions are unaffected '
                         'and may still be pre-tax.'),
        ('If the plan has no Roth option', 'Affected workers <strong>cannot make catch-up '
                                           'contributions</strong>. A plan is not required to add '
                                           'Roth.'),
        ('2026 catch-up limits', '<strong>$8,000</strong> for 50 and older, <strong>$11,250</strong> '
                                 'instead of that for ages 60 through 63.'),
    ]) + """
      <h2>Why the test is narrower than it sounds</h2>

      <p>Three details decide whether the rule applies, and each one is easy to get wrong.</p>

      <p><strong>It looks backward.</strong> Your status for a given year depends on what you earned
      the year before, so a raise this year does not change this year&rsquo;s treatment, and a drop in
      pay does not retroactively exempt you.</p>

      <p><strong>It is employer by employer.</strong> The test uses wages from the employer that
      sponsors the plan, and wages from separate employers are generally not added up. The final
      regulations make exceptions in specified situations, such as related employers or a common
      paymaster, so the plan administrator is the place to ask. Someone who changed jobs mid-year is
      measured against the new employer&rsquo;s plan using the pay that employer reported.</p>

      <p><strong>It counts W-2 wages only.</strong> Box 3 of the W-2 is the reference. Investment income
      and self-employment income are not part of the test, which is why a business owner reporting on
      Schedule C or a K-1 is outside the Roth-only requirement even when total income is high.</p>

      <blockquote class="pull">
        <p>The rule does not ask how much you earn. It asks how much your plan&rsquo;s sponsor paid you
        in FICA wages last year.</p>
      </blockquote>

""" + AD_INLINE + """
      <h2>Box 3 is not Box 1</h2>

      <p>The two wage boxes on a W-2 can differ by thousands of dollars for exactly the people this
      rule is about. Box 1 is taxable wages, which is <em>reduced</em> by pre-tax 401(k) deferrals. Box 3
      is Social Security wages, which is <em>not</em>: elective deferrals count as FICA wages. An
      employee paid $160,000 who put $24,500 into a pre-tax 401(k) shows about $135,500 in Box 1 and
      $160,000 in Box 3, before any other payroll adjustments. The regulations use the Box 3 figure,
      so a person can look below the line on Box 1 and still be above it. The test is wages that
      <em>exceed</em> the threshold: someone at exactly $150,000 in 2025 is not over it for 2026.</p>

      <h2>What stays the same</h2>

      <p>The rule is about the <em>type</em> of catch-up contribution, not the amount. The regular
      annual deferral limit, $24,500 in 2026, is unaffected, and it can still be pre-tax. Only the
      extra amount allowed at 50 and older is redirected to Roth for those over the line. Workers
      below the threshold keep whatever choice their plan already gave them. A Roth catch-up
      gives up the upfront income-tax exclusion that a pre-tax contribution carries, and qualified
      withdrawals later are tax-free. That does not mean the lifetime tax bill comes out the same, and
      the rule does not raise the amount that may be contributed. The 2026 figures above are labeled
      as 2026; the 2027 limits had not been officially published when this was checked.</p>

      <h2>The 60&ndash;63 window and the plan that has no Roth</h2>

      <p>The higher catch-up for ages 60 through 63, covered in the
      <a href="/catch-up-60-63">piece on the four-year window</a>, runs through the same rule. A worker in
      that age range above the wage threshold can still use the larger amount, but only as Roth, and
      only if the plan allows it.</p>

      <p>The plan option matters more than it first appears. Plans are not required to offer Roth
      deferrals. If yours does not and does allow catch-up contributions, workers over the threshold are
      effectively shut out of them, while workers under it are not. Whether a given plan will add a Roth
      feature is a decision for its sponsor, and the answer will be in the plan&rsquo;s own materials.</p>

      <h2>What to check</h2>

""" + check([
        'Find <strong>Box 3</strong> of last year&rsquo;s W-2 from the employer that sponsors the plan. '
        'That is the number the test uses, not Box 1.',
        'Compare it with the threshold for the contribution year. For 2026 it is $150,000; for 2027, '
        'wait for the IRS figure rather than relying on an estimate.',
        'Ask the plan administrator whether the plan <strong>offers a Roth option</strong> and '
        'how it will handle catch-up contributions.',
        'If you are self-employed or a partner with no W-2 wages from the plan, the Roth-only rule '
        'does not apply to you.',
        'A Roth catch-up is not deducted when contributed, so take-home pay can differ from a '
        'pre-tax contribution of the same size.',
    ]) + """
      <p>For most workers 50 and older the rule changes nothing. For those above the line it changes
      the form the contribution takes, and for those whose plan has no Roth option it decides whether
      they can make one at all.</p>
""",
    'sources': [
        ('Trucker Huss &mdash; The Roth Catch-Up Regulations Are Final',
         'https://www.truckerhuss.com/newsletter/roth-catchup-regulations/'),
        ('Kahn Litwin &mdash; IRS, Treasury issue final regulations on Roth catch-up contributions '
         'under SECURE 2.0',
         'https://kahnlitwin.com/blogs/tax-blog/irs-treasury-issue-final-regulations-on-roth-catch-up-contributions-under-secure-2-0'),
        ('Voya &mdash; IRS issues final regs on mandatory age 50+ Roth catch-up and increased '
         'catch-up contributions',
         'https://www.voya.com/voya-insights/irs-issues-final-regs-mandatory-age-50-roth-catch-and-increased-catch-contributions'),
        ('CAPTRUST &mdash; Mandatory Roth Catch-Up Q&amp;A',
         'https://www.captrust.com/resources/mandatory-roth-catch-up-qa/'),
        ('NAPA &mdash; 2027 Retirement Contribution Limits Come into Focus',
         'https://www.napa-net.org/news/2026/9/2027-retirement-contribution-limits-come-into-focus/'),
    ],
    'next': {'slug': 'catch-up-60-63',
             'title': 'The four-year 401(k) catch-up window at 60&ndash;63',
             'blurb': 'The larger catch-up amount, and the four years it applies.'},
}
