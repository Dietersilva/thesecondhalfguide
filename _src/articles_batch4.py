#!/usr/bin/env python3
"""Fourth batch: the Medicare structure pieces and the vaccine thresholds."""

from build_articles import facts, check, AD_INLINE, CHECKED

ARTICLES4 = {}

# -------------------------------------------------- Advantage vs Original
ARTICLES4['advantage-vs-original'] = {
    'title': 'Medicare Advantage vs Original Medicare: The Structural Differences &mdash; The Second Half Guide',
    'eyebrow': 'Facts &amp; thresholds',
    'h1': 'Advantage or Original: what actually differs',
    'dek': 'Not which one you should pick &mdash; that depends on facts about you we don’t have. What '
           'each one is, how the money works, and the one decision that gets much harder to reverse later.',
    'meta': '8 minute read &middot; Verified against Medicare rules and 2026 figures',
    'checked': CHECKED,
    'body': """      <p>Almost everything written about this is a recommendation. You'll be told Advantage is a great
      deal, or that it's a trap, usually by someone earning a commission either way.</p>

      <p>This isn't that. These are two genuinely different structures, each with real advantages, and
      which one suits you depends on your health, your doctors, your travel, your state and your budget
      &mdash; none of which we know. What we <em>can</em> do is lay out how each is built, because most
      bad outcomes here come from not understanding the machinery rather than from picking wrong.</p>

      <p>And there's one piece of timing that genuinely matters, which almost nobody mentions until it's
      too late. That's at the bottom, and it's the reason to read this before your 65th birthday rather
      than after.</p>

      <h2>The two structures</h2>

      <p><strong>Original Medicare</strong> is the federal program: Part A (hospital) and Part B
      (medical). You can see any provider in the country who accepts Medicare, which is most of them. No
      networks, no referrals. It doesn't include drug coverage, so people add a Part D plan. And it has
      <em>no annual limit on what you can pay out of pocket</em> — which is why most people also buy a
      Medigap supplement policy to cover the gaps.</p>

      <p><strong>Medicare Advantage</strong> (Part C) is Medicare delivered through a private insurer.
      The plan covers everything Original covers, usually bundles in drug coverage, and often adds
      dental, vision, hearing and gym benefits. Premiums are frequently $0 beyond your Part B premium. In
      exchange, you use the plan's provider network, may need referrals, and prior authorisation is
      common. Critically, it <em>does</em> cap your annual out-of-pocket spending.</p>

""" + facts('The same care, two different money structures', [
        ('Where you can go', 'Original: any provider accepting Medicare, anywhere in the US. Advantage: '
                             'the plan’s network, usually regional, with higher costs or no coverage '
                             'outside it.'),
        ('Referrals &amp; approvals', 'Original: generally none. Advantage: referrals may be required, '
                                      'and prior authorisation is routine.'),
        ('Out-of-pocket cap', 'Original: none at all. Advantage: an annual maximum, set by the plan.'),
        ('Monthly cost', 'Original: Part B ($202.90 in 2026) plus Part D plus a Medigap premium. '
                         'Advantage: Part B plus often $0 or a low plan premium.'),
        ('When you use it', 'Original + Medigap: most costs already covered, few surprises. Advantage: '
                            'copays per visit, per test, per stay &mdash; cheaper if healthy, more if not.'),
        ('Extras', 'Original: none. Advantage: commonly dental, vision, hearing, fitness &mdash; usually '
                   'with modest annual caps.'),
    ]) + """
      <h2>The trade underneath all of it</h2>

      <p>Strip away the marketing and the structures make opposite bets.</p>

      <p>Original plus Medigap front-loads your costs into predictable monthly premiums, and in return
      very little is unpredictable afterward. You pay more in good years. In a catastrophic year you're
      largely insulated, and you can go to any specialist in the country without asking permission.</p>

      <p>Advantage front-loads almost nothing and charges you as you use care. If you're healthy, you may
      spend far less. If you get seriously ill, you'll pay copays up to your annual cap &mdash; which is
      real protection Original doesn't have on its own, but the cap can still be several thousand dollars,
      and you're navigating networks and prior authorisations while unwell.</p>

      <blockquote class="pull">
        <p>One structure charges you steadily whether or not you're sick. The other charges you when you
        are. Neither is a trick — but they suit different lives.</p>
      </blockquote>

""" + AD_INLINE + """
      <h2>Things that are true and often left out</h2>

      <ul>
        <li><strong>Advantage's out-of-pocket cap is a genuine advantage over bare Original.</strong>
        People who dislike Advantage skip this. Original Medicare alone has no ceiling, and that's a real
        exposure.</li>
        <li><strong>The dental and vision extras are real but capped.</strong> Often one or two thousand
        dollars a year. Useful for cleanings and glasses. Coverage for major work like implants varies by plan and is often limited or excluded &mdash; check the specific plan before assuming.</li>
        <li><strong>Networks change.</strong> Your doctor being in-network this year doesn't guarantee
        next year, which is why the fall review matters.</li>
        <li><strong>Prior authorisation is a real difference in kind</strong>, not just paperwork. It can
        mean delays for imaging, rehab or a skilled nursing stay.</li>
        <li><strong>Travel matters more than people expect.</strong> Original travels anywhere in the US.
        Most Advantage plans are regional — relevant for snowbirds and people whose grandchildren are
        three states away.</li>
        <li><strong>Neither covers much outside the country</strong>, and neither covers long-term
        custodial care.</li>
      </ul>

      <h2>The part that’s hard to reverse</h2>

      <p>Here is the fact that belongs at the center of this decision, and it's structural rather than a
      matter of opinion.</p>

      <p>You can switch between Advantage and Original every fall. That direction is easy. But going
      <em>back</em> to Original usually means wanting a Medigap policy to cover the gaps — and Medigap
      has its own enrollment rules, which are far less forgiving.</p>

""" + facts('Medigap enrollment', [
        ('Your one guaranteed window', 'Six months, starting the first month you are 65 <em>and</em> '
                                       'enrolled in Part B. During it, insurers must sell you any policy '
                                       'they offer at standard rates, regardless of health.'),
        ('The 12-month trial right', 'If you join Advantage when first eligible and leave within 12 '
                                     'months, you can buy Medigap with guaranteed issue. Apply no earlier '
                                     'than 60 days before your coverage ends and no later than 63 days '
                                     'after.'),
        ('After that', 'In most states insurers may use medical underwriting &mdash; they can ask health '
                       'questions, charge more, or decline you.'),
        ('Unless you live somewhere with better rules', 'New York, Connecticut and '
                                                        'Massachusetts don’t allow underwriting at all &mdash; '
                                                        'Massachusetts is guaranteed issue all year. '
                                                        'Washington allows switching after 90 days. A '
                                                        'growing list of states &mdash; including '
                                                        'California, Illinois, Oregon, Nevada, Maryland '
                                                        'and Virginia &mdash; run &ldquo;birthday '
                                                        'rules&rdquo; giving an annual window.'),
    ]) + """
      <p>The practical consequence: choosing Advantage at 65 is not symmetrical with choosing Original.
      One leaves the door open; the other may not. If you're in New York — as we are — this matters far
      less, because underwriting isn't permitted. In most of the country it matters a great deal.</p>

      <p>That's not an argument against Advantage. Millions of people are well served by it and pay less.
      It's an argument for knowing which decisions are reversible before you make them.</p>

      <h2>What to actually do</h2>

""" + check([
        'Check your <strong>state’s Medigap rules</strong> first. It changes how consequential this '
        'decision is more than any other single fact.',
        'List your <strong>doctors and hospitals</strong> and check them against any Advantage plan’s '
        'network for <em>next</em> year, not this one.',
        'Run your <strong>prescriptions</strong> through the Plan Finder at <em>medicare.gov</em> under '
        'both structures. Compare estimated annual totals, not premiums.',
        'Ask how often you <strong>travel or live elsewhere</strong> for part of the year.',
        'If you want Medigap, buy it in your <strong>six-month window</strong>. This is the single most '
        'time-sensitive thing in this article.',
        'Talk to your <strong>SHIP</strong> counselor &mdash; free, and unlike a broker, they earn '
        'nothing from your choice. Find yours at <em>shiphelp.org</em>.',
    ]) + """
      <p>Anyone who tells you one of these is simply better than the other is telling you about
      themselves, not about you. What's actually true is narrower and more useful: they're different
      machines, they fail in different ways, and one of the doors between them closes quietly six months
      after you turn 65.</p>
""",
    'sources': [
        ('Medicare &mdash; Your coverage options',
         'https://www.medicare.gov/basics/get-started-with-medicare/get-more-coverage/your-coverage-options'),
        ('Medicare &mdash; When can I buy Medigap?',
         'https://www.medicare.gov/health-drug-plans/medigap/ready-to-buy'),
        ('Medicare &mdash; Switching or dropping a Medigap policy',
         'https://www.medicare.gov/health-drug-plans/medigap/ready-to-buy/change-policies/switch-drop'),
        ('CMS &mdash; 2026 Medicare Parts A &amp; B premiums and deductibles',
         'https://www.cms.gov/newsroom/fact-sheets/2026-medicare-parts-b-premiums-deductibles'),
    ],
    'next': {'slug': 'medicare-gaps',
             'title': 'What Medicare doesn’t cover',
             'blurb': 'Dental, vision, hearing and the big one people discover too late &mdash; long-term care.'},
}

# -------------------------------------------------- what Medicare misses
ARTICLES4['medicare-gaps'] = {
    'title': 'What Medicare Doesn’t Cover &mdash; The Second Half Guide',
    'eyebrow': 'Facts &amp; thresholds',
    'h1': 'What Medicare doesn’t cover',
    'dek': 'Teeth, eyes, ears &mdash; and the very large one most people don’t discover until a parent '
           'needs it. Worth knowing before you’re planning around an assumption that isn’t true.',
    'meta': '6 minute read &middot; Verified against 2026 Medicare rules',
    'checked': CHECKED,
    'body': """      <p>Medicare is a good program. It is also, in a few specific places, not the program people
      assume it is &mdash; and the gaps tend to be discovered at the worst possible moment, usually in a
      hospital corridor.</p>

      <p>None of this is hidden. It's just that nobody sits you down at 65 and reads you the list.</p>

      <h2>The big one: long-term care</h2>

      <p>If you take one thing from this page, take this. <strong>Medicare does not pay for long-term
      custodial care.</strong> Not in a nursing home, not assisted living, not a home aide who helps with
      bathing, dressing, meals and medication.</p>

      <p>This is the single most consequential misunderstanding in American retirement planning, and it's
      easy to see how it arises, because Medicare <em>does</em> cover something that looks similar.</p>

""" + facts('Skilled nursing care under Medicare, 2026', [
        ('What’s covered', 'Short-term <em>skilled</em> care &mdash; rehabilitation and nursing after a '
                           'qualifying hospital stay. Recovery, not residence.'),
        ('The entry requirement', 'Generally a qualifying inpatient hospital stay of at least three days. '
                                  'Being held &ldquo;under observation&rdquo; rather than admitted does '
                                  'not count &mdash; a distinction that has cost families a great deal.'),
        ('Days 1&ndash;20', '$0 per day, after the $1,736 Part A deductible for the benefit period.'),
        ('Days 21&ndash;100', '$217.00 per day in coinsurance.'),
        ('Day 101 onward', 'You pay everything.'),
        ('Custodial care', 'Not covered at any point, at any duration, if that’s all you need.'),
    ]) + """
      <p>So the maximum is 100 days, it's conditional, and it's for getting better rather than for living
      somewhere. The care most people picture when they think &ldquo;nursing home&rdquo; is paid for
      privately, by long-term care insurance, or &mdash; once savings are largely gone &mdash; by
      Medicaid, which is a separate program with strict income and asset rules.</p>

      <blockquote class="pull">
        <p>Medicare covers getting better. It does not cover needing help. Those are different things,
        and the second one is far more expensive.</p>
      </blockquote>

""" + AD_INLINE + """
      <h2>Teeth, eyes and ears</h2>

      <p>Original Medicare covers essentially none of the routine care in these three areas:</p>

      <ul>
        <li><strong>Dental.</strong> No cleanings, fillings, extractions, dentures, root canals or
        implants. Very narrow exceptions exist where dental work is integral to a covered medical
        procedure.</li>
        <li><strong>Vision.</strong> No routine eye exams for glasses, and no glasses or contacts. Medical
        eye conditions &mdash; cataract surgery, glaucoma screening for those at risk, macular
        degeneration &mdash; <em>are</em> covered, and one pair of corrective lenses after cataract
        surgery.</li>
        <li><strong>Hearing.</strong> No routine hearing exams and no hearing aids. Diagnostic hearing
        tests ordered by a doctor are covered.</li>
      </ul>

      <p>Medicare Advantage plans commonly include these as extras, which is a genuine selling point
      &mdash; but the benefits are typically capped at modest annual amounts. Enough for a cleaning and
      a pair of glasses; not enough for implants or premium hearing aids. Read the cap, not the headline.</p>

      <p>One bright spot worth knowing: since 2022, hearing aids have been available
      <strong>over the counter</strong> in the US for mild to moderate hearing loss, without a
      prescription or an audiologist visit. That has pulled prices from many thousands of dollars down to
      the hundreds for a lot of people. Medicare still won't pay, but the number it isn't paying is much
      smaller than it used to be.</p>

      <h2>The rest of the list</h2>

      <ul>
        <li><strong>Care outside the United States</strong>, with narrow exceptions. Covered in our
        <a href="/travel-insurance">travel insurance</a> piece &mdash; this is the gap that catches
        travelers.</li>
        <li><strong>Routine foot care</strong> such as toenail clipping and callus removal, unless you
        have a qualifying condition like diabetes.</li>
        <li><strong>Cosmetic surgery</strong>, other than reconstruction after injury or covered surgery.</li>
        <li><strong>Most chiropractic care</strong> beyond spinal manipulation to correct subluxation.</li>
        <li><strong>Concierge or retainer fees</strong> charged by a practice for access. Medicare pays
        the covered services; the membership fee is yours.</li>
      </ul>

      <h2>And a few things people don’t realize <em>are</em> covered</h2>

      <p>The list runs both ways, and this side is under-used:</p>

""" + check([
        'An <strong>annual wellness visit</strong> at no cost &mdash; not a physical, but a planning and '
        'screening appointment. Widely under-claimed.',
        'A long list of <strong>preventive screenings</strong> at $0: cardiovascular, diabetes, several '
        'cancers, bone density, depression.',
        '<strong>Vaccines</strong> &mdash; ACIP-recommended ones are $0 under Part D, including shingles, '
        'which used to run a couple of hundred dollars.',
        '<strong>Diabetes supplies and self-management training</strong>, plus therapeutic shoes for '
        'those who qualify.',
        '<strong>Mental health care</strong>, including therapy, and since 2024 marriage and family '
        'therapists and mental health counselors can bill Medicare directly.',
        '<strong>Telehealth</strong>, though the rules have shifted repeatedly since 2020 &mdash; check '
        'current terms rather than assuming.',
    ]) + """
      <p>The gaps are real, but the useful reaction isn't alarm. Three of them &mdash; dental, vision,
      hearing &mdash; are budgetable annoyances of a few hundred to a couple of thousand a year. The
      fourth, long-term care, is a genuinely large financial risk, and it's the one worth thinking about
      deliberately rather than discovering.</p>

      <p>Everything else on this page is footnotes by comparison.</p>
""",
    'sources': [
        ('Medicare &mdash; What Part A &amp; Part B don’t cover',
         'https://www.medicare.gov/what-medicare-covers/what-part-a-covers'),
        ('Medicare &mdash; Skilled nursing facility care',
         'https://www.medicare.gov/coverage/skilled-nursing-facility-care'),
        ('Medicare &mdash; 2026 costs at a glance',
         'https://www.medicare.gov/basics/costs/medicare-costs'),
        ('FDA &mdash; Over-the-counter hearing aids',
         'https://www.fda.gov/medical-devices/hearing-aids/otc-hearing-aids-what-you-should-know'),
    ],
    'next': {'slug': 'vaccine-ages',
             'title': 'The vaccine schedule nobody hands you',
             'blurb': 'Which vaccines start at which age &mdash; and why several of them now cost nothing.'},
}

# -------------------------------------------------- vaccines by age
ARTICLES4['vaccine-ages'] = {
    'title': 'The Vaccine Schedule Nobody Hands You &mdash; The Second Half Guide',
    'eyebrow': 'Facts &amp; thresholds',
    'h1': 'The vaccine schedule nobody hands you',
    'dek': 'Children get a schedule on a card. Adults get nothing &mdash; despite several vaccines now '
           'starting at 50, and most of them costing nothing on Medicare.',
    'meta': '5 minute read &middot; Reflects current CDC recommendations',
    'checked': CHECKED,
    'body': """      <p>Every parent knows the childhood vaccine schedule. It arrives on a card, the doctor tracks it,
      and nobody has to go looking.</p>

      <p>Adults get no such thing. The recommendations exist, they're public, and they've changed
      meaningfully in the last two years &mdash; two of them moved <em>down</em> to age 50 — but there's
      no card, no reminder, and often no conversation unless you raise it.</p>

      <p>So here's the list, by the age it starts. Which of these is right for you is a conversation with
      your doctor; what they are and when they begin is just information, and you shouldn't have to dig
      for it.</p>

""" + facts('Adult vaccines by starting age', [
        ('From 50 &mdash; Shingles', 'Two doses of the recombinant vaccine, two to six months apart. '
                                     'Recommended for adults 50 and over. Shingles risk climbs sharply '
                                     'with age, and the complication people fear &mdash; lasting nerve '
                                     'pain &mdash; is what the vaccine most reduces.'),
        ('From 50 &mdash; Pneumococcal', 'CDC lowered this from 65 to <strong>50</strong> in late 2024. '
                                         'A single dose of a conjugate vaccine for most adults who '
                                         'haven’t had one.'),
        ('50&ndash;74 &mdash; RSV', 'For those at increased risk &mdash; chronic heart or lung disease, '
                                    'diabetes, kidney disease, weakened immunity, or living in a nursing '
                                    'home. A single dose.'),
        ('From 75 &mdash; RSV', 'Recommended for everyone, regardless of health. Also a single dose.'),
        ('Every 10 years &mdash; Td/Tdap', 'A tetanus booster, and most adults are overdue. Tdap once if '
                                           'you’ve never had it.'),
        ('Annually &mdash; Flu', 'Higher-dose and adjuvanted formulations are specifically designed for '
                                 'adults 65 and over.'),
        ('COVID-19', 'Recommendations have changed repeatedly and are now more risk-based. This is the '
                     'one genuinely worth checking current CDC guidance on rather than trusting anything '
                     'written months ago &mdash; including this.'),
    ]) + """
      <h2>The two that moved</h2>

      <p>If your mental model is &ldquo;vaccines are a 65-and-over thing,&rdquo; it's out of date by
      about fifteen years.</p>

      <p><strong>Pneumococcal moved from 65 to 50</strong> in October 2024 &mdash; a substantial change
      affecting tens of millions of people, and one that got remarkably little attention. The reasoning
      was that risk of pneumococcal disease starts climbing meaningfully well before 65.</p>

      <p><strong>RSV expanded downward too.</strong> It began as a 60-plus recommendation, and now covers
      everyone at 75, plus anyone 50 to 74 with a qualifying risk condition. RSV isn't just a childhood
      illness; in older adults it causes tens of thousands of hospitalisations a year.</p>

      <blockquote class="pull">
        <p>Two of these recommendations changed in the last two years, and both moved earlier. If nobody
        has raised them with you, that's not evidence they don't apply.</p>
      </blockquote>

""" + AD_INLINE + """
      <h2>The cost thing, which genuinely changed</h2>

      <p>This is the part worth knowing even if you've already decided how you feel about vaccines.</p>

      <p>Since January 2023, Medicare Part D has been required to cover all ACIP-recommended adult
      vaccines at <strong>$0 out of pocket</strong>. No copay, no coinsurance, no deductible.</p>

      <p>Before that, the shingles vaccine typically cost a couple of hundred dollars out of pocket
      &mdash; and cost was the single most-cited reason people skipped it. In 2023 alone, 10.3 million
      Part D enrollees received a free vaccine, saving over $400 million collectively. Shingles
      vaccination rose sharply the moment the price went to zero, which tells you the barrier was never
      really hesitancy for most people.</p>

      <p>One wrinkle worth knowing so you're not caught out: <strong>which part pays depends on the
      vaccine.</strong> Flu, pneumococcal and COVID vaccines are covered under Part B. Shingles, RSV and
      Tdap fall under Part D. Both routes are $0 for the recommended vaccines &mdash; but a pharmacy
      occasionally gets the billing wrong, and if you're asked to pay for one of these, that's worth
      questioning rather than accepting.</p>

      <h2>Worth doing</h2>

""" + check([
        'Ask at your <strong>next appointment</strong>: &ldquo;Which adult vaccines am I due for?&rdquo; '
        'It rarely comes up unless you raise it.',
        'If you’re <strong>50 to 64</strong>, don’t assume none of this applies. Shingles and '
        'pneumococcal both start at 50 now.',
        'Check your <strong>tetanus booster</strong> date. Most adults cannot remember it, which usually '
        'means it’s been more than ten years.',
        'If you have a <strong>chronic condition</strong> and are 50&ndash;74, ask specifically about RSV '
        '&mdash; the risk-based rule is easy for a busy practice to overlook.',
        'If you’re asked to <strong>pay</strong> for an ACIP-recommended vaccine on Medicare, ask them to '
        'check the billing. It should be $0.',
        'Pharmacies administer most of these <strong>without an appointment</strong>, which removes the '
        'usual reason for putting it off.',
    ]) + """
      <p>We don't tell people what to put in their bodies &mdash; that's genuinely a conversation for you
      and your doctor, and it should account for your health history in ways a website can't.</p>

      <p>But you can't have that conversation about something you don't know exists. Two of these
      recommendations changed recently, both moved earlier, and most of them now cost nothing. That's
      information you're entitled to have before deciding either way.</p>
""",
    'sources': [
        ('CDC &mdash; Adult immunisation schedule',
         'https://www.cdc.gov/vaccines/hcp/imz-schedules/adult-age.html'),
        ('CDC &mdash; Pneumococcal vaccine recommendations',
         'https://www.cdc.gov/pneumococcal/hcp/vaccine-recommendations/index.html'),
        ('CDC &mdash; RSV vaccine guidance for adults',
         'https://www.cdc.gov/rsv/hcp/vaccine-clinical-guidance/index.html'),
        ('CDC &mdash; Shingles vaccination',
         'https://www.cdc.gov/shingles/vaccines/index.html'),
        ('ASPE &mdash; Part D savings from eliminating vaccine cost-sharing',
         'https://aspe.hhs.gov/sites/default/files/documents/329fd579ada6515d3be404f06821c361/aspe-ira-vaccine-part-d.pdf'),
    ],
    'next': {'slug': 'senior-age',
             'title': '55, 60, 62, 65: when does &ldquo;senior&rdquo; actually start?',
             'blurb': 'Every threshold in this decade, now including the two that start at 50.'},
}
