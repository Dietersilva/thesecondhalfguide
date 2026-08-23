#!/usr/bin/env python3
"""Tenth batch: three high-search-demand gaps -- Social Security spousal
benefits, the HSA/Medicare timing trap, and the 60-63 401(k) catch-up
window."""

from build_articles import facts, check, AD_INLINE

ARTICLES10 = {}

# Verified 24 August 2026, independent of the shared CHECKED constant used
# by earlier batches -- these three are newly researched.
CHECKED10 = '24 August 2026'

# --------------------------------------------------------- spousal benefits
ARTICLES10['spousal-benefits'] = {
    'title': 'Social Security Spousal Benefits: What You&rsquo;re Actually Entitled To &mdash; The Second Half Guide',
    'eyebrow': 'Facts &amp; thresholds',
    'h1': 'Social Security spousal benefits: what you&rsquo;re actually entitled to',
    'dek': 'Married or divorced, you may be entitled to a benefit based on your spouse&rsquo;s or '
           'ex-spouse&rsquo;s earnings record &mdash; up to half of theirs, not on top of your own. The '
           'rules that decide it are stricter than most people assume.',
    'meta': '6 minute read &middot; Verified against SSA rules',
    'checked': CHECKED10,
    'body': """      <p>A spousal benefit is not a bonus added to your own Social Security check. It is a separate
      benefit, calculated off your spouse&rsquo;s (or ex-spouse&rsquo;s) earnings record instead of your
      own — and whether it helps you depends on rules most people only discover after they&rsquo;ve
      already filed.</p>

""" + facts('The rule, precisely', [
        ('Married spousal benefit', 'Up to <strong>50% of the higher earner&rsquo;s Primary Insurance '
                                    'Amount (PIA)</strong> — the benefit they would get at their own full '
                                    'retirement age — if you claim at your own full retirement age.'),
        ('Divorced spousal benefit', 'The same 50% ceiling, if the marriage lasted <strong>at least 10 '
                                     'years</strong> and you are currently unmarried.'),
        ('Claiming early', 'Reduces the spousal benefit permanently, the same way claiming your own '
                           'retirement benefit early does.'),
        ('You get the higher one, not both', 'SSA pays whichever is larger — your own retirement benefit '
                                             'or the spousal benefit — not the sum of the two.'),
        ('No delayed credits on this one', 'Waiting past your own full retirement age does '
                                           '<strong>not</strong> grow the spousal benefit. It tops out at '
                                           'your FRA, whether you claim then, at 68, or at 70.'),
        ('Your ex does not need to know', 'If you have been divorced at least two years, you can claim on '
                                          'an ex-spouse&rsquo;s record even if they have not filed yet — '
                                          'and it does not reduce anything they or a current spouse '
                                          'receive.'),
    ]) + """
      <h2>The part that surprises people: you don&rsquo;t choose</h2>

      <p>Since 2016, <strong>deemed filing</strong> applies to essentially everyone in this site&rsquo;s
      age range. Filing for one benefit you&rsquo;re eligible for is treated as filing for all of them at
      once — your own retirement benefit and any spousal benefit you qualify for. SSA compares them and
      pays the larger. The old strategy of collecting a spousal benefit alone while your own benefit kept
      growing with delayed retirement credits no longer exists for almost anyone reading this.</p>

      <p>That makes the <a href="/delayed-retirement-credit">delayed retirement credit</a> math
      one-directional here: it can still be worth delaying your <em>own</em> benefit past FRA if it will
      end up larger than half your spouse&rsquo;s — but delaying does nothing for a spousal benefit
      itself, which is fixed at your FRA amount regardless of when you actually claim it.</p>

      <blockquote class="pull">
        <p>The spousal benefit is not something you request on top of your own. It is the answer to a
        comparison SSA makes automatically the moment you file.</p>
      </blockquote>

""" + AD_INLINE + """
      <h2>The divorced-spouse rules specifically</h2>

""" + check([
        'The marriage must have lasted <strong>10 years or more</strong>. A marriage that ended at nine '
        'years and eleven months does not qualify, and there is no partial credit.',
        'You must be <strong>currently unmarried</strong>. Remarrying generally ends eligibility on the '
        'ex-spouse&rsquo;s record — unless that later marriage itself ends by divorce, death or '
        'annulment.',
        'Your ex&rsquo;s remarriage does not affect you. Their new spouse&rsquo;s eligibility and yours '
        'are calculated independently.',
        'If divorced <strong>two years or more</strong>, you can file even if your ex has not started '
        'their own benefit yet, as long as they are old enough to qualify for one.',
        'If you have more than one former spouse who meets the 10-year rule, you can choose which record '
        'to claim against — usually whichever pays more.',
    ]) + """
      <h2>Worth checking before you file</h2>

      <p>Because the comparison is automatic, there is no separate application for &ldquo;spousal
      benefits&rdquo; layered on top of your own — you apply for retirement benefits and tell SSA about
      the marriage (current or former), and the calculation happens at that point. Getting the <a
      href="/social-security-login">earnings record right</a> beforehand, for both records if it&rsquo;s a
      divorced-spouse claim, is the main thing worth doing in advance. An error in either record changes
      the comparison.</p>

      <p>None of this is a reason to file at any particular age — that depends on your health, your other
      income, and what a spouse or survivor benefit does to household planning, which
      <a href="/widows-penalty">the widow&rsquo;s penalty piece</a> on this site covers from the other
      side. It is a reason to know which of the two numbers you are actually going to be paid before you
      assume the answer.</p>
""",
    'sources': [
        ('SSA &mdash; Benefits Planner: Filing Rules for Retirement and Spouses Benefits',
         'https://www.ssa.gov/benefits/retirement/planner/claiming.html'),
        ('SSA &mdash; Frequently Asked Questions: Deemed filing',
         'https://www.ssa.gov/faqs/en/questions/KA-01202.html'),
        ('SSA &mdash; Benefits for Your Divorced Spouse',
         'https://www.ssa.gov/benefits/retirement/planner/applying7.html'),
    ],
    'next': {'slug': 'hsa-medicare-timing',
             'title': 'The HSA rule that can cost you a 6% tax at 65',
             'blurb': 'Another Social Security/Medicare timing rule most people learn about too late.'},
}

# --------------------------------------------------------------- HSA timing
ARTICLES10['hsa-medicare-timing'] = {
    'title': 'The HSA Rule That Can Cost You a 6% Tax at 65 &mdash; The Second Half Guide',
    'eyebrow': 'Facts &amp; thresholds',
    'h1': 'The HSA rule that can cost you a 6% tax at 65',
    'dek': 'If you&rsquo;re still working past 65 with an HSA-eligible health plan, enrolling in Medicare '
           'later can reach backward and tax contributions you already made. The fix is timing, not '
           'paperwork.',
    'meta': '5 minute read &middot; Verified against IRS and Medicare rules',
    'checked': CHECKED10,
    'body': """      <p>Health Savings Accounts and Medicare do not mix — you cannot contribute to an HSA for any month
      you are covered by Medicare, full stop. Most people learn this the easy way, by stopping
      contributions when Medicare starts. The trap is for people who keep working past 65, stay on an
      HSA-eligible employer plan, and enroll in Medicare later — because Medicare can reach backward and
      cover months they had already assumed were still HSA-eligible.</p>

""" + facts('The rule, precisely', [
        ('The trigger', 'Enrolling in <strong>Medicare Part A</strong> after 65 &mdash; including '
                        'automatic enrollment, if you claim Social Security at or after 65.'),
        ('The reach-back', 'Part A coverage applies <strong>retroactively up to 6 months</strong>, but '
                           'never earlier than the month you turned 65.'),
        ('The conflict', 'You are not HSA-eligible for any month covered by Medicare, including a month '
                         'covered <em>retroactively</em>.'),
        ('The penalty', 'A <strong>6% excise tax</strong> on any HSA contribution made during a month '
                        'later found to be retroactively covered by Medicare.'),
        ('The fix', 'Stop HSA contributions at least <strong>6 months before</strong> you apply for '
                    'Medicare, or before your 65th birthday if you plan to enroll right at 65.'),
        ('What is not affected', 'Money already in the HSA. It stays yours, stays tax-free for qualified '
                                 'medical expenses, and can be used to pay Medicare premiums (except '
                                 'Medigap) after 65.'),
    ]) + """
      <h2>Who this actually reaches</h2>

      <p>Almost nobody who enrolls in Medicare right at 65 hits this. The trap is specific to people who
      keep working past 65 on an employer&rsquo;s high-deductible health plan, keep contributing to an
      HSA, and then either delay Medicare deliberately or trigger it accidentally by claiming Social
      Security. Claiming Social Security at or after 65 <strong>automatically enrolls you in Medicare Part
      A</strong> — you do not get to keep the HSA-eligible coverage and collect Social Security at the
      same time without running into this.</p>

      <p>The 6-month lookback also has a floor: it never reaches earlier than the month you turned 65.
      Someone who works to 68 and then enrolls has the same 6-month exposure window as someone who works
      to 66 — the retroactive coverage does not stretch back to their 65th birthday in either case.</p>

      <blockquote class="pull">
        <p>The contribution was legal when you made it. The problem is that Medicare, once it starts, can
        decide it started six months earlier than the day you actually enrolled.</p>
      </blockquote>

""" + AD_INLINE + """
      <h2>What to do about it</h2>

""" + check([
        'If you plan to <strong>keep working past 65</strong> on an HSA-eligible plan and delay Medicare '
        'deliberately, that is fine &mdash; just know the 6-month exposure applies whenever you eventually '
        'do enroll.',
        'If you plan to <strong>claim Social Security at or after 65</strong>, stop HSA contributions at '
        'least 6 months before that claim takes effect, since claiming triggers automatic Part A '
        'enrollment.',
        'If you already over-contributed during a retroactive-coverage window, you can generally '
        '<strong>withdraw the excess</strong> before your tax filing deadline to avoid the 6% excise tax '
        'on that amount &mdash; talk to the HSA custodian about the correction process.',
        'Employer contributions count too. If your employer contributes to your HSA automatically, that '
        'also needs to stop on the same schedule.',
        'None of this affects an HSA balance you already have. It is only about <em>new</em> '
        'contributions during the overlap window.',
    ]) + """
      <p>This is a timing rule, not a reason to avoid an HSA-eligible plan while still working. The whole
      exposure is contained to a single 6-month window around whenever Medicare enrollment actually
      happens — get that window right and the rest of the HSA&rsquo;s tax treatment is unaffected.</p>
""",
    'sources': [
        ('IRS &mdash; Publication 969, Health Savings Accounts and Other Tax-Favored Health Plans',
         'https://www.irs.gov/publications/p969'),
        ('Medicare &mdash; Health Savings Accounts (HSAs) and Medicare',
         'https://www.medicare.gov/basics/costs/health-savings-accounts'),
        ('Medicare &mdash; How Part A and Part B sign-up periods work',
         'https://www.medicare.gov/basics/get-started-with-medicare/sign-up/when-does-medicare-coverage-start'),
    ],
    'next': {'slug': 'catch-up-60-63',
             'title': 'The four-year 401(k) catch-up window at 60&ndash;63',
             'blurb': 'Another narrow, easy-to-miss window &mdash; this one on the savings side.'},
}

# ---------------------------------------------------------- 60-63 catch-up
ARTICLES10['catch-up-60-63'] = {
    'title': 'The Four-Year 401(k) Catch-Up Window at 60&ndash;63 &mdash; The Second Half Guide',
    'eyebrow': 'Facts &amp; thresholds',
    'h1': 'The four-year 401(k) catch-up window at 60&ndash;63',
    'dek': 'For four calendar years only, the catch-up limit on a 401(k) jumps well past the standard '
           'age-50 amount &mdash; but only if your plan opts in, and only if you know to ask.',
    'meta': '5 minute read &middot; Verified against IRS 2026 figures',
    'checked': CHECKED10,
    'body': """      <p>Everyone 50 and older can already put more into a 401(k) than younger workers can. Fewer people
      know there is a second, larger step up — available only during the calendar years you are 60, 61, 62
      or 63, and only if your employer&rsquo;s plan specifically allows it.</p>

""" + facts('The 2026 numbers', [
        ('Standard elective deferral limit', '$24,500 &mdash; what anyone under 50 can contribute.'),
        ('Standard catch-up, age 50+', 'An additional $8,000, for a total of $32,500.'),
        ('Super catch-up, ages 60&ndash;63', 'An additional <strong>$11,250 instead</strong> of the '
                                             'standard catch-up, for a total of <strong>$35,750</strong>.'),
        ('The window', 'Only the calendar years you turn 60, 61, 62 or 63. Turn 64, and the limit drops '
                       'back to the standard $8,000 catch-up.'),
        ('Employer opt-in required', 'Plans are not required to offer the higher catch-up even if they '
                                     'already allow the standard 50+ catch-up. Ask your plan '
                                     'administrator directly.'),
        ('The Roth requirement', 'If your prior-year wages from that employer exceeded $150,000 '
                                 '(indexed), <strong>all</strong> of your catch-up contributions that '
                                 'year — not just the extra amount — must go into a Roth account.'),
    ]) + """
      <h2>Why the window is exactly four years</h2>

      <p>SECURE 2.0 set the higher catch-up specifically for the calendar years someone is age 60 through
      63 — not a running &ldquo;60 and older&rdquo; category the way the standard catch-up works. Turn 64
      partway through a year and that year still counts at the higher limit; the following year, once
      you&rsquo;ve turned 64, the amount reverts to the ordinary $8,000 catch-up. There is no extending it
      and no repeating it — four specific tax years, tied to your birth year, and then it&rsquo;s gone.</p>

      <p>For someone with the cash flow to use it, that is up to $27,000 more sheltered over four years
      than the standard catch-up alone would allow — a meaningful amount in the years right before
      retirement, when income is often at its highest and the runway to grow it is shortest.</p>

      <blockquote class="pull">
        <p>This is not automatic and it is not universal. It exists only in plans that chose to offer it,
        for four specific years, and nobody is required to tell you it applies to you.</p>
      </blockquote>

""" + AD_INLINE + """
      <h2>The Roth trap specifically</h2>

      <p>The income threshold is not about your total household income or your overall wealth — it is
      specifically <strong>wages from the employer sponsoring the plan</strong>, in the prior calendar
      year. Cross $150,000 (indexed annually) in wages from that employer, and <em>every dollar</em> of
      catch-up contribution that plan year — the standard portion and the extra super catch-up alike — has
      to go in as Roth, meaning taxed now rather than deferred. This is a plan-level rule, not something
      you elect; get the mechanics wrong and a plan can reject the contribution rather than quietly
      converting it.</p>

""" + check([
        'Ask your plan administrator directly whether your 401(k) offers the <strong>age 60&ndash;63 '
        'super catch-up</strong>. It is not universal, and it will not be flagged for you automatically.',
        'Check whether your prior-year wages from that specific employer put you over the '
        '<strong>$150,000 Roth-mandate threshold</strong> &mdash; this determines whether your catch-up '
        'contributions land pre-tax or Roth.',
        'If you turn 60 this year, mark your calendar: this is the <strong>first</strong> of your four '
        'eligible years, and the amount you can contribute changes again the year you turn 64.',
        'If you have multiple employers or a job change during this window, the eligibility and '
        'wage-threshold questions reset with each new employer&rsquo;s plan &mdash; confirm the rule with '
        'each one rather than assuming continuity.',
        'This applies to <strong>elective deferrals</strong> you choose to contribute, not to employer '
        'matching or profit-sharing contributions, which follow separate limits.',
    ]) + """
      <p>The four-year shape of this is what makes it easy to miss — it is not a standing feature of
      turning 60 the way the regular catch-up is a standing feature of turning 50. It opens once, runs for
      four years exactly, and closes on schedule whether or not anyone used it.</p>
""",
    'sources': [
        ('IRS &mdash; Retirement topics: Catch-up contributions',
         'https://www.irs.gov/retirement-plans/plan-participant-employee/retirement-topics-catch-up-contributions'),
        ('IRS &mdash; Retirement topics: 401(k) and profit-sharing plan contribution limits',
         'https://www.irs.gov/retirement-plans/plan-participant-employee/retirement-topics-401k-and-profit-sharing-plan-contribution-limits'),
    ],
    'next': {'slug': 'spousal-benefits',
             'title': 'Social Security spousal benefits: what you&rsquo;re actually entitled to',
             'blurb': 'Another rule that depends entirely on knowing to ask the right question.'},
}
