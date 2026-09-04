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
    'checked': CHECKED14,
    'body': """      <p>Sometime this month, an envelope from your Medicare Advantage or Part D plan will arrive that
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
      out-of-pocket cap on covered drugs rises to <strong>$2,400</strong>, up from $2,100. The deductible
      that counts toward it rises to <strong>$700</strong>, up from $615. Both figures will show up
      somewhere in this year&rsquo;s ANOC for anyone with Part D coverage, and both are large enough to
      change what a year of prescriptions actually costs.</p>

      <blockquote class="pull">
        <p>The number at the top of the letter is usually the premium. The number that actually changes
        what you pay over a year is usually further down &mdash; in the drug formulary, not the headline.</p>
      </blockquote>

""" + AD_INLINE + """
      <h2>Where the real information is buried</h2>

      <p>Plans lead with the premium because it is the easiest number to compare and the least likely to
      alarm anyone. It is also, for most people, not where the money actually moves.</p>

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

      <p>If nothing arrives by early October, that&rsquo;s worth following up on rather than assuming your
      plan has no changes this year. CMS requires plans to get it to you by September 30; call your plan
      directly to request a copy, and if that doesn&rsquo;t resolve it, <strong>1-800-MEDICARE</strong> can
      help.</p>

      <h2>Advantage plans and standalone drug plans get different letters</h2>

      <p>What&rsquo;s inside the envelope depends on what kind of plan you have. A <strong>standalone Part
      D</strong> plan &mdash; drug coverage only, paired with Original Medicare &mdash; sends an ANOC that&rsquo;s
      almost entirely about drug costs: premium, deductible, formulary and pharmacy network. A
      <strong>Medicare Advantage</strong> plan bundles medical and drug coverage together, so its ANOC
      covers more ground: the same drug-cost items, plus changes to the provider network, referral
      requirements, and the plan&rsquo;s service area. Losing a doctor from the network is exactly the kind
      of change that shows up in an Advantage ANOC and never appears at all in a standalone Part D one
      &mdash; another reason the letter is worth reading in full rather than skimmed for the premium line.</p>

      <h2>What to actually do with it</h2>

""" + check([
        'Find the <strong>formulary and drug-tier section</strong> and check every prescription you '
        'currently take against it, not just the ones you remember being expensive.',
        'Check whether your <strong>preferred pharmacy</strong> is still preferred. The same drug at the '
        'same counter can cost a different amount if that status changed.',
        'Note the new <strong>2027 out-of-pocket cap ($2,400) and deductible ($700)</strong> if you have '
        'Part D coverage &mdash; both are higher than this year, regardless of which plan you keep.',
        'If anything in the letter concerns you, the window to act is <strong>October 15 to December '
        '7</strong>. Outside that window, this year&rsquo;s plan carries into next year automatically.',
        'The ANOC tells you what your plan is changing to. It does not tell you what a better-fit plan '
        'would cost &mdash; that comparison lives at the Medicare Plan Finder, separately.',
        'If you have an Advantage plan, check the <strong>network and referral</strong> sections too, not '
        'just drug costs &mdash; a doctor leaving the network is exactly the kind of change this letter '
        'exists to disclose.',
    ]) + """
      <p>Nobody enjoys reading insurance mail closely. This is the one piece of it each year built entirely
      out of things that are about to be true whether you read it or not &mdash; which is the whole case for
      reading it before October 15, rather than after.</p>
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
    'title': 'The 2027 Social Security COLA Isn’t Official Yet &mdash; The Second Half Guide',
    'eyebrow': 'Facts &amp; thresholds',
    'h1': 'The 2027 Social Security COLA isn&rsquo;t official yet',
    'dek': 'Headlines this summer have already put a number on next year&rsquo;s raise. Social Security '
           'hasn&rsquo;t announced one &mdash; and won&rsquo;t until mid-October, once data that doesn&rsquo;t '
           'exist yet is finished.',
    'meta': '5 minute read &middot; Verified against BLS/CRS methodology and independent COLA trackers',
    'checked': CHECKED14,
    'body': """      <p>By late summer, several independent trackers had already put a number on the 2027 Social
      Security cost-of-living adjustment &mdash; and some coverage repeated those numbers as if the decision
      had been made. It hasn&rsquo;t. The Social Security Administration has not announced a 2027 COLA, and
      structurally cannot, until data that doesn&rsquo;t exist yet has been collected.</p>

""" + facts('Where things actually stand', [
        ('2.8%', 'The <em>official</em>, already-locked-in 2026 COLA, announced in October 2025 and in '
                 'effect since January 2026.'),
        ('3.5% &ndash; 3.7%', 'The range of independent 2027 <em>estimates</em> circulating as of late '
                              'summer 2026, from three separate trackers &mdash; not from Social '
                              'Security.'),
        ('3', 'The number of months of data that actually decide it: July, August and September CPI-W, '
             'averaged and compared to the same three months a year earlier.'),
        ('14 October 2026', 'The date the Social Security Administration is expected to announce the '
                            'official 2027 COLA, after the Bureau of Labor Statistics releases September '
                            'inflation data.'),
        ('$0', 'How much of the estimate range above is a government figure, until that date.'),
    ]) + """
      <h2>Where the estimates come from</h2>

      <p>Three groups have published 2027 COLA forecasts using July inflation data: The Senior Citizens
      League estimated <strong>3.6%</strong>, AARP projected <strong>3.5%</strong>, and independent analyst
      Mary Johnson put it at <strong>3.7%</strong>. All three are running the same public CPI-W formula the
      government itself will eventually use &mdash; they are not guessing randomly. But all three are
      working from two-thirds of the data the real number requires. August and September inflation figures
      can still move the result in either direction before the government&rsquo;s own number is calculated.</p>

      <blockquote class="pull">
        <p>None of these figures are Social Security&rsquo;s number. They are outside groups running the
        government&rsquo;s own formula on data that isn&rsquo;t finished yet.</p>
      </blockquote>

""" + AD_INLINE + """
      <h2>Why three trackers publish three different numbers</h2>

      <p>All three groups are running the same public formula on the same underlying government data, so
      the spread between 3.5% and 3.7% isn&rsquo;t disagreement about the rule &mdash; it&rsquo;s a
      difference in timing and rounding as each one updated its own estimate through the summer. A forecast
      published right after July&rsquo;s CPI-W release reflects one month of real data and two months of
      assumption. The same tracker&rsquo;s estimate a few weeks later, after August&rsquo;s release, is
      built on two-thirds real data instead of one-third &mdash; and estimates published this way generally
      narrow, rather than widen, as more of the actual quarter comes in. That narrowing stops entirely once
      September&rsquo;s figure lands and the government runs the calculation itself.</p>

      <h2>The formula, briefly</h2>

      <p>The COLA is not a policy choice or a negotiation. It comes from the Consumer Price Index for Urban
      Wage Earners and Clerical Workers &mdash; CPI-W &mdash; averaged across July, August and September,
      and compared to the same three-month average from the prior year the formula last used. The
      percentage change, rounded to the nearest tenth of a percent, becomes the COLA. It is the identical
      process that produced 2.8% for 2026, run again on next year&rsquo;s data.</p>

      <p>If the range holds, a COLA in the mid-3s would be the largest increase since 2023 &mdash; but
      &ldquo;if it holds&rdquo; is doing real work in that sentence. August and September data haven&rsquo;t
      been fully counted yet, and the whole point of the formula is that nobody, including the trackers
      publishing estimates, gets to shortcut that.</p>

      <p>To put the range in dollars rather than percent: on today&rsquo;s average retired-worker benefit
      of about $2,071 a month (itself the result of the 2026 COLA), a 3.5% adjustment works out to roughly
      $72 a month, and 3.7% to roughly $77. That arithmetic is simple and it is also entirely provisional
      &mdash; it applies whichever estimate turns out closest, and none of them is the number Social
      Security will actually use. A smaller benefit sees a smaller dollar increase at the same percentage,
      and a larger one sees more &mdash; the COLA is a percentage of what you already receive, not a flat
      amount added to every check alike.</p>

      <h2>The raise and the deposit are not the same number</h2>

      <p>Whatever the 2027 COLA turns out to be, it will not be the amount that shows up in the monthly
      deposit. That happened with 2026&rsquo;s already-official 2.8%: it added about $56 to the average
      benefit, but the Medicare Part B premium rose from $185.00 to $202.90 over the same period &mdash; an
      increase of $17.90, deducted automatically before the payment arrives. Net effect: about $38 of the
      announced $56 actually landed. A <a href="/cola">hold-harmless</a> rule keeps the Part B increase
      from ever exceeding the COLA in dollar terms, so the payment shouldn&rsquo;t go backward &mdash; but it
      routinely arrives smaller than the headline percentage implies, and 2027&rsquo;s Part B premium hasn&rsquo;t
      been announced yet either.</p>

      <h2>What&rsquo;s worth doing while you wait</h2>

""" + check([
        'Treat every number published before <strong>14 October 2026</strong> as an estimate, however '
        'confidently it&rsquo;s stated &mdash; including the ones in this article.',
        'The real number, when it lands, comes directly from the <strong>Social Security '
        'Administration</strong>, not from a tracker or a news estimate.',
        'A COLA percentage is not the same as what actually lands in your account. Part B premiums for '
        '2027 are announced separately, and typically absorb part of any increase before it arrives '
        '&mdash; see the mechanics on <a href="/cola">the COLA page</a> for how that worked in 2026.',
        'The three months that decide it &mdash; July, August, September &mdash; are the only ones that '
        'matter. Inflation news from earlier in the year, however dramatic, already happened before the '
        'clock started.',
        'Independent trackers have been revising their 2027 estimates downward over the summer as '
        'inflation cooled, converging toward roughly <strong>3.5%&ndash;3.7%</strong> by August &mdash; a '
        'range that only closes entirely once September&rsquo;s figure is in.',
    ]) + """
      <p>The estimate season exists because people want to plan, and there is nothing wrong with knowing
      the range. The distinction worth holding onto is which number is a forecast and which one is Social
      Security&rsquo;s &mdash; and until mid-October, there is only one of those. When the real figure
      arrives, it will come from the Social Security Administration directly, not from any of the trackers
      quoted above, however close their guess turns out to be.</p>
""",
    'sources': [
        ('Congressional Research Service &mdash; Social Security: Cost-of-Living Adjustments',
         'https://www.congress.gov/crs-product/94-803'),
        ('Bureau of Labor Statistics &mdash; The use of the CPI in Social Security COLAs',
         'https://www.bls.gov/opub/btn/archive/the-use-of-the-cpi-in-social-security-cost-of-living-adjustments-colas.pdf'),
        ('CNBC &mdash; Social Security COLA estimates for 2027 fall as inflation moderates',
         'https://www.cnbc.com/2026/08/12/social-security-cola-estimates-for-2027-fall-as-inflation-moderates.html'),
        ('The Senior Citizens League &mdash; COLA Watch',
         'https://seniorsleague.org/cola-watch/'),
        ('AARP &mdash; Social Security COLA Preview: Will 2027 Benefits Go Up?',
         'https://www.aarp.org/social-security/cola-2027-increase-estimate/'),
    ],
    'next': {'slug': 'cola',
             'title': 'The COLA: why a raise doesn&rsquo;t feel like one',
             'blurb': 'What happens to a COLA once it&rsquo;s official and Medicare&rsquo;s premium takes '
                      'its share &mdash; the part that applies whatever October&rsquo;s number turns out '
                      'to be.'},
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
        ('What you can lose', 'Your card number and personal information, and in some versions a '
                              'recurring charge you did not agree to &mdash; not just the price of '
                              'parking.'),
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

      <p>Parking meters and lot payment kiosks are the pattern the FTC named specifically, and QR-based
      payment has become common enough at airports, downtown lots, hospitals and event venues that most
      people no longer think twice about scanning one. That familiarity is exactly what makes a tampered
      sticker easy to miss &mdash; it looks like every other QR code you&rsquo;ve paid with this year.</p>

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
      also print the operator&rsquo;s official app name or a phone number directly on the same sign &mdash;
      neither of which a scammer can intercept with a piece of paper. Where the meter itself takes a card or
      coins directly, that route avoids the QR code entirely. None of this requires distrusting parking
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
