"""Related-reading clusters.

Each list is a set of pages a reader on any one of them would plausibly want
next. A page's related links come from the clusters it appears in, ranked by
how close the two pages sit inside a cluster (order below is deliberate: closest
neighbors first). The first cluster naming a page is its home and counts triple. Pages in no cluster, or with fewer than MIN links, are topped
up from their own homepage category, newest first. Slugs that are not built
pages are ignored, so a cluster can name a page before it ships.
"""

CLUSTERS = [
    # Medicare: enrolling, windows, switching
    ['medicare-enrollment', 'open-enrollment', 'medicare-advantage-oep', 'medigap-window',
     'advantage-vs-original', 'anoc-letter', 'cobra-medicare-trap', 'hsa-medicare-timing'],
    # Medicare Advantage and the 2027 plan year
    ['ma-plan-exits-2027', 'ma-flex-card-2027', 'medicare-marketing-rules-2026', 'anoc-letter',
     'medicare-2027-costs', 'advantage-vs-original', 'open-enrollment'],
    # What Medicare costs
    ['medicare-2027-costs', 'drug-cap', 'drug-negotiation-2027', 'irmaa', 'medicare-savings',
     'medicare-gaps', 'globe-part-b-drugs'],
    ['medicare-gaps', 'long-term-care', 'observation-status', 'wellness-visit', 'medigap-window'],
    ['irmaa', 'medicare-savings', 'medicare-2027-costs', 'cola', 'aca-subsidy-cliff'],
    ['aca-subsidy-cliff', 'aca-unauthorized-enrollment', 'cobra-medicare-trap', 'medicare-enrollment'],
    # Social Security: claiming and benefits
    ['social-security-62', 'delayed-retirement-credit', 'spousal-benefits', 'widows-penalty',
     'claiming-age-clarity-act', 'cola', 'wep-gpo-repeal'],
    ['cola', 'cola-2027-estimate', 'no-tax-on-social-security', 'irmaa', 'delayed-retirement-credit',
     'medicare-savings'],
    ['no-tax-on-social-security', 'senior-deduction', 'standard-deduction-65'],
    # Social Security: dealing with the agency
    ['overpayment-clawback', 'ssi-wage-reporting', 'compassionate-allowances', 'social-security-login'],
    ['wep-gpo-repeal', 'spousal-benefits', 'social-security-62', 'widows-penalty'],
    # Taxes
    ['senior-deduction', 'senior-deduction-phaseout', 'senior-deduction-sunset', 'standard-deduction-65',
     'no-tax-on-social-security', 'property-tax'],
    # Retirement accounts
    ['catch-up-60-63', 'roth-catch-up', 'rule-of-55', 'rmd-deadline', 'hsa-medicare-timing'],
    ['rmd-deadline', 'beneficiary-form', 'senior-deduction'],
    # Estate paperwork
    ['beneficiary-form', 'power-of-attorney', 'digital-estate', 'widows-penalty', 'long-term-care',
     'rmd-deadline'],
    # Fraud
    ['enrollment-scams', 'search-ad-scam', 'medicare-card-scam', 'five-minute-rule',
     'medical-equipment-fraud', 'aca-unauthorized-enrollment'],
    ['five-minute-rule', 'bank-imposter-scam', 'gold-courier-scam', 'voice-cloning', 'romance-scams',
     'qr-parking-scam'],
    # Aging in place
    ['aging-in-place', 'falls', 'driving', 'hearing-aids', 'downsizing-math', 'long-term-care'],
    ['falls', 'aging-in-place', 'pickleball-injuries', 'vaccine-ages', 'wellness-visit'],
    ['downsizing-math', 'property-tax', 'aging-in-place'],
    # Travel
    ['airport-help', 'airport-security', 'passport-traps', 'travel-medications', 'cruise-medical',
     'travel-insurance'],
    ['the-big-trip', 'go-go-years', 'senior-travel-discounts', 'parks-pass', 'parks-fee-free-days',
     'senior-age'],
    ['passport-traps', 'etias', 'portugal-d7-visa', 'travel-insurance'],
    ['vaccine-ages', 'travel-medications', 'cruise-medical'],
    # Family
    ['grandparent-529-fafsa', 'long-distance', 'skip-gen-travel', 'on-call', 'free-college'],
    ['skip-gen-travel', 'the-big-trip', 'long-distance'],
    ['approaching-60', 'senior-age', 'social-security-62', 'medicare-enrollment', 'catch-up-60-63'],
    ['senior-age', 'approaching-60', 'parks-pass', 'senior-travel-discounts'],
]

MIN = 3
MAX = 4
SPARE = 1  # one extra, in case the page's own "next up" link is among them


def related_for(path, pages, category_pages):
    """Return up to MAX + SPARE related paths for `path`.

    pages: set of built article paths (with leading slash).
    category_pages: this page's homepage-category siblings, newest first.
    """
    slug = path.lstrip('/')
    scores = {}
    home = True  # the first cluster naming this page is its home cluster
    for cluster in CLUSTERS:
        if slug not in cluster:
            continue
        weight = 3 if home else 1
        home = False
        i = cluster.index(slug)
        for j, other in enumerate(cluster):
            if other == slug or '/' + other not in pages:
                continue
            scores['/' + other] = scores.get('/' + other, 0) + weight / (1 + abs(i - j))
    ranked = sorted(scores, key=lambda p: (-scores[p], p))
    out = ranked[:MAX + SPARE]
    if len(out) < MIN + SPARE:
        for p in category_pages:
            if p != path and p in pages and p not in out:
                out.append(p)
            if len(out) >= MIN + SPARE:
                break
    return out
