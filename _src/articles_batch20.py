#!/usr/bin/env python3
"""Twentieth batch: two pieces tied to news in the last days of September 2026 --
CMS's 2027 Medicare Advantage / Part D cost projections (28 September, plus the
28 July Part D bid announcement and the April rate announcement), and the state
of the EU's ETIAS travel authorization (no start date; the EU Entry/Exit System
is what actually applies to Americans now).

cms.gov, europa.eu and aha.org are proxy-blocked here, so neither primary source
could be read directly. Verified per CLAUDE.md section 2: agreement across
independent reporting that traces back to the agency (AJMC, Becker's, AMCP and
Medicare Interactive for the CMS figures; AARP, Fragomen, Travel Weekly, iVisa
and Newsweek for ETIAS/EES). Where sources split -- ETIAS's age-70 fee cutoff --
the copy says so instead of picking one."""

from build_articles import facts, check, AD_INLINE

ARTICLES20 = {}

CHECKED20 = '1 October 2026'

# ------------------------------------------------------------ 2027 Medicare
ARTICLES20['medicare-2027-costs'] = {
    'title': 'The 2027 Medicare Plan Numbers, and What an Average Can&rsquo;t Tell You '
             '&mdash; The Second Half Guide',
    'eyebrow': 'Facts &amp; thresholds',
    'h1': 'The 2027 Medicare plan numbers, and what an average can&rsquo;t tell you',
    'dek': 'CMS projects lower average Medicare Advantage premiums for 2027, a Part D deductible of up to $700, '
           'and the end of a program that held standalone drug-plan premiums down. The national '
           'average is not a number any one plan charges.',
    'meta': '6 minute read &middot; Checked against CMS&rsquo;s announcements and independent '
            'reporting that cites them',
    'checked': '9 October 2026',
    'body': """      <p>On September 28, CMS published its projections for 2027 Medicare Advantage and Part D
      premiums. The headline is a decline: the average Medicare Advantage premium is projected to fall
      from $14.37 a month to $12.00. It is a real number from a real agency, and it is worth reading
      for what it is &mdash; a national average of projections, weighted across every plan in the
      country. It is not the price of any plan you can actually enroll in.</p>

""" + facts('The 2027 figures, at a glance', [
        ('Average Medicare Advantage premium', '$14.37 a month in 2026, projected at <strong>$12.00</strong> '
                                               'for 2027 &mdash; a 16.5% decline.'),
        ('Average Part D premium inside Advantage plans', '$11.32 in 2026, projected at about '
                                                          '<strong>$7</strong> &mdash; down 38%.'),
        ('Average standalone Part D premium', '$35.09 in 2026, projected at about <strong>$36</strong> '
                                              '&mdash; up less than a dollar.'),
        ('Part D deductible', 'Up to <strong>$700</strong> in 2027, from $615. That is the most a plan '
                              'may charge, not what every plan does.'),
        ('Part D out-of-pocket cap', '<strong>$2,400</strong> in 2027, from $2,100. It applies to '
                                     'standalone plans and Advantage plans with drug coverage alike.'),
        ('National base beneficiary premium', '<strong>$41.33</strong>, up $2.34 (6%). A formula input, '
                                              'not a bill &mdash; more on it below.'),
        ('Projected Advantage enrollment', 'About 34 million people, roughly 47% of everyone with '
                                           'Medicare &mdash; essentially flat.'),
        ('Open enrollment', '15 October &ndash; 7 December. Coverage for 2027 begins 1 January.'),
    ]) + """
      <h2>What an average is, and isn&rsquo;t</h2>

      <p>The Advantage and Part D premium figures are projections built from the bids plans submitted,
      averaged with each plan weighted by the enrollment it expects. That is a sound way to describe
      the market as a whole. It does not say what happens to a specific plan, and it can&rsquo;t.
      An average can fall while a particular plan&rsquo;s premium rises; that is arithmetic, not
      something CMS claimed. What the number tells you is which way the total moved.</p>

      <blockquote class="pull">
        <p>A falling national average and a rising price for your plan can both be true at once. The
        average only tells you which way the total moved.</p>
      </blockquote>

      <p>The premium is also one cost among several. Copays, deductibles, which doctors are in the
      network and which drugs sit on which tier all vary plan by plan, and none of them is in a
      premium average. Reading the $12.00 as &ldquo;Advantage costs less next year&rdquo; reads more
      into it than it contains.</p>

""" + AD_INLINE + """
      <h2>The part that is the same for everyone</h2>

      <p>The Part D numbers are different in kind, because they are set by rule rather than by
      averaging. The out-of-pocket cap rises to $2,400 and the defined standard deductible to a
      maximum of $700, which a plan may set lower, both finalized in CMS&rsquo;s April rate announcement. Once your covered drug costs reach the
      cap, your cost for the rest of that calendar year is zero. The deductible counts toward the
      cap; it does not sit on top of it. We cover how the cap works &mdash; and what it doesn&rsquo;t
      cover &mdash; in <a href="/drug-cap">The $2,100 Medicare drug cap</a>.</p>

      <h2>The program that ended</h2>

      <p>On July 28, CMS announced that the Part D Premium Stabilization Demonstration will end after
      2026. As CMS described it, the program had given standalone drug plans a $10 monthly premium
      reduction and limited how much any single plan&rsquo;s premium could rise in a year to $50.
      Those protections are gone for 2027.</p>

      <p>CMS still projects the average standalone premium to rise by under a dollar. That is a
      statement about the average. Whether a particular standalone plan&rsquo;s premium moves by
      more, now that the per-plan limit no longer applies, is something the plan&rsquo;s own 2027
      figures will answer and the national average will not.</p>

      <h2>What the $41.33 actually does</h2>

      <p>The national base beneficiary premium is not what anyone pays. It is the number the Part D
      formulas are built on &mdash; and the one that sets the late-enrollment penalty. If you go 63
      days or more without Part D or other creditable drug coverage after your initial enrollment period ends,
      the penalty is 1% of the base premium for each full month you went without, rounded to the
      nearest ten cents, added to your premium for as long as you have Part D.</p>

""" + facts('The same lapse, two years', [
        ('20 uncovered months, 2026', '20 &times; 1% &times; $38.99 = $7.80 a month'),
        ('20 uncovered months, 2027', '20 &times; 1% &times; $41.33 = $8.30 a month'),
        ('How long it lasts', 'Generally for as long as you have Part D. The dollar amount is '
                              'recalculated each year from the new base premium.'),
    ]) + """
      <h2>What no national figure can tell you</h2>

      <p>Your plan&rsquo;s own premium, drug list and network for 2027 are the things no national
      figure can supply. The 2027 plan information has been on Medicare.gov&rsquo;s Plan Finder since
      October 1, and CMS published the 2027 Star Ratings there on October 8. If your current plan is
      leaving your area, the notice was due by October 2 &mdash; see
      <a href="/ma-plan-exits-2027">More Medicare Advantage plans are disappearing for 2027</a>.
      Your plan&rsquo;s Annual Notice of Change, mailed by the end of September, lists next
      year&rsquo;s changes to your own coverage; <a href="/anoc-letter">The Medicare letter arriving
      in September</a> covers how to read it.</p>

      <p>The Part B premium for 2027 has not been announced either. The Medicare Trustees&rsquo; 2026
      report projected $209.50 a month, against $202.90 in 2026; CMS&rsquo;s official figure normally
      arrives in the fall. The projection is a forecast and the announcement can differ from it.</p>

      <h2>Where each number lives</h2>

""" + check([
        '<strong>Your plan&rsquo;s 2027 premium, deductible and copays:</strong> the Annual Notice of '
        'Change your plan mailed, and the Plan Finder on Medicare.gov. Not the national averages.',
        '<strong>Whether your plan continues:</strong> the non-renewal letter due by 2 October, if '
        'your plan is leaving.',
        '<strong>The $2,400 cap and the $700 deductible ceiling:</strong> set by CMS. The cap applies to '
        'every Part D plan; $700 is the most a plan may charge as a deductible, and your plan&rsquo;s '
        'own figure can be lower.',
        '<strong>The national averages above:</strong> CMS&rsquo;s projections &mdash; useful context '
        'for the market, not a quote for any plan.',
        '<strong>Open enrollment:</strong> 15 October through 7 December, with changes effective '
        '1 January. <a href="/open-enrollment">What the window is actually for</a>.',
    ]) + """
      <p>The averages will be quoted a great deal over the next few weeks. They are accurate
      descriptions of the whole country and weak predictions of your plan, and the figure that
      matters for you is the one printed on your own plan&rsquo;s page.</p>
""",
    'sources': [
        ('CMS &mdash; Medicare Advantage and Medicare Prescription Drug Programs Expected to Remain '
         'Stable in 2027',
         'https://www.cms.gov/newsroom/press-releases/medicare-advantage-medicare-prescription-drug-programs-expected-remain-stable-2027'),
        ('CMS &mdash; Medicare Part D 2027 National Average Monthly Bid Amount Information',
         'https://www.cms.gov/newsroom/fact-sheets/medicare-part-d-2027-national-average-monthly-bid-amount-information'),
        ('CMS &mdash; 2027 Medicare Advantage and Part D Rate Announcement (fact sheet)',
         'https://www.cms.gov/newsroom/fact-sheets/2027-medicare-advantage-part-d-rate-announcement'),
        ('AJMC &mdash; CMS Projects 16.5% Drop in 2027 Medicare Advantage Premiums',
         'https://www.ajmc.com/view/cms-projects-16-5-drop-in-2027-medicare-advantage-premiums'),
        ('Becker&rsquo;s Payer Issues &mdash; CMS projects lower Medicare Advantage premiums, flat '
         'enrollment for 2027',
         'https://www.beckerspayer.com/payer/medicare-advantage/cms-projects-lower-medicare-advantage-premiums-flat-enrollment-for-2027/'),
        ('AMCP &mdash; CMS Announces National Average Monthly Bid Amount and Conclusion of the Part D '
         'Premium Stabilization Demonstration',
         'https://www.amcp.org/regulatory-newsbreak/regulatory-newsbreak-cms-announces-national-average-monthly-bid-amount-and-conclusion-part-d-premium'),
        ('Medicare Interactive &mdash; The Part D late enrollment penalty',
         'https://www.medicareinteractive.org/wp-content/uploads/Part-D-LEP.pdf'),
    ],
    'next': {'slug': 'ma-plan-exits-2027',
             'title': 'More Medicare Advantage plans are disappearing for 2027',
             'blurb': 'The other half of the 2027 picture: whether the plan the average describes '
                      'will still exist for you.'},
}

# ---------------------------------------------------------------- ETIAS
ARTICLES20['etias'] = {
    'title': 'ETIAS: The EU Travel Authorization That Isn&rsquo;t Live Yet '
             '&mdash; The Second Half Guide',
    'eyebrow': 'Facts &amp; thresholds',
    'h1': 'ETIAS: the EU travel authorization that isn&rsquo;t live yet',
    'dek': 'Europe&rsquo;s new &euro;20 entry authorization has no start date, and websites are '
           'charging for it anyway. What does apply to Americans right now is a fingerprint check '
           'at the border.',
    'meta': '5 minute read &middot; Checked against EU announcements and independent travel and '
            'legal reporting',
    'checked': CHECKED20,
    'body': """      <p>If you have been reading about ETIAS &mdash; the European Travel Information and
      Authorisation System &mdash; you could be forgiven for thinking you need to apply this year.
      You do not. As of 1 October 2026 the system is not in operation, the European Union is not
      collecting applications, and it has not said when it will start.</p>

""" + facts('ETIAS, at a glance', [
        ('Status', 'Not in operation. The EU&rsquo;s official ETIAS page states that no applications '
                   'are being collected.'),
        ('Start date', 'None. The &ldquo;last quarter of 2026&rdquo; target was dropped from the '
                       'official page in July 2026, and 2027 is now the likely year.'),
        ('Fee, once it starts', '<strong>&euro;20</strong> per applicant, set by the European '
                                'Commission on 17 July 2025 &mdash; up from the original &euro;7.'),
        ('Who pays', 'Ages 18 through 70. Applicants under 18 or over 70 pay nothing, but still '
                     'have to apply.'),
        ('Validity', 'Three years, or until the linked passport expires, whichever comes first.'),
        ('Official site', '<strong>travel-europe.europa.eu</strong> (and the EU&rsquo;s own app). '
                          'Any other address is not the EU.'),
    ]) + """
      <h2>What it is</h2>

      <p>ETIAS is a pre-travel screening for people who do not need a visa to visit the Schengen
      area. It is not a visa. Nothing is stamped or mailed; an approval is a code tied electronically
      to your passport, good for short stays of up to 90 days in any 180. It is the EU&rsquo;s version
      of what the United States already asks of European visitors through ESTA, and once it is
      running it will apply to Americans.</p>

      <h2>Why there is no date</h2>

      <p>ETIAS depends on eu-LISA, the EU agency that builds and runs it, finishing its technical
      work. Reporting in July said the agency had concluded that a 2026 start was not achievable,
      and the &ldquo;last quarter of 2026&rdquo; wording disappeared from the official page. A
      revised schedule was expected after eu-LISA&rsquo;s September board meeting. None had
      appeared in the sources checked for this piece. The place a date will show up first is the
      official page itself.</p>

      <p>The UK trade press had also reported that the EU was set to delay ETIAS after problems
      with long lines under the other new border system, covered below. The two are connected:
      ETIAS was meant to arrive after that system settled in.</p>

      <p>The date has moved before. When Euronews reported the new &euro;7 fee in August 2022, the
      headline said travelers would not have to pay until autumn 2023. By March 2025 it described the
      system as delayed until 2026. Then came the fourth-quarter-2026 target, and now its removal.
      A start date that has been wrong several times is a reason to read the official page rather
      than a headline.</p>

      <h2>The part that is already costing people money</h2>

      <p>A permit with no start date is an ideal product for anyone willing to invent one. Websites
      that sell ETIAS applications exist, and the EU has warned about fraudulent ETIAS sites. The
      logic is not complicated: no application can be submitted because none is being collected, so a
      site that takes a payment today is not selling an ETIAS authorization.</p>

      <blockquote class="pull">
        <p>The real application will cost &euro;20 on an address ending in .europa.eu. Anything that
        costs more, or ends in anything else, is not it.</p>
      </blockquote>

      <p>The pattern is the familiar one: an official-looking page, a fee, a deadline that feels
      real. <a href="/five-minute-rule">Why scammers need you to act right now</a> covers why the
      deadline is always the tell.</p>

""" + AD_INLINE + """
      <h2>What does apply now: the Entry/Exit System</h2>

      <p>The change Americans will actually meet in Europe is not a form completed beforehand.
      The EU&rsquo;s Entry/Exit System, EES, has been fully operating at the external borders of the
      Schengen area since 10 April 2026. For a short stay:</p>

""" + facts('EES for a visa-exempt American', [
        ('First entry', 'A photo and four fingerprints are taken and linked to your passport. Children '
                        'under 12 are exempt from the fingerprints.'),
        ('Passport stamps', 'Generally no longer used for short stays the system covers. The record '
                            'is electronic.'),
        ('The 90-day limit', 'The system counts your days automatically against the 90-in-any-180 '
                             'rule.'),
        ('What you do beforehand', 'Nothing. There is no pre-registration and no fee.'),
        ('What to expect', 'Longer lines at some borders while countries adjust, as early travelers '
                           'reported.'),
    ]) + """
      <p>The 90-in-180 rule is the part that matters most to anyone who spends long stretches in
      Europe, and EES changes how it is enforced. The window rolls: on any given day the system looks
      back 180 days and counts the days you spent inside Schengen during that period, and the total
      may not exceed 90. If you spent 80 days there, left, and came back 20 days later, your 80 earlier
      days are still inside the lookback, so you would have only 10 days left until the earliest of
      them age out. The same arithmetic always applied; the difference now is that the system does
      the counting rather than a border officer reading stamps.</p>

      <h2>The age line is unsettled</h2>

      <p>Reporting is not uniform on the fee exemption for older travelers. The EU&rsquo;s own wording,
      as quoted by AARP and others, is applicants <em>under 18 or over 70</em>. AARP elsewhere
      summarizes it as 70 and older. Those differ for exactly one birthday. Until ETIAS is open and
      the application spells out the rule, the age-70 edge is not worth treating as settled.</p>

      <h2>What is true today</h2>

""" + check([
        '<strong>ETIAS is not required for any trip</strong> because it is not operating. There is '
        'nothing to buy.',
        '<strong>A site that takes payment for it now is not the EU.</strong> The real address ends '
        'in .europa.eu.',
        '<strong>What applies at the border is EES:</strong> a photo and four fingerprints on first '
        'entry, no stamp, no pre-registration.',
        '<strong>The fee, when it starts, is &euro;20</strong>, with an exemption for under-18 and '
        'over-70 applicants who still have to apply.',
        '<strong>Your passport still has to meet the entry rules.</strong> '
        '<a href="/passport-traps">The passport rules that turn people away at check-in</a> covers '
        'the ones that catch people.',
    ]) + """
      <p>For anyone planning a European trip in 2027 or later, the sensible note to keep is a short
      one: check the official ETIAS page before booking. It will say when the system is open, and it
      will be the only place that is certain to.</p>
""",
    'sources': [
        ('European Commission, Migration and Home Affairs &mdash; The European travel authorisation '
         'ETIAS will cost EUR 20 (17 July 2025)',
         'https://home-affairs.ec.europa.eu/news/european-travel-authorisation-etias-will-cost-eur-20-2025-07-17_en'),
        ('ETIAS (official EU site) &mdash; Frequently asked questions',
         'https://travel-europe.europa.eu/etias/faq'),
        ('AARP &mdash; What to Know About European ETIAS Application and Fee',
         'https://www.aarp.org/travel/travel-tips/etias-application-and-payment-information/'),
        ('Fragomen &mdash; European Union: Warning on Fraudulent ETIAS Websites',
         'https://www.fragomen.com/insights/european-union-warning-on-fraudulent-etias-websites.html'),
        ('iVisa News &mdash; EU removes ETIAS 2026 launch date from website',
         'https://www.ivisa.com/news/2026-07-20-eu-etias-launch-date-removed-website-delay'),
        ('Euronews &mdash; Americans and Brits hit with new &euro;7 EU entry fee, but won&rsquo;t have '
         'to pay until autumn 2023',
         'https://www.euronews.com/travel/2022/08/08/brits-and-americans-must-pay-7-to-travel-to-the-eu-from-2022'),
        ('Euronews &mdash; Everything travellers need to know about the EU&rsquo;s ETIAS scheme '
         '(March 2025)',
         'https://www.euronews.com/travel/2025/03/14/eus-etias-travel-authorisation-delayed-until-2026-heres-when-youll-have-to-pay'),
        ('Travel Weekly &mdash; EU &lsquo;set to delay&rsquo; Etias system after EES queue chaos',
         'https://travelweekly.co.uk/news/eu-set-to-delay-etias-system-after-ees-queue-chaos'),
        ('Newsweek &mdash; US tourists face fingerprinting, facial scans starting today',
         'https://www.newsweek.com/us-tourists-face-fingerprinting-facial-scans-from-today-11812044'),
    ],
    'next': {'slug': 'passport-traps',
             'title': 'The passport rules that turn people away at check-in',
             'blurb': 'The other entry rule, and the one that has nothing to do with ETIAS: what a '
                      'passport has to look like at the gate.'},
}
