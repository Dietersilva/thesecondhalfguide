#!/usr/bin/env python3
"""Eighth batch: the remaining non-travel backlog."""

from build_articles import facts, check, AD_INLINE, CHECKED

ARTICLES8 = {}

# ------------------------------------------------------- Medicare Savings
ARTICLES8['medicare-savings'] = {
    'title': 'The Medicare Help Millions Qualify For and Never Claim &mdash; The Second Half Guide',
    'eyebrow': 'Facts &amp; thresholds',
    'h1': 'The Medicare help millions qualify for and never claim',
    'dek': 'Four Medicare Savings Programs help with premiums and deductibles, and a separate program '
           'helps with drug costs. The income limits are higher than most people assume, and take-up '
           'is dismal.',
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
        ('QDWI', 'The fourth Savings Program, and the narrowest: it helps certain working people '
                 'with disabilities who lost premium-free Part A pay that Part A premium.'),
        ('The automatic part', 'Qualify for <strong>QMB, SLMB or QI</strong> and you are automatically '
                               'eligible for Extra Help too. QDWI works differently.'),
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
        <li><strong>&ldquo;It's welfare.&rdquo;</strong> These programs are run through your state's
        Medicaid office, which is what puts people off, but what they do is pay a Medicare bill you are
        already being charged. You are not taking someone else's place either; QI is the only one with a
        cap, and it routinely goes unfilled.</li>
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

      <p>If there's a pension, the decision that mattered most was made years earlier, usually at
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
           'decade. The good news is that the best-supported prevention costs nothing.',
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

      <p>It isn't grab bars. Grab bars help, and you should have them. But the strongest evidence sits with
      <strong>exercise done regularly at a difficulty that actually challenges your balance</strong>
      &mdash; programs combining balance, gait, functional and strength work. Which specific component
      does the most is not something the trials can cleanly separate.</p>

      <p>Roughly a third fewer falls, from three sessions a week. No drug in this space comes close, and
      the effect compounds — stronger legs also mean an easier time on stairs, longer walks, and a better
      chance of getting up unaided if you do go down.</p>

      <p>The word doing the work is <em>challenging</em>. Gentle seated movement is pleasant and does
      very little for balance. The programs with good trial evidence — Tai Chi, Otago — deliberately
      put you near the edge of your balance, safely, so the system adapts. Standing on one leg while
      holding a counter is closer to the target than a chair-based class.</p>

      <blockquote class="pull">
        <p>The best-supported thing you can do about falls costs nothing, takes about half an hour three
        times a week, and is almost never what people go looking for.</p>
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
      the clearest warning sign gets hidden from the one person who could act on it.</p>

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

      <p>The medication review and the fall-risk screening are the two parts most likely to turn up
      something, given <a href="/falls">what the fall numbers look like</a> and how quietly a
      medication list grows.</p>

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


# ------------------------------------------------------------------- IRMAA
ARTICLES8['irmaa'] = {
    'title': 'IRMAA 2026: Medicare Income Surcharge Explained &mdash; The Second Half Guide',
    'eyebrow': 'Facts &amp; thresholds',
    'h1': 'The Medicare surcharge based on what you earned two years ago',
    'dek': 'Cross one income line and your Medicare premium jumps by hundreds a month. The income '
           'that counts is from two years back &mdash; and retiring is grounds to appeal it.',
    'meta': '6 minute read &middot; 2026 figures verified against CMS and SSA',
    'checked': CHECKED,
    'body': """      <p>Most people meet IRMAA by letter. It arrives in the fall, it is written in the flat
      register of federal correspondence, and it says your Medicare premium next year will be
      substantially more than the number everybody else quotes.</p>

      <p>The name is <strong>Income-Related Monthly Adjustment Amount</strong>. It is a surcharge added
      to your Medicare Part B and Part D premiums when your income is above a threshold. Two things
      about how it works catch people out, and both are worth knowing before the letter arrives rather
      than after.</p>

""" + facts('What IRMAA costs in 2026', [
        ('The standard Part B premium', '$202.90 a month. This is what most people pay and what most '
                                        'articles quote.'),
        ('Where the surcharge starts', 'Modified adjusted gross income above <strong>$109,000 '
                                       'single</strong> or <strong>$218,000 married filing '
                                       'jointly</strong>.'),
        ('The first step up', '$284.10 a month for Part B &mdash; about $81 more, or roughly $975 a '
                              'year, and that is the smallest bracket.'),
        ('The top of the scale', '$689.90 a month, reached above $500,000 single or $750,000 joint. '
                                 'Five brackets in total.'),
        ('Part D as well', 'A separate surcharge of roughly $14.50 to $91.00 a month on top of whatever '
                           'your drug plan charges.'),
        ('Whose income counts', 'Your MAGI &mdash; adjusted gross income plus tax-exempt interest, '
                                'which is why municipal bonds do not help here.'),
    ]) + """
      <h2>The first thing: it looks backwards</h2>

      <p>Your 2026 premium is set by your <strong>2024</strong> tax return. Medicare uses the most recent
      return the IRS has passed along, which is generally two years old &mdash; occasionally three, if
      the newer one was not available when the determination was made.</p>

      <p>That lag is the whole problem. The year that decides your premium is often the last year you
      were working &mdash; or the year you sold a house, converted an IRA to a Roth, took a large
      distribution, or received a settlement. By the time the surcharge lands you may have retired, your
      income may have halved, and none of that is visible to the calculation.</p>

      <p>People assume the letter reflects what they are earning now. It reflects what they were earning
      the year before last.</p>

      <h2>The second thing: it is a cliff, not a slope</h2>

      <p>IRMAA does not phase in. Cross a threshold by a single dollar and you owe the entire bracket.
      At the first step that is about <strong>$975 across the year in Part B alone</strong>, and more at
      the higher ones. The Part D surcharge is separate and sits on top of it, so the Part B figure is
      not your total exposure. There is no proration and no partial credit.</p>

      <p>Which means the amounts that trigger it are often small and accidental: a year-end bonus, a
      required distribution slightly larger than expected, a capital gain from selling something you had
      held for decades. The mechanism does not care that the income was one-off.</p>

""" + AD_INLINE + """
      <h2>The part almost nobody is told</h2>

      <p><strong>You can ask for it to be recalculated, and retiring is one of the accepted reasons.</strong></p>

      <p>Social Security keeps a list of life-changing events that justify using your current income
      instead of the two-year-old figure. The form is <strong>SSA-44</strong>, it is two pages, and it is
      free. The accepted events are:</p>

""" + check([
        'Work stoppage &mdash; which includes <strong>retirement</strong>. This is the common one, and '
        'the one people do not realize counts.',
        'Work reduction &mdash; cutting back hours or moving to part-time.',
        'Marriage, divorce or annulment, or the <strong>death of a spouse</strong>.',
        'Loss of income-producing property, through disaster or other events outside your control.',
        'Loss of pension income.',
        'Employer settlement payment, or the employer closing or going bankrupt.',
    ]) + """
      <p>You file the form with an estimate of this year's income and documentation of the event &mdash;
      a letter from your employer, a death certificate, a divorce decree. Decisions generally take a
      month or two, and an approval can be backdated to when the event happened, which sometimes means a
      refund of premiums already paid.</p>

      <p>What does not qualify is simply disagreeing with the number. A one-time capital gain or a Roth
      conversion is <strong>not</strong> a life-changing event on this list, however much it feels like
      one &mdash; the gain was real income in the year it happened. There are separate routes if the
      underlying tax data is wrong rather than merely inconvenient: an amended return, corrected IRS
      information, or asking Social Security to use a more recent year's return than the one it used.</p>

      <blockquote class="pull">
        <p>The surcharge is calculated automatically. The appeal is not. Nobody files SSA-44 on your
        behalf, and nothing in the letter suggests you might have grounds to.</p>
      </blockquote>

      <h2>What to do with this</h2>

      <p><strong>If you are 63,</strong> that is the year that will set your first Medicare premium at
      65. Whatever lands in it &mdash; a Roth conversion, a property sale, deferred compensation, an
      unusually large distribution &mdash; is what the calculation will read two years later, however
      little it resembles your income by then.</p>

      <p><strong>If you have just retired and a surcharge letter arrives,</strong> file SSA-44. Your
      income has changed and the calculation has not caught up. This is precisely the situation the form
      exists for.</p>

      <p><strong>If the letter is simply correct,</strong> it still only applies for one year at a time.
      The determination is redone annually against a fresh return, so a single high year does not follow
      you permanently. It follows you for one year, two years later.</p>

      <p>The thresholds themselves move a little each year with inflation, which is worth checking rather
      than assuming: the 2026 figures above are not the 2025 ones. Medicare publishes the full bracket
      table each fall, and the letter you receive will name the bracket it has put you in.</p>

      <p>None of this is a reason to earn less. It is a reason to know that the line exists, roughly where
      it sits, and that the calculation behind it is looking at a year you have probably stopped thinking
      about.</p>
""",
    'sources': [
        ('Medicare &mdash; Part B costs',
         'https://www.medicare.gov/basics/costs/medicare-costs'),
        ('SSA &mdash; Request to lower an Income-Related Monthly Adjustment Amount',
         'https://www.ssa.gov/medicare/lower-irmaa'),
        ('SSA &mdash; Form SSA-44', 'https://www.ssa.gov/forms/ssa-44.pdf'),
        ('Medicare &mdash; Drug coverage (Part D) costs',
         'https://www.medicare.gov/drug-coverage-part-d/costs-for-medicare-drug-coverage'),
    ],
    'next': {'slug': 'medicare-savings',
             'title': 'The Medicare help millions qualify for and never claim',
             'blurb': 'The surcharge has a mirror image: if your income is modest, there are programs '
                      'that pay the premium instead.'},
}


# ------------------------------------------------- observation status
ARTICLES8['observation-status'] = {
    'title': 'Medicare Observation Status and the 3-Day Rule &mdash; The Second Half Guide',
    'eyebrow': 'Facts &amp; thresholds',
    'h1': 'Three nights in a hospital bed, and Medicare says you were never admitted',
    'dek': 'Observation is a billing status, not a place. It looks identical from the bed, and it '
           'can cost you the nursing-home stay afterward. Since 2025 there is finally a way to '
           'appeal it.',
    'meta': '6 minute read &middot; Verified against CMS rules and the Alexander v. Azar remedy',
    'checked': CHECKED,
    'body': """      <p>Someone falls, breaks a hip, and spends three nights in a hospital. They are in a hospital
      bed, on a hospital ward, wearing a hospital gown, with hospital staff coming and going. Then they
      are discharged to a skilled nursing facility for rehabilitation, and a bill arrives for the whole
      thing.</p>

      <p>The explanation is that they were never admitted. They were under <strong>observation</strong>,
      which Medicare treats as outpatient care &mdash; and outpatient days do not count toward the three
      inpatient days Medicare requires before it will pay for the nursing facility afterward.</p>

      <p>Nothing about the room tells you which one you are in.</p>

""" + facts('The two statuses, and what turns on them', [
        ('Inpatient', 'You were formally admitted. Part A covers the stay, after one deductible.'),
        ('Observation', 'Outpatient care that happens to involve a bed. Part B covers it &mdash; which '
                        'means 20% coinsurance, and Original Medicare puts no cap on that.'),
        ('The three-day rule', 'Medicare pays for a skilled nursing facility only after <strong>three '
                               'consecutive inpatient days</strong>. Observation days never count toward '
                               'them, however many there are.'),
        ('The drugs you already take', 'Your routine medications given during an outpatient stay are '
                                       'often not covered the way they would be as an inpatient, and '
                                       'get billed separately.'),
        ('What it can cost', 'The hospital coinsurance is the small part. The nursing facility that '
                             'Medicare then declines to pay for is the large one.'),
        ('Under Medicare Advantage', 'Plans can set their own rules here and some waive the three-day '
                                     'requirement entirely. Ask your plan rather than assuming either '
                                     'way.'),
    ]) + """
      <h2>You are told, but not asked</h2>

      <p>Since 2017 hospitals have had to hand you a form called the <strong>MOON</strong> &mdash; the
      Medicare Outpatient Observation Notice &mdash; if you have been receiving observation services as
      an outpatient for more than 24 hours. It has to arrive within 36 hours, in writing, with a
      plain-language explanation of why you do not meet the criteria for admission.</p>

      <p>It is worth knowing exactly what that form is and is not. It is a notification. For most of its
      existence it came with <strong>no right of appeal at all</strong> &mdash; it told you the decision
      and left you with it. People signed it while medicated, or exhausted, or without reading it,
      because it looked like the twentieth piece of paper in a stack of admission forms.</p>

""" + AD_INLINE + """
      <h2>What changed in 2025</h2>

      <p>A class action called <em>Alexander v. Azar</em>, upheld on appeal in 2022, forced Medicare to
      create an appeal that did not previously exist. CMS issued the rule in October 2024 and turned the
      process on in two stages:</p>

""" + check([
        '<strong>From 1 January 2025</strong> &mdash; a retrospective appeal, filed after the fact, for '
        'Part A coverage that was denied because your status changed.',
        '<strong>From 14 February 2025</strong> &mdash; an expedited appeal you can file '
        '<strong>while still in the hospital</strong>, before you are discharged, which is the version '
        'that can actually change what happens next.',
    ]) + """
      <p>There is an important limit on who this covers, and it is the thing most likely to be
      misunderstood. The appeal is for people in Original Medicare who were <strong>initially admitted
      as an inpatient and then reclassified</strong> to outpatient observation during the stay. It is
      not, on its own terms, a route for someone placed under observation from the moment they
      arrived.</p>

      <p>That distinction matters enormously in practice and it is not intuitive. It is worth asking
      directly, in the hospital, which of the two happened &mdash; because the answer determines whether
      this door is open to you.</p>

      <h2>What to do, in the room</h2>

      <p>The question worth asking out loud on the first day and again on the second:
      <strong>&ldquo;Am I an inpatient or under observation right now?&rdquo;</strong> Not <em>have I
      been admitted</em>, which people answer loosely, and not <em>am I staying overnight</em>, which is
      not the same question. Ask for the answer plainly, and ask again if the stay goes on, because the
      status can be changed partway through.</p>

      <p>If the answer is observation, ask the hospital's case manager or discharge planner whether the
      attending physician believes an inpatient admission is justified. Status is a clinical judgment
      applied against Medicare's criteria, not a fixed fact, and doctors do revisit it.</p>

      <p>If you were admitted and then moved to observation, say that you want to appeal, and say it
      before discharge. That is the expedited route, and it is the one with teeth.</p>

      <p>And if you are the family member rather than the patient: this is the thing to handle. Someone
      who has just broken a hip is in no condition to interrogate their own billing status, and the
      window in which the question matters is the few days when they are least able to ask it.</p>

      <blockquote class="pull">
        <p>Nobody in the room will raise this with you. The form arrives, it gets signed, and the
        consequence shows up weeks later in an envelope.</p>
      </blockquote>

      <p>One more piece of housekeeping: an updated MOON form takes effect in April 2026. Whichever
      version you are handed, read the part explaining why you do not meet inpatient criteria. That is
      the hospital's own reasoning, in writing, and it is what any appeal will turn on.</p>
""",
    'sources': [
        ('CMS &mdash; Hospital Appeals, Change of Inpatient Status (Alexander v. Azar)',
         'https://www.cms.gov/medicare/appeals-grievances/original-medicare-appeals/'
         'hospital-appeals-change-inpatient-status-alexander-v-azar'),
        ('CMS &mdash; Appeal Rights for Certain Changes in Patient Status, final rule',
         'https://www.federalregister.gov/documents/2024/10/15/2024-23195/'
         'medicare-program-appeal-rights-for-certain-changes-in-patient-status'),
        ('Medicare &mdash; Skilled nursing facility care',
         'https://www.medicare.gov/coverage/skilled-nursing-facility-care'),
        ('Center for Medicare Advocacy &mdash; Outpatient observation status',
         'https://medicareadvocacy.org/medicare-info/observation-status/'),
    ],
    'next': {'slug': 'long-term-care',
             'title': 'Long-term care: the numbers, before the sales pitch',
             'blurb': 'What the nursing facility actually costs, if Medicare declines to pay for it.'},
}


# ------------------------------------------------------- Medigap window
ARTICLES8['medigap-window'] = {
    'title': 'The Medigap 6-Month Open Enrollment Window &mdash; The Second Half Guide',
    'eyebrow': 'Facts &amp; thresholds',
    'h1': 'The six months that decide whether you can ever buy Medigap',
    'dek': 'One window, once, and it does not reopen. Inside it no insurer can ask about your health. '
           'Outside it, in most states, they can ask anything and say no.',
    'meta': '6 minute read &middot; Verified against Medicare and state Medigap rules',
    'checked': CHECKED,
    'body': """      <p>Most Medicare deadlines are annoying. You miss one, you pay a penalty, you carry on. This one
      is different in kind: miss it and a product you wanted may simply stop being available to you, for
      the rest of your life, because of your medical history.</p>

      <p>It is called the <strong>Medigap open enrollment period</strong>. It lasts six months, it happens
      once, and almost nobody is told what it costs to let it pass.</p>

""" + facts('The window, precisely', [
        ('How long', 'Six months. One time. It does not repeat and it cannot be reopened.'),
        ('When it starts', 'The first month you are <strong>both 65 or older and enrolled in Part '
                           'B</strong> &mdash; not your birthday. Delaying Part B for employer coverage '
                           'delays this too.'),
        ('What it guarantees', 'Any Medigap policy sold in your state, at the standard rate, with no '
                               'health questions and no refusal.'),
        ('What closes with it', 'In most states, insurers may then ask your full medical history, charge '
                                'you more for it, or decline you outright.'),
        ('Where the rules are better', 'A few states &mdash; New York, Connecticut, Massachusetts and '
                                       'Maine among them &mdash; require guaranteed issue beyond this '
                                       'window. The rules differ between them, so check your own.'),
        ('If you move', 'State protections generally attach to where you live rather than following '
                        'you, so a move can change what is available. Check the rules of the state you '
                        'are moving to before assuming they match.'),
    ]) + """
      <h2>What underwriting actually means here</h2>

      <p>Inside the window, the application asks your name, your address and your Medicare number. Outside
      it, in most of the country, the application asks about your health &mdash; and the answers decide
      the outcome.</p>

      <p>This is not a formality that ends with a higher price. Insurers can and do decline applications
      outright. The conditions that cause trouble are the ordinary ones people accumulate in their
      sixties and seventies, not exotic ones. Someone perfectly healthy at 65 who buys nothing, and
      returns at 70 after a cardiac event or a cancer diagnosis, is applying in a different world from
      the one they left.</p>

""" + AD_INLINE + """
      <h2>Why people miss it</h2>

      <p>Almost always for a reason that felt sensible at the time.</p>

""" + check([
        'They chose Medicare Advantage at 65, which is a perfectly reasonable choice &mdash; but the '
        'Medigap window ran out in the background while they were in it.',
        'They were still working with employer coverage, delayed Part B, and did not realize the '
        'Medigap clock had not started rather than being paused indefinitely.',
        'They looked at the premium at 65, decided they were healthy and did not need it, and planned '
        'to revisit the question later. Later is the problem.',
        'Nobody ever mentioned it. It is not on the enrollment paperwork and it is not what the '
        'advertising is about.',
    ]) + """
      <h2>The exceptions worth knowing</h2>

      <p>The window is not the only route to guaranteed issue, and if you are outside it the exceptions
      are where to look first. Federal rules create guaranteed-issue rights in specific circumstances
      &mdash; among them losing employer or union coverage that was paying alongside Medicare, and a
      Medicare Advantage plan leaving your area or ending its contract.</p>

      <p>There is also a <strong>trial right</strong>: if you joined a Medicare Advantage plan when you
      first became eligible at 65, you generally have twelve months to switch back to Original Medicare
      and buy a Medigap policy with guaranteed issue. Twelve months, from the start of that plan. It is a
      genuine safety net and it is easy to spend without noticing.</p>

      <p>These rights are narrower than the open enrollment window, they come with their own timing
      rules, and they are worth confirming with your state's own program rather than an insurer's
      salesperson.</p>

      <blockquote class="pull">
        <p>The decision at 65 is not only which coverage you want now. It is whether you keep the option
        of changing your mind later.</p>
      </blockquote>

      <h2>What to do about it</h2>

      <p><strong>If you are approaching 65,</strong> find out exactly when your six months start &mdash;
      it hangs on your Part B enrollment date, not your birthday &mdash; and write the end date down.
      Decide inside it, not after.</p>

      <p><strong>If you are still working past 65 on employer coverage,</strong> the window opens when
      you take Part B. That is usually when you retire, and it is the moment to have this decision
      already made rather than to start thinking about it.</p>

      <p><strong>If the window has closed,</strong> it is still worth applying rather than assuming the
      answer. Underwriting standards vary between insurers, and a decline from one is not a decline from
      all. Check whether your state has broader rules, and check whether any guaranteed-issue right
      applies to your situation.</p>

      <p>Free help exists and does not sell anything: every state has a <strong>SHIP</strong>, a State
      Health Insurance Assistance Program, with counselors who earn no commission whichever way you go.
      Their number is on our <a href="/numbers">page of numbers worth keeping by the phone</a>.</p>
""",
    'sources': [
        ('Medicare &mdash; When can I buy Medigap?',
         'https://www.medicare.gov/health-drug-plans/medigap/ready-to-buy'),
        ('Medicare Interactive &mdash; Medigap enrollment periods and guaranteed issue',
         'https://www.medicareinteractive.org/understanding-medicare/health-coverage-options/'
         'supplemental-insurance-for-original-medicare-medigaps/'
         'medigap-purchasing-details-enrollment-periods-guaranteed-issue-and-more'),
        ('NCOA &mdash; Medigap open enrollment',
         'https://www.ncoa.org/article/medigap-open-enrollment-period/'),
        ('SHIP &mdash; free local Medicare counseling', 'https://www.shiphelp.org/'),
    ],
    'next': {'slug': 'advantage-vs-original',
             'title': 'Advantage or Original: what actually differs',
             'blurb': 'The choice this window is really about, laid out without the sales pitch.'},
}


# ------------------------------------------------------------- RMDs / QCDs
ARTICLES8['rmd-deadline'] = {
    'title': 'RMD Rules 2026: Age 73 or 75, and QCDs &mdash; The Second Half Guide',
    'eyebrow': 'Facts &amp; thresholds',
    'h1': 'The withdrawal the IRS requires, and the deadline that costs 25%',
    'dek': 'At some point the tax deferral ends and the government wants its share. The age depends on '
           'your birth year, the first one has a trap in it, and there is a route that skips the tax '
           'entirely.',
    'meta': '6 minute read &middot; 2026 figures verified against IRS rules',
    'checked': CHECKED,
    'body': """      <p>Most money in a traditional 401(k) or IRA has never been taxed. That was the deal: deduct it
      going in, pay on the way out. Required minimum distributions are the government collecting on the
      second half of that arrangement, and they are not optional.</p>

      <p><em>Most</em>, because some traditional IRAs also hold nondeductible contributions &mdash;
      money that was already taxed on the way in. That creates after-tax basis, it is tracked on IRS
      Form 8606, and it means part of each withdrawal is not taxable again. If you ever made a
      contribution you could not deduct, this applies to you and it is worth telling whoever prepares
      your return.</p>

      <p>Three things about them catch people, and the first is that the starting age is no longer a
      single number.</p>

""" + facts('The rules, in 2026 terms', [
        ('When they start', 'Age <strong>73</strong> if you were born between 1951 and 1959. Age '
                            '<strong>75</strong> if you were born in 1960 or later.'),
        ('The annual deadline', '31 December, every year after the first.'),
        ('The first one only', 'You may delay it to <strong>1 April</strong> of the following year '
                               '&mdash; which is where the trap is.'),
        ('Missing one', 'A <strong>25% excise tax</strong> on whatever you failed to withdraw. It drops '
                        'to 10% if you correct it within the IRS window, generally two years.'),
        ('Which accounts', 'Traditional IRAs, SEP and SIMPLE IRAs, and most workplace plans. Roth IRAs '
                           'have never required them for the original owner.'),
        ('The charitable route', 'A qualified charitable distribution from an IRA, available from age '
                                 '<strong>70&frac12;</strong>, up to <strong>$111,000</strong> per '
                                 'person in 2026 &mdash; $222,000 for a married couple each giving from '
                                 'their own IRA.'),
    ]) + """
      <h2>The first-year trap</h2>

      <p>The rule that lets you delay your first withdrawal to 1 April sounds like a kindness. Used
      carelessly it is expensive, because the second one is still due on 31 December of that same year.</p>

      <p>Delay the first and you take <strong>two distributions in one calendar year</strong>. Both land
      in the same tax return, stacked on top of each other. That can push you into a higher bracket, make
      more of your Social Security taxable, and &mdash; the one people do not see coming &mdash; raise
      your income above an IRMAA threshold, which sets your Medicare premium two years later.</p>

      <p>Sometimes doubling up genuinely is the right call, if the following year's income will be much
      lower. But it should be a decision, not a side effect of not getting round to it in December.</p>

""" + AD_INLINE + """
      <h2>The penalty is real, and it is survivable</h2>

      <p>Miss a distribution and the excise tax is <strong>25% of the amount you should have taken</strong>.
      Not 25% of your account, and not a tax on the withdrawal itself &mdash; a penalty on the shortfall,
      on top of the ordinary income tax you still owe when you do take it.</p>

      <p>It used to be 50%, which was among the harshest penalties in the tax code. SECURE 2.0 cut it,
      and added something more useful: correct the mistake within the IRS's window, generally two years,
      and the penalty falls to <strong>10%</strong>. There is also a waiver route &mdash; file Form 5329
      promptly and show the miss had reasonable cause &mdash; and the IRS does grant it.</p>

      <p>So a missed distribution is a problem to fix quickly rather than a catastrophe to panic about.
      The expensive version is the one nobody notices for years.</p>

      <h2>The part worth knowing if you give to charity</h2>

      <p>A <strong>qualified charitable distribution</strong> sends money straight from your IRA to a
      charity, and it never counts as your income at all.</p>

      <p>That last clause is what makes it behave differently from a donation you write a check for and
      deduct. A deduction only reduces tax if you itemize, and most people over 65 now take the standard
      deduction instead. A QCD is not a deduction at all: the money never enters your income, which also
      keeps it out of the calculations that read your income &mdash; the taxable share of your Social
      Security, and the IRMAA thresholds that set your Medicare premium two years later.</p>

""" + check([
        'Available from age <strong>70&frac12;</strong> &mdash; earlier than RMDs begin, so there are '
        'years when you can do this before you are required to withdraw anything.',
        'Up to <strong>$111,000</strong> per person in 2026. A married couple can each give that much '
        'from their own IRA.',
        'It counts toward your RMD for the year, up to the amount given.',
        'It must go <strong>directly</strong> from the IRA to the charity. Money that passes through '
        'your hands first is an ordinary withdrawal, taxed as one.',
        'It has to be a qualifying charity. Donor-advised funds and private foundations generally do '
        'not count.',
    ]) + """
      <blockquote class="pull">
        <p>The deadline is 31 December, and it is a real one. Custodians get busy in the last week of
        December, and a transfer that does not complete in time counts as missed.</p>
      </blockquote>

      <h2>What to actually do</h2>

      <p><strong>Find your age.</strong> Born 1951 to 1959, it is 73. Born 1960 or later, it is 75. This
      changed under SECURE 2.0 and a great deal of material still in circulation says 73 for everyone.</p>

      <p><strong>Do it in November.</strong> Not late December. Custodians are slow at year end,
      paperwork gets returned, and the deadline does not care why the transfer failed to settle.</p>

      <p><strong>If you have several accounts,</strong> the rules on which ones can be combined differ
      between IRAs and workplace plans. This is the part where people miscalculate in good faith, and
      it is worth asking your custodian rather than assuming.</p>

      <p><strong>The distinction is worth knowing before December,</strong> because the two routes are
      not interchangeable once the money has moved. A distribution that reaches you first is an ordinary
      taxable withdrawal, whatever you do with it afterward.</p>
""",
    'sources': [
        ('IRS &mdash; Required minimum distributions',
         'https://www.irs.gov/retirement-plans/retirement-plan-and-ira-required-minimum-distributions-faqs'),
        ('IRS &mdash; Retirement plan and IRA required minimum distributions',
         'https://www.irs.gov/retirement-plans/plan-participant-employee/'
         'retirement-topics-required-minimum-distributions-rmd'),
        ('Congressional Research Service &mdash; Qualified charitable distributions from IRAs',
         'https://www.congress.gov/crs-product/IF11377'),
        ('IRS &mdash; Form 5329', 'https://www.irs.gov/forms-pubs/about-form-5329'),
    ],
    'next': {'slug': 'irmaa',
             'title': 'The Medicare surcharge based on what you earned two years ago',
             'blurb': 'The threshold a doubled-up first distribution can push you over.'},
}


# --------------------------------------------- senior deduction: phase-out
ARTICLES8['senior-deduction-phaseout'] = {
    'title': 'Senior Deduction Phase-Out: The $75,000 Line &mdash; The Second Half Guide',
    'eyebrow': 'Facts &amp; thresholds',
    'h1': 'The $75,000 line, and what the senior deduction is worth above it',
    'dek': 'The $6,000 deduction does not stop at the threshold, it shrinks. Six cents for every dollar '
           'over &mdash; which means the arithmetic is worth doing before December.',
    'meta': '5 minute read &middot; 2026 figures verified against IRS rules',
    'checked': CHECKED,
    'body': """      <p>Most coverage of the new senior deduction stops at two numbers: <strong>$6,000</strong>, and
      <strong>$75,000</strong>. You get the deduction if you are 65 or older, and it starts phasing out
      above $75,000 of income.</p>

      <p>What almost nothing explains is what happens <em>between</em> those points, which is where a lot
      of people actually are. It does not vanish at $75,001. It shrinks, at a fixed rate, and the rate is
      slow enough that the deduction is still worth real money well past the threshold.</p>

""" + facts('The arithmetic, 2026', [
        ('The deduction', '$6,000 per person 65 or older. A married couple where both qualify get '
                          '<strong>$12,000</strong> between them.'),
        ('Where it starts shrinking', 'Modified adjusted gross income above <strong>$75,000 single</strong> '
                                      'or <strong>$150,000 married filing jointly</strong>.'),
        ('How fast', 'It falls by <strong>6 cents for every dollar</strong> of income above the threshold.'),
        ('Where it reaches zero', '$175,000 single. $250,000 joint.'),
        ('Which years', 'Tax years <strong>2025 through 2028</strong> only. It is temporary.'),
        ('Standard or itemized', 'You can claim it either way. It is not tied to taking the standard '
                                 'deduction.'),
    ]) + """
      <h2>What the taper actually costs you</h2>

      <p>Six percent is gentler than people assume. Work it through for a single filer 65 or older:</p>

""" + check([
        'At <strong>$75,000</strong> or below &mdash; the full $6,000.',
        'At <strong>$85,000</strong> &mdash; $10,000 over the line, so $600 comes off. You still have '
        '$5,400.',
        'At <strong>$100,000</strong> &mdash; $25,000 over, so $1,500 comes off. Still $4,500.',
        'At <strong>$125,000</strong> &mdash; half gone. $3,000 left.',
        'At <strong>$175,000</strong> &mdash; nothing left.',
    ]) + """
      <p>The practical point is that <strong>being over the threshold is not the same as being out</strong>.
      Someone at $100,000 who assumes the deduction is not for them is leaving $4,500 of deduction
      unclaimed on the assumption that a headline number applied to them.</p>

""" + AD_INLINE + """
      <h2>What tends to push people over the line</h2>

      <p>Because the taper keys off a single year's income, what usually moves someone up the slope is
      not their ordinary income at all. It is a one-off: a large retirement distribution, a Roth
      conversion, the sale of a house or a long-held investment, or a lump sum arriving in a year that
      was otherwise quiet.</p>

      <p>Worth recognizing if it describes your year, because the deduction you get is set by that year's
      figure rather than by how your income usually looks.</p>

      <p>A second threshold watches the same money. <a href="/irmaa">IRMAA</a>, the Medicare surcharge,
      is also calculated from modified adjusted gross income &mdash; but from the return filed
      <strong>two years earlier</strong>, so a high 2026 income sets a 2028 premium. And unlike this
      deduction it is a cliff rather than a taper: in 2026 the first step above $109,000 single or
      $218,000 joint adds about $975 to a year's Part B premiums, whether you cross the line by ten
      thousand dollars or by one.</p>

      <p>The two do not use identical calculations and their thresholds are far apart. The point is only
      that a single unusual year can show up in both places, and in the Medicare one it shows up
      late.</p>

      <blockquote class="pull">
        <p>The deduction tapers. The Medicare surcharge does not &mdash; and it reads your income two
        years after the fact.</p>
      </blockquote>

      <h2>Two things to check before assuming</h2>

      <p><strong>Which income figure applies.</strong> The threshold is modified adjusted gross income
      &mdash; not your gross pay, and not your taxable income after deductions. It starts from adjusted
      gross income and adds certain amounts back, tax-exempt interest and some foreign-income exclusions
      among them. If none of those apply to you the two figures are the same; if they do, the number that
      counts here is the higher one.</p>

      <p><strong>Whether both of you qualify.</strong> The $12,000 for a married couple requires
      <em>both</em> spouses to be 65 or older. A couple where one is 66 and the other is 63 gets $6,000
      this year and the second $6,000 in the year the younger one turns 65 &mdash; assuming the provision
      is still in force, which it is not scheduled to be after 2028.</p>

      <p>None of this is a reason to earn less. It is a reason to know the line is a slope rather than a
      wall, and roughly where on it you are standing.</p>
""",
    'sources': [
        ('IRS &mdash; Check your eligibility for the new enhanced deduction for seniors',
         'https://www.irs.gov/newsroom/check-your-eligibility-for-the-new-enhanced-deduction-for-seniors'),
        ('IRS &mdash; 2026 filing season updates and resources for seniors',
         'https://www.irs.gov/newsroom/2026-filing-season-updates-and-resources-for-seniors'),
    ],
    'next': {'slug': 'no-tax-on-social-security',
             'title': '&ldquo;No tax on Social Security&rdquo;: what the law actually did',
             'blurb': 'The deduction is real. The phrase attached to it in the press is not.'},
}


# ------------------------------------- "no tax on Social Security"
ARTICLES8['no-tax-on-social-security'] = {
    'title': 'No Tax on Social Security: What the Law Actually Did &mdash; The Second Half Guide',
    'eyebrow': 'Facts &amp; thresholds',
    'h1': '&ldquo;No tax on Social Security&rdquo;: what the law actually did',
    'dek': 'A real deduction arrived for people over 65. It is not what the phrase says it is, and the '
           'rules taxing Social Security were not touched.',
    'meta': '6 minute read &middot; Verified against IRS and SSA rules',
    'checked': CHECKED,
    'body': """      <p>If you have heard that Social Security is no longer taxed, you heard something that was said a
      great deal and is not accurate. What actually passed was a <strong>$6,000 deduction for people 65
      and older</strong>, and the distinction between those two things decides whether your own tax bill
      changes.</p>

      <p>The deduction is real and worth having. It is just a different mechanism, pointed at a different
      group of people, and it leaves the rules that tax Social Security exactly where they were.</p>

""" + facts('The two things being confused', [
        ('What passed', 'A $6,000 deduction per person 65 or older, for tax years 2025 through 2028, '
                        'phasing out above $75,000 single or $150,000 joint.'),
        ('What did not pass', 'Any change to how Social Security benefits are taxed. Those rules are '
                              'untouched.'),
        ('Who it reaches', 'People 65 and older. Social Security can start at 62, and disability and '
                           'survivor benefits reach people younger still &mdash; none of them get this.'),
        ('What it reduces', 'Your taxable income generally. Not your benefit, and not the share of your '
                            'benefit that counts as income.'),
        ('Whether it ends', 'Yes. After 2028 unless Congress extends it.'),
    ]) + """
      <h2>How Social Security is actually taxed</h2>

      <p>The rule that decides this is called <strong>provisional income</strong> &mdash; roughly your
      adjusted gross income, plus any tax-exempt interest, plus half of your Social Security benefit.
      Where that lands sets how much of the benefit is taxable.</p>

""" + facts('The thresholds that decide it', [
        ('Single, under $25,000', 'None of your benefit is taxable.'),
        ('Single, $25,000&ndash;$34,000', 'Up to 50% of the benefit becomes taxable.'),
        ('Single, above $34,000', 'Up to 85% becomes taxable.'),
        ('Married filing jointly', 'The same tiers, at $32,000 and $44,000.'),
        ('The part that matters', 'None of these figures has ever been adjusted for inflation. The '
                                  '$25,000 and $32,000 tiers were enacted in 1983 and applied from 1984; '
                                  'the $34,000 and $44,000 tiers were enacted in 1993 and applied from '
                                  '1994.'),
    ]) + """
""" + AD_INLINE + """
      <h2>Why those frozen numbers matter more than the deduction</h2>

      <p>Almost everything else in the tax code moves with inflation. Brackets shift each year. The
      standard deduction rises. The Social Security wage base climbs with average wages. The benefit
      itself gets a cost-of-living adjustment every January.</p>

      <p>These thresholds do not move at all. They were enacted in 1983 and 1993, took effect the
      following year in each case, and have stayed at those figures while everything measured against
      them grew.</p>

      <p>The effect is slow and one-directional. When the first tier was written, taxation of benefits
      reached fewer than one in ten recipients. It now reaches well over half. Nobody voted for that
      each year; it is simply what happens when a fixed line meets four decades of inflation.</p>

      <blockquote class="pull">
        <p>Your COLA raises your benefit every January. The line that decides whether the benefit is
        taxed has not moved since 1984. Those two facts have been pushing in opposite directions your
        whole retirement.</p>
      </blockquote>

      <h2>So what does the deduction actually do for you</h2>

      <p>It lowers your taxable income by up to $6,000, which for many people over 65 means less tax
      overall &mdash; and for some, enough less that they owe nothing. That is a genuinely good outcome
      and it is where the phrase came from.</p>

      <p>But note what it does not do:</p>

""" + check([
        'It does not change how much of your benefit is <strong>counted</strong> as income. The '
        'provisional income calculation runs exactly as before.',
        'It does not help anyone <strong>under 65</strong>, including people who claimed at 62 and '
        'people receiving disability or survivor benefits.',
        'It does not help if your income is <strong>above the phase-out</strong> &mdash; it shrinks by '
        'six cents per dollar over the threshold and is gone entirely at $175,000 single, $250,000 joint.',
        'It does not help if you already <strong>owed no federal income tax</strong>. A deduction reduces '
        'what is taxed; if nothing was being taxed, there is nothing to reduce.',
    ]) + """
      <p>That last one is worth sitting with, because it inverts the intuition. A deduction is only
      worth something if there is tax to reduce. Someone whose income is low enough that they owe no
      federal income tax gets no benefit from a larger deduction &mdash; not because of anything to do
      with Social Security, but because there was nothing to subtract from. The value lands in the
      middle, and it is largest for people with enough other taxable income to use it.</p>

      <h2>What to do about it</h2>

      <p>Two facts settle whether it reaches you: whether you are 65 by the end of the tax year, and
      where your income sits relative to $75,000 single or $150,000 joint. One feature is worth knowing
      because it is unusual and easily missed &mdash; the deduction applies whether you itemize or take
      the standard deduction, so it is not something you forfeit by itemizing.</p>

      <p>And treat &ldquo;no tax on Social Security&rdquo; as what it is: a description of a political
      goal rather than of the law. The <a href="/senior-deduction">deduction itself</a> is worth
      understanding on its own terms.</p>
""",
    'sources': [
        ('IRS &mdash; Check your eligibility for the new enhanced deduction for seniors',
         'https://www.irs.gov/newsroom/check-your-eligibility-for-the-new-enhanced-deduction-for-seniors'),
        ('SSA &mdash; Income taxes and your Social Security benefit',
         'https://www.ssa.gov/benefits/retirement/planner/taxes.html'),
        ('Congressional Research Service &mdash; Social Security: Taxation of Benefits',
         'https://www.congress.gov/crs-product/RL32552'),
    ],
    'next': {'slug': 'standard-deduction-65',
             'title': 'What someone over 65 can actually deduct in 2026',
             'blurb': 'Three separate amounts, and they stack. Most people only know about one.'},
}


# ------------------------------------------- stacking the deductions
ARTICLES8['standard-deduction-65'] = {
    'title': 'Standard Deduction Over 65 in 2026: How the Three Amounts Stack '
             '&mdash; The Second Half Guide',
    'eyebrow': 'Facts &amp; thresholds',
    'h1': 'What someone over 65 can actually deduct in 2026',
    'dek': 'There are three separate amounts, they stack, and most coverage mentions one. Together they '
           'come to more than most people expect.',
    'meta': '5 minute read &middot; 2026 figures verified against IRS rules',
    'checked': CHECKED,
    'body': """      <p>Ask most people over 65 what their standard deduction is and you will get one number, usually
      the headline one. There are actually <strong>three separate amounts</strong> reducing what you are
      taxed on, they are governed by different rules, and they add together.</p>

      <p>Two of them are parts of the standard deduction itself: a basic amount, plus an addition for
      being 65 or older. The third, the new $6,000 senior deduction, is <strong>not part of the standard
      deduction at all</strong> &mdash; it is a separate deduction that arrives whether you take the
      standard deduction or itemize. That distinction does no work in the arithmetic and a great deal of
      work in understanding what you are entitled to.</p>

""" + facts('The three, for 2026', [
        ('1. The base standard deduction', '$16,100 single. $32,200 married filing jointly. '
                                           '$24,150 head of household.'),
        ('2. The age-65 addition', 'An extra $2,050 if you are single or head of household. $1,650 '
                                   '<em>per qualifying spouse</em> if married. Part of the standard '
                                   'deduction, and decades old.'),
        ('3. The new senior deduction', 'A separate $6,000 per person 65 or older, for 2025 through 2028, '
                                        'phasing out above $75,000 single or $150,000 joint. New in '
                                        '2025.'),
        ('The unusual part', 'Number three applies <strong>whether you itemize or not</strong>. The first '
                             'two exist only if you take the standard deduction.'),
        ('The blindness addition', 'A separate matter from either. The same age-based addition amounts '
                                   'apply if you are blind, and someone who is both 65 or older and '
                                   'blind can claim it twice.'),
    ]) + """
      <h2>What that adds up to</h2>

      <p>A single filer aged 66, income under $75,000:</p>

""" + check([
        '$16,100 base standard deduction',
        '+ $2,050 age-65 addition',
        '+ $6,000 new senior deduction',
        '= <strong>$24,150 of income not taxed</strong>',
    ]) + """
      <p>A married couple, both 67, joint income under $150,000:</p>

""" + check([
        '$32,200 base standard deduction',
        '+ $1,650 &times; 2 for the age addition',
        '+ $6,000 &times; 2 for the new senior deduction',
        '= <strong>$47,500 of income not taxed</strong>',
    ]) + """
""" + AD_INLINE + """
      <h2>Why this changes the itemizing question</h2>

      <p>Itemizing only helps if your deductible expenses exceed <em>the standard deduction</em> &mdash;
      which is the first two amounts, not all three. For a couple both 67 that is $35,500, and it is a
      high bar: clearing it takes a large mortgage, serious medical bills, substantial charitable giving,
      or some combination.</p>

      <p>Note which amounts are actually on that scale. Because the $6,000 applies either way,
      <strong>it is not part of the comparison at all</strong> &mdash; it arrives whichever route you
      take. Only the first two sit on the standard-deduction side. For a couple both 67 that is $35,500,
      not $47,500, and $35,500 is the figure itemized deductions have to beat.</p>

      <p>The comparison is also not purely arithmetic: itemizing carries record-keeping, and some
      itemized deductions have their own floors and limits. But the headline number is the one above.</p>

      <blockquote class="pull">
        <p>The new $6,000 is not a reason to stop itemizing, because it arrives regardless. It is also
        not part of the sum that decides the question.</p>
      </blockquote>

      <h2>Two mistakes worth avoiding</h2>

      <p><strong>Assuming the age addition is the new thing.</strong> It is not. The extra amount for
      being 65 or older has existed for decades and is separate from the 2025 provision. Some coverage
      conflates them, which makes the new deduction sound smaller than it is or the old one sound newer
      than it is.</p>

      <p><strong>Assuming turning 65 mid-year means half.</strong> It does not. If you reach 65 by the
      end of the tax year, you get the full amounts for that year. There is no proration. The IRS also
      treats someone born on 1 January as having reached that age the previous day, which occasionally
      pulls a birthday back into the earlier tax year.</p>

      <p>If your income is above $75,000 single or $150,000 joint, the third amount shrinks rather than
      disappears &mdash; the arithmetic is in
      <a href="/senior-deduction-phaseout">the phase-out piece</a>. And if you heard this described as
      &ldquo;no tax on Social Security,&rdquo; <a href="/no-tax-on-social-security">that is a different
      thing entirely</a>.</p>
""",
    'sources': [
        ('IRS &mdash; 2026 filing season updates and resources for seniors',
         'https://www.irs.gov/newsroom/2026-filing-season-updates-and-resources-for-seniors'),
        ('IRS &mdash; Check your eligibility for the new enhanced deduction for seniors',
         'https://www.irs.gov/newsroom/check-your-eligibility-for-the-new-enhanced-deduction-for-seniors'),
    ],
    'next': {'slug': 'senior-deduction-sunset',
             'title': 'The senior deduction ends after 2028',
             'blurb': 'It is written into the law, and almost nobody claiming it seems to know.'},
}


# ------------------------------------------------- the 2028 sunset
ARTICLES8['senior-deduction-sunset'] = {
    'title': 'The Senior Deduction Ends After 2028 &mdash; The Second Half Guide',
    'eyebrow': 'Facts &amp; thresholds',
    'h1': 'The senior deduction ends after 2028',
    'dek': 'Four tax years, written into the law from the start and rarely mentioned in the coverage. '
           'What ends in 2029, what does not, and what the deduction actually depends on.',
    'meta': '5 minute read &middot; 2026 figures verified against IRS rules',
    'checked': CHECKED,
    'body': """      <p>The $6,000 deduction for people 65 and older is not a permanent feature of the tax code. It
      applies to <strong>tax years 2025, 2026, 2027 and 2028</strong>, and then it stops unless Congress
      acts.</p>

      <p>That was in the legislation from the beginning. It is not a rumor or a projection. And it is the
      part least likely to reach someone who learned about the deduction from a headline, because the
      headline never mentioned an end date.</p>

""" + facts('What is and is not scheduled to end', [
        ('The $6,000 senior deduction', 'Ends after tax year 2028.'),
        ('The base standard deduction', 'No scheduled expiry, and adjusted for inflation each year.'),
        ('The age-65 addition', 'No scheduled expiry. $2,050 single or $1,650 per qualifying spouse in '
                                '2026.'),
        ('Social Security taxation rules', 'Unchanged by this law and with no scheduled change. Those '
                                           'thresholds have been frozen since they took effect in 1984 '
                                           'and 1994.'),
        ('What happens in 2029', 'Nothing dramatic. Your deduction drops by up to $6,000 per qualifying '
                                 'person, and your taxable income rises accordingly.'),
    ]) + """
      <h2>What it is worth while it lasts</h2>

      <p>The value depends on your bracket, which is the honest answer, but the shape is easy. A deduction
      reduces the income you are taxed on, so $6,000 of deduction is worth $6,000 multiplied by whatever
      rate applies to your top dollars. For a couple where both qualify, the amount is $12,000.</p>

      <p>Over four years, for a couple in the middle brackets, that is not a rounding error. It is worth
      knowing it is a window rather than a permanent state.</p>

""" + AD_INLINE + """
      <h2>Two things the deadline does not change</h2>

      <p>An end date invites the thought that the deduction should be used while it is there. Two features
      of how it works are worth knowing before drawing that conclusion, because both cut against it.</p>

      <p><strong>It phases out on a single year's income.</strong> A large one-off sum landing in one of
      these years raises the income that sets the deduction, shrinking it by six cents on the dollar above
      $75,000 single or $150,000 joint and removing it entirely at $175,000 or $250,000. The deduction is
      not a fixed $6,000 waiting to be claimed; its size depends on the same figure any unusual income
      would raise.</p>

      <p><strong><a href="/irmaa">IRMAA</a> reads the same income, two years late.</strong> Medicare
      surcharges are calculated from the return filed two years earlier, so income in these years sets
      premiums in 2027 through 2030. Unlike this deduction, IRMAA is a cliff: crossing a threshold by one
      dollar costs the whole bracket, about $975 a year at the first step in 2026.</p>

      <blockquote class="pull">
        <p>The deduction is set by one year's income. So is the Medicare surcharge, two years later. An
        unusual year shows up in both.</p>
      </blockquote>

      <h2>Whether it will be extended</h2>

      <p>Congress can amend or extend the provision at any point, as it can with any part of the tax
      code, and temporary provisions are sometimes extended and sometimes allowed to lapse. What that
      will be here is not knowable now, and anyone telling you otherwise is guessing.</p>

      <p>What is knowable is the law as it currently stands, which provides the deduction through tax
      year 2028 and no further. That is the version worth understanding, and it is the one your 2029
      return will be filed against unless something changes before then.</p>

      <p>If you are not yet 65, the arithmetic is different again: the window may close before you are
      eligible for much of it. Someone turning 65 in 2028 gets one year of it.</p>
""",
    'sources': [
        ('IRS &mdash; Check your eligibility for the new enhanced deduction for seniors',
         'https://www.irs.gov/newsroom/check-your-eligibility-for-the-new-enhanced-deduction-for-seniors'),
        ('IRS &mdash; 2026 filing season updates and resources for seniors',
         'https://www.irs.gov/newsroom/2026-filing-season-updates-and-resources-for-seniors'),
    ],
    'next': {'slug': 'irmaa',
             'title': 'The Medicare surcharge based on what you earned two years ago',
             'blurb': 'The other threshold watching the same income, and the one that does not taper.'},
}
