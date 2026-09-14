(() => {
'use strict';
const TODAY = {year: 2026, month: 9};
const MAIN = [62, 65, 67];
const YEARS = [62, 63, 64, 65, 66, 67];
const MONTHS = ['January','February','March','April','May','June','July','August','September','October','November','December'];
const $ = id => document.getElementById(id);
const MONEY_FMT = new Intl.NumberFormat('en-US', {style: 'currency', currency: 'USD', maximumFractionDigits: 0});
const money = n => MONEY_FMT.format(Number.isFinite(n) ? n : 0);
const pct = n => `${Math.max(0, Math.min(999, Math.round(n)))}%`;
const num = (id, min = 0, max = 1e9) => {const e = $(id), v = Number(e?.value); return Number.isFinite(v) ? Math.max(min, Math.min(max, v)) : min;};
const radio = name => document.querySelector(`input[name="${name}"]:checked`)?.value || '';

// Average wage index, contribution-and-benefit base, and PIA bend points by year.
// Known years are SSA-published/projected figures; other years fall back to extrapolation below.
const AWI = {1980:12513.46,1981:13773.10,1982:14531.34,1983:15239.24,1984:16135.07,1985:16822.51,1986:17321.82,1987:18426.51,1988:19334.04,1989:20099.55,1990:21027.98,1991:21811.60,1992:22935.42,1993:23132.67,1994:23753.53,1995:24705.66,1996:25913.90,1997:27426.00,1998:28861.44,1999:30469.84,2000:32154.82,2001:32921.92,2002:33252.09,2003:34064.95,2004:35648.55,2005:36952.94,2006:38651.41,2007:40405.48,2008:41334.97,2009:40711.61,2010:41673.83,2011:42979.61,2012:44321.67,2013:44888.16,2014:46481.52,2015:48098.63,2016:48642.15,2017:50321.89,2018:52145.80,2019:54099.99,2020:55628.60,2021:60575.07,2022:63795.13,2023:66621.80,2024:69846.57,2025:72025.07,2026:75246.70,2027:78286.92,2028:81537.43,2029:85047.82,2030:88895.99,2031:92915.31,2032:96989.47,2033:101085.63,2034:105045.59,2035:109064.86};
const CBB = {1980:25900,1981:29700,1982:32400,1983:35700,1984:37800,1985:39600,1986:42000,1987:43800,1988:45000,1989:48000,1990:51300,1991:53400,1992:55500,1993:57600,1994:60600,1995:61200,1996:62700,1997:65400,1998:68400,1999:72600,2000:76200,2001:80400,2002:84900,2003:87000,2004:87900,2005:90000,2006:94200,2007:97500,2008:102000,2009:106800,2010:106800,2011:106800,2012:110100,2013:113700,2014:117000,2015:118500,2016:118500,2017:127200,2018:128400,2019:132900,2020:137700,2021:142800,2022:147000,2023:160200,2024:168600,2025:176100,2026:184500,2027:190200,2028:198900,2029:206700,2030:215400,2031:224700,2032:234900,2033:245400,2034:256200,2035:267000};
const BEND = {2018:[895,5397],2019:[926,5583],2020:[960,5785],2021:[996,6002],2022:[1024,6172],2023:[1115,6721],2024:[1174,7078],2025:[1226,7391],2026:[1286,7749],2027:[1326,7991],2028:[1385,8348],2029:[1441,8686],2030:[1501,9046],2031:[1565,9436],2032:[1636,9863],2033:[1710,10309],2034:[1785,10761],2035:[1861,11215]};
const AC = new Map(), PC = new Map();
const awi = y => {if (AC.has(y)) return AC.get(y); let v = AWI[y] || (y < 1980 ? AWI[1980] / Math.pow(1.045, 1980 - y) : AWI[2035] * Math.pow(1.038, y - 2035)); AC.set(y, v); return v;};
const cbb = y => CBB[y] || (y < 1980 ? CBB[1980] / Math.pow(1.05, 1980 - y) : CBB[2035] * Math.pow(1.04, y - 2035));
const bend = y => {if (BEND[y]) return BEND[y]; if (y < 2018) {const f = awi(y - 2) / awi(2016); return [Math.round(895 * f), Math.round(5397 * f)];} const f = awi(y - 2) / awi(2033); return [Math.round(1861 * f), Math.round(11215 * f)];};
const fra = y => y >= 1960 ? 67 : y <= 1937 ? 65 : y <= 1954 ? 66 : 66 + (y - 1954) * 2 / 12;
const factor = (age, y) => {const f = fra(y), m = Math.round((age - f) * 12); if (!m) return 1; if (m < 0) {const e = -m; return 1 - Math.min(36, e) * (5 / 9 / 100) - Math.max(0, e - 36) * (5 / 12 / 100);} return 1 + Math.min(m, Math.max(0, (70 - f) * 12)) * (2 / 3 / 100);};
const spFactor = (age, y) => {const m = Math.max(0, Math.round((fra(y) - age) * 12)); return m ? 1 - Math.min(36, m) * (25 / 36 / 100) - Math.max(0, m - 36) * (5 / 12 / 100) : 1;};

function populateMonths() {
  ['birth-month', 'spouse-birth-month'].forEach(id => {
    const e = $(id);
    if (!e || e.options.length) return;
    MONTHS.forEach((m, i) => {const o = document.createElement('option'); o.value = i + 1; o.textContent = m; e.appendChild(o);});
    e.value = '1';
  });
}

function person(prefix = '') {
  const spouse = prefix === 'spouse-';
  return {
    birthMonth: num(prefix + 'birth-month', 1, 12),
    birthYear: num(prefix + 'birth-year', 1930, 1970),
    retireAge: num(prefix + 'retire-age', 62, 75),
    wages: num(spouse ? 'spouse-wages' : 'wages'),
    futureWages: num(spouse ? 'spouse-future-wages' : 'future-wages'),
    years: num(prefix + 'years-worked', 10, 45),
    override: num(spouse ? 'spouse-ss-override' : 'ss-override'),
    overrideAge: num(spouse ? 'spouse-ss-override-age' : 'ss-override-age', 62, 70),
    countable: num(spouse ? 'spouse-countable-earnings' : 'countable-earnings'),
  };
}

// PIA depends on the claim age being evaluated: wage projection stops at whichever
// comes first, that age, the planned retirement age, or the table's projection cap.
function piaCalc(p, a) {
  if (p.override > 0) return p.override / Math.max(.1, factor(p.overrideAge, p.birthYear));
  const ey = p.birthYear + 62, iy = ey - 2, cy = TODAY.year;
  const last = Math.min(Math.max(0, p.wages), cbb(cy));
  const yrs = Math.max(10, Math.min(45, p.years));
  const start = cy - yrs + 1;
  const end = Math.max(cy, Math.min(p.birthYear + a, p.birthYear + p.retireAge, 2035));
  const v = [];
  for (let y = start; y <= end; y++) {
    let n = y <= cy ? last * (awi(y) / awi(cy)) / Math.pow(1.02, cy - y) : Math.min(p.futureWages || p.wages, cbb(y));
    n = Math.min(n, cbb(y));
    v.push(n * (y < iy ? awi(iy) / awi(y) : 1));
  }
  v.sort((x, y) => y - x);
  const top = v.slice(0, 35);
  while (top.length < 35) top.push(0);
  const aime = Math.floor(top.reduce((x, y) => x + y, 0) / 420);
  const [b1, b2] = bend(ey);
  let q = .9 * Math.min(aime, b1);
  if (aime > b1) q += .32 * Math.min(aime - b1, b2 - b1);
  if (aime > b2) q += .15 * (aime - b2);
  return Math.floor(q * 10) / 10;
}
function pia(p, a) {
  const k = [p.birthYear, p.retireAge, p.wages, p.futureWages, p.years, p.override, p.overrideAge, a].join('|');
  if (PC.has(k)) return PC.get(k);
  const v = piaCalc(p, a);
  PC.set(k, v);
  return v;
}
function monthly(a, p) {return pia(p, a) * factor(a, p.birthYear);}
function grossAnnual(a, p) {return monthly(a, p) * 12;}
function withheldAnnual(a, p, limit) {
  const f = fra(p.birthYear);
  if (a >= f) return 0;
  const g = grossAnnual(a, p);
  // The calendar year full retirement age is reached uses a higher limit and a $1-for-$3 rule
  // instead of the standard $1-for-$2 rule that applies in earlier years.
  return f - a < 1 ? Math.min(g, Math.max(0, p.countable - 65160) / 3) : Math.min(g, Math.max(0, p.countable - limit) / 2);
}
function personAnnual(a, p, test, limit) {return Math.max(0, grossAnnual(a, p) - (test ? withheldAnnual(a, p, limit) : 0));}
function excess(ra, r, wa, w) {return Math.max(0, .5 * pia(w, wa) - pia(r, ra)) * spFactor(ra, r.birthYear);}

// Household Social Security total for a given pair of claim ages, including each
// spouse's own worker benefit plus any spousal excess either qualifies for.
function comp(a, b, s, age = null, test = false) {
  const off = (s.you.birthYear + (s.you.birthMonth - 1) / 12) - (s.spouse.birthYear + (s.spouse.birthMonth - 1) / 12);
  const spouseAge = age === null ? Infinity : age + off;
  const youActive = age === null || age >= a;
  const spouseActive = s.household === 'couple' && (age === null || spouseAge >= b);
  const youOwn = youActive ? personAnnual(a, s.you, test, s.limit) : 0;
  const spouseOwn = spouseActive ? personAnnual(b, s.spouse, test, s.limit) : 0;
  let youExcess = 0, spouseExcess = 0;
  if (youActive && spouseActive) {
    youExcess = excess(a, s.you, b, s.spouse) * 12;
    spouseExcess = excess(b, s.spouse, a, s.you) * 12;
  }
  const total = youOwn + spouseOwn + youExcess + spouseExcess;
  return {youOwn, spouseOwn, youExcess, spouseExcess, total, monthly: total / 12};
}
function ssAnnual(claimAge, s, test = false) {return comp(claimAge, claimAge, s, null, test).total;}
function atAge(age, a, b, s, test = false) {return comp(a, b, s, age, test).total;}

function state() {
  return {
    household: radio('household'), earlyUse: radio('early-ss-use'),
    you: person(), spouse: person('spouse-'),
    traditional: num('traditional-balance'), roth: num('roth-balance'), taxable: num('taxable-balance'),
    contrib: num('annual-contrib'), employer: num('employer-contrib'),
    spouseContrib: num('spouse-contrib'), spouseEmployer: num('spouse-employer-contrib'),
    returnRate: num('return-rate', 0, 12) / 100,
    pension: num('pension-income'), other: num('other-income'), spending: num('annual-spending'),
    horizon: num('horizon', 80, 100), limit: num('earnings-limit'),
    partB: $('part-b-start')?.value || '', hsa: !!$('hsa')?.checked,
    coverage: !!$('active-employer-coverage')?.checked, creditable: !!$('creditable-drug')?.checked,
    employerSize: $('employer-size')?.value || 'unknown',
  };
}

function ageNow(p) {let a = TODAY.year - p.birthYear; if (TODAY.month < p.birthMonth) a--; return a;}
// A birth-date offset that translates between "your age" and "your spouse's age."
function householdOffset(s) {return (s.you.birthYear + (s.you.birthMonth - 1) / 12) - (s.spouse.birthYear + (s.spouse.birthMonth - 1) / 12);}
// The household's shared "both retired" age, since a couple's retirement dates can differ.
function bothRetiredAge(s) {if (s.household !== 'couple') return s.you.retireAge; return Math.max(s.you.retireAge, s.spouse.retireAge - householdOffset(s));}
function contributionsAt(age, s) {
  let c = age < s.you.retireAge ? s.contrib + s.employer : 0;
  if (s.household === 'couple' && age + householdOffset(s) < s.spouse.retireAge) c += s.spouseContrib + s.spouseEmployer;
  return c;
}
function baseAtRetirement(s, rate = s.returnRate) {
  let bal = s.traditional + s.roth + s.taxable;
  const start = ageNow(s.you), retire = bothRetiredAge(s);
  for (let age = start; age < retire; age++) {bal *= 1 + rate; bal += contributionsAt(age, s);}
  return bal;
}
function portfolioForClaim(claimAge, s, rate = s.returnRate) {
  let bal = s.traditional + s.roth + s.taxable;
  const start = ageNow(s.you), retire = bothRetiredAge(s);
  for (let age = start; age < retire; age++) {
    bal *= 1 + rate;
    bal += contributionsAt(age, s);
    if (s.earlyUse === 'invest') bal += atAge(age, claimAge, claimAge, s, true);
  }
  const atRetire = bal;
  for (let age = Math.round(retire); age < s.horizon; age++) {
    bal *= 1 + rate;
    const income = atAge(age, claimAge, claimAge, s, false) + s.pension + s.other;
    bal -= Math.max(0, s.spending - income);
    if (bal < 0) {bal = 0; break;}
  }
  return {atRetire, horizon: bal};
}
// Cumulative benefits received through a given age, accounting for the birth-date
// offset so a couple's two claim clocks line up correctly against each other.
function cumulative(claimAge, through, s) {
  const off = s.household === 'couple' ? householdOffset(s) : 0;
  let total = 0;
  for (let age = Math.floor(Math.min(claimAge, claimAge - off)); age <= through; age++) total += atAge(age, claimAge, claimAge, s, age < s.you.retireAge);
  return total;
}
function cumulativeMixed(a, b, through, s) {
  const off = s.household === 'couple' ? householdOffset(s) : 0;
  let total = 0;
  for (let age = Math.floor(Math.min(a, b - off)); age <= through; age++) total += atAge(age, a, b, s, age < s.you.retireAge);
  return total;
}
function cross(a, b, s) {for (let age = b; age <= 100; age++) {if (cumulative(b, age, s) >= cumulative(a, age, s)) return age;} return null;}
function incomeAtRetirement(claimAge, s) {return atAge(s.you.retireAge, claimAge, claimAge, s, false) + s.pension + s.other;}
function spendingCoverage(claimAge, s) {if (s.spending <= 0) return 100; return incomeAtRetirement(claimAge, s) / s.spending * 100;}

function renderMeaning(s) {
  const be65 = cross(62, 65, s), be67 = cross(62, 67, s), p62 = portfolioForClaim(62, s), p67 = portfolioForClaim(67, s);
  const earlyWithheld = withheldAnnual(62, s.you, s.limit) + (s.household === 'couple' ? withheldAnnual(62, s.spouse, s.limit) : 0);
  const lines = [];
  lines.push(`<div class="rsm-note"><strong>Cash sooner vs. larger check later:</strong> Claiming at 62 starts income earlier. Claiming at 67 produces about <b>${money(ssAnnual(67, s) - ssAnnual(62, s))} more per year</b> once both strategies are fully in pay status.</div>`);
  if (be65 || be67) lines.push(`<div class="rsm-note"><strong>When waiting catches up:</strong> Under these inputs, 65 catches 62 at about <b>age ${be65 || '100+'}</b>, while 67 catches 62 at about <b>age ${be67 || '100+'}</b>.</div>`);
  lines.push(`<div class="rsm-note"><strong>Portfolio consequence:</strong> At age ${s.horizon}, the model shows about <b>${money(p62.horizon)}</b> remaining if you claim at 62 versus <b>${money(p67.horizon)}</b> if you claim at 67, using your spending and return assumptions.</div>`);
  if (earlyWithheld > 0) lines.push(`<div class="rsm-note"><strong>Working matters:</strong> Your entered earnings could cause roughly <b>${money(earlyWithheld)}</b> of first-year benefits to be withheld if benefits begin at 62 under the current 2026 earnings-test limit.</div>`);
  $('meaning-results').innerHTML = lines.join('');
}
function renderGoals(s) {
  const retire = s.you.retireAge, earningsImpact = withheldAnnual(62, s.you, s.limit) > 0;
  $('goal-results').innerHTML = `<div class="rsm-medicare-card"><strong>Claim at 62</strong><p><b>Best fit for:</b> earlier cash flow or a shorter planning horizon.${earningsImpact ? ' Your entered work earnings make this option less attractive before FRA because benefits may be withheld.' : ''}</p></div><div class="rsm-medicare-card"><strong>Claim at 65</strong><p><b>Best fit for:</b> a middle path between earlier checks and a larger monthly benefit.${Math.abs(retire - 65) <= 1 ? ' This also lines up closely with your entered retirement age.' : ''}</p></div><div class="rsm-medicare-card"><strong>Claim at 67</strong><p><b>Best fit for:</b> maximizing the monthly benefit among these three choices and placing more weight on longevity protection.</p></div>`;
}
function renderEarnings(s) {
  const people = [['You', s.you]];
  if (s.household === 'couple') people.push(['Spouse', s.spouse]);
  $('earnings-results').innerHTML = people.map(([label, p]) => {
    const w62 = withheldAnnual(62, p, s.limit), gross = grossAnnual(62, p), net = Math.max(0, gross - w62);
    if (w62 <= 0) return `<div class="rsm-note"><strong>${label}:</strong> Entered countable earnings are not above the current ${money(s.limit)} annual limit, so this simple 62 illustration shows no earnings-test withholding.</div>`;
    return `<div class="rsm-note"><strong>${label} at 62:</strong> Estimated gross benefit ${money(gross)}/yr. With entered countable earnings, roughly <b>${money(w62)}</b> could be withheld, leaving about <b>${money(net)}</b> paid before tax in this simplified full-year illustration. Benefits withheld under the earnings test are not simply lost; SSA later adjusts for months withheld at full retirement age.</div>`;
  }).join('');
}
function renderStress(s) {
  const base = s.returnRate, low = Math.max(0, base - .02), high = Math.min(.10, base + .02);
  const rows = [['Conservative', low], ['Your assumption', base], ['Stronger return', high]];
  $('stress-body').innerHTML = rows.map(([label, rate]) => `<tr><td><strong>${label}</strong><br><small>${(rate * 100).toFixed(1)}% annual return</small></td>${MAIN.map(age => {const v = portfolioForClaim(age, s, rate).horizon; return `<td>${v > 0 ? money(v) : '<b>$0</b><br><small>portfolio depleted before horizon</small>'}</td>`;}).join('')}</tr>`).join('');
}
function renderCouple(s) {
  const panel = $('couple-panel');
  if (s.household !== 'couple') {panel?.classList.add('rsm-hidden'); return;}
  panel?.classList.remove('rsm-hidden');
  $('couple-body').innerHTML = MAIN.map(a => `<tr><td><strong>You ${a}</strong></td>${MAIN.map(b => `<td>${money(comp(a, b, s).total)}/yr<br><small>${money(cumulativeMixed(a, b, s.horizon, s))} cumulative by ${s.horizon}</small></td>`).join('')}</tr>`).join('');
  const c = comp(65, 65, s);
  $('survivor-watch').innerHTML = `<div class="rsm-note"><strong>Household Social Security at 65:</strong> Your worker benefit ${money(c.youOwn / 12)}/mo + spouse worker benefit ${money(c.spouseOwn / 12)}/mo${c.youExcess ? ` + your spousal excess ${money(c.youExcess / 12)}/mo` : ''}${c.spouseExcess ? ` + spouse spousal excess ${money(c.spouseExcess / 12)}/mo` : ''} = <b>${money(c.monthly)}/mo household total</b>.</div><div class="rsm-note"><strong>Survivor-income watch:</strong> A two-benefit household can become a one-benefit household after the first death. The exact survivor amount depends on claiming ages and survivor rules, so this matrix intentionally does not pretend the two checks simply continue. Treat survivor planning as a separate decision before choosing a couple strategy.</div>`;
}
function renderWatch(s) {
  const roughEarnings = s.you.wages + (s.household === 'couple' ? s.spouse.wages : 0), irmaa = s.household === 'couple' ? 218000 : 109000;
  const items = [];
  items.push(`<div class="rsm-medicare-card"><strong>Social Security can be taxable</strong><p>The benefits shown above are gross. Depending on other income, part of Social Security can be included in federal taxable income. The model does not subtract federal or state tax from the comparison yet.</p></div>`);
  items.push(`<div class="rsm-medicare-card${roughEarnings > irmaa ? ' rsm-alert' : ''}"><strong>IRMAA review</strong><p>For 2026, higher Medicare premiums begin above ${money(irmaa)} of MAGI for ${s.household === 'couple' ? 'married joint' : 'individual'} filers. Your entered Social Security-covered earnings total ${money(roughEarnings)}. Earnings are <b>not</b> the same as MAGI, so this is a review flag, not an IRMAA calculation. Medicare generally uses tax information from two years earlier.</p></div>`);
  items.push(`<div class="rsm-medicare-card"><strong>Current Part B benchmark</strong><p>The standard Medicare Part B premium is $202.90 per month in 2026. Future premiums at your actual enrollment date will be different, so the calculator does not bake today's premium into a long-range retirement forecast.</p></div>`);
  $('watch-results').innerHTML = items.join('');
}
function renderTable(s) {
  $('strategy-body').innerHTML = MAIN.map(age => {
    const p = portfolioForClaim(age, s), be = age === 62 ? 'Baseline' : (cross(62, age, s) ? `About age ${cross(62, age, s)}` : 'After 100');
    return `<tr${age === 65 ? ' class="rsm-focus-row"' : ''}><td>${age}${age === 65 ? '<br><span class="rsm-tag">middle option</span>' : ''}</td><td>${money(ssAnnual(age, s) / 12)}/mo</td><td>${money(ssAnnual(age, s))}</td><td>${be}</td><td>${money(p.atRetire)}</td><td>${money(p.horizon)}</td></tr>`;
  }).join('');
}
function renderPathCards(s) {
  const cards = [...document.querySelectorAll('#path-cards .rsm-path-card')];
  MAIN.forEach((age, i) => {
    const card = cards[i];
    if (!card) return;
    const c = comp(age, age, s), p = portfolioForClaim(age, s);
    card.innerHTML = `<span>Claim at</span><strong>${age}</strong><span class="rsm-path-money">${money(c.monthly)}/mo</span><div class="rsm-path-meta"><span>Annual benefit: ${money(c.total)}</span><span>Portfolio at retirement: ${money(p.atRetire)}</span><span>Portfolio at horizon: ${money(p.horizon)}</span></div>`;
  });
}
function renderIncome(s) {
  $('income-results').innerHTML = MAIN.map(age => {
    const guaranteed = incomeAtRetirement(age, s), gap = Math.max(0, s.spending - guaranteed), coverage = spendingCoverage(age, s);
    const bridge = s.you.retireAge < age ? `<br><small>Social Security has not started at retirement; bridge ${Math.max(0, age - s.you.retireAge).toFixed(0)} year(s) first.</small>` : '';
    return `<div class="rsm-medicare-card"><strong>Claim at ${age}</strong><p>Income available at retirement: <b>${money(guaranteed)}</b><br>Spending target: <b>${money(s.spending)}</b><br>Covered without portfolio withdrawals: <b>${pct(coverage)}</b><br>${gap ? `Initial portfolio need: <b>${money(gap)}/yr</b>` : 'Entered guaranteed income covers the spending target.'}${bridge}</p></div>`;
  }).join('');
}
function renderRoadmap(s) {
  const couple = s.household === 'couple';
  $('roadmap').innerHTML = YEARS.map(age => `<div class="rsm-roadmap-item"><div class="rsm-age">Age ${age}</div><div class="rsm-rail"><span class="rsm-dot"></span></div><div class="rsm-roadmap-copy">Estimated ${couple ? 'household ' : ''}Social Security if ${couple ? 'both start' : 'started'} at ${age}: <strong>${money(ssAnnual(age, s))}/yr</strong>${age === 64 ? ' Begin detailed Medicare and HSA timing review.' : ''}${age === 65 ? ' Medicare eligibility is a separate decision from Social Security claiming.' : ''}</div></div>`).join('');
}
function renderChart(s) {
  const svg = $('crossover-chart'), W = 820, H = 360, p = {l: 70, r: 20, t: 20, b: 42}, end = s.horizon, ages = [];
  for (let a = 62; a <= end; a++) ages.push(a);
  const series = MAIN.map(a => ({a, vals: ages.map(x => x < a ? 0 : cumulative(a, x, s))})), max = Math.max(1, ...series.flatMap(z => z.vals));
  const x = a => p.l + (a - 62) / (end - 62) * (W - p.l - p.r), y = v => H - p.b - v / max * (H - p.t - p.b);
  let out = '';
  for (let i = 0; i <= 4; i++) {const yy = p.t + (H - p.t - p.b) * i / 4; out += `<line x1="${p.l}" y1="${yy}" x2="${W - p.r}" y2="${yy}" stroke="var(--line)"/>`;}
  const colors = ['var(--pine)', 'var(--gold)', 'var(--ink-soft)'], dash = ['', '9 5', '3 4'];
  series.forEach((z, i) => {let d = ''; ages.forEach((a, j) => d += `${j ? 'L' : 'M'}${x(a)} ${y(z.vals[j])} `); out += `<path d="${d}" fill="none" stroke="${colors[i]}" stroke-width="3" stroke-dasharray="${dash[i]}"/>`;});
  [62, 65, 67, 70, 80, end].filter((v, i, a) => v <= end && a.indexOf(v) === i).forEach(a => out += `<text x="${x(a)}" y="${H - 14}" text-anchor="middle" font-size="12" fill="var(--ink-faint)">${a}</text>`);
  svg.innerHTML = out;
}
function renderMedicare(s) {
  const y = s.you.birthYear + 65, m = s.you.birthMonth, c = [];
  c.push(`<div class="rsm-medicare-card"><strong>Age 65</strong><p>Your Medicare eligibility month is approximately <b>${MONTHS[m - 1]} ${y}</b>. Review enrollment timing about 3 months before.</p></div>`);
  if (s.coverage) c.push(`<div class="rsm-medicare-card"><strong>Active employer coverage</strong><p>Whether Part B can be delayed safely depends on the active employer plan and employer size. Confirm with the plan administrator.</p></div>`);
  if (s.hsa) c.push(`<div class="rsm-medicare-card rsm-alert"><strong>HSA warning</strong><p>Coordinate HSA contributions before Medicare enrollment because retroactive Part A can matter.</p></div>`);
  if (!s.creditable) c.push(`<div class="rsm-medicare-card rsm-alert"><strong>Part D</strong><p>Confirm whether existing drug coverage is creditable before delaying Part D.</p></div>`);
  $('medicare-results').innerHTML = c.join('');
}
function renderNotes(s) {
  const couple = s.household === 'couple';
  $('strategy-notes').innerHTML = `<div class="rsm-note"><strong>Social Security:</strong> ${s.you.override > 0 ? 'Using the SSA estimate you entered.' : 'Using an SSA-style estimate from covered earnings, work history, wage indexing and a 35-year benefit calculation.'}</div><div class="rsm-note"><strong>Portfolio:</strong> The model starts with ${money(s.traditional + s.roth + s.taxable)}, adds entered contributions while working, then fills any retirement-spending gap after Social Security, pension and other income.</div>${couple ? `<div class="rsm-note"><strong>Couples:</strong> Household totals use indexed earnings, taxable wage caps, a highest-35 calculation, claim-age adjustments and estimated spousal excess where applicable. Both worker benefits are shown separately from any spousal excess. Survivor benefits are separate.</div>` : ''}<div class="rsm-note"><strong>Official check:</strong> Compare estimates with ${couple ? "each spouse's" : 'your'} Social Security statement before filing.</div>`;
}
function render() {
  const s = state(), couple = s.household === 'couple';
  $('spouse-inputs')?.classList.toggle('rsm-hidden', !couple);
  document.querySelectorAll('.spouse-advanced').forEach(e => e.classList.toggle('rsm-hidden', !couple));

  const th = [...document.querySelectorAll('.rsm-strategy-table th')];
  if (th[1]) th[1].textContent = couple ? 'Household monthly SS' : 'Monthly SS';
  if (th[2]) th[2].textContent = couple ? 'Household annual SS' : 'Annual SS';
  if (th[4]) th[4].textContent = couple ? 'Household portfolio when both retired' : 'Portfolio at retirement';
  if (th[5]) th[5].textContent = couple ? 'Household portfolio at horizon' : 'Portfolio at horizon';
  const ssLabel = $('ss-at-65')?.closest('.rsm-stat')?.querySelector('span');
  if (ssLabel) ssLabel.textContent = couple ? 'Estimated household Social Security at 65' : 'Estimated Social Security at 65';
  const balLabel = $('projected-balance')?.closest('.rsm-stat')?.querySelector('span');
  if (balLabel) balLabel.textContent = couple ? 'Projected household savings when both are retired' : 'Projected savings at retirement';
  const best = $('focus-age')?.parentElement;
  if (best) {
    const sp = best.querySelector('span'), sm = best.querySelector('small');
    if (sp) sp.textContent = couple ? 'Retirement ages' : 'Retire at';
    if (sm) sm.textContent = couple ? 'you / spouse' : 'your input';
  }
  $('focus-age').textContent = couple ? `${Math.round(s.you.retireAge)} / ${Math.round(s.spouse.retireAge)}` : Math.round(s.you.retireAge);
  $('current-balance').textContent = money(s.traditional + s.roth + s.taxable);
  $('projected-balance').textContent = money(baseAtRetirement(s));
  $('ss-at-65').textContent = money(ssAnnual(65, s)) + '/yr';
  $('spending-target').textContent = money(s.spending) + '/yr';
  $('break-even-65').textContent = `about age ${cross(62, 65, s) || '100+'}`;
  $('break-even-67').textContent = `about age ${cross(62, 67, s) || '100+'}`;
  $('break-even-65-67').textContent = `about age ${cross(65, 67, s) || '100+'}`;
  $('horizon-display').textContent = 'Age ' + s.horizon;
  $('summary-copy').textContent = (couple && Math.abs(s.you.retireAge - s.spouse.retireAge) > .01)
    ? `Household view: you retire at ${Math.round(s.you.retireAge)} and your spouse/partner at ${Math.round(s.spouse.retireAge)}. Contributions stop separately for each person, and the portfolio results above account for both retirement dates.`
    : `Using ${s.you.override > 0 ? 'your SSA estimate' : 'an SSA-style estimate'}, compare claiming at 62, 65 and 67 while your savings, contributions, retirement income and spending assumptions flow through the model.`;

  renderMeaning(s); renderGoals(s); renderEarnings(s); renderStress(s); renderCouple(s); renderWatch(s);
  renderTable(s); renderPathCards(s); renderIncome(s); renderRoadmap(s); renderChart(s); renderMedicare(s); renderNotes(s);
}
function previewLinks() {
  const p = new URLSearchParams(location.search), token = p.get('_vercel_share');
  if (!token) return;
  document.querySelectorAll('a[href^="/"]').forEach(a => {const u = new URL(a.getAttribute('href'), location.origin); u.searchParams.set('_vercel_share', token); a.href = u.pathname + u.search + u.hash;});
}
function setupModes() {
  const q = $('rsm-quick-mode'), a = $('rsm-advanced-mode'), h = $('rsm-mode-help');
  if (!q || !a) return;
  const set = (m, scroll = false) => {
    const x = m === 'advanced';
    document.body.classList.toggle('is-advanced', x);
    document.body.classList.toggle('is-quick', !x);
    q.classList.toggle('is-active', !x);
    a.classList.toggle('is-active', x);
    q.setAttribute('aria-pressed', String(!x));
    a.setAttribute('aria-pressed', String(x));
    if (h) h.textContent = x ? 'Advanced mode keeps every planning control visible. Your Quick-mode entries stay in place.' : 'Quick mode keeps the inputs short. Advanced mode adds contributions, pensions, return assumptions, Medicare and exact SSA estimates.';
    if (scroll) $('calculator-title')?.scrollIntoView({behavior: 'smooth', block: 'start'});
  };
  q.addEventListener('click', () => set('quick', true));
  a.addEventListener('click', () => set('advanced', true));
  set('quick');
}
let renderTimer = 0;
function scheduleRender() {clearTimeout(renderTimer); renderTimer = setTimeout(() => requestAnimationFrame(render), 180);}
function immediateRender() {clearTimeout(renderTimer); requestAnimationFrame(render);}
function init() {
  populateMonths();
  setupModes();
  previewLinks();
  document.querySelectorAll('.rsm-page input,.rsm-page select').forEach(e => {
    const live = e.matches('input[type=number],input[type=text],input[type=month]');
    if (live) e.addEventListener('input', scheduleRender);
    e.addEventListener('change', immediateRender);
  });
  $('print-report')?.addEventListener('click', () => window.print());
  $('rsm-reset')?.addEventListener('click', () => location.reload());
  render();
}
if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init, {once: true});
else init();
})();
