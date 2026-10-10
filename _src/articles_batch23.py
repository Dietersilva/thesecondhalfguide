#!/usr/bin/env python3
"""Twenty-third batch: four pieces from the second week of October 2026 --
the one-time $90 Part B payment from the Medicare Improvement Fund, the 2027
Medicare Advantage and Part D Star Ratings (published 8 October), CMS's
probationary prior authorization for newly enrolled DMEPOS suppliers (starts
15 October), and the Medicare GLP-1 Bridge ($50 a month, July 2026 through
December 2027).

cms.gov, medicare.gov and ssa.gov are proxy-blocked here, so no primary source
was read directly. Verified per CLAUDE.md section 2 by agreement across
independent reporting that traces to the agency. Deliberately omitted because
only one source gave it, or sources split: the bank/check memo wording for the
$90 payment, the share of Part D enrollees in 4-star drug plans, the 5-star
special enrollment period (broker sources only), DME prior-authorization
decision timeframes beyond CMS's own probationary FAQ, and the 28 October
expansion of required codes (one syndicated release)."""

from build_articles import facts, check, AD_INLINE

ARTICLES23 = {}

CHECKED23 = '10 October 2026'

# ------------------------------------------------------------------ $90 payment
ARTICLES23['medicare-90-payment'] = {
    'title': 'The $90 Medicare Payment: Who Gets It and Who Doesn&rsquo;t &mdash; The Second Half Guide',
    'eyebrow': 'Facts &amp; thresholds',
    'h1': 'The $90 Medicare payment: who gets it and who doesn&rsquo;t',
    'dek': 'A one-time $90 payment is going to people in Original Medicare Part B this month. No application '
           'is needed, but eligibility depends on your kind of Medicare, where you live, whether Medicaid '
           'helps pay your premium and whether you pay IRMAA.',
    'meta': '5 minute read &middot; Checked against CMS&rsquo;s FAQ, Medicare.gov and independent reporting '
            'that cites them',
    'checked': CHECKED23,
    'recheck': {'due': '2026-11-02', 'why': 'Paper checks were due later in October -- confirm the payment '
                'run is complete and no further groups or dates were announced.'},
    'body': """      <p>Medicare is sending a one-time payment of <strong>$90</strong> to people with Original Medicare
      Part B. CMS describes it as coming from the Medicare Improvement Fund and says about 20.8 million
      people are eligible. Most were to receive it by direct deposit on or around October 8, and anyone
      without a deposit account on file gets a Treasury check later in the month.</p>

      <p>The payment is real, it is small, and it comes with a rule that every scammer in the country
      is already using: you do not apply for it, and nobody has to &ldquo;verify&rdquo; anything for it to
      arrive.</p>

""" + facts('The payment, at a glance', [
        ('Amount', '<strong>$90</strong>, one time.'),
        ('Source', 'The Medicare Improvement Fund, per CMS&rsquo;s FAQ. Separate from your monthly Social '
                   'Security benefit.'),
        ('Who is paid', 'People in <strong>Original Medicare Part B</strong> who live in the United States. '
                        'A Medigap policy or a Part D plan on top of Original Medicare does not disqualify '
                        'you.'),
        ('Who is left out', 'People in <strong>Medicare Advantage</strong>; people receiving '
                            '<strong>Medicaid assistance with their Medicare premium</strong>; people who '
                            'pay <strong>IRMAA</strong> (the income-related surcharge); and people living '
                            'outside the U.S.'),
        ('How many', 'About <strong>20.8 million</strong> people, per CMS.'),
        ('How it arrives', 'Direct deposit, most around <strong>October 8</strong>. Otherwise a Treasury '
                           'check mailed later in October.'),
        ('Do you apply?', '<strong>No.</strong> There is no form and no sign-up.'),
        ('Questions', '1-800-MEDICARE (1-800-633-4227).'),
    ]) + """
      <h2>Who is left out, and why that surprises people</h2>

      <p>The exclusions are worth reading slowly, because each one catches a different kind of
      household. (Living in the United States is also a condition of getting the payment.)</p>

      <p><strong>Medicare Advantage.</strong> The payment goes to people in Original Medicare Part B, so a
      person in an Advantage plan is not in the group, even though that person also has Part B.
      Roughly half of people with Medicare are in Advantage plans, which means a large share of the
      Medicare population will see nothing.</p>

      <p><strong>Medicaid premium help.</strong> People receiving Medicaid assistance with their Medicare
      premium are not eligible. This is the exclusion that confuses lower-income readers, who
      might reasonably assume the opposite.</p>

      <p><strong>IRMAA.</strong> People who pay the income-related surcharge are excluded. There is no
      single &ldquo;income cutoff&rdquo; to memorize here: it is the IRMAA status that decides, and that
      status is set by a tax return from two years ago. For 2026, the surcharge starts above $109,000 of
      income for a single filer and $218,000 for a married couple filing jointly, as covered in
      <a href="/irmaa">the piece on IRMAA</a>; anyone paying it, at any bracket, is excluded.
      Several widely shared posts have claimed an
      income cutoff of around $19,000. That figure is a misreading and is not part of the rule.</p>

      <blockquote class="pull">
        <p>The payment goes to a category of enrollment, not to a level of need. Whether you get it
        depends on which kind of Medicare you have and whether anyone else is paying your premium.</p>
      </blockquote>

""" + AD_INLINE + """
      <h2>How it is paid, and what you do not have to do</h2>

      <p>Social Security makes the payment, using the banking information it already has for you.
      Most people with direct deposit set up were to see it around October 8. People without a deposit
      account on file get a paper check at the address Medicare has for them, later in October. If you
      moved recently and your Medicare address is out of date, that is the situation in which a check
      goes astray. Medicare says official address changes for Medicare are made through Social Security.</p>

      <p>You do not log in anywhere, fill in anything or call anyone. Medicare.gov has a page about the
      one-time premium rebate letter, and CMS has published an FAQ. Those are the places the details
      live.</p>

      <h2>The scam that arrives with it</h2>

      <p>Any benefit paid to more than twenty million people is an opening for a call. The pattern is
      predictable: a text, an email or a phone call says the payment is &ldquo;held&rdquo; or
      &ldquo;pending,&rdquo; and that to release it you must confirm a bank account, a Medicare number
      or a Social Security number, or pay a small processing fee. None of that is part of how this
      payment works. If the money is going to reach you, it is going to reach you without your help.</p>

      <p>The same instinct covers the reverse case. If someone tells you that you have been
      &ldquo;approved for extra&rdquo; and need to act before a deadline, the absence of any application
      process is your answer. The longer piece on <a href="/enrollment-scams">why your phone rings more
      in October</a> covers the season&rsquo;s other scripts.</p>

      <h2>If you expected it and it did not come</h2>

      <p>If an expected payment has not arrived, the first things to check are whether one of the
      exclusions applies (a Medicare Advantage plan, Medicaid premium help, IRMAA) and whether the
      deposit or mailing information on file is current.
      Direct deposits can take a short while to show up and paper checks later still, so the
      later-October window matters before concluding anything has gone wrong. For an actual eligibility
      question, 1-800-MEDICARE is the number CMS gives.</p>

      <p>The payment arrives separately from your monthly Social Security benefit and does not replace
      or change it. Eligibility questions are best settled with Medicare directly, at the number
      above, rather than with anyone who contacts you first.</p>

      <p>It is also worth knowing that the payment is not a change to your premium. The Part B
      premium for 2027 has not been announced, and the $90 does not alter what you owe in January.</p>

      <h2>What to check</h2>

""" + check([
        'Which kind of Medicare you have: <strong>Original Medicare</strong> with Part B is in; a '
        '<strong>Medicare Advantage</strong> plan is out.',
        'Whether <strong>Medicaid helps pay your Medicare premium</strong>, or you pay '
        '<strong>IRMAA</strong>. Either one means no payment.',
        'If you have direct deposit with Social Security, look for the deposit. If you do not, watch for a '
        '<strong>Treasury check</strong> later in October at your address on file with Medicare.',
        'The official payment involves no <strong>application</strong>, no fee and no bank-account '
        'verification.',
        'For an eligibility question, call <strong>1-800-MEDICARE (1-800-633-4227)</strong>, a number you '
        'looked up yourself, not one in a text.',
    ]) + """
      <p>The payment is a small, one-time event. What is worth carrying forward is the shape of it: a
      real benefit, an automatic one, and a simple rule for spotting anyone pretending otherwise.</p>
""",
    'sources': [
        ('CMS &mdash; Medicare Improvement Fund Premium Rebate: Frequently Asked Questions',
         'https://www.cms.gov/newsroom/fact-sheets/medicare-improvement-fund-premium-rebate-frequently-asked-questions'),
        ('Medicare.gov &mdash; One-time premium rebate letter',
         'https://www.medicare.gov/basics/forms-publications-mailings/mailings/other/one-time-premium-rebate-letter'),
        ('CNBC &mdash; Medicare beneficiaries may get $90 payment to offset Part B premium',
         'https://www.cnbc.com/2026/10/05/medicare-part-b-beneficiaries-90-payment.html'),
        ('Kiplinger &mdash; Who Qualifies for the New $90 Medicare Part B Rebate?',
         'https://www.kiplinger.com/retirement/medicare/who-qualifies-for-the-new-medicare-part-b-rebate'),
    ],
    'next': {'slug': 'medicare-savings',
             'title': 'The Medicare help millions qualify for and never claim',
             'blurb': 'Some people left out of the payment already have their premium paid through a '
                      'Medicare Savings Program. Here is how those work.'},
}

# ------------------------------------------------------------------ Star Ratings
ARTICLES23['star-ratings-2027'] = {
    'title': 'The 2027 Medicare Star Ratings: What a Star Does and Doesn&rsquo;t Say &mdash; The Second Half Guide',
    'eyebrow': 'Facts &amp; thresholds',
    'h1': 'The 2027 Medicare Star Ratings: what a star does and doesn&rsquo;t say',
    'dek': 'CMS published the 2027 ratings on October 8, a week before open enrollment. About 71% of '
           'Advantage drug-plan members are in a four-star contract or better. That is a statement about '
           'contracts, not about your doctors or your costs.',
    'meta': '6 minute read &middot; Checked against CMS&rsquo;s October 8 fact sheet and independent '
            'reporting that cites it',
    'checked': CHECKED23,
    'body': """      <p>On October 8, CMS published the 2027 Star Ratings for Medicare Advantage and Part D plans on
      the Medicare Plan Finder. They arrive one week before open enrollment begins on October 15, which
      is when most people will see them, usually as a row of stars next to a plan&rsquo;s name.</p>

      <p>Stars are a useful number and an easy one to over-read. Here is what the 2027 ratings say, and
      what they leave out.</p>

""" + facts('The 2027 ratings, at a glance', [
        ('Published', '<strong>October 8, 2026</strong>, on the Medicare Plan Finder. They apply to plan '
                      'year 2027.'),
        ('Advantage drug plans (MA-PD)', 'About <strong>71%</strong> of enrollees are in contracts rated '
                                         '<strong>four stars or more</strong>, weighted by enrollment.'),
        ('Contracts at four or more', 'About <strong>37%</strong> of Advantage drug-plan contracts '
                                      '(188 of them) earned four stars or higher.'),
        ('Average rating', 'MA-PD average <strong>3.99</strong>, down from 4.01 for 2026.'),
        ('Contracts rated', '508 Advantage drug-plan contracts for 2027.'),
        ('Standalone drug plans', 'About <strong>27%</strong> (11 contracts) earned four stars or more.'),
        ('Nonprofit vs. for-profit', 'About 44% of nonprofit contracts earned four or more stars, against '
                                     'about 34% of for-profit Advantage drug-plan contracts.'),
        ('Open enrollment', '<strong>15 October &ndash; 7 December</strong>. Coverage starts 1 January.'),
    ]) + """
      <h2>What the 71% means</h2>

      <p>The headline number is a share of people, not of plans. When CMS says about 71% of
      Advantage drug-plan members are in a contract with four or more stars, it is weighting each
      contract by how many people are enrolled in it. Because large insurers hold most of the
      enrollment, a handful of big contracts can pull the people-weighted figure well above the
      share of contracts. The two numbers on the table show the gap: 71% of members, but 37% of
      contracts.</p>

      <p>The average rating moved the other way. At 3.99 for 2027, the Advantage drug-plan average
      slipped slightly from 4.01 the year before, which is a small change and is not a trend by
      itself. The ratings have been near four for several years.</p>

      <blockquote class="pull">
        <p>A star rating describes a contract&rsquo;s performance on a set of measures. It does not tell
        you whether a given plan covers your doctor, your drugs or your pharmacy.</p>
      </blockquote>

      <h2>What a star is attached to</h2>

      <p>Ratings belong to a <strong>contract</strong>, which is the agreement between CMS and an
      insurer. One contract can cover many different plans in many counties, with different
      premiums, networks and benefits. Two plans with the same stars can look entirely different from
      the inside, because CMS assigns ratings at the contract level and every plan under a contract
      shows that contract&rsquo;s rating. That is why a rating describes a contract well and a single
      plan only loosely.</p>

      <p>The overall rating blends many measures, from how well a plan keeps members healthy to how it
      handles complaints and appeals and how members rate their experience. A single number
      compresses all of that. It is possible for a contract to do well on average and still have a weak
      spot that matters to one person, such as the network in a particular county.</p>

""" + AD_INLINE + """
      <h2>How the ratings have moved</h2>

      <p>The Advantage drug-plan average has hovered near four stars: 4.07 for 2024, 3.95 for 2025,
      4.01 for 2026 and 3.99 for 2027. A reader seeing &ldquo;four stars&rdquo; on a plan is therefore
      seeing roughly the market average, not an outlier. The 37% of contracts at four or more stars
      shows the same thing from the other side: most contracts sit around the middle, and a
      four-star rating is common rather than rare.</p>

      <p>For standalone drug plans the picture is different. Only 11 contracts earned four stars or
      more, about 27%, which is a much smaller group than the Advantage side. CMS also reports a
      difference between nonprofit contracts, where about 44% reached four stars, and for-profit
      Advantage drug-plan contracts, where about 34% did. That is a fact about contracts in the
      ratings, not a finding about any one insurer&rsquo;s plan in your county.</p>

      <h2>Why it matters for the money</h2>

      <p>Star Ratings are not only a consumer tool. They affect what CMS pays plans: higher-rated
      contracts are eligible for quality bonus payments, and CMS says the ratings published for 2027
      will affect Medicare Advantage quality bonus payments for 2028. That gives insurers a strong
      reason to chase four stars, and it is one reason a plan&rsquo;s marketing leans on its rating.
      A rating is real information, but it is also something the seller has every reason to put
      first.</p>

      <h2>The part the stars cannot tell you</h2>

      <p>A four-star contract can leave out the one specialist you see every month. A three-star plan
      can include every doctor and every drug on your list at the lowest cost in the county. The
      national story and the household story are separate, which is the same point made in the piece on
      <a href="/medicare-2027-costs">the 2027 plan numbers</a>: an average describes the market, and
      your plan is a single point in it.</p>

      <p>The ratings also say nothing about whether a plan is staying. Insurers have announced exits
      for 2027 regardless of their stars; the piece on
      <a href="/ma-plan-exits-2027">plans disappearing for 2027</a> covers that, and the notice about it
      was due by October 2.</p>

      <h2>Using the ratings during open enrollment</h2>

      <p>The ratings land at the same time as the other 2027 information. The Annual Notice of Change
      tells you what your current plan is changing; the Plan Finder lets you price the alternatives with
      your own drugs and pharmacy, and shows the Star Ratings alongside the cost and benefit
      information. A star rating does not replace a plan&rsquo;s provider network, drug list, pharmacy
      network and cost sharing, which are the things that decide whether a plan covers what you
      use.</p>

      <p>Plans also change from year to year, and so do ratings. A rating published in October describes
      performance measured earlier, which means a plan&rsquo;s 2027 coverage and its 2027 stars are
      not measures of the same thing. The stars describe how a contract has done; the Plan Finder
      describes what it will offer.</p>

      <h2>What to check</h2>

""" + check([
        'The Plan Finder shows Star Ratings next to each plan&rsquo;s <strong>premium, deductible, '
        'copays, network and drug list</strong>; the rating does not replace any of them.',
        'A rating belongs to a <strong>contract</strong> that can cover many plans, so several plans '
        'can show the same stars.',
        'Your own <strong>doctors, drugs and pharmacy</strong> are checked in the Plan Finder, not by '
        'the rating.',
        'Your <strong>Annual Notice of Change</strong> lists what changes in your own plan for 2027.',
        'Open enrollment runs <strong>15 October through 7 December</strong>; changes take effect '
        '1 January.',
    ]) + """
      <p>The stars are one number among many. Used for what they are, a rough measure of how a
      contract performed, they help. Used as a verdict on your own coverage, they say more than they
      can.</p>
""",
    'sources': [
        ('CMS &mdash; 2027 Medicare Advantage and Part D Star Ratings (fact sheet)',
         'https://www.cms.gov/newsroom/fact-sheets/2027-medicare-advantage-part-d-star-ratings'),
        ('CMS &mdash; Part C and D Performance Data',
         'https://www.cms.gov/medicare/health-drug-plans/part-c-d-performance-data'),
        ('Fierce Healthcare &mdash; CMS releases the 2027 Medicare Advantage star ratings',
         'https://www.fiercehealthcare.com/payers/cms-about-71-mapd-plan-enrollees-coverage-four-or-more-stars-2027'),
    ],
    'next': {'slug': 'open-enrollment',
             'title': 'Open enrollment: what the 15 October window is actually for',
             'blurb': 'The window these ratings arrived for, and what it lets you change.'},
}

# ------------------------------------------------------- DME probationary prior auth
ARTICLES23['dme-prior-authorization'] = {
    'title': 'The Equipment Prior-Authorization Change Starting October 15 &mdash; The Second Half Guide',
    'eyebrow': 'Facts &amp; thresholds',
    'h1': 'The equipment prior-authorization change starting October 15',
    'dek': 'Starting October 15, CMS requires some newly enrolled equipment suppliers to get approval '
           'before delivering and billing certain items. It applies to the supplier, not to every patient or every '
           'product.',
    'meta': '6 minute read &middot; Checked against CMS&rsquo;s program page, a Medicare contractor&rsquo;s '
            'guidance and trade reporting',
    'checked': CHECKED23,
    'recheck': {'due': '2026-11-15', 'why': 'A month after the start -- confirm the effective date held and '
                'check whether CMS changed the item list or the suppliers covered.'},
    'body': """      <p>Beginning <strong>October 15, 2026</strong>, CMS is introducing what it calls
      <em>probationary prior authorization</em> for certain durable medical equipment, prosthetics,
      orthotics and supplies, usually shortened to DMEPOS. It applies to suppliers that are newly
      enrolled in Medicare, or that go through certain changes in ownership, and it covers a list of
      designated items.</p>

      <p>It reads like a patient-facing rule and is not one. The requirement sits with the supplier. It
      arrives in the same month as the equipment-fraud crackdown covered earlier on this site.</p>

""" + facts('The change, at a glance', [
        ('Start date', '<strong>October 15, 2026</strong>.'),
        ('Who it applies to', '<strong>Newly enrolled</strong> DMEPOS suppliers, and suppliers with '
                              'certain <strong>changes of ownership</strong>, effective on or after '
                              'that date.'),
        ('What they must do', 'Get <strong>prior authorization</strong> before furnishing a designated '
                              'item and submitting the Medicare claim.'),
        ('How long', 'A <strong>one-year</strong> probationary period, beginning with the '
                     'supplier&rsquo;s first bill for a listed item.'),
        ('Which items', 'A CMS list of designated codes, including <strong>orthoses</strong> '
                        '(braces) and related devices. CMS publishes the full list.'),
        ('Who it does not apply to', 'Suppliers outside the new-enrollment and ownership-change group. '
                                     'The existing prior-authorization program is separate and '
                                     'continues.'),
    ]) + """
      <h2>What prior authorization is</h2>

      <p>Prior authorization is a review that happens <em>before</em> an item is delivered and billed.
      The supplier sends the documentation to a Medicare contractor, which decides whether the request
      appears to meet coverage rules. A &ldquo;provisional affirmation&rdquo; means a later claim is
      likely to be paid, provided the other requirements are met. A non-affirmation means it likely
      would not be. The point is to catch items that do not meet the rules before Medicare pays for
      them, not after.</p>

      <p>CMS has set the probationary version to move quickly. Its FAQ says the contractors send decision
      letters by the fifth business day after receiving a request, and there is a faster route when
      waiting could seriously jeopardize a patient&rsquo;s health.</p>

      <h2>Why it is aimed at new suppliers</h2>

      <p>The logic is straightforward. A supplier that enrolled last month has no billing history to
      examine, so the review moves to the front: approval first, payment after. A supplier with years of
      claims behind it is in a different position, and the probationary period applies to the first
      kind. It is a way of looking closely at billing in the first year.</p>

      <blockquote class="pull">
        <p>The rule is about who is billing, not about who is buying. A new supplier gets a year of
        closer review; an established one does not.</p>
      </blockquote>

""" + AD_INLINE + """
      <h2>What a patient could notice</h2>

      <p>Most patients will notice nothing. The probationary program applies to newly enrolled or
      ownership-changing suppliers; established suppliers can still be subject to Medicare&rsquo;s
      existing equipment prior-authorization requirements, which are a separate program. If you get one of the designated items from a supplier that is new to Medicare, the
      supplier has to have the approval in hand before it delivers the item and bills, which can mean
      a short wait.  That is a reason to ask early rather than a reason to worry.</p>

      <p>It is not a requirement that you do anything. The supplier submits the request. What you can
      do is ask the supplier whether the item needs prior authorization and whether it has been
      submitted, and keep the name and phone number of the person you spoke with.</p>

      <h2>Where it sits in Medicare</h2>

      <p>CMS runs this as one of its fee-for-service compliance programs, which means it concerns
      Original Medicare billing. Medicare Advantage plans set their own authorization rules, and those
      are separate from this one. The existing prior-authorization program for certain equipment
      continues to apply to suppliers generally; the probationary program is an additional layer for
      the newly enrolled.</p>

      <p>Suppliers affected are told directly. CMS&rsquo;s enrollment contractors send notification
      letters and welcome packets, so a new supplier is not left to discover the requirement on its
      own. For a patient, the practical effect is that a supplier should already know whether it is
      under the probationary rule.</p>

      <h2>If a request is not approved</h2>

      <p>A non-affirmation is not a dead end. CMS&rsquo;s prior-authorization rules allow a supplier to
      correct the documentation and resubmit, and there is no cap on resubmissions. What does not
      work is billing around the process: a claim for a designated item without an affirmation is
      subject to denial. If a supplier tells you an item is on hold, the question to ask is what the
      contractor said was missing.</p>

      <h2>What it is not</h2>

      <p>It is not a new requirement for every piece of equipment, and it is not a change to what
      Medicare covers. The existing rules about orders and documentation still apply, including the
      required list of items that need a face-to-face visit and a written order before delivery,
      described in <a href="/medical-equipment-fraud">the piece on the equipment fraud crackdown</a>.
      Prior authorization is an extra checkpoint for a defined group of suppliers and items, layered on
      top of those rules.</p>

      <p>It does not change what you pay either. For covered equipment under Original Medicare, the usual cost is 20% of the
      Medicare-approved amount after the Part B deductible when the supplier accepts assignment; a
      supplier that does not accept assignment can cost more. The new checkpoint affects timing and
      billing, not those rules.</p>

      <p>It is also not a sign that a supplier is doing anything wrong. A new business has to start
      somewhere, and this is a condition of starting.</p>

      <h2>Questions worth asking a supplier</h2>

      <p>None of these is a test a supplier should fail for being new. They are the questions an
      ordinary customer asks of any business that is about to bill a government program in their name.
      Is this item one that needs prior authorization? Has the request gone in, and when? Who is the
      practitioner whose order it rests on? If there is a delay, whom do I call? A supplier that is
      working correctly answers all four without difficulty.</p>

      <h2>What to check</h2>

""" + check([
        'If you are getting equipment, ask whether the supplier is <strong>new to Medicare</strong> and '
        'whether the item needs <strong>prior authorization</strong>.',
        'Ask whether the request has been <strong>submitted and approved</strong> before you expect '
        'delivery.',
        'Your own <strong>practitioner&rsquo;s order</strong> is still the starting point for any covered '
        'item.',
        'Check your <strong>Medicare Summary Notice</strong> or plan statement for equipment you did not '
        'receive, and report it to <strong>1-800-MEDICARE</strong>.',
    ]) + """
      <p>The change is narrow and mostly invisible to people who already deal with established
      suppliers. Its significance is the direction: more scrutiny at the point where a new supplier
      first bills Medicare.</p>
""",
    'sources': [
        ('CMS &mdash; Probationary Prior Authorization Process for Newly Enrolled Suppliers of Certain '
         'DMEPOS Items',
         'https://www.cms.gov/data-research/monitoring-programs/medicare-fee-service-compliance-programs/prior-authorization-pre-claim-review-initiatives/probationary-prior-authorization-process-newly-enrolled-suppliers-certain-durable-medical-equipment'),
        ('CMS &mdash; Probationary Prior Authorization process, FAQs',
         'https://www.cms.gov/files/document/dmepos-ppa-faqs.pdf'),
        ('CGS Medicare &mdash; Probationary Prior Authorization (PPA) for Certain Newly Enrolled DMEPOS '
         'Suppliers',
         'https://www.cgsmedicare.com/jc/pa/probationary-prior-authorization.html'),
        ('Ossur &mdash; CMS Introduces Probationary Prior Authorization for Newly Enrolled DMEPOS '
         'Suppliers',
         'https://www.ossur.com/en-us/professionals/ossur-rr/cms-introduces-probationary-prior-authorization-for-newly-enrolled-dmepos-suppliers'),
    ],
    'next': {'slug': 'medical-equipment-fraud',
             'title': 'The medical equipment fraud crackdown, and what to check on your own statement',
             'blurb': 'The enforcement story behind the change, and how to read your own claims.'},
}

# ------------------------------------------------------------------ GLP-1 Bridge
ARTICLES23['glp1-bridge'] = {
    'title': 'The Medicare GLP-1 Bridge: $50 a Month, With Conditions &mdash; The Second Half Guide',
    'eyebrow': 'Facts &amp; thresholds',
    'h1': 'The Medicare GLP-1 Bridge: $50 a month, with conditions',
    'dek': 'Through the end of 2027, some people in Part D can get certain weight-loss GLP-1 drugs for $50 '
           'a month. It is a temporary program with a specific drug list, clinical criteria and its own '
           'approval path that starts at the pharmacy.',
    'meta': '6 minute read &middot; Checked against Medicare.gov and CMS materials as reported by '
            'independent sources',
    'checked': CHECKED23,
    'recheck': {'due': '2026-12-01', 'why': 'CMS says the eligible drug list can change -- confirm the '
                'current drugs and criteria on CMS.gov and Medicare.gov.'},
    'body': """      <p>Original Medicare&rsquo;s drug benefit has not generally paid for drugs used only for weight
      loss. The <strong>Medicare GLP-1 Bridge</strong> is a short-term CMS demonstration that changes
      that for a defined group, from <strong>July 1, 2026 through December 31, 2027</strong>. Eligible
      people in a Part D plan pay <strong>$50</strong> for a one-month supply of certain covered drugs.</p>

      <p>It is a real program with real limits. Most of what matters is in the conditions.</p>

""" + facts('The Bridge, at a glance', [
        ('Runs', '<strong>July 1, 2026 &ndash; December 31, 2027</strong>.'),
        ('Cost', '<strong>$50</strong> for a one-month (28- or 30-day) supply.'),
        ('Who', 'People with Part D drug coverage, through a standalone plan or an eligible Medicare '
                'Advantage plan that includes it, with a prescription for <strong>weight '
                'management</strong> who meet the clinical criteria.'),
        ('Drugs (as of July 1)', 'Wegovy in all forms, Foundayo in all forms, and Zepbound in the '
                                 '<strong>KwikPen</strong> only. CMS says the list may change.'),
        ('Clinical criteria', 'A BMI of 35 or more; or 30 or more with heart failure with preserved '
                              'ejection fraction, uncontrolled hypertension despite treatment, or chronic '
                              'kidney disease stage 3a or above; or 27 or more with prediabetes, a prior '
                              'heart attack, a prior stroke or symptomatic peripheral artery disease '
                              '(poor circulation in the legs or arms that causes symptoms). The BMI '
                              'counted is the one when treatment started.'),
        ('Not eligible', 'Anyone whose GLP-1 is for an indication Part D already covers: type 2 diabetes, '
                         'moderate-to-severe obstructive sleep apnea, or noncirrhotic MASH with '
                         'moderate-to-advanced liver fibrosis. Those go through the Part D plan.'),
        ('How approval works', 'It starts at the <strong>pharmacy</strong>. A <strong>CMS central '
                               'processor</strong>, not your Part D plan, handles the prior '
                               'authorization.'),
    ]) + """
      <h2>What the program is, and what it is not</h2>

      <p>The Bridge is a demonstration, not a change to Medicare&rsquo;s benefit. It is meant to cover
      a gap while CMS works out longer-term coverage, and it ends on a fixed date. Part D plans stay out
      of the flow: they do not carry the cost or the risk of the covered drugs, and the prior
      authorization and the pharmacy payment run through a processor CMS set up for the purpose.</p>

      <p>Those drugs are also not covered through the usual Part D benefit for weight loss, which is why
      the program exists. For people who take GLP-1 drugs for type 2 diabetes, nothing here applies;
      those prescriptions are handled through the person&rsquo;s Part D plan, subject to that
      plan&rsquo;s coverage rules, which is why diabetes is on the exclusion list for the Bridge
      itself.</p>

      <blockquote class="pull">
        <p>The Bridge is a temporary program with a fixed end date, a short drug list and its own
        approval route. It is not a standing benefit.</p>
      </blockquote>

      <h2>The conditions that decide it</h2>

      <p>Three layers have to line up. The first is the coverage: you need Part D drug coverage, which can be a standalone plan or an
      eligible Medicare Advantage plan that includes it. The second is the prescription: it has to be for weight management, and it has to be for a use Part D does not
      already cover. The
      third is the clinical profile, which CMS sets out as a BMI threshold that rises or falls with
      specific other conditions. A higher BMI qualifies on its own; a lower one qualifies only with a
      listed condition alongside it. Certain diagnoses rule a person out altogether.</p>

      <p>The drug list is narrower than many people assume. Not every GLP-1 is on it, and for Zepbound
      only the KwikPen counts. A prescription written for a product that is not on the list will not
      go through the Bridge.</p>

""" + AD_INLINE + """
      <h2>How the money works</h2>

      <p>The $50 is a copay for a one-month supply, and it has two features that surprise people. It
      does not count toward your Part D deductible or toward the annual out-of-pocket cap. And it does
      not change with a low-income subsidy: people who receive Extra Help are eligible if they have
      Part D, but they still pay the $50. The cap and the deductible are covered in
      <a href="/drug-cap">the piece on the drug cap</a>; this program sits outside both.</p>

      <p>The visit and any care-plan fees are billed separately, so the $50 is the price of the drug,
      not of the whole course of care.</p>

      <h2>What the Bridge leaves alone</h2>

      <p>People who take Ozempic or Mounjaro for type 2 diabetes stay in their Part D plan, which
      handles those prescriptions under its own coverage rules. The Bridge is for weight management with the three drugs on the
      list. It is also not a route to compounded versions of these medicines, which are not covered
      under the program.</p>

      <p>It sits next to two other 2027 changes covered here. The Part D out-of-pocket cap rises to
      $2,400 in 2027, and the first negotiated prices for a second round of drugs take effect in
      January, as described in
      <a href="/drug-negotiation-2027">the piece on the next round of Medicare drug discounts</a>.
      The Bridge is separate from both and ends on its own date.</p>

      <h2>How a person actually gets it</h2>

      <p>The process starts when the prescriber sends an eligible prescription to a pharmacy. The
      pharmacy checks Bridge eligibility with a claim and, if prior authorization is needed, sends the
      request to the prescriber. The prescriber then submits the required form to the CMS central
      processor, and the pharmacy fills the prescription once it is approved. CMS notes that a
      prescriber who tries to start the prior authorization before the pharmacy has submitted that
      first claim will get a &ldquo;patient not found&rdquo; error, and that the processor&rsquo;s
      decision can take up to 72 hours.</p>

      <p>A person cannot sign up on their own, and no website will enroll you in it. That is the
      practical test for anyone offering to arrange access for a fee: the official route runs through a
      prescriber and a pharmacy, and costs nothing beyond the $50 and the care itself.</p>

      <p>One more detail worth knowing: if your Medicare drug plan is already paying for your GLP-1,
      that medication continues through the plan rather than switching to the Bridge.</p>

      <h2>What happens after 2027</h2>

      <p>The Bridge ends on December 31, 2027. CMS describes it as short-term and has not described what
      replaces it in the materials reported here. Anyone planning around the $50 price should treat it
      as a price that exists for a fixed window and check what has been announced as that date nears.
      That is a fact about the program&rsquo;s design, not a prediction about what comes next.</p>

      <h2>What to check</h2>

""" + check([
        'You need <strong>Part D drug coverage</strong>, standalone or through an eligible Medicare '
        'Advantage plan. Original Medicare alone, with no drug plan, does not qualify.',
        'Ask your prescriber whether you meet the <strong>clinical criteria</strong> and whether the '
        'drug is on the <strong>current list</strong>. CMS says the list may change.',
        'The sequence runs <strong>prescriber to pharmacy, pharmacy to prescriber, prescriber to CMS&rsquo;s '
        'central processor</strong>. You do not apply yourself.',
        'The <strong>$50</strong> does not count toward your Part D deductible or out-of-pocket cap, and '
        'it is not reduced by Extra Help.',
        'Be wary of anyone offering to <strong>arrange access for a fee</strong> or asking for a Medicare '
        'number by phone or text.',
    ]) + """
      <p>The Bridge is an answer to a specific question, which is who can get certain weight-loss drugs
      at a set price until the end of 2027. Whether it applies to a given person is a conversation
      between that person and a prescriber, with the list and the criteria in hand.</p>
""",
    'sources': [
        ('Medicare.gov &mdash; Medicare GLP-1 Bridge: GLP-1 Drugs for $50 a Month (fact sheet)',
         'https://www.medicare.gov/publications/12234-medicare-glp-1-bridge-glp-1-drugs-for-50-a-month.pdf'),
        ('CMS &mdash; Medicare GLP-1 Bridge: Information for Providers',
         'https://www.cms.gov/medicare/coverage/prescription-drug-coverage/medicare-glp-1-bridge/information-providers'),
        ('National Council on Aging &mdash; The Medicare GLP-1 Bridge Program: Eligibility, Costs, and '
         'Coverage',
         'https://www.ncoa.org/article/expanding-access-to-weight-loss-medications-the-medicare-glp-1-bridge-program/'),
        ('AMCP &mdash; CMS Releases Frequently Asked Questions on the Medicare GLP-1 Bridge',
         'https://www.amcp.org/regulatory-newsbreak-cms-releases-frequently-asked-questions-medicare-glp-1-bridge'),
    ],
    'next': {'slug': 'drug-negotiation-2027',
             'title': 'The next round of Medicare drug discounts arrives in January',
             'blurb': 'The other major change to what Medicare pays for drugs, effective 1 January.'},
}
