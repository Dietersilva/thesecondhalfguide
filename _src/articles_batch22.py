#!/usr/bin/env python3
"""Twenty-second batch: two pieces from the week of 5-9 October 2026 --
the Claiming Age Clarity Act (H.R. 5284), which renames Social Security's
claiming ages without changing any age or dollar amount (cleared Congress on
29 September; no signature reported at checking time), and CMS's final GLOBE
model for Medicare Part B drugs (finalized 30 September, published in the
Federal Register 2 October, sued over by PhRMA on 7 October).

cms.gov, congress.gov, federalregister.gov and ssa.gov are proxy-blocked here,
so no primary source was read directly. Verified per CLAUDE.md section 2 by
agreement across independent results that trace to the agency or the bill text.
Deliberately omitted because sources split or only one source gave it: the GLOBE
savings totals, the share of covered drugs with 2-12 percent coinsurance, the
named therapeutic categories, and the Claiming Age Clarity Act's implementation
deadline for SSA."""

from build_articles import facts, check, AD_INLINE

ARTICLES22 = {}

CHECKED22 = '9 October 2026'

# ------------------------------------------------------ Claiming Age Clarity Act
ARTICLES22['claiming-age-clarity-act'] = {
    'title': 'Social Security&rsquo;s Claiming Ages Are Getting New Names &mdash; The Second Half Guide',
    'eyebrow': 'Facts &amp; thresholds',
    'h1': 'Social Security&rsquo;s claiming ages are getting new names',
    'dek': 'Congress has sent the President a bill that would rename &ldquo;early,&rdquo; &ldquo;full&rdquo; '
           'and &ldquo;delayed&rdquo; retirement. It changes the labels. It does not change a single age '
           'or dollar amount.',
    'meta': '5 minute read &middot; Checked against the bill text and independent reporting on its '
            'passage',
    'checked': CHECKED22,
    'recheck': {'due': '2026-10-23', 'why': 'The President has a fixed window to sign or veto -- confirm '
                'whether H.R. 5284 became law and update the opening and the status row.'},
    'body': """      <p>On September 29, the Senate passed the Claiming Age Clarity Act by unanimous consent. The House
      had already passed the identical bill on December 1, 2025, so nothing more is needed from Congress.
      The bill, H.R. 5284, went to the President. At the time of this writing no signature had been
      reported.</p>

      <p>What it does is small, and it is easy to overstate. Social Security would change the words it uses
      for the three ages everyone argues about. It would not move the age at which anyone can file, would
      not change what a benefit is worth, and would not touch a formula.</p>

""" + facts('The bill, at a glance', [
        ('Bill', 'H.R. 5284, the Claiming Age Clarity Act.'),
        ('Status', 'Passed the House on December 1, 2025 and the Senate on September 29, 2026 without '
                   'changes. Sent to the President. No signature reported as of October 9.'),
        ('Age 62', 'Now &ldquo;early eligibility age.&rdquo; Would become the <strong>minimum monthly '
                   'benefit age</strong>.'),
        ('Full retirement age', 'Now 66 to 67 depending on birth year. Would become the '
                                '<strong>standard monthly benefit age</strong>.'),
        ('Age 70', 'The age after which waiting adds nothing. Would become the <strong>maximum monthly '
                   'benefit age</strong>.'),
        ('What does not change', 'When you can file, the size of any reduction or increase, and every '
                                 'dollar amount.'),
    ]) + """
      <h2>Why the words matter to anyone</h2>

      <p>The current names carry a built-in bias. &ldquo;Early&rdquo; sounds like a mistake and
      &ldquo;full&rdquo; sounds like the proper amount, which treats a filing at 62 as a discounted version
      of something. As reported, the aim is to describe the same ages by what they do to the
      monthly check: the smallest, the standard and the largest. The wording is meant to make the
      trade-off visible without telling anyone which choice to make.</p>

      <p>The reporting around the bill describes it the same way. It is a terminology change, with
      supporters on both sides of the aisle, and its effect depends on whether plainer names change what
      people understand when they read a benefit statement.</p>

      <h2>How it got here</h2>

      <p>H.R. 5284 passed the House on December 1, 2025, with Representative Smucker, a Pennsylvania
      Republican, as its lead sponsor. The Senate then took it up and passed it on September 29, 2026 by
      unanimous consent, meaning no senator objected and no roll call was held. Because the Senate did
      not amend it, the House did not need to vote again. A bill that reaches the President this way
      becomes law if signed, or if the President does nothing for the period the Constitution allows
      while Congress is in session. A veto would send it back.</p>

      <h2>The ages themselves, as they stand</h2>

""" + facts('Full retirement age, by birth year', [
        ('1954 or earlier', '66'),
        ('1955', '66 and 2 months'),
        ('1956', '66 and 4 months'),
        ('1957', '66 and 6 months'),
        ('1958', '66 and 8 months'),
        ('1959', '66 and 10 months'),
        ('1960 or later', '<strong>67</strong>'),
    ]) + """
      <p>Those are the ages the bill would call the &ldquo;standard monthly benefit age.&rdquo; The
      table is the current law and the bill leaves it alone.</p>

      <h2>What stays exactly the same</h2>

      <p>Everything numerical on the page is untouched. A person born in 1960 or later still reaches full
      retirement age at 67. Filing at 62 still reduces the monthly benefit; for someone whose full
      retirement age is 67, the check at 62 is about 70 percent of the full amount. Waiting past full
      retirement age still adds 8 percent a year of delayed credit up to age 70. Those figures are set by
      law and by the Social Security Act&rsquo;s formulas, and this bill does not amend them.</p>

      <p>The same goes for the earnings test, spousal and survivor benefits, and the cost-of-living
      adjustment. The bill is a vocabulary change applied to existing rules.</p>

      <p>The arithmetic behind the three ages is worth restating because the new names describe it.
      Filing before full retirement age reduces the benefit by 5/9 of 1 percent for each of the first 36
      months early and 5/12 of 1 percent for each month beyond that. That produces the roughly 30
      percent reduction at 62 for a person whose full retirement age is 67. Waiting beyond full
      retirement age adds 2/3 of 1 percent per month, the 8 percent a year, until age 70, after which
      nothing more is added. &ldquo;Minimum,&rdquo; &ldquo;standard&rdquo; and &ldquo;maximum&rdquo; are
      shorthand for the bottom, the middle and the top of that range.</p>

      <blockquote class="pull">
        <p>A bill that renames the ages is not a bill that moves them. Every filing age and every
        percentage on your statement stays where it is.</p>
      </blockquote>

""" + AD_INLINE + """
      <h2>What would actually look different</h2>

      <p>Reporting on the bill says the new terms would replace the old ones in how the Social Security
      Administration describes the ages: on its website, in its publications and on the materials sent to
      beneficiaries. The phrase &ldquo;delayed retirement credit&rdquo; is also reported to be on its way
      out. Because the bill needs a signature first and the agency would then have to update its
      materials, nothing about the vocabulary on a statement in your mailbox changes this month.</p>

      <p>It also means the older names will be in circulation for some time. Articles, calculators and
      advisers will use both, and a reader may meet &ldquo;full retirement age&rdquo; and
      &ldquo;standard monthly benefit age&rdquo; in the same week describing the same birthday. The pieces on this
      site about filing at 62 and about what delaying adds use the current terms, which remain the ones
      the Social Security Administration uses today.</p>

      <h2>What to watch</h2>

""" + check([
        'Whether the bill becomes law: the President signs it, vetoes it, or lets it become law without '
        'a signature. Congress.gov shows the status of H.R. 5284.',
        'Your own numbers are unchanged either way. Your full retirement age depends on your birth year '
        'and is on your <strong>my Social Security</strong> statement.',
        'If you read a headline saying the retirement age has been changed, check whether it means the '
        'name or the age. In this bill it is only the name.',
        'For the arithmetic of filing at 62 versus waiting, see '
        '<a href="/social-security-62">the piece on filing at 62</a> and '
        '<a href="/delayed-retirement-credit">what delaying actually adds</a>.',
    ]) + """
      <p>A bill like this is useful mostly as a reminder of how much of the Social Security conversation
      happens in vocabulary. The three ages are the same ones they were last week. If they are renamed,
      the only thing a reader needs to do is learn which new phrase points to which old one.</p>
""",
    'sources': [
        ('CNBC &mdash; Claiming Age Clarity Act would change Social Security claiming terms',
         'https://www.cnbc.com/2026/10/01/claiming-age-clarity-act-social-security.html'),
        ('AARP &mdash; Can New Social Security Wording Lead to Bigger Checks?',
         'https://www.aarp.org/social-security/retirement-age-clarity-act/'),
        ('GovTrack &mdash; Claiming Age Clarity Act (H.R. 5284)',
         'https://www.govtrack.us/congress/bills/119/hr5284'),
        ('Rep. Smucker &mdash; Bipartisan Claiming Age Clarity Act Heads to President&rsquo;s Desk',
         'https://smucker.house.gov/media/press-releases/smuckers-bipartisan-claiming-age-clarity-act-heads-presidents-desk'),
        ('NewsNation &mdash; Congress passes bill to rename Social Security claiming ages',
         'https://www.newsnationnow.com/business/your-money/congress-social-security/'),
    ],
    'next': {'slug': 'social-security-62',
             'title': 'Filing at 62, by the arithmetic',
             'blurb': 'The age the bill would rename, and what the reduction actually is.'},
}

# -------------------------------------------------------------------- GLOBE
ARTICLES22['globe-part-b-drugs'] = {
    'title': 'The Medicare Part B Drug Test That Starts in 2027 &mdash; The Second Half Guide',
    'eyebrow': 'Facts &amp; thresholds',
    'h1': 'The Medicare Part B drug test that starts in 2027, and who is in it',
    'dek': 'CMS has finalized a mandatory pricing model for some drugs given in a doctor&rsquo;s office '
           'or clinic. It applies to Original Medicare patients in randomly chosen areas, not everyone, '
           'and a drug industry lawsuit is already pending.',
    'meta': '6 minute read &middot; Checked against the Federal Register notice and independent '
            'reporting on the final rule',
    'checked': CHECKED22,
    'recheck': {'due': '2026-11-30', 'why': 'The rule\'s reported effective date, and the PhRMA lawsuit '
                'asks a court to postpone it -- confirm the date held and the lawsuit\'s status.'},
    'body': """      <p>On September 30, CMS finalized a model it calls GLOBE, short for Global Benchmark for
      Efficient Drug Pricing. It was published in the Federal Register on October 2. It concerns Medicare
      Part B, which pays for drugs a clinician gives you in an office or clinic &mdash; infusions and some
      injections, for example &mdash; and not for the prescriptions you pick up at a pharmacy, which fall
      under Part D.</p>

      <p>The short version: for certain drugs, in certain places, what Medicare pays and what the patient
      owes would be tied to what other wealthy countries pay. It is a test, it is mandatory for the areas
      chosen, and it does not start for patients until April 2027.</p>

""" + facts('GLOBE, at a glance', [
        ('Who is in it', 'People with <strong>Original Medicare</strong> who live in randomly selected '
                         'geographic areas, about <strong>25%</strong> of Original Medicare enrollees. '
                         'Selection is by ZIP code area.'),
        ('Who is not', 'People in <strong>Medicare Advantage</strong>. And no one chooses to join or '
                       'leave: it is mandatory in the selected areas.'),
        ('What it covers', 'Part B drugs, meaning those given in a clinic or office. Not Part D '
                           'pharmacy prescriptions.'),
        ('Which drugs', 'Single-source drugs and sole-source biologics above $100 million a year in '
                        'Part B spending. Orphan-only drugs, cell and gene therapies and plasma-derived '
                        'products are excluded.'),
        ('Benchmark', 'Prices in <strong>19 other countries</strong>, including Canada, Germany, Japan '
                      'and the United Kingdom.'),
        ('Data collection starts', '<strong>January 1, 2027</strong> (manufacturers submit international '
                                   'prices voluntarily).'),
        ('Lower coinsurance starts', '<strong>April 1, 2027</strong>, running to March 31, 2032.'),
        ('Litigation', 'PhRMA, the drug industry trade group, sued on <strong>October 7</strong> in federal '
                       'court in Washington to block it.'),
    ]) + """
      <h2>What a patient would notice</h2>

      <p>In Original Medicare, Part B generally leaves the patient with <strong>20% coinsurance</strong>
      on a covered drug given in a clinic. That share is a percentage of the price, which is why a very
      expensive drug can mean a very large bill. The GLOBE model ties the coinsurance for the drugs it
      covers to the international benchmark rather than to the full U.S. price. CMS gave an illustration
      in which coinsurance falls to 10%, so that a patient owing $20 on a $100 allowed amount would owe
      $10. That example shows how the mechanism works. It is not a promise about any particular drug.</p>

      <p>Providers are paid less to offset the lower coinsurance, since Medicare&rsquo;s payment is the
      allowed amount minus the patient&rsquo;s share. The patient-facing change is therefore the
      coinsurance line, not what the clinic bills.</p>

      <h2>Why it is narrower than the proposal</h2>

      <p>The final rule is smaller than what CMS first proposed. The start was pushed from October 2026
      to 2027, the covered drugs were limited to specific categories with more than $100 million in
      annual Part B spending, and several kinds of drugs were excluded. Estimates of the savings fell
      sharply as a result, though the figures reported for the old and new versions are not directly
      comparable, so this piece does not quote them.</p>

      <blockquote class="pull">
        <p>GLOBE is a test in about a quarter of Original Medicare, not a change for everyone. Whether
        you are in it depends on where you live, not on what you chose.</p>
      </blockquote>

""" + AD_INLINE + """
      <h2>Part B and Part D are different systems</h2>

      <p>It helps to keep the two apart, because news about drug prices usually blurs them. Part D covers
      drugs you take yourself and pick up at a pharmacy, and it has the annual out-of-pocket cap and the
      negotiated prices covered in the piece on the
      <a href="/drug-negotiation-2027">next round of Medicare drug discounts</a>. Part B covers drugs
      administered by a clinician, usually where you are treated, and it works on the 20 percent
      coinsurance described above. GLOBE concerns Part B only. It is a separate effort from the
      negotiation program and does not change the Part D rules.</p>

      <p>Because it is built as a test, CMS chose the areas at random. That is deliberate: a test needs
      a comparison group. Two people with the same plan and the same drug can have different coinsurance
      depending on the ZIP code each lives in. The model does not look at income, diagnosis or the
      plan a person would prefer, and neither a patient nor a doctor can opt into it or out of it.</p>

      <h2>The timeline</h2>

      <p>The proposal would have started the model on October 1, 2026. The final rule moved the start
      to January 1, 2027, when drug manufacturers may begin submitting their international prices
      voluntarily. The part patients feel starts on April 1, 2027, with the lower coinsurance, and the
      performance years run through March 31, 2032. The rule&rsquo;s own effective date, reported as
      November 30, 2026, is when it becomes part of the regulations, and is a different date from the
      day a patient sees any change.</p>

      <h2>The lawsuit</h2>

      <p>The model rests on CMS&rsquo;s authority to test payment approaches. PhRMA argues in its
      complaint that the statute does not let the agency tie Medicare drug rebates to prices in other
      countries, and asks the court to declare the rule unlawful and postpone its effective date. The
      effective date reported for the final rule is November 30, 2026. A court can narrow, delay or
      block a rule, so the April 2027 start is the plan, not a guarantee. The outcome of the case will
      decide whether that happens on schedule.</p>

      <h2>What this does not touch</h2>

      <p>Part D premiums, the $2,400 out-of-pocket cap on prescriptions and the Part B premium are all
      separate from this model. Nothing about GLOBE changes what is on a Medicare Advantage plan&rsquo;s
      benefit page. If a person is in Original Medicare, lives in a selected area and is given a covered
      drug, the coinsurance line is what changes.</p>

      <h2>What to watch</h2>

""" + check([
        'You are affected only if you have <strong>Original Medicare</strong>, live in a selected '
        'area, and are given a covered Part B drug. Medicare Advantage members are not included.',
        'Nothing changes for patients before <strong>April 1, 2027</strong>, even if the rule takes '
        'effect earlier.',
        'Ask the clinic or infusion center about <strong>coinsurance</strong> before a course of '
        'treatment starts. That is the number the model is designed to change.',
        'Follow the court case. A ruling could change the start date or the model itself.',
        'Part D prescriptions you fill at a pharmacy are a separate system and are unaffected.',
    ]) + """
      <p>Whether the model survives, and what it saves, will take years to show. The thing to know now
      is narrow: who is in it, what it touches, and when it starts.</p>
""",
    'sources': [
        ('Federal Register &mdash; Global Benchmark for Efficient Drug Pricing (GLOBE) Model',
         'https://www.federalregister.gov/documents/2026/10/02/2026-20281/global-benchmark-for-efficient-drug-pricing-globe-model'),
        ('CMS &mdash; CMS Finalizes New Mandatory Drug Payment Model to Deliver Lower Drug Prices for '
         'Beneficiaries in Original Medicare Part B',
         'https://www.cms.gov/newsroom/press-releases/cms-finalizes-new-mandatory-drug-payment-model-deliver-lower-drug-prices-beneficiaries-original'),
        ('AJMC &mdash; CMS Finalizes Mandatory GLOBE Model to Test Lower Part B Drug Costs',
         'https://www.ajmc.com/view/cms-finalizes-mandatory-globe-model-to-test-lower-part-b-drug-costs'),
        ('Skadden &mdash; CMS Finalizes the GLOBE Model',
         'https://www.skadden.com/insights/publications/2026/10/cms-finalizes-the-globe-model'),
        ('Fierce Healthcare &mdash; PhRMA launches new legal challenge as CMS brings &ldquo;most '
         'favored nation&rdquo; pricing to Medicare Part B',
         'https://www.fiercehealthcare.com/pharma/phrma-launches-new-legal-challenge-cms-brings-most-favored-nation-pricing-medicare-part-b'),
    ],
    'next': {'slug': 'drug-cap',
             'title': 'The $2,100 drug cap',
             'blurb': 'The pharmacy side of Medicare drug costs, which GLOBE does not touch.'},
}
