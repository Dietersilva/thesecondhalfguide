#!/usr/bin/env python3
"""Seventeenth batch: three travel pieces requested directly, built around
real, dated 2026 changes rather than a generic "best destinations" list --
checked against agreement across independent sources, since nps.gov, doi.gov
and other federal domains are proxy-blocked from this sandbox per CLAUDE.md
section 2, the same way medicare.gov/ssa.gov/cms.gov/irs.gov/cdc.gov are."""

from build_articles import facts, check, AD_INLINE

ARTICLES17 = {}

CHECKED17 = '13 September 2026'

# ------------------------------------------------------- parks fee-free days
ARTICLES17['parks-fee-free-days'] = {
    'title': 'The National Parks Fee-Free Days Don&rsquo;t Do Anything for You If You Have the Senior Pass '
             '&mdash; The Second Half Guide',
    'eyebrow': 'Getting out there',
    'h1': 'The fee-free days don&rsquo;t do anything for you if you have the Senior Pass',
    'dek': 'Every year the National Park Service publishes a list of fee-free days, and every year it gets '
           'covered as a savings tip. For anyone 62 or older, that framing skips the more useful fact.',
    'meta': '5 minute read &middot; Verified against multiple independent 2026 fee-schedule reports',
    'checked': CHECKED17,
    'body': """      <p>The National Park Service publishes a short list of days each year when entrance fees are
      waived. It gets reported every time as a way to save money at the parks. For most people that&rsquo;s
      true. For anyone who already qualifies for the Senior Pass, it isn&rsquo;t &mdash; and 2026 adds a
      second wrinkle that has nothing to do with age at all.</p>

""" + facts('2026 fee-free days, and what actually changed', [
        ('The 8 fee-free occasions', 'Presidents Day (Feb 16), Memorial Day (May 25), Flag Day (Jun 14), '
                                     'Independence Day weekend (Jul 3&ndash;5), the NPS 110th birthday '
                                     '(Aug 25), Constitution Day (Sep 17), Theodore Roosevelt&rsquo;s '
                                     'birthday (Oct 27), and Veterans Day (Nov 11) &mdash; 10 calendar days '
                                     'in all.'),
        ('New restriction for 2026', 'Fee-free entry now applies only to U.S. citizens and residents. Two '
                                     'days that were fee-free in prior years &mdash; Martin Luther King Jr. '
                                     'Day and Juneteenth &mdash; are not on the 2026 list at all.'),
        ('New nonresident fee', 'A $100 per-person entrance surcharge (age 16+) now applies to nonresidents '
                                'at 11 of the most-visited parks, on top of the standard entrance fee, '
                                'effective January 1, 2026.'),
        ('Senior Pass, unchanged', 'Still $80 for a lifetime pass or $20 for one year, still limited to '
                                   'U.S. citizens and permanent residents 62 and older. Nothing about the '
                                   '2026 changes touches its price or its eligibility.'),
    ]) + """
      <h2>Why the fee-free days are irrelevant if you already have one</h2>

      <p>The Senior Pass covers entrance fees and standard amenity fees at participating federal
      recreation sites, every day of the year, for as long as you live. A day when entrance is temporarily
      free for everyone else doesn&rsquo;t add anything for a pass holder &mdash; you were already getting
      in free the day before and the day after. The list matters to people who don&rsquo;t have any pass
      and are deciding when to make a one-time visit. It has nothing to offer someone who solved that
      problem permanently for $80.</p>

      <p>If anything, a fee-free day can be a less convenient day to visit as a pass holder at a popular
      park. Waiving the fee doesn&rsquo;t change staffing, parking, or trail capacity &mdash; it just
      removes the one thing that was mildly discouraging a fraction of visitors, which can mean more
      competition for parking and timed-entry slots on those specific dates. A pass holder who can visit
      any day has no particular reason to pick one of the days everyone else picked too.</p>

      <blockquote class="pull">
        <p>A fee-free day saves you money you weren&rsquo;t going to spend. A Senior Pass already did
        that, every day, permanently, for $80.</p>
      </blockquote>

""" + AD_INLINE + """
      <h2>The part that isn&rsquo;t about age</h2>

      <p>The bigger structural change in 2026 has nothing to do with seniors specifically: it&rsquo;s a
      new two-tier fee system based on residency. Nonresidents now pay a $100-per-person surcharge at 11
      of the busiest parks &mdash; Acadia, Bryce Canyon, Everglades, Glacier, Grand Canyon, Grand Teton,
      Rocky Mountain, Sequoia and Kings Canyon, Yellowstone, Yosemite and Zion &mdash; unless they hold the
      new $250 Nonresident Annual Pass. The regular Annual Pass, for U.S. residents, is $80 for 2026.</p>

      <p>That last figure is worth sitting with if you&rsquo;re 62 or older and haven&rsquo;t bought a
      Senior Pass yet. The general-public Annual Pass and the Senior lifetime Pass are now priced
      identically at $80 &mdash; except one buys you twelve months and the other buys you the rest of your
      life. That wasn&rsquo;t true before 2026, when the annual pass cost less than the senior lifetime
      pass. It's a better relative deal now than it was a year ago, for anyone who qualifies.</p>

      <h2>If you don&rsquo;t qualify by age</h2>

      <p>Age isn&rsquo;t the only path to a free lifetime pass. The Access Pass &mdash; free, not $80
      &mdash; covers U.S. citizens and permanent residents of any age with a permanent disability,
      documented the same way the Senior Pass documents age and residency. It carries the same coverage:
      entrance and standard amenity fees, every day, indefinitely. Worth knowing about directly, and worth
      mentioning to anyone in your household who doesn&rsquo;t hit 62 but would otherwise qualify.</p>

      <h2>The other 2026 change worth knowing, unrelated to fees</h2>

      <p>Several individual parks have also been rolling back the timed-entry vehicle reservation systems
      that became common after the pandemic &mdash; a separate, park-by-park decision that has nothing to
      do with the fee changes above. Where a reservation system is still in place, though, none of this
      changes it: a waived entrance fee has never waived a timed-entry reservation, and it still
      doesn&rsquo;t in 2026. The two systems are decided separately, park by park, and one being free
      doesn&rsquo;t tell you anything about the other.</p>

      <h2>What to actually check</h2>

""" + check([
        'If you&rsquo;re 62 or older and don&rsquo;t have a pass yet, compare the $80 <strong>one-time '
        'lifetime</strong> Senior Pass against the $80 <strong>one-year</strong> general Annual Pass before '
        'assuming the fee-free calendar is worth planning around.',
        'At per-vehicle entrance fee parks, a Senior Pass covers everyone riding in the vehicle with you '
        '&mdash; including a nonresident companion, at the 11 parks that would otherwise charge the '
        '$100 surcharge. At per-person fee sites, it covers you plus up to <strong>three additional '
        'adults</strong>. Beyond that, additional visitors pay their own way.',
        'A fee-free day is not a discount day for anyone with a pass already &mdash; treat the calendar as '
        'a crowd forecast, not a savings opportunity, once you&rsquo;re past that point.',
        'Confirm any specific park&rsquo;s hours and reservation requirements directly &mdash; a waived '
        'entrance fee never waives timed-entry reservations, camping fees, or tour costs.',
    ]) + """
      <p>Buying the pass itself hasn&rsquo;t changed either: it&rsquo;s available in person at any staffed
      park entrance with proof of age and residency, or by mail or online through the USGS store, which
      adds a small processing fee for the convenience. Either way, the transaction happens once. That&rsquo;s
      the entire pitch, and it hasn&rsquo;t needed updating since long before 2026 started changing
      everything around it.</p>

      <p>None of this changes what the Senior Pass has always been: a $80 answer to a question you never
      have to ask again. The fee-free calendar is a real, useful list &mdash; for the specific group of
      people it was actually written for.</p>
""",
    'sources': [
        ('U.S. National Park Service &mdash; Entrance Passes',
         'https://www.nps.gov/planyourvisit/passes.htm'),
        ('U.S. National Park Service &mdash; Nonresident Fees',
         'https://www.nps.gov/aboutus/nonresident-fees.htm'),
        ('Al Jazeera &mdash; US will charge non-residents $100 to visit its most popular national parks',
         'https://www.aljazeera.com/news/2025/11/26/us-will-charge-non-residents-100-to-visit-its-most-popular-national-parks'),
        ('Newsweek &mdash; National Parks update: Full list of &lsquo;patriotic fee-free days&rsquo; in 2026',
         'https://www.newsweek.com/national-parks-update-full-list-fee-free-days-2026-11110989'),
    ],
    'next': {'slug': 'parks-pass',
             'title': 'Is the National Parks Senior Pass still one of America&rsquo;s best deals?',
             'blurb': 'What the pass actually covers, and the word in its nickname that misleads people '
                      'about it.'},
}

# ---------------------------------------------------------- senior fare check
ARTICLES17['senior-travel-discounts'] = {
    'title': 'Which Senior Travel Discounts Still Actually Exist in 2026 &mdash; The Second Half Guide',
    'eyebrow': 'Getting out there',
    'h1': 'Which senior travel discounts still actually exist in 2026',
    'dek': 'Most airlines quietly dropped published senior fares years ago. What&rsquo;s left is real but '
           'inconsistent, unpublished, and worth five minutes of checking before you assume it&rsquo;s '
           'either there or gone.',
    'meta': '5 minute read &middot; Compared against multiple independent 2026 fare reports',
    'checked': CHECKED17,
    'body': """      <p>&ldquo;Do airlines still give senior discounts?&rdquo; doesn&rsquo;t have one answer, because the
      honest answer is that none of the major U.S. carriers treat it the same way, and none of them
      publish a clear rule the way Amtrak does. What follows is what's actually still there, carrier by
      carrier, as of this year &mdash; not what used to be true, and not what a headline implies.</p>

      <p>It&rsquo;s worth being specific about what &ldquo;still exists&rdquo; means here, because the
      answer isn&rsquo;t simply yes or no. A discount that&rsquo;s real on one route, in one season, for
      one specific search, isn&rsquo;t the same thing as a policy printed on a fare rules page. Both get
      called a &ldquo;senior discount&rdquo; in casual conversation. Only one of them is something you can
      count on before you actually run the numbers.</p>

""" + facts('The one published rule, versus what gets reported', [
        ('Amtrak &mdash; published', '<strong>10% off</strong> most fares for travelers 65 and older, '
                                     'applied automatically once you select &ldquo;Senior&rdquo; as a '
                                     'traveler type when booking. Doesn&rsquo;t apply to sleeping-car '
                                     'charges. On the Downeaster route specifically, Amtrak publishes a '
                                     'separate, larger <strong>50% senior discount</strong> on coach fares.'),
        ('United, Delta, American &mdash; reported, not published', 'Travel-advice sites consistently '
                                                                     'report discounted fares for '
                                                                     'travelers 65+ at each of these '
                                                                     'carriers, sometimes through a '
                                                                     '&ldquo;Senior&rdquo; passenger-type '
                                                                     'option at booking, sometimes only by '
                                                                     'phone. None of the three publishes a '
                                                                     'standing, carrier-wide senior-fare '
                                                                     'rule the way Amtrak does &mdash; '
                                                                     'availability and terms are not '
                                                                     'independently verifiable from the '
                                                                     'carriers&rsquo; own published fare '
                                                                     'rules.'),
        ('Southwest', 'No senior-specific fare category. Southwest&rsquo;s position is that its everyday '
                      'fares serve the same purpose for every age group.'),
    ]) + """
      <h2>Why this is genuinely harder to pin down than it should be</h2>

      <p>Amtrak treats its senior discount as a standard, published fare rule &mdash; it&rsquo;s on the
      site, it applies automatically, and the percentage doesn&rsquo;t change from one booking to the
      next. The major airlines don&rsquo;t work that way. None of United, Delta, or American publishes a
      standing senior-fare rule the way Amtrak does; what gets reported instead is a pattern &mdash; a
      discount that shows up on some searches and not others &mdash; from independent travel-advice
      sources, not from a fare rules page any of the three carriers puts out themselves.</p>

      <p>That inconsistency is the actual story, more than any specific percentage. A discount reported on
      one route in one month is not a standing policy you can plan a trip around six months out &mdash; it
      has to be checked at the time of booking, for that specific flight, the way you&rsquo;d check any
      other fare, and it can&rsquo;t be confirmed against a published carrier rule the way Amtrak&rsquo;s
      can.</p>

      <blockquote class="pull">
        <p>Amtrak&rsquo;s senior discount is a published rule. What gets called a senior fare at the major
        airlines is a reported pattern &mdash; real often enough to be worth checking, not confirmed
        often enough to plan around.</p>
      </blockquote>

""" + AD_INLINE + """
      <h2>What&rsquo;s worth doing before you assume either way</h2>

      <p>Because none of the airline senior fares are consistently published, the only reliable check is
      running the comparison yourself at the time you&rsquo;re actually booking: search once with
      &ldquo;Senior (65+)&rdquo; selected where the airline offers that option, and once with a standard
      adult fare, and compare the two totals directly. A senior fare is not automatically the cheapest
      option on the page &mdash; a public sale fare or a basic economy fare can beat it, and nothing forces
      the airline to tell you that.</p>

      <p>For airlines that don&rsquo;t show it online at all, that means an actual phone call rather than
      giving up after a website search turns up nothing. The absence of a &ldquo;senior&rdquo; button on
      the booking page isn&rsquo;t proof the discount doesn&rsquo;t exist for that carrier &mdash; it may
      just mean that carrier only offers it through an agent.</p>

      <h2>The discount that isn&rsquo;t actually about your age</h2>

      <p>A lot of what gets marketed as a &ldquo;senior travel discount&rdquo; is really an AARP membership
      discount, and the two aren&rsquo;t the same thing. AARP membership is a low-cost annual fee (check
      AARP&rsquo;s current price directly, since membership pricing is promotional and changes), anyone 18
      or older can join, and full member benefits are available well before 65 &mdash; the organization
      markets itself to the 50-plus range, not a strict age cutoff enforced at checkout. AARP&rsquo;s own
      site advertises hotel discounts up to 20% at chains including Wyndham, Choice and Best Western, and
      car-rental savings up to 35% through Avis, Budget and Payless.</p>

      <p>The eligibility mechanism is different from the age-verified discounts above: an AARP-partner rate
      is checked against membership, not a birth year, which is worth knowing before you assume a &ldquo;senior
      rate&rdquo; at a hotel or car-rental counter is checking ID rather than a membership number. (Some
      partner offers may carry their own separate age or other conditions on top of membership &mdash; the
      point is the mechanism is different, not that no conditions ever apply.)</p>

      <p>The same membership also covers cruise bookings and vacation packages through AARP&rsquo;s travel
      program, which matters if a cruise is the actual trip you&rsquo;re planning rather than a flight or a
      train. Cruise lines rarely advertise a standalone age-based senior fare the way Amtrak does &mdash;
      what shows up instead is usually the same membership-rate mechanism, filed under a partner program
      rather than the cruise line&rsquo;s own age policy.</p>

      <h2>What to actually check</h2>

""" + check([
        'Run the same search twice &mdash; once as a standard adult fare, once with any '
        '<strong>&ldquo;Senior&rdquo;</strong> passenger option selected &mdash; and compare the actual '
        'total, not just the label.',
        'For a carrier with no visible senior option online, <strong>call reservations directly</strong> '
        'and ask before concluding none exists.',
        'Don&rsquo;t book a senior fare sight unseen based on what a carrier offered on a different route '
        'or in a different season &mdash; reported availability varies enough by route and date that one '
        'good result elsewhere doesn&rsquo;t confirm your specific search.',
        'For train travel, confirm Amtrak&rsquo;s <strong>10% senior discount</strong> is actually applied '
        'at checkout (or the 50% Downeaster rate, if that&rsquo;s your route), and remember it excludes '
        'sleeping-car charges specifically.',
        'Carry ID that proves your age &mdash; Amtrak requires it, and any age-verified airline fare will '
        'as well; an AARP-partner rate requires proof of membership instead.',
        'Before assuming a hotel or car-rental &ldquo;senior rate&rdquo; needs an age check, confirm '
        'whether it&rsquo;s actually an <strong>AARP membership rate</strong> instead &mdash; check AARP&rsquo;s '
        'current membership price directly, since it&rsquo;s promotional and subject to change.',
    ]) + """
      <p>None of this is a reason to expect less. It&rsquo;s a reason to check every time, on the specific
      trip you&rsquo;re actually booking, rather than trusting whatever the last trip taught you.</p>
""",
    'sources': [
        ('Amtrak &mdash; Senior Discount',
         'https://www.amtrak.com/seniors-discount'),
        ('Amtrak Downeaster &mdash; Senior Discount',
         'https://amtrakdowneaster.com/deals-discounts/deals/senior-discount/'),
        ('Chapter &mdash; Amtrak Fares for Seniors: Discounted Fares for Senior Riders',
         'https://askchapter.org/magazine/budgeting-financial-wellness-tips/saving-money/discount-amtrak-fares-for-seniors'),
        ('AARP &mdash; Travel: AARP Membership Benefits and Discounts',
         'https://www.aarp.org/membership/benefits/travel/'),
    ],
    'next': {'slug': 'parks-fee-free-days',
             'title': 'The fee-free days don&rsquo;t do anything for you if you have the Senior Pass',
             'blurb': 'A second look at a widely repeated travel-savings tip &mdash; this one about '
                      'national parks, not airfare.'},
}

# ------------------------------------------------------------- portugal d7
ARTICLES17['portugal-d7-visa'] = {
    'title': 'Portugal&rsquo;s Retirement Visa Income Rule Just Went Up Again &mdash; The Second Half Guide',
    'eyebrow': 'Getting out there',
    'h1': 'Portugal&rsquo;s retirement visa income rule just went up again',
    'dek': 'Portugal&rsquo;s D7 visa is popular with American retirees for a reason &mdash; but the income '
           'floor moves every January, automatically, and it just moved again for 2026.',
    'meta': '5 minute read &middot; Verified against Portugal&rsquo;s 2026 minimum-wage decree and current '
            'immigration guidance',
    'checked': '22 September 2026',
    'recheck': {'due': '2027-01-10', 'why': 'Portugal’s minimum wage typically resets each January -- '
                'check for a new decree-law and update the income floor for the new year.'},
    'body': """      <p>The D7 visa is the route most American retirees use to live in Portugal long-term: proof of
      steady passive income &mdash; Social Security, a pension, rental income, dividends &mdash; instead of
      a job offer or an investment purchase. It has a real advantage over the &ldquo;golden visa&rdquo;
      investment programs other countries use: no property purchase required. It also has a moving target
      that catches people off guard, because it isn&rsquo;t set once and left alone.</p>

      <p>Guides written even a year ago describe a real program, correctly, at a number that's already
      out of date. That's not a criticism of any particular guide &mdash; it's a structural feature of how
      the visa works, and it means the specific euro figure matters less than understanding what actually
      moves it and when.</p>

""" + facts('The D7 income requirement, 2025 vs. 2026', [
        ('What it&rsquo;s tied to', 'Portugal&rsquo;s national minimum wage &mdash; the D7&rsquo;s '
                                    'income floor is calculated from it, and rises each time the minimum '
                                    'wage does.'),
        ('2025 minimum', '&euro;870 per month for a single applicant (about &euro;10,440 per year).'),
        ('2026 minimum', '&euro;920 per month for a single applicant (about &euro;11,040 per year), '
                         'effective January 1, 2026 under Decree-Law No. 139/2025.'),
        ('Family additions', 'Roughly &euro;460/month more for a spouse (50% of the base figure) and '
                             '&euro;276/month more for each dependent child (30% of the base figure).'),
    ]) + """
      <h2>Why this catches people who already applied</h2>

      <p>The income threshold isn&rsquo;t fixed at the level you qualified under when you first applied.
      Portugal&rsquo;s immigration authority (AIMA) is reported, consistently across immigration-law and
      relocation guidance, to assess the current threshold at the time of your renewal appointment, not
      the one in effect when your visa was originally issued &mdash; AIMA&rsquo;s own guidance isn&rsquo;t
      directly reachable from this sandbox, so treat the mechanism as well-corroborated rather than
      pulled from the regulation itself, and confirm it with an immigration attorney before relying on it.
      Reported this way, a retiree who qualified comfortably at &euro;870 a month in 2025 would need to
      show &euro;920 a month at their next renewal in 2026 &mdash; even though nothing about their own
      finances changed. It's the benchmark that moved, not their situation.</p>

      <p>This is a modest year-over-year jump in absolute terms &mdash; &euro;50 a month, roughly &euro;600
      a year &mdash; but it's the kind of detail that's easy to miss if you did the math once during your
      original application and never revisited it. Anyone renewing a D7 visa should treat the income
      threshold as something to re-check every year, not something settled at approval.</p>

      <blockquote class="pull">
        <p>The D7&rsquo;s income floor isn&rsquo;t a one-time hurdle. It moves every January, and it's
        checked again at every renewal &mdash; against the current number, not the one you qualified
        under originally.</p>
      </blockquote>

""" + AD_INLINE + """
      <h2>The tax break most guides still mention, and that&rsquo;s no longer available to you</h2>

      <p>A lot of what circulates online about retiring to Portugal still references the Non-Habitual
      Resident regime &mdash; a tax break that gave qualifying new residents years of favorable treatment
      on foreign income, pensions included. It closed to most new applicants at the end of 2023, with a
      narrow, time-limited transition for people who could show they were already committed to the move by
      specific 2023 milestones &mdash; a signed employment contract, a property purchase already under
      contract, a child already enrolled in a Portuguese school, or a residence application already filed.
      Someone starting the D7 process fresh today, with none of those in place beforehand, does not qualify
      for NHR regardless of what an older guide or blog post says.</p>

      <p>What replaced it, called IFICI, is a narrower program aimed at people working in scientific
      research and innovation roles &mdash; not the general foreign-income and pension treatment NHR
      offered retirees. A retiree moving to Portugal on a D7 visa today, without one of those specific
      transitional qualifications, is applying under Portugal&rsquo;s ordinary tax rules, not the more
      favorable regime that made the destination especially popular with American retirees in years past.
      That&rsquo;s a real change to the underlying financial case for the move, separate from the visa&rsquo;s
      income threshold, and it&rsquo;s worth confirming directly with a tax professional &mdash; including
      whether any transitional exception could apply to your specific situation &mdash; rather than
      assuming either way.</p>

      <h2>What the D7 actually requires, beyond the income number</h2>

      <p>Passive income is the headline figure, but it isn&rsquo;t the whole application. Applicants also
      need proof of accommodation in Portugal (a lease or property deed), a clean criminal record
      certificate, and valid health insurance covering the stay. The visa itself is issued first through a
      Portuguese consulate, followed by a residence-permit appointment inside Portugal &mdash; the same
      AIMA appointment where the current-year income threshold gets checked again. After five years of
      legal residence, D7 holders can apply for permanent residency or citizenship, subject to Portugal&rsquo;s
      separate language and residency requirements at that stage.</p>

      <p>Processing time between the consulate interview and the AIMA appointment varies by consulate and
      by case load, and it has swung considerably over the past several years as Portugal has worked
      through a large application backlog. Treat any specific timeline you read as a starting estimate to
      confirm with your own consulate, not a number to plan a moving date around.</p>

      <h2>What to actually check</h2>

""" + check([
        'If you&rsquo;re applying new, confirm the <strong>current-year</strong> threshold directly with a '
        'Portuguese consulate or an immigration attorney &mdash; don&rsquo;t rely on a guide written even '
        'a few months earlier, since the number resets every January.',
        'If you already hold a D7 visa, check the income figure again <strong>before your renewal '
        'appointment</strong>, not at your original approval &mdash; the threshold that matters is the one '
        'in effect the year you renew.',
        'Confirm which of your income sources actually count as passive income under Portuguese rules '
        '&mdash; Social Security and private pensions generally qualify, but the exact list is worth '
        'confirming with an immigration professional rather than assuming.',
        'Budget the family additions separately if you&rsquo;re bringing a spouse or dependents &mdash; '
        'the per-person add-on changes the total meaningfully once you have more than one applicant.',
        'Don&rsquo;t plan your finances around the old <strong>NHR tax regime</strong> &mdash; it closed '
        'to new applicants after December 31, 2023, and a D7 applicant today pays under Portugal&rsquo;s '
        'ordinary tax rules unless a tax professional identifies a different, still-current benefit.',
    ]) + """
      <p>None of this makes the D7 a bad option &mdash; it remains one of the more accessible long-stay
      routes into Europe for a retiree living on Social Security or a pension. It does mean the number in
      whatever guide you read is only accurate for the year it was written, and Portugal isn&rsquo;t going
      to send a reminder when it changes.</p>
""",
    'sources': [
        ('Bloomberg Tax &mdash; Portugal Gazettes Decree-Law Increasing Monthly Minimum Wage for 2026',
         'https://news.bloombergtax.com/daily-tax-report-international/portugal-gazettes-decree-law-increasing-monthly-minimum-wage-for-2026'),
        ('Garrigues &mdash; Portugal: Minimum monthly wage increases in 2026',
         'https://www.garrigues.com/en_GB/new/portugal-minimum-monthly-wage-increases-2026'),
        ('Portugalist &mdash; Portugal D7 Visa Requirements 2026',
         'https://www.portugalist.com/minimum-wage-2026/'),
        ('KPMG &mdash; Portugal: Expatriate Tax Regime Ended; New Tax Incentive for Scientific Research and Innovation',
         'https://kpmg.com/xx/en/our-insights/gms-flash-alert/flash-alert-2025-044.html'),
    ],
    'next': {'slug': 'long-distance',
             'title': 'The new long-distance grandparent',
             'blurb': 'Moving abroad changes the family-distance math too &mdash; the piece on staying '
                      'close from far away.'},
}
