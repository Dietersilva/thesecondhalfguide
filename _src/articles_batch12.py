#!/usr/bin/env python3
"""Twelfth batch: three pieces built from actual agency announcements in the
two weeks before this run -- SSA's August 11 Compassionate Allowances
expansion, the Medicare card reissue/scam pairing from this spring that is
still circulating, and SSA's July 24 SSI modernization report (automatic
wage reporting via the Payroll Information Exchange)."""

from build_articles import facts, check, AD_INLINE

ARTICLES12 = {}

# Verified 28 August 2026, independent of the shared CHECKED constant.
CHECKED12 = '28 August 2026'

# ------------------------------------------------------ compassionate allowances
ARTICLES12['compassionate-allowances'] = {
    'title': 'Social Security&rsquo;s Fast Track for a Severe Diagnosis &mdash; The Second Half Guide',
    'eyebrow': 'Facts &amp; thresholds',
    'h1': 'Social Security&rsquo;s fast track for a severe diagnosis',
    'dek': 'A little-known SSA list lets certain disability claims skip the usual months of review and '
           'be approved on medical evidence alone. Fourteen conditions were added to it on August 11, '
           'bringing the total to 314.',
    'meta': '6 minute read &middot; Verified against SSA rules',
    'checked': CHECKED12,
    'body': """      <p>A standard Social Security disability claim can take months, sometimes over a year, to move
      through review. For a specific list of conditions serious enough that there is little real question
      about the outcome, SSA skips most of that. The program is called <strong>Compassionate
      Allowances</strong>, and on August 11, 2026, SSA added 14 conditions to it &mdash; bringing the list
      to 314.</p>

""" + facts('The rule, precisely', [
        ('What it is', 'A published list of specific medical conditions serious enough that SSA can '
                       'approve a disability claim based on <strong>medical confirmation of the diagnosis '
                       'alone</strong>, rather than the standard multi-step disability review.'),
        ('The August 2026 update', '<strong>14 conditions</strong> were added on August 11, 2026, '
                                   'bringing the Compassionate Allowances (CAL) list to <strong>314 '
                                   'conditions</strong> in total.'),
        ('What kind of conditions', 'Mostly rare, severe genetic and neurological disorders and specific '
                                    'aggressive cancers &mdash; not a general &ldquo;serious illness&rdquo; '
                                    'catch-all. Only a condition actually on the published list qualifies.'),
        ('Which programs it covers', 'Both <strong>Social Security Disability Insurance (SSDI)</strong> '
                                     'and <strong>Supplemental Security Income (SSI)</strong> use the same '
                                     'medical disability determination, so CAL applies to a claim filed '
                                     'under either one.'),
        ('Track record', 'SSA reports that more than <strong>1.2 million people</strong> have been '
                         'approved through Compassionate Allowances since the program began in 2008.'),
        ('Processing time', 'A CAL-flagged claim can be approved in <strong>days to a few weeks</strong>, '
                            'instead of the months a standard disability claim typically takes.'),
    ]) + """
      <h2>The part that matters: it speeds the decision, not the waiting periods</h2>

      <p>There is no separate application for Compassionate Allowances. You file for disability the
      normal way &mdash; through SSDI, SSI, or both &mdash; and name your condition. SSA&rsquo;s system is
      built to automatically flag an application that mentions a listed condition and route it for
      expedited review. You still have to provide adequate medical evidence; the program speeds up the
      decision once that evidence supports the diagnosis, it does not replace the evidence.</p>

      <p>It also does not touch two waiting periods that are separate from the disability decision itself.
      SSDI benefits generally still begin <strong>five months</strong> after your disability onset date,
      and Medicare eligibility through SSDI still generally requires a further <strong>24-month</strong>
      wait after benefits start &mdash; a Compassionate Allowances approval does not shorten either one.
      The one standing exception is ALS, which has no five-month benefit wait and no 24-month Medicare
      wait at all; Medicare starts the same month SSDI does.</p>

      <h2>A related, separate fast track</h2>

      <p>SSA runs a second, related process called <strong>Quick Disability Determinations (QDD)</strong>,
      easy to confuse with Compassionate Allowances because both exist to speed up the most clear-cut
      claims. The difference is how each one identifies a case. CAL works from the published list of
      specific named conditions; QDD instead runs a computer model over every incoming application, looking
      for language and documentation patterns that predict a claim is very likely to be approved, whatever
      the diagnosis. A condition that never makes the CAL list can still be flagged and fast-tracked through
      QDD if the application and the medical record make the case clearly enough on their own.</p>

      <p>New conditions do not appear on the CAL list by accident. SSA adds to it through public outreach
      hearings and by evaluating nominations from medical professionals, advocacy organizations and the
      public, alongside research from the National Institutes of Health and patient advocacy groups.
      Anyone can submit a condition for consideration through SSA&rsquo;s own site &mdash; which is part of
      why the list keeps growing several times a year rather than sitting fixed.</p>

      <blockquote class="pull">
        <p>Compassionate Allowances answers one question fast: does the medical evidence clearly meet the
        bar. It does not change how soon the money, or Medicare, actually starts.</p>
      </blockquote>

""" + AD_INLINE + """
      <h2>Who this actually reaches</h2>

      <p>SSDI is only available before full retirement age &mdash; once you reach it, disability benefits
      convert to retirement benefits on their own. That makes this most relevant to readers who are not
      there yet: someone in their late fifties or early sixties facing a sudden, severe diagnosis, or
      helping a spouse or family member through one. SSI has no age ceiling in the same way, so it also
      matters for a lower-income household at any age in this range. Either way, the value of Compassionate
      Allowances is knowing it exists <em>before</em> a claim is filed, since naming the condition clearly
      is what lets SSA&rsquo;s system catch it.</p>

""" + check([
        'Name the <strong>specific condition</strong> on your application or when you first contact SSA, '
        'so the system can flag it automatically.',
        'You still need <strong>adequate medical evidence</strong> &mdash; expedited review does not '
        'replace documentation of the diagnosis.',
        'Check the current list yourself at SSA&rsquo;s Compassionate Allowances page; it is updated '
        'several times a year and this August&rsquo;s 14 additions will not be the last.',
        'Remember the <strong>five-month SSDI wait and 24-month Medicare wait</strong> still apply, ALS '
        'excepted &mdash; CAL changes the speed of the decision, not these separate clocks.',
        'If your condition is not on the list, you can still qualify for disability the standard way. CAL '
        'only changes how fast a listed condition is decided, not who is eligible in general.',
    ]) + """
      <p>None of this changes what disability itself requires — an inability to do substantial work because
      of the condition. What changes is how long it takes SSA to agree, for the specific conditions severe
      enough to be on this list.</p>
""",
    'sources': [
        ('SSA &mdash; Social Security Adds 14 Conditions to Compassionate Allowances List',
         'https://www.ssa.gov/news/en/press/releases/2026-08-11.html'),
        ('SSA &mdash; Compassionate Allowances',
         'https://www.ssa.gov/compassionateallowances/'),
        ('SSA &mdash; Complete List of Conditions',
         'https://www.ssa.gov/compassionateallowances/conditions.htm'),
        ('SSA &mdash; Quick Disability Determinations (QDD)',
         'https://www.ssa.gov/disabilityresearch/qdd.htm'),
    ],
    'next': {'slug': 'ssi-wage-reporting',
             'title': 'Your SSI wage reports just became automatic',
             'blurb': 'Another change from this year’s SSA modernization push, this one for people who work while on SSI or SSDI.'},
}

# --------------------------------------------------------- medicare card scam
ARTICLES12['medicare-card-scam'] = {
    'title': 'The New Medicare Card Scam, and the Real Reissue Behind It &mdash; The Second Half Guide',
    'eyebrow': 'Facts &amp; thresholds',
    'h1': 'The new Medicare card scam, and the real reissue behind it',
    'dek': 'About 1.3 million Medicare numbers were reissued this spring after a security incident. '
           'Nothing about anyone&rsquo;s coverage changed &mdash; but the real event gave scammers a new '
           'script that is still circulating.',
    'meta': '5 minute read &middot; Verified against CMS and SMP guidance',
    'checked': CHECKED12,
    'body': """      <p>Some Medicare beneficiaries received a new card in the mail this spring with a new number on
      it, unprompted, without asking for one. That part was real: CMS reissued roughly 1.3 million
      Medicare numbers after a security incident affecting Medicare claims-processing systems. The trouble
      is that the same event became the basis for a scam call &mdash; and the calls kept coming long after
      the real reissue was finished.</p>

""" + facts('The rule, precisely', [
        ('What happened', 'CMS reissued <strong>Medicare Beneficiary Identifiers</strong> &mdash; the '
                          'number on your Medicare card &mdash; for about <strong>1.3 million '
                          'people</strong>, following a security incident tied to Medicare '
                          'claims-processing systems.'),
        ('Timing', 'New cards were mailed in <strong>March 2026</strong>; the new numbers took effect on '
                   '<strong>April 14, 2026</strong>.'),
        ('What actually changed', 'Only the identification number. Benefits, premiums, a Medicare '
                                  'Advantage or Part D plan, and a Medigap policy were <strong>not '
                                  'affected</strong>.'),
        ('What CMS said about fraud', 'The agency reported <strong>no confirmed cases</strong> of '
                                      'identity theft or fraud tied directly to the incident in its public '
                                      'statements at the time.'),
        ('The rule that stops the scam', 'Medicare does not call, text, or email you first to '
                                         '&ldquo;verify,&rdquo; &ldquo;activate,&rdquo; or '
                                         '&ldquo;confirm&rdquo; a card or number. A reissued card simply '
                                         'arrives by mail, with a letter explaining why.'),
        ('One more difference from the old card', 'A current Medicare card and number no longer contain '
                                                   'your <strong>Social Security number</strong> &mdash; a '
                                                   'separate change from before this reissue, but worth '
                                                   'knowing if you are comparing an older card in a drawer '
                                                   'against a newer one.'),
    ]) + """
      <h2>The part that matters: the scam outlived the event</h2>

      <p>The actual reissue was finished by mid-April. The scam calls referencing it were not. Callers
      claiming to be from Medicare told people they needed a new, more secure &ldquo;chip card,&rdquo; or
      offered free medical equipment or extra benefits, and asked the person to &ldquo;verify&rdquo; their
      current Medicare number, Social Security number, or bank details first. None of that is how a real
      reissue works — it borrowed the credibility of a genuine event that most people had heard about, and
      used it to make an old script sound current.</p>

      <p>A genuine CMS mailing about a number change reads like paperwork, not an offer. It explains what
      changed and why, gives you a number to call if you have questions, and does not ask you to pay
      anything, read back a code, or provide information to keep your coverage active. Coverage was never
      at risk in the first place — the reissue only changed the identifying number, not eligibility for
      anything. A message that suggests your Medicare could lapse unless you act quickly is, by itself, a
      sign the message did not come from Medicare.</p>

      <blockquote class="pull">
        <p>The real reissue explained why some cards changed. It did not explain anything by phone, and
        neither does Medicare — a call asking you to confirm your number is the scam, not the update.</p>
      </blockquote>

""" + AD_INLINE + """
      <h2>How to tell your mail, or a call, is legitimate</h2>

""" + check([
        'A real reissued card arrives <strong>by mail</strong>, with a letter explaining why the number '
        'changed. It does not arrive as a phone call or text first.',
        'Medicare does not call unless you asked them to call you back, or you called them first.',
        'If you are unsure whether a card or letter is genuine, call <strong>1-800-MEDICARE</strong> '
        '(1-800-633-4227) directly &mdash; never a number provided in the mailing or by the caller.',
        'Never give your Medicare number, Social Security number, or bank details to anyone who contacts '
        '<strong>you</strong> first.',
        'If a caller has already asked for this information, report it to the <strong>Senior Medicare '
        'Patrol</strong> at 1-877-808-2468, or your local SMP.',
        'Need a replacement anyway? Order one through your secure Medicare.gov account or by calling '
        '1-800-MEDICARE &mdash; never through a link or number in an unsolicited message.',
    ]) + """
      <p>The reissue itself is over. The habit worth keeping is not: treat any unsolicited call or text
      about your Medicare number the same way regardless of what event it claims to reference, because the
      next pretext will not announce itself as fake either.</p>
""",
    'sources': [
        ('Medicare &mdash; Your Medicare Card',
         'https://www.medicare.gov/basics/get-started-with-medicare/using-medicare/your-medicare-card'),
        ('Senior Medicare Patrol &mdash; Medicare Cards',
         'https://smpresource.org/medicare-fraud/medicare-cards/'),
        ('SSA &mdash; How do I get a replacement Medicare card?',
         'https://www.ssa.gov/faqs/en/questions/KA-01735.html'),
    ],
    'next': {'slug': 'bank-imposter-scam',
             'title': 'The phone call that empties bank accounts',
             'blurb': 'A different caller, the same pattern: urgency, a request to confirm something, and a reason not to hang up and check.'},
}

# ------------------------------------------------------------- SSI wage reporting
ARTICLES12['ssi-wage-reporting'] = {
    'title': 'Your SSI Wage Reports Just Became Automatic &mdash; The Second Half Guide',
    'eyebrow': 'Facts &amp; thresholds',
    'h1': 'Your SSI wage reports just became automatic',
    'dek': 'If you or a family member gets SSI and works, Social Security used to rely entirely on you to '
           'report every paycheck by hand. A system called the Payroll Information Exchange now does much '
           'of that for you.',
    'meta': '5 minute read &middot; Verified against SSA rules',
    'checked': CHECKED12,
    'body': """      <p>Supplemental Security Income has always come with a strict rule: report your wages to SSA every
      month, by hand, or risk an overpayment if a raise or extra shift went unreported. On July 24, 2026,
      SSA reported that a system called the <strong>Payroll Information Exchange (PIE)</strong> now
      handles much of that automatically, for recipients who work for a participating employer.</p>

""" + facts('The rule, precisely', [
        ('The old rule, still mostly true', 'SSI recipients who work have long had to report wages to SSA '
                                            'themselves, every month, or risk an overpayment if income '
                                            'went unreported.'),
        ('What changed', 'The Payroll Information Exchange pulls wage and employment data directly from '
                         'participating payroll providers each month, <strong>automatically</strong>, for '
                         'SSDI and SSI recipients whose employer is part of the exchange.'),
        ('Status', 'PIE reached full-scale monthly operation in <strong>September 2025</strong>, and SSA '
                   'highlighted it again in a <strong>July 24, 2026</strong> report as part of a wider '
                   'round of SSI improvements.'),
        ('The SSI Improvement Office', 'SSA named a lead executive over a newly created SSI Improvement '
                                       'Office in 2026 &mdash; the first time the agency has had one '
                                       '&mdash; overseeing changes meant to reduce improper payments and '
                                       'speed up service.'),
        ('Where the data comes from', 'Wage information comes from payroll data providers that '
                                      'participate in the exchange, <strong>not from every employer '
                                      'automatically</strong>.'),
        ('It reduces the burden, not the requirement', 'Income PIE cannot see &mdash; self-employment, or '
                                                        'a job with a payroll provider outside the exchange '
                                                        '&mdash; still needs to be reported the old way.'),
    ]) + """
      <h2>The part that matters: automatic reporting is not automatic accuracy</h2>

      <p>PIE reduces the chance of an overpayment caused by a wage change nobody reported in time — a
      common way people ended up owing money back, through no fault beyond a missed phone call or form. It
      does not eliminate overpayment risk generally, and wages are not the only thing SSA has automated
      checks for. SSI also comes with a strict <strong>resource limit</strong> — $2,000 for an individual,
      $3,000 for a couple — and money held above that in a bank account is, separately from unreported
      wages, one of the leading causes of SSI overpayments.</p>

      <p>SSA checks this through a different system, the <strong>Access to Financial Institution
      (AFI)</strong> tool, which SSA expanded as part of the same 2026 modernization push. AFI lets SSA
      electronically query financial institutions to confirm a recipient&rsquo;s account balances actually
      fall under the resource limit, including a geographic search of other states a recipient has lived
      in, to catch an account that was never reported. Like PIE, AFI verifies something SSA used to rely on
      recipients to self-report — it does not change what the resource limit is, only how SSA confirms
      whether someone is under it.</p>

      <p>If a wage-related, or resource-related, overpayment notice arrives anyway — because an employer
      was not on the exchange, because self-employment income went unreported, or for any other reason —
      the same rules this site has already covered still apply: the deadlines inside that notice, not the
      balance, decide whether withholding starts immediately or not at all.</p>

      <blockquote class="pull">
        <p>Automating the wage report removes one way to get an overpayment wrong by accident. It does not
        remove the notice, the deadline inside it, or the need to still report what the system cannot
        see.</p>
      </blockquote>

""" + AD_INLINE + """
      <h2>What to actually do</h2>

""" + check([
        'If you receive SSI or SSDI and work for an employer, ask whether the Payroll Information '
        'Exchange is active for your record &mdash; it is not universal yet.',
        'Keep reporting income PIE does not cover: <strong>self-employment</strong>, tips, or an employer '
        'outside the exchange.',
        'Keep your own pay stubs regardless. Automatic reporting reduces the paperwork, not the value of '
        'your own record if a dispute comes up.',
        'If a wage-related overpayment notice arrives anyway, the same <strong>30-day and 60-day</strong> '
        'deadlines that govern any Social Security overpayment still apply.',
    ]) + """
      <p>None of this changes what SSI still requires from a recipient who works. What changes is how much
      of the reporting SSA can now see on its own, before a missed report turns into a notice.</p>
""",
    'sources': [
        ('SSA &mdash; Social Security Announces Significant Improvements in the Supplemental Security '
         'Income Program',
         'https://www.ssa.gov/news/en/press/releases/2026-07-24.html'),
        ('SSA &mdash; What is payroll information exchange and how does Social Security use it?',
         'https://www.ssa.gov/faqs/en/questions/KA-10116.html'),
        ('SSA &mdash; Access to Financial Institutions (AFI)',
         'https://www.ssa.gov/improperpayments/afi.html'),
    ],
    'next': {'slug': 'overpayment-clawback',
             'title': 'The Social Security overpayment letter, and the deadline inside it',
             'blurb': 'If a wage-related overpayment notice arrives anyway, this is the calendar that decides what happens next.'},
}
