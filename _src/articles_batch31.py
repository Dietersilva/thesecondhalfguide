#!/usr/bin/env python3
"""Thirty-first batch (27 November 2026): the December 2026 and January 2027 Social
Security and SSI payment dates, including the payments that move to 31 December
because 1 January is a federal holiday and 3 January a Sunday.

ssa.gov was not read directly: dates verified per CLAUDE.md section 2 by agreement
across independent results (Kiplinger, NerdWallet, Newsweek, the SSA announcement of
the 2027 COLA for the 31 December SSI date) and by calendar arithmetic. Deliberately
omitted because only one dated copy gave it: how many days to wait before contacting
SSA about a missing payment, and the 2027 SSI federal payment amounts."""

from build_articles import facts, check, AD_INLINE

ARTICLES31 = {}

CHECKED31 = '27 November 2026'

ARTICLES31['payment-dates-january-2027'] = {
    'title': 'Social Security Payment Dates: December 2026 and January 2027 &mdash; The Second Half Guide',
    'eyebrow': 'Facts &amp; thresholds',
    'h1': 'Some January Social Security payments arrive on 31 December',
    'dek': 'January 1 is a holiday and January 3 is a Sunday, so one group is paid early and SSI '
           'recipients get two deposits in December. The dates, by birthday.',
    'meta': '5 minute read &middot; Checked against SSA&rsquo;s announcement and independent payment-schedule '
            'reporting',
    'checked': CHECKED31,
    'body': """      <p>Social Security pays on a fixed calendar, and the calendar bends around weekends and
      federal holidays. January 2027 is one of the months where it bends. <strong>1 January</strong> is a
      Friday and a federal holiday, and <strong>3 January</strong> is a Sunday. Anyone whose payment is
      normally dated the 3rd therefore gets the January payment on <strong>Thursday, 31 December
      2026</strong>. Supplemental Security Income, which is paid on the 1st, moves to the same day.</p>

      <p>Nothing is extra and nothing is lost. It is the same benefit, paid a few days earlier than the
      calendar would suggest. For most readers the schedule is simpler: the payment lands on a Wednesday
      set by the day of the month you were born.</p>

""" + facts('The payment dates, December 2026 and January 2027', [
        ('Thursday, 3 December', 'People who started Social Security before May 1997, and people who '
                                 'receive both Social Security and SSI.'),
        ('Wednesday, 9 December', 'Born on the 1st through the 10th of any month.'),
        ('Wednesday, 16 December', 'Born on the 11th through the 20th.'),
        ('Wednesday, 23 December', 'Born on the 21st through the 31st.'),
        ('Tuesday, 1 December', 'SSI payment for December.'),
        ('Thursday, 31 December', 'The January payment for the 3rd-of-the-month group and for SSI, paid early '
                                  'because of the holiday.'),
        ('Wednesday, 13 January', 'Born on the 1st through the 10th.'),
        ('Wednesday, 20 January', 'Born on the 11th through the 20th.'),
        ('Wednesday, 27 January', 'Born on the 21st through the 31st.'),
    ]) + """
      <h2>How the birthday rule works</h2>

      <p>For people who began benefits in May 1997 or later, and who do not also receive SSI, the payment
      date is set by the day of the month on which the person who holds the Social Security record was
      born. A birthday on the 1st through the 10th is paid on the second Wednesday of the month. The 11th
      through the 20th is paid on the third Wednesday, and the 21st through the 31st on the fourth. The date
      depends on the day of the month only, not the month or the year, and it does not change from one
      month to the next except where the calendar forces it.</p>

      <p>One detail trips people up. The day that counts is the birthday of the person whose Social
      Security number the benefit is paid on, not the day of the person receiving it. Someone who receives
      a spouse&rsquo;s or a survivor&rsquo;s benefit is therefore paid on the schedule of the person who
      earned it. A person born on the 14th who receives a benefit earned by a spouse born on the 6th is
      paid on the second Wednesday, not the third.</p>

      <h2>Why the payment moves to 31 December</h2>

      <p>When a payment date falls on a weekend or a federal holiday, Social Security pays on the business
      day before. The 3rd of January 2027 is a Sunday. The business day before it would be Friday the 1st,
      but that is New Year&rsquo;s Day. The next day back is Thursday, 31 December. SSI follows the same
      logic from the other direction: it is due on the 1st, which is a holiday, so it also arrives on
      31 December.</p>

      <p>For SSI recipients this means two deposits dated in December, one on 1 December and one on
      31 December, and none dated in January. A budget built around one deposit a month may look
      different for a month. The money is the same. The next SSI deposit after 31 December falls on
      1 February.</p>

      <blockquote class="pull">
        <p>A payment dated 31 December is the January payment. It arrives early. It does not replace one
        and it does not add one.</p>
      </blockquote>

""" + AD_INLINE + """
      <h2>Why a January payment is for December</h2>

      <p>Social Security pays a month behind. The payment that arrives in a given month is the benefit for
      the month before it. The payment dated in January covers December, and the one dated in February
      covers January. That is why a cost-of-living adjustment that takes effect with December benefits is
      first seen in the payment received in January, and why a person who becomes entitled in a given
      month generally receives the first payment the following month.</p>

      <p>It also explains a common point of confusion about the early payment. A payment dated 31 December
      is still the payment for December, received at the end of the month rather than the beginning of the
      next. What moved is the date it is paid, not the month it covers. A person who counts payments by
      the month printed on a bank statement will see December carry two deposits and January none, even though
      the number of payments over the year is unchanged.</p>

      <h2>The payment that carries the raise</h2>

      <p>The 3.6% cost-of-living adjustment for 2027 shows up in the payments dated in January. The Social
      Security Administration&rsquo;s announcement of the increase says larger SSI payments begin on
      31 December 2026, and that the average retirement benefit rises by about $75 a month.
      The details of how the raise compares with the Medicare premium are on
      <a href="/cola-2027-estimate">the page on the 2027 COLA</a>.</p>

      <p>For most people whose Medicare Part B premium is withheld from the benefit, the raise in the first
      payment of 2027 is smaller than the headline percentage suggests. The 2027 premium is
      $209.40, up from $202.90, as set out on
      <a href="/part-b-premium-2027">the page on the 2027 Part B amounts</a>. The deduction is made
      before the money arrives, so the figure that reaches the bank account is the net.</p>

      <h2>What to check on your own record</h2>

""" + check([
        'Which group you are in. Your <strong>my Social Security</strong> account shows the payment date. '
        'If you cannot sign in, <a href="/social-security-login">the page on locked-out accounts</a> '
        'covers the options.',
        'Whether the early payment affects you. It applies to the 3rd-of-the-month group and to SSI. The '
        'Wednesday groups are paid on 13, 20 and 27 January.',
        'Whether your bank credits deposits on the date they are sent or a day later. The date '
        'SSA publishes is the payment date, not the date a particular bank posts it.',
        'If you receive SSI and work, report wages on time. The reporting rules are on '
        '<a href="/ssi-wage-reporting">the SSI wage reporting page</a>.',
    ]) + """
      <p>The schedule is published by the agency for the whole year, and the holidays that move it are the
      same ones every year. The only unusual part of this one is how they fall: a Friday holiday followed
      by a Sunday. It is the kind of detail that is easy to miss until a payment seems to be early, and
      then is easy to explain.</p>
""",
    'sources': [
        ('Social Security Administration &mdash; Social Security Announces 3.6 Percent Benefit Increase for 2027',
         'https://www.ssa.gov/news/en/press/releases/2026-10-14.html'),
        ('Social Security Administration &mdash; Schedule of Social Security benefit payments, 2026',
         'https://www.ssa.gov/pubs/EN-05-10031-2026.pdf'),
        ('Kiplinger &mdash; Social Security payment schedule for 2027',
         'https://www.kiplinger.com/retirement/social-security/social-security-payment-schedule-2027'),
        ('NerdWallet &mdash; Social Security payment dates, December and January',
         'https://www.nerdwallet.com/retirement/learn/social-security-payment-schedule'),
        ('Newsweek &mdash; When will December 2026 Social Security payments arrive',
         'https://newsweek.com/when-will-december-2026-social-security-payments-arrive-12731971'),
    ],
    'next': {'slug': 'cola-2027-estimate',
             'title': 'The 2027 COLA: 3.6%, and what it takes with it',
             'blurb': 'The raise, the Medicare premium that comes out of it, and what is left.'},
}
