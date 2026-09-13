#!/usr/bin/env python3
"""Sixteenth batch: one piece requested directly rather than found in the
weekly news sweep. Covers a durable methodology change (the FAFSA
Simplification Act) rather than breaking news -- checked against agreement
across independent financial-aid sources, since the federal FAFSA/Dept. of
Education sites are proxy-blocked from this sandbox per CLAUDE.md section 2."""

from build_articles import facts, check, AD_INLINE

ARTICLES16 = {}

CHECKED16 = '13 September 2026'

# ---------------------------------------------------- grandparent 529 & FAFSA
ARTICLES16['grandparent-529-fafsa'] = {
    'title': 'The Grandparent 529 Rule Changed, and Most Families Still Don&rsquo;t Know It '
             '&mdash; The Second Half Guide',
    'eyebrow': 'Facts &amp; thresholds',
    'h1': 'The grandparent 529 rule changed, and most families still don&rsquo;t know it',
    'dek': 'For years, a grandparent helping pay for college could quietly cost a grandchild financial '
           'aid. A federal rule change removed that trap &mdash; but not everywhere, and not for every '
           'school.',
    'meta': '5 minute read &middot; Verified against the FAFSA Simplification Act and current CSS Profile guidance',
    'checked': CHECKED16,
    'body': """      <p>If you opened a 529 account for a grandchild years ago, you may also have absorbed a piece of
      advice that came with it: don&rsquo;t touch it until the financial aid forms are already filed,
      or spend it down carefully in the last year of school, because a distribution could cost your
      grandchild aid. That advice was correct for a long time. It is now mostly obsolete, and a lot of
      families haven&rsquo;t heard the update.</p>

      <p>The change is real and it is federal law, not a rumor or a temporary waiver. But &ldquo;mostly&rdquo;
      is doing real work in that sentence, and the exception is the part almost nobody mentions.</p>

""" + facts('The grandparent 529 rule, before and after', [
        ('Old rule (through the 2023&ndash;24 aid year)',
         'A distribution from a grandparent-owned 529 plan, spent on the grandchild&rsquo;s college costs, '
         'was reported on the FAFSA as the student&rsquo;s untaxed income &mdash; and could reduce aid '
         'eligibility by as much as 50 cents for every dollar distributed.'),
        ('New rule (2024&ndash;25 aid year onward)',
         'That question was removed from the FAFSA entirely. Grandparent-owned 529 distributions are not '
         'reported as student income, and the account itself was never reported as an asset in the first '
         'place &mdash; only accounts owned by the student or a parent are.'),
        ('What changed it', 'The FAFSA Simplification Act, which replaced the old Expected Family '
                            'Contribution formula with the Student Aid Index. This is a permanent '
                            'methodology change, not a one-year exception.'),
        ('What it doesn&rsquo;t touch', 'The CSS Profile &mdash; a separate financial-aid form used by '
                                        'roughly 200 private colleges for their own institutional aid. It '
                                        'still asks about grandparent-owned accounts.'),
    ]) + """
      <h2>What actually changed, mechanically</h2>

      <p>The pre-2024 FAFSA had a line that, in practice, existed to catch exactly this kind of support:
      money paid on the student&rsquo;s behalf by someone other than a parent. A grandparent&rsquo;s 529
      distribution, a check from an aunt, cash from a family friend &mdash; all of it landed in the same
      bucket and counted as the student&rsquo;s own untaxed income. Student income is assessed far more
      harshly than parent income in the federal aid formula, which is why a well-meaning grandparent
      writing a tuition check at the right moment could shrink a grandchild&rsquo;s aid package.</p>

      <p>The new, simplified FAFSA deleted that question. It isn&rsquo;t buried or reworded &mdash; it
      no longer exists on the form. Because of that, it doesn&rsquo;t matter which year a grandparent
      makes the distribution, or how it&rsquo;s timed against when the FAFSA gets filed. There is no
      longer a question capturing it, for any year going forward.</p>

      <p>Worth separating out, because the two get confused constantly: an <strong>asset</strong> and a
      <strong>distribution</strong> are different questions on the FAFSA. A 529 plan owned by a parent (or
      the student) has always counted as a parent asset, assessed gently &mdash; up to about 5.64% of its
      value toward the family&rsquo;s expected contribution. A 529 plan owned by a grandparent was never
      counted as an asset at all, on the old FAFSA or the new one, because it isn&rsquo;t the parent&rsquo;s
      or student&rsquo;s account. The part that changed is narrower and specific: what happens when money
      actually comes <em>out</em> of that grandparent-owned account and reaches the student.</p>

      <blockquote class="pull">
        <p>The old advice was to time a grandparent&rsquo;s 529 distribution carefully. The new FAFSA
        doesn&rsquo;t ask the question that made timing matter.</p>
      </blockquote>

""" + AD_INLINE + """
      <h2>The part almost nobody mentions: the CSS Profile</h2>

      <p>The FAFSA is not the only financial-aid form in use. Roughly 200 private colleges and scholarship
      programs &mdash; concentrated among selective private schools &mdash; also require the CSS Profile, a
      separate application run by the College Board, to determine their own institutional aid. The CSS
      Profile is more detailed than the FAFSA by design, and it has not adopted the FAFSA&rsquo;s
      simplification. It still asks directly about grandparent-owned accounts and planned distributions,
      and individual schools decide for themselves how much weight to give that answer.</p>

      <p>That means the same family, the same 529 account, and the same distribution can be invisible to
      one college&rsquo;s aid formula and visible to another&rsquo;s &mdash; depending on which form that
      specific school requires. A state university relying solely on the FAFSA and a private college that
      also requires the CSS Profile are not playing by the same rule, even though both are awarding
      need-based aid to the same student.</p>

      <h2>What this doesn&rsquo;t change</h2>

      <p>None of this affects how 529 plans work for taxes, or what counts as a qualified education expense.
      It's specifically about how a distribution is reported on financial-aid applications. It also doesn&rsquo;t
      guarantee more aid &mdash; it removes a specific penalty that used to apply to one kind of support. A
      family whose grandchild wasn&rsquo;t going to qualify for need-based aid regardless of income won&rsquo;t
      see a different outcome because of this change.</p>

      <h2>What to actually check</h2>

""" + check([
        'Find out whether every school on your grandchild&rsquo;s list requires the <strong>CSS '
        'Profile</strong> in addition to the FAFSA &mdash; the College Board publishes a participating-'
        'school list, and it changes school to school, not state to state.',
        'If a school requires the CSS Profile, ask that school&rsquo;s financial aid office directly how '
        'it treats grandparent-owned 529 distributions &mdash; the form asks the question, but schools '
        'don&rsquo;t all weigh the answer the same way.',
        'If every school on the list is FAFSA-only, the old advice to delay or carefully time a '
        'grandparent&rsquo;s 529 distribution no longer serves the purpose it used to.',
        'This applies to any nonparent support, not only grandparents &mdash; the same FAFSA question '
        'covered money from any relative or family friend, and its removal covers all of it equally.',
        'None of this changes what a 529 plan owned by a <strong>parent or the student</strong> reports as '
        'an asset &mdash; that question is still on the form, at the older, gentler asset rate.',
    ]) + """
      <p>A rule this specific rarely gets a headline, so it tends to travel by word of mouth years after
      it takes effect &mdash; which is exactly how a grandparent can still be quietly working around a
      penalty that a federal form stopped asking about two aid cycles ago.</p>
""",
    'sources': [
        ('Saving for College &mdash; The &ldquo;Grandparent Loophole&rdquo;: Grandparent-Owned 529 '
         'Accounts and the New FAFSA',
         'https://www.savingforcollege.com/article/new-fafsa-removes-roadblocks-for-grandparent-529-plans'),
        ('Kiplinger &mdash; Use the 529 &ldquo;Grandparent Loophole&rdquo; to Maximize College Savings',
         'https://www.kiplinger.com/personal-finance/college/use-the-529-grandparent-loophole-to-maximize-college-savings'),
        ('Saving for College &mdash; Does a 529 Plan Affect Financial Aid?',
         'https://www.savingforcollege.com/article/yes-your-529-plan-will-affect-financial-aid'),
        ('College Board &mdash; CSS Profile',
         'https://cssprofile.collegeboard.org/'),
    ],
    'next': {'slug': 'long-distance',
             'title': 'The new long-distance grandparent',
             'blurb': 'Grandparenting keeps changing shape &mdash; this is the piece on the version that '
                      'isn&rsquo;t about money at all.'},
}
