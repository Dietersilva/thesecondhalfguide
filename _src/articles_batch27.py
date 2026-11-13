#!/usr/bin/env python3
"""Twenty-seventh batch: two pieces from 6 November 2026 that bear on readers
55-70 and are not covered elsewhere on the site -- the Medicaid work
(community-engagement) requirement that states must start by 1 January 2027 for
expansion adults 19 to 64 (CMS issued its interim final rule on 1 June 2026),
and the WISeR model that has put prior authorization into traditional Medicare in
six states since January 2026.

Revised 13 November 2026 after an outside audit: the 29 October 2026 court ruling
(Massachusetts v. Oz) is added to the Medicaid piece; WISeR is described as two routes
(prior authorization or pre-payment review). Verified by agreement across independent
reporting; the CMS participant-guide payment rate (reported as 25 percent), the provider
exemption process and several Medicaid procedural details come from the audit and are
described without figures or stated cautiously. Omitted: the 10-20 percent vendor-share
figure (an October 2025 AHA estimate), a service count, and vendor names."""

from build_articles import facts, check, AD_INLINE

ARTICLES27 = {}

CHECKED27 = '13 November 2026'

# ------------------------------------------------------- Medicaid work requirement
ARTICLES27['medicaid-work-requirements'] = {
    'title': 'Medicaid Work Requirements in 2027: What Adults 55 to 64 Need to Know &mdash; The Second Half Guide',
    'eyebrow': 'Facts &amp; thresholds',
    'h1': 'Medicaid work requirements in 2027: what adults 55 to 64 need to know',
    'dek': 'Expansion adults 19 to 64 face a monthly work, study or service requirement from 1 January 2027. '
           'A federal court changed part of CMS&rsquo;s rule on 29 October. What still applies, and what to ask '
           'your state.',
    'meta': '6 minute read &middot; Checked against CMS&rsquo;s rule, the 29 October court ruling and '
            'independent reporting that cites them',
    'checked': CHECKED27,
    'recheck': {'due': '2026-12-15', 'why': 'Check the Massachusetts v. Oz ruling for an appeal or stay, any '
                'guidance CMS issues in response, and which states have announced launch dates; recheck again '
                'before 1 January 2027.'},
    'body': """      <p>Most coverage of Medicaid work requirements is about younger adults. The age range in the
      rule is 19 to 64. That includes a lot of readers of this site: people in their late fifties and early
      sixties who left a job, have no employer coverage, and are covered through their state&rsquo;s
      Medicaid expansion while they wait for Medicare at 65.</p>

      <h2>The court ruling, and what it did not change</h2>

      <p>On <strong>29 October 2026</strong>, a federal judge in Massachusetts (<em>Commonwealth of
      Massachusetts v. Oz</em>) ruled against part of CMS&rsquo;s rule. The court vacated the extra test CMS
      added for the medically frail exemption, which would have required a person to show that a condition
      significantly impaired the ability to work. It also issued an injunction for the 25 states and the
      District of Columbia that brought the case, and the reporting says it bars penalties on those states
      for implementation errors or delays for six months. The court left in place the rule&rsquo;s 12-month
      look-back for claims data and its limits on relying on a person&rsquo;s own statement.</p>

      <p>The ruling does not remove the requirement or change the <strong>1 January 2027</strong> start date.
      The reporting reviewed does not say whether CMS will appeal, and the situation may change quickly.
      Whether any of this applies to you depends on your state, so ask the state Medicaid agency which rules
      it is using.</p>

""" + facts('The Medicaid work requirement, in numbers', [
        ('1 January 2027', 'The date states must begin applying the requirement. States may start earlier.'),
        ('1 June 2026', 'When CMS issued its interim final rule on how states apply it.'),
        ('Ages 19 to 64', 'The adults covered, primarily people enrolled through Medicaid expansion.'),
        ('80 hours a month', 'Qualifying activity: work, community service, a work program, or at least '
                             'half-time education, which can also qualify separately.'),
        ('$580 a month', 'Average monthly income of at least this much counts instead of the hours. It is '
                         'the federal minimum wage times 80 hours.'),
        ('30 days', 'From receipt of a notice of noncompliance to show compliance or an exemption.'),
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
      accepted and when the first notices go out differ from state to state. States may begin earlier than
      January. A state that cannot be ready can apply for a temporary good-faith-effort exemption, which
      delays implementation until no later than 31 December 2028. Whether a given state has done so is a
      question for the state&rsquo;s Medicaid agency.</p>

      <h2>What counts toward the 80 hours</h2>

      <p>The rule counts several kinds of activity: employment, community service, participation in a
      work program, and education at least half-time, which is a separate path. Income can count in place
      of the hours. The income measure is the household&rsquo;s monthly income calculated under the modified
      adjusted gross income (MAGI) method, and a state may average seasonal income over several months. The
      $580 figure is the federal minimum wage of $7.25 multiplied by 80.</p>

      <p>Compliance is checked when a person applies, and states look back one to three months before the
      application month. At renewal, the state checks a number of qualifying months. Your state decides some of
      these mechanics, so the notice you receive is the document that controls.</p>

      <blockquote class="pull">
        <p>The question is not whether you worked this week. It is whether the state can verify 80 hours,
        income or an exemption for the months it checks.</p>
      </blockquote>

""" + AD_INLINE + """
      <h2>Who is exempt</h2>

      <p>Coverage of the rule gives examples of exemptions: parents or caregivers of a child 13 or younger
      or of a person with a disability, veterans with a total disability rating, people who are medically
      frail, former foster youth, and American Indians and Alaska Natives. States may also adopt
      hardship exceptions of their own. These are examples, not a complete list, and the list a state uses
      is the state&rsquo;s. How a person shows an exemption, including whether a self-declaration is enough,
      differs before and from 1 January 2028, so ask the state which evidence it accepts. The 29 October
      ruling concerns the medically frail exemption in particular.</p>

      <p>There is no exemption based on age alone listed in the coverage reviewed for this page, including
      for people in their late fifties or early sixties.</p>

      <h2>When the state cannot verify compliance</h2>

      <p>If a state cannot verify that a person met the requirement or qualified for an exemption, it must
      send a notice. The person then has 30 calendar days from receipt to show compliance or an exemption.
      For people already enrolled, coverage continues during that window, and the state is expected to check
      whether the person qualifies another way before ending it. Coverage ends only if the window closes
      without a satisfactory response. CMS has said a person who loses coverage this way can reapply, with
      no lockout period, and the state may offer a conditional reconsideration route.</p>

      <p>One consequence matters for anyone who relies on the Marketplace as a fallback. Under the federal
      law and CMS&rsquo;s description of it, a person denied or disenrolled from Medicaid solely for not meeting
      the requirement cannot get Marketplace premium tax credits on that basis. That is why this page sits
      beside <a href="/aca-subsidy-cliff">the ACA subsidy cliff page</a>.</p>

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
        'A <strong>29 October 2026</strong> federal ruling struck CMS&rsquo;s added medical-frailty test, with '
        'protection for 25 plaintiff states and D.C. It did not change the start date.',
        'It covers expansion adults <strong>19 to 64</strong>: <strong>80 hours a month</strong> of work, '
        'service, a work program or half-time school, or about <strong>$580 a month</strong> in income.',
        'Exemptions include caregivers of a child 13 or younger, medically frail people and veterans with a '
        'total disability rating, among others. Age alone is not listed.',
        'A missed or unverified month brings a notice and <strong>30 calendar days</strong> to respond. '
        'Verification varies by state, so check with your state&rsquo;s Medicaid agency.',
    ]) + """
      <p>The deadline is set by federal law and the process is set by each state. For anyone covered
      this way, the practical question is what the state will ask to see, and when it will ask.</p>
""",
    'sources': [
        ('CMS &mdash; Medicaid community engagement requirement interim final rule with comment period (fact sheet)',
         'https://www.cms.gov/newsroom/fact-sheets/medicaid-community-engagement-requirement-certain-individuals-interim-final-rule-comment-period-cms'),
        ('Medicaid.gov &mdash; Community engagement requirement for certain individuals (interim final rule briefing)',
         'https://www.medicaid.gov/medicaid/downloads/ce-requirement-ifc-deck.pdf'),
        ('STAT &mdash; Judge rejects new Medicaid work rules for the medically frail (29 October 2026)',
         'https://www.statnews.com/2026/10/29/medicaid-work-requirements-judge-blocks-new-limits-medical-frailty/'),
        ('HFMA &mdash; Court vacates CMS medical frailty restriction in Medicaid work requirement',
         'https://www.hfma.org/payment-reimbursement-and-managed-care/medicaid-work-requirement-medical-frailty-ruling/'),
        ('Ballotpedia News &mdash; CMS releases interim final rule for Medicaid work requirements, defines medical '
         'frailty exemption (12 June 2026)',
         'https://news.ballotpedia.org/2026/06/12/cms-releases-interim-final-rule-for-medicaid-work-requirements-defines-medical-frailty-exempt/'),
        ('Center on Budget and Policy Priorities &mdash; A guide to reducing coverage losses through effective '
         'implementation of Medicaid&rsquo;s new work requirement',
         'https://www.cbpp.org/research/health/a-guide-to-reducing-coverage-losses-through-effective-implementation-of-medicaids'),
        ('Foley Hoag &mdash; CMS issues interim final rule imposing Medicaid work requirements for expansion '
         'populations (June 2026)',
         'https://foleyhoag.com/news-and-insights/publications/alerts-and-updates/2026/june/cms-issues-interim-final-rule-imposing-medicaid-work-requirements-for-expansion-populations/'),
    ],
    'next': {'slug': 'medicare-savings',
             'title': 'The Medicare help millions qualify for and never claim',
             'blurb': 'Four Medicare Savings Programs and Extra Help, and the income limits most people '
                      'overestimate.'},
}

# ------------------------------------------------------------- WISeR
ARTICLES27['wiser-prior-authorization'] = {
    'title': 'WISeR Adds a Payment-Review Step to Original Medicare in Six States &mdash; The Second Half Guide',
    'eyebrow': 'Facts &amp; thresholds',
    'h1': 'WISeR adds a payment-review step to Original Medicare in six states',
    'dek': 'A CMS pilot that began in January 2026 adds prior authorization or pre-payment review for certain '
           'Part B services in Arizona, New Jersey, Ohio, Oklahoma, Texas and Washington. Medicare Advantage '
           'is not part of it.',
    'meta': '6 minute read &middot; Checked against CMS, CRS, KFF and independent reporting on the model',
    'checked': CHECKED27,
    'recheck': {'due': '2026-12-15', 'why': 'Check CMS&rsquo;s WISeR page for the current services list, any '
                'exemption (gold card) program, and any expansion or legislative action.'},
    'body': """      <p>One common argument for choosing Original Medicare over an Advantage plan is that Original
      Medicare does not make a provider ask permission first. In six states that has been less true since
      January 2026. The pilot is called WISeR, short for Wasteful and Inappropriate Service Reduction. It
      puts a payment-review step on a defined list of Part B services, either approval before the service or
      review before payment.</p>

      <p>It is worth a page now because the choice between Original Medicare and an Advantage plan is
      made during open enrollment, and one familiar talking point has an exception for people who live in
      these states.</p>

""" + facts('The WISeR model, in numbers', [
        ('Six states', 'Arizona, New Jersey, Ohio, Oklahoma, Texas and Washington.'),
        ('January 2026', 'When the model began. Services provided before 15 January 2026 are not subject '
                         'to it.'),
        ('31 December 2031', 'When the model is scheduled to end, per the Congressional Research Service.'),
        ('Original Medicare only', 'Medicare Advantage plans are not part of WISeR.'),
        ('Selected services', 'A defined list of services and codes in CMS&rsquo;s current operational guide. '
                              'Sources count the categories differently.'),
        ('Two routes', 'The provider either requests prior authorization before the service, or the claim goes '
                       'through post-service, pre-payment review.'),
    ]) + """
      <h2>What it is</h2>

      <p>Prior authorization means a provider gets approval before delivering a service, or Medicare may
      not pay for it. Advantage plans have used it for years. Original Medicare mostly has not, with
      exceptions such as some equipment, covered on
      <a href="/dme-prior-authorization">the equipment prior authorization page</a>. WISeR extends the idea
      to a set of Part B services. It is a CMS Innovation Center model, which means a time-limited test and
      not a permanent rule.</p>

      <p>The model is keyed to providers and suppliers in the six states. It applies to Original Medicare
      claims and not to Medicare Advantage members, who are subject to their own plans&rsquo; rules. Railroad
      Medicare is excluded. Whether it will be extended to other states or services has not been announced in
      the reporting reviewed.</p>

      <h2>Which services</h2>

      <p>The list is a set of Part B services chosen as vulnerable to overuse. KFF&rsquo;s description names
      skin substitutes used in treating severe or chronic wounds, electrical nerve stimulator implants and
      certain orthopedic pain services such as cervical fusion and epidural steroid injections. Other
      summaries include arthroscopy for knee osteoarthritis. The authoritative list is the selected services
      and codes in CMS&rsquo;s current operational guide for providers, which CMS can update during the
      model, so this page does not give a single number.</p>

      <blockquote class="pull">
        <p>The rule is not that everything in Original Medicare now needs approval. It is that a specific
        list is reviewed, for providers in six specific states.</p>
      </blockquote>

""" + AD_INLINE + """
      <h2>Who decides, and how the participants are paid</h2>

      <p>Each state has one participating technology company that reviews requests. Reporting says the
      companies use artificial intelligence to help with review and that licensed clinicians make decisions
      not to approve a request. Participants are not paid a flat fee. They are paid a share of savings
      attributed to the review process, and payments are adjusted for timeliness, accuracy and the
      provider&rsquo;s experience with the process. CMS has also said inaccurate results can lower a
      participant&rsquo;s payment. Critics see an incentive to deny; supporters say the model could reduce
      spending that falls on taxpayers and beneficiaries.</p>

      <p>Providers and suppliers submit the requests, not patients. A patient&rsquo;s practical contact with
      the model is often indirect: a scheduled procedure waiting for an approval, or a non-affirmation the
      provider has to pursue. When a request is not approved, the provider can resubmit it, with a
      peer-to-peer conversation available, which is different from a formal appeal of a denied claim.
      CMS&rsquo;s operational guide is the place to confirm which route applies to a specific service. CMS has
      also described a process under which providers with high approval rates can be exempted from review.</p>

      <h2>What is contested</h2>

      <p>The model has drawn criticism from advocacy groups, medical associations and some members of
      Congress. A bill to repeal it, H.R. 5940, the Seniors Deserve SMARTER Care Act, was introduced in the
      House on 7 November 2025 by Representative Suzan DelBene. The reporting reviewed shows no action
      beyond its referral to committee. The Center for Medicare Advocacy published an article on the model on
      26 March 2026 that raised concerns; that is the view of an advocacy group and not a measured finding.</p>

      <h2>Where this fits in the enrollment choice</h2>

      <p>None of this is a recommendation. It is one fact that belongs next to the others in the choice
      covered on <a href="/advantage-vs-original">the Advantage or Original page</a>: Advantage plans use
      prior authorization broadly, Original Medicare uses it for a defined list, and in six states that
      list now carries a payment-review step. The window for changing a plan is covered on
      <a href="/open-enrollment">the open enrollment page</a>, and the services that fall outside both are
      on <a href="/medicare-gaps">the gaps page</a>.</p>

      <h2>What&rsquo;s worth keeping in mind</h2>

""" + check([
        'Since <strong>January 2026</strong>, a pilot called WISeR has put a payment-review step on selected '
        'Part B services in <strong>Arizona, New Jersey, Ohio, Oklahoma, Texas and Washington</strong>.',
        'It applies to <strong>Original Medicare only</strong>; Medicare Advantage plans are outside it. It is '
        'scheduled to run to <strong>31 December 2031</strong>.',
        'The review comes in two forms: <strong>prior authorization</strong> before the service, or '
        '<strong>pre-payment review</strong> of the claim afterwards.',
        'Providers and suppliers submit the requests. The participants are paid a share of savings, which is '
        'both the model&rsquo;s design and the main criticism.',
        'The model is a time-limited test. A repeal bill was introduced in November 2025 and has not advanced '
        'in the reporting reviewed.',
    ]) + """
      <p>The accurate statement is narrower than either side of the argument makes it. Original Medicare
      still does not require approval for most services. In six states, for a defined list, there is now a
      review step before payment.</p>
""",
    'sources': [
        ('Congressional Research Service &mdash; Overview of the Medicare Wasteful and Inappropriate Service '
         'Reduction (WISeR) Model',
         'https://www.congress.gov/crs-product/IF13133'),
        ('CMS &mdash; WISeR Model',
         'https://www.cms.gov/priorities/innovation/innovation-models/wiser'),
        ('CMS &mdash; WISeR Model Frequently Asked Questions',
         'https://www.cms.gov/priorities/innovation/files/document/wiser-model-frequently-asked-questions'),
        ('KFF &mdash; Examining the potential impact of Medicare&rsquo;s new WISeR model',
         'https://www.kff.org/medicare/examining-the-potential-impact-of-medicares-new-wiser-model/'),
        ('American Bar Association &mdash; The WISeR model comes to Original Medicare: what providers and '
         'suppliers in model states should know (2026)',
         'https://www.americanbar.org/groups/health_law/resources/esource/2026/the-wiser-model-comes-to-original-medicare/'),
        ('Representative DelBene &mdash; Democrats introduce legislation to block harmful red tape in Medicare',
         'https://delbene.house.gov/news/documentsingle.aspx?DocumentID=4221'),
        ('Kiplinger &mdash; Prior authorization for traditional Medicare patients has started in 6 states',
         'https://www.kiplinger.com/retirement/medicare/prior-authorization-coming-to-traditional-medicare'),
        ('Center for Medicare Advocacy &mdash; Early reports on WISeR model are troubling (26 March 2026)',
         'https://medicareadvocacy.org/early-reports-on-wiser-model-are-troubling/'),
    ],
    'next': {'slug': 'advantage-vs-original',
             'title': 'Advantage or Original: what actually differs',
             'blurb': 'The choice most people make once a year, and the differences that do not appear on '
                      'the plan card.'},
}
