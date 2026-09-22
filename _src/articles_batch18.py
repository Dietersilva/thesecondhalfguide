#!/usr/bin/env python3
"""Eighteenth batch: two pieces built on CMS's finalized Contract Year 2027
Medicare Advantage and Part D rule (Federal Register, 6 April 2026) -- one
covering a consumer-facing mechanic (the debit-card plan-year lock) and one
covering a consumer-protection rollback (marketing rules loosening 1 October
2026, days before Annual Enrollment opens). Checked against agreement across
independent sources, since cms.gov and federalregister.gov are proxy-blocked
from this sandbox per CLAUDE.md section 2."""

from build_articles import facts, check, AD_INLINE

ARTICLES18 = {}

CHECKED18 = '22 September 2026'

# --------------------------------------------------- MA debit/flex card 2027
ARTICLES18['ma-flex-card-2027'] = {
    'title': 'The Medicare Advantage Debit Card Rule Arriving in 2027 &mdash; The Second Half Guide',
    'eyebrow': 'Facts &amp; thresholds',
    'h1': 'The Medicare Advantage debit card rule arriving in 2027',
    'dek': 'If your plan loads a grocery, dental or over-the-counter allowance onto a card each year, '
           'three things about how that card works are changing &mdash; including the reminder that used '
           'to tell you money was still sitting there.',
    'meta': '5 minute read &middot; Verified against CMS&rsquo;s finalized 2027 Medicare Advantage rule',
    'checked': CHECKED18,
    'body': """      <p>A lot of Medicare Advantage plans hand out a debit card as a supplemental benefit.
      Depending on the plan and a member&rsquo;s eligibility, it may cover over-the-counter items, food or
      groceries, dental cost-sharing, transportation, utilities, or some mix of those &mdash; not every
      plan offers one, the mix varies by plan, and Original Medicare has no such card at all. But for the
      plans that do offer one, CMS finalized three changes to how that card works, starting with the 2027
      plan year.</p>

      <p>None of them are effective yet. All three come from the same regulation: the Contract Year 2027
      Medicare Advantage and Part D final rule, which CMS published in the Federal Register on 6 April
      2026. The changes apply to coverage starting 1 January 2027.</p>

""" + facts('The 2027 debit-card rule, at a glance', [
        ('6 April 2026', 'When CMS finalized the rule, in the Contract Year 2027 Medicare Advantage and '
                         'Part D final rule.'),
        ('2027 plan year', 'The first coverage year the new card rules apply to.'),
        ('Real time', 'A card must electronically verify at the point of sale that a purchase is actually '
                      'for a plan-covered benefit, not just that it happened at an approved kind of store. '
                      'CMS did not mandate one specific technology to do this.'),
        ('Plan-year limit', 'A plan may keep issuing the same physical card year to year, but the dollar '
                            'amount or benefit allocation loaded onto it cannot carry from one plan year '
                            'into the next. This is a forward-looking design rule &mdash; it does not '
                            'retroactively rewrite whatever your current plan already promised for a 2026 '
                            'balance.'),
        ('Dropped', 'The mid-year reminder notice CMS previously required plans to send about how much of '
                    'an allowance was still unused.'),
    ]) + """
      <h2>What actually changes</h2>

      <p>The first change is how the card checks a purchase. Under the new rule, a supplemental-benefit
      debit card has to verify electronically, at the point of sale, that the transaction is actually for
      a plan-covered benefit &mdash; rather than approving a purchase because it happened at an approved
      kind of store. CMS declined to require one specific technology to do this, mentioning merchant
      category codes and inventory-approval systems as examples of mechanisms plans might use. In practice,
      that means a card can decline part of a purchase at the register even at a store the plan otherwise
      allows, if an item falls outside what the plan covers.</p>

      <p>The second change is the one with a deadline attached. Starting with the 2027 plan year, a
      plan may keep issuing the same physical card, but the dollar amount or benefit allocation loaded onto
      it cannot carry from one plan year into the next. Balances that some plans previously let members
      roll forward are locked to the plan year they were issued for. If a plan loads $50 a month toward an
      allowance and a member doesn&rsquo;t spend all of it, that unspent amount stops existing when the
      plan year ends, rather than adding to the following year&rsquo;s balance.</p>

      <p>The third change removes a safeguard rather than adding one. CMS had required plans to send
      members a mid-year reminder showing how much of a supplemental-benefit balance was still unspent.
      The final rule drops that requirement. The two changes arrive together: a hard forfeiture deadline
      with one less built-in nudge that the deadline exists.</p>

      <blockquote class="pull">
        <p>The reminder that used to tell you money was still on the card is going away in the same rule
        that makes losing that money automatic.</p>
      </blockquote>

""" + AD_INLINE + """
      <h2>The part worth being precise about</h2>

      <p>It is tempting to read this as &ldquo;your 2026 balance disappears on January 1,&rdquo; and that
      overstates it. The plan-year lock applies to balances issued under a 2027-design card, so the first
      time it can actually forfeit anything is at the end of 2027, when a 2027 balance would otherwise have
      rolled into 2028. Whether a plan currently lets a 2026 balance carry into 2027 depends on that
      plan&rsquo;s own current design, not on this rule &mdash; some already didn&rsquo;t allow rollover at
      all, and this rule doesn&rsquo;t change that history. What it does guarantee is that going forward,
      no plan can design a card that lets a balance survive past the year it was issued for.</p>

      <p>The other detail worth separating from the headline: this rule only touches Medicare Advantage
      plans that choose to offer a supplemental benefit through a debit card in the first place. Not every
      Advantage plan does, and Original Medicare never has one. If your plan doesn&rsquo;t issue this kind
      of card, none of the above applies to you.</p>

      <h2>A public eligibility requirement, too</h2>

      <p>A related piece of the same rule affects plans offering Special Supplemental Benefits for the
      Chronically Ill (SSBCI) &mdash; an extra tier of benefits, like broader food or transportation
      allowances, available only to members who meet specific medical or eligibility criteria. Plans
      offering SSBCI must now publicly post the plan-developed eligibility criteria they use, rather than
      leaving members to discover the conditions only after a card arrives or a claim is denied.</p>

      <h2>Worth doing before the year turns over</h2>

""" + check([
        'Check your <strong>current 2026 balance</strong> now, while a mid-year reminder notice might '
        'still be part of your plan&rsquo;s current design. Don&rsquo;t assume next year&rsquo;s plan will '
        'send one.',
        'Read your plan&rsquo;s <strong>Annual Notice of Change</strong>, arriving by 30 September, for '
        'exactly how it describes the 2027 allowance and any rollover language.',
        'If you are comparing plans during Annual Enrollment, ask directly whether a debit-card benefit '
        'exists at all, and whether unused amounts carry forward under the plan&rsquo;s <strong>current, '
        'stated terms</strong> &mdash; not under this rule, which sets a ceiling on rollover going '
        'forward but doesn&rsquo;t require a plan to offer any.',
        'If a card declines part of a purchase, treat it as the <strong>point-of-sale check working as '
        'designed</strong> &mdash; an item outside the plan&rsquo;s covered categories, not necessarily a '
        'card malfunction &mdash; and ask the plan which categories apply before assuming an error.',
        'If your plan offers benefits tied to a chronic-illness eligibility tier, look for the '
        '<strong>publicly posted criteria</strong> the plan is now required to provide, rather than relying '
        'on what a card mailer or enrollment call describes.',
    ]) + """
      <p>None of this changes what Medicare Advantage is or isn&rsquo;t required to offer. It changes how
      precisely a benefit some plans already offer has to behave, and it removes one of the reminders that
      used to make the deadline easy to miss. The plan year is now a hard edge for this kind of balance;
      knowing that in September is more useful than finding out in January.</p>
""",
    'sources': [
        ('CMS &mdash; Contract Year 2027 Medicare Advantage and Part D Final Rule (fact sheet)',
         'https://www.cms.gov/newsroom/fact-sheets/contract-year-2027-medicare-advantage-part-d-final-rule'),
        ('KFF &mdash; Changes to the Medicare Advantage Program Enhance Some Consumer Protections But Roll '
         'Back Others',
         'https://www.kff.org/medicare/changes-to-the-medicare-advantage-program-enhance-some-consumer-protections-but-roll-back-others/'),
        ('HFMA &mdash; 2027 Medicare Advantage &ndash; Part D Final Rule Summary',
         'https://www.hfma.org/payment-reimbursement-and-managed-care/2027-medicare-advantage-part-d-final-rule-summary/'),
        ('24/7 Wall St. &mdash; In 2027 the Flex Card Checks Your Cart at the Register',
         'https://247wallst.com/personal-finance/2026/08/31/in-2027-the-flex-card-checks-your-cart-at-the-register-what-the-plan-wont-cover-can-be-declined-with-a-line-behind-you/'),
    ],
    'next': {'slug': 'anoc-letter',
             'title': 'The Medicare letter arriving in September, and why it&rsquo;s worth reading',
             'blurb': 'The notice that will actually say how your plan is handling this exact change for '
                      '2027 &mdash; if it applies to you at all.'},
}

# ------------------------------------------------- Medicare marketing rules
ARTICLES18['medicare-marketing-rules-2026'] = {
    'title': 'Medicare&rsquo;s Sales Rules Loosen on October 1 &mdash; The Second Half Guide',
    'eyebrow': 'Facts &amp; thresholds',
    'h1': 'Medicare&rsquo;s sales rules loosen on October 1',
    'dek': 'Two weeks before Annual Enrollment opens, several federal limits on how agents and plans can '
           'reach you are being removed. Here is exactly what changed &mdash; and what is still against '
           'the rules regardless.',
    'meta': '5 minute read &middot; Verified against CMS&rsquo;s finalized 2027 marketing rule and '
            'independent industry coverage',
    'checked': CHECKED18,
    'body': """      <p>Every fall, the volume of Medicare sales calls, mailers and television ads goes up ahead of
      Annual Enrollment. This year, the federal rules governing that outreach are loosening at the same
      time, not tightening. The change takes effect <strong>1 October 2026</strong> &mdash; two weeks
      before Annual Enrollment opens on 15 October &mdash; under the same Contract Year 2027 Medicare
      Advantage and Part D final rule CMS published on 6 April 2026.</p>

""" + facts('What changes 1 October 2026', [
        ('0 hours', 'The new required wait between signing a Scope of Appointment form and a one-on-one '
                    'sales meeting, down from 48 hours.'),
        ('6 years, not 10', 'How long a plan or agent must keep a call record: the actual audio for the '
                            'first 3 years, then audio or a complete transcript for years 4 through 6.'),
        ('Documentation eased, not removed', 'Marketing language such as &ldquo;best&rdquo; or '
                          '&ldquo;most&rdquo; no longer has to cite supporting data directly in the '
                          'material &mdash; but the claim still has to be true and provable if asked.'),
        ('Notice, then removed', 'The required 12-hour gap between an educational event and a sales event '
                    'at the same location is gone, but plans must still announce the switch and give '
                    'attendees a chance to leave first.'),
        ('Still required', 'A signed Scope of Appointment before any specific plan, premium, network or '
                           'benefit can be discussed.'),
        ('Still banned', 'Enrolling someone without consent, and unsolicited contact that violates '
                         'Medicare&rsquo;s permission-to-contact rules.'),
    ]) + """
      <h2>What actually changes</h2>

      <p>The Scope of Appointment, or SOA, is the form that establishes an agent has your permission to
      discuss specific Medicare plans with you. It still exists and is still required. What changes is the
      waiting period: previously, an agent generally had to let 48 hours pass after you signed an SOA
      before holding a one-on-one appointment to discuss actual plans. Starting 1 October, that wait
      disappears &mdash; an agent can move from your signature straight into a sales conversation the same
      day, even the same call.</p>

      <p>Plans and agents also no longer have to keep call records for as long, though the change is more
      specific than a flat cut. The required retention period drops from ten years to six: the actual
      audio recording is required for the first three years, and for years four through six a plan may
      keep either the audio or a complete, accurate transcript instead. A recording made this Annual
      Enrollment has to survive in one of those two forms into roughly 2032, not 2029.</p>

      <p>CMS is also easing how superlative marketing language gets documented &mdash; claims like
      &ldquo;best,&rdquo; &ldquo;top-rated&rdquo; or &ldquo;most affordable.&rdquo; The underlying rule
      does not change: a claim like that still has to be factually supportable, and materials still cannot
      be misleading, confusing or inaccurate. What changes is that a plan no longer has to cite the
      supporting data directly inside the marketing material itself. CMS can still request that
      documentation later, during a review or a complaint investigation.</p>

      <p>A fourth change affects events. Plans holding an educational session &mdash; an informational
      seminar not tied to enrolling in a specific plan &mdash; previously had to wait 12 hours before
      holding a sales-focused event at the same location. That gap is removed, so a marketing event can now
      follow an educational one immediately, at the same address, the same day. One protection survives the
      change intact: the plan still has to clearly announce that the educational portion is ending and a
      marketing event is starting, and give attendees a real chance to leave before it begins &mdash; CMS
      has said something as brief as a restroom or snack break counts.</p>

      <blockquote class="pull">
        <p>The tools built to slow a sales conversation down didn&rsquo;t get stronger heading into this
        year&rsquo;s Annual Enrollment. Several got shorter, right as the volume of calls and mail goes
        up.</p>
      </blockquote>

""" + AD_INLINE + """
      <h2>Why the 48-hour rule existed in the first place</h2>

      <p>The waiting period being removed wasn&rsquo;t arbitrary. CMS introduced it in a 2024 final rule,
      effective from the September 2023 sales season, and said at the time that a mandatory pause gave
      beneficiaries &mdash; including more vulnerable ones &mdash; time to consult a caregiver or family
      member and consider their options before a plan-specific sales conversation began. In the 2027 rule,
      CMS reversed that reasoning, concluding the delay more often got in the way of beneficiaries who
      already wanted the information and were ready to talk. As of 1 October, the built-in space is gone,
      and whatever pause happens between signing an SOA and hearing a sales pitch is left entirely up to
      the individual agent and the individual beneficiary.</p>

      <h2>What did not change</h2>

      <p>Two protections survive intact, and they are worth knowing precisely because so much around them
      loosened. CMS left in place the general prohibition on enrolling someone in a plan without their
      consent. And Medicare&rsquo;s permission-to-contact rules, which restrict unsolicited outreach to
      beneficiaries, are unchanged by this rule &mdash; the specifics of what counts as permitted contact
      versus a prohibited cold call are detailed enough that they are worth checking against Medicare&rsquo;s
      own guidance directly rather than reducing to a single bright line here.</p>

      <p>That distinction matters for a simple reason: an unsolicited call is still something the rules
      constrain, loosened rule or not. A call that does not fit within what Medicare&rsquo;s
      permission-to-contact rules allow is not simply pushier marketing under a looser regime &mdash; it is
      outside the rules as they still stand after 1 October.</p>

      <h2>Why the retention change matters more than it sounds</h2>

      <p>Ten years down to six still doesn&rsquo;t sound like a consumer-facing change, but it affects what
      exists later if a disagreement comes up about what an agent told you. A shorter required retention
      period means a shorter paper trail if a dispute about a call surfaces well after the fact &mdash; the
      kind of dispute that, under a Medicare Advantage enrollment made in October, might not surface until
      a coverage gap shows up the following spring. A recording made this Annual Enrollment has to survive,
      in full audio for the first three years and then as audio or a transcript for three more, into
      roughly 2032 &mdash; four years short of the decade a beneficiary previously had to request one.</p>

      <h2>Worth doing this Annual Enrollment</h2>

""" + check([
        'If a call is <strong>unsolicited</strong> &mdash; you did not give that number to an agent, plan '
        'or lead site for a callback &mdash; treat that as against the rules on its own, regardless of '
        'anything else that happened on the call.',
        'A shorter wait after signing a Scope of Appointment does not shorten <strong>your</strong> right '
        'to take time. &ldquo;Send that to me in writing&rdquo; and &ldquo;I need to check with someone '
        'first&rdquo; remain complete sentences, any time you use them.',
        'Superlative claims like &ldquo;best plan&rdquo; or &ldquo;most coverage&rdquo; still have to be '
        'true and provable, but a plan no longer has to show its work inside the material itself &mdash; '
        'so treat the claim as something to verify yourself rather than something already substantiated on '
        'the page.',
        'If something about a call or enrollment feels wrong, contact your <strong>State Health Insurance '
        'Assistance Program (SHIP)</strong> or <strong>1-800-MEDICARE</strong> to report it. A shorter '
        'federal retention window is a reason to report sooner, not a reason not to.',
        'Remember the Scope of Appointment itself is still required before specific plans, premiums or '
        'benefits come up &mdash; if that conversation starts before any SOA at all, that is still out of '
        'bounds under the rule as it stands after 1 October.',
    ]) + """
      <p>None of this means every call this fall is a problem, and most agents and plans operate well
      within whatever rules apply. But the rules themselves are looser this year than last, at the exact
      moment the outreach volume is highest. Knowing precisely which protections loosened, and which two
      did not, is the difference between reasonable caution and either complacency or unnecessary alarm.</p>
""",
    'sources': [
        ('CMS &mdash; Contract Year 2027 Medicare Advantage and Part D Final Rule (fact sheet)',
         'https://www.cms.gov/newsroom/fact-sheets/contract-year-2027-medicare-advantage-part-d-final-rule'),
        ('Medicare Rights Center &mdash; Final 2027 Medicare Advantage and Part D Rule Increases Plan Pay '
         'and Relaxes Marketing Restrictions',
         'https://www.medicarerights.org/medicare-watch/2026/04/16/final-2027-medicare-advantage-and-part-d-rule-increases-plan-pay-and-relaxes-marketing-restrictions'),
        ('FinanceBuzz &mdash; Medicare&rsquo;s Marketing Rules Loosen October 1',
         'https://financebuzz.com/news/medicares-marketing-rules-loosen'),
    ],
    'next': {'slug': 'enrollment-scams',
             'title': 'Why your phone rings more in October',
             'blurb': 'The scam patterns that show up every Annual Enrollment &mdash; now arriving under '
                      'looser federal marketing rules than last year&rsquo;s.'},
}
