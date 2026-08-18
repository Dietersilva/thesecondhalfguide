#!/usr/bin/env python3
"""Fifth batch: hearing aids after the OTC rule, long-term care costs, and the
cost-of-living adjustment."""

from build_articles import facts, check, AD_INLINE, CHECKED

ARTICLES5 = {}

# -------------------------------------------------------------- hearing aids
ARTICLES5['hearing-aids'] = {
    'title': 'Hearing Aids: What the Over-the-Counter Rule Actually Changed &mdash; The Second Half Guide',
    'eyebrow': 'Home &amp; everyday life',
    'h1': 'Hearing aids: what the over-the-counter rule actually changed',
    'dek': 'For decades a pair cost as much as a used car and required an audiologist. Since 2022 you '
           'can buy them off a shelf &mdash; and the price floor fell through.',
    'meta': '6 minute read &middot; Prices and FDA rules verified for 2026',
    'checked': CHECKED,
    'body': """      <p>Hearing loss is the most common untreated condition of later life, and the reason has never
      really been medical. It was that hearing aids cost thousands of dollars, weren't covered by
      Medicare, and required appointments with a specialist before you could even find out what you'd be
      buying.</p>

      <p>In August 2022 the FDA created a new category: over-the-counter hearing aids, for adults with
      perceived mild-to-moderate hearing loss. No prescription, no audiologist, no referral. You can buy
      them in a pharmacy or online the way you buy reading glasses.</p>

      <p>Four years on, that's produced a genuinely different market — and a fair amount of confusion
      about what's worth buying.</p>

""" + facts('What things cost in 2026', [
        ('OTC hearing aids', 'Roughly $200 to $2,500 a pair. Most full-featured self-fitting devices land '
                             'somewhere around $800&ndash;$1,500.'),
        ('Prescription hearing aids', 'Typically $2,500 to $6,000 a pair, usually bundled with fitting, '
                                      'follow-ups and adjustments.'),
        ('AirPods Pro 2', 'About $249. In 2024 the FDA authorised Apple’s Hearing Aid Feature — the first '
                          'over-the-counter hearing aid <em>software</em>.'),
        ('Medicare', 'Pays nothing toward any of them. Diagnostic hearing tests ordered by a doctor are '
                     'covered; the devices are not.'),
        ('Medicare Advantage', 'Often includes a hearing benefit, usually capped at a modest annual '
                               'amount. Read the cap.'),
    ]) + """
      <h2>The AirPods thing is real, and it surprises people</h2>

      <p>It sounds like a gimmick. It isn't.</p>

      <p>The FDA authorised Apple's Hearing Aid Feature for AirPods Pro 2 after testing with 118 adults
      with mild-to-moderate hearing loss, and found benefits comparable to professionally fitted devices.
      You take a hearing test on your iPhone, and it tunes the earbuds to your specific loss.</p>

      <p>For about $249, from a product many people already own, that is a substantial change. And
      there's a second-order effect worth naming: wearing AirPods in public reads as completely
      ordinary, where wearing a hearing aid still carries stigma for a lot of people. The device that
      finally gets someone to address their hearing may turn out to be the one that doesn't look like a
      medical device at all.</p>

      <blockquote class="pull">
        <p>The barrier to treating hearing loss was never really the hearing loss. It was a $5,000 price
        tag and a device people didn't want to be seen wearing.</p>
      </blockquote>

""" + AD_INLINE + """
      <h2>When over-the-counter is the wrong answer</h2>

      <p>This is the part the sellers gloss over, and it matters.</p>

      <p>OTC devices are authorised specifically for <strong>perceived mild-to-moderate</strong> hearing
      loss in adults. That word &ldquo;perceived&rdquo; is doing real work — you're self-diagnosing, and
      people are not reliably good at it. See a doctor rather than a shelf if any of these apply:</p>

      <ul>
        <li><strong>Hearing loss in one ear only</strong>, or noticeably worse in one ear. This can
        signal something that needs investigating.</li>
        <li><strong>Sudden hearing loss.</strong> This is treated as a medical emergency — days matter.</li>
        <li><strong>Pain, drainage, or a feeling of fullness</strong> in the ear.</li>
        <li><strong>Ringing in one ear only</strong>, or severe tinnitus.</li>
        <li><strong>Dizziness or balance problems</strong> alongside the hearing change.</li>
        <li><strong>Severe loss</strong> — if you can't follow conversation even in a quiet room, OTC
        devices are not designed for you.</li>
      </ul>

      <p>Also worth knowing: a lot of &ldquo;hearing loss&rdquo; turns out to be earwax. It's a
      genuinely common cause, it's trivially fixable, and it's an embarrassing thing to discover after
      spending a thousand dollars.</p>

      <h2>What you give up, and what you don’t</h2>

      <p>The honest comparison isn't &ldquo;cheap versus good.&rdquo; It's about what the price includes.</p>

      <p>Prescription hearing aids are bundled with a professional: someone measures your hearing
      properly, fits the device, and adjusts it over several appointments. Getting a hearing aid to work
      well is an iterative process, and that expertise is much of what you're paying for. For complex
      loss, it earns its money.</p>

      <p>OTC devices hand that job to you and to the app. Modern self-fitting software is genuinely good
      — it runs a test and tunes to your results — but if it isn't right, there's no one to adjust it
      but you.</p>

      <p>The practical middle path a lot of people take: get a real hearing test first (many are free,
      and the diagnostic one is covered by Medicare when a doctor orders it), then use those results to
      decide whether your loss is in OTC territory before spending anything.</p>

      <h2>Worth doing</h2>

""" + check([
        'Get your <strong>ears checked for wax</strong> before buying anything. It is the cheapest '
        'possible fix and a genuinely common cause.',
        'Get a <strong>real hearing test</strong>. Knowing whether your loss is mild, moderate or severe '
        'is what tells you which market you are shopping in.',
        'Check the <strong>return policy</strong> before you buy. The FDA does not require OTC hearing aids '
        'to come with one, though many sellers offer a return window voluntarily &mdash; and you will '
        'want it.',
        'If you have an iPhone and AirPods Pro 2, <strong>try the Hearing Aid Feature first</strong>. '
        'It costs nothing to find out.',
        'Give any device <strong>two to three weeks</strong>. Amplified hearing sounds strange at first '
        'and most people who quit, quit in the first few days.',
        'On Medicare Advantage, <strong>check the hearing benefit cap</strong> before assuming it covers '
        'a decent pair.',
    ]) + """
      <p>Untreated hearing loss isn't only about missing conversation. It's linked in research to social
      withdrawal and to a faster pace of cognitive decline — which is a good reason not to file this
      under vanity or wait until it's obviously bad.</p>

      <p>Medicare still won't pay. But the number it isn't paying has fallen by roughly an order of
      magnitude, and that is a genuinely different situation from the one most people still assume.</p>
""",
    'sources': [
        ('FDA &mdash; OTC hearing aids: what you should know',
         'https://www.fda.gov/medical-devices/hearing-aids/otc-hearing-aids-what-you-should-know'),
        ('FDA &mdash; Authorisation of the first OTC hearing aid software',
         'https://www.fda.gov/news-events/press-announcements/fda-authorizes-first-over-counter-hearing-aid-software'),
        ('NIDCD &mdash; Hearing aids',
         'https://www.nidcd.nih.gov/health/hearing-aids'),
        ('Medicare &mdash; Hearing and balance exams',
         'https://www.medicare.gov/coverage/hearing-balance-exams'),
    ],
    'next': {'slug': 'medicare-gaps',
             'title': 'What Medicare doesn’t cover',
             'blurb': 'Hearing is one of four gaps. The fourth is the one that costs real money.'},
}

# ------------------------------------------------------------ long-term care
ARTICLES5['long-term-care'] = {
    'title': 'Long-Term Care: The Numbers, Before the Sales Pitch &mdash; The Second Half Guide',
    'eyebrow': 'Facts &amp; thresholds',
    'h1': 'Long-term care: the numbers, before the sales pitch',
    'dek': 'It is one of the largest financial risks in retirement and the least planned for. Here is what care '
           'actually costs, who pays for it now, and what insurance does and doesn’t do.',
    'meta': '7 minute read &middot; Costs from the 2025&ndash;26 Cost of Care survey',
    'checked': CHECKED,
    'body': """      <p>We've said elsewhere that Medicare doesn't cover long-term custodial care. That's the single
      most consequential gap in American retirement planning, and it deserves more than a sentence.</p>

      <p>So this piece is the numbers. Not whether you should buy insurance — that depends on your
      assets, your health, your family and your state, and anyone who answers it without asking about
      all four is selling something. Just what things cost, who actually pays, and what the products
      do.</p>

      <h2>What care costs</h2>

""" + facts('National median costs', [
        ('Assisted living', 'About $6,200 a month &mdash; roughly $74,400 a year '
                            '(CareScout, 2025).'),
        ('Nursing home, semi-private', 'About $315 a day &mdash; roughly $115,000 a year.'),
        ('Nursing home, private room', 'About $355 a day &mdash; roughly $130,000 a year.'),
        ('Home health aide', 'Billed hourly. A few hours a day adds up faster than people expect; '
                             'round-the-clock care can exceed a nursing home.'),
        ('Trend', 'Costs have been rising roughly 4&ndash;5% a year, ahead of general inflation.'),
        ('Regional spread', 'Enormous. State medians range from around $3,250 a month to well over '
                            '$6,800 for the same level of assisted living.'),
    ]) + """
      <p>Those are medians, which means half of everything costs more. And the number that matters isn't
      the annual figure — it's the annual figure multiplied by however long care is needed, which is the
      part nobody can tell you in advance.</p>

      <blockquote class="pull">
        <p>Most people who need long-term care need it for a while and then don't. A minority need it for
        years. The problem is that the second group is the one that empties an estate, and you don't
        know which group you're in.</p>
      </blockquote>

      <h2>Who actually pays, today</h2>

      <p>In practice the money comes from four places, and it is worth being clear-eyed about each.</p>

      <ul>
        <li><strong>You do</strong>, out of savings, investments and home equity. This is how most care
        starts being paid for.</li>
        <li><strong>Medicaid</strong>, which is the largest payer of long-term care in the country.
        Eligibility is means-tested and set state by state, with income and asset limits, a look-back
        period on gifts and transfers that is five years in most states, and rules that turn on your
        circumstances rather than simply on having spent down savings. Not every facility accepts it,
        which can narrow the options available to you. Planning for it is genuinely specialist legal
        work.</li>
        <li><strong>Long-term care insurance</strong>, if you bought it, and if the policy's conditions
        are met.</li>
        <li><strong>Your family</strong>, in unpaid hours. This is the payer that never appears in the
        cost figures, and the one most often relied on &mdash; usually a daughter or a wife, usually
        while also working.</li>
      </ul>

      <p><strong>Medicare is not on that list</strong>, beyond the short skilled-nursing benefit after a
      qualifying hospital stay. Neither is your Medigap policy.</p>

""" + AD_INLINE + """
      <h2>What the insurance actually does</h2>

      <p>Traditional long-term care insurance pays a daily or monthly benefit once you can't perform a
      set number of <em>activities of daily living</em> — typically two of six: bathing, dressing,
      eating, transferring, toileting, continence — or have a cognitive impairment. Policies have an
      elimination period (a waiting period before benefits start, often 90 days), a benefit cap, and a
      benefit period.</p>

      <p>Three features decide most of the value:</p>

      <ul>
        <li><strong>Inflation protection.</strong> At 4&ndash;5% annual cost growth, a benefit fixed
        today is worth dramatically less in twenty years. Policies without it can look adequate and turn
        out not to be.</li>
        <li><strong>What counts as care.</strong> Most people want to stay home; make sure home care is
        covered as generously as facility care, not as an afterthought.</li>
        <li><strong>Who decides you qualify.</strong> The claims process is where these policies succeed
        or disappoint.</li>
      </ul>

      <h2>The industry’s own history is part of the decision</h2>

      <p>This deserves stating plainly, because it explains a lot about the market.</p>

      <p>Insurers badly mispriced traditional policies sold in the 1990s and 2000s — people lived longer,
      used more care, and let fewer policies lapse than the models assumed. The result was steep
      premium increases on existing policyholders, sometimes repeatedly, sometimes decades in. Some
      carriers left the market entirely.</p>

      <p>That's not a reason to dismiss the product. It <em>is</em> the reason to ask directly: can this
      premium be raised, by how much historically, and what happens to my coverage if I can no longer
      afford it? A policy you drop at 78 after twenty years of payments is the worst outcome available.</p>

      <p>It is also why <strong>hybrid policies</strong> — life insurance or an annuity with a
      long-term care rider — are now widely sold. They typically pay something to your heirs if care is
      never needed, which removes the &ldquo;use it or lose it&rdquo; objection, and premiums are often
      guaranteed. You generally pay more for that certainty.</p>

      <h2>What changes the answer</h2>

""" + check([
        '<strong>How much you have.</strong> Very large estates can self-fund; very small ones will '
        'reach Medicaid regardless. Insurance is aimed most squarely at the middle.',
        '<strong>Your age now.</strong> Premiums rise steeply with age and underwriting gets harder. '
        'The 50s and early 60s are when most people can still qualify affordably.',
        '<strong>Your health.</strong> These policies are medically underwritten. Waiting until you are '
        'worried is often waiting until you are uninsurable.',
        '<strong>Whether you are protecting a spouse.</strong> One partner needing years of care can '
        'consume assets the other still needs to live on. This is the strongest single argument for '
        'coverage.',
        '<strong>Your state.</strong> Partnership programs in many states let you shelter additional '
        'assets from Medicaid spend-down if you hold a qualifying policy.',
        '<strong>Who would actually provide care.</strong> Assuming a family member will is a plan with '
        'a person’s life inside it &mdash; worth discussing with them rather than about them.',
    ]) + """
      <p>The reason to think about this in your 50s and 60s rather than your 70s isn't that something is
      about to happen. It's that every option here — insurance, Medicaid planning, modifying a house,
      even an honest family conversation — is cheaper and more available before there's a crisis.</p>

      <p>The most expensive version of this is the one where nobody planned, and a family makes
      permanent financial decisions in a hospital corridor in the space of a week.</p>
""",
    'sources': [
        ('CareScout / Genworth &mdash; Cost of Care survey',
         'https://www.carescout.com/cost-of-care'),
        ('Medicare &mdash; Long-term care',
         'https://www.medicare.gov/coverage/long-term-care'),
        ('LongTermCare.gov &mdash; U.S. Administration for Community Living',
         'https://acl.gov/ltc'),
        ('NAIC &mdash; Long-term care insurance',
         'https://content.naic.org/insurance-topics/long-term-care-insurance'),
    ],
    'next': {'slug': 'medicare-gaps',
             'title': 'What Medicare doesn’t cover',
             'blurb': 'The four gaps, and why this one is in a different category from the others.'},
}

# ---------------------------------------------------------------------- COLA
ARTICLES5['cola'] = {
    'title': 'The COLA: Why a Raise Doesn’t Feel Like One &mdash; The Second Half Guide',
    'eyebrow': 'Facts &amp; thresholds',
    'h1': 'The COLA: why a raise doesn’t feel like one',
    'dek': 'Social Security rose 2.8% this year. For an average retired worker paying the standard Part B '
           'premium, Medicare took back about a third of it before the money ever arrived — which is the '
           'part the headlines skip.',
    'meta': '5 minute read &middot; Verified against SSA and CMS figures for 2026',
    'checked': CHECKED,
    'body': """      <p>Every October the Social Security Administration announces the cost-of-living adjustment for
      the following year, it leads the news for a day, and then a great many people notice in January
      that their deposit didn't grow by anything like what was announced.</p>

      <p>They're not imagining it. The arithmetic is public, it just never makes the headline.</p>

""" + facts('The 2026 adjustment', [
        ('2.8%', 'The COLA announced on 24 October 2025, effective with January 2026 payments.'),
        ('$2,015 → $2,071', 'The average retired worker’s monthly benefit &mdash; an increase of about '
                            '$56.'),
        ('$185.00 → $202.90', 'The standard Medicare Part B premium over the same period &mdash; an '
                              'increase of $17.90, deducted straight from the benefit.'),
        ('About $38', 'What is actually left of the average increase once Part B is taken out.'),
        ('~71 million', 'People receiving the adjustment.'),
        ('Next announcement', 'October 2026, for benefits beginning January 2027.'),
    ]) + """
      <h2>The part that gets skipped</h2>

      <p>For most retirees, the Part B premium is deducted from the Social Security payment before it
      arrives. So the announced COLA and the money you receive are two different numbers, and the gap
      between them is a Medicare premium increase that gets announced separately, weeks later, with far
      less coverage.</p>

      <p>This year that's $17.90 of an average $56 — a bit under a third of the raise, gone before it
      lands. For someone with a below-average benefit, the proportion is larger, because the Part B
      increase is a flat dollar amount while the COLA is a percentage. The smaller your benefit, the
      more of your raise Medicare takes.</p>

      <blockquote class="pull">
        <p>The COLA is a percentage. The Part B increase is a flat dollar amount. That asymmetry means
        the smallest benefits lose the largest share of their raise.</p>
      </blockquote>

      <p>One protection worth knowing about: the <strong>hold harmless</strong> provision generally
      prevents your Part B increase from exceeding your COLA increase in dollar terms, so most people's
      net Social Security payment shouldn't actually fall year over year. It protects you from going
      backward. It doesn't get you the raise you read about.</p>

""" + AD_INLINE + """
      <h2>Why the number is what it is</h2>

      <p>The COLA isn't a policy decision or a negotiation. It's a formula: the change in a price index
      called <strong>CPI-W</strong> — the Consumer Price Index for Urban Wage Earners and Clerical
      Workers — measured from the third quarter of one year to the third quarter of the next.</p>

      <p>The name gives away the long-running criticism. CPI-W tracks the spending of working people. It
      is not built around what retirees actually buy, and retirees spend a much larger share of their
      income on medical care and housing — categories that have generally risen faster than the basket
      as a whole.</p>

      <p>An alternative index, <strong>CPI-E</strong>, weights an older household's spending and has
      historically run slightly higher in most years. Proposals to switch to it come up regularly in
      Congress and have not passed. Whatever you think of that debate, it explains the persistent gap
      between an official adjustment and the felt experience of costs.</p>

      <h2>What the COLA does and doesn’t touch</h2>

      <ul>
        <li>It applies to <strong>Social Security retirement, survivor and disability benefits</strong>,
        and to <strong>SSI</strong>.</li>
        <li>It is <strong>permanent and compounding</strong> — it raises the base your future
        adjustments are calculated from. Over a long retirement this matters far more than any single
        year's number.</li>
        <li>It does <strong>not</strong> raise most private pensions, which frequently have no inflation
        adjustment at all.</li>
        <li>It does <strong>not</strong> change the income thresholds at which Social Security benefits
        become taxable. Those are not indexed, so each COLA pushes a few more people over them &mdash; a
        slow, quiet effect that catches households by surprise.</li>
      </ul>

      <h2>What to do with the announcement</h2>

""" + check([
        'When the number lands in <strong>October</strong>, wait for the <strong>Part B premium</strong> '
        'before doing any arithmetic. The two together are the real figure.',
        'Check your <strong>December statement</strong> at <em>ssa.gov</em> for the actual January '
        'amount rather than estimating it.',
        'If most of your income is a <strong>pension without a COLA</strong>, remember that its buying '
        'power falls every single year. This is the quiet risk in an otherwise comfortable retirement.',
        'Watch the <strong>taxation thresholds</strong>. They do not move, so a large COLA can '
        'incidentally make more of your benefit taxable.',
        'Ignore the annual round of <strong>&ldquo;the COLA is a scam&rdquo;</strong> and '
        '&ldquo;benefits are being cut&rdquo; posts. The formula is published, and the number is '
        'arithmetic, not a decision someone made about you.',
    ]) + """
      <p>2.8% on a $2,015 benefit is $56. Medicare takes $17.90 of it. What arrives is about $38 a
      month, and whether that keeps pace with your own costs depends on things CPI-W was never designed
      to measure.</p>

      <p>None of which makes the adjustment worthless — it compounds, it's permanent, and pensions
      without one lose ground every year by comparison. It's just a good deal smaller than the headline,
      and now you know exactly where the difference went.</p>
""",
    'sources': [
        ('SSA &mdash; 2026 cost-of-living adjustment fact sheet',
         'https://www.ssa.gov/news/en/cola/factsheets/2026.html'),
        ('SSA &mdash; Social Security announces 2.8 percent benefit increase for 2026',
         'https://www.ssa.gov/news/en/press/releases/2025-10-24.html'),
        ('CMS &mdash; 2026 Medicare Parts A &amp; B premiums and deductibles',
         'https://www.cms.gov/newsroom/fact-sheets/2026-medicare-parts-b-premiums-deductibles'),
        ('SSA &mdash; Income taxes and your Social Security benefits',
         'https://www.ssa.gov/benefits/retirement/planner/taxes.html'),
    ],
    'next': {'slug': 'senior-age',
             'title': '55, 60, 62, 65: when does &ldquo;senior&rdquo; actually start?',
             'blurb': 'The thresholds that shape this decade, and the two that carry permanent '
                      'consequences.'},
}
