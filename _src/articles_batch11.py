#!/usr/bin/env python3
"""Eleventh batch: the Social Security overpayment clawback rate change,
the COBRA-to-Medicare penalty trap, and the Medicare Advantage OEP window
people confuse with AEP."""

from build_articles import facts, check, AD_INLINE

ARTICLES11 = {}

# Verified 27 August 2026, independent of the shared CHECKED constant used
# by earlier batches -- these three are newly researched.
CHECKED11 = '27 August 2026'

# --------------------------------------------------------- overpayment clawback
ARTICLES11['overpayment-clawback'] = {
    'title': 'The Social Security Overpayment Letter, and the Deadline Inside It &mdash; The Second Half Guide',
    'eyebrow': 'Facts &amp; thresholds',
    'h1': 'The Social Security overpayment letter, and the deadline inside it',
    'dek': 'SSA can now take half of your monthly check to recover an overpayment that may not even '
           'have been your fault. Two deadlines inside the letter decide whether that starts '
           'immediately or not at all.',
    'meta': '6 minute read &middot; Verified against SSA guidance',
    'checked': CHECKED11,
    'body': """      <p>An overpayment notice tells you SSA paid you more than it should have and wants the difference
      back. It happens more often than people expect — a return to work that changed the earnings test,
      a marital status change, an administrative error on SSA&rsquo;s own end — and the amount can run into
      the thousands. What decides how badly it hurts is not the letter itself, but how fast you respond to
      it.</p>

""" + facts('The rule, precisely', [
        ('The current default rate', 'Up to <strong>50% of your monthly benefit</strong> withheld, for '
                                     'Title II overpayments (retirement, survivors and disability) on '
                                     'notices sent on or after April 25, 2025.'),
        ('SSI is different', 'Supplemental Security Income overpayments are withheld at a separate, lower '
                             '<strong>10%</strong> default rate, unaffected by the Title II change.'),
        ('It moved twice in two months', 'SSA briefly announced reverting to <strong>100%</strong> '
                                         'withholding in March 2025, then reversed that to the current 50% '
                                         'default a few weeks later, before the 100% rate took effect.'),
        ('Two different remedies', 'A <strong>reconsideration</strong> (Form SSA-561) disputes that you '
                                   'were overpaid, or the amount. A <strong>waiver</strong> (Form SSA-632) '
                                   'concedes the overpayment but argues it wasn&rsquo;t your fault and you '
                                   'can&rsquo;t afford to repay it. You can file both at once.'),
        ('No deadline on the waiver', 'There is no time limit to request a waiver. There is a time limit '
                                      'that determines whether withholding pauses while SSA decides.'),
    ]) + """
      <h2>The part that actually decides the outcome</h2>

      <p>File within <strong>30 days</strong> of the date on the notice — either a reconsideration or a
      waiver request — and withholding does not start at all while SSA reviews it. Miss that window and
      file later, and withholding can already be underway by the time your request is filed; filing then
      suspends further withholding while the review is pending, but does not undo what was already taken.
      A reconsideration filed within 60 days still pauses withholding during review; after that, it may
      not.</p>

      <p>The waiver itself has no deadline — you can request one at any time. But requesting it inside
      that first 30 days is what keeps money in your check while you wait for an answer, rather than
      having to get it back later if you win.</p>

      <blockquote class="pull">
        <p>The overpayment amount is fixed by the time the letter arrives. What is still negotiable is
        whether half your check disappears starting this month, or not until SSA has actually decided
        you&rsquo;re wrong.</p>
      </blockquote>

""" + AD_INLINE + """
      <h2>What to actually do with the letter</h2>

""" + check([
        'Read the <strong>date on the notice</strong>, not the date you opened the envelope. The 30-day '
        'and 60-day clocks run from the notice date.',
        'If you think the overpayment is <strong>wrong or the amount is off</strong>, file Form '
        '<strong>SSA-561</strong> (Request for Reconsideration).',
        'If you don&rsquo;t dispute it but <strong>can&rsquo;t afford the withholding</strong> or it '
        'wasn&rsquo;t your fault, file Form <strong>SSA-632</strong> (Request for Waiver).',
        'When in doubt, <strong>file both at the same time</strong> — they address different questions '
        'and one does not substitute for the other.',
        'If your income comes from <strong>SSI</strong> rather than retirement, survivors or disability '
        'benefits, remember the 10% default rate applies to you, not the 50% Title II rate.',
        'You can also request a <strong>different repayment rate</strong> than SSA&rsquo;s default without '
        'disputing the overpayment at all — a lower, negotiated monthly amount is often available for the '
        'asking.',
    ]) + """
      <p>None of this is a reason to ignore a legitimate overpayment — it is a reason to open the letter
      the day it arrives rather than the week after, since the calendar inside it, not the balance, is
      what most people lose control of first.</p>
""",
    'sources': [
        ('SSA &mdash; What can I do if I&rsquo;m notified that I have an overpayment?',
         'https://www.ssa.gov/faqs/en/questions/KA-02345.html'),
        ('SSA &mdash; Resolve an overpayment',
         'https://www.ssa.gov/manage-benefits/resolve-overpayment'),
        ('SSA &mdash; Form SSA-632, Request for Waiver of Overpayment Recovery',
         'https://www.ssa.gov/forms/ssa-632.html'),
        ('SSA &mdash; Understanding SSI Overpayments',
         'https://www.ssa.gov/ssi/text-overpay-ussi.htm'),
    ],
    'next': {'slug': 'cobra-medicare-trap',
             'title': 'The COBRA-to-Medicare trap',
             'blurb': 'Another deadline-driven rule with a permanent penalty for missing it.'},
}

# ------------------------------------------------------- COBRA/Medicare trap
ARTICLES11['cobra-medicare-trap'] = {
    'title': 'The COBRA-to-Medicare Trap &mdash; The Second Half Guide',
    'eyebrow': 'Facts &amp; thresholds',
    'h1': 'The COBRA-to-Medicare trap',
    'dek': 'COBRA can keep your health plan going after a job ends. It does not keep you safe from '
           'Medicare&rsquo;s late-enrollment penalty — and the clock most people think COBRA pauses is '
           'actually already running.',
    'meta': '6 minute read &middot; Verified against CMS, DOL and Medicare rules',
    'checked': CHECKED11,
    'body': """      <p>COBRA lets you keep the exact health plan you had at work after you leave a job, for up to 18
      months, if you pay the full premium yourself. For someone leaving work at 63 or 64, that can look
      like a bridge all the way to Medicare. The mistake it invites is assuming COBRA also bridges the
      Medicare enrollment clock. It does not.</p>

""" + facts('COBRA, briefly', [
        ('How long', 'Generally <strong>18 months</strong> after a qualifying event like job loss, for '
                     'employers with 20 or more workers.'),
        ('What it costs', 'The full premium — employee and employer share combined — plus up to a 2% '
                          'administrative fee. Often several times what was deducted from a paycheck.'),
        ('What you get', 'The identical plan you had while employed. You cannot switch to a different '
                         'plan through COBRA.'),
        ('The election window', 'Generally <strong>60 days</strong> from losing coverage or from the '
                                'COBRA notice, whichever is later, to elect it.'),
    ]) + """
      <h2>Where it goes wrong at 65</h2>

""" + facts('The trap, precisely', [
        ('COBRA is not creditable coverage for Part B', 'Medicare does not treat COBRA as coverage based '
                                                         'on current employment. It does not delay or '
                                                         'excuse Medicare enrollment the way an active '
                                                         'employer plan does.'),
        ('The clock starts at job loss, not at COBRA&rsquo;s end', 'Your Medicare enrollment window is '
                                                                    'generally tied to when active '
                                                                    'employment (and the group health plan '
                                                                    'that came with it) actually ended — '
                                                                    'not to how long COBRA continues '
                                                                    'afterward.'),
        ('The penalty is permanent', 'Miss the window while relying on COBRA and the Part B late-enrollment '
                                     'penalty — roughly 10% of the premium for each full 12-month period '
                                     'you could have enrolled but did not — applies for as long as you '
                                     'have Part B, which for most people is the rest of their life.'),
        ('Part D is treated differently', 'Some COBRA plans do include creditable drug coverage for Part D '
                                          'purposes, but this has to be confirmed with the plan directly — '
                                          'it is not automatic the way it is not automatic for Part B '
                                          'either.'),
    ]) + """
      <blockquote class="pull">
        <p>COBRA and an active employer plan can look identical from the inside — same card, same
        network, same premium structure minus the employer&rsquo;s share. Medicare does not see them the
        same way.</p>
      </blockquote>

""" + AD_INLINE + """
      <h2>What actually protects you</h2>

      <p>The safe route is enrolling in Medicare on its own schedule regardless of what COBRA is doing —
      generally within the seven-month window centered on turning 65, covered in more detail in <a
      href="/medicare-enrollment">the Medicare enrollment deadline piece</a> on this site. If you are
      leaving a job at or after 65 with <em>active</em> employer coverage, that coverage can open a
      genuine Special Enrollment Period; COBRA taken after that employment ends is a different thing and
      does not reopen or extend that window.</p>

""" + check([
        'If you are turning 65 while on COBRA, <strong>enroll in Medicare on schedule anyway</strong>. '
        'Do not wait for COBRA to run out.',
        'Confirm directly with your COBRA plan administrator whether the drug coverage is '
        '<strong>creditable for Part D</strong> — do not assume it, either way.',
        'Once Medicare starts, <strong>COBRA is often no longer the primary payer</strong> and can end '
        'early as a result — ask the plan administrator how your specific COBRA coverage responds to '
        'Medicare enrollment.',
        'If you are unsure whether your situation counts as &ldquo;active employment&rdquo; coverage versus '
        '<strong>COBRA continuation</strong>, that distinction is the one to get an SSA or SHIP counselor '
        'to confirm before assuming either way.',
        'Consider Medigap timing too: enrolling in Medicare while still effectively covered by COBRA can '
        'affect your <a href="/medigap-window">one-time Medigap open enrollment window</a>, which starts '
        'when Part B starts, not when other coverage ends.',
    ]) + """
      <p>Eighteen months of COBRA feels like a plan. The Medicare clock underneath it runs on its own
      schedule regardless, and the penalty for guessing wrong about that does not go away once you
      notice it.</p>
""",
    'sources': [
        ('CMS &mdash; COBRA Continuation Coverage',
         'https://www.cms.gov/cciio/programs-and-initiatives/other-insurance-protections/cobra_fact_sheet'),
        ('U.S. Department of Labor &mdash; FAQs on COBRA Continuation Health Coverage for Workers',
         'https://www.dol.gov/agencies/ebsa/about-ebsa/our-activities/resource-center/faqs/cobra-continuation-health-coverage-workers'),
        ('Medicare &mdash; Part B late enrollment penalty',
         'https://www.medicare.gov/basics/costs/medicare-costs/avoid-penalties'),
    ],
    'next': {'slug': 'medicare-advantage-oep',
             'title': 'The other Medicare enrollment window, in January',
             'blurb': 'A second, narrower window that only opens after you are already on Medicare Advantage.'},
}

# --------------------------------------------------- Medicare Advantage OEP
ARTICLES11['medicare-advantage-oep'] = {
    'title': 'The Other Medicare Enrollment Window, in January &mdash; The Second Half Guide',
    'eyebrow': 'Facts &amp; thresholds',
    'h1': 'The other Medicare enrollment window, in January',
    'dek': 'Fall&rsquo;s Annual Enrollment Period isn&rsquo;t the only chance to change Medicare coverage. '
           'A second, narrower window opens every January &mdash; but only for people already on Medicare '
           'Advantage, and only once.',
    'meta': '5 minute read &middot; Verified against CMS enrollment rules',
    'checked': CHECKED11,
    'body': """      <p>Most of what gets said about changing Medicare coverage points to the fall — the <a
      href="/open-enrollment">Annual Enrollment Period</a>, October 15 through December 7. That is the big
      one, but it is not the only one. A second, considerably narrower window opens every January, and it
      is easy to confuse with the first.</p>

""" + facts('The two windows, side by side', [
        ('Annual Enrollment Period (AEP)', 'October 15 &ndash; December 7. Open to <strong>everyone on '
                                           'Medicare</strong>. Switch between Original Medicare and '
                                           'Medicare Advantage in either direction, change Advantage plans, '
                                           'change Part D plans.'),
        ('Medicare Advantage Open Enrollment Period (MA OEP)', 'January 1 &ndash; March 31. Open only to '
                                                                'people <strong>already enrolled in a '
                                                                'Medicare Advantage plan</strong> on '
                                                                'January 1.'),
        ('What MA OEP allows', 'One change: switch to a <strong>different Medicare Advantage plan</strong>, '
                               'or drop Advantage entirely and return to <strong>Original Medicare</strong> '
                               '(picking up a standalone Part D plan at the same time, if returning to '
                               'Original Medicare).'),
        ('What it does not allow', 'You cannot use MA OEP to switch <em>into</em> Medicare Advantage from '
                                   'Original Medicare, and you cannot use it to change a standalone Part D '
                                   'plan while staying on Original Medicare.'),
        ('One change only', 'Unlike AEP, which allows changing your mind more than once before it ends, '
                            'MA OEP permits a single plan change during the window.'),
    ]) + """
      <h2>Why the two get confused</h2>

      <p>Both are commonly called &ldquo;Medicare open enrollment&rdquo; in casual conversation, which is
      exactly the source of the confusion. AEP is the broad one, open to anyone with Medicare, that most
      marketing and most news coverage is actually about. MA OEP is a narrower do-over, specifically for
      people who used AEP (or any other window) to land on a Medicare Advantage plan and, within the first
      few months of the year, decide it isn&rsquo;t working for them.</p>

      <p>A common real scenario: someone switches to a new Medicare Advantage plan during AEP in the fall,
      the plan takes effect January 1, and within weeks they discover a doctor they need is out of network
      or a drug isn&rsquo;t covered the way they expected. MA OEP exists for exactly that — one more
      chance to correct course before locking in for the rest of the year.</p>

      <blockquote class="pull">
        <p>AEP is where most people make their decision. MA OEP is where some people get to unmake it —
        once, and only if they were already on Medicare Advantage to begin with.</p>
      </blockquote>

""" + AD_INLINE + """
      <h2>Worth knowing</h2>

""" + check([
        'If you are on <strong>Original Medicare</strong> as of January 1, MA OEP does not apply to you '
        'at all — it only opens for existing Medicare Advantage enrollees.',
        'The change you make during MA OEP takes effect the <strong>first day of the month after</strong> '
        'the plan receives your request, not January 1 retroactively.',
        'If you return to Original Medicare during MA OEP, you can pick up a <strong>standalone Part D '
        'plan</strong> at the same time — this is one of the few times you can newly enroll in Part D '
        'outside AEP without a separate qualifying event.',
        'Returning to Original Medicare here does <strong>not</strong> reopen your one-time <a '
        'href="/medigap-window">Medigap guaranteed-issue window</a> unless you separately qualify for a '
        'protection under your state&rsquo;s rules or a federal trial-right provision.',
        'Because it is one change only, use it deliberately — this is not a second AEP to shop around in, '
        'it is a single correction.',
    ]) + """
      <p>Two windows, seven months apart, serving different purposes — one broad and available to
      everyone with Medicare, the other narrow and available only to undo a Medicare Advantage decision
      that already didn&rsquo;t work out. Confusing which one applies to you is the easiest way to miss
      both.</p>
""",
    'sources': [
        ('Medicare &mdash; Medicare Advantage Open Enrollment Period',
         'https://www.medicare.gov/basics/get-started-with-medicare/coverage-choices/how-to-compare-medicare-options'),
        ('CMS &mdash; Enrollment periods for Medicare Advantage and Part D',
         'https://www.cms.gov/medicare/enrollment-renewal/health-drug-plans/enrollment-periods'),
    ],
    'next': {'slug': 'overpayment-clawback',
             'title': 'The Social Security overpayment letter, and the deadline inside it',
             'blurb': 'Another rule where the calendar, not the balance, decides the outcome.'},
}
