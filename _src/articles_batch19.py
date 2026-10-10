#!/usr/bin/env python3
"""Nineteenth batch: two pieces built on federal anti-fraud enforcement
announced in September 2026 -- CMS barring 11 durable medical equipment
suppliers over $3.4 billion in suspected billing, and CMS canceling roughly
315,000 ACA Marketplace enrollments covering more than 760,000 people over
unauthorized broker-assisted sign-ups. Both actions are proxy-blocked at
cms.gov and healthcare.gov, so verified via agreement across independent
reporting (Fierce Healthcare, MedTrade, HPN, SMP Resource Center for the DME
action; NPR, Forbes, FindLaw, Groom Law Group for the Marketplace action) per
CLAUDE.md section 2."""

from build_articles import facts, check, AD_INLINE

ARTICLES19 = {}

CHECKED19 = '27 September 2026'

# ------------------------------------------------- medical equipment fraud
ARTICLES19['medical-equipment-fraud'] = {
    'title': 'The Medical Equipment Fraud Crackdown, and What to Check on Your Own Statement '
             '&mdash; The Second Half Guide',
    'eyebrow': 'Facts &amp; thresholds',
    'h1': 'The medical equipment fraud crackdown, and what to check on your own statement',
    'dek': 'CMS just barred eleven suppliers tied to more than $3.4 billion in suspected fraudulent '
           'billing. The headline number isn&rsquo;t the useful part &mdash; the useful part is what '
           'it confirms about a line item you might already be seeing.',
    'meta': '5 minute read &middot; Verified against CMS&rsquo;s announcement and independent '
            'healthcare-industry reporting',
    'checked': '9 October 2026',
    'body': """      <p>On September 8, 2026, the Centers for Medicare &amp; Medicaid Services barred eleven medical
      equipment suppliers from receiving further Medicare Advantage payments, citing more than $3.4 billion
      in suspected fraudulent billing across 2025 and into 2026. The number is large enough to make
      headlines. The pattern behind it is the more useful thing for an actual Medicare beneficiary to
      know.</p>

""" + facts('The crackdown, at a glance', [
        ('11', 'Durable medical equipment suppliers barred from receiving Medicare Advantage Part C and '
               'Part D payments.'),
        ('$3.4 billion+', 'Suspected fraudulent billing tied to these suppliers, identified across 2025 '
                          'and into 2026.'),
        ('What they billed for', 'Equipment beneficiaries never requested or received &mdash; including '
                                 'claims submitted for people who had already died.'),
        ('4 of the 11', 'Suppliers already revoked from Original Medicare who had shifted to billing '
                        'Medicare Advantage plans instead.'),
        ('September 8, 2026', 'When CMS announced the action, as part of a broader federal anti-fraud '
                              'push.'),
        ('Where you&rsquo;d see this', 'Your Medicare Summary Notice, if you have Original Medicare, or '
                                       'your plan&rsquo;s Explanation of Benefits, if you have Medicare '
                                       'Advantage.'),
    ]) + """
      <h2>What &ldquo;DME fraud&rdquo; actually looks like</h2>

      <p>Durable medical equipment &mdash; DME, sometimes expanded to DMEPOS for equipment, prosthetics,
      orthotics and supplies &mdash; covers wheelchairs, walkers, hospital beds, CPAP machines, diabetic
      testing supplies, back braces and similar items a doctor orders for use at home. It is also one of
      the most consistently exploited corners of Medicare billing, because a supplier can submit a claim
      for equipment without much friction verifying the beneficiary actually asked for it, wanted it, or
      is even still alive to use it.</p>

      <p>That last detail is not a rhetorical flourish. CMS specifically cited billing for deceased
      beneficiaries as one of the patterns behind this action &mdash; claims submitted using a real Medicare
      identifier after the person on it had already died, which nobody was in a position to catch on the
      receiving end. The other core pattern was simpler: equipment billed to Medicare that the beneficiary
      never requested and never received at all.</p>

      <blockquote class="pull">
        <p>Four of the eleven barred suppliers had already been revoked from Original Medicare and had
        simply moved to billing Medicare Advantage plans instead. Being on an Advantage plan didn&rsquo;t
        put anyone outside the pattern this action was built to catch.</p>
      </blockquote>

""" + AD_INLINE + """
      <h2>Why this is a fraud story, not a marketing-spam story</h2>

      <p>Unsolicited calls and mailers offering a &ldquo;free&rdquo; knee brace or genetic testing kit have
      been a known nuisance for years, and it is easy to file every version of that under annoying but
      basically harmless. This action is CMS&rsquo;s own confirmation that the harmless read is sometimes
      wrong: real dollars moved on real claims, using real beneficiary information, for equipment that in
      many cases never reached anyone. An unexpected line item for a piece of equipment is not automatically
      proof of fraud &mdash; billing errors and legitimate items you forgot ordering both happen &mdash; but
      it is no longer reasonable to assume it is always nothing.</p>

      <h2>The part enforcement announcements don&rsquo;t cover</h2>

      <p>Barring a supplier from future payments is a forward-looking action. It stops these eleven
      companies from billing Medicare Advantage plans going forward; it does not retroactively notify every
      individual beneficiary whose identifier may have been used, and it does not automatically refund a
      charge that already went through. CMS enforcement operates at the level of the supplier and the
      program, not the individual statement. Whether your own record was ever touched by any of this is
      not something this announcement answers for you &mdash; it is something only your own Medicare
      Summary Notice or plan statement can.</p>

      <p>That statement is worth knowing how to read regardless of this specific action. If you have
      Original Medicare, CMS mails a Medicare Summary Notice every three months listing every claim billed
      under your number, what Medicare paid, and what you owe. If you have a Medicare Advantage plan, the
      equivalent document is your plan&rsquo;s Explanation of Benefits, and the mailing schedule is set by
      the plan rather than by CMS directly. For Original Medicare, the same claims are available anytime by logging into your Medicare.gov
      account, which is faster than waiting for the next paper mailing. For Medicare Advantage, claims
      go through the plan, so use the plan&rsquo;s member portal or call the number on your card.</p>

      <h2>What a legitimate DME order actually requires</h2>

      <p>One useful fact for telling a real order apart from a fraudulent one: Medicare coverage of
      equipment runs through your own treating practitioner, who has to write an order for the item
      before a supplier bills for it. How much more is required depends on the item. CMS keeps a
      published list of equipment, 83 items as of April 2026, for which a qualifying face-to-face visit
      with the practitioner within the previous six months is required and the written order has to
      reach the supplier before delivery. Power wheelchairs and scooters are on it, and some oxygen
      codes were added in January 2026. Items that are not on the list can still carry their own
      documentation rules. Either way, a caller offering to send you a back brace, a knee sleeve or
      diabetic supplies after a phone quiz &mdash; with no order from your own practitioner &mdash; is
      not describing how the legitimate process works, regardless of how official the call sounds.</p>

      <h2>What to actually do about it</h2>

""" + check([
        'Check your <strong>Medicare Summary Notice</strong> (Original Medicare) or your plan&rsquo;s '
        '<strong>Explanation of Benefits</strong> (Medicare Advantage) for equipment you don&rsquo;t '
        'recognize &mdash; not just once, but each time one arrives.',
        'Never give your <strong>Medicare number</strong> to anyone who calls, mails, or advertises '
        '&ldquo;free&rdquo; braces, equipment or supplies you did not ask for. A real Medicare number is '
        'worth money to exactly this kind of scheme.',
        'A legitimate order comes from your <strong>own treating practitioner</strong>, who writes the '
        'order for the item &mdash; not a phone screening from an unfamiliar company. For items on '
        'CMS&rsquo;s required list, a qualifying visit has to come first.',
        'Suppliers already barred from Original Medicare shifting to bill <strong>Medicare Advantage</strong> '
        'instead was part of the pattern this action targeted &mdash; being on an Advantage plan is not '
        'outside the risk.',
        'If you spot a charge for something you never received, <strong>report it</strong>: 1-800-MEDICARE, '
        'the Senior Medicare Patrol Resource Center at 877-808-2468, or the HHS Office of Inspector '
        'General&rsquo;s hotline at 1-800-HHS-TIPS. You do not need proof to ask that it be looked at.',
        'Barring a supplier stops <strong>future</strong> claims from that company. It does not automatically '
        'refund or flag anything already billed &mdash; checking your own statement is still on you.',
    ]) + """
      <p>The $3.4 billion figure is a measure of what CMS caught, not a measure of what any individual
      reader needs to worry about personally. The part actually worth carrying forward is smaller and more
      durable than the headline: an unexpected item on a Medicare statement is worth a second look, a
      real DME order comes from your own treating practitioner, and reporting a suspicious charge costs you
      nothing but a phone call.</p>
""",
    'sources': [
        ('CMS &mdash; CMS Cracks Down on Massive $3.4 Billion Medical Equipment Supplier Fraud Scheme',
         'https://www.cms.gov/newsroom/press-releases/cms-cracks-down-massive-3-4-billion-medical-equipment-supplier-fraud-scheme'),
        ('Fierce Healthcare &mdash; CMS puts more pressure on DME suppliers as part of anti-fraud push',
         'https://www.fiercehealthcare.com/payers/cms-puts-more-pressure-dme-suppliers-part-anti-fraud-push'),
        ('Senior Medicare Patrol &mdash; Durable Medical Equipment Fraud',
         'https://smpresource.org/medicare-fraud/fraud-schemes/durable-medical-equipment-fraud/'),
        ('Medicare.gov &mdash; Reporting Medicare fraud and abuse',
         'https://www.medicare.gov/basics/reporting-medicare-fraud-and-abuse'),
    ],
    'next': {'slug': 'medicare-card-scam',
             'title': 'The new Medicare card scam, and the real reissue behind it',
             'blurb': 'Another instance of a real federal action creating an opening scammers use to sound '
                      'legitimate.'},
}

# --------------------------------------------- Marketplace unauthorized enrollment
ARTICLES19['aca-unauthorized-enrollment'] = {
    'title': 'CMS Canceled 760,000 Marketplace Enrollments Over Fraud &mdash; The Second Half Guide',
    'eyebrow': 'Facts &amp; thresholds',
    'h1': 'CMS canceled 760,000 Marketplace enrollments over fraud concerns',
    'dek': 'An anti-fraud sweep canceled roughly 315,000 ACA Marketplace enrollments covering '
           'more than 760,000 people, effective August 31 and announced September 22. CMS says every one was confirmed unauthorized; outside analysts '
           'question whether legitimate enrollees could still be caught. Here is how to find out which '
           'side of that you are on.',
    'meta': '5 minute read &middot; Verified against independent reporting on CMS&rsquo;s September 22 '
            'announcement',
    'checked': '9 October 2026',
    'recheck': {'due': '2026-10-20', 'why': 'Marketplace open enrollment approaches -- confirm the appeal '
                'and re-enrollment mechanics described here still match, and check whether CMS published '
                'further guidance for affected consumers.'},
    'body': """      <p>On September 22, 2026, CMS announced that it had canceled roughly 315,000 ACA Marketplace
      enrollments, covering more than 760,000 people, as part of an anti-fraud action targeting
      unauthorized broker-assisted sign-ups. The cancellations themselves took effect on August 31;
      September 22 is the date of the announcement. If you or someone in your household has Marketplace coverage
      &mdash; the bridge many people use between leaving a job and reaching Medicare at 65 &mdash; this is
      worth five minutes of your own checking, regardless of whether you think you did anything wrong.</p>

""" + facts('The action, at a glance', [
        ('315,000', 'Marketplace enrollments CMS canceled, effective August 31 and announced September 22, 2026.'),
        ('760,000+', 'Individual people covered by those canceled enrollments.'),
        ('~$2.2 billion', 'Advance premium tax credit payments CMS expects to recover as a result.'),
        ('Why flagged', 'Enrolled with agent or broker assistance but lacking verified citizenship or '
                        'immigration documentation, or insurers unable to identify the claims or contact '
                        'the enrollee at all.'),
        ('New broker freeze', 'Agents and brokers without an active 2026 Marketplace registration are '
                              'temporarily barred from registering for the 2027 plan year.'),
        ('90 days', 'The standard window to appeal a Marketplace eligibility determination, counted from '
                    'the date on the Eligibility Notice.'),
    ]) + """
      <h2>What actually happened</h2>

      <p>The cancellations trace back to a pattern of broker misconduct CMS had already been investigating:
      agents and brokers &mdash; disproportionately ones newly registered for the 2026 plan year &mdash;
      enrolling people in Marketplace plans without adequate verification, sometimes without the enrollee&rsquo;s
      informed consent at all. CMS paired the cancellations with an interim final rule freezing new broker
      registrations for 2027 unless the agent already had an active 2026 registration, and has issued
      termination notices to more than 200 agents and brokers since January. CMS has also sent 569 notices
      of intent to terminate agreements with brokers whose 2026 applications were missing basic applicant
      information, including Social Security numbers &mdash; the kind of gap that makes an enrollment
      difficult to verify as legitimate in the first place.</p>

      <p>Most of the flagged brokers, by CMS&rsquo;s own account, were new to the Marketplace channel:
      agents who had first registered to sell ACA plans for the 2026 season. New registrants are a small
      share of all broker-assisted enrollments overall, but accounted for a disproportionate share of the
      enrollments flagged as potentially fraudulent &mdash; which is part of why the interim rule targets
      new 2027 registrations specifically, rather than broker activity across the board.</p>

      <p>CMS frames this as recovering federal money paid out on enrollments that should never have existed.
      CMS says the canceled enrollments were confirmed unauthorized. Outside analysts are not as sure
      the process was airtight: KFF&rsquo;s Cynthia Cox told the Associated Press that coverage obtained
      through fraud should be canceled, but questioned whether the government had said enough about how
      the affected people were identified, and reporting has raised the possibility that qualified
      enrollees who missed a notice in time were canceled too. That is a concern from outside the agency,
      not something CMS has conceded.</p>

      <blockquote class="pull">
        <p>An enforcement announcement measures what an agency caught in aggregate. It does not tell any
        individual person which side of that sweep they personally landed on.</p>
      </blockquote>

""" + AD_INLINE + """
      <h2>Why this matters specifically for this site&rsquo;s readers</h2>

      <p>Marketplace coverage is disproportionately used by people in their late fifties and early sixties
      &mdash; old enough to have left an employer plan, too young yet for Medicare at 65. If that describes
      your own coverage or a spouse&rsquo;s, this action is not background noise about a federal program;
      it is a direct question about whether your own household&rsquo;s health coverage is still active
      right now, today, whether or not you have received anything in the mail saying otherwise.</p>

      <h2>The part worth acting on immediately</h2>

      <p>CMS&rsquo;s enforcement action was built around aggregate fraud patterns across a broker channel,
      not around individually notifying every affected household in a way guaranteed to reach them before
      their coverage actually lapses. That is the same structural gap this site has flagged in enforcement
      stories before: the agency&rsquo;s job is closing the pattern, not personally confirming your own
      status to you. Whether your coverage was part of the 315,000 canceled enrollments is something you
      have to check yourself, and doing so costs nothing and takes a few minutes.</p>

      <h2>If your coverage was actually canceled</h2>

      <p>Marketplace eligibility determinations carry a standing appeal right: generally 90 days from the
      date on an Eligibility Notice to file an appeal, through the Marketplace Appeals Center. If you
      believe your own cancellation was an error &mdash; you are a citizen or lawfully present, you did
      respond to any notice you received, or you never used a broker at all &mdash; that appeal path exists
      specifically for this. Filing costs nothing and does not require a lawyer.</p>

      <h2>What to actually do</h2>

""" + check([
        'Log into your <strong>HealthCare.gov</strong> account (or your state&rsquo;s own Marketplace site) '
        'now and confirm your coverage still shows active &mdash; don&rsquo;t assume it is because nothing '
        'has arrived in the mail.',
        'If your coverage was canceled and you believe that was in error, you generally have <strong>90 '
        'days</strong> from the date on your Eligibility Notice to file an appeal through the Marketplace '
        'Appeals Center.',
        'If you need to re-enroll, go directly to <strong>HealthCare.gov</strong> or your state&rsquo;s '
        'official Marketplace &mdash; not a search ad, a social media link, or an unsolicited caller, given '
        'that broker misconduct is exactly what triggered this action in the first place.',
        'Be wary of anyone who calls promising to <strong>restore your coverage</strong> or guarantee a '
        'specific subsidy amount for a fee. The appeal and re-enrollment process is free through official '
        'channels.',
        'Even if your own coverage wasn&rsquo;t affected, confirm the <strong>agent or broker</strong> listed '
        'on your account is one you actually chose yourself &mdash; the new registration freeze exists '
        'because unauthorized agents were being attached to consumer accounts without their knowledge.',
        'If you are newly uninsured because of this and need coverage before Medicare eligibility, act '
        'before your state&rsquo;s <strong>open enrollment</strong> window closes rather than after &mdash; '
        'a gap here can mean a real gap in coverage, not just paperwork.',
    ]) + """
      <p>Nothing about this action requires you to have done anything wrong to be affected by it. The
      single most useful thing to take from it is the five minutes it takes to log in and look &mdash; not
      because the crackdown was necessarily aimed at you, but because whether it was is not something
      anyone is going to reliably tell you first.</p>
""",
    'sources': [
        ('NPR &mdash; HHS cancels health insurance of 760,000 individuals enrolled in healthcare.gov plans',
         'https://www.npr.org/2026/09/22/nx-s1-5977991/hhs-cancels-health-insurance-of-760-000-individuals-enrolled-in-healthcare-gov-plans'),
        ('Forbes &mdash; CMS Canceled ACA Coverage For 760,000 People Over Fraud. Here&rsquo;s What Patients '
         'Should Know',
         'https://www.forbes.com/sites/jessepines/2026/09/23/cms-canceled-aca-coverage-for-760000-people-over-fraud-heres-what-patients-should-know'),
        ('Groom Law Group &mdash; CMS Targets Unauthorized Marketplace Enrollments and Broker Misconduct',
         'https://www.groom.com/resources/cms-targets-unauthorized-marketplace-enrollments-and-broker-misconduct-102o2yg/'),
        ('HealthCare.gov &mdash; What can I appeal?',
         'https://www.healthcare.gov/marketplace-appeals/'),
    ],
    'next': {'slug': 'aca-subsidy-cliff',
             'title': 'The ACA subsidy cliff is back in 2026',
             'blurb': 'The other major change affecting Marketplace coverage in the same window as this '
                      'enforcement action.'},
}
