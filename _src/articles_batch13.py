#!/usr/bin/env python3
"""Thirteenth batch: two lighter, leisure-side pieces requested alongside the
serious cluster -- pickleball injury data and skip-gen travel. Both verified
against NEISS-based research / an industry survey and a State Department
travel-document rule, respectively. A third idea (TSA PreCheck vs Global
Entry pricing) was dropped after checking -- it duplicates /airport-security,
which already covers that comparison in detail."""

from build_articles import facts, check, AD_INLINE

ARTICLES13 = {}

CHECKED13 = '29 August 2026'

# ------------------------------------------------------------- pickleball
ARTICLES13['pickleball-injuries'] = {
    'title': 'Pickleball Is Sending More People to the ER Than It Used To &mdash; The Second Half Guide',
    'eyebrow': 'Facts &amp; thresholds',
    'h1': 'Pickleball is sending more people to the ER than it used to',
    'dek': 'The fastest-growing sport in America skews heavily toward this exact age group &mdash; and so '
           'do the injuries. The numbers, and what the research says actually reduces the risk.',
    'meta': '5 minute read &middot; Verified against NEISS-based research',
    'checked': CHECKED13,
    'body': """      <p>Pickleball&rsquo;s growth has been hard to miss &mdash; new courts, retiree leagues, a court
      repainted at the local park almost every season. What gets less coverage is the other number that
      grew alongside it: emergency room visits for pickleball injuries, concentrated overwhelmingly in
      players 50 and older.</p>

""" + facts('The numbers', [
        ('The ER trend', 'Estimated pickleball-related ER visits rose from about <strong>8,300 in '
                         '2018</strong> to more than <strong>31,000 in 2025</strong>, based on analyses of '
                         'the federal injury-surveillance data (NEISS) hospitals report from.'),
        ('Who is actually getting hurt', 'Adults <strong>50 and older</strong> accounted for more than '
                                         '<strong>4 in 5</strong> of the roughly 125,000 pickleball ER '
                                         'visits recorded from 2018 through 2025. <strong>Half</strong> of '
                                         'those were players 65 and older.'),
        ('It is not just more players', 'Among players 65+, the injury rate <strong>per 1,000 '
                                        'participants</strong> rose from 2.5 in 2019 to 6.8 in 2023 &mdash; '
                                        'a rate increase, not only a volume increase from more people '
                                        'playing.'),
        ('What actually causes the injuries', 'Falls, trips and slips account for <strong>nearly '
                                              'half</strong> of all pickleball injuries. Strains and '
                                              'sprains make up about 29%; fractures about 27% of emergency '
                                              'department visits.'),
        ('A gender gap in fracture risk', 'Women 60+ were roughly <strong>3 times</strong> more likely to '
                                          'suffer a fracture, and <strong>9 times</strong> more likely to '
                                          'fracture a wrist specifically, than men 60+ in the same '
                                          'NEISS-based analysis.'),
    ]) + """
      <h2>Why this sport, and why this age group</h2>

      <p>Pickleball asks for something tennis and golf mostly don&rsquo;t: short, hard bursts of lateral
      movement and quick direction changes on a small court, from a standing start, often after years away
      from any racquet sport. That combination &mdash; sudden pivots, a compact playing surface, players
      returning to activity after a long gap &mdash; is exactly the pattern behind most of the fall-related
      injuries in the data above. It is a genuinely good source of cardiovascular activity and, for many
      people in this age range, some of the only regular exercise they get. The injury pattern is not a
      reason to stop playing; it is a reason to know what actually drives it.</p>

      <blockquote class="pull">
        <p>The sport did not get more dangerous. More people your age started playing it, played it harder
        than their bodies were warmed up for, and the emergency rooms noticed before anyone else did.</p>
      </blockquote>

""" + AD_INLINE + """
      <h2>What the research points to</h2>

""" + check([
        'Court shoes with <strong>lateral support</strong>, not running shoes &mdash; running shoes are '
        'built to grip going forward, not for the side-to-side stopping pickleball actually demands.',
        'A real <strong>warm-up</strong> before playing, especially first thing in the morning or after '
        'sitting for a while. Cold muscles and tendons are a documented factor in racquet-sport strains.',
        'Know your own <strong>bone-density status</strong> if you are a woman over 60 &mdash; the '
        'fracture-risk gap in the data above is specific enough to be worth a conversation with your '
        'doctor, not a general caution.',
        'Backward movement and quick pivots are where falls concentrate. Playing a position and a pace '
        'that keeps you moving mostly forward and side to side reduces the highest-risk motion.',
        'Sitting out a game, or a day, when a knee or ankle already feels off is not overcaution &mdash; '
        'most of these injuries are acute (a fall or a bad step), not gradual wear.',
    ]) + """
      <p>None of this is a reason to trade pickleball for the couch. It is the same trade the site made
      with falls generally: knowing what actually causes the injury changes what you do about it more than
      general caution ever does.</p>
""",
    'sources': [
        ('KCUR/NPR &mdash; Missouri hospitals are seeing more pickleball injuries as sport&rsquo;s '
         'popularity surges',
         'https://www.kcur.org/health/2026-08-14/missouri-hospitals-are-seeing-more-pickleball-injuries-as-sports-popularity-surges'),
        ('PMC &mdash; Pickleball-Related Geriatric Fractures and Pediatric Equipment-Related Injuries Are '
         'Increasing in Emergency Departments Across the United States',
         'https://pmc.ncbi.nlm.nih.gov/articles/PMC12827217/'),
        ('PMC &mdash; Non-fatal senior pickleball and tennis-related injuries treated in United States '
         'emergency departments, 2010&ndash;2019',
         'https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8091689/'),
    ],
    'next': {'slug': 'falls',
             'title': 'Falls: the numbers, and what actually reduces them',
             'blurb': 'The same question asked about falls generally, not just on the pickleball court.'},
}

# ------------------------------------------------------------- skip-gen travel
ARTICLES13['skip-gen-travel'] = {
    'title': 'Skip-Gen Travel: Grandparents and Grandkids, No Parents &mdash; The Second Half Guide',
    'eyebrow': 'Facts &amp; thresholds',
    'h1': 'Skip-gen travel: grandparents and grandkids, no parents',
    'dek': 'A specific kind of family trip is growing fast &mdash; grandparent and grandchild, without the '
           'grandchild&rsquo;s parents along. The numbers behind it, and the one piece of paperwork that '
           'actually matters if the trip crosses a border.',
    'meta': '5 minute read &middot; Verified against industry survey and State Department guidance',
    'checked': CHECKED13,
    'body': """      <p>&ldquo;Skip-gen&rdquo; travel is a specific thing, distinct from the family reunion trip where
      three generations all go together: a grandparent takes a grandchild somewhere, and the child&rsquo;s
      parents stay home. It has a name now because it has gotten common enough to have one.</p>

""" + facts('The numbers', [
        ('How common it is', 'In the Family Travel Association&rsquo;s annual US Family Travel Survey, '
                             '<strong>71%</strong> of grandparents say they have taken a multigenerational '
                             'trip recently, and <strong>57%</strong> say they are planning one.'),
        ('Skip-gen is grandparent-led', 'On skip-gen trips specifically &mdash; grandchild, no parents '
                                        '&mdash; grandparents plan about <strong>75%</strong> of them and '
                                        'pay for about <strong>84%</strong>.'),
        ('Who pays on the wider category', 'Across multigenerational trips broadly, roughly '
                                           '<strong>half</strong> of grandparents pay for the entire trip '
                                           'themselves; most of the rest split costs with their adult '
                                           'children.'),
        ('Not the same trip', 'A multigenerational trip (everyone travels together) and a skip-gen trip '
                              '(grandparent and grandchild only) are reported as two distinct, both-growing '
                              'categories in the same survey data &mdash; not one blended trend.'),
    ]) + """
      <h2>The one piece of paperwork that actually matters</h2>

      <p>The United States does not require a written permission letter for a minor to travel
      internationally with a grandparent rather than a parent. Individual <strong>destination
      countries</strong> often do, or airlines may ask for one at check-in even where the destination
      itself does not strictly require it. The State Department&rsquo;s own guidance is to check with the
      embassy or consulate of wherever the trip is headed, since the requirement is set by the destination,
      not by the US.</p>

      <p>Where a letter is expected, the standard version is simple: both parents sign a statement
      naming the grandparent and acknowledging the child is traveling with that person, with their
      permission, and it is preferably in English and notarized. It costs nothing but a trip to a notary
      and a few weeks of lead time &mdash; the kind of thing that is easy to forget until it is the reason
      a family is pulled aside at a border.</p>

      <blockquote class="pull">
        <p>Nobody plans a skip-gen trip around the paperwork. It is the one part of the trip that can
        actually stop it, and it is also the cheapest and easiest part to get right in advance.</p>
      </blockquote>

""" + AD_INLINE + """
      <h2>What to actually do before booking</h2>

""" + check([
        'If the trip crosses a border, <strong>contact the destination country&rsquo;s embassy or '
        'consulate</strong> directly to ask about consent-letter requirements &mdash; do not assume US '
        'rules are the only ones that apply.',
        'Where a letter is expected, both parents should sign it, and getting it <strong>notarized</strong> '
        'is the safer default even when a destination does not explicitly require notarization.',
        'Carry the grandchild&rsquo;s own <strong>passport</strong> and, if relevant, proof of the family '
        'relationship (a birth certificate) &mdash; airline staff and border agents ask for this more '
        'often than families expect.',
        'For a domestic trip, the paperwork bar is much lower, but a signed permission note covering '
        'medical treatment authorization is still worth having in case of an urgent care visit.',
        'Book with the grandparent as the primary contact wherever the itinerary allows it, since that is '
        'who will be asked to produce documentation if anything is questioned.',
    ]) + """
      <p>The trend itself is the easy part &mdash; grandparents already know whether they want to take a
      grandchild somewhere. The paperwork is the part that decides whether the plan survives contact with
      an actual border.</p>
""",
    'sources': [
        ('Family Travel Association &mdash; 2025 US Family Travel Survey',
         'https://www.familytravel.org/assets/pdf/FTA-Survey2025-Report/'),
        ('U.S. Department of State &mdash; Minors traveling abroad',
         'https://travel.state.gov/en/international-travel/planning/personal-needs/minors.html'),
        ('USAGov &mdash; International travel documents for children',
         'https://www.usa.gov/travel-documents-children'),
    ],
    'next': {'slug': 'the-big-trip',
             'title': 'The big trip, done right',
             'blurb': 'Not where to go — the logistics that decide whether the trip you have been imagining actually works.'},
}
