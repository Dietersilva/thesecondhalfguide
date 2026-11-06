#!/usr/bin/env python3
"""Twenty-seventh batch: two pieces from 6 November 2026 that bear on readers
55-70 and are not covered elsewhere on the site -- the Medicaid work
(community-engagement) requirement that states must start by 1 January 2027 for
expansion adults 19 to 64 (CMS issued its interim final rule on 1 June 2026),
and the WISeR model that has put prior authorization into traditional Medicare in
six states since January 2026.

cms.gov, medicaid.gov and congress.gov were not read directly: verified per
CLAUDE.md section 2 by agreement across independent reporting that traces to the
agency. Deliberately omitted because only one source gave it, or sources
conflicted: how many expansion states there are, a 90-day window to regain
Medicaid coverage, whether people denied Medicaid over the requirement can still
get Marketplace premium credits, the exact WISeR service count (sources say 13
to 17), the WISeR appeal route, a 3-day decision deadline, the WISeR vendor
names, and any state's early start."""

from build_articles import facts, check, AD_INLINE

ARTICLES27 = {}

CHECKED27 = '6 November 2026'

# ------------------------------------------------------- Medicaid work requirement
ARTICLES27['medicaid-work-requirements'] = {
    'title': 'Medicaid Work Requirements Start 2027: What the Rule Says for Ages 55&ndash;64 '
             '&mdash; The Second Half Guide',
    'eyebrow': 'Facts &amp; thresholds',
    'h1': 'Medicaid work requirements start 1 January 2027: what the rule says for ages 55 to 64',
    'dek': 'Adults 19 to 64 covered through Medicaid expansion will have to show 80 hours a month of '
           'work, study or service, or an exemption. The deadline, what counts, and what happens after '
           'a missed month.',
    'meta': '6 minute read &middot; Checked against CMS&rsquo;s rule and independent reporting that '
            'cites it',
    'checked': CHECKED27,
    'recheck': {'due': '2027-01-05', 'why': 'The requirement begins 1 January 2027 -- confirm which states '
                'started on time, any state granted a delay, and any court action on the CMS rule.'},
    'body': """      <p>Most coverage of Medicaid work requirements is about younger adults. The age range in the
      rule is 19 to 64. That includes a lot of readers of this site: people in their late fifties and early
      sixties who left a job, have no employer coverage, and are covered through their state&rsquo;s
      Medicaid expansion while they wait for Medicare at 65.</p>

      <p>The requirement is not new this week. CMS issued the rule that tells states how to apply it on
      <strong>1 June 2026</strong>, and it was published in the Federal Register two days later. The date
      that matters is the one Congress set: states must have it running by <strong>1 January 2027</strong>.
      That is eight weeks away.</p>

""" + facts('The Medicaid work requirement, in numbers', [
        ('1 January 2027', 'The date states must begin applying the requirement. States may start earlier.'),
        ('1 June 2026', 'When CMS issued its interim final rule on how states apply it.'),
        ('Ages 19 to 64', 'The adults covered, primarily people enrolled through Medicaid expansion.'),
        ('80 hours a month', 'The qualifying activity needed: work, community service, a work program, or '
                             'at least half-time education.'),
        ('$580 a month', 'Earning at least this much counts instead of the hours. It is the federal minimum '
                         'wage times 80 hours.'),
        ('30 days', 'The time a person gets to respond to a notice of noncompliance before coverage ends.'),
        ('31 December 2028', 'The latest a state could delay, if it receives a good-faith-effort exemption.'),
    ]) + """
      <h2>Who is covered, and where it stops</h2>

      <p>The requirement applies to adults in the Medicaid expansion group, the people who qualify
      because their state extended Medicaid to adults with incomes up to a set level. It does not apply
      to every person with Medicaid. The age range in the rule ends at 64. A person who turns 65 is outside
      it, which is a reminder that for many readers the requirement would apply for a few years at most
      before Medicare begins. How that handoff works is on
      <a href="/medicare-enrollment">the Medicare enrollment page</a>.</p>

      <p>Medicaid is run by states, so the details of how a month is verified, what paperwork is
      accepted and when the first notices go out differ from state to state. States are also allowed to
      begin earlier than January. And a state that cannot be ready can apply for a temporary
      good-faith-effort exemption, which delays implementation until no later than 31 December 2028.
      Whether a given state has done so is a question for the state&rsquo;s Medicaid agency.</p>

      <h2>What counts toward the 80 hours</h2>

      <p>The rule counts several kinds of activity: employment, community service, participation in a
      work program, and education at least half-time. Earning at least $580 a
      month counts in place of the hours, which is the federal minimum wage of $7.25 multiplied by 80.</p>

      <p>Compliance is checked when a person applies, and states may look back over one to three months
      before the application month to see whether the requirement was met. Between renewals, reporting
      says the rule gives people some flexibility about which months they show the activity.</p>

      <blockquote class="pull">
        <p>The question is not whether you worked this week. It is whether the state can verify 80 hours,
        or an exemption, for the month it checks.</p>
      </blockquote>

""" + AD_INLINE + """
      <h2>Who is exempt</h2>

      <p>The exemptions listed in coverage of the rule include parents or caregivers of a child 13 or
      younger or of a person with a disability, veterans with a total disability rating, people who are
      medically frail, former foster youth, and American Indians and Alaska Natives. Residence in a
      federally identified disaster area is also reported as an exemption by one source. The rule limits how much a
      person can rely on their own statement to show medical frailty, which means the state may ask for
      documentation.</p>

      <p>There is no exemption based on age alone listed in the coverage reviewed for this page, including
      for people in their late fifties or early sixties. Anyone who thinks an exemption may apply should
      read the state&rsquo;s own list, because the rule leaves states to build the process and
      the evidence they accept.</p>

      <h2>What happens when a month is missed</h2>

      <p>If a state cannot verify that a person met the requirement or qualified for an exemption, it must
      send a notice and give the person 30 days to show compliance. Coverage continues during those
      30 days, and the state has to check whether the person qualifies another way before ending it.
      Coverage ends only if the window closes without a satisfactory response. The days are calendar
      days, and the termination can take effect after the window rather than the day after.</p>

      <p>Two details were left out of this page because sources disagreed. One is whether a person who
      loses Medicaid over the requirement can get a Marketplace premium tax credit. Reporting is split,
      and the answer should come from the CMS rule or a state notice. The other is a reported 90-day
      window to regain coverage without a new application, which only one guide mentioned. Neither
      should be assumed.</p>

      <h2>Where this sits among the other changes</h2>

      <p>For a reader who is 60 and between jobs, this is one piece of a larger set of coverage dates.
      The Marketplace side is on <a href="/aca-subsidy-cliff">the ACA subsidy cliff page</a>, the
      employer-coverage side is on <a href="/cobra-medicare-trap">the COBRA page</a>, and the programs
      that help once a person has Medicare are on <a href="/medicare-savings">the Medicare Savings
      Programs page</a>. This page is about the one that turns on a monthly record.</p>

      <h2>What&rsquo;s worth keeping in mind</h2>

""" + check([
        'States must begin applying the requirement by <strong>1 January 2027</strong>; some may start '
        'earlier, and a state with a good-faith exemption can delay to the end of 2028.',
        'It covers expansion adults <strong>19 to 64</strong>: <strong>80 hours a month</strong> of work, '
        'service, a work program or half-time school, or <strong>$580 a month</strong> in earnings.',
        'Exemptions include caregivers of a child 13 or younger, medically frail people, veterans with a '
        'total disability rating, former foster youth and American Indians and Alaska Natives. Age alone '
        'is not listed.',
        'A missed or unverified month brings a notice and <strong>30 days</strong> to respond before coverage '
        'ends.',
        'The details of verification vary by state. Your state&rsquo;s Medicaid agency is the place to '
        'check yours.',
    ]) + """
      <p>The deadline is set by federal law and the process is set by each state. For anyone covered
      this way, the practical question is what the state will ask to see, and when it will ask.</p>
""",
    'sources': [
        ('CMS &mdash; Medicaid community engagement requirement interim final rule with comment period (fact sheet)',
         'https://www.cms.gov/newsroom/fact-sheets/medicaid-community-engagement-requirement-certain-individuals-interim-final-rule-comment-period-cms'),
        ('Medicaid.gov &mdash; Community engagement requirement for certain individuals (interim final rule briefing)',
         'https://www.medicaid.gov/medicaid/downloads/ce-requirement-ifc-deck.pdf'),
        ('Ballotpedia News &mdash; CMS releases interim final rule for Medicaid work requirements, defines medical '
         'frailty exemption (12 June 2026)',
         'https://news.ballotpedia.org/2026/06/12/cms-releases-interim-final-rule-for-medicaid-work-requirements-defines-medical-frailty-exempt/'),
        ('Center on Budget and Policy Priorities &mdash; A guide to reducing coverage losses through effective '
         'implementation of Medicaid&rsquo;s new work requirement',
         'https://www.cbpp.org/research/health/a-guide-to-reducing-coverage-losses-through-effective-implementation-of-medicaids'),
        ('Foley Hoag &mdash; CMS issues interim final rule imposing Medicaid work requirements for expansion '
         'populations (June 2026)',
         'https://foleyhoag.com/news-and-insights/publications/alerts-and-updates/2026/june/cms-issues-interim-final-rule-imposing-medicaid-work-requirements-for-expansion-populations/'),
        ('NACo &mdash; CMS issues interim final rule on Medicaid community engagement requirements',
         'https://www.naco.org/news/cms-issues-interim-final-rule-medicaid-community-engagement-requirements'),
    ],
    'next': {'slug': 'medicare-savings',
             'title': 'The Medicare help millions qualify for and never claim',
             'blurb': 'Four Medicare Savings Programs and Extra Help, and the income limits most people '
                      'overestimate.'},
}

# ------------------------------------------------------------- WISeR
ARTICLES27['wiser-prior-authorization'] = {
    'title': 'Prior Authorization Has Reached Traditional Medicare in Six States &mdash; The Second Half Guide',
    'eyebrow': 'Facts &amp; thresholds',
    'h1': 'Prior authorization has reached traditional Medicare in six states',
    'dek': 'A CMS pilot that began in January requires approval before certain Part B services in Arizona, '
           'New Jersey, Ohio, Oklahoma, Texas and Washington. Medicare Advantage is not part of it.',
    'meta': '6 minute read &middot; Checked against CRS, KFF and independent reporting on the CMS model',
    'checked': CHECKED27,
    'body': """      <p>One of the standard arguments for choosing Original Medicare over an Advantage plan is
      that Original Medicare does not make you ask permission first. In six states that has been less
      true since January. The pilot is called WISeR, short for Wasteful and Inappropriate Service
      Reduction, and it brings prior authorization into traditional Medicare for a list of Part B
      services.</p>

      <p>This is not new this week. It began in January 2026, and it runs for six years. It is worth a page
      during Annual Enrollment because the choice between Original Medicare and an Advantage plan is
      being made now, and one of the usual talking points has an exception.</p>

""" + facts('The WISeR model, in numbers', [
        ('Six states', 'Arizona, New Jersey, Ohio, Oklahoma, Texas and Washington.'),
        ('January 2026', 'When the model began. Prior authorization requests started in early January for '
                         'services later that month.'),
        ('31 December 2031', 'When the model is scheduled to end, per the Congressional Research Service.'),
        ('Original Medicare only', 'Medicare Advantage plans are not part of WISeR.'),
        ('About 13 to 17', 'The number of service categories, depending on the source. KFF&rsquo;s analysis '
                           'notes CMS delayed adding two services originally scheduled for 2026.'),
        ('10% to 20%', 'The share of savings tied to denied care that the American Hospital Association says '
                       'participating vendors receive.'),
    ]) + """
      <h2>What it is</h2>

      <p>Prior authorization means a provider has to get approval before delivering a service, or
      Medicare may not pay for it. Advantage plans have used it for years. Original Medicare mostly has
      not, with exceptions such as some equipment, covered on
      <a href="/dme-prior-authorization">the equipment prior authorization page</a>. WISeR extends the
      idea to a set of Part B services for people living in the six states, and it is a CMS Innovation
      Center model, which means a time-limited test and not a permanent rule.</p>

      <p>It applies to people in Original Medicare who live in those states. It does not apply to Medicare
      Advantage members, who are already subject to their own plans&rsquo; rules. Whether it will be
      extended to other states or services is not announced. KFF notes CMS could expand it, and no
      expansion for January 2027 turned up in the reporting checked here.</p>

      <h2>Which services</h2>

      <p>The list is a set of Part B services chosen as vulnerable to overuse. KFF&rsquo;s description names
      skin substitutes used in treating severe or chronic wounds, electrical nerve stimulator implants and
      certain orthopedic pain services such as cervical fusion and epidural steroid injections. Other
      summaries include arthroscopy for knee osteoarthritis. Sources count the categories differently,
      from about 13 to 17, so this page does not give a single number. The authoritative list is the
      provider guide CMS publishes, and it can change during the model.</p>

      <blockquote class="pull">
        <p>The rule is not that everything in Original Medicare now needs approval. It is that a specific
        list does, in six specific states.</p>
      </blockquote>

""" + AD_INLINE + """
      <h2>Who decides, and how the decision-makers are paid</h2>

      <p>Each state has one participating technology company that reviews requests. Reporting says the
      companies use artificial intelligence to help with review and that licensed clinicians make every
      decision not to approve a request. Vendors are not paid a flat fee. CMS describes a performance-based
      share of savings, and the American Hospital Association puts it at 10% to 20% of the savings
      associated with denied care. Critics point to that as an incentive to deny, and supporters, such as
      America&rsquo;s Physician Groups, say the model could reduce costs that fall on taxpayers and
      beneficiaries. Both positions are on the record. The page does not take one.</p>

      <p>Providers submit the requests, not patients. A patient&rsquo;s practical contact with the model is
      often indirect: a scheduled procedure waiting for an approval, or a denial that the provider has to
      pursue. How a decision not to approve can be challenged was not settled in the reporting reviewed,
      and the American Hospital Association has asked CMS to let patients appeal. The page leaves the
      process out for that reason.</p>

      <h2>What is contested</h2>

      <p>The model has drawn criticism from advocacy groups and some members of Congress. Two
      representatives introduced the Seniors Deserve SMARTER Care Act, which would repeal it. No vote on
      that bill turned up. The Center for Medicare Advocacy has called early reports on the model troubling, which is the
      view of an advocacy group and not a measured finding. The model&rsquo;s own results are not in
      yet.</p>

      <h2>Where this fits in the enrollment choice</h2>

      <p>None of this is a recommendation. It is one fact that belongs next to the others in the choice
      covered on <a href="/advantage-vs-original">the Advantage or Original page</a>: Advantage plans use
      prior authorization broadly, Original Medicare uses it for a defined list, and in six states that
      list is longer than it used to be. The window for changing a plan is covered on
      <a href="/open-enrollment">the open enrollment page</a>, and the services that fall outside both are
      on <a href="/medicare-gaps">the gaps page</a>.</p>

      <h2>What&rsquo;s worth keeping in mind</h2>

""" + check([
        'Since <strong>January 2026</strong>, a pilot called WISeR has required prior authorization for a '
        'list of Part B services in <strong>Arizona, New Jersey, Ohio, Oklahoma, Texas and Washington</strong>.',
        'It applies to <strong>Original Medicare only</strong>; Medicare Advantage plans are outside it. It is '
        'scheduled to run to <strong>31 December 2031</strong>.',
        'Services reported include skin substitutes, nerve stimulator implants and some orthopedic pain '
        'procedures. Counts differ from 13 to 17 by source.',
        'Providers submit the requests. Vendors are paid a share of savings, which is both the model&rsquo;s '
        'design and the main criticism.',
        'The model is a time-limited test. A bill to repeal it has been introduced; no vote was found.',
    ]) + """
      <p>The accurate statement is narrower than either side of the argument makes it. Original Medicare
      still does not require approval for most services. In six states, for a defined list, it now does.</p>
""",
    'sources': [
        ('Congressional Research Service &mdash; Overview of the Medicare Wasteful and Inappropriate Service '
         'Reduction (WISeR) Model',
         'https://www.congress.gov/crs-product/IF13133'),
        ('KFF &mdash; Examining the potential impact of Medicare&rsquo;s new WISeR model',
         'https://www.kff.org/medicare/examining-the-potential-impact-of-medicares-new-wiser-model/'),
        ('Kiplinger &mdash; Prior authorization for traditional Medicare patients has started in 6 states',
         'https://www.kiplinger.com/retirement/medicare/prior-authorization-coming-to-traditional-medicare'),
        ('American Hospital Association &mdash; AHA comments on CMS WISeR model (23 October 2025)',
         'https://www.aha.org/lettercomment/2025-10-23-aha-comments-cms-wiser-model'),
        ('Center for Medicare Advocacy &mdash; Early reports on WISeR model are troubling',
         'https://medicareadvocacy.org/early-reports-on-wiser-model-are-troubling/'),
        ('Moss Adams &mdash; Medicare WISeR prior authorization model (January 2026)',
         'http://www.mossadams.com/articles/2026/01/medicare-wiser-model'),
    ],
    'next': {'slug': 'advantage-vs-original',
             'title': 'Advantage or Original: what actually differs',
             'blurb': 'The choice most people make once a year, and the differences that do not appear on '
                      'the plan card.'},
}
