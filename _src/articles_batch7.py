#!/usr/bin/env python3
"""Seventh batch: gaps found by checking what is actually current — the WEP/GPO
repeal, the Social Security login change, and the gold courier scam."""

from build_articles import facts, check, AD_INLINE, CHECKED

ARTICLES7 = {}

# ---------------------------------------------------------------- WEP / GPO
ARTICLES7['wep-gpo-repeal'] = {
    'title': 'The Pension Rule That Cut Your Social Security Is Gone &mdash; The Second Half Guide',
    'eyebrow': 'Facts &amp; thresholds',
    'h1': 'The pension rule that cut your Social Security is gone',
    'dek': 'If you worked as a teacher, firefighter, police officer or public employee, two provisions '
           'quietly reduced your benefit for decades. Both were repealed &mdash; and a lot of people '
           'affected still don’t know.',
    'meta': '6 minute read &middot; Verified against SSA guidance',
    'checked': CHECKED,
    'body': """      <p>For more than forty years, two rules reduced Social Security benefits for people who'd earned a
      pension from work not covered by Social Security. Mostly that meant public employees: teachers,
      firefighters, police officers, some state and local government workers, some federal employees
      under the older retirement system.</p>

      <p>They were called the <strong>Windfall Elimination Provision</strong> and the <strong>Government
      Pension Offset</strong>, and they were among the most resented rules in the whole program.</p>

      <p><strong>The Social Security Fairness Act repealed both.</strong> It was signed on 5 January 2025
      and applies to benefits payable from January 2024 onward — meaning it was retroactive from the day
      it passed.</p>

      <p>Roughly 3 million people were affected. A great many have already had their payments adjusted
      and received back pay. But this got much less coverage than its size warranted, and people still
      turn up who don't know their benefit went up, or who never claimed at all because the old rules
      made it look pointless.</p>

""" + facts('What the two rules did, and what changed', [
        ('WEP', 'Reduced <em>your own</em> retirement or disability benefit if you also had a pension '
                'from work where you didn’t pay Social Security tax.'),
        ('GPO', 'Reduced or wiped out <em>spousal and survivor</em> benefits for the same group. This '
                'was the harsher of the two &mdash; it frequently eliminated the benefit entirely.'),
        ('Repealed', 'Both, by the Social Security Fairness Act, signed 5 January 2025.'),
        ('Effective from', 'Benefits payable for January 2024 onward &mdash; so back pay was owed.'),
        ('Who was affected', 'Around 3 million people, overwhelmingly retired public servants and their '
                             'spouses and widows.'),
        ('Do you need to apply?', 'Not if you were already receiving benefits &mdash; SSA has processed '
                                  'the overwhelming majority automatically. If you never filed, you '
                                  'almost certainly do need to.'),
    ]) + """
      <h2>The group most likely to be missing out</h2>

      <p>Here's the part worth reading twice, because automatic adjustments don't reach these people.</p>

      <p>The GPO was severe enough that many spouses and widows of Social Security–covered workers
      <strong>never bothered to file at all</strong>. If a financial planner or an SSA representative told
      you in 2009 that your teacher's pension would wipe out any widow's benefit, you'd have sensibly
      concluded there was nothing to claim, and never opened a file.</p>

      <p>SSA can adjust payments for people already in the system. It cannot adjust a claim that was
      never made. So if you're in that group — you were told years ago not to bother because of a public
      pension — <strong>that advice is now out of date, and the benefit may be substantial.</strong></p>

      <blockquote class="pull">
        <p>If someone once told you a public pension made your spousal or survivor benefit worthless,
        that was true then. It isn't now.</p>
      </blockquote>

""" + AD_INLINE + """
      <h2>What to check</h2>

""" + check([
        'Already receiving Social Security and had WEP or GPO applied? Look at your <strong>current '
        'payment amount</strong> and confirm it rose. Most adjustments and back payments have been made.',
        'Told years ago not to file for a <strong>spousal or survivor benefit</strong> because of a '
        'public pension? Contact SSA. This is where money is most often left unclaimed.',
        'Still working in public service and planning your claim? The old arithmetic no longer applies '
        '&mdash; <strong>any estimate made before 2025 understates your benefit</strong>.',
        'Check your <strong>my Social Security</strong> account for your current benefit and earnings '
        'record. (If you can’t get in, see <a href="/social-security-login">the login change</a> '
        '&mdash; the old username and password no longer work.)',
        'If something looks wrong, call SSA on <strong>1-800-772-1213</strong> or make an appointment at '
        'a local office. Expect waits, and go with your pension details to hand.',
        'Be alert for <strong>scams</strong> built on this. Nobody legitimate charges a fee to release '
        'your back pay, and SSA will not call you demanding information to process it.',
    ]) + """
      <h2>One open question</h2>

      <p>There's an unresolved dispute about how far back retroactive benefits should go for people who
      <em>never filed a claim</em> — whether such a claim can be backdated a full twelve months or only
      six. Some members of Congress have pushed back on SSA's interpretation. That argument is above your
      pay grade and mine, but it's a reason to file sooner rather than later: the longer you wait, the
      more months fall off the back end regardless of how it's settled.</p>

      <p>This is a rare thing in retirement policy — a change that made a large number of people
      unambiguously better off, applied retroactively, requiring nothing from most of them. It deserved
      more attention than it got, and the people it's still failing to reach are the ones who gave up on
      the system years ago because it told them not to bother.</p>
""",
    'sources': [
        ('SSA &mdash; Social Security Fairness Act: WEP and GPO update',
         'https://www.ssa.gov/benefits/retirement/social-security-fairness-act.html'),
        ('SSA &mdash; Benefits planner: retirement',
         'https://www.ssa.gov/benefits/retirement/'),
        ('SSA &mdash; Contact Social Security', 'https://www.ssa.gov/agency/contact/'),
    ],
    'next': {'slug': 'social-security-login',
             'title': 'Locked out of your Social Security account',
             'blurb': 'The old username and password stopped working. Here is what replaced them.'},
}

# ------------------------------------------------------------- SSA login
ARTICLES7['social-security-login'] = {
    'title': 'Locked Out of Your Social Security Account &mdash; The Second Half Guide',
    'eyebrow': 'Facts &amp; thresholds',
    'h1': 'Locked out of your Social Security account',
    'dek': 'The username and password you’ve used for years no longer work. Nothing has gone wrong '
           '&mdash; the sign-in system was replaced, and getting back in takes about twenty minutes.',
    'meta': '5 minute read &middot; Verified against SSA guidance',
    'checked': CHECKED,
    'body': """      <p>You go to check your benefit statement, type in the username you've used since 2016, and it
      doesn't work. You try to reset the password and that doesn't work either. Nothing on the screen
      explains why.</p>

      <p>Your account is fine. Social Security <strong>retired its own username-and-password system</strong>
      and moved sign-in to two outside credential services. If you had an old-style login, it simply
      stopped working, and the message explaining that was easy to miss.</p>

      <h2>What replaced it</h2>

      <p>You now sign in through one of two identity services: <strong>Login.gov</strong>, run by the
      federal government, or <strong>ID.me</strong>, a private company the government contracts with. Both verify who you are once, then let you into Social Security — and, in
      Login.gov's case, a long list of other federal services with the same credential.</p>

""" + facts('The two options', [
        ('Login.gov', 'Run by the federal government and the simpler path for most people. If you have '
                      'no strong reason to choose otherwise, choose this.'),
        ('ID.me', 'A private service SSA also accepts. Useful if you already have an account, or if '
                  'Login.gov can’t verify you &mdash; which happens with recent moves, military '
                  'addresses, or a thin credit file.'),
        ('Already have either?', 'Use it. You don’t need a new account, and one credential works across '
                                 'many agencies.'),
        ('How long it takes', 'Typically 5&ndash;20 minutes, once.'),
        ('What you’ll need', 'An email address, a phone, a state ID or driver’s license, and your Social '
                             'Security number.'),
        ('Two-factor', 'Required. A code by text or an authenticator app each time you sign in.'),
    ]) + """
      <blockquote class="pull">
        <p>This is a one-time twenty minutes, not a permanent obstacle — and the same credential opens
        a good deal of the rest of the government, though not every agency accepts both providers.</p>
      </blockquote>

""" + AD_INLINE + """
      <h2>Where people get stuck</h2>

      <p>Identity verification is the step that defeats people, and usually for reasons that have nothing
      to do with them doing it wrong:</p>

      <ul>
        <li><strong>No recent credit history.</strong> These systems often verify identity against credit
        records. If you have no mortgage, no car loan and no credit card activity — which describes a lot
        of people who've paid everything off — there may be nothing to check you against.</li>
        <li><strong>A frozen credit file.</strong> Sensible protection against fraud, and it blocks
        verification. You may need to lift the freeze temporarily, then reinstate it.</li>
        <li><strong>A recent move</strong>, so your address doesn't match records yet.</li>
        <li><strong>A phone not in your name</strong> — a family plan in a spouse's or child's name is a
        very common cause.</li>
        <li><strong>Name mismatches</strong> after marriage, divorce, or between a license and Social
        Security records.</li>
      </ul>

      <p>If online verification fails, <strong>you are not stuck.</strong> Both services offer alternative
      routes, ID.me includes a video call with a person, and you can always verify in person at a Social
      Security office or, for Login.gov, at a participating post office. That last option is
      underpublicised and works well for people who'd rather deal with a human.</p>

      <h2>The scam that lives on this</h2>

      <p>A confusing change to a government login is exactly the conditions fraud needs, and there is
      already a wave of it.</p>

      <p>You may get an email or text saying your Social Security account has been suspended, needs
      re-verification, or will be closed unless you act — with a link. <strong>Don't use the link.</strong>
      A page reached that way can be a convincing copy built to harvest exactly the information that lets
      someone redirect your benefits &mdash; and you cannot tell from looking. The safe move does not
      depend on judging the message: go to ssa.gov yourself and sign in there. If the warning was real,
      it will be waiting for you inside your account.</p>

      <p>The rule from <a href="/five-minute-rule">the five-minute rule</a> applies unchanged: if the
      contact came to you, go to <em>ssa.gov</em> by typing it yourself.</p>

""" + check([
        'Go to <strong>ssa.gov</strong> by typing the address. Never through a link in an email or text.',
        'Choose <strong>Login.gov</strong> unless you already have ID.me.',
        'Have your <strong>ID, phone and Social Security number</strong> to hand before you start.',
        'If you have a <strong>credit freeze</strong>, plan to lift it temporarily &mdash; then put it '
        'straight back.',
        'If online verification fails, use the <strong>in-person option</strong> at a post office or '
        'Social Security office rather than trying repeatedly.',
        'Write down which service you used and keep your <strong>two-factor method</strong> current. '
        'Changing phone numbers without updating it is the commonest way people lock themselves out again.',
    ]) + """
      <p>Once you're in, it's worth the trip: your earnings record, your benefit estimate, your current
      payment, and your tax forms all live there. The earnings record in particular is worth checking —
      errors do occur, and they quietly shrink a benefit you haven't claimed yet.</p>
""",
    'sources': [
        ('SSA &mdash; Changes to your my Social Security account',
         'https://www.ssa.gov/myaccount/account-transition-faqs.html'),
        ('SSA &mdash; Create an account', 'https://www.ssa.gov/myaccount/create.html'),
        ('Login.gov help', 'https://www.login.gov/help/'),
        ('SSA &mdash; Scam awareness', 'https://www.ssa.gov/scam/'),
    ],
    'next': {'slug': 'wep-gpo-repeal',
             'title': 'The pension rule that cut your Social Security is gone',
             'blurb': 'Two provisions that reduced benefits for public servants were repealed. Some '
                      'people still haven’t claimed.'},
}

# ------------------------------------------------------------ courier scams
ARTICLES7['gold-courier-scam'] = {
    'title': 'When the Scammer Sends Someone to Your Door &mdash; The Second Half Guide',
    'eyebrow': 'Protecting yourself',
    'h1': 'When the scammer sends someone to your door',
    'dek': 'A fast-growing fraud against older adults ends with a stranger collecting cash or gold bars '
           'from your house. The FBI logged about 725 of these in 2025, with $311.8 million in reported '
           'losses, and 98% of the losses fall on people over 60.',
    'meta': '6 minute read &middot; Reflects current FBI and FTC warnings',
    'checked': CHECKED,
    'reader': True,
    'body': """      <p>Most fraud ends with a wire transfer or a gift card. This one ends with a person arriving at
      your house to collect gold bullion, and it is growing fast enough that the FBI has issued repeated
      public warnings.</p>

      <p>In the first months of 2026 alone, federal prosecutors put losses from gold bar schemes at more
      than <strong>$50 million</strong>. In one FBI field office's tally of courier pickups, roughly
      <strong>98% of the losses came from people over 60</strong>.</p>

      <p>It is worth understanding in detail, because it doesn't look like the scams people have been
      warned about.</p>

      <h2>How it actually runs</h2>

      <p>The sequence is remarkably consistent, and it's built as a relay — each stranger hands you to
      the next, and each one seems more official:</p>

      <ol>
        <li><strong>A pop-up or alert</strong> appears on your computer, often locking the screen, with a
        number to call for support.</li>
        <li><strong>The &ldquo;help desk&rdquo;</strong> takes remote control of the machine and announces
        it has found something alarming. Frequently they claim to have found illegal images — a
        deliberately humiliating accusation, chosen because shame stops people telling anyone.</li>
        <li><strong>You're transferred to your &ldquo;bank&rdquo;</strong>, who confirm your accounts are
        compromised or implicated.</li>
        <li><strong>Then to a &ldquo;federal agent&rdquo;</strong> — FBI, FTC, Treasury or the Justice
        Department — who explains you're under investigation, or that your money must be moved somewhere
        safe.</li>
        <li><strong>You're told to convert your savings</strong> into cash or gold bars, to protect them
        in a &ldquo;government escrow account&rdquo; while the investigation proceeds.</li>
        <li><strong>A courier is dispatched</strong> to collect it, sometimes with a code word to prove
        they're legitimate. The gold leaves your house in a stranger's car.</li>
      </ol>

""" + facts('The tells, in the order you’ll meet them', [
        ('A pop-up with a phone number', 'A number that appears inside an alarming warning is the entry '
                                         'point for a large share of these cases. Whether or not the '
                                         'software is genuine, that is not the number to call.'),
        ('Remote access to your computer', 'Once granted, everything they show you on your own screen is '
                                           'under their control.'),
        ('An accusation designed to shame', 'Illegal images, money laundering, drug money. The point is '
                                            'to stop you telling your family.'),
        ('Being transferred &ldquo;up&rdquo;', 'Bank, then agency, then a senior investigator. Each '
                                               'handover is theater.'),
        ('&ldquo;Government escrow&rdquo;', 'No such thing exists. It is not a real process.'),
        ('Buying gold or withdrawing cash', 'This is the moment. No legitimate process ends here.'),
        ('Someone coming to your home', 'No agency sends a courier for your valuables. Ever.'),
    ]) + """
      <blockquote class="pull">
        <p>No government agency — not the FBI, not the FTC, not the Treasury — will ever ask you to buy
        gold. There is no version of this that is real.</p>
      </blockquote>

""" + AD_INLINE + """
      <h2>Why intelligent people go through with it</h2>

      <p>From outside it looks impossible. Inside it's built carefully.</p>

      <p>The accusation does most of the work. Being told there's illegal material on your computer is
      humiliating and frightening, and the natural response is to sort it out privately rather than
      involve your family — which delivers exactly the isolation the scheme needs. Several documented
      victims kept it secret from a spouse in the same house.</p>

      <p>Then the money is never framed as a payment. You're not buying anything or paying a fine. You're
      being told to <em>protect</em> your own savings by moving them somewhere secure — which sounds
      prudent rather than reckless. Handing gold to a courier feels, at that moment, like the responsible
      thing to do.</p>

      <p>And it runs for days or weeks, with daily calls and updates. It's a relationship by the time the
      courier arrives.</p>

      <h2>The rules that stop it</h2>

""" + check([
        '<strong>Never call a number that a pop-up gave you.</strong> If you think the warning might '
        'be real, close the browser &mdash; hold the power button if you must &mdash; and reach the '
        'company through a number you looked up yourself. That works whether the warning was genuine '
        'or not, which is the point.',
        'Never give <strong>remote access</strong> to anyone who contacted you first.',
        'No agency, bank or investigator will ever tell you to buy <strong>gold, silver or '
        'cryptocurrency</strong>, or to hand valuables to a courier. Treat any of these as proof.',
        'Any demand for <strong>secrecy from your family</strong> is the tell. Real investigations don’t '
        'require you to lie to your spouse.',
        'If you’re accused of something shocking, that is the moment to <strong>tell somebody</strong>, '
        'not to handle it alone. The accusation exists to isolate you.',
        'Hang up and <strong>call back on a number you looked up</strong> &mdash; your bank’s card, the '
        'agency’s public site. Then report it at <em>ic3.gov</em> and <em>ReportFraud.ftc.gov</em>.',
    ]) + """
      <h2>If it’s already happened</h2>

      <p>Report it immediately at <strong>ic3.gov</strong> — speed genuinely matters, and couriers have
      been arrested and assets recovered when reports came in fast. Tell your bank. Have the computer
      properly cleaned, since remote-access software may still be on it. And change passwords from a
      <em>different</em> device.</p>

      <p>Then, please, tell someone. The shame is engineered — it is a designed feature of the scheme,
      not a reflection of your judgment — and it's the thing that keeps people silent while the same
      crew moves to the next address.</p>
""",
    'sources': [
        ('FBI &mdash; Warning on gold bar and bulk cash courier scams',
         'https://www.fbi.gov/contact-us/field-offices/boston/news/fbi-boston-warns-of-increase-in-gold-bar-and-bulk-cash-courier-scams'),
        ('FBI IC3 &mdash; Elder fraud', 'https://www.ic3.gov/crimeinfo/elderfraud'),
        ('FTC &mdash; Scams against older adults',
         'https://consumer.ftc.gov/all-scams/scams-against-older-adults'),
        ('FTC &mdash; Report fraud', 'https://reportfraud.ftc.gov/'),
    ],
    'next': {'slug': 'five-minute-rule',
             'title': 'The five-minute rule',
             'blurb': 'The habit underneath every one of these &mdash; and why urgency is the tell that '
                      'outlives any particular script.'},
}
