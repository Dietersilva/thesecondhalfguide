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
        ('What actually causes the injuries', 'Falls, trips and slips account for <strong>nearly '
                                              'half</strong> of all pickleball ER visits in the same '
                                              '2018&ndash;2025 analysis. A separate, earlier study focused '
                                              'specifically on seniors (60+, 2010&ndash;2019) found the '
                                              'leading diagnoses among that group were strains and sprains '
                                              '(33.2%) and fractures (28.1%).'),
        ('A gender gap in fracture risk', 'In that same senior-specific 2010&ndash;2019 study, women 60+ '
                                          'were <strong>3.7 times</strong> more likely than men 60+ to '
                                          'suffer a fracture, and <strong>9.3 times</strong> more likely to '
                                          'suffer a wrist fracture specifically.'),
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
        <p>Popularity explains part of the surge in injuries. It does not explain why older players make up
        such a lopsided share of them &mdash; that part is about the sport itself, and who is playing it.</p>
      </blockquote>

""" + AD_INLINE + """
      <h2>What tends to reduce the risk</h2>

      <p>Sports-medicine guidance for older recreational players who take up a new racquet sport commonly
      emphasizes the same handful of things: a proper warm-up, footwear built for lateral movement rather
      than running, and building up intensity gradually rather than playing at full pace from the first
      match. None of this is specific research about pickleball&rsquo;s exact injury mechanisms &mdash; it
      is the general standard for this kind of activity, applied to a sport that happens to fit the pattern
      closely.</p>

""" + check([
        'Court shoes built for <strong>lateral support</strong> are the standard recommendation over '
        'running shoes, which are built to grip going forward rather than stop side to side.',
        'A proper <strong>warm-up</strong> before playing, especially first thing in the morning or after '
        'sitting for a while, is standard sports-medicine advice for racquet sports generally.',
        'The fracture-risk gap between men and women 60+ in the data above is specific enough that it is '
        'worth knowing about, whatever you and your doctor already discuss about bone health.',
        'Falls, not overuse, drive most of these injuries &mdash; a bad step or a hard pivot, not gradual '
        'wear. That is why footwear and warm-up matter more here than in a lot of other exercise.',
    ]) + """
      <p>None of this is a reason to trade pickleball for the couch. The data above says something more
      specific: this particular sport, played by this particular age group, has a real and rising injury
      count behind the fun of it &mdash; worth knowing, not worth avoiding.</p>
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
        ('Sports &amp; Fitness Industry Association &mdash; 2026 Topline Participation Report',
         'https://sfia.org/research/u-s-pickleball-participation/'),
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
    'dek': 'Grandparents are increasingly central to family travel &mdash; including trips where the '
           'grandchild&rsquo;s parents stay home. The numbers behind it, and the one piece of paperwork '
           'that actually matters if the trip crosses a border.',
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
                              '(grandparent and grandchild only) are reported as two distinct categories in '
                              'the same survey data, not one blended trend. About <strong>11%</strong> of '
                              'parents surveyed say they plan a skip-gen trip in the next 12 months '
                              '&mdash; a steady share, not a sudden spike.'),
    ]) + """

      <p>The figures above come from the Family Travel Association&rsquo;s 2025 US Family Travel Survey, of
      1,596 US parents and grandparents surveyed in summer 2025 &mdash; self-reported survey responses, not
      a government dataset.</p>

      <h2>The one piece of paperwork that actually matters</h2>

      <p>The United States does not require a written permission letter for a minor to travel
      internationally with a grandparent rather than a parent. Individual <strong>destination
      countries</strong> often do, or airlines may ask for one at check-in even where the destination
      itself does not strictly require it. The State Department&rsquo;s own guidance is to check with the
      embassy or consulate of wherever the trip is headed, since the requirement is set by the destination,
      not by the US.</p>

      <p>Where a letter is expected, the standard version is simple: both parents sign a statement
      naming the grandparent and acknowledging the child is traveling with that person, with their
      permission, and it is preferably in English and notarized. The State Department&rsquo;s own guidance
      also says to always bring a copy of the child&rsquo;s birth certificate, or other evidence of the
      legal relationship, regardless of what a specific destination requires.</p>

      <blockquote class="pull">
        <p>Nobody plans a skip-gen trip around the paperwork. It is the one part of the trip that can
        actually stop it, and it is also the cheapest and easiest part to get right in advance.</p>
      </blockquote>

""" + AD_INLINE + """
      <h2>What to actually do before booking</h2>

""" + check([
        'If the trip crosses a border, <strong>contact the destination country&rsquo;s embassy or '
        'consulate</strong> directly to ask about consent-letter requirements &mdash; the State Department '
        'says this varies by country and the US does not set the rule.',
        'Where a letter is expected, both parents should sign it. A notarized letter in English is the '
        'commonly recommended form, even in places that do not explicitly require notarization.',
        'Always carry the grandchild&rsquo;s own <strong>passport</strong> and a copy of their '
        '<strong>birth certificate</strong> or other evidence of the family relationship &mdash; official '
        'guidance recommends this regardless of destination.',
        'A signed note authorizing emergency medical treatment is commonly recommended for a minor '
        'traveling without a parent, domestic trips included; state rules on who can authorize treatment '
        'vary, so check what applies where you live and where you are headed.',
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
