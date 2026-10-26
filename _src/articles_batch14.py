#!/usr/bin/env python3
"""Fourteenth batch: three pieces built around things that changed or came due
in the first week of September 2026, checked against CMS's finalized CY2027
rule, the SSA/BLS COLA methodology, and a fresh FTC consumer alert. A fourth
idea -- the new SSA online disability tools mentioned in SSA's September
information package -- was dropped after checking: the underlying announcement
didn't carry an independently verifiable date or figure distinct from what
/compassionate-allowances already covers, so it would have been reaching."""

from build_articles import facts, check, AD_INLINE

ARTICLES14 = {}

CHECKED14 = '4 September 2026'

# ------------------------------------------------------------------- ANOC
ARTICLES14['anoc-letter'] = {
    'title': 'The Medicare Letter Arriving in September, and Why It’s Worth Reading '
             '&mdash; The Second Half Guide',
    'eyebrow': 'Facts &amp; thresholds',
    'h1': 'The Medicare letter arriving in September, and why it&rsquo;s worth reading',
    'dek': 'Every Medicare Advantage and Part D plan has to mail its Annual Notice of Change by '
           'September 30. It is a legal deadline, not a marketing mailer &mdash; and what actually '
           'changes is usually not the number printed at the top.',
    'meta': '6 minute read &middot; Verified against CMS&rsquo;s finalized 2027 rule',
    'checked': '16 October 2026',
    'body': """      <p>By the end of September, an envelope from your Medicare Advantage or Part D plan should have arrived that
      looks a lot like the junk mail already piling up ahead of open enrollment. It isn&rsquo;t. It&rsquo;s
      called the <strong>Annual Notice of Change</strong> &mdash; ANOC, if anyone shortens it in front of
      you &mdash; and federal rules require every plan to mail it to you by <strong>September 30</strong>,
      every year, without exception.</p>

      <p>What it contains is a full list of everything about your specific plan that changes on
      <strong>January 1</strong>. Not a comparison to other plans, not a sales pitch &mdash; a disclosure of
      what your own plan is about to do differently.</p>

""" + facts('What the ANOC actually is', [
        ('September 30', 'Legal deadline for every Medicare Advantage and Part D plan to mail its ANOC '
                         'for the coming year.'),
        ('January 1, 2027', 'When the changes described in this year&rsquo;s letter take effect.'),
        ('October 15 &ndash; December 7', 'The Annual Enrollment Period &mdash; the window during which '
                                          'you can act on anything the letter tells you, by switching '
                                          'plans.'),
        ('What it covers', 'Only your own plan&rsquo;s changes: premium, deductible, copays, coinsurance, '
                           'the drug formulary, and the provider network.'),
        ('What it does not do', 'Compare your plan to any other. That comparison is what the Medicare '
                                'Plan Finder at <em>medicare.gov</em> is for.'),
    ]) + """
      <h2>Why 2027&rsquo;s letter carries more weight than most</h2>

      <p>CMS finalized new Part D numbers for 2027 this spring, and they are a real jump. The annual
      out-of-pocket <strong>threshold</strong> on covered drugs rises to <strong>$2,400</strong>, up from
      $2,100 &mdash; that applies to every Part D plan. The <strong>defined-standard deductible</strong>
      rises to <strong>$700</strong>, up from $615 &mdash; that figure is the maximum a plan is allowed to
      charge; individual plans can and do set it lower, or waive it. Your ANOC will show what your specific
      plan actually charges for 2027, not necessarily the defined-standard number itself.</p>

      <blockquote class="pull">
        <p>The premium is only one of the numbers that can change what your coverage costs over a year.
        Drug tiers, formulary changes, cost-sharing and pharmacy status can matter just as much.</p>
      </blockquote>

""" + AD_INLINE + """
      <h2>Where the real information is buried</h2>

      <p>Plans typically lead with the premium, since it is the easiest single number to compare across
      plans. It is also, for most people, not where the money actually moves.</p>

      <p>A maintenance medication that sat on one pricing tier this year can move to a higher tier for
      2027, pick up a new prior-authorization requirement, or drop off the formulary entirely &mdash; and
      none of that shows up in the premium line. Neither does a preferred pharmacy losing its preferred
      status, which can change what the same prescription costs at the same counter. The letter discloses
      all of this. It just doesn&rsquo;t lead with it.</p>

      <p>The practical habit is simple: don&rsquo;t stop reading after the premium and deductible. Find the
      section listing drug tier and formulary changes, and check every medication you actually take against
      it &mdash; not just the ones you remember being expensive.</p>

      <h2>The other document in the envelope</h2>

      <p>Some plans mail the ANOC together with a second, much longer document called the <strong>Evidence
      of Coverage</strong>. They serve different jobs. The ANOC is a short summary of what&rsquo;s
      <em>changing</em>. The Evidence of Coverage is the full rulebook &mdash; everything the plan covers,
      what you pay for each type of service, and how to appeal a denied claim &mdash; regardless of whether
      anything about it changed this year. If your plan didn&rsquo;t include one, it&rsquo;s available on
      the plan&rsquo;s website or by calling member services, and it&rsquo;s the document to check if a
      specific benefit matters to you beyond what the ANOC happened to mention.</p>

      <p>If nothing has arrived, that&rsquo;s worth following up on rather than assuming your
      plan has no changes this year. CMS requires plans to get it to you by September 30; call your plan
      directly to request a copy, and if that doesn&rsquo;t resolve it, <strong>1-800-MEDICARE</strong> can
      help.</p>

      <h2>Advantage plans and standalone drug plans get different letters</h2>

      <p>What&rsquo;s inside the envelope depends on what kind of plan you have. A <strong>standalone Part
      D</strong> plan &mdash; drug coverage only, paired with Original Medicare &mdash; sends an ANOC that&rsquo;s
      almost entirely about drug costs: premium, deductible, formulary and pharmacy network. Most
      <strong>Medicare Advantage</strong> plans include Part D drug coverage along with medical coverage
      (a minority don&rsquo;t), so their ANOC typically covers more ground: the same drug-cost items, plus
      changes to the provider network, referral requirements, and the plan&rsquo;s service area. Losing a
      doctor from the network is exactly the kind of change that shows up in an Advantage ANOC and never
      appears at all in a standalone Part D one
      &mdash; another reason the letter is worth reading in full rather than skimmed for the premium line.</p>

      <h2>What to actually do with it</h2>

""" + check([
        'Find the <strong>formulary and drug-tier section</strong> and check every prescription you '
        'currently take against it, not just the ones you remember being expensive.',
        'Check whether your <strong>preferred pharmacy</strong> is still preferred. The same drug at the '
        'same counter can cost a different amount if that status changed.',
        'If you have Part D coverage, the <strong>2027 out-of-pocket threshold rises to $2,400</strong> '
        'no matter which plan you keep. The <strong>defined-standard deductible rises to $700</strong>, '
        'but that&rsquo;s the maximum &mdash; check your own ANOC for what your specific plan actually '
        'charges.',
        'If anything in the letter concerns you, the window to act is <strong>October 15 to December '
        '7</strong> &mdash; and it opened on October 15. Outside that window, this year&rsquo;s plan '
        'carries into next year automatically.',
        'The ANOC tells you what your plan is changing to. It does not tell you what a better-fit plan '
        'would cost &mdash; that comparison lives at the Medicare Plan Finder, separately.',
        'If you have an Advantage plan, check the <strong>network and referral</strong> sections too, not '
        'just drug costs &mdash; a doctor leaving the network is exactly the kind of change this letter '
        'exists to disclose.',
    ]) + """
      <p>Nobody enjoys reading insurance mail closely. This is the one piece of it each year built entirely
      out of things that are about to be true whether you read it or not &mdash; which is the whole case for
      reading it while the enrollment window is still open, through December 7.</p>
""",
    'sources': [
        ('CMS &mdash; Contract Year 2027 Medicare Advantage and Part D Final Rule (fact sheet)',
         'https://www.cms.gov/newsroom/fact-sheets/contract-year-2027-medicare-advantage-part-d-final-rule'),
        ('UnitedHealthcare &mdash; Medicare plan Annual Notice of Change: what to look for',
         'https://www.uhc.com/news-articles/medicare-articles/medicare-plan-annual-notice-of-change-what-to-look-for'),
        ('Kiplinger &mdash; Medicare is changing in 2027: 8 things that will impact your wallet',
         'https://www.kiplinger.com/retirement/medicare/changes-coming-to-medicare-in-2027'),
        ('24/7 Wall St. &mdash; Medicare&rsquo;s 2027 drug deductible is $700, up $85',
         'https://247wallst.com/personal-finance/2026/08/28/medicares-2027-drug-deductible-is-700-up-85-you-pay-all-of-it-before-your-plan-pays-anything/'),
        ('National Council on Aging &mdash; What is a Medicare Annual Notice of Change (ANOC)?',
         'https://www.ncoa.org/article/what-is-a-medicare-annual-notice-of-change-anoc/'),
    ],
    'next': {'slug': 'drug-cap',
             'title': 'The $2,100 drug cap: real protection, narrower than it sounds',
             'blurb': 'What the out-of-pocket cap covers, what it doesn&rsquo;t, and the 2027 numbers '
                      'this year&rsquo;s letter is about to confirm.'},
}

# --------------------------------------------------------------- 2027 COLA
ARTICLES14['cola-2027-estimate'] = {
    'title': 'The 2027 Social Security COLA Is 3.6% &mdash; The Second Half Guide',
    'eyebrow': 'Facts &amp; thresholds',
    'h1': 'The 2027 Social Security COLA is 3.6%',
    'dek': 'Social Security announced the official 2027 raise on 14 October: 3.6%, starting with January '
           'benefits. The earnings limits and the taxable maximum moved with it &mdash; and Medicare&rsquo;s '
           '2027 premium, which decides what you keep, has not been announced.',
    'meta': '5 minute read &middot; Checked against the SSA announcement and independent reports',
    'checked': '16 October 2026',
    'body': """      <p>On 14 October 2026 the Social Security Administration announced a <strong>3.6%</strong>
      cost-of-living adjustment for 2027. It applies to Social Security benefits starting with the January
      2027 payments, and to Supplemental Security Income payments starting 31 December 2026. It is the
      largest adjustment since the 8.7% for 2023, and it is higher than the 2.8% that took effect in
      January 2026. Nobody has to apply for it; the increase is added automatically.</p>

""" + facts('The official 2027 figures', [
        ('3.6%', 'The 2027 COLA, announced 14 October 2026. The 2026 COLA was 2.8%.'),
        ('$2,095 &rarr; $2,170', 'The average retired-worker benefit before and after the increase, '
                                 'according to the Social Security Administration &mdash; about $75 a '
                                 'month.'),
        ('$192,300', 'The 2027 taxable maximum &mdash; the most earnings subject to Social Security tax. '
                     'It was $184,500 in 2026.'),
        ('$25,560', 'The 2027 earnings limit for people who have not reached full retirement age all year. '
                    'It was $24,480 in 2026.'),
        ('$67,920', 'The 2027 earnings limit in the year a person reaches full retirement age.'),
        ('31 December 2026', 'When the increased SSI payment is paid.'),
        ('Not yet announced', 'The 2027 Medicare Part B premium and deductible. CMS had not published them '
                              'as of 16 October 2026.'),
    ]) + """
      <h2>How the 3.6% was set</h2>

      <p>The COLA is not a policy choice or a negotiation. It comes from the Consumer Price Index for Urban
      Wage Earners and Clerical Workers &mdash; CPI-W &mdash; averaged across July, August and September,
      and compared with the same three-month average a year earlier. The percentage change, rounded to the
      nearest tenth of a percent, becomes the COLA. September&rsquo;s inflation data, released the same day
      as the announcement, is the last piece, which is why the number cannot be known before mid-October.</p>

      <p>The independent trackers this site cited in September, which were running the same public formula
      on two of the three months, had put the range at 3.5% to 3.6%. The official result landed at the top
      of it. That is the ordinary pattern: estimates narrow as the quarter fills in, and the final figure
      comes from the government&rsquo;s own calculation, not from any forecaster&rsquo;s.</p>

      <blockquote class="pull">
        <p>3.6% is the percentage. What lands in the account is a different number, and the difference is
        set by what is deducted before it arrives.</p>
      </blockquote>

""" + AD_INLINE + """
      <h2>What 3.6% means in dollars</h2>

      <p>The Social Security Administration puts the average retired-worker benefit at $2,095 before the
      increase and $2,170 after &mdash; roughly $75 a month. That is an average. A COLA is a percentage of
      the benefit a person already receives, not a flat amount added to every check alike, so the dollar
      figure scales with the benefit:</p>

      <p>A $1,500 benefit rises by about $54 a month. A $2,000 benefit rises by about $72. A $3,000 benefit
      rises by about $108. The arithmetic is the same for everyone; only the starting point differs.</p>

      <h2>The raise and the deposit are still different numbers</h2>

      <p>The Part B premium is usually deducted from Social Security before the payment arrives, and the
      2027 premium has not been announced. For comparison, the 2026 premium rose from $185.00 to $202.90
      &mdash; an increase of $17.90 that came out of the 2.8% COLA before it reached most people&rsquo;s
      accounts. A hold-harmless provision limits how much of a COLA the Part B increase can absorb for many
      people who have the premium withheld from their benefit, but it does not cover everyone: people newly
      enrolled in Medicare, higher earners paying the <a href="/irmaa">IRMAA surcharge</a>, and people whose
      premium is paid by Medicaid are among those it does not protect. The mechanics are laid out on
      <a href="/cola">the COLA page</a>.</p>

      <p>Until CMS publishes the 2027 premium and deductible, the net effect of the 3.6% cannot be
      calculated. Projections exist, but a projection is not an announcement, and this site does not treat
      one as the other.</p>

      <h2>The other numbers that moved</h2>

      <p><strong>The earnings limit.</strong> A person who claims benefits before full retirement age and
      keeps working has benefits withheld once earnings pass a yearly limit. For 2027 that limit is
      <strong>$25,560</strong> for anyone below full retirement age for the entire year: $1 in benefits is
      withheld for every $2 earned above it. In the calendar year a person reaches full retirement age, the
      limit is <strong>$67,920</strong> and the rate is $1 withheld for every $3 above it, counting only the
      earnings before the month full retirement age is reached. After that month there is no limit. Benefits
      withheld are not forfeited: the Social Security Administration recalculates the monthly benefit at
      full retirement age to credit the months that were withheld. The test does not apply to income
      from investments, pensions or retirement accounts &mdash; only to wages and self-employment income.</p>

      <p><strong>The taxable maximum.</strong> Social Security tax applies to earnings up to a cap, which
      rises to <strong>$192,300</strong> in 2027 from $184,500. At 6.2% each for the employee and the
      employer, the most either pays in Social Security tax on wages is $11,922.60. The Medicare tax has no
      wage cap and is unchanged. The cap matters mainly to people still working at higher earnings in
      their late fifties and sixties; for everyone else, it changes nothing.</p>

      <h2>When the notice and the first payment arrive</h2>

      <p>Social Security sends each beneficiary a notice of the new amount. People with a <em>my Social
      Security</em> account can read it in the Message Center beginning in late November, ahead of the
      paper copy; the 2027 Medicare premium for people who have it withheld is expected to appear there at
      the same time. People who do not use online notices receive a one-page mailed notice in December.
      The first payment at the new amount comes with the January 2027 benefit. For most people, that is the
      Wednesday tied to their birthday: 13 January for birthdays on the 1st through the 10th, 20 January
      for the 11th through the 20th, and 27 January for the 21st through the 31st. SSI recipients are paid
      the increase on 31 December.</p>

      <h2>What&rsquo;s worth checking now</h2>

""" + check([
        'The official 2027 COLA is <strong>3.6%</strong>, announced 14 October 2026 by the Social '
        'Security Administration. Any earlier figure &mdash; including the 3.5%&ndash;3.6% estimates '
        'published in September &mdash; has been superseded.',
        'A COLA percentage is not the same as what lands in an account. The <strong>2027 Part B '
        'premium</strong> is announced separately and, for most people who have it withheld, comes out '
        'of the increase first &mdash; see <a href="/cola">the COLA page</a>.',
        'The <strong>earnings limit</strong> for people under full retirement age rose to $25,560, and to '
        '$67,920 in the year full retirement age is reached. The limit applies to wages and '
        'self-employment income only.',
        'The <strong>taxable maximum</strong> rose to $192,300. It affects only earnings above the 2026 '
        'cap of $184,500.',
        'The new benefit amount is sent to each beneficiary in a notice from the Social Security '
        'Administration; that notice, not a news estimate, is the number that governs the January '
        'payment.',
    ]) + """
      <p>The estimate season is over, and the useful thing about it ending is that the arguments about
      which forecaster was closest stop mattering. The percentage is set. What remains open is the part
      the Social Security Administration does not decide: what Medicare charges for 2027, and how much of
      the 3.6% survives the deduction. That number arrives from CMS, and until it does, the honest figure
      for the net raise is that there isn&rsquo;t one yet.</p>
""",
    'sources': [
        ('Social Security Administration &mdash; Social Security Announces 3.6 Percent Benefit Increase for 2027',
         'https://www.ssa.gov/blog/en/posts/2026-10-14.html'),
        ('Social Security Administration &mdash; 2027 Cost-of-Living Adjustment fact sheet',
         'https://www.ssa.gov/news/en/cola/factsheets/2027.html'),
        ('Journal of Accountancy &mdash; Social Security wage base and COLA announced for 2027',
         'https://www.journalofaccountancy.com/news/2026/oct/social-security-wage-base-and-cola-announced-for-2027/'),
        ('Axios &mdash; Social Security recipients will see rise in monthly payments next year',
         'https://www.axios.com/2026/10/14/social-security-cola-inflation'),
        ('Kiplinger &mdash; 2027 Social Security COLA is 3.6%: What You Need to Know',
         'https://www.kiplinger.com/retirement/social-security/2027-social-security-cola-is-3-6-percent'),
        ('Bureau of Labor Statistics &mdash; The use of the CPI in Social Security COLAs',
         'https://www.bls.gov/opub/btn/archive/the-use-of-the-cpi-in-social-security-cost-of-living-adjustments-colas.pdf'),
    ],
    'next': {'slug': 'cola',
             'title': 'The COLA: why a raise doesn&rsquo;t feel like one',
             'blurb': 'What happens to a COLA once it&rsquo;s official and Medicare&rsquo;s premium takes '
                      'its share &mdash; the part that applies whatever the percentage turns out to be.'},
}

# ----------------------------------------------------------- QR parking scam
ARTICLES14['qr-parking-scam'] = {
    'title': 'The Parking Meter QR Code Might Not Be the Real One &mdash; The Second Half Guide',
    'eyebrow': 'Protecting yourself',
    'h1': 'The parking meter QR code might not be the real one',
    'dek': 'The FTC issued a fresh consumer alert on a simple trick: a sticker with a fake QR code, placed '
           'directly over the real one, at a meter you have no reason to distrust.',
    'meta': '5 minute read &middot; Verified against a September 2026 FTC consumer alert',
    'checked': CHECKED14,
    'body': """      <p>On September 3, 2026, the Federal Trade Commission published a consumer alert about a scam that
      needs nothing more sophisticated than a sticker and a printer. Scammers place a QR code of their own
      directly over the legitimate one on a parking meter, a lot payment sign, or a toll notice &mdash; and
      wait for someone to scan it.</p>

      <p>It works because nothing about the meter itself looks wrong. The post is real, the sign is real,
      the parking spot is real. The only thing that&rsquo;s been touched is a two-inch square of paper,
      often printed to match the size, shape and color of the legitimate code closely enough that it
      registers as normal on a quick glance.</p>

      <p>Most fraud aimed at this age group runs on urgency &mdash; a caller who needs an answer in the
      next five minutes, before there&rsquo;s time to think it through. This one is different. There&rsquo;s
      no caller, no deadline, no one on the phone at all. It just waits at a meter for whoever happens to
      need to park, which is precisely what makes it easy to walk past without a second thought, and why it
      doesn&rsquo;t announce itself the way a threatening phone call does.</p>

""" + facts('What the FTC is warning about', [
        ('September 3, 2026', 'Date of the FTC&rsquo;s consumer alert on this specific pattern.'),
        ('Where it shows up', 'Parking meters and lot payment signs most often; the FTC and other agencies '
                              'have also flagged the same trick on toll notices.'),
        ('How it works', 'A sticker bearing a scammer&rsquo;s own QR code is placed over the legitimate '
                         'one, redirecting your payment and your card details to them instead of the '
                         'parking operator.'),
        ('What you can lose', 'Per the FTC: your card number, your personal information, or both &mdash; '
                              'not just the price of parking.'),
        ('The tell', 'A sticker sitting slightly proud of the sign underneath it, or a link that previews '
                     'somewhere that doesn&rsquo;t match the parking operator&rsquo;s name.'),
        ('Where to report it', 'ReportFraud.ftc.gov, and the parking operator or property manager if the '
                               'meter belongs to a lot or garage rather than the city.'),
    ]) + """
      <h2>Why a QR code is an easier con than a fake website</h2>

      <p>A phishing email or a spoofed website at least gives you a full address to look at before you
      commit to anything. A QR code hides its destination until after you&rsquo;ve already scanned it &mdash;
      most phones show a link preview, but plenty of people tap through without reading it, especially when
      they&rsquo;re standing in a parking lot trying not to be late for something.</p>

      <blockquote class="pull">
        <p>Nothing about the meter has to be fake for this to work. Only the two-inch sticker on top of it
        does.</p>
      </blockquote>

""" + AD_INLINE + """
      <h2>Where this is showing up</h2>

      <p>Parking meters and lot payment kiosks are the pattern the FTC named specifically. QR-based payment
      has become familiar enough at meters like these that most people no longer think twice about scanning
      one &mdash; and that familiarity is exactly what makes a tampered sticker easy to miss. It looks like
      every other QR code you&rsquo;ve paid with this year.</p>

      <p>It is also not an isolated trick. Two related versions have drawn their own federal warnings in
      the past year. The FBI&rsquo;s Internet Crime Complaint Center warned in mid-2025 about unsolicited
      packages arriving with a QR code inside, urging the recipient to scan it to identify a mystery
      delivery &mdash; scanning instead leads to a data-harvesting site or a malicious download. And the
      FTC separately warned in April 2026 about text messages impersonating a state court or toll agency,
      claiming a traffic or toll violation and including a QR code to &ldquo;pay the fine&rdquo;
      immediately. All three &mdash; the parking sticker, the mystery package, and the toll text &mdash;
      share the same mechanic: a QR code hides its destination, and something ordinary-looking lends it
      borrowed credibility.</p>

      <h2>The alternative that sidesteps the whole problem</h2>

      <p>A tampered sticker only works if you use it. Most parking meters and lots that offer QR payment
      also print the operator&rsquo;s official app name or a phone number directly on the same sign.
      Neither is immune to tampering in theory, but a scammer would need to cover far more of the sign to
      fake both, rather than the one small sticker over the QR code &mdash; using an independently verified
      official app or phone number, or looking the operator up yourself rather than trusting anything
      printed on the sign, avoids relying on the QR code specifically. Where the meter itself takes a card
      or coins directly, that route avoids the QR code entirely. None of this requires distrusting parking
      technology generally; it just means the QR code on the sign is one option among several, not the only
      way to pay, and it&rsquo;s worth defaulting to one of the others whenever they&rsquo;re available.</p>

      <h2>What actually protects you</h2>

""" + check([
        'Before scanning, <strong>look at the sticker itself</strong>. A code that sits slightly raised, '
        'crooked, or on a different material than the sign around it is the clearest sign of tampering.',
        'Most phone cameras show a <strong>link preview</strong> before opening it. Read the actual web '
        'address &mdash; check for misspellings or a domain that doesn&rsquo;t match the parking operator '
        '&mdash; before tapping through.',
        'If a lot has an <strong>official app or a phone number</strong> printed on the sign, use that '
        'instead of the QR code. It is not vulnerable to a sticker.',
        'If you already scanned and paid through a code that turned out to be fake, contact your '
        '<strong>card issuer</strong> immediately to dispute the charge and watch for further ones.',
        'Report it at <strong>ReportFraud.ftc.gov</strong> &mdash; and if the meter or lot has an operator '
        'or property manager, tell them too, since the sticker is still there for the next person until '
        'someone removes it.',
    ]) + """
      <p>This one doesn&rsquo;t require falling for a story or a caller pretending to be someone else. It
      only requires trusting a piece of paper that had no business being there &mdash; which is exactly why
      a five-second look at the sticker, before the tap, is the entire defense. And it&rsquo;s a defense
      that costs nothing and takes no longer than scanning the code would have in the first place: glance
      at the sticker, glance at the link preview, and only then tap through.</p>
""",
    'sources': [
        ('FTC Consumer Advice &mdash; See a QR code parked somewhere? Don&rsquo;t scan it&hellip;yet!',
         'https://consumer.ftc.gov/consumer-alerts/2026/09/see-qr-code-parked-somewhere-dont-scan-ityet'),
        ('Better Business Bureau &mdash; Double check that QR code before you pay for parking',
         'https://www.bbb.org/article/scams/28996-bbb-scam-alert-double-check-that-qr-code-before-you-pay-for-parking'),
        ('The Post and Courier &mdash; Your next scan could be a scam: FBI, FTC warn on QR codes',
         'https://www.postandcourier.com/business/scams-qr-codes-parking-packages-fbi/article_88d1d27b-492c-46b4-9b54-5727e6909841.html'),
        ('FBI &mdash; Unsolicited Packages Containing QR Codes Used to Initiate Fraud Schemes',
         'https://www.fbi.gov/investigate/cyber/alerts/2025/unsolicited-packages-containing-qr-codes-used-to-initiate-fraud-schemes'),
        ('FTC Consumer Advice &mdash; That text about a traffic violation is probably a scam',
         'https://consumer.ftc.gov/consumer-alerts/2026/04/text-about-traffic-violation-probably-scam'),
    ],
    'next': {'slug': 'five-minute-rule',
             'title': 'The five-minute rule',
             'blurb': 'The urgency tell behind most phone and text scams &mdash; a different mechanism '
                      'than this one, worth knowing alongside it.'},
}
