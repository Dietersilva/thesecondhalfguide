#!/usr/bin/env python3
"""Thirtieth batch (Friday drafts, 24 November 2026): the Audubon Christmas Bird Count
and the TSA rules for flying with a grandchild.

Sources opened directly this session: audubon.org (CBC overview, About, Join or start,
Explore data, 126th CBC summary), the Audubon CBC Feeder Watching Guidance PDF (read
from the saved copy), cbc.audubon.org, fws.gov, tsa.gov (identification page, traveling
with children page, the 8 July 2025 shoes-off release).

Deliberately omitted because it could not be confirmed from an agency page: Great
Backyard Bird Count dates for 2027; family-seating rules (the DOT page returned an
access error); any figure for airline policies."""

from build_articles import facts, check, AD_INLINE

ARTICLES30 = {}

CHECKED30 = '24 November 2026'

# ------------------------------------------------------------- Christmas Bird Count
ARTICLES30['christmas-bird-count'] = {
    'title': 'The Christmas Bird Count: How to Join From Your Backyard &mdash; The Second Half Guide',
    'eyebrow': 'Facts &amp; dates',
    'h1': 'The Christmas Bird Count: how to join from your backyard',
    'dek': 'The count began in 1900 as an alternative to a holiday shooting contest. It runs every winter '
           'from 14 December to 5 January, it is free, and a feeder count can be done from your own yard if it sits inside a count circle '
           'and the local compiler has agreed.',
    'meta': '6 minute read &middot; Checked against Audubon&rsquo;s own pages and its feeder-watching guidance',
    'checked': CHECKED30,
    'body': """      <p>On Christmas Day in 1900, the ornithologist Frank Chapman proposed an alternative to a holiday
      tradition called the Side Hunt, in which participants competed to see who could shoot the most birds
      and small mammals. Instead of shooting them, go out and count them. That first year, according to
      Audubon, 27 birders conducted 25 counts in the United States and Canada and tallied around 90
      species.</p>

      <p>The count has taken place every winter since 1900. This season it runs between
      <strong>14 December 2026 and 5 January 2027</strong>. Participation is free, and Audubon says it is
      open to bird enthusiasts of any level.</p>

""" + facts('The Christmas Bird Count at a glance', [
        ('14 Dec 2026 &ndash; 5 Jan 2027', 'The window. Each local count picks a single day inside it.'),
        ('Free', 'Audubon: participation is free and open to bird enthusiasts of any level.'),
        ('15 miles wide', 'The size of each count circle, per Audubon.'),
        ('1900', 'First count, on Christmas Day: 27 birders, 25 counts, around 90 species.'),
        ('126th count (2025&ndash;26)', '85,222 participants, 2,701 circles, 43,815,563 birds, 21 countries or territories.'),
        ('10,993', 'Feeder counters in the 2025&ndash;26 count, out of 85,222 participants.'),
        ('More than 300', 'Peer-reviewed articles published using the count&rsquo;s data.'),
    ]) + """
      <h2>How a count is organized</h2>

      <p>It is not one event. It is more than 2,700 local counts, each inside a designated circle on the
      map that Audubon says is 15 miles wide, and each held on one day inside the window. A local organizer
      called a compiler picks the day. Audubon&rsquo;s pages do not list the 2026&ndash;27 dates; your
      circle&rsquo;s compiler sets its own.</p>

      <p>To take part you register and coordinate in advance with that local leader. Audubon&rsquo;s Circle
      Finder locates counts near you. Contact the compiler of a nearby circle to confirm whether your own
      address can be included in a feeder count.</p>

      <h2>Two ways to take part</h2>

      <p><strong>A field count</strong> means surveying an area during daylight, alone or in a group. Some
      counts also include night surveys.</p>

      <p><strong>A feeder count</strong> is the one that can be done from home. Audubon&rsquo;s wording is
      that you count &ldquo;all the birds you see or hear from your own backyard or local park at a
      stationary bird feeder within a CBC circle,&rdquo; and that no binoculars or hiking are required. Two
      conditions follow. The feeder has to be inside a circle, and all of your counting has to fall within
      the 24-hour period that is your circle&rsquo;s count day. Feeder counters were 10,993 of the 85,222
      participants last season, about one in eight, by the site&rsquo;s own arithmetic.</p>

""" + AD_INLINE + """
      <h2>The counting rule that surprises people</h2>

      <p>Audubon&rsquo;s feeder-watching guidance asks for the largest number of each species you see or hear
      at the same time, not a running total. Its example: if the first time you look you see one Northern
      Cardinal and two Blue Jays, and you hear one chickadee, you write down those numbers. If later you see
      two cardinals and three Blue Jays at once, you replace the earlier numbers with the larger ones. The
      guidance is direct: &ldquo;Do not add your counts together.&rdquo;</p>

      <p>The reason is that a Blue Jay can visit the feeder twenty times. Added together, one bird becomes
      twenty. Audubon says the method means you will never report an individual bird more than once, and
      that it matters most for jays, chickadees and nuthatches, which cache food and make repeated
      visits.</p>

      <p>Three details from the same guidance:</p>

      <ul>
        <li><strong>Count what is nearby, not only what is on the feeder.</strong> If two House Sparrows are
        on the feeder and six more are waiting in a bush, count all eight. Birds that simply fly over, such
        as Canada Geese, are not counted.</li>
        <li><strong>Record only on count day,</strong> between midnight and 11:59 p.m. for your circle.</li>
        <li><strong>Record your effort.</strong> Note the number of observers and the time you spent
        actually watching, to the nearest quarter hour. If you are working in the kitchen and can see the
        feeder for part of an hour, record only that part. Audubon calls effort data equally important to
        the species counts.</li>
      </ul>

      <p>The guidance also asks you to confirm your location with the compiler or sector leader before count
      day, so that field counters in the area do not count the same birds.</p>

      <h2>The part nobody mentions: the data is the point</h2>

      <p>It is easy to read this as a hobby with a holiday theme. It is a long-running dataset. Audubon says
      four types of data are collected during every count: dates and times, observer effort, weather, and
      the bird observations. Effort and weather are what let scientists compare a snowy afternoon with two
      observers to a clear day with ten.</p>

      <p>Audubon reports that more than 300 peer-reviewed articles have been published using the
      data, and says it helped reveal dramatic declines in grassland birds such as the Eastern Meadowlark
      and the Bobolink. The U.S. Fish and Wildlife Service describes it the same way: the data is compiled
      and used to learn about long-term bird trends, and has appeared in reports such as the State of the
      Birds Report.</p>

      <p>That explains why the rules are strict. Audubon&rsquo;s feeder guidance gives the reason in a
      sentence: for the data to be scientifically valid, participants must follow the same counting
      procedure for all species. Even when the male and the female of a species look different and appear at
      different times, they are counted as two only if seen together.</p>

      <h2>A small difference between two official histories</h2>

      <p>Audubon describes 27 birders conducting 25 counts. The Fish and Wildlife Service describes the first
      count as taking place in 25 locations, from California to Canada. Both report about 90 species. The
      two accounts do not spell out how the observer count and the location count relate, so this article
      gives each as its source states it.</p>

      <h2>What the rule means in practice</h2>

""" + check([
        'The window is <strong>14 December 2026 to 5 January 2027</strong>. Each circle counts on one day '
        'inside it, set by its compiler.',
        'Registration and advance coordination with a local leader are required. Audubon&rsquo;s Circle '
        'Finder shows counts near you.',
        'A feeder count must be inside a circle and within the circle&rsquo;s 24-hour count day.',
        'Record the <strong>largest number seen or heard at the same time</strong> for each species. Do not '
        'add visits together. Record the time you spend watching and the number of observers.',
        'Audubon&rsquo;s pages do not say whether a compiler can decline a particular feeder, so this '
        'article does not.',
    ]) + """
      <p>For readers who would like to try it, the first step is the Circle Finder and a call or message to
      the nearest circle&rsquo;s compiler. Audubon lists cbcadmin@audubon.org for general support. Researchers
      who plan to use the data in published work are asked to notify Audubon through its online data-use
      form.</p>
""",
    'sources': [
        ('Audubon &mdash; Christmas Bird Count',
         'https://www.audubon.org/community-science/christmas-bird-count'),
        ('Audubon &mdash; About the Christmas Bird Count',
         'https://www.audubon.org/community-science/christmas-bird-count/about-christmas-bird-count'),
        ('Audubon &mdash; Join or start a Christmas Bird Count',
         'https://www.audubon.org/community-science/christmas-bird-count/join-or-start-christmas-bird-count'),
        ('Audubon &mdash; Circle Finder', 'https://cbc.audubon.org/en/join'),
        ('Audubon &mdash; Summary of the 126th Christmas Bird Count (2025&ndash;2026)',
         'https://www.audubon.org/community-science/christmas-bird-count/summary-of-126th-cbc-2025-2026'),
        ('Audubon &mdash; Explore Christmas Bird Count data',
         'https://www.audubon.org/community-science/christmas-bird-count/explore-christmas-bird-count-data'),
        ('Audubon &mdash; Christmas Bird Count Feeder Watching Guidance (PDF)',
         'https://media.audubon.org/2025-11/CBC%20Feeder%20Watching%20Guidance.pdf'),
        ('U.S. Fish and Wildlife Service &mdash; &rsquo;Tis the season for the Christmas Bird Count',
         'https://www.fws.gov/story/tis-season-christmas-bird-count'),
    ],
    'next': {'slug': 'skip-gen-travel',
             'title': 'Skip-gen travel',
             'blurb': 'Grandparents and grandkids on a trip with no parents: what the survey shows and the '
                      'paperwork that can stop it.'},
}

# ---------------------------------------------------------- Flying with a grandchild
ARTICLES30['flying-with-a-grandchild-tsa'] = {
    'title': 'Flying With a Grandchild: What TSA Asks of the Child, and of You &mdash; The Second Half Guide',
    'eyebrow': 'Travel &amp; rules',
    'h1': 'Flying with a grandchild: what TSA asks of the child, and of you',
    'dek': 'For a domestic flight, TSA does not require children under 18 to show ID. Adults must. '
           'Airlines may have their own rules.',
    'meta': '6 minute read &middot; Domestic flights only &middot; Checked against TSA&rsquo;s own pages',
    'checked': CHECKED30,
    'body': """      <p>The most common question before a first flight with a grandchild is about paperwork. For a
      domestic trip, TSA&rsquo;s answer is short: the child does not need identification, and you do.
      That is the TSA checkpoint rule for domestic travel. Airlines may have their own requirements.</p>

      <p>On its identification page, TSA states: &ldquo;TSA does not require children under 18 to provide
      identification when traveling within the United States.&rdquo; It adds that unaccompanied minors who
      are eligible for TSA PreCheck must show an acceptable ID to receive expedited screening, and it tells
      travelers to contact the airline with questions about its own ID requirements for people under 18.
      The same page says adult passengers 18 and older must show valid identification at the checkpoint in
      order to travel.</p>

      <p>That second sentence applies to every adult, grandparent or not, whether or not a child is with
      them.</p>

""" + facts('What TSA says about children at a domestic checkpoint', [
        ('Child under 18', 'No ID required for travel within the United States.'),
        ('Adult 18 and older', 'Valid identification required at the checkpoint.'),
        ('Modified screening', 'For children who appear to be 12 years old and younger.'),
        ('Standard screening', 'For children 13 years and older.'),
        ('Liquids over 3.4 oz', 'Formula, breast milk, toddler drinks and baby or toddler food may exceed 3.4 oz and need not fit in a quart bag.'),
        ('Strollers, car seats', 'Screened by X-ray; equipment that does not fit gets a visual or physical inspection.'),
        ('Separation', '&ldquo;Children will not be separated from their parent/guardian.&rdquo;'),
        ('Questions', 'TSA Cares, (855) 787-2227, 72 hours before travel.'),
    ]) + """
      <h2>The line between 12 and 13</h2>

      <p>TSA says it has developed modified screening procedures for children who appear to be 12 years old
      and younger, and that standard procedures apply to children 13 and older. The word is
      &ldquo;appear.&rdquo; TSA&rsquo;s public page does not spell out how officers resolve every borderline
      case.</p>

      <h2>What happens to a child at the checkpoint</h2>

      <ul>
        <li><strong>Walking.</strong> Children who can walk through the metal detector may go through
        separately from the adult. Infants and small children may be carried through it.</li>
        <li><strong>The body scanner.</strong> TSA says that if a child can remain standing in the required
        position for 5 seconds, the child may be screened through advanced imaging technology. It also says
        an adult who is carrying an infant or child may not be screened by that technology.</li>
        <li><strong>An alarm.</strong> A child 12 or under who alarms has a chance to go through again, or
        the officer may use other procedures to resolve the alarm and reduce the need for a pat-down.</li>
        <li><strong>Equipment.</strong> Strollers, umbrella strollers, baby carriers, car seats, booster
        seats and backpacks must be screened by X-ray. TSA says to take infants and children out of
        strollers and car seats and carry them through the metal detector. Equipment that does not fit
        through the X-ray machine gets a visual or physical inspection.</li>
        <li><strong>Who the officer talks to.</strong> TSA says officers will consult parents or the
        traveling guardian about the child&rsquo;s screening, and that children will not be separated from
        their parent or guardian. The page does not separately define every grandparent&rsquo;s status. If
        that is a concern, ask TSA before you travel.</li>
      </ul>

""" + AD_INLINE + """
      <h2>Formula, drinks and food for a young grandchild</h2>

      <p>The usual rule for carry-on liquids is a quart bag of containers 3.4 oz or smaller. TSA makes an
      exception for children: formula, breast milk, toddler drinks and baby or toddler food, including puree
      pouches, may be carried in amounts over 3.4 oz and do not need to fit in the quart bag. You remove them
      from the carry-on for separate screening and tell the officer. TSA says it may test liquids for
      explosives or prohibited items. If you do not want the items X-rayed or opened, you notify the officer.
      The page adds that additional screening procedures may be required to resolve alarms, so declining
      does not end screening.</p>

      <p>Ice packs, freezer packs, gel packs and liquid-filled teethers are allowed in carry-ons. The page
      gives only the over-3.4-oz wording and sets no maximum quantity, so this article does not supply
      one.</p>

      <h2>Where TSA sends questions</h2>

      <p>TSA&rsquo;s page tells travelers to call TSA Cares at (855) 787-2227 72 hours before traveling with
      questions about screening policies, procedures and what to expect at the checkpoint. It also lists
      AskTSA, which it describes as available 365 days a year, with live assistance from 8 a.m. to 6 p.m.
      Eastern. Hours can change, so confirm them on TSA&rsquo;s page before you rely on them. Screening a
      child is a judgment made by an officer on the day, which is why TSA points people to a person rather
      than a table.</p>

      <h2>The part nobody mentions</h2>

      <p><strong>Your airline&rsquo;s rules are separate from TSA&rsquo;s.</strong> TSA&rsquo;s own page sends
      travelers to the airline for questions about ID requirements for people under 18. TSA does not
      address whether an airline wants a letter or other authorization from a child&rsquo;s parents, and
      nothing on the TSA pages makes one a TSA requirement. Before departure, confirm the airline&rsquo;s own
      rules for a child traveling with an adult who is not a parent, and ask the child&rsquo;s parents what
      they want you to carry.</p>

      <p><strong>Seating together is an airline matter.</strong> Whether an airline will seat an adult beside
      a child at no extra charge is not something TSA&rsquo;s pages cover, and this article gives no figure
      for it. Check the airline&rsquo;s own policy when you book.</p>

      <p><strong>One line on TSA&rsquo;s children page is out of date.</strong> The page still says children
      12 and under can leave their shoes, light jackets and headwear on. On 8 July 2025 TSA announced that
      passengers traveling through domestic airports can keep their shoes on at checkpoints, so shoes no
      longer distinguish children. The same release says other aspects of TSA&rsquo;s layered security
      approach still apply, so officers can still ask for additional screening.</p>

      <p><strong>International trips are different.</strong> Everything above is about domestic flights. For a
      trip that crosses a border, see <a href="/skip-gen-travel">the page on skip-generation travel</a>
      for the paperwork a destination can require. For the adult&rsquo;s own ID, see
      <a href="/tsa-confirmid-fee">the page on the $45 airport ID fee</a>.</p>

      <h2>What the rule means in practice</h2>

""" + check([
        'TSA does not require ID for a child under 18 on a <strong>domestic</strong> flight. Airlines may '
        'have their own ID requirements.',
        'An adult 18 or older must show valid identification at the checkpoint.',
        'Children who appear 12 or younger get modified screening; 13 and older get standard screening.',
        'Formula, breast milk, toddler drinks and baby or toddler food over 3.4 oz are allowed outside the '
        'quart bag. Remove them for separate screening and tell the officer.',
        'Call TSA Cares at (855) 787-2227 72 hours ahead for questions about screening.',
    ]) + """
      <p>This is what TSA says. Airline policies may differ, and TSA&rsquo;s pages carry no publication
      date, so check the current version in the week you fly.</p>
""",
    'sources': [
        ('TSA &mdash; Identification', 'https://www.tsa.gov/travel/security-screening/identification'),
        ('TSA &mdash; Traveling with children',
         'https://www.tsa.gov/travel/tsa-cares/traveling-children'),
        ('TSA &mdash; DHS to end &ldquo;shoes-off&rdquo; travel policy (8 July 2025)',
         'https://www.tsa.gov/news/press/releases/2025/07/08/dhs-end-shoes-travel-policy'),
    ],
    'next': {'slug': 'skip-gen-travel',
             'title': 'Skip-gen travel',
             'blurb': 'The paperwork that matters when a grandparent takes a grandchild across a border.'},
}
