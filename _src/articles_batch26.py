#!/usr/bin/env python3
"""Twenty-sixth batch: four travel and leisure pieces from 1 November 2026 --
the TSA ConfirmID $45 fee (in effect since 1 February), the total solar eclipse
of 2 August 2027 (the first reachable total eclipse for most readers in years),
the UK's Electronic Travel Authorisation for Americans, and what to check about
SilverSneakers and Medicare gym benefits before Annual Enrollment closes.

cms.gov, tsa.gov and gov.uk were not read directly: Verified per CLAUDE.md
section 2 by agreement across independent reporting that traces to the agency.
Deliberately omitted because only one source gave it: how long TSA accepts an
expired ID, the date UK ETAs became mandatory for Americans, an airside-transit
exemption at Heathrow, any individual plan's 2027 fitness benefit beyond Aetna,
Medicare Advantage fitness cuts reported for single plans, eclipse tour prices,
and Egypt's entry rules."""

from build_articles import facts, check, AD_INLINE

ARTICLES26 = {}

CHECKED26 = '1 November 2026'

# ------------------------------------------------------------- TSA ConfirmID
ARTICLES26['tsa-confirmid-fee'] = {
    'title': 'The $45 TSA ID Fee: Who Pays It and Who Does Not &mdash; The Second Half Guide',
    'eyebrow': 'Facts &amp; thresholds',
    'h1': 'The $45 airport ID fee: who pays it, and who does not',
    'dek': 'Since 1 February, a domestic flyer without REAL ID or another accepted ID can pay $45 for '
           'TSA&rsquo;s backup identity check. It is optional, it does not guarantee you board, and it '
           'is paid in one place only.',
    'meta': '5 minute read &middot; Checked against TSA&rsquo;s ConfirmID announcements and reporting',
    'checked': CHECKED26,
    'body': """      <p>Two things happened at American airports in the last eighteen months, and they are easy to
      blur together. On 7 May 2025 the REAL ID rule began to be fully enforced: a standard driver&rsquo;s
      license without the star no longer works as identification at a TSA checkpoint. Then on
      1 February 2026 TSA added a fee to the end of that story. This page is about the fee.</p>

      <p>It will not touch most readers. TSA&rsquo;s early numbers, released 5 February, said between 95%
      and 99% of travelers were already showing a REAL ID or another accepted document. But the people it
      does touch tend to find out at the worst moment, which is why the details are worth having first.</p>

""" + facts('TSA ConfirmID, in numbers', [
        ('1 February 2026', 'When the ConfirmID fee began.'),
        ('$45', 'The fee for travelers 18 and older who cannot present REAL ID or another accepted '
                'document. Using ConfirmID is optional.'),
        ('10 days', 'How long one payment is valid, counted from the first travel date on the receipt.'),
        ('Pay.gov', 'The only place the fee is paid, reached through TSA.gov/ConfirmID.'),
        ('No guarantee', 'TSA says paying does not guarantee that your identity will be verified or that '
                         'you will be allowed through the checkpoint.'),
        ('7 May 2025', 'When full REAL ID enforcement began at TSA checkpoints.'),
        ('Under 18', 'Children are not required to show identification for domestic flights.'),
    ]) + """
      <h2>What ConfirmID is</h2>

      <p>It is a fallback, not a new requirement. A traveler who arrives at security without a REAL ID
      or another accepted form of identification can pay the $45 fee in advance on Pay.gov, show the
      emailed receipt at the checkpoint, and go through an alternative process to verify who they are.
      TSA has said that process may take longer, and that passengers who do not present an accepted ID
      should expect increased wait times. The payment covers a 10-day window starting from the first
      travel date on the receipt. A traveler who passes through another checkpoint after those ten days,
      still without an accepted ID, would pay again.</p>

      <p>Paying does not buy certainty. TSA&rsquo;s own wording is that the fee does not guarantee
      successful verification. A traveler whose identity cannot be confirmed can still be turned away at
      the checkpoint, and the fee is reported to be nonrefundable. For anyone with a flight to catch,
      that is the sentence that matters.</p>

      <h2>What is accepted without the fee</h2>

      <p>A REAL ID-compliant license or identification card, which carries a star marking, is the common
      one. But a U.S. passport or passport card works without any fee, as do the DHS trusted-traveler
      cards (Global Entry, NEXUS, SENTRI and FAST), a state-issued Enhanced Driver&rsquo;s License, and
      military identification, including cards issued to dependents. TSA keeps the complete list on its
      identification page, and it is the list to check before a flight, because it can change.</p>

      <p>That has a practical consequence for the readers of this site. A passport card, which many
      people keep for a cruise, is an accepted document for a domestic flight. So is a Global Entry card,
      which is one more reason Global Entry is the better buy, as <a href="/airport-security">the airport
      security page</a> works out. And a temporary paper license, issued while a new one is in the mail,
      is not an accepted document on its own, a gap that catches people who renewed shortly before a trip.</p>

      <blockquote class="pull">
        <p>The fee is not the cost of flying without ID. It is the cost of asking TSA to try to verify you
        without it.</p>
      </blockquote>

""" + AD_INLINE + """
      <h2>Who actually ends up paying it</h2>

      <p>The groups are predictable. People whose licenses were renewed before the star was added and who
      never went back to the motor vehicles office. People who have not flown since 2019 and carry an
      older card. People who have moved states and are carrying a license that was never replaced. And
      people with a perfectly good license who simply did not realize it lacked the star. None of this is
      a judgment about the traveler. It is a gap between a renewal date and a federal deadline.</p>

      <p>The rule underneath is unchanged and simple: for a domestic flight, an adult needs one accepted
      form of identification, not two. A person who holds a valid passport already has it, and the fee
      is irrelevant to them.</p>

      <h2>Where scammers fit in</h2>

      <p>A federal fee with a payment page and a deadline is exactly the shape a scam takes. The official
      path is narrow: TSA says the fee can be paid only through Pay.gov, reached from TSA.gov/ConfirmID,
      and that the payment is followed by a receipt emailed from Pay.gov. A text, an email or a search
      ad offering to &ldquo;process&rdquo; the TSA fee for a charge is not that path. This is the same
      pattern covered on <a href="/five-minute-rule">the five-minute rule page</a>: an official-looking
      page, a fee and a reason to hurry.</p>

      <h2>What TSA has not said</h2>

      <p>The fee was introduced in a TSA announcement in December 2025 and described by TSA on its own
      site. The agency has not published, in the material available here, a count of how many travelers
      have used ConfirmID or how many of them were cleared. The figure it has given is the share of
      travelers who arrive with a compliant ID, which is the 95% to 99% above. Anything more specific
      about outcomes would be a guess, and this page does not make one.</p>

      <p>Other airport rules that changed recently are on
      <a href="/airport-security">the airport security page</a>, and the help available to travelers who
      need it is on <a href="/airport-help">the airport help page</a>. Passport rules that turn people away
      at borders, which are a different problem, are on
      <a href="/passport-traps">the passport page</a>.</p>

      <h2>What&rsquo;s worth keeping in mind</h2>

""" + check([
        'Since <strong>1 February 2026</strong>, travelers 18 and older without REAL ID or another accepted '
        'ID can pay <strong>$45</strong> to use TSA ConfirmID. It is optional.',
        'The fee is paid <strong>only on Pay.gov</strong>, through TSA.gov/ConfirmID, and covers 10 days.',
        'Paying does <strong>not guarantee</strong> verification or boarding.',
        'A <strong>passport, passport card, Global Entry card</strong> or Enhanced Driver&rsquo;s License is '
        'accepted without the fee. A temporary paper license is not.',
        'Children under 18 do not need ID for domestic flights.',
    ]) + """
      <p>For almost everyone, the answer is to bring something on TSA&rsquo;s accepted list. The fee
      exists for the few travelers in a hundred who did not.</p>
""",
    'sources': [
        ('TSA &mdash; TSA ConfirmID', 'https://www.tsa.gov/tsaconfirm-id'),
        ('TSA &mdash; TSA introduces new $45 fee option for travelers without REAL ID starting February 1 '
         '(1 December 2025)',
         'https://www.tsa.gov/news/press/releases/2025/12/01/tsa-introduces-new-45-fee-option-for-travelers-without-real-id'),
        ('TSA &mdash; TSA successfully rolls out TSA ConfirmID (5 February 2026)',
         'https://www.tsa.gov/news/press/releases/2026/02/05/tsa-successfully-rolls-out-tsa-confirmid-0'),
        ('TSA &mdash; TSA begins REAL ID full enforcement on May 7',
         'https://www.tsa.gov/news/press/releases/2025/04/11/tsa-begins-real-id-full-enforcement-may-7'),
        ('TSA &mdash; REAL ID frequently asked questions', 'https://www.tsa.gov/realid/realid-faqs'),
        ('CNBC &mdash; Real ID fee: TSA to charge non-compliant travelers starting Feb. 1',
         'https://www.cnbc.com/2026/01/31/real-id-fee-tsa.html'),
    ],
    'next': {'slug': 'airport-security',
             'title': 'Airport security after 75, and what PreCheck still buys',
             'blurb': 'The shoes-off rule is gone. What is left of the perk, and the Global Entry '
                      'arithmetic.'},
}

# ------------------------------------------------------------- eclipse 2027
ARTICLES26['eclipse-2027'] = {
    'title': 'The 2 August 2027 Total Solar Eclipse: Path and Duration &mdash; The Second Half Guide',
    'eyebrow': 'Facts &amp; thresholds',
    'h1': 'The 2 August 2027 total solar eclipse: where it crosses, how long it lasts',
    'dek': 'Southern Spain gets a few minutes of darkness at midday. Egypt gets more than six. For a reader '
           'in the lower 48, the next total eclipse at home is in 2044.',
    'meta': '6 minute read &middot; Checked against Spain&rsquo;s IGN, NASA and eclipse-guide reporting',
    'checked': CHECKED26,
    'body': """      <p>A total solar eclipse is the rare travel event with a fixed date, a fixed place and no
      second chance. The next one that Americans can reasonably plan around is on
      <strong>2 August 2027</strong>. It crosses the Atlantic, the Strait of Gibraltar, southern Spain
      and North Africa, and ends in Egypt. Tour operators are already selling trips, which is the reason
      this page is worth having nine months ahead of the date and not nine days.</p>

      <p>It is also a page about a calendar, not a recommendation. What follows is the geometry, the
      durations and the logistics reported so far, and what the sources do not agree on.</p>

""" + facts('The 2 August 2027 eclipse, in numbers', [
        ('2 August 2027', 'The date of the total solar eclipse.'),
        ('About 6 minutes 23 seconds', 'The longest totality, near Luxor in Egypt&rsquo;s Nile Valley.'),
        ('About 4 minutes 48 seconds', 'Totality at Ceuta, the longest in Spanish territory, per Spain&rsquo;s '
                                       'National Geographic Institute (IGN).'),
        ('About 2 minutes 54 seconds', 'Totality at Cádiz, per IGN. Another guide gives 2 minutes 56 '
                                       'seconds.'),
        ('About 1 minute 48 seconds', 'Totality at Málaga, per IGN.'),
        ('About 10:45', 'Local time totality begins along the Spanish coast, in the morning.'),
        ('23 August 2044', 'The next total eclipse visible from the contiguous United States, per NASA.'),
    ]) + """
      <h2>Where the path goes</h2>

      <p>In Spain, totality covers the autonomous cities of Ceuta and Melilla, almost all of Cádiz
      province, much of Málaga province, and the southernmost parts of Granada and Almería. Gibraltar is
      in the path. The reason these numbers differ so much within a few hundred miles is geometry: the
      shadow&rsquo;s center line crosses the coast at a different angle than its edges, and a place near the
      edge gets a shorter eclipse than a place near the middle. Standing in the wrong town can cost minutes.</p>

      <p>Egypt is the other end of the logic. The longest totality on land is near Luxor, at about six
      minutes and twenty-three seconds. Cairo and the pyramids at Giza are not on the path. They would see
      a deep partial eclipse of about 95%, which is dramatic and is not totality. A traveler who books a
      trip around Cairo to see the eclipse has booked the wrong city.</p>

      <blockquote class="pull">
        <p>Ninety-five percent of the Sun covered is a good afternoon. One hundred percent is a different
        experience, and it begins and ends at the edge of the path.</p>
      </blockquote>

""" + AD_INLINE + """
      <h2>Spain or Egypt: what the reporting says</h2>

      <p>The guides agree on the trade. Egypt offers longer totality and much lower risk of cloud in
      August. Spain is easier to reach and to move around in, but the Atlantic coast has a higher chance
      of cloud, and a narrow strip of the south coast is expected to be crowded. One guide expects
      heavy road congestion and says parking will be a significant problem. A few minutes of totality
      is a short window to leave to chance at the end of a traffic jam.</p>

      <p>Reported durations differ by a few seconds between sources, which is normal for a
      path-edge calculation and not an error. They are close enough to compare cities, and not close
      enough to plan to the second. One guide claims a mainland Spanish town gets nearly the maximum
      Spanish duration, which disagrees with the IGN figures above, so this page does not repeat it.</p>

      <h2>The part about eyes</h2>

      <p>Looking at the Sun is dangerous except for one moment. The widely repeated guidance in the
      eclipse guides is that eclipse glasses meeting the <strong>ISO 12312-2</strong> standard must be
      worn during every partial phase, before and after totality, and may be removed only during the brief
      total phase, inside the path of totality, and put back on as soon as the first bright sliver of Sun
      returns. Ordinary sunglasses are not a substitute, and the glasses do not protect a camera, binoculars
      or a telescope. Checking the marking on the glasses, and not the packaging, is the point.
      The agency guidance (NASA, the American Astronomical Society) is worth reading directly before the
      date, because most of the pages that repeat it are selling glasses.</p>

      <h2>Why 2044 matters to a reader in their sixties</h2>

      <p>The last total eclipse across the lower 48 was on 8 April 2024. According to NASA, the next one
      that can be seen from the contiguous United States is on 23 August 2044, with a path through the
      northern Plains and the Rockies. Alaska gets a total eclipse in March 2033. Someone who is 62 today
      will be 80 in 2044. That is not a reason to book anything. It is a fact about the calendar that the
      travel pages tend to leave out, and it explains why a trip to Spain or Egypt in 2027 is being
      treated as the one that counts.</p>

      <h2>What to settle early</h2>

      <p>The items that cost money to get wrong are the ones that are fixed in time. The date is fixed, which
      is why tour operators have been offering itineraries for some time (for example, an Egypt program
      in late July and early August 2027), and why a booking made late has fewer choices. Travel insurance matters more for a trip with a one-day purpose, and the
      <a href="/travel-insurance">travel insurance page</a> covers what the policies actually do.
      Entry rules are a separate matter: Spain is part of the Schengen area, and the EU&rsquo;s new
      authorization is covered on <a href="/etias">the ETIAS page</a>. Egypt&rsquo;s entry rules were not
      checked for this page and should be confirmed with the State Department before booking.</p>

      <p>For readers building a larger trip around it, <a href="/the-big-trip">the big trip page</a> and
      <a href="/go-go-years">the go-go years page</a> are the wider planning pieces.</p>

      <h2>What&rsquo;s worth keeping in mind</h2>

""" + check([
        'The total solar eclipse is on <strong>2 August 2027</strong>, crossing southern Spain and North '
        'Africa and ending in Egypt.',
        'Longest totality: about <strong>6 minutes 23 seconds</strong> near Luxor. In Spain: about '
        '4 minutes 48 seconds at Ceuta, 2 minutes 54 seconds at Cádiz, 1 minute 48 seconds at Málaga.',
        '<strong>Cairo and Giza are outside the path</strong>: about 95% partial, not total.',
        'Wear <strong>ISO 12312-2</strong> eclipse glasses for every partial phase; remove them only during '
        'totality, inside the path.',
        'The next total eclipse visible from the contiguous United States is <strong>23 August 2044</strong>.',
    ]) + """
      <p>The eclipse will happen on schedule. Everything else about getting there is the part that can go
      wrong, and most of it is decided months before.</p>
""",
    'sources': [
        ('Instituto Geográfico Nacional (Spain) &mdash; Total solar eclipse, 2 August 2027',
         'https://astronomia.ign.es/en/web/guest/eclipses-de-sol-y-luna/eclipse-total-sol-de-2-de-agosto-2027'),
        ('Atlas Obscura &mdash; 2027 total solar eclipse: where to see it',
         'https://www.atlasobscura.com/articles/guide-to-2027-total-eclipse'),
        ('NASA Science &mdash; 2024 total solar eclipse and future eclipses',
         'https://science.nasa.gov/eclipses/future-eclipses/eclipse-2024/'),
        ('Space.com &mdash; Eclipse experts&rsquo; best travel tips for the total solar eclipse 2027',
         'https://www.space.com/stargazing/solar-eclipses/eclipse-experts-best-travel-tips-for-the-total-solar-eclipse-2027'),
        ('National Eclipse &mdash; 2027 total solar eclipse maps for Spain, North Africa and Egypt',
         'https://nationaleclipse.com/maps/main/2027-total-solar-eclipse-maps.html'),
        ('Wikipedia &mdash; Solar eclipse of August 2, 2027',
         'https://en.wikipedia.org/wiki/Solar_eclipse_of_August_2,_2027'),
    ],
    'next': {'slug': 'the-big-trip',
             'title': 'The big trip, done right',
             'blurb': 'Planning one trip that has to go right, and the decisions that cost money to '
                      'reverse.'},
}

# ------------------------------------------------------------- UK ETA
ARTICLES26['uk-eta'] = {
    'title': 'UK ETA for Americans: The &pound;20 Travel Authorization &mdash; The Second Half Guide',
    'eyebrow': 'Facts &amp; thresholds',
    'h1': 'The UK&rsquo;s &pound;20 travel authorization: what Americans need before the flight',
    'dek': 'Britain now wants an Electronic Travel Authorisation from American visitors, checked by the '
           'airline before you board. The fee, the validity, and where the copycat sites are.',
    'meta': '5 minute read &middot; Checked against the Home Office factsheet, UK Parliament and '
            'independent guides',
    'checked': CHECKED26,
    'body': """      <p>A visit to Britain used to require a passport and an answer to a few questions at the border.
      Now it requires something before the flight. The UK&rsquo;s Electronic Travel Authorisation, the ETA,
      is a digital permission linked to your passport that American visitors have to hold before they
      travel. It is live, it is cheap, and it is the kind of thing that can be sold to you by someone else
      at three times the price.</p>

      <p>It is also not the same thing as the European Union&rsquo;s ETIAS, which has not started. People
      mix them up constantly, and the mix-up is where most of the cost is.</p>

""" + facts('The UK ETA, in numbers', [
        ('&pound;20', 'The fee, per the Home Office&rsquo;s April 2026 factsheet. Older guides list '
                      '&pound;16; they are out of date.'),
        ('2 years', 'How long an ETA lasts, or until the passport expires, whichever comes first.'),
        ('6 months', 'The longest stay it permits on any one visit. It allows multiple trips while valid.'),
        ('Up to 3 working days', 'The government&rsquo;s stated processing window. Most decisions are '
                                 'reported to come within a day.'),
        ('Each traveler', 'Every person, including a child, needs their own ETA. It is tied to a passport.'),
        ('25 February 2026', 'The date a UK Parliament statement says carriers must check for permission to '
                             'travel before boarding.'),
    ]) + """
      <h2>What it is, and what it is not</h2>

      <p>An ETA is permission to travel to the UK. It is not a visa, and it is not a guarantee of entry.
      A border officer can still refuse a visitor who has one, and guides describe it as
      authorizing travel, not admission. It does not allow work. It is a screening step that moves the
      question of whether you may come from the border to before you leave.</p>

      <p>It applies to Americans, Canadians, Australians and citizens of all 27 EU countries, among others.
      British and Irish citizens are exempt, including dual citizens, and a US-Irish dual national would
      travel on the Irish passport. Airlines now check. A UK Parliament written statement dated
      25 February 2026 says carriers are required to verify, through automated checks against Home
      Office records, that a passenger holds permission to travel before they board. A traveler without
      one can be refused at the gate, which is a worse place to find out than a website.</p>

      <p>The exemptions are narrow. People who already hold certain UK immigration permissions are
      exempt, as are some transit passengers. A visitor from the United States who is not British or Irish
      should assume the ETA applies, and check GOV.UK for the specific case. The ETA is linked to a
      passport and does not replace it. The six-month limit is a ceiling on any one visit, not a
      promise of how long a border officer will allow.</p>

      <h2>How to apply, and how long it takes</h2>

      <p>The Home Office&rsquo;s factsheet points applicants to the UK ETA app, available from the Apple and
      Google stores, and guides add that an application can also be made through the government&rsquo;s own
      GOV.UK pages. The application asks for a passport, a photograph and some questions, and the
      stated decision window is up to three working days. Reporting says most applications are decided
      within a day, which makes the sensible rule to apply well before the trip, and not at the airport.</p>

      <blockquote class="pull">
        <p>The official fee is &pound;20. Anything that costs more is a service fee for filling in the same
        form.</p>
      </blockquote>

""" + AD_INLINE + """
      <h2>Where the extra charges come from</h2>

      <p>Several third-party websites advertise UK ETA services at a higher price, and they are not the
      official channel. One guide notes that they charge a service fee on top of the &pound;20, and that
      paying more does not get a faster decision. The pattern is familiar from
      <a href="/etias">the ETIAS page</a>: the real thing exists, a copy sits in front of it, and the copy
      looks official because it uses the same words. The check is the same too. The application is made in
      the government&rsquo;s own app or on a GOV.UK address. A site that asks for a larger payment, or that
      promises an &ldquo;express&rdquo; decision, is not that.</p>

      <h2>The details that cause trouble</h2>

      <p>Because the ETA is tied to a passport, a new passport means a new ETA. A person who renews their
      passport between buying the ticket and flying needs to apply again for the new document. Every
      traveler needs their own, including a grandchild on the same trip, and there is no family
      application. And the passport used to apply must be the one the traveler flies on, which matters for
      someone who holds two.</p>

      <p>Several commercial guides say Americans have needed an ETA since early 2025. This page does not
      repeat the exact date, because the official sources checked did not give it. What the official
      sources do show is that the requirement is in force and that airlines enforce it. One guide also
      describes an exemption for passengers who stay in the airside transit area without passing through
      UK border control and calls it temporary. That is not confirmed here and should be checked on GOV.UK
      before a connection.</p>

      <h2>Where this sits among the other changes</h2>

      <p>Europe&rsquo;s fingerprint and photo checks have been running at Schengen borders since April, and
      the EU&rsquo;s authorization, ETIAS, has no start date. The UK&rsquo;s ETA is the one of the three that
      requires an action before an American flies to Britain now. Travel documents that go wrong at borders
      in other ways are on <a href="/passport-traps">the passport page</a>, and the broader planning for a
      long trip is on <a href="/the-big-trip">the big trip page</a>.</p>

      <h2>What&rsquo;s worth keeping in mind</h2>

""" + check([
        'American visitors need a UK ETA before they fly. It costs <strong>&pound;20</strong> and lasts '
        '<strong>two years</strong> or until the passport expires.',
        'Each traveler, <strong>including children</strong>, needs their own. It is tied to the passport, so a '
        'new passport means a new ETA.',
        'Apply through the <strong>UK ETA app or GOV.UK</strong>. Decisions can take up to three working days.',
        'Airlines check for permission to travel before boarding. An ETA is <strong>not a visa and not a '
        'guarantee of entry</strong>.',
        'Sites charging more than &pound;20 are not the government.',
    ]) + """
      <p>The form takes a few minutes and the fee is small. The cost, when there is one, comes from the
      wrong website, or from finding out at the gate.</p>
""",
    'sources': [
        ('UK Home Office &mdash; Electronic Travel Authorisation (ETA) factsheet, April 2026',
         'https://homeofficemedia.blog.gov.uk/electronic-travel-authorisation-eta-factsheet-april-2026/'),
        ('UK Parliament &mdash; Written statement on ETA checks by carriers (25 February 2026)',
         'https://questions-statements.parliament.uk/written-statements/detail/2026-02-25/hcws1361'),
        ('University of Wisconsin &mdash; U.S. citizens traveling to the UK: new ETA requirement',
         'https://www.wisconsin.edu/travel/2026/08/14/20266/'),
        ('Schengen Traveler &mdash; UK ETA for US citizens 2026',
         'https://schengentraveler.com/uk-eta-americans/'),
    ],
    'next': {'slug': 'etias',
             'title': 'ETIAS: the EU travel authorization that isn&rsquo;t live yet',
             'blurb': 'Europe&rsquo;s equivalent has no start date, and websites are charging for it '
                      'anyway.'},
}

# ------------------------------------------------------------- SilverSneakers
ARTICLES26['silversneakers-2027'] = {
    'title': 'SilverSneakers and Medicare Gym Benefits for 2027: What to Check &mdash; The Second Half Guide',
    'eyebrow': 'Facts &amp; thresholds',
    'h1': 'SilverSneakers and Medicare gym benefits for 2027: what to check before 7 December',
    'dek': 'Original Medicare does not pay for a gym. Some Medicare Advantage plans do, in different '
           'programs under different names, and the benefit is decided plan by plan, every year.',
    'meta': '5 minute read &middot; Checked against plan announcements, SilverSneakers and independent '
            'reporting',
    'checked': CHECKED26,
    'body': """      <p>&ldquo;Free gym membership with Medicare&rdquo; is one of the most searched phrases of the
      fall, and it is both true and misleading. It is true for many people with a Medicare Advantage
      plan. It is not true of Medicare itself. The difference is why a benefit that was there in 2026 can
      be gone in 2027 with no change to anything the person did.</p>

      <p>Annual Enrollment runs through 7 December. Here is what is known about the gym benefit, what is
      not, and where to look.</p>

""" + facts('Medicare gym benefits, in numbers', [
        ('Original Medicare', 'Parts A and B do not cover gym memberships or fitness programs.'),
        ('Plan by plan', 'Fitness benefits are add-ons to individual Medicare Advantage plans. They can '
                         'be added, changed or removed each year.'),
        ('About 9 in 10', 'Share of Medicare Advantage plans offering some fitness benefit in 2026, down '
                          'slightly from 2025. Reports citing KFF give 93% and 91%.'),
        ('15 October &ndash; 7 December', 'Annual Enrollment, when a plan can be changed for 2027.'),
        ('1 January &ndash; 31 March 2027', 'The Medicare Advantage Open Enrollment Period, which allows one '
                                           'change for people already in an Advantage plan.'),
        ('Plan documents', 'The 2027 Summary of Benefits and Evidence of Coverage control what is '
                           'provided. The Annual Notice of Change summarizes the differences.'),
    ]) + """
      <h2>What SilverSneakers is</h2>

      <p>SilverSneakers is a fitness program that a health plan buys on behalf of its members, who then
      get access to participating gyms and classes at no extra cost. It is not a Medicare benefit. It is a
      product that some plans license, in the same way that other plans use their own programs. The best
      known alternative is UnitedHealthcare&rsquo;s Renew Active, which is reported to appear on certain
      UnitedHealthcare Medicare Advantage and AARP Medicare Supplement plans. A member who sees a different
      name on a 2027 notice has not necessarily lost the benefit. The program name changed.</p>

      <p>That is the first thing to check, because the names are not interchangeable. Someone who has used
      a particular gym through SilverSneakers needs to know whether that gym is part of the plan&rsquo;s
      new program, and not just whether &ldquo;a fitness benefit&rdquo; is listed.</p>

      <h2>What is known about 2027</h2>

      <p>Aetna has said it will continue to offer a SilverSneakers basic fitness membership to individual
      Medicare Advantage members at no additional cost. Beyond that, no industry-wide announcement of
      drops turned up, and the reporting is mixed. Some plans have dropped SilverSneakers but offer a
      similar benefit in its place. Others have dropped fitness benefits altogether. The overall figure
      shows how small the shift is in aggregate and how large it can be for one person: about nine in ten
      Advantage plans offered some fitness benefit in 2026, and a few points fewer than the year before.</p>

      <p>It is also not limited to Advantage plans. Some Medicare Supplement (Medigap) policies include a
      fitness program, though not as a standard feature, and an insurer&rsquo;s own materials are the place
      to see whether a given policy does.</p>

      <blockquote class="pull">
        <p>A gym benefit is part of the plan, not part of Medicare. It can change on 1 January with nothing
        else changing.</p>
      </blockquote>

""" + AD_INLINE + """
      <h2>Where to look, in order</h2>

      <p>The Annual Notice of Change is the first place. It is mailed in the fall and lists what is
      changing for the coming year, including a changed or dropped benefit. It is covered on
      <a href="/anoc-letter">the Annual Notice of Change page</a>. The Evidence of Coverage is the
      binding document, and the Summary of Benefits gives the short form. SilverSneakers itself says to
      ask the health plan whether the program is included going into 2027, and offers a way to check on
      its own site. Calling the plan and asking for the benefit by name is slower than reading a page
      and more reliable than a brochure.</p>

      <p>Plan details that vary include which gyms participate, whether home fitness kits are offered,
      and whether the benefit comes with a card, an app or a separate sign-up. None of that carries over
      automatically if a person changes plans in the fall.</p>

      <h2>The timing rule people miss</h2>

      <p>Annual Enrollment is when a plan can be changed for 2027. A person who finds out in January that
      the gym benefit is gone has a narrower option: the Medicare Advantage Open Enrollment Period,
      1 January to 31 March, which allows one change by someone already in an Advantage plan. One guide
      adds that losing a fitness benefit does not, by itself, create a special enrollment period. That
      is a general reporting point and not a statement about any person&rsquo;s eligibility. The practical
      consequence is plain: the notice that arrives in the fall is the one to read in the fall. The
      rules for the January window are on <a href="/medicare-advantage-oep">the Advantage open
      enrollment page</a>, and the broader rules for October and December are on
      <a href="/open-enrollment">the open enrollment page</a>.</p>

      <h2>What a fitness benefit is, and is not</h2>

      <p>A gym benefit is one line among many in a plan, alongside the allowances covered on
      <a href="/ma-flex-card-2027">the flex card page</a>. It is not a medical service, and Medicare does
      cover the free yearly visit that is a different thing, covered on
      <a href="/wellness-visit">the wellness visit page</a>. The reason the gym benefit is worth a look is
      that it is decided plan by plan and can change each year. This page does not say whether a person should choose a plan for it. It says where the
      benefit is written down.</p>

      <h2>What&rsquo;s worth keeping in mind</h2>

""" + check([
        '<strong>Original Medicare does not cover</strong> gym memberships. Fitness benefits belong to '
        'individual Medicare Advantage plans, and to some Medigap policies.',
        'The program can change name or disappear each year. <strong>Aetna</strong> says it continues '
        'SilverSneakers basic for individual Advantage members; UnitedHealthcare uses its own '
        '<strong>Renew Active</strong>.',
        'Read the <strong>Annual Notice of Change</strong> and the 2027 <strong>Evidence of Coverage</strong>; '
        'check the program name and the participating gym.',
        'Annual Enrollment closes <strong>7 December</strong>. After that, a person already in an Advantage '
        'plan has one change from 1 January to 31 March.',
    ]) + """
      <p>The benefit is easy to take for granted because it is free to use. It is only free for as long as
      the plan still includes it, and the place that says so is a letter most people do not open.</p>
""",
    'sources': [
        ('Aetna &mdash; 2027 Medicare Advantage plans and benefits',
         'https://www.aetna.com/insights/news/aetna-2027-medicare-advantage-plans.html'),
        ('U.S. News &mdash; Is your Medicare plan dropping SilverSneakers? What to know for 2026 and 2027',
         'https://health.usnews.com/medicare/articles/what-is-silver-sneakers'),
        ('SilverSneakers &mdash; Do you have SilverSneakers? Here&rsquo;s how to find out',
         'https://www.silversneakers.com/blog/do-you-have-silversneakers-heres-how-to-find-out/'),
        ('SilverSneakers &mdash; Why doesn&rsquo;t my new Medicare plan have SilverSneakers?',
         'https://silversneakers.com/blog/why-doesnt-my-new-medicare-plan-have-silversneakers/'),
        ('Humana &mdash; What is SilverSneakers and does Medicare cover it?',
         'https://www.humana.com/medicare/medicare-resources/silver-sneakers-and-medicare'),
        ('Highmark &mdash; Medicare fitness programs',
         'https://medicare.highmark.com/shop/medicare/learn/plan-perks-and-services/highmark-fitness.html'),
    ],
    'next': {'slug': 'anoc-letter',
             'title': 'The Annual Notice of Change letter, and what it says',
             'blurb': 'The one piece of fall mail that tells you what changes in your plan next year.'},
}
