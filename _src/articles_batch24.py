#!/usr/bin/env python3
"""Twenty-fourth batch: three pieces from the third week of October 2026 --
what the 2026 Social Security Trustees Report actually says (released 9 June;
the COLA coverage keeps pairing it with the 2032 headline), the recurring
"activate your COLA" scam (the 2027 COLA was announced 14 October), and the
Medicare Prescription Payment Plan during Annual Enrollment.

cms.gov, medicare.gov and ssa.gov are proxy-blocked here, so no primary source
was read directly. Verified per CLAUDE.md section 2 by agreement across
independent reporting that traces to the agency. Deliberately omitted because
only one source gave it: CBO's own projected benefit cut, a 2024 OIG alert date,
and the exact 2027 renewal wording for the Prescription Payment Plan."""

from build_articles import facts, check, AD_INLINE

ARTICLES24 = {}

CHECKED24 = '16 October 2026'

# ------------------------------------------------------------- Trustees Report
ARTICLES24['social-security-trust-fund'] = {
    'title': 'What the 2026 Trustees Report Says About Social Security &mdash; The Second Half Guide',
    'eyebrow': 'Facts &amp; thresholds',
    'h1': 'What the 2026 Trustees Report actually says about Social Security',
    'dek': 'The numbers behind the 2032 and 2034 headlines: which fund runs short, what share of benefits '
           'would still be payable, and what the report does not say.',
    'meta': '6 minute read &middot; Checked against the Trustees Report as published by SSA and CRS',
    'checked': CHECKED24,
    'body': """      <p>Every time Social Security makes news, a second number follows it around. This month the
      3.6% cost-of-living adjustment was announced, and within hours it was being printed beside a date
      in the early 2030s and the word &ldquo;cut.&rdquo; The two numbers are unrelated. The COLA comes
      from a formula applied to consumer prices. The date comes from the annual report of the
      program&rsquo;s trustees.</p>

      <p>That report was released on <strong>9 June 2026</strong>, more than four months ago, and it is
      still the current one. It is not new this week. It is worth setting out plainly because the
      headlines compress it badly.</p>

""" + facts('The 2026 Trustees Report, in numbers', [
        ('9 June 2026', 'When the 2026 Trustees Report was released.'),
        ('Fourth quarter of 2032', 'When the retirement and survivors fund (OASI) is projected to run out '
                                    'of reserves &mdash; one quarter earlier than last year&rsquo;s '
                                    'projection.'),
        ('78%', 'The share of scheduled OASI benefits that continuing income would cover at that point, '
                'if the law is not changed. The remaining 22% is the projected shortfall.'),
        ('2034', 'When the retirement, survivors and disability funds, treated as one combined fund, are '
                 'projected to run out of reserves. CRS gives the third quarter of 2034.'),
        ('83%', 'The share of scheduled benefits the combined funds&rsquo; income would cover at that '
                'point.'),
        ('Through 2100', 'The disability fund (DI) is projected to pay full benefits for the whole '
                         '75-year period.'),
        ('4.42%', 'The long-range actuarial deficit, as a share of taxable payroll, for 2026&ndash;2100. '
                  'Last year&rsquo;s report put it at 3.82% for 2025&ndash;2099.'),
    ]) + """
      <h2>What &ldquo;runs out&rdquo; means</h2>

      <p>The trust funds hold reserves built up when payroll taxes exceeded benefits paid. Depletion is
      the date those reserves reach zero. It is not the date benefits stop. Payroll taxes keep arriving
      every pay period, and the report estimates how much of the scheduled benefit that continuing income
      would cover. For the retirement fund in the fourth quarter of 2032 the answer is 78%.</p>

      <p>That percentage is the whole content of the &ldquo;22% cut&rdquo; headline. It is a systemwide
      financing estimate: the share of scheduled benefits that continuing income could support. It is not
      an enacted 22% cut to every person&rsquo;s monthly check, and current law does not say exactly how
      benefits would be paid once reserves are exhausted. The Congressional Research Service has described
      two possibilities: full benefits paid late, or reduced benefits paid on time. No decision has been
      made, and the report does not predict what Congress will do.</p>

      <blockquote class="pull">
        <p>Depletion is the date the reserves reach zero, not the date benefits stop. The report counts
        what the continuing income would pay.</p>
      </blockquote>

""" + AD_INLINE + """
      <h2>Two funds, one headline</h2>

      <p>Social Security is paid from two legally separate trust funds: Old-Age and Survivors Insurance
      for retirement and survivor benefits, and Disability Insurance. They are reported separately and
      also together. The 2032 date belongs to the retirement fund alone. The 2034 date is what results
      when the two are combined as though they were one, and it assumes the funds are allowed to be
      treated that way. The disability fund, on its own, is not projected to run short at all within the
      report&rsquo;s 75-year window.</p>

      <p>Headlines usually pick one date and drop the other. A reader who sees &ldquo;2032&rdquo; in one
      place and &ldquo;2034&rdquo; in another is not seeing a contradiction; they are seeing two different
      funds.</p>

      <h2>What changed from the 2025 report</h2>

      <p>The projected date moved earlier by one quarter. The long-range deficit widened, from 3.82% of
      taxable payroll in last year&rsquo;s report to 4.42% in this one. Coverage of the report points to
      the Trustees&rsquo; assumptions about lower birth rates and lower net immigration, and to a lower
      expected level of revenue from income taxes on benefits following the 2025 tax law. Those are the
      assumptions behind the projection, and they are exactly the kind of inputs that change from one
      report to the next.</p>

      <p>It is also worth holding onto what a projection is. The report works from a set of intermediate
      assumptions about the economy and population and gives a single central estimate. A different
      assumption set would move the date. The Trustees publish a new report every year, and the figures in
      it are revised each time.</p>

      <h2>Medicare is reported separately</h2>

      <p>The same Trustees also report on Medicare&rsquo;s Hospital Insurance fund, which pays for Part A.
      The 2026 report projects that fund can pay full benefits until the <strong>second quarter of
      2033</strong>, also one quarter earlier than last year, after which income would cover about 89% of
      scheduled benefits. That fund is separate from Social Security&rsquo;s, funded differently, and
      the dates should not be merged into one &ldquo;the program runs out&rdquo; sentence.</p>

      <h2>What the report does not say</h2>

      <p>It does not say benefits already being paid will be cut on a particular date; it describes what
      the law would produce without changes. It does not say what legislation will be passed. It does
      not change anything about the cost-of-living adjustment, which is set separately by the
      consumer-price formula covered on <a href="/cola-2027-estimate">the 2027 COLA page</a>. And it does
      not describe any individual&rsquo;s benefit: 78% is the aggregate share of scheduled benefits that
      projected continuing income could support, not a calculation for any one person&rsquo;s
      record.</p>

      <p>For the ages this site is written for, the dates are close enough to be worth knowing and far
      enough away that they are not a deadline. A person who is 66 now is 72 in 2032. A person who is 60
      is 66. The report&rsquo;s figures apply to people of every age who are receiving benefits at the
      time, which is why the same headline shows up in coverage aimed at people of every age.</p>

      <h2>What&rsquo;s worth keeping straight</h2>

""" + check([
        '<strong>2032</strong> is the retirement and survivors fund alone. <strong>2034</strong> is the '
        'combined retirement, survivors and disability funds.',
        '<strong>78%</strong> and <strong>83%</strong> are the shares of scheduled benefits that '
        'continuing income would cover at depletion, under current law. They are not announced cuts.',
        'The disability fund is not projected to run out within the 75-year projection period.',
        'Medicare&rsquo;s Hospital Insurance fund is projected separately: the second quarter of '
        '<strong>2033</strong>, with income covering about <strong>89%</strong> at that point.',
        'The report was released on <strong>9 June 2026</strong>. The 3.6% COLA announced in October is '
        'unrelated to it.',
    ]) + """
      <p>A headline can hold one number. A report holds several, each with a condition attached. The
      useful habit is to ask of any date: which fund, what share of benefits, under what assumptions.
      The 2026 report answers all three, and answers them differently from the way most coverage does.</p>
""",
    'sources': [
        ('Social Security Administration &mdash; Status of the Social Security and Medicare Programs '
         '(Trustees Report summary)',
         'https://www.ssa.gov/oact/trsum/'),
        ('Social Security Administration &mdash; 2026 OASDI Trustees Report, conclusion',
         'https://www.ssa.gov/oact/TR/2026/II_E_conclu.html'),
        ('Congressional Research Service &mdash; Social Security: Selected Findings of the 2026 Annual '
         'Report',
         'https://www.everycrsreport.com/reports/IF13256.html'),
        ('National Taxpayers Union Foundation &mdash; Social Security and Medicare trust fund depletion '
         'dates move closer',
         'https://www.ntu.org/foundation/detail/social-security-and-medicare-trust-fund-depletion-dates-move-closer'),
        ('Fox Business &mdash; Social Security has less than 10 years before reserves are exhausted, new '
         'trustees report warns',
         'https://www.foxbusiness.com/personal-finance/social-security-has-less-than-10-years-before-reserves-exhausted-new-trustees-report-warns'),
    ],
    'next': {'slug': 'cola-2027-estimate',
             'title': 'The 2027 Social Security COLA is 3.6%',
             'blurb': 'The adjustment that is set by a price formula, not by the trust funds, and the '
                      'other 2027 numbers that moved with it.'},
}

# -------------------------------------------------------------------- COLA scam
ARTICLES24['cola-scam'] = {
    'title': 'The Social Security &ldquo;COLA Activation&rdquo; Scam &mdash; The Second Half Guide',
    'eyebrow': 'Protecting yourself',
    'h1': 'The Social Security &ldquo;COLA activation&rdquo; scam',
    'dek': 'The 3.6% increase is automatic. Every year, scammers invent a step &mdash; a fee, a phone '
           'call, a form &mdash; that Social Security&rsquo;s inspector general says does not exist.',
    'meta': '5 minute read &middot; Checked against SSA and SSA Inspector General materials and AARP '
            'reporting',
    'checked': '26 October 2026',
    'body': """      <p>On 14 October the Social Security Administration announced a 3.6% cost-of-living
      adjustment for 2027. The increase is applied automatically. Nobody has to apply, pay or call to
      receive it. That plain fact is the entire basis of a scam that reappears every fall, and it is
      easier to see once the real process is laid out beside the fake one.</p>

      <p>One note on timing, because the site&rsquo;s rule is to say how old a fact is. This piece was
      first checked on 16 October 2026 and updated on 26 October. The Inspector General&rsquo;s earlier
      alerts cited below date from 2022, 2024 and 2025. A warning about the 2027 increase itself followed
      the announcement: reports dated 21&ndash;22 October say Social Security is warning that scammers
      are asking for activation fees, requests to change direct-deposit details, personal or financial
      information, and visits to imitation websites or downloads of malicious software, all tied to the
      new increase. The pitch is old and the number in it changes.</p>

""" + facts('The real process, and the fake one', [
        ('3.6%', 'The 2027 COLA, announced 14 October 2026. It takes effect with January 2027 benefits.'),
        ('$0', 'The cost of receiving it. There is no fee, no application and no &ldquo;activation.&rdquo;'),
        ('Late November', 'When COLA notices begin to appear in the Message Center of a personal '
                          '<em>my Social Security</em> account, as reported from SSA&rsquo;s announcement.'),
        ('December', 'When people who do not use the online notices receive the mailed COLA notice.'),
        ('What a real notice shows', 'The new benefit amount and any deductions, with dates and dollar '
                                     'figures. It does not ask for money or for information.'),
        ('Where to report', '<em>oig.ssa.gov</em> for Social Security impersonation, and '
                            '<em>reportfraud.ftc.gov</em> for fraud generally.'),
    ]) + """
      <h2>What the scam looks like</h2>

      <p>The variants differ in packaging. The pitch underneath is always the same: the raise is real, but
      something has to be done to get it.</p>

      <p>The Inspector General&rsquo;s office has warned about <strong>letters</strong> made to look like
      Social Security letterhead that tell the recipient to call a toll-free number to turn on a benefit
      increase. The number reaches a scammer. It has also warned about calls and messages that demand a
      fee or personal details to &ldquo;activate&rdquo; the increase. AARP&rsquo;s reporting on the
      scheme describes messages that ask for $100, and links to websites that closely imitate the
      agency&rsquo;s own. In June 2024 the office put out a separate alert that a claimed &ldquo;$600
      June increase&rdquo; was bogus.</p>

      <p>The Inspector General&rsquo;s position across these alerts is consistent: the annual increase is
      automatic and needs no extra information or action from the beneficiary.</p>

      <blockquote class="pull">
        <p>If someone says there is a step required to receive the COLA, the step is the scam. The raise
        arrives without one.</p>
      </blockquote>

""" + AD_INLINE + """
      <h2>Why it works in October</h2>

      <p>It works because the first half of the story is true. The raise exists, the percentage is in the
      news, and many beneficiaries are expecting a notice. A letter or call that mentions the real figure
      sounds informed. In the same weeks, Medicare&rsquo;s Annual Enrollment has opened and Medicare
      premiums are about to be announced, so a reader is already braced for mail and calls about
      money. The mail that is real, such as the plan notices covered on
      <a href="/anoc-letter">the Annual Notice of Change page</a>, looks a lot like the mail that isn&rsquo;t.</p>

      <p>Impersonators also lean on the agency&rsquo;s real branding and the names of real officials. A
      page that looks right is not evidence that it is.</p>

      <h2>The pitch is old; only the number changes</h2>

      <p>This is not a one-year problem. AARP was describing COLA-themed Social Security phone scams in
      2022. The Inspector General&rsquo;s office warned in October 2022 that offers to increase a
      benefit come from criminals, in June 2024 about a &ldquo;$600 June increase&rdquo; that did not
      exist, and in July 2025 about the letters. Each wave borrows
      whatever the current figure is. For 2026 the figure was 2.8%; for 2027 it is 3.6%. A message that
      cites the right percentage has told you only that the sender reads the news.</p>

      <p>One practical consequence follows from the agency&rsquo;s own schedule. The real notice does not
      begin appearing online until late November and does not arrive by mail until December. A letter or
      call about &ldquo;your COLA&rdquo; that shows up in October is ahead of that schedule. That is an
      inference from the dates rather than a rule the agency has published, and it is a reason to verify
      the contact independently, not proof that it is fraudulent.</p>

      <h2>How the real notice reaches you</h2>

      <p>Social Security sends each beneficiary a notice of the new amount. People with a <em>my Social
      Security</em> account can read it in the Message Center starting in late November, before the paper
      copy. People without online notices get a one-page mailed notice in December that lays out the new
      benefit amount and any deductions, including the Medicare premium. The first higher payment arrives
      with the January 2027 benefit, on the usual schedule; for most people that means the Wednesday tied
      to their birthday.</p>

      <p>None of it asks for a payment, a password or a Social Security number. If a contact does ask for
      one, it did not come through that process.</p>

      <h2>Where the real information lives</h2>

      <p>The Message Center in a personal <em>my Social Security</em> account, the one-page notice in the
      mail, and the 3.6% announcement on <em>ssa.gov</em> are the main places. The agency&rsquo;s own
      offices and its published phone number, found on <em>ssa.gov</em> rather than on a letter, are also
      legitimate ways to ask. A text, a social media post, or a call or letter that points to a different
      website is a reason to stop and check. The practical test is to reach the same information through a
      route you chose, by typing the agency&rsquo;s address yourself, instead of the route the message
      offered you.</p>

      <h2>What the agency has said about how it contacts people</h2>

      <p>The Inspector General has said Social Security does not pressure people into acting right away,
      and advises hanging up or ignoring a suspicious call, text, email or letter, then checking
      <em>ssa.gov</em> directly instead of through anything in the message. That is the same pattern covered in
      <a href="/five-minute-rule">the page on why scammers need you to act right now</a>, and the
      follow-through for people locked out of their own account is on
      <a href="/social-security-login">the Social Security login page</a>.</p>

      <h2>What&rsquo;s worth keeping in mind</h2>

""" + check([
        'The 2027 COLA of <strong>3.6%</strong> is applied automatically. There is no fee, application or '
        '&ldquo;activation.&rdquo;',
        'A real COLA notice shows the new amount and deductions. It does not ask for money, a password or '
        'a Social Security number.',
        'Notices appear in the <em>my Social Security</em> Message Center starting in late November, and '
        'by mail in December for people who do not use online notices.',
        'A toll-free number printed on a letter proves nothing. Letters can be copied from real '
        'letterhead; the Inspector General has warned about exactly this.',
        'Social Security impersonation can be reported at <em>oig.ssa.gov</em>, and any fraud at '
        '<em>reportfraud.ftc.gov</em>.',
    ]) + """
      <p>The scam survives because the premise is true: the raise is real, and people want to be sure they
      get it. The reassuring fact is the same every year. They will, and nothing about the process requires
      them to prove anything to anyone first.</p>
""",
    'sources': [
        ('SSA Office of the Inspector General &mdash; Inspector General warns of newest imposter scam tactic '
         '(17 July 2025)',
         'https://oig.ssa.gov/scam-alerts/2025-07-17-inspector-general-warns-of-newest-imposter-scam-tactic/'),
        ('SSA Office of the Inspector General &mdash; Scam alert: Inspector General warns $600 June '
         'increase is bogus (13 June 2024)',
         'https://oig.ssa.gov/news-releases/2024-06-13-scam-alert-inspector-general-warns-600-june-increase-is-bogus'),
        ('AARP &mdash; Warning: fake Social Security COLA phone calls',
         'https://www.aarp.org/money/scams-fraud/warning-fake-social-security-cola-phone-calls/'),
        ('Social Security Administration &mdash; 2027 COLA press release (14 October 2026)',
         'https://www.ssa.gov/news/en/press/releases/2026-10-14.html'),
        ('Nasdaq &mdash; 4 2027 Social Security COLA dates you need to know',
         'https://www.nasdaq.com/articles/4-2027-social-security-cola-dates-you-need-know'),
    ],
    'next': {'slug': 'social-security-login',
             'title': 'Locked out of your Social Security account',
             'blurb': 'What to do when the account the real notice lives in will not let you in.'},
}

# ------------------------------------------------ Medicare Prescription Payment Plan
ARTICLES24['prescription-payment-plan'] = {
    'title': 'The Medicare Prescription Payment Plan: Same Cap, Paid Monthly &mdash; The Second Half Guide',
    'eyebrow': 'Facts &amp; thresholds',
    'h1': 'The Medicare Prescription Payment Plan: same cap, paid monthly',
    'dek': 'The plan does not lower what Part D costs. It spreads the out-of-pocket cap &mdash; $2,400 in '
           '2027 &mdash; into monthly bills. And changing plans in open enrollment ends it.',
    'meta': '5 minute read &middot; Checked against CMS&rsquo;s 2027 announcement and independent '
            'plan and advocacy sources',
    'checked': CHECKED24,
    'body': """      <p>Part D has an annual cap on what a person pays out of pocket for covered drugs: $2,100 in
      2026, rising to <strong>$2,400</strong> in 2027. The cap protects the total. It does not protect the
      timing. A person who fills an expensive drug in January can owe a large share of the year&rsquo;s cap
      at the pharmacy counter in a single visit.</p>

      <p>The <strong>Medicare Prescription Payment Plan</strong> exists for that problem. It does nothing
      about the total. It changes when the money is due.</p>

""" + facts('The plan, at a glance', [
        ('2027 cap', '<strong>$2,400</strong> in covered Part D drug costs per year, whether or not '
                     'you use the plan. The 2026 cap is $2,100.'),
        ('2027 deductible', 'The standard deductible rises to <strong>$700</strong> from $615. That is the '
                            'most a plan may charge; some plans charge less.'),
        ('What it changes', 'The <em>timing</em> of payments. Instead of paying at the pharmacy, you are '
                            'billed monthly by your plan.'),
        ('Cost to join', 'Nothing. There is no fee or interest for using it.'),
        ('How to join', 'Through your own Part D plan. It is voluntary, and it can be started at any '
                        'point in the year, not only during open enrollment.'),
        ('Switching plans', 'Participation is with a specific plan. A person who changes plans needs to '
                            'enroll with the new plan.'),
    ]) + """
      <h2>How the monthly bill is calculated</h2>

      <p>Once enrolled, a person stops paying at the counter for covered drugs. Each month the plan bills
      the lesser of two amounts: what the person owes so far, or a monthly cap. In the first month the cap
      is the annual out-of-pocket threshold, less any eligible costs already incurred, divided by the
      number of months left in the plan year, counting the current month. In later months the cap is the
      unpaid balance plus any new costs, divided by the months left.</p>

      <p>An example for 2027. A person enrolls in January and has $700 in eligible out-of-pocket drug
      costs that month. The first bill is <strong>$200</strong>: the lesser of $700 and the $2,400
      threshold divided by twelve. The remaining $500 carries forward. If $120 in new eligible costs
      arrives in February, that month&rsquo;s bill is about $56.36, which is $500 plus $120 divided by the
      eleven months left. Later bills change as new costs arrive and fewer months remain. The arithmetic
      is the plan&rsquo;s formula, and what it does is spread the same total into smaller pieces.</p>

      <blockquote class="pull">
        <p>The plan changes when the money is due, not how much of it there is.</p>
      </blockquote>

""" + AD_INLINE + """
      <h2>The worst case, in dollars</h2>

      <p>Take the largest possible case for 2027: a person whose first fill of the year is expensive enough
      to reach the whole $2,400 cap at once. Without the plan, that is $2,400 due at the pharmacy. With
      the plan, the January bill is $2,400 divided by twelve, which is $200. The cap is the same and so is
      the total. The plan only changes how it arrives: one bill of $2,400, or a bill of $200 a month for
      twelve months. For a smaller January fill, the monthly figure shrinks in proportion.</p>

      <h2>How a person actually asks</h2>

      <p>Enrollment goes through the person&rsquo;s own Part D plan, not through Medicare directly. The
      plan, in turn, tells the pharmacy that the person is enrolled, so the pharmacy bills the plan instead
      of collecting at the counter. Each plan has its own phone line and process for the request, and the
      plan&rsquo;s member services is where to start. The program is voluntary, and a person can also
      leave it at any time. The details of the request vary by plan, so the plan&rsquo;s own instructions
      are the ones that apply.</p>

      <h2>What it does not do</h2>

      <p>It does not lower a drug&rsquo;s price. It does not change the cap, so a person who would reach
      $2,400 anyway reaches it with or without the plan. It does not change which drugs a plan covers or
      what tier they sit on. And the monthly bills are not optional once a person is enrolled: they are
      what the person owes. According to advocacy-group descriptions of the rules, a plan can end a
      person&rsquo;s participation if the bills go unpaid, though the drug coverage itself continues, and
      returning to the plan means first settling what is owed.</p>

      <p>For a person who would pay most of the cap across the year anyway through a steady set of
      monthly prescriptions, the difference is small. The plan matters most when one or two fills early in
      the year are large. That is a statement about how the formula behaves, not advice about who should
      use it.</p>

      <h2>Why it comes up in October</h2>

      <p>Annual Enrollment runs from 15 October through 7 December, and it is when many people change
      Part D plans. The plan&rsquo;s participation does not follow the person: under the rules described
      for 2026, people already in the plan are carried forward when they stay in the same plan, and
      people who move to a different plan need to enroll with the new one. Coverage chosen in the window
      starts on 1 January 2027, so a person who joins a new plan and wants to spread January&rsquo;s costs
      has to ask the new plan to enroll them.</p>

      <p>Two other 2027 Part D facts sit alongside it in coverage of next year&rsquo;s changes: insulin
      stays capped at $35 a month for a covered supply, and adult vaccines recommended by the
      federal advisory committee remain free under Part D. Neither depends on the payment plan.</p>

      <p>The rest of the 2027 Part D picture is covered on
      <a href="/medicare-2027-costs">the page on 2027 Medicare costs</a> and on
      <a href="/drug-cap">the page about the drug cap</a>. The plan is only a payment mechanism sitting on
      top of those numbers.</p>

      <h2>What&rsquo;s worth checking</h2>

""" + check([
        'The 2027 out-of-pocket cap is <strong>$2,400</strong> for everyone with Part D, with or without '
        'the Prescription Payment Plan.',
        'The plan costs nothing to join and can be started at any time through <strong>your own Part D '
        'plan</strong>.',
        'Each month the plan bills the lesser of what you owe so far and a monthly cap. In the first '
        'month the cap is the remaining threshold divided by the months left &mdash; for 2027, at most '
        '$200 &mdash; and later months use your unpaid balance plus new costs, divided by the months '
        'left.',
        'Participation is tied to a plan. If you switch plans during open enrollment '
        '(<strong>15 October&ndash;7 December</strong>), you need to enroll with the new plan.',
        'The plan does not reduce the total. A person who would pay $2,400 pays $2,400, only in smaller '
        'pieces.',
    ]) + """
      <p>The plan is one of the least dramatic features Medicare has added to Part D, and for a certain
      kind of bill it is the difference between a manageable January and an unmanageable one. It is worth
      understanding precisely because it is so easily mistaken for a discount.</p>
""",
    'sources': [
        ('CMS &mdash; Medicare Advantage and Medicare prescription drug programs expected to remain stable '
         'in 2027 (28 September 2026)',
         'https://www.cms.gov/newsroom/press-releases/medicare-advantage-medicare-prescription-drug-programs-expected-remain-stable-2027'),
        ('Kiplinger &mdash; 8 changes coming to Medicare in 2027',
         'https://www.kiplinger.com/retirement/medicare/changes-coming-to-medicare-in-2027'),
        ('Blue Cross and Blue Shield of Minnesota &mdash; Medicare Prescription Payment Plan',
         'https://www.bluecrossmn.com/understanding-health-insurance/prescription-drugs/medicare-prescription-payment-plan'),
        ('Patient Advocate Foundation &mdash; Changes to Medicare in the Inflation Reduction Act',
         'https://www.patientadvocate.org/whats-changing'),
        ('Optum &mdash; Three key changes in 2026 for patients with Medicare Part D',
         'https://business.optum.com/en/support/hcp-resources/medicare-part-d-changes-2026.html'),
    ],
    'next': {'slug': 'drug-cap',
             'title': 'The $2,100 drug cap: real protection, narrower than it sounds',
             'blurb': 'What the out-of-pocket cap covers, what it does not, and how the 2027 numbers '
                      'change it.'},
}
