#!/usr/bin/env python3
"""Fifteenth batch: two pieces built around real September 2026 developments
in the run-up to Medicare's Annual Enrollment Period, checked against CMS's
own rate/negotiation materials and multiple independent insurer/trade-press
reports. A candidate on updated 2027 COLA estimates was dropped this week --
the August CPI-W release (scheduled September 11) produced conflicting,
unconfirmed figures across sources at checking time, not a clean update
worth publishing over last week's still-accurate piece."""

from build_articles import facts, check, AD_INLINE

ARTICLES15 = {}

CHECKED15 = '11 September 2026'

# --------------------------------------------------------- MA plan exits 2027
ARTICLES15['ma-plan-exits-2027'] = {
    'title': 'More Medicare Advantage Plans Are Disappearing for 2027 '
             '&mdash; The Second Half Guide',
    'eyebrow': 'Facts &amp; thresholds',
    'h1': 'More Medicare Advantage plans are disappearing for 2027',
    'dek': 'Several major insurers are pulling Medicare Advantage plans out of markets for 2027, '
           'well over a million members combined. If yours is one of them, the letter saying so is '
           'arriving now &mdash; and it starts a clock most people don&rsquo;t know about.',
    'meta': '6 minute read &middot; Verified against CMS rate data and multiple insurer announcements',
    'checked': CHECKED15,
    'body': """      <p>Last week&rsquo;s note about the Annual Notice of Change covered the routine version of this
      letter &mdash; premium shifts, formulary tweaks, network changes. This year, for a meaningful number
      of people, the letter says something bigger: the plan itself won&rsquo;t exist in 2027.</p>

      <p>Several of the largest Medicare Advantage insurers have confirmed 2027 market exits, and the
      combined number of affected members is well into seven figures.</p>

""" + facts('Who is pulling back, and by how much', [
        ('Humana', 'Confirmed exits affecting about <strong>600,000</strong> members nationally for 2027 '
                   '&mdash; the majority in plans rated 3.5 stars or lower.'),
        ('UnitedHealthcare', 'A preliminary 2027 list covering roughly <strong>34 counties across 12 '
                             'states</strong>, affecting more than 20,000 members.'),
        ('Molina Healthcare', 'Exiting its Medicare Advantage Part D product entirely for 2027, to focus '
                              'exclusively on its dual-eligible line.'),
        ('September 30', 'The deadline for your plan to notify you in writing, by law, if it is leaving '
                         'your area for 2027 &mdash; the same deadline covered in last week&rsquo;s ANOC '
                         'piece.'),
    ]) + """
      <p>These three are the confirmed, named exits as of this writing. Other insurers have signaled
      smaller pullbacks in specific counties, and the full national picture won&rsquo;t be final until
      plans file their complete 2027 bids. The reliable way to find out whether your own plan is affected
      isn&rsquo;t a headline number &mdash; it&rsquo;s the letter arriving from your plan by September 30,
      or a direct check at the Medicare Plan Finder once 2027 plans are listed.</p>

      <p>This also isn&rsquo;t a new pattern starting this year. For the 2026 plan year, roughly 2.9
      million Medicare Advantage enrollees in standard HMO and PPO plans faced forced disenrollment
      nationally &mdash; about 10% of that group, against a roughly 1% average annual rate from 2018
      through 2024. Rural beneficiaries were hit hardest: they made up about 14% of typical enrollees but
      nearly 23% of those whose plans were terminated. The 2027 wave described above is a continuation of
      that trend, not a one-year event.</p>

      <h2>Why, in a year CMS actually paid insurers more</h2>

      <p>The obvious assumption is that Medicare cut payments and insurers left in response. That isn&rsquo;t
      what happened. CMS finalized the 2027 Medicare Advantage payment rate at <strong>+2.48%</strong>
      &mdash; over $13 billion more industry-wide &mdash; a larger increase than insurers had been told to
      expect in the earlier proposal.</p>

      <p>The exits are happening anyway, and the detail that explains it is which plans are leaving:
      overwhelmingly the lower-rated ones. This reads less like a funding crisis and more like insurers
      trimming plans that were losing money regardless of the overall payment environment &mdash; margin
      recovery on specific underperforming products, not a broad retreat from Medicare Advantage.</p>

      <blockquote class="pull">
        <p>CMS raised Medicare Advantage payments for 2027. Insurers are still leaving markets anyway
        &mdash; which says more about which specific plans were losing money than about the year&rsquo;s
        overall funding.</p>
      </blockquote>

""" + AD_INLINE + """
      <h2>What happens automatically if your plan leaves</h2>

      <p>If your Medicare Advantage plan exits your area, you don&rsquo;t lose Medicare &mdash; coverage
      reverts automatically to <strong>Original Medicare</strong> (Parts A and B) on the date your plan
      ends. What it doesn&rsquo;t include automatically is drug coverage; Original Medicare has no Part D
      built in, so without action you could be without prescription coverage.</p>

      <p>Two protections follow specifically from the plan leaving, not from anything you have to prove
      about your own health:</p>

      <ul>
        <li><strong>A federal guaranteed-issue right to buy a Medigap policy.</strong> When your Medicare
        Advantage plan leaves Medicare or stops serving your area, federal law entitles you to buy a
        Medigap policy without medical underwriting &mdash; an insurer can&rsquo;t deny you or charge more
        for a pre-existing condition in this specific situation.</li>
        <li><strong>A Special Enrollment Period</strong> to pick a new Medicare Advantage plan or add a
        standalone Part D drug plan.</li>
      </ul>

      <p>Some states go further than the federal minimum. Maine extends the standard one-year Medicare
      Advantage trial period to three years before medical underwriting can apply. California lets
      Medicare Advantage enrollees buy a Medigap policy from the same insurer, without underwriting, if
      that plan reduced benefits, raised cost-sharing, or dropped a provider who was treating them &mdash;
      a broader trigger than a full market exit. Neither example is universal; what your own state actually
      guarantees is worth a direct call to your state insurance department or a SHIP counselor rather than
      assuming the federal floor is the whole picture.</p>

      <h2>The SEP timing depends on when your plan actually ends</h2>

""" + facts('Two different SEP windows', [
        ('Plan ends December 31', 'SEP runs from <strong>December 8</strong> &mdash; the day after AEP '
                                  'closes &mdash; through the <strong>end of February</strong>.'),
        ('Plan ends mid-year', 'SEP runs from <strong>one month before</strong> the termination date '
                               'through <strong>two months after</strong> it.'),
    ]) + """
      <p>Outside either of these SEPs, changing Medicare Advantage plans generally means waiting for the
      next Annual Enrollment Period. That&rsquo;s the reason the termination date matters as much as the
      fact of termination itself &mdash; miss the window tied to your specific date, and the next chance is
      months away.</p>

      <h2>What to actually check</h2>

""" + check([
        'Read your <strong>ANOC or termination letter</strong> closely enough to know which case applies: '
        'is your plan changing, or ending entirely?',
        'If it&rsquo;s ending, note the <strong>exact termination date</strong> &mdash; that date sets '
        'your SEP window, and the two scenarios above run on different clocks.',
        'If you want a Medigap policy, the guaranteed-issue right tied to a plan leaving your area is '
        'time-limited. Don&rsquo;t assume it waits for you.',
        'Without action, you will have <strong>Original Medicare with no drug coverage</strong> starting '
        'the day your plan ends. If you take any prescriptions, treat picking a new Part D option as '
        'urgent, not optional.',
        'A free <strong>SHIP counselor</strong> (<em>shiphelp.org</em>) can walk through your specific '
        'letter with you at no cost and no commission on whatever you choose next.',
    ]) + """
      <p>None of this is optional reading. A routine ANOC asks you to notice a few numbers changed. A
      termination letter starts a clock, and the clock doesn&rsquo;t wait for December 7 if your plan ends
      mid-year.</p>
""",
    'sources': [
        ('Becker&rsquo;s Payer Issues &mdash; Humana to exit Medicare Advantage plans covering 600,000 '
         'members in 2027',
         'https://www.beckerspayer.com/payer/medicare-advantage/humana-to-exit-medicare-advantage-plans-covering-600000-members-in-2027/'),
        ('Becker&rsquo;s Hospital Review &mdash; 4 insurers exiting Medicare Advantage markets',
         'https://www.beckershospitalreview.com/finance/4-insurers-exiting-medicare-advantage-markets/'),
        ('CMS &mdash; 2027 Medicare Advantage and Part D Rate Announcement (fact sheet)',
         'https://www.cms.gov/newsroom/fact-sheets/2027-medicare-advantage-part-d-rate-announcement'),
        ('National Council on Aging &mdash; What are the Medicare Advantage Special Enrollment Periods?',
         'https://www.ncoa.org/article/medicare-advantage-special-enrollment-periods/'),
        ('Q1Medicare &mdash; Am I granted a Special Enrollment Period when CMS terminates my Medicare '
         'Advantage plan&rsquo;s contract?',
         'https://q1medicare.com/faq/FAQ.php?faq=SEP-for-CMS-terminates-Medicare-Advantage-plans&faq_id=160'),
        ('Yahoo News &mdash; Millions of US Medicare Advantage enrollees forced to switch plans, study finds',
         'https://www.yahoo.com/news/articles/millions-us-medicare-advantage-enrollees-165838125.html'),
    ],
    'next': {'slug': 'anoc-letter',
             'title': 'The Medicare letter arriving in September, and why it&rsquo;s worth reading',
             'blurb': 'What the routine version of this letter covers, and the September 30 deadline '
                      'behind both pieces.'},
}

# ------------------------------------------------------- drug negotiation 2027
ARTICLES15['drug-negotiation-2027'] = {
    'title': 'The Next Round of Medicare Drug Discounts Arrives in January '
             '&mdash; The Second Half Guide',
    'eyebrow': 'Facts &amp; thresholds',
    'h1': 'The next round of Medicare drug discounts arrives in January',
    'dek': 'CMS finalized these prices with manufacturers back in late 2025. January 1 is when 15 more '
           'drugs &mdash; including Ozempic and Wegovy &mdash; actually get cheaper for Medicare. What '
           'the negotiated price is, and isn&rsquo;t, before you compare 2027 plans this fall.',
    'meta': '6 minute read &middot; Verified against CMS&rsquo;s own selected-drug list',
    'checked': CHECKED15,
    'body': """      <p>This isn&rsquo;t breaking news &mdash; CMS finished negotiating this round of Medicare drug
      prices with manufacturers in late 2025, and it hasn&rsquo;t changed since. What makes it worth
      covering now is the date attached to it: the second round of negotiated prices takes effect
      <strong>January 1, 2027</strong>, which lands right in the middle of this fall&rsquo;s plan-comparison
      season.</p>

      <p>The negotiation itself is Medicare doing something it was barred from doing for decades: for the
      first time under a 2022 law, the government directly negotiates prices with drug manufacturers for a
      short list of the highest-cost, highest-volume drugs in Part D each year. Round one covered ten
      drugs, effective since January 2026. Round two is the second annual group, effective January 2027,
      and a third round is already underway for 2028.</p>

""" + facts('The second round, at a glance', [
        ('15 drugs', 'Selected for the second round of Medicare drug price negotiation, agreements '
                    'finalized with manufacturers by November 2025.'),
        ('January 1, 2027', 'When the negotiated prices actually take effect.'),
        ('Ozempic, Wegovy, Rybelsus', 'The GLP-1 diabetes and weight-loss drugs in this round &mdash; '
                                      'Medicare&rsquo;s negotiated price drops from a $959 list price to '
                                      '<strong>$274</strong> for a 30-day supply, about a 71% cut.'),
        ('38% &ndash; 85%', 'The discount range across all 15 drugs versus list price; average discount '
                            'about 52%.'),
        ('~5.3 million', 'Medicare enrollees who used one of these 15 drugs in the year CMS used to '
                         'calculate the savings.'),
    ]) + """
      <h2>What &ldquo;negotiated price&rdquo; actually means for you</h2>

      <p>The number CMS announces is the <strong>Maximum Fair Price</strong> &mdash; what Medicare and Part
      D plans pay for the drug, not necessarily the amount that shows up at your pharmacy counter. What you
      actually pay still depends on your specific plan, your deductible, and where you are in the coverage
      year &mdash; the same structure covered on <a href="/drug-cap">the $2,100 drug cap page</a>. A lower
      negotiated price lowers the cost the whole system is paying, which over time affects premiums and
      formularies, but it is not a guarantee of a specific copay.</p>

      <p>Concretely, that means a negotiated price changes the number underneath every phase of Part D
      coverage &mdash; the deductible, the initial coverage period, and the point at which the annual
      out-of-pocket threshold kicks in. Whether that translates into a smaller bill for you personally
      depends on how your plan structures cost-sharing for that drug: a plan that charges a percentage of
      the drug&rsquo;s cost (common for higher, &ldquo;specialty&rdquo; tiers) passes a lower negotiated
      price straight through as a lower copay. A plan that charges a flat dollar amount per tier doesn&rsquo;t
      automatically do that &mdash; the flat copay is set by the plan, not derived directly from the
      negotiated price. Either way, the negotiated price is real; what it does to your specific bill is a
      question your plan&rsquo;s formulary answers, not this article.</p>

      <blockquote class="pull">
        <p>A negotiated price is what Medicare pays the manufacturer. What you pay at the counter is still
        decided by your plan, your deductible, and the calendar.</p>
      </blockquote>

""" + AD_INLINE + """
      <h2>Why the GLP-1 drugs are the headline of this round</h2>

      <p>Ozempic, Wegovy and Rybelsus are all versions of the same drug, semaglutide, from Novo Nordisk
      &mdash; prescribed at enormous volume for type 2 diabetes and, in Wegovy&rsquo;s case, weight
      management. Round two also includes Dupixent, a widely prescribed treatment for eczema, asthma and
      related conditions. Round one, effective since January 2026, covered ten drugs including blood
      thinners and diabetes medications like Eliquis (list $521, negotiated $231) and Jardiance (list $573,
      negotiated $197). Round two&rsquo;s roughly 71% cut on the semaglutide drugs is a bigger single
      reduction on a more widely prescribed class of medication than anything in the first round.</p>

      <p>Round one is also the closest thing to evidence for how round two will actually play out, since
      it has now run for most of a year. CMS has estimated it produced roughly $6 billion in program
      savings and $1.5 billion in out-of-pocket savings for beneficiaries with Part D coverage in 2026.
      That doesn&rsquo;t mean every individual saw a lower bill &mdash; it&rsquo;s an aggregate figure,
      shaped by formulary placement and where each person was in their coverage year &mdash; but it&rsquo;s
      a real result from the same mechanism about to apply to a second, larger group of drugs.</p>

      <h2>What to actually check this fall</h2>

""" + check([
        'Check whether a drug you take is one of the <strong>15 selected for round two</strong> &mdash; '
        'CMS publishes the full list, and this piece names only the highest-volume ones.',
        'A lower negotiated price does not automatically mean a lower <strong>tier or copay</strong> on '
        'your specific plan next year. Confirm your actual 2027 cost through your ANOC or the Medicare '
        'Plan Finder, not through the headline discount.',
        'If you&rsquo;re comparing plans for 2027, a drug moving to a negotiated price is one more reason '
        'to re-run the <strong>Plan Finder</strong> with your actual prescription list rather than '
        'assuming last year&rsquo;s best-fit plan is still the best fit.',
        'Round one&rsquo;s prices (Eliquis, Jardiance and eight others) have already been in effect since '
        'January 2026 &mdash; if you take one of those, the discount is not new for 2027.',
    ]) + """
      <p>The decision here was made almost a year ago. What changes on January 1 is that it stops being a
      number in a CMS press release and starts being the price your plan is actually paying &mdash; which
      is the part worth knowing before, not after, you pick a 2027 plan. A round three list, covering 15
      more drugs with prices effective January 1, 2028, was already announced in January 2026 &mdash; this
      program is now a recurring annual event, not a one-time change, and each fall&rsquo;s plan comparison
      is likely to have a new round to account for going forward.</p>
""",
    'sources': [
        ('CMS &mdash; Medicare Drug Price Negotiation Program: Selected Drugs for Initial Price '
         'Applicability Year 2027 (fact sheet)',
         'https://www.cms.gov/files/document/factsheet-medicare-negotiation-selected-drug-list-ipay-2027.pdf'),
        ('CMS &mdash; Selected Drugs and Negotiated Prices',
         'https://www.cms.gov/initiatives/medicare-prescription-drug-affordability/overview/medicare-drug-price-negotiation-program/selected-drugs-negotiated-prices'),
        ('Managed Healthcare Executive &mdash; CMS negotiates a 70% discount for Ozempic and Wegovy',
         'https://www.managedhealthcareexecutive.com/view/cms-negotiates-a-70-discount-for-ozempic-and-wegovy'),
        ('Medicare Rights Center &mdash; Negotiated prices take effect for ten drugs in 2026',
         'https://www.medicarerights.org/medicare-watch/2025/10/09/negotiated-prices-take-effect-for-ten-drugs-in-2026'),
    ],
    'next': {'slug': 'drug-cap',
             'title': 'The $2,100 drug cap: real protection, narrower than it sounds',
             'blurb': 'What the out-of-pocket cap covers and what it doesn&rsquo;t &mdash; the structure '
                      'a negotiated price plugs into, not a replacement for it.'},
}
