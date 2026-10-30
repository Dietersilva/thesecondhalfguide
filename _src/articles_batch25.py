#!/usr/bin/env python3
"""Twenty-fifth batch: three pieces from the last week of October 2026 --
the Social Security earnings test (the 2027 limits were announced 14 October
and the test has no page of its own), the FTC's annual report on older adults
and fraud (19 October), and Medicare telehealth, which Congress extended to the
end of 2027 in February and which nobody has written up for the people who use
it.

cms.gov, ssa.gov and ftc.gov are proxy-blocked here, so no primary source was
read directly. Verified per CLAUDE.md section 2 by agreement across independent
reporting that traces to the agency. Deliberately omitted because only one
source gave it: the share of FTC loss reports at $100,000 or more, the
government- and business-impersonation dollar totals, the Public Law number of
the telehealth extension, the 2030 date for hospital-at-home, and any
statement about permanent mental-health telehealth rules."""

from build_articles import facts, check, AD_INLINE

ARTICLES25 = {}

CHECKED25 = '30 October 2026'

# ------------------------------------------------------------- earnings test
ARTICLES25['earnings-test'] = {
    'title': 'Social Security While Working: The 2027 Earnings Test &mdash; The Second Half Guide',
    'eyebrow': 'Facts &amp; thresholds',
    'h1': 'Working while you collect Social Security: the 2027 earnings test',
    'dek': 'Claim before full retirement age and keep working, and Social Security may hold back part of '
           'your benefit. The 2027 limits, what counts toward them, and what happens to the money.',
    'meta': '6 minute read &middot; Checked against SSA&rsquo;s 2027 announcement and independent '
            'explanations of the rule',
    'checked': CHECKED25,
    'body': """      <p>The retirement earnings test is one of the most misunderstood rules in Social Security,
      mostly because its name sounds like a tax. It is not a tax and it is not a penalty. It applies to
      people who have started their benefits <em>before</em> full retirement age and who are still
      working, and it decides how much of the benefit is paid out while they do.</p>

      <p>The 2027 limits were announced on 14 October, along with the cost-of-living adjustment. They
      rose, as they do every year. The rule itself is long-standing, and nothing about it changed this
      fall. What follows is the rule and this year&rsquo;s numbers.</p>

""" + facts('The earnings test, 2027', [
        ('$25,560', 'The annual earnings limit for anyone under full retirement age for the whole of '
                    '2027. It was $24,480 in 2026.'),
        ('$1 for every $2', 'Withheld from benefits for each dollar of earnings above that limit.'),
        ('$67,920', 'The limit in the calendar year a person reaches full retirement age. It was $65,160 '
                    'in 2026.'),
        ('$1 for every $3', 'Withheld for each dollar above that limit, counting only earnings before the '
                            'month full retirement age is reached.'),
        ('$2,130 and $5,660', 'The monthly versions of the two limits, used in the first year a person '
                              'receives benefits.'),
        ('After full retirement age', 'No limit. The test stops applying in the month a person reaches '
                                      'full retirement age.'),
        ('What counts', 'Wages and net earnings from self-employment. Pensions, annuities, interest and '
                        'investment income do not.'),
    ]) + """
      <h2>Who it applies to</h2>

      <p>Only people who are receiving Social Security retirement benefits and have not yet reached
      full retirement age. For anyone born in 1960 or later, full retirement age is 67. Someone who is
      working but has not claimed is not subject to the test at all, because there is no benefit to
      withhold. The test is about the overlap: claiming early while still earning.</p>

      <p>It also applies on top of the early-claiming reduction, not instead of it. A person who claims at
      62 already receives a permanently smaller monthly amount. The earnings test then decides how much
      of that smaller amount is actually paid in a year of high earnings. The two are separate rules, and
      the reduction for claiming early is covered on
      <a href="/social-security-62">the page about filing at 62</a>.</p>

      <h2>The two rates, with numbers</h2>

      <p>In a year when a person is under full retirement age for the whole year, the limit is $25,560.
      Social Security withholds $1 of benefits for every $2 earned above it. A person who earns $35,560
      is $10,000 over the limit, so $5,000 of benefits is withheld. A person who earns $25,000 is under it
      and nothing is withheld.</p>

      <p>In the year a person reaches full retirement age, the test is milder in two ways. The limit is
      higher, at $67,920, and the rate is $1 for every $3 above it. Only earnings before the month of
      full retirement age count. A person who earns $76,920 before that month is $9,000 over, so $3,000
      is withheld. Earnings after that month, however large, are ignored.</p>

      <blockquote class="pull">
        <p>The test only ever looks at work. A large pension or a year of investment gains does not move it.</p>
      </blockquote>

""" + AD_INLINE + """
      <h2>What counts, and what does not</h2>

      <p>Only earned income counts: gross wages from a job, and net earnings from self-employment.
      Pensions, annuities, interest, dividends and capital gains are not counted, and neither are
      investment returns generally. Rental income is not counted unless it is earned through
      self-employment. That is why two people with the same total income can face very different
      results. One has a salary, the other a pension and a brokerage account.</p>

      <p>The test is also separate from income tax. Social Security benefits can be taxable whatever
      the earnings test does, and Medicare premiums can rise with income under a different rule, covered
      on <a href="/irmaa">the IRMAA page</a>. Three different tests look at income and they do not
      share a definition.</p>

      <h2>The monthly rule in the first year</h2>

      <p>The annual limits would be hard on someone who works most of a year and then retires. So in the
      first year a person receives benefits, a monthly test applies as well. For 2027 the monthly limits
      are $2,130 for someone under full retirement age all year and $5,660 for the year full retirement
      age is reached, which are the annual limits divided by twelve. A month in which earnings stay
      under the monthly limit can produce a full benefit for that month, even if the person&rsquo;s
      earnings for the whole year were above the annual limit.</p>

      <p>An illustration. A person earns $80,000 from January through June, retires, and starts benefits
      in July. The annual test would flag the year. But from July through December, earnings are zero, which
      is under the monthly limit, so those months are paid in full. Self-employed people face an extra
      check, because Social Security also looks at whether they are still working substantially in their
      own business, whatever the income.</p>

      <h2>The money is held back, not lost</h2>

      <p>This is the part most descriptions skip. Benefits withheld under the earnings test are not
      forfeited. At full retirement age, Social Security recalculates the monthly benefit to credit the
      months in which payments were withheld, as if the person had claimed correspondingly later.
      A person with several withheld months ends up with a somewhat higher benefit for the rest of their
      life. How long it takes for the higher benefit to repay the amount withheld depends on the
      individual case. One published estimate puts it at roughly twelve to fifteen years, which is a
      rough figure and not an SSA number.</p>

      <p>It is also why the test sits oddly beside the rule for waiting past full retirement age, covered
      on <a href="/delayed-retirement-credit">the delayed retirement credit page</a>. That credit is a
      percentage added for each month of delay. The credit for withheld months is a recalculation that
      reflects months in which the person did not receive a benefit.</p>

      <h2>Where the limits come from</h2>

      <p>The earnings-test limits are not tied to the cost-of-living adjustment. They move with the
      national average wage index, which is why the limit rose 4.4% this year while the COLA was 3.6%.
      The wage figures behind that appear on
      <a href="/cola-2027-estimate">the page on the 2027 COLA</a>, alongside the new taxable maximum.
      Overpayments that arise when earnings were not reported on time are a separate subject, covered on
      <a href="/overpayment-clawback">the overpayment page</a>.</p>

      <p>One note on the news. The Claiming Age Clarity Act, which would rename ages 62 and 70 as
      &ldquo;minimum&rdquo; and &ldquo;maximum&rdquo; benefit ages, would change labels, not the
      earnings test. Its status is on
      <a href="/claiming-age-clarity-act">its own page</a>.</p>

      <h2>What&rsquo;s worth keeping in mind</h2>

""" + check([
        'The 2027 limits are <strong>$25,560</strong> for people under full retirement age all year '
        '($1 withheld per $2 above) and <strong>$67,920</strong> in the year full retirement age is reached '
        '($1 per $3 above).',
        'Only <strong>wages and net self-employment earnings</strong> count. Pensions, annuities, interest '
        'and investment income do not.',
        'In the first year of benefits, a <strong>monthly test</strong> also applies: $2,130 under full '
        'retirement age, $5,660 in the year it is reached.',
        'Withheld benefits are <strong>recalculated into a higher benefit</strong> at full retirement age. '
        'They are held back, not forfeited.',
        'The test <strong>ends</strong> in the month a person reaches full retirement age.',
    ]) + """
      <p>The rule is simple to state and easy to get wrong in the details. That is why the numbers above
      are worth having written down before a job offer, a part-time contract, or a first benefit
      payment arrives.</p>
""",
    'sources': [
        ('Social Security Administration &mdash; 2027 COLA press release (14 October 2026)',
         'https://www.ssa.gov/news/en/press/releases/2026-10-14.html'),
        ('The Tax Adviser &mdash; Social Security wage base and COLA announced for 2027',
         'https://www.thetaxadviser.com/news/2026/oct/social-security-wage-base-and-cola-announced-for-2027/'),
        ('Kiplinger &mdash; 9 changes to Social Security in 2027',
         'https://www.kiplinger.com/retirement/social-security/changes-coming-to-social-security-in-2027'),
        ('The Motley Fool &mdash; This 2027 Social Security rule change is a small victory for some working '
         'beneficiaries (19 October 2026)',
         'https://www.fool.com/retirement/2026/10/19/2027-social-security-rule-change-small-victory/'),
        ('AARP &mdash; Do I get back money Social Security withholds because I work?',
         'https://www.aarp.org/social-security/faq/withholding-while-working/'),
        ('CNBC &mdash; Social Security earnings test can reduce benefits for retirees who work (27 April 2026)',
         'https://www.cnbc.com/2026/04/27/social-security-benefits-reduced.html'),
    ],
    'next': {'slug': 'delayed-retirement-credit',
             'title': 'What delaying Social Security actually adds to your check',
             'blurb': 'The other side of the claiming-age choice: the published rule for waiting past full '
                      'retirement age.'},
}

# ------------------------------------------------------- FTC older adults report
ARTICLES25['ftc-older-adults-fraud-report'] = {
    'title': 'What the FTC Report Says Older Adults Lost to Fraud &mdash; The Second Half Guide',
    'eyebrow': 'Protecting yourself',
    'h1': 'What the FTC&rsquo;s new report says older adults lost to fraud',
    'dek': 'About $3 billion in reported losses in 2025, five times the 2020 figure. What the number '
           'counts, what it leaves out, and what it says about how the losses happen.',
    'meta': '5 minute read &middot; Checked against the FTC&rsquo;s report and press release and '
            'independent coverage',
    'checked': CHECKED25,
    'body': """      <p>On 19 October the Federal Trade Commission sent Congress its annual report on older
      consumers, titled <em>Protecting Older Consumers 2025&ndash;2026</em>. The headline was a dollar
      figure that is easy to repeat and easy to misread: people 60 and older reported losing about
      <strong>$3 billion</strong> to fraud in 2025.</p>

      <p>This is the second thing worth saying about the number. The first is how recent it is. The
      report is eleven days old as of this writing, and its figures cover calendar 2025. An earlier FTC
      release, in December 2025, described 2024 data, and the two should not be mixed.</p>

""" + facts('The FTC report, in numbers', [
        ('19 October 2026', 'When the FTC released <em>Protecting Older Consumers 2025&ndash;2026</em>.'),
        ('About $3 billion', 'Fraud losses reported by people 60 and older in 2025.'),
        ('About $600 million', 'The comparable figure for 2020. The total has grown roughly fivefold.'),
        ('Over $1 billion', 'Reported losses to investment scams, the largest single category. Up 42% '
                            'from 2024.'),
        ('$13.3 billion to $119.5 billion', 'The FTC&rsquo;s estimate of what fraud costs older adults '
                                            'once unreported losses are counted. The range reflects '
                                            'different assumptions.'),
    ]) + """
      <h2>What the $3 billion counts</h2>

      <p>The figure is <em>reported</em> loss. It is what people told the FTC, or what reached the FTC
      through the other agencies and organizations that feed its Consumer Sentinel database. A scam that
      nobody reports is not in it. That is the single most important thing about the number, and it cuts
      the other way from what most readers assume. The $3 billion is a floor.</p>

      <p>The FTC says as much itself. Using different assumptions about how many people never
      report, it estimates the true cost to older adults in
      2025 at somewhere between $13.3 billion and $119.5 billion. A range that wide says the agency
      does not know the answer. It does say the reported figure is a small piece of it.</p>

      <h2>Why the total grew fivefold</h2>

      <p>From about $600 million in 2020 to about $3 billion in 2025 is not a story about more
      people being fooled by the same thing. According to coverage of the report, the rise was driven
      largely by individual losses of $100,000 or more, often to investment scams, romance scams and
      impersonators. A smaller number of very large losses moves a total much more than a large number
      of small ones.</p>

      <p>That is also why investment scams top the list. They reported more than $1 billion in losses
      for the age group, a 42% increase over the year before. Coverage of the report says
      the victims were often reached through social media.</p>

      <blockquote class="pull">
        <p>The biggest losses are not the clumsy scams. They are the patient ones.</p>
      </blockquote>

""" + AD_INLINE + """
      <h2>What the report does not say</h2>

      <p>It does not say older adults are fooled more often than younger ones. What the FTC reports
      is a difference in the size of the loss: older adults reported much higher median losses than
      younger adults in 2025. A person can be careful and still be the target of the kind of scam that
      goes after a savings account, because that is where the money is.</p>

      <p>It also does not rank scams by how likely any one person is to meet them. A category with
      a large total can be rare and costly. A category with a small total can be everywhere and cheap.
      That distinction matters for the next time one of these headlines appears.</p>

      <h2>What older adults most often report</h2>

      <p>Coverage of the report lists the categories in which older adults are more likely than younger
      adults to report a loss: tech support scams, prize, sweepstakes and lottery scams, romance scams,
      government impersonation, and scams in which someone impersonates a friend or family member. The
      list is a mix of the old and the new. A prize notice is a letter-era scam. A cloned voice is not.
      Both appear in the same table because the report counts what people reported, not the technology
      used.</p>

      <h2>Reading the next headline</h2>

      <p>A fraud number is only as useful as three details attached to it: the year it covers, whether
      it is a reported or an estimated figure, and who did the counting. The $3 billion is reported,
      2025 and the FTC&rsquo;s. The $119.5 billion is estimated, also 2025 and also the FTC&rsquo;s, and it is
      the upper end of a range. Quoting one as if it were the other is the most common way these numbers
      go wrong in circulation.</p>

      <h2>The same pattern, in this site&rsquo;s other pieces</h2>

      <p>Most of the categories in the report already have their own page here. The patient,
      relationship-driven kind is on <a href="/romance-scams">the romance scams page</a>. The caller who
      says an account is compromised is on <a href="/bank-imposter-scam">the bank imposter page</a>, and
      the follow-up in which someone arrives in person is on
      <a href="/gold-courier-scam">the courier page</a>. The tactic that ties them together, which is
      creating urgency, is on <a href="/five-minute-rule">the five-minute rule page</a>. And a voice that
      sounds like a family member is covered on <a href="/voice-cloning">the voice cloning page</a>.</p>

      <h2>Where to report</h2>

      <p>Reports go to <em>reportfraud.ftc.gov</em>. Social Security impersonation can also be reported to
      the agency&rsquo;s Inspector General at <em>oig.ssa.gov</em>. Reporting is how a loss reaches the
      number at the top of this page, which is part of why the FTC keeps asking for it.</p>

      <p>The FTC&rsquo;s long-standing line on payment is that a legitimate business or agency will not
      ask for payment by gift card, wire transfer or cryptocurrency. That is a statement about how the
      requests arrive, not about the people receiving them.</p>

      <h2>What&rsquo;s worth keeping in mind</h2>

""" + check([
        'The FTC report released <strong>19 October 2026</strong> covers 2025: about <strong>$3 billion</strong> '
        'in reported losses by people 60 and older, up roughly fivefold from 2020.',
        'That figure is <strong>reported</strong> loss only. The FTC&rsquo;s own estimate of the full cost '
        'runs from $13.3 billion to $119.5 billion.',
        'Investment scams were the costliest category, with <strong>over $1 billion</strong> reported, '
        'up 42% in a year.',
        'The report is about the size of losses, not about who is more easily fooled. Older adults '
        'reported much higher median losses than younger adults.',
        'Fraud can be reported at <em>reportfraud.ftc.gov</em>.',
    ]) + """
      <p>The number will probably be quoted all year. It is worth knowing what it is a count of before it
      is.</p>
""",
    'sources': [
        ('Federal Trade Commission &mdash; FTC issues annual report to Congress on agency&rsquo;s actions to '
         'protect older adults (October 2026)',
         'https://www.ftc.gov/news-events/news/press-releases/2026/10/ftc-issues-annual-report-congress-agencys-actions-protect-older-adults'),
        ('Federal Trade Commission &mdash; Protecting Older Consumers 2025&ndash;2026: a report of the '
         'Federal Trade Commission (19 October 2026)',
         'https://www.ftc.gov/system/files/ftc_gov/pdf/2026-older-adults-report-10192026.pdf'),
        ('PYMNTS &mdash; FTC data shows investment scams fuel fivefold surge in seniors&rsquo; fraud losses',
         'https://www.pymnts.com/cybersecurity/fraud-prevention/2026/ftc-data-shows-investment-scams-fuel-fivefold-surge-in-seniors-fraud-losses/'),
        ('PPC Land &mdash; Older Americans lost $3 billion to fraud in 2025, FTC tells Congress',
         'https://ppc.land/older-americans-lost-3-billion-to-fraud-in-2025-ftc-tells-congress/'),
        ('AccountsRecovery.net &mdash; FTC: older adults reported $3 billion in fraud losses in 2025 '
         '(22 October 2026)',
         'https://www.accountsrecovery.net/2026/10/22/ftc-older-adults-reported-3-billion-in-fraud-losses-in-2025/'),
    ],
    'next': {'slug': 'romance-scams',
             'title': 'Intelligence was never the issue',
             'blurb': 'How the patient, relationship-driven scams work, and why careful people lose to them.'},
}

# ------------------------------------------------------------- telehealth
ARTICLES25['medicare-telehealth-2027'] = {
    'title': 'Medicare Telehealth Is Covered Through 2027 &mdash; The Second Half Guide',
    'eyebrow': 'Facts &amp; thresholds',
    'h1': 'Medicare telehealth: covered at home through the end of 2027',
    'dek': 'The pandemic-era telehealth rules were extended again in February. What they allow, what a '
           'visit costs, and what comes back on 1 January 2028 if Congress does nothing.',
    'meta': '5 minute read &middot; Checked against reporting on the 2026 appropriations law and '
            'independent explainers',
    'checked': CHECKED25,
    'body': """      <p>This is not new this week. Congress extended Medicare&rsquo;s expanded telehealth
      coverage on 3 February 2026, nearly nine months ago, after the previous extension ran out at the end
      of January. It is worth a page now because Annual Enrollment is running, because the date is easy
      to get wrong, and because the question it answers is a practical one: can a Medicare patient see a
      doctor from home?</p>

      <p>For now, yes. The extension runs through <strong>31 December 2027</strong>.</p>

""" + facts('Medicare telehealth, in numbers', [
        ('3 February 2026', 'When the two-year extension was signed, as part of the Consolidated '
                            'Appropriations Act, 2026.'),
        ('31 December 2027', 'The last day the expanded flexibilities are in effect.'),
        ('1 January 2028', 'When the older limits return, unless Congress acts again.'),
        ('Your home', 'Counts as the place you receive the visit. Before 2020, in most cases it did not.'),
        ('20%', 'The usual Part B coinsurance, after the Part B deductible. A telehealth visit is billed '
                'like an in-person one.'),
        ('$283', 'The 2026 Part B deductible. The 2027 figure has not been announced.'),
    ]) + """
      <h2>What the extension keeps in place</h2>

      <p>Before 2020, Original Medicare paid for telehealth only in narrow circumstances. The patient
      generally had to live in a rural area and had to be at a medical facility, such as a clinic, when
      the visit happened. The pandemic rules lifted both limits, and Congress has extended them in
      stages ever since.</p>

      <p>Through the end of 2027, coverage continues to include visits from the patient&rsquo;s home,
      without a rural-area requirement. It continues to allow audio-only visits for some services, which
      matters to people who do not have a smartphone or a reliable video connection. The category of
      practitioners who can bill for telehealth stays wider than it was before the pandemic, and now
      includes physical therapists, occupational therapists, speech-language pathologists and
      audiologists. Not every service qualifies for every format, and audio-only in particular is
      limited. A patient&rsquo;s own provider is the one who knows which of its visits are covered.</p>

      <blockquote class="pull">
        <p>The extension is a date, not a permanent change. The rule that applies is the rule in force on
        the day of the visit.</p>
      </blockquote>

""" + AD_INLINE + """
      <h2>How it got here</h2>

      <p>The expanded rules began in 2020 as an emergency measure. Congress extended them several times,
      and they were set to expire on 30 January 2026. They lapsed briefly, then returned in the
      appropriations law signed on 3 February, which pushed the end date out to the close of 2027. Each
      extension has been written as a deadline instead of a permanent rule, which is why a patient who
      used telehealth in 2024 and 2025 can reasonably wonder whether it still works. It does, until the
      end of next year.</p>

      <h2>What a visit costs</h2>

      <p>Telehealth is paid under Part B, so the usual Part B cost-sharing applies: the annual deductible,
      then 20% of the Medicare-approved amount. The deductible for 2026 is $283. The 2027 amount
      is announced each fall, and as of 30 October it has not been. The projected figures are discussed
      on <a href="/medicare-2027-costs">the page on 2027 Medicare costs</a>. A Medigap policy that pays
      the 20% coinsurance pays it for telehealth as well, because it is the same Part B service.</p>

      <p>Nothing about this changes with the extension. It extended where and how a visit can happen,
      not what Medicare pays for it.</p>

      <h2>What still limits a visit</h2>

      <p>The extension lifts location limits. It does not make every visit a telehealth visit.
      Medicare keeps a list of the services that can be delivered by telehealth, and a provider has to
      be one that Medicare allows to bill for them. A visit that needs a physical examination, a
      procedure or a test cannot be done through a screen, and the provider decides which of its
      appointments are offered that way.</p>

      <p>Because the visits are paid under Part B, a patient needs Part B for Original Medicare to pay
      for them. And anyone who reads that the telehealth rules &ldquo;expire in January&rdquo; is
      reading coverage from before the February law, when that was true. The January date in those
      articles has passed. The date that matters now is the end of 2027.</p>

      <h2>What happens on 1 January 2028</h2>

      <p>Unless Congress extends the rules again or makes them permanent, the pre-pandemic limits come
      back: the rural and facility restrictions and the narrower list of covered situations. That is
      about fourteen months away. Congress has extended these rules repeatedly, sometimes after a
      lapse. That is a pattern, and it is not a promise. Reporting on the extension notes that there has been
      little movement on bills to make the flexibilities permanent.</p>

      <p>So the practical shape of the rule is a window. A person planning care across the end of 2027,
      for example a recurring series of visits, should expect the rules for visits in January 2028 to be
      whatever Congress has decided by then.</p>

      <h2>A note about what this page leaves out</h2>

      <p>Mental health care by telehealth has its own set of rules, and reporting on them is not
      consistent about which parts are permanent and which are on the same 2027 clock, so this page does
      not describe them. The same goes for prescribing of controlled substances by telehealth, which
      is governed by federal drug enforcement rules rather than by Medicare. Neither is covered here, and
      the provider&rsquo;s office is the right place to ask about both.</p>

      <p>Medicare Advantage plans are separate again. Each plan sets its own network and visit rules,
      which is one more reason the plan&rsquo;s own
      materials are the ones that apply. Other places where the plan&rsquo;s own rules matter are on
      <a href="/advantage-vs-original">the Advantage or Original page</a>.</p>

      <h2>What&rsquo;s worth keeping in mind</h2>

""" + check([
        'Medicare&rsquo;s expanded telehealth coverage runs through <strong>31 December 2027</strong>, '
        'under a law signed 3 February 2026.',
        'A visit can take place <strong>from home</strong>, without a rural-area requirement.',
        'It is paid like any Part B service: the deductible, then <strong>20%</strong>. The 2026 deductible '
        'is $283; the 2027 figure has not been announced.',
        'Audio-only visits are allowed for <strong>some</strong> services, not all.',
        'On <strong>1 January 2028</strong> the older limits return unless Congress acts again.',
    ]) + """
      <p>The rule that governs a visit is the rule on the day of the visit. For the next fourteen months,
      that rule is generous. After that, it depends on a vote.</p>
""",
    'sources': [
        ('Center for Medicare Advocacy &mdash; Medicare telehealth coverage extended through 2027',
         'https://medicareadvocacy.org/medicare-telehealth-coverage-extended-through-2027/'),
        ('American Bar Association &mdash; Congress extends Medicare telehealth flexibilities through 2027',
         'https://www.americanbar.org/groups/health_law/news/2026/medicare-telehealth-flexibilities-extended-2027/'),
        ('Forbes &mdash; Congress extends Medicare telehealth coverage for two years (3 February 2026)',
         'https://www.forbes.com/sites/brucejapsen/2026/02/03/congress-extends-medicare-telehealth-coverage-for-two-years/'),
        ('KFF &mdash; What to know about Medicare coverage of telehealth',
         'https://www.kff.org/medicare/what-to-know-about-medicare-coverage-of-telehealth/'),
        ('Foley &amp; Lardner &mdash; Medicare telehealth flexibilities: countdown to January 30, 2026',
         'https://www.foley.com/insights/publications/2026/01/medicare-telehealth-flexibilities-countdown-to-january-30-2026-and-what-comes/'),
    ],
    'next': {'slug': 'medicare-gaps',
             'title': 'What Medicare doesn&rsquo;t cover',
             'blurb': 'The short list of things Original Medicare leaves out, and the large one most people '
                      'discover late.'},
}
