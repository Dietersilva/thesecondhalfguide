#!/usr/bin/env python3
"""Sixth batch: the travel cluster — airport help, security, passports,
medications and equipment, cruise medicine, and planning the big trip."""

from build_articles import facts, check, AD_INLINE, CHECKED

ARTICLES6 = {}

# ------------------------------------------------------------- airport help
ARTICLES6['airport-help'] = {
    'title': 'The Airport Help You’re Entitled To, and Nobody Mentions &mdash; The Second Half Guide',
    'eyebrow': 'Getting out there',
    'h1': 'The airport help you’re entitled to, and nobody mentions',
    'dek': 'Wheelchairs, escorts through the terminal, someone to walk you through security. All free, '
           'all yours by law &mdash; and almost entirely unused, because nobody tells you and asking '
           'feels like admitting something.',
    'meta': '6 minute read &middot; Verified against DOT and TSA guidance',
    'checked': CHECKED,
    'body': """      <p>Airports have quietly become one of the main reasons people stop travelling.</p>

      <p>Not the flying. The distance from the kerb to the gate, the standing in queues, the shoes, the
      belt, the tight connection at an airport the size of a small town. Plenty of people who are
      perfectly capable of enjoying two weeks in Lisbon look at the getting-there and decide it isn't
      worth it.</p>

      <p>What almost nobody realises is that the help exists, it's free, and it isn't a favour. It's
      federal law.</p>

      <h2>What the law actually says</h2>

      <p>The <strong>Air Carrier Access Act</strong> requires airlines to provide assistance to
      passengers with a disability or reduced mobility, at no charge. And the definition is broader than
      most people assume &mdash; you do not need a diagnosis, a permanent condition, or a wheelchair of
      your own. If you can't comfortably manage the walk from check-in to the gate, you qualify.</p>

""" + facts('What you can ask for, free of charge', [
        ('Kerb to gate', 'A wheelchair and someone to push it, from the moment you arrive at the terminal '
                         'to your seat on the aircraft.'),
        ('Between gates', 'Assistance across a connection &mdash; often the leg that actually defeats '
                          'people, in an unfamiliar airport with 40 minutes to spare.'),
        ('An escort, without a wheelchair', 'If walking is fine but navigating isn’t, you can ask for '
                                            'someone to guide you. This is a real and much less '
                                            'well-known option.'),
        ('Boarding assistance', 'Including an aisle chair where a normal wheelchair won’t fit.'),
        ('At the far end', 'The same again on arrival, through to baggage claim and the kerb.'),
        ('The cost', 'Nothing. Airlines are prohibited from charging for any of it.'),
    ]) + """
      <blockquote class="pull">
        <p>You don't need a diagnosis and you don't need to justify yourself. &ldquo;I'd like wheelchair
        assistance&rdquo; is a complete sentence.</p>
      </blockquote>

      <h2>How to arrange it</h2>

      <p>Airlines ask for <strong>48 hours' notice</strong> (Southwest says 24), and giving it makes
      everything smoother. But here's the part worth knowing: <strong>they cannot refuse you because you
      didn't call ahead.</strong> If you arrive and need help you didn't book, ask at the check-in desk.</p>

      <p>You can usually add assistance when booking online — look for &ldquo;special assistance&rdquo; or
      &ldquo;accessibility&rdquo; in the passenger details. If you booked through an agent or a website,
      call the airline directly afterwards to confirm it's on the reservation, because it doesn't always
      travel with the booking.</p>

      <h2>Security: TSA Cares</h2>

      <p>Separately from the airline, the TSA runs a programme called <strong>TSA Cares</strong>. Call
      <strong>1-855-787-2227</strong> at least 72 hours before your flight and they'll arrange a
      Passenger Support Specialist to meet you and walk you through screening.</p>

      <p>This is the right call if screening itself is the difficult part — a medical device, a joint
      replacement that sets off the detector, a condition that makes standing in line hard, or a
      travelling companion with dementia for whom the queue is genuinely distressing. It's free, and it
      is startlingly under-used.</p>

""" + AD_INLINE + """
      <h2>The part that isn’t about logistics</h2>

      <p>Let's be honest about why this help goes unused, because it usually isn't ignorance.</p>

      <p>Asking for a wheelchair feels like a statement about yourself. People who've walked eighteen
      holes that month don't want to be pushed through Terminal C. There's a sense that the help is for
      someone worse off, and that taking it is either an admission or a bit of a cheat.</p>

      <p>Two things worth saying against that. First, the service exists for <em>reduced mobility</em>,
      not disability alone — a bad knee, a recent surgery, a heart condition, or simply not being able to
      do three-quarters of a mile at pace with a bag all qualify, and the staff pushing the chair are not
      assessing you.</p>

      <p>Second, and more practically: the alternative to using it is often not travelling. Plenty of
      people quietly stop taking trips because the airport became the hard part, and never connect that
      decision to a free service they'd have found mildly embarrassing to request. Measured against
      seeing your grandchildren, that's a poor trade.</p>

      <h2>Making it work</h2>

""" + check([
        'Request assistance <strong>when you book</strong>, then <strong>call the airline</strong> to '
        'confirm it is on the reservation. Bookings made through third parties often lose it.',
        'Give yourself <strong>more time, not less</strong>. Assistance is a queue like any other, and at '
        'busy airports there can be a wait for someone to arrive.',
        'On connections, tell them at the <strong>first</strong> airport that you need help at the next '
        'one. It should be on the booking, but confirming costs nothing.',
        'For screening difficulties, call <strong>TSA Cares on 1-855-787-2227</strong> at least 72 hours '
        'ahead.',
        'Bring a <strong>doctor’s note</strong> if you have implants, a pump, or a device. Not required, '
        'but it shortens conversations.',
        'If assistance is denied or badly handled, airlines must have a <strong>Complaints Resolution '
        'Official</strong> available. Ask for one by name &mdash; it changes the conversation immediately.',
    ]) + """
      <p>None of this makes an airport pleasant. It does remove the specific part that stops people
      travelling, and it costs nothing but a phone call and a small amount of pride.</p>

      <p>Of everything on this site, this may be the item with the widest gap between how useful it is and
      how few people know about it.</p>
""",
    'sources': [
        ('U.S. Department of Transportation &mdash; Wheelchair and guided assistance',
         'https://www.transportation.gov/individuals/aviation-consumer-protection/wheelchair-and-guided-assistance'),
        ('U.S. DOT &mdash; Passengers with disabilities',
         'https://www.transportation.gov/individuals/aviation-consumer-protection/passengers-disabilities'),
        ('TSA Cares', 'https://www.tsa.gov/travel/passenger-support'),
    ],
    'next': {'slug': 'airport-security',
             'title': 'Airport security after 75, and whether PreCheck is worth it',
             'blurb': 'The shoe rule, the jacket exception nobody mentions, and the actual arithmetic on '
                      'PreCheck versus Global Entry.'},
}

# ---------------------------------------------------------- airport security
ARTICLES6['airport-security'] = {
    'title': 'Airport Security After 75, and Whether PreCheck Is Worth It &mdash; The Second Half Guide',
    'eyebrow': 'Getting out there',
    'h1': 'Airport security after 75, and whether PreCheck is worth it',
    'dek': 'There is a real age threshold in airport screening, it starts at 75, and it is narrower than '
           'people think. Here is what it covers and what it doesn’t.',
    'meta': '5 minute read &middot; Fees and rules verified for 2026',
    'checked': CHECKED,
    'body': """      <p>Among the many age thresholds we've catalogued on this site, here's one that turns up in an
      unexpected place: airport security.</p>

      <p><strong>Passengers 75 and older can keep their shoes on</strong> during standard screening. It's
      part of the TSA's risk-based approach, it requires no application and no fee, and a surprising
      number of people who qualify have never heard of it.</p>

      <p>It's also narrower than it sounds, in a way that matters if you're deciding whether to pay for
      anything.</p>

""" + facts('The screening options, 2026', [
        ('Turning 75', 'Shoes stay on in standard lanes. No fee, no application, no card &mdash; it '
                       'applies automatically.'),
        ('The catch', 'The 75+ exemption does <em>not</em> cover light jackets. Those still come off for '
                      'imaging in standard lanes.'),
        ('TSA PreCheck', 'About $77&ndash;$85 for five years, depending on the enrolment provider. Shoes, '
                         'belt and light jacket stay on; laptops and liquids stay in the bag; separate, '
                         'usually shorter lane.'),
        ('Global Entry', '$120 for five years. <strong>Includes PreCheck</strong>, and speeds re-entry '
                         'into the US through passport control.'),
        ('CLEAR', 'A separate paid service, several hundred dollars a year. Moves you to the front of the '
                  'identity-check queue. It does not change how you are screened.'),
        ('Age 12 and under', 'Also keep shoes on, travelling with an eligible adult.'),
    ]) + """
      <h2>The arithmetic that surprises people</h2>

      <p>Global Entry costs $120 and includes PreCheck. PreCheck alone costs roughly $77–$85. So the
      extra $35–$43 buys you expedited re-entry into the United States on international trips —
      and it's spread across five years.</p>

      <p>If you travel abroad even once in five years, <strong>Global Entry is the better buy</strong>,
      and it isn't close. The queue at passport control after a long-haul flight is the one that
      genuinely tests people. The main argument for PreCheck alone is that it's slightly easier to get:
      Global Entry requires an in-person interview, and appointment waits at some enrolment centres run
      to months.</p>

      <blockquote class="pull">
        <p>Global Entry is $43 more than PreCheck across five years and includes it. If there's any
        chance of an international trip, that's the one.</p>
      </blockquote>

""" + AD_INLINE + """
      <h2>Why PreCheck still helps after 75</h2>

      <p>Because of the jacket. In standard lanes a light jacket comes off for imaging regardless of age
      — PreCheck removes that, along with the belt, and lets your laptop and liquids stay in the bag.</p>

      <p>Which is really the point: the value of PreCheck isn't speed so much as <strong>the number of
      separate physical operations</strong> you perform at the belt while people queue behind you.
      Standard screening asks you to remove a jacket, a belt, shoes if you're under 75, take a laptop
      out, take liquids out, and reassemble all of it one-handed at the far end. PreCheck removes most of
      that.</p>

      <p>For anyone with arthritic hands, balance issues, or a strong dislike of being hurried, that's
      the benefit. Not minutes saved — fumbling avoided.</p>

      <h2>A few things worth knowing</h2>

      <ul>
        <li><strong>Check your Known Traveler Number is on the booking.</strong> PreCheck only works if
        the airline has your KTN, and it doesn't always carry over from an old profile or a booking made
        by someone else.</li>
        <li><strong>Some credit cards reimburse the fee</strong> for PreCheck or Global Entry, often once
        every four years. If you carry a travel card, check before paying.</li>
        <li><strong>Medical devices and implants:</strong> tell the officer before screening. A joint
        replacement will set off a detector, and saying so first turns a search into a formality.</li>
        <li><strong>Medications and mobility aids don't count</strong> against carry-on limits, and
        liquids that are medically necessary are exempt from the usual limit — declare them.</li>
        <li><strong>REAL ID</strong> is now required for domestic flights. A passport works too. Check
        your licence has the star before you rely on it.</li>
      </ul>

""" + check([
        'Turning 75? You already have the shoe exemption &mdash; <strong>nothing to apply for</strong>.',
        'Travelling abroad at all in the next five years? <strong>Global Entry</strong>, not PreCheck.',
        'Check whether a <strong>credit card</strong> you already hold reimburses the fee.',
        'Put your <strong>Known Traveler Number</strong> in your airline profile and check it appears on '
        'each booking.',
        'Tell the officer about <strong>implants and devices</strong> before you step through, not after '
        'the alarm.',
        'Confirm your driver’s licence is <strong>REAL ID compliant</strong>, or carry your passport.',
    ]) + """
      <p>None of this is dramatic. But screening is the part of the journey most likely to leave someone
      flustered before they've even boarded, and a fair amount of it is avoidable for either nothing or
      about $24 a year.</p>
""",
    'sources': [
        ('TSA &mdash; Screening for passengers 75 and older',
         'https://www.tsa.gov/travel/tsa-cares/screening-passengers-75-and-older'),
        ('TSA PreCheck', 'https://www.tsa.gov/precheck'),
        ('U.S. Customs and Border Protection &mdash; Global Entry',
         'https://www.cbp.gov/travel/trusted-traveler-programs/global-entry'),
        ('TSA &mdash; REAL ID', 'https://www.tsa.gov/real-id'),
    ],
    'next': {'slug': 'passport-traps',
             'title': 'The passport rules that turn people away at check-in',
             'blurb': 'The six-month rule, renewal timing, and the card that won’t fly you anywhere.'},
}

# ------------------------------------------------------------ passport traps
ARTICLES6['passport-traps'] = {
    'title': 'The Passport Rules That Turn People Away at Check-In &mdash; The Second Half Guide',
    'eyebrow': 'Getting out there',
    'h1': 'The passport rules that turn people away at check-in',
    'dek': 'A valid passport is not always a usable one. The rule that catches people has nothing to do '
           'with the expiry date printed inside it.',
    'meta': '5 minute read &middot; Processing times verified for 2026',
    'checked': CHECKED,
    'body': """      <p>You can be denied boarding on an international flight holding a passport that has not expired.
      It happens at check-in, at the airport, with bags packed and a non-refundable trip behind it.</p>

      <p>The reason is a rule most people have never heard of, and airlines enforce it because they're
      the ones fined if they carry someone a country then refuses.</p>

      <h2>The six-month rule</h2>

      <p>Many countries require your passport to be valid for <strong>at least six months beyond the
      date you enter</strong> — some ask for three. If your passport expires in four months and you're
      flying to a country with a six-month requirement, you will be turned away, and the fact that the
      document is technically valid makes no difference at all.</p>

      <p>Dozens of countries apply some version of this, including much of Asia and the Middle East and a
      number of destinations across Europe. It varies, it changes, and the only reliable check is the
      State Department's country page for wherever you're going.</p>

""" + facts('What to know before you book', [
        ('The six-month rule', 'Many countries require six months of validity beyond entry; some require '
                               'three. Airlines enforce it at check-in.'),
        ('Blank pages', 'Some countries require one or two entirely blank pages for stamps. A full '
                        'passport can be refused.'),
        ('Routine renewal', 'About 4&ndash;6 weeks in 2026, plus roughly a week of postal time at each '
                            'end. Budget two months.'),
        ('Expedited', 'About 2&ndash;3 weeks for an extra $60, again plus mailing.'),
        ('The passport card', 'Valid for land and sea crossings to Canada, Mexico, the Caribbean and '
                              'Bermuda. <strong>Not valid for international air travel.</strong>'),
        ('Name mismatches', 'The name on the ticket must match the passport. Marriage, divorce and '
                            'middle-name variations cause real problems.'),
    ]) + """
      <blockquote class="pull">
        <p>The practical rule: renew when you have a year left, not when it expires. It removes the whole
        category of problem.</p>
      </blockquote>

""" + AD_INLINE + """
      <h2>The passport card mistake</h2>

      <p>The card is cheaper, fits in a wallet, and looks like a passport. People get one thinking
      they've solved international travel and discover otherwise at the airport.</p>

      <p>It works for driving into Canada or Mexico and for cruises that begin and end in the US. It will
      not board you onto an international flight — including, awkwardly, the flight home if a cruise goes
      wrong and you need to fly back from a foreign port. That's a genuine scenario worth thinking about
      before relying on the card for a cruise.</p>

      <h2>Timing, which is the whole game</h2>

      <p>Processing has improved considerably: routine runs about four to six weeks, expedited two to
      three. But those figures start when your application <em>arrives</em>, not when you post it, so add
      roughly a week either side.</p>

      <p>Which means a renewal begun in mid-May for a July trip is uncomfortably tight, and the same
      renewal begun in February is a non-event. There are urgent-travel appointments at passport agencies
      for genuine emergencies, but they require proof of imminent travel and appointments are limited —
      not a plan, a rescue.</p>

      <h2>Worth doing</h2>

""" + check([
        'Look at your passport <strong>now</strong>. If it expires within a year, renew it &mdash; not '
        'when it expires.',
        'Check the <strong>State Department country page</strong> for each destination before booking. '
        'It lists validity and blank-page requirements.',
        'Confirm the <strong>name on your ticket matches the passport exactly</strong>, including middle '
        'names.',
        'Count your <strong>blank pages</strong> if you have travelled a lot.',
        'Never rely on a <strong>passport card</strong> for anything involving a plane.',
        'Photograph the ID page and keep a copy separately from the passport. It does not replace it, but '
        'it speeds up replacing a lost one considerably.',
    ]) + """
      <p>This is the least interesting article on the site and possibly the most expensive one to ignore.
      A renewal costs a stamp and some patience in February. In June it costs a trip.</p>
""",
    'sources': [
        ('U.S. Department of State &mdash; Passports',
         'https://travel.state.gov/content/travel/en/passports.html'),
        ('U.S. Department of State &mdash; Country information',
         'https://travel.state.gov/content/travel/en/international-travel/International-Travel-Country-Information-Pages.html'),
        ('U.S. Department of State &mdash; Passport card',
         'https://travel.state.gov/content/travel/en/passports/need-passport/card.html'),
    ],
    'next': {'slug': 'travel-medications',
             'title': 'Flying with medications and medical equipment',
             'blurb': 'What you can carry, what needs approval in advance, and the one device you '
                      'genuinely cannot bring.'},
}

# ------------------------------------------------------- meds and equipment
ARTICLES6['travel-medications'] = {
    'title': 'Flying With Medications and Medical Equipment &mdash; The Second Half Guide',
    'eyebrow': 'Getting out there',
    'h1': 'Flying with medications and medical equipment',
    'dek': 'Most of it is easier than people fear. One thing is a hard no, and a few require paperwork '
           'weeks in advance &mdash; which is the part that ruins trips.',
    'meta': '6 minute read &middot; Verified against TSA and FAA rules',
    'checked': CHECKED,
    'body': """      <p>The anxiety here is usually out of proportion to the rules. Medication travels far more
      easily than most people expect, and the security side is largely accommodating.</p>

      <p>But there's one absolute prohibition, and a couple of things that need arranging weeks ahead
      rather than at the gate. Those are what this piece is for.</p>

      <h2>The hard no: oxygen tanks</h2>

      <p><strong>You cannot bring your own oxygen cylinder onto a commercial aircraft.</strong> Compressed
      and liquid oxygen are hazardous materials and they are not permitted, in the cabin or the hold. No
      exceptions, no doctor's note.</p>

      <p>What is permitted is an <strong>FAA-approved portable oxygen concentrator</strong>, which makes
      oxygen from cabin air rather than storing it. If you use oxygen, this is the single most important
      thing to sort out before booking, because it has several moving parts:</p>

      <ul>
        <li>The device must be an <strong>FAA-accepted model</strong>. Not all concentrators are.</li>
        <li>You must carry <strong>batteries for at least 150% of the expected flight time</strong> —
        including likely delays. For a six-hour flight that's nine hours of battery, which is more than
        people bring.</li>
        <li>Most airlines require <strong>advance notification</strong> and many want a form signed by
        your doctor, often 48 hours ahead or more.</li>
        <li>Airlines generally <strong>no longer supply oxygen</strong> themselves. The concentrator is
        the route.</li>
      </ul>

      <p>The good news: under the Air Carrier Access Act, an approved concentrator must be permitted in
      the cabin, and as an assistive device it <strong>doesn't count toward your carry-on allowance</strong>.</p>

""" + facts('What travels easily', [
        ('Pills and tablets', 'No quantity limit in carry-on. Original labelled bottles aren’t federally '
                              'required but make everything faster, and some countries do want them.'),
        ('Liquid medication', 'Exempt from the 3-1-1 liquid limit in reasonable quantities. Declare it at '
                              'the checkpoint and it may be screened separately.'),
        ('Needles and syringes', 'Permitted with the medication they go with. Declare them.'),
        ('CPAP machines', 'Permitted, don’t count as carry-on, and can be screened separately. Bring an '
                          'extension cord and a plug adapter.'),
        ('Cooling packs', 'Allowed for medication that needs them, including gel packs, even if not '
                          'frozen solid.'),
        ('Mobility aids', 'Wheelchairs, walkers, canes &mdash; all permitted, none count as baggage.'),
    ]) + """
      <blockquote class="pull">
        <p>Everything you can't replace goes in your carry-on. Checked bags go missing, and a bag that
        catches up with you on Thursday is no help on Tuesday.</p>
      </blockquote>

""" + AD_INLINE + """
      <h2>Crossing borders is a different question</h2>

      <p>TSA rules govern getting on the plane. They have nothing to do with what's legal where you land,
      and that trips people up.</p>

      <p>Some medications that are entirely ordinary in the US are <strong>controlled or banned
      elsewhere</strong> — certain stimulants, some strong painkillers, some sleep medications, and a
      number of cold remedies containing pseudoephedrine. Japan, the UAE, Singapore and others enforce
      this seriously, and &ldquo;it's prescribed&rdquo; is not always a defence.</p>

      <p>The check takes ten minutes: look up the destination country's embassy page for medication
      rules. Carry a copy of your prescription and a letter from your doctor listing what you take and
      why. Keep everything in labelled original packaging when crossing borders.</p>

      <h2>The practical failures</h2>

      <p>The problems people actually have are rarely regulatory:</p>

      <ul>
        <li><strong>Running out.</strong> Bring more than the trip needs — a week extra is a reasonable
        rule. Delays happen, and refilling a US prescription abroad is not straightforward.</li>
        <li><strong>Time zones.</strong> For most medication, shifting gradually is fine. For anything
        time-critical — insulin, some heart and thyroid medication, anticoagulants — ask your doctor for
        a plan before you go rather than improvising at 35,000 feet.</li>
        <li><strong>Splitting supplies.</strong> Divide medication between two bags in case one goes
        astray.</li>
        <li><strong>Refrigeration.</strong> Confirm the hotel has a fridge that actually works, not a
        minibar that cools to 12°C.</li>
      </ul>

""" + check([
        'Use a concentrator? Sort the <strong>airline’s approval</strong> and the <strong>150% battery '
        'rule</strong> before you book anything else.',
        'Everything essential goes in the <strong>carry-on</strong>, split across two bags if you can.',
        'Pack <strong>a week more</strong> than the trip requires.',
        'Check the <strong>destination country’s rules</strong> on your specific medications.',
        'Carry a <strong>doctor’s letter</strong> listing medications and devices. It costs nothing and '
        'ends most conversations.',
        'Ask about <strong>time-zone dosing</strong> before you leave if anything you take is '
        'time-critical.',
    ]) + """
      <p>Almost none of this is difficult. It's just that the pieces requiring lead time — the
      concentrator approval, the doctor's letter, the extra refill — cannot be sorted out at the airport,
      and that's exactly where people discover they needed them.</p>
""",
    'sources': [
        ('TSA &mdash; What can I bring? Medications',
         'https://www.tsa.gov/travel/security-screening/whatcanibring/items/medications'),
        ('FAA &mdash; Portable oxygen concentrators',
         'https://www.faa.gov/hazmat/packsafe/pocs'),
        ('TSA &mdash; Portable oxygen concentrators',
         'https://www.tsa.gov/travel/security-screening/whatcanibring/items/portable-oxygen-concentrators'),
        ('CDC &mdash; Travellers’ health: taking medicines abroad',
         'https://wwwnc.cdc.gov/travel/page/pack-smart'),
    ],
    'next': {'slug': 'cruise-medical',
             'title': 'What happens if you get sick on a cruise',
             'blurb': 'The ship’s doctor bills you, Medicare doesn’t travel, and the helicopter costs '
                      'more than the cruise.'},
}

# ------------------------------------------------------------ cruise medical
ARTICLES6['cruise-medical'] = {
    'title': 'What Happens If You Get Sick on a Cruise &mdash; The Second Half Guide',
    'eyebrow': 'Getting out there',
    'h1': 'What happens if you get sick on a cruise',
    'dek': 'There is a doctor on board. They bill you, your Medicare almost certainly doesn’t apply, and '
           'if you have to leave the ship the number gets very large very quickly.',
    'meta': '5 minute read &middot; Costs and coverage rules verified for 2026',
    'checked': CHECKED,
    'body': """      <p>Cruising suits a lot of people in this stage of life, for good reasons: you unpack once, the
      walking is optional, and there's a doctor on board.</p>

      <p>That last one is where a reasonable assumption goes wrong. There is indeed a medical centre.
      It's just not part of your fare, it doesn't work like a hospital at home, and the thing everybody's
      insurance is really for — getting off the ship — is the part with the eye-watering number attached.</p>

""" + facts('What it costs at sea', [
        ('A consultation', 'Roughly $100&ndash;$200 during posted hours.'),
        ('After hours', 'Commonly $300&ndash;$600 for the same visit outside clinic times.'),
        ('Tests and treatment', 'X-rays, bloods, IV fluids and medication are billed separately and add '
                                'up into the thousands quickly.'),
        ('An overnight in the infirmary', 'Roughly $1,000&ndash;$3,000 a day.'),
        ('Medical evacuation', '$15,000 to well over $200,000 depending on distance and aircraft. '
                               'Helicopter lifts from a ship commonly run $15,000&ndash;$50,000.'),
        ('How you pay', 'Charged to your onboard account, settled at the end of the cruise. You pay '
                        'first and claim later.'),
    ]) + """
      <h2>Why Medicare almost never helps here</h2>

      <p>Original Medicare generally doesn't cover care outside the United States. There's a narrow
      exception for a ship <em>within six hours of a US port</em> — which, on a Caribbean or Alaskan
      itinerary, describes very little of the trip and none of the interesting parts.</p>

      <p>So on a typical cruise you are, in practical terms, uninsured by Medicare from the moment you're
      properly at sea. Some Medigap plans include a foreign travel emergency benefit — 80% after a $250
      deductible, up to a <strong>$50,000 lifetime</strong> limit, and only for care beginning in the
      first 60 days of a trip. That's real help against a hospital bill and thin comfort against an air
      ambulance.</p>

      <blockquote class="pull">
        <p>The ship's doctor is a business, not a benefit. And the helicopter is not the cruise line's
        problem — it's yours.</p>
      </blockquote>

""" + AD_INLINE + """
      <h2>The evacuation is the actual risk</h2>

      <p>A ship's medical centre handles a great deal: minor injuries, infections, stabilising someone
      until port. What it cannot do is major surgery or sustained intensive care. If something serious
      happens, the answer is getting you to a hospital on land — by helicopter, by diverting the ship, or
      by disembarking you at the next port and arranging transport from there.</p>

      <p>Cruise contracts generally place the cost of that on the passenger. And the bill doesn't stop at
      the aircraft: you may then be in a hospital in a country you hadn't planned to visit, paying cash,
      possibly needing a medically supervised flight home afterwards — <em>repatriation</em>, which is
      separately expensive and separately covered, or not.</p>

      <p>This is the specific reason travel insurance exists for cruises, and why <strong>medical
      evacuation coverage matters more than trip cancellation</strong> for anyone on Medicare. Cancellation
      protects a deposit. Evacuation protects against a number larger than most people's annual income.</p>

      <h2>What to check before you sail</h2>

""" + check([
        'Confirm your policy includes <strong>emergency medical evacuation and repatriation</strong>, and '
        'look at the limits. Six figures is the level that matters.',
        'Check whether your <strong>Medigap plan</strong> has the foreign travel benefit &mdash; and '
        'remember $50,000 is a lifetime, not annual, limit.',
        'On <strong>Medicare Advantage</strong>, ask specifically about emergency care abroad. Plans vary '
        'and the answer is rarely on the summary page.',
        'Buy the policy <strong>soon after your first deposit</strong> if you have any ongoing condition '
        '&mdash; the pre-existing condition waiver has a short purchase window.',
        'Bring <strong>more medication than the itinerary needs</strong> and keep it in your cabin, not a '
        'checked bag.',
        'Bring a <strong>one-page medical summary</strong>: conditions, medications, doses, allergies, '
        'emergency contact. A ship’s doctor has no access to your records.',
    ]) + """
      <p>None of this is an argument against cruising. It suits this stage of life better than most kinds
      of travel, and the overwhelming majority of trips involve nothing worse than a sunburn.</p>

      <p>It's an argument for knowing that the doctor down the corridor is a private clinic, that your
      usual coverage stops at the shoreline, and that the one thing worth insuring properly is the
      helicopter you'll probably never need.</p>
""",
    'sources': [
        ('Medicare &mdash; Travel outside the U.S.',
         'https://www.medicare.gov/coverage/travel-outside-the-u.s.'),
        ('Medicare &mdash; How to compare Medigap policies',
         'https://www.medicare.gov/health-drug-plans/medigap/basics/compare-policies'),
        ('CDC &mdash; Cruise ship travel',
         'https://wwwnc.cdc.gov/travel/page/cruise-ship-travel'),
        ('U.S. Department of State &mdash; Cruise ship passengers',
         'https://travel.state.gov/content/travel/en/international-travel/before-you-go/travelers-with-special-considerations/cruise.html'),
    ],
    'next': {'slug': 'the-big-trip',
             'title': 'The big trip, done right',
             'blurb': 'The logistics that decide whether an ambitious trip at 68 works or falls apart.'},
}

# --------------------------------------------------------------- the big trip
ARTICLES6['the-big-trip'] = {
    'title': 'The Big Trip, Done Right &mdash; The Second Half Guide',
    'eyebrow': 'Getting out there',
    'h1': 'The big trip, done right',
    'dek': 'Not where to go &mdash; you know where you want to go. The logistics that decide whether the '
           'trip you have been imagining for years actually works.',
    'meta': '6 minute read &middot; Getting out there',
    'checked': CHECKED,
    'body': """      <p>There's no shortage of writing about where to go. Every publication has a list, and you almost
      certainly already know what's on yours — the place you've been meaning to see, the trip you said
      you'd take when there was time.</p>

      <p>What's harder to find is the unglamorous part: what actually makes an ambitious trip work at 65
      or 70, and what quietly wrecks it. Almost all of it is decided months before departure, by
      decisions that feel administrative at the time.</p>

      <h2>Sequence the list by difficulty, not by age</h2>

      <p>We've argued elsewhere that the <a href="/go-go-years">countdown framing of retirement travel</a>
      gets the variable wrong. It's worth restating here as a planning rule.</p>

      <p>Rank the trips you want by <strong>physical and logistical difficulty</strong> — altitude,
      walking distance, terrain, distance from a hospital, how often you change hotels. Do the hard ones
      first, not because time is short, but because difficulty is the thing that changes. A week in
      Rome can be made easier at 80 in a dozen ways. A trek at altitude cannot.</p>

""" + facts('The lead times that actually bind', [
        ('Passport', 'Renew if under a year of validity. Routine runs 4&ndash;6 weeks plus postage, and '
                     'many countries require six months beyond entry.'),
        ('Travel insurance', 'Buy within days of your first deposit if you have any ongoing condition '
                             '&mdash; the pre-existing waiver window is short and cannot be reopened.'),
        ('Visas', 'Weeks to months for some destinations, and several now require a passport valid well '
                  'beyond the trip.'),
        ('Vaccinations', 'Some travel vaccines need multiple doses over weeks. Start early.'),
        ('Medical equipment', 'Airline approval for an oxygen concentrator can take longer than you '
                              'expect. Sort it before booking, not after.'),
        ('Global Entry', 'Interview appointments can be months out at busy enrolment centres.'),
    ]) + """
      <blockquote class="pull">
        <p>Nearly everything that ruins a big trip was fixable in February and impossible in June.</p>
      </blockquote>

""" + AD_INLINE + """
      <h2>Design the itinerary around energy, not coverage</h2>

      <p>The commonest mistake on a once-in-a-lifetime trip is trying to see everything, because it feels
      like the only chance. It's also the reliable way to arrive home exhausted having enjoyed very
      little of it.</p>

      <p>A few structural choices make a large difference:</p>

      <ul>
        <li><strong>Fewer bases, longer stays.</strong> Changing hotels is the single most tiring thing in
        travel &mdash; packing, transfers, re-orienting. Three nights minimum anywhere; a week where you
        can. Day trips out from a base beat a new city every second night.</li>
        <li><strong>One thing a day.</strong> One museum, one site, one long lunch. Two is a stretch,
        three is a forced march, and the memory of a rushed day is worse than not going.</li>
        <li><strong>A day of nothing after the flight.</strong> Not a lost day &mdash; the thing that
        makes the following ten work.</li>
        <li><strong>Build in an empty afternoon each week.</strong> It absorbs the weather, the bad
        night's sleep, the thing that runs long.</li>
        <li><strong>Book the flight for arrival, not price.</strong> Landing at 6am after an overnight
        with no room until 3pm starts a trip badly for the sake of $80.</li>
      </ul>

      <h2>The things worth paying up for</h2>

      <p>On a trip you've waited years for, the value of money is different from an ordinary holiday, and
      there are two or three places where spending genuinely buys the trip rather than a nicer version
      of it:</p>

      <ul>
        <li><strong>A direct flight</strong>, or at least a long connection. The tight connection in an
        unfamiliar airport is where trips actually come apart.</li>
        <li><strong>Location over luxury.</strong> A modest hotel in the centre beats a smart one forty
        minutes out, every time, because it means you can go back and rest in the middle of the day.</li>
        <li><strong>A lift.</strong> Charming European buildings are famous for four flights of narrow
        stairs. Ask, specifically — &ldquo;is there an elevator&rdquo; is not a rude question.</li>
        <li><strong>Refundable bookings</strong>, when the trip is a year out and your health a year from
        now is a forecast rather than a fact.</li>
      </ul>

      <h2>Before you go</h2>

""" + check([
        'Get a <strong>medical opinion</strong> if the trip involves altitude, remoteness, long flights or '
        'a condition you manage. Ask directly what to plan for.',
        'Carry a <strong>one-page medical summary</strong> and a doctor’s letter listing medications, plus '
        'copies of your passport, insurance and prescriptions &mdash; stored separately.',
        'Confirm the trip has <strong>medical evacuation cover</strong> if it goes anywhere remote. This '
        'is the coverage that matters and the one people skip.',
        'Book <strong>airport assistance</strong> in advance if the terminal is the hard part. It is free '
        'and it changes the day.',
        'Start <strong>walking now</strong> if the trip involves walking. Eight weeks of building distance '
        'is worth more than any packing decision.',
        'Leave the <strong>itinerary and your insurance details</strong> with someone at home.',
    ]) + """
      <p>The trips people remember aren't usually the ones that covered the most ground. They're the ones
      where nothing went badly wrong and there was enough energy left to enjoy what they'd come for.</p>

      <p>That outcome is bought in advance, mostly with lead time and restraint, and hardly at all with
      the thing everyone spends their planning on — deciding where to go.</p>
""",
    'sources': [
        ('CDC &mdash; Travellers’ health', 'https://wwwnc.cdc.gov/travel'),
        ('U.S. Department of State &mdash; Country information',
         'https://travel.state.gov/content/travel/en/international-travel/International-Travel-Country-Information-Pages.html'),
        ('U.S. Department of State &mdash; Travellers with special considerations',
         'https://travel.state.gov/content/travel/en/international-travel/before-you-go/travelers-with-special-considerations.html'),
    ],
    'next': {'slug': 'airport-help',
             'title': 'The airport help you’re entitled to',
             'blurb': 'Free wheelchairs, escorts and screening support &mdash; the reason the getting-there '
                      'stops being the hard part.'},
}
