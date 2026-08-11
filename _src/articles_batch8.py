#!/usr/bin/env python3
"""Eighth batch: the remaining non-travel backlog."""

from build_articles import facts, check, AD_INLINE, CHECKED

ARTICLES8 = {}

# ------------------------------------------------------- Medicare Savings
ARTICLES8['medicare-savings'] = {
    'title': 'The Medicare Help Millions Qualify For and Never Claim &mdash; The Second Half Guide',
    'eyebrow': 'Facts &amp; thresholds',
    'h1': 'The Medicare help millions qualify for and never claim',
    'dek': 'Four programs pay your Part B premium, your deductibles, or your drug costs. The income '
           'limits are higher than most people assume, and take-up is dismal.',
    'meta': '6 minute read &middot; 2026 limits verified',
    'checked': CHECKED,
    'body': """      <p>If your income is modest, there are programs that will pay your Medicare Part B premium —
      $202.90 a month in 2026, straight out of your Social Security payment — and in some cases your
      deductibles and copays too.</p>

      <p>They are chronically under-claimed. Millions of people who qualify have never applied, generally
      for one of three reasons: they've never heard of them, they assume the limits are far lower than
      they are, or they think of this as welfare and would rather not.</p>

      <p>So here are the actual numbers.</p>

""" + facts('Medicare Savings Programs, 2026 monthly income limits', [
        ('QMB', 'About $1,350 single / $1,824 couple. The most comprehensive: pays your Part B premium '
                '<em>and</em> your deductibles, coinsurance and copays.'),
        ('SLMB', 'About $1,616 single / $2,184 couple. Pays the Part B premium.'),
        ('QI', 'About $1,816 single / $2,455 couple. Pays some or all of the Part B premium. First come, '
               'first served each year.'),
        ('Resource limit', 'Around $9,950 for an individual. Your home and usually one car don’t count.'),
        ('Extra Help', 'Separate program for drug costs &mdash; roughly $23,475 a year single / '
                       '$31,725 couple.'),
        ('The automatic part', 'Qualify for any Medicare Savings Program and you are <strong>automatically '
                               'eligible for Extra Help</strong> too.'),
    ]) + """
      <h2>What it’s actually worth</h2>

      <p>Start with the Part B premium: $202.90 a month is <strong>about $2,435 a year</strong>, added
      straight back onto your Social Security payment. For someone on the average benefit of $2,071 a
      month, that's close to a 10% raise.</p>

      <p>QMB goes considerably further. It covers deductibles, coinsurance and copays, and QMB enrollees
      are protected from being billed by providers for Medicare-covered services at all.</p>

      <p>And Extra Help transforms drug costs. With it, generics run about <strong>$5.10</strong> and
      brand-name drugs about <strong>$12.65</strong> in 2026, with no late-enrollment penalty for Part D.</p>

      <blockquote class="pull">
        <p>Qualifying for the smallest of these programs is worth roughly $2,400 a year. Qualifying for
        the largest can be worth several times that.</p>
      </blockquote>

""" + AD_INLINE + """
      <h2>Four things people get wrong</h2>

      <ul>
        <li><strong>&ldquo;My income is too high.&rdquo;</strong> Maybe. But states set their own limits
        and <strong>many are more generous than the federal floor</strong> — some have raised limits
        substantially, and a few have removed the asset test entirely. The only way to know is to apply
        in your state.</li>
        <li><strong>&ldquo;I own my house, so I won't qualify.&rdquo;</strong> Your primary home doesn't
        count toward the resource limit. Neither, usually, does one car.</li>
        <li><strong>&ldquo;It's welfare.&rdquo;</strong> These are Medicare programs funded partly by
        the payroll taxes you paid for forty years. You are not taking someone else's place; QI is the
        only one with a cap, and it routinely goes unfilled.</li>
        <li><strong>&ldquo;It'll affect my estate.&rdquo;</strong> Medicare Savings Programs are not
        long-term-care Medicaid, and estate recovery rules generally do not apply to MSP benefits in the
        way people fear. Worth asking about specifically rather than assuming the worst.</li>
      </ul>

      <h2>How to apply</h2>

""" + check([
        'Apply for <strong>Extra Help</strong> directly with Social Security at <em>ssa.gov</em>, by '
        'phone on 1-800-772-1213, or on paper. It is a short form.',
        'Apply for <strong>Medicare Savings Programs</strong> through your <strong>state Medicaid '
        'office</strong> &mdash; not Medicare. This split confuses people and is the commonest reason an '
        'application never gets made.',
        'Do it even if you think you are slightly over. <strong>State limits vary</strong> and some '
        'income is disregarded in the calculation.',
        'Ask your <strong>SHIP counselor</strong> to help &mdash; free, and they do these applications '
        'constantly. <em>shiphelp.org</em>.',
        'Try <strong>BenefitsCheckUp</strong> at <em>benefitscheckup.org</em>, which screens for these '
        'alongside food, energy and property tax help in one pass.',
        'If your income drops &mdash; a spouse dies, you stop working &mdash; <strong>apply again</strong>. '
        'Eligibility is not a one-time verdict.',
    ]) + """
      <p>The reason to take this seriously even if you're comfortable: circumstances change. The most
      common path into these programs is a household going from two Social Security payments to one,
      which is the subject of <a href="/widows-penalty">a separate piece on this site</a> and is far more
      financially violent than people expect.</p>

      <p>Twenty minutes and a form is a strange price for $2,400 a year, and it's the reason this is
      probably the most materially useful article we've published.</p>
""",
    'sources': [
        ('Medicare &mdash; Medicare Savings Programs',
         'https://www.medicare.gov/basics/costs/help/medicare-savings-programs'),
        ('SSA &mdash; Extra Help with Medicare prescription drug costs',
         'https://www.ssa.gov/medicare/part-d-extra-help'),
        ('NCOA &mdash; BenefitsCheckUp', 'https://benefitscheckup.org/'),
        ('SHIP &mdash; Free local Medicare counselling', 'https://www.shiphelp.org/'),
    ],
    'next': {'slug': 'widows-penalty',
             'title': 'The widow’s penalty',
             'blurb': 'One benefit stops, and the tax brackets halve. The arithmetic surprises almost '
                      'everyone.'},
}

# ---------------------------------------------------------- widow's penalty
ARTICLES8['widows-penalty'] = {
    'title': 'The Widow’s Penalty &mdash; The Second Half Guide',
    'eyebrow': 'Facts &amp; thresholds',
    'h1': 'The widow’s penalty',
    'dek': 'When one spouse dies, household income falls sharply and the tax brackets narrow at the same '
           'time. It is one of the harshest bits of arithmetic in retirement, and it is rarely explained '
           'in advance.',
    'meta': '6 minute read &middot; Verified against SSA and IRS rules',
    'checked': CHECKED,
    'body': """      <p>It has an ugly name and it deserves one, because the effect is genuinely punitive and it lands
      on people in the worst year of their lives.</p>

      <p>Two things happen at once when a spouse dies. Household income falls. And the tax system moves
      you from married-filing-jointly to single, where the brackets are roughly half as wide. Less money,
      taxed at higher rates.</p>

      <h2>The Social Security part</h2>

      <p>The rule that surprises people: a surviving spouse <strong>does not receive both benefits</strong>.
      They receive the higher of the two, and the smaller one stops.</p>

      <p>So a couple receiving $2,400 and $1,600 a month — $4,000 between them — becomes a survivor
      receiving $2,400. <strong>Household Social Security income falls by 40%</strong>, and the survivor's
      expenses do not fall by anything like that. Property taxes, insurance, utilities and the mortgage
      are unchanged. Medicare premiums are per person, so that halves, but very little else does.</p>

""" + facts('What changes, and when', [
        ('Social Security', 'The survivor keeps the higher benefit. The smaller one stops. Generally '
                            'available from age 60, or 50 if disabled.'),
        ('Filing status', 'You can usually file jointly for the <em>year</em> of death. After that, '
                          'single &mdash; unless you have a dependent child, which allows qualifying '
                          'surviving spouse status for two more years.'),
        ('Standard deduction', 'Roughly halves when you move to single.'),
        ('Tax brackets', 'Single brackets are about half as wide as joint ones, so the same income is '
                         'taxed at higher rates.'),
        ('Medicare IRMAA', 'The income thresholds for high-income Medicare surcharges are lower for '
                           'single filers. A survivor can be pushed into a surcharge on <em>less</em> '
                           'income than the couple had.'),
        ('Pensions', 'Depends entirely on the survivor election made at retirement. Some continue in '
                     'full, some at 50% or 75%, and some stop completely.'),
    ]) + """
      <blockquote class="pull">
        <p>Income falls by a third or more. The tax brackets narrow by half. Those two things happening
        in the same year is the penalty.</p>
      </blockquote>

""" + AD_INLINE + """
      <h2>The pension election nobody remembers making</h2>

      <p>If there's a pension, the single most consequential decision was made years earlier, usually at
      a desk, on a form, in a hurry.</p>

      <p>Taking the higher single-life payment rather than a reduced joint-and-survivor option means the
      pension <strong>stops entirely at death</strong>. Couples take that option all the time, sometimes
      for good reasons and sometimes because the larger number looked better and the form was
      confusing.</p>

      <p>If you're not yet retired, this is worth deliberate attention. If you're already receiving a
      pension, find out now which election was made — it determines whether the survivor faces a 40% cut
      or something far worse.</p>

      <h2>Things worth doing in advance</h2>

      <p>Almost everything that helps has to happen before, which is precisely why this belongs on a site
      for people in their late 50s and 60s rather than in a bereavement pamphlet.</p>

""" + check([
        'Find out <strong>which pension survivor election</strong> is in place. This is the biggest single '
        'variable and the easiest to have forgotten.',
        'Understand how <strong>delaying the higher earner’s Social Security</strong> works here: because '
        'the survivor keeps the larger benefit, delaying the bigger one raises the payment for whichever '
        'of you lives longer. It functions as survivor insurance.',
        'Look at whether <strong>Roth conversions</strong> make sense in your joint-filing years. Filling '
        'the wider married brackets now can mean less taxable income later at single rates &mdash; a '
        'genuine planning conversation to have with an accountant, not a website.',
        'Check <strong>life insurance</strong> against the actual shortfall rather than a round number.',
        'Make sure <strong>both spouses can operate the finances.</strong> Where the money is, which '
        'accounts exist, how the bills get paid. This is the practical failure that compounds everything '
        'else.',
        'Know that a survivor may newly qualify for <a href="/medicare-savings">Medicare Savings '
        'Programs</a> on the reduced income. Eligibility is not judged once.',
    ]) + """
      <h2>One deadline worth knowing</h2>

      <p>If the house is going to be sold, timing matters more than almost anyone realizes. A surviving
      spouse can use the <strong>full $500,000 capital gains exclusion</strong> on a home sale — but
      generally only if the sale happens <strong>within two years of the death</strong>. After that it
      drops to $250,000.</p>

      <p>On a long-held house in an appreciated market, that two-year window can be worth tens of
      thousands of dollars. It is a genuinely cruel deadline to attach to a grieving person, and almost
      nobody is told about it in time.</p>

      <p>None of this is cheerful. But every item on this page is easier to handle at 62 with both people
      in the room than at 78 with one.</p>
""",
    'sources': [
        ('SSA &mdash; Survivor benefits', 'https://www.ssa.gov/benefits/survivors/'),
        ('IRS &mdash; Filing status', 'https://www.irs.gov/publications/p501'),
        ('IRS &mdash; Topic 701: Sale of your home', 'https://www.irs.gov/taxtopics/tc701'),
        ('Medicare &mdash; Part B costs and IRMAA',
         'https://www.medicare.gov/basics/costs/medicare-costs'),
    ],
    'next': {'slug': 'medicare-savings',
             'title': 'The Medicare help millions qualify for and never claim',
             'blurb': 'Programs that pay your Part B premium &mdash; and a survivor may newly qualify.'},
}

# ------------------------------------------------------------------- falls
ARTICLES8['falls'] = {
    'title': 'Falls: The Numbers, and What Actually Reduces Them &mdash; The Second Half Guide',
    'eyebrow': 'Home &amp; everyday life',
    'h1': 'Falls: the numbers, and what actually reduces them',
    'dek': 'More than one in four older adults falls each year, and fall deaths have risen 51% in a '
           'decade. The good news is that the single most effective intervention is free.',
    'meta': '6 minute read &middot; CDC and USPSTF figures',
    'checked': CHECKED,
    'body': """      <p>Falls are the thing that most often turns an independent life into a dependent one — not
      because a fall is usually fatal, but because a broken hip at 78 begins a chain of events that can
      end somewhere nobody chose.</p>

      <p>They're also treated as bad luck, which is the part worth arguing with. A large share of fall
      risk is measurable and modifiable, and the most effective single intervention costs nothing.</p>

""" + facts('What the data show', [
        ('More than 1 in 4', 'Older adults who report a fall each year.'),
        ('~3.85 million', 'Emergency department visits by older adults for falls in 2024.'),
        ('43,020', 'Older adults who died from preventable falls in 2024.'),
        ('Up 51%', 'The rise in fall-related deaths among older adults over the past decade. ED visits '
                   'are up 38%.'),
        ('About 33%', 'The reduction in fall risk from challenging lower-body strength and balance '
                      'training three times a week.'),
        ('31&ndash;58%', 'Reductions associated with Tai Chi programs in trial data. Structured '
                         'programs like Otago show 23&ndash;40%.'),
    ]) + """
      <h2>The intervention that works</h2>

      <p>It isn't grab bars. Grab bars help, and you should have them. But the evidence is clearest and
      strongest on one thing: <strong>lower-body strength and balance training, done regularly, at a
      difficulty that actually challenges your balance.</strong></p>

      <p>Roughly a third fewer falls, from three sessions a week. No drug in this space comes close, and
      the effect compounds — stronger legs also mean an easier time on stairs, longer walks, and a better
      chance of getting up unaided if you do go down.</p>

      <p>The word doing the work is <em>challenging</em>. Gentle seated movement is pleasant and does
      very little for balance. The programs with good trial evidence — Tai Chi, Otago — deliberately
      put you near the edge of your balance, safely, so the system adapts. Standing on one leg while
      holding a counter is closer to the target than a chair-based class.</p>

      <blockquote class="pull">
        <p>The single most effective thing you can do about falls costs nothing, takes about half an hour
        three times a week, and is almost never what people go looking for.</p>
      </blockquote>

""" + AD_INLINE + """
      <h2>The other risk factors, roughly in order</h2>

      <ul>
        <li><strong>Medication.</strong> Psychoactive medications in particular — sleep aids,
        anti-anxiety medication, some antidepressants — carry a well-documented fall risk, and so does
        taking many medications at once. A pharmacist-led medication review is a legitimate and
        under-used request.</li>
        <li><strong>Vision.</strong> Uncorrected vision, and specifically <em>bifocals or progressives on
        stairs</em>, which distort depth exactly where it matters. Some people keep a single-vision pair
        for walking.</li>
        <li><strong>Blood pressure drops on standing.</strong> Very common, very treatable, and
        frequently the actual cause of a fall recorded as a trip.</li>
        <li><strong>Feet and footwear.</strong> Pain, numbness, and shoes without a back. Slippers are a
        genuine hazard.</li>
        <li><strong>The house.</strong> Loose rugs, poor lighting, no stair rail, clutter on the route to
        the bathroom at night.</li>
        <li><strong>Fear of falling.</strong> Counter-intuitive but well documented: people who become
        afraid move less, weaken faster, and fall more.</li>
      </ul>

      <h2>Worth doing</h2>

""" + check([
        'Start <strong>strength and balance work three times a week</strong>. Look for Tai Chi or a '
        'recognized falls-prevention class &mdash; many senior centers and Area Agencies on Aging run '
        'them free.',
        'Ask for a <strong>medication review</strong> naming falls as the reason. Bring everything, '
        'including supplements and anything over the counter.',
        'Get your <strong>eyes checked</strong>, and consider single-vision glasses for walking and '
        'stairs if you wear progressives.',
        'Ask your doctor to check <strong>blood pressure sitting and standing</strong>. It takes two '
        'minutes and is regularly the answer.',
        'Do the <strong>cheap house fixes</strong>: lighting, remove loose rugs, rails on both sides of '
        'stairs, a clear lit path to the bathroom.',
        'If you have fallen &mdash; even without injury &mdash; <strong>tell your doctor</strong>. One '
        'fall is the strongest predictor of the next, and it is the most under-reported event in '
        'medicine because people are embarrassed.',
    ]) + """
      <p>The last one matters most. Falls go unmentioned because they feel like evidence of decline, so
      the single most useful warning sign gets hidden from the one person who could act on it.</p>

      <p>A fall isn't a verdict about age. It's a data point about strength, medication, vision and blood
      pressure — every one of which can be changed.</p>
""",
    'sources': [
        ('CDC &mdash; Facts about falls',
         'https://www.cdc.gov/falls/data-research/facts-stats/index.html'),
        ('USPSTF &mdash; Falls prevention in community-dwelling older adults',
         'https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/falls-prevention-community-dwelling-older-adults-interventions'),
        ('National Council on Aging &mdash; Falls prevention',
         'https://www.ncoa.org/article/get-the-facts-on-falls-prevention/'),
        ('Eldercare Locator &mdash; Find local programs', 'https://eldercare.acl.gov/'),
    ],
    'next': {'slug': 'aging-in-place',
             'title': 'Aging in place: staying home is a goal, not a plan',
             'blurb': 'The house changes that matter, and the one that usually decides it.'},
}

# ------------------------------------------------------- wellness visit
ARTICLES8['wellness-visit'] = {
    'title': 'The Free Medicare Visit That Isn&rsquo;t a Physical &mdash; The Second Half Guide',
    'eyebrow': 'Facts &amp; thresholds',
    'h1': 'The free Medicare visit that isn&rsquo;t a physical',
    'dek': 'You get one every year at no cost. It is not a physical, which is the source of most of the '
           'confusion &mdash; and of most of the surprise bills.',
    'meta': '5 minute read &middot; Verified against Medicare coverage rules',
    'checked': CHECKED,
    'body': """      <p>Medicare covers an <strong>Annual Wellness Visit</strong> every year at no cost to you: no
      copay, no deductible, no coinsurance.</p>

      <p>About 60% of Medicare beneficiaries living in the community had one in 2022, by CMS&rsquo;s own
      beneficiary survey — so this is not an unknown benefit. The problem is what people think they are
      getting. A large share arrive expecting a physical, and some leave with an unexpected bill, because
      of a distinction that is genuinely confusing and rarely explained at the front desk.</p>

      <h2>Three different appointments with similar names</h2>

""" + facts('What each one is', [
        ('Welcome to Medicare visit', 'A one-off, available in your first 12 months on Part B. Free.'),
        ('Annual Wellness Visit', 'Once every 12 months thereafter. Free. A prevention-planning '
                                  'appointment, not an examination.'),
        ('Annual physical', '<strong>Not covered by Medicare at all.</strong> A hands-on head-to-toe '
                            'exam is a separate service you pay for.'),
        ('The overlap problem', 'If your doctor treats a symptom or manages a condition during the '
                                'wellness visit, that portion is billed as a regular visit &mdash; with '
                                'your usual copay and deductible.'),
    ]) + """
      <h2>What actually happens in it</h2>

      <p>The wellness visit is a review and a plan rather than an examination. Expect:</p>

      <ul>
        <li>Height, weight, blood pressure and other routine measurements</li>
        <li>A review of your <strong>medical and family history</strong></li>
        <li>A full list of your <strong>medications and supplements</strong> and who prescribes them</li>
        <li>A <strong>cognitive assessment</strong> &mdash; brief, and one of the more valuable parts</li>
        <li>Screening for <strong>depression</strong> and for <strong>fall risk</strong></li>
        <li>A written, personalised <strong>screening schedule</strong> for the next 5&ndash;10 years</li>
        <li>An opportunity to discuss <strong>advance care planning</strong>, which is covered here</li>
      </ul>

      <blockquote class="pull">
        <p>It's the appointment where somebody finally looks at your whole picture rather than the reason
        you came in — which is exactly what stops being routine once you have several doctors.</p>
      </blockquote>

""" + AD_INLINE + """
      <h2>Why it's worth having even though it isn't a physical</h2>

      <p>The instinctive reaction is that a visit with no examination isn't worth the trip. That
      undersells what it's for.</p>

      <p>By this stage of life a lot of people have a cardiologist, an endocrinologist, an orthopaedist
      and a primary care doctor, each managing their own piece. Nobody is looking at the whole list. The
      wellness visit is structurally designed to be that appointment — every medication in one place,
      every screening reviewed against your actual history, cognition and mood and fall risk all checked
      because the format requires it rather than because you raised them.</p>

      <p>The medication review alone justifies it. So does the fall-risk screening, given <a href="/falls">what
      the fall numbers look like</a>.</p>

      <h2>How to avoid the surprise bill</h2>

""" + check([
        'Book it as an <strong>&ldquo;Annual Wellness Visit&rdquo;</strong> by name. Not a physical, not '
        'a check-up &mdash; the words matter to the billing.',
        'Ask the office directly: <strong>&ldquo;will this be billed as anything other than the wellness '
        'visit?&rdquo;</strong> Ask before, not after.',
        'If you want to <strong>discuss a problem</strong>, say so and expect that part to be billed '
        'normally. That is legitimate &mdash; just not a surprise if you knew.',
        'Consider <strong>booking a separate appointment</strong> for ongoing issues so the wellness '
        'visit stays clean.',
        'Bring <strong>every medication and supplement</strong>, in the bottles. This is the part with '
        'the most value and it depends entirely on what you bring.',
        'Bring your <strong>family history</strong> and a list of your other doctors.',
    ]) + """
      <p>One more thing worth knowing: the visit resets every 12 months, not every calendar year. If you
      had it last March, you're eligible again this March — and booking it earlier gets rejected, which
      is another common source of an unexpected bill.</p>

      <p>Free, annual, and it's the only appointment in the system designed to look at all of you at
      once. It's a strange thing to leave unused.</p>
""",
    'sources': [
        ('Medicare &mdash; Yearly wellness visits',
         'https://www.medicare.gov/coverage/yearly-wellness-visits'),
        ('Medicare &mdash; Welcome to Medicare preventive visit',
         'https://www.medicare.gov/coverage/welcome-to-medicare-preventive-visit'),
        ('Medicare &mdash; Preventive and screening services',
         'https://www.medicare.gov/coverage/preventive-screening-services'),
    ],
    'next': {'slug': 'falls',
             'title': 'Falls: the numbers, and what actually reduces them',
             'blurb': 'The fall-risk screening in the wellness visit exists for a reason.'},
}

# --------------------------------------------------------------- downsizing
ARTICLES8['downsizing-math'] = {
    'title': 'Downsizing: The Arithmetic People Skip &mdash; The Second Half Guide',
    'eyebrow': 'Home &amp; everyday life',
    'h1': 'Downsizing: the arithmetic people skip',
    'dek': 'Selling a big house and buying a small one sounds like it frees up money. Sometimes it does. '
           'The costs that decide it are the ones nobody puts in the spreadsheet.',
    'meta': '6 minute read &middot; Tax rules verified against IRS guidance',
    'checked': CHECKED,
    'body': """      <p>The pitch is straightforward: sell the four-bedroom house, buy something smaller, pocket the
      difference, spend less on upkeep.</p>

      <p>It's often right. But the gap between the two sale prices is not the money you end up with, and
      the difference between those two numbers is where downsizing decisions quietly go wrong.</p>

      <h2>What comes out of the sale</h2>

""" + facts('The costs that reduce the difference', [
        ('Selling costs', 'Agent commission, transfer taxes, attorney fees, and whatever the inspection '
                          'turns up. Commonly around 6&ndash;10% of the sale price all in.'),
        ('Preparing to sell', 'Paint, repairs, staging, the roof you have been deferring.'),
        ('Moving', 'More than expected after decades in one house, and often a storage unit for a while.'),
        ('Buying costs', 'Closing costs, inspections, and immediate work on the new place.'),
        ('The new running costs', 'A smaller house is not automatically cheaper. A newer condo can carry '
                                  'high monthly fees; a smaller house in a nicer area can carry higher '
                                  'property taxes.'),
        ('Furnishing', 'Very little of a large house fits a small one, and people underestimate this '
                       'consistently.'),
    ]) + """
      <p>None of these are hidden — they're just usually left out of the mental version, which runs
      &ldquo;sell for $600,000, buy for $400,000, that's $200,000.&rdquo; After costs, that figure is
      frequently closer to $130,000, and a chunk of that goes on furnishing and settling in.</p>

      <p>That doesn't make downsizing wrong. It makes it a smaller financial event than people expect —
      which matters, because the financial case is often what's used to justify a decision that's really
      about something else.</p>

      <h2>The tax rule to know before you list</h2>

      <p>You can generally exclude <strong>$250,000 of gain</strong> on the sale of your main home, or
      <strong>$500,000 if married filing jointly</strong>, provided you owned and lived in it for two of
      the previous five years.</p>

      <p>For a house bought in 1985, gains above those thresholds are entirely possible, and the excess is
      taxable. Keep records of capital improvements across the years you owned it — they raise your cost
      basis and reduce the gain, and the receipts you can't find are the ones that cost you.</p>

      <blockquote class="pull">
        <p>A surviving spouse keeps the full $500,000 exclusion only if the sale happens within two years
        of the death. After that it halves.</p>
      </blockquote>

      <p>That deadline is worth flagging on its own, because it collides with grief. Selling the house is
      exactly the decision people are counselled not to rush — and there is a genuine two-year tax clock
      running while they take that advice. Not a reason to hurry, but a reason to know the date.</p>

""" + AD_INLINE + """
      <h2>The non-financial reasons, which are usually the real ones</h2>

      <p>Most people who downsize successfully didn't do it for the money. They did it for one of these,
      and the money was a bonus:</p>

      <ul>
        <li><strong>Single-floor living</strong>, or a house that will still work in fifteen years.</li>
        <li><strong>Less to maintain</strong> — the yard, the gutters, the second bathroom nobody uses.</li>
        <li><strong>Location.</strong> Closer to family, or somewhere you can still get about if you stop
        driving. As <a href="/aging-in-place">we've argued elsewhere</a>, this decides more than
        architecture does.</li>
        <li><strong>Less house than life.</strong> Heating and cleaning rooms that are shut most of the
        year.</li>
      </ul>

      <p>The counter-case deserves equal weight: moving costs money and energy, a paid-off house is
      unusually cheap to live in, and leaving a neighborhood where you know people has a real cost that
      never appears in a spreadsheet.</p>

      <h2>Before you decide</h2>

""" + check([
        'Work out the <strong>real net proceeds</strong> &mdash; sale price minus 6&ndash;10% of costs, '
        'minus preparation, minus moving, minus furnishing.',
        'Compare <strong>total monthly running costs</strong>, not house sizes: taxes, insurance, fees, '
        'utilities, maintenance.',
        'Dig out records of <strong>capital improvements</strong> before you list. They reduce a taxable '
        'gain and they are impossible to reconstruct later.',
        'If you are a <strong>surviving spouse</strong>, find out where you are in the two-year window.',
        'Test the new location for the <strong>no-driving scenario</strong>. It is the question that '
        'ages best.',
        'Consider <strong>renting for a year</strong> in the area you think you want. It is the cheapest '
        'possible way to discover you were wrong.',
    ]) + """
      <p>Downsizing is usually a good decision made for slightly wrong reasons. The house is genuinely
      too big, the stairs are genuinely a future problem, and the money released is genuinely useful.</p>

      <p>It's just rarely the windfall the arithmetic seems to promise — and knowing that in advance is
      what stops a sound decision from feeling like a disappointment.</p>
""",
    'sources': [
        ('IRS &mdash; Topic 701: Sale of your home', 'https://www.irs.gov/taxtopics/tc701'),
        ('IRS &mdash; Publication 523: Selling your home',
         'https://www.irs.gov/publications/p523'),
        ('Consumer Financial Protection Bureau &mdash; Buying a house',
         'https://www.consumerfinance.gov/owning-a-home/'),
    ],
    'next': {'slug': 'aging-in-place',
             'title': 'Aging in place: staying home is a goal, not a plan',
             'blurb': 'The other side of the same decision, and the question that decides both.'},
}

# ------------------------------------------------------------------ driving
ARTICLES8['driving'] = {
    'title': 'The Driving Conversation &mdash; The Second Half Guide',
    'eyebrow': 'Home &amp; everyday life',
    'h1': 'The driving conversation',
    'dek': 'Age alone is a poor predictor of who should stop driving. Specific, checkable things are '
           'much better ones &mdash; and there is a great deal of road between driving as usual and '
           'giving up the keys.',
    'meta': '6 minute read &middot; Home &amp; everyday life',
    'checked': CHECKED,
    'body': """      <p>This is the conversation families dread most, and they usually get it wrong in the same way:
      they treat it as a single yes-or-no decision about a person's competence, held once, under
      pressure.</p>

      <p>It isn't that. Driving is a set of specific abilities — vision, reaction time, neck rotation,
      attention, judgment — and they change at different rates in different people. Some 80-year-olds
      are safer drivers than some 60-year-olds. Age by itself tells you remarkably little.</p>

      <h2>Renewal rules vary enormously by state</h2>

      <p>There's no national standard. States set their own rules, and many apply extra requirements
      after a certain age — shorter renewal cycles, in-person renewal instead of online, mandatory vision
      testing, and in a few cases a road test.</p>

      <p>The ages and requirements differ so widely that any table here would mislead. Look up
      <strong>your own state's DMV rules</strong> — it takes two minutes, and it tells you what's coming
      and when.</p>

""" + facts('What actually predicts risk', [
        ('Vision', 'Acuity, peripheral vision, night vision, glare recovery. Cataracts affect driving '
                   'long before they affect reading.'),
        ('Neck and shoulder mobility', 'Checking blind spots requires rotation. Arthritis quietly removes '
                                       'this and people compensate without noticing.'),
        ('Reaction time and attention', 'Particularly divided attention &mdash; a junction with several '
                                        'things happening at once.'),
        ('Medications', 'Sedatives, some painkillers, sleep aids, and combinations. The same list that '
                        'raises fall risk.'),
        ('Cognition', 'Getting lost on familiar routes is a more serious signal than any driving error.'),
        ('Foot and leg strength', 'Moving reliably between pedals.'),
    ]) + """
      <blockquote class="pull">
        <p>The question is never &ldquo;are you too old to drive?&rdquo; It's &ldquo;which specific
        thing has changed, and what does that rule out?&rdquo;</p>
      </blockquote>

""" + AD_INLINE + """
      <h2>The middle ground everyone forgets</h2>

      <p>Because the conversation gets framed as all-or-nothing, families skip the enormous space in
      between — where most people actually live for years.</p>

      <ul>
        <li><strong>No night driving.</strong> Night vision and glare recovery decline earliest, and this
        single restriction removes a large share of risk.</li>
        <li><strong>No motorways</strong>, or no unfamiliar motorway junctions.</li>
        <li><strong>Local only</strong> — a known radius, known routes.</li>
        <li><strong>Not in bad weather.</strong></li>
        <li><strong>Not at rush hour.</strong></li>
        <li><strong>A car that helps</strong> — backup camera, blind-spot warning, automatic braking.
        These are genuinely useful and can extend safe driving by years.</li>
      </ul>

      <p>Many people self-impose these gradually and sensibly. Noticing and endorsing that, rather than
      escalating to the keys, is usually the right family response.</p>

      <h2>Having the conversation</h2>

""" + check([
        'Start <strong>early and generally</strong>, long before it is urgent: &ldquo;how would we know '
        'when it was time?&rdquo; is a much easier question at 68 than at 84.',
        'Talk about <strong>specific incidents</strong>, not age. &ldquo;You got lost coming back from '
        'the shop&rdquo; is a fact. &ldquo;You’re too old&rdquo; is an insult that ends the conversation.',
        'Get a <strong>medical and vision check first</strong>. Cataracts, medication and hearing are '
        'fixable, and often the problem is one of those rather than driving itself.',
        'Consider a <strong>professional driving assessment</strong> &mdash; occupational therapists '
        'certified as driver rehabilitation specialists do these. An outside verdict removes the family '
        'from the judgment.',
        'Solve <strong>transport before removing driving.</strong> Nothing goes worse than taking the '
        'keys with no plan &mdash; that is how people become isolated, and isolation does its own damage.',
        'Ask your <strong>Area Agency on Aging</strong> about local transport programs. Many run '
        'volunteer driver schemes nobody knows about.',
    ]) + """
      <p>The last point is the one families most often get backward. Driving isn't only transport — it's
      autonomy, and the ability to leave the house without asking anyone. Take that away without
      replacing it and you've traded a driving risk for a loneliness one, which has its own well-documented
      health effects.</p>

      <p>Do the transport plan first. Then the conversation is about how to get places, not about what
      someone can no longer do.</p>
""",
    'sources': [
        ('NHTSA &mdash; Older drivers', 'https://www.nhtsa.gov/road-safety/older-drivers'),
        ('CDC &mdash; Older adult drivers',
         'https://www.cdc.gov/older-adult-drivers/about/index.html'),
        ('National Institute on Aging &mdash; Older drivers',
         'https://www.nia.nih.gov/health/older-drivers'),
        ('Eldercare Locator &mdash; Transport help', 'https://eldercare.acl.gov/'),
    ],
    'next': {'slug': 'aging-in-place',
             'title': 'Aging in place: staying home is a goal, not a plan',
             'blurb': 'Driving is usually what decides whether staying put actually works.'},
}
