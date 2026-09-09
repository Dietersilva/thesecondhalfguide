(() => {
  'use strict';

  const TODAY = { year: 2026, month: 9 };
  const AGES = [62, 63, 64, 65, 66, 67];
  const MONTHS = ['January','February','March','April','May','June','July','August','September','October','November','December'];
  const $ = (id) => document.getElementById(id);
  const money0 = (n) => new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD', maximumFractionDigits: 0 }).format(Number.isFinite(n) ? n : 0);
  const money1 = (n) => new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD', maximumFractionDigits: 0 }).format(Number.isFinite(n) ? n : 0);
  const pct = (n) => `${(Number.isFinite(n) ? n : 0).toFixed(1)}%`;

  const defaults = {
    household: 'couple', birthMonth: 11, birthYear: 1964, retireAge: 65, wages: 50000,
    ssKnown: 2600, ssKnownAge: 62, spouseBirthMonth: 7, spouseBirthYear: 1964,
    spouseRetireAge: 65, spouseWages: 135000, spouseSsKnown: 3200, spouseSsKnownAge: 65,
    portfolio: 800000, annualContrib: 71500, otherIncome: 10000, returnRate: 5,
    annualSpending: 90000, horizon: 85, earningsLimit: 24480, countableEarnings: 50000,
    partBStart: '', hsa: false, activeEmployerCoverage: true, creditableDrug: true
  };

  function clamp(n, min, max) {
    n = Number(n);
    if (!Number.isFinite(n)) return min;
    return Math.min(max, Math.max(min, n));
  }

  function numberValue(id, min = 0, max = Number.MAX_SAFE_INTEGER) {
    const el = $(id);
    return clamp(el ? el.value : 0, min, max);
  }

  function selectedHousehold() {
    const el = document.querySelector('input[name="household"]:checked');
    return el ? el.value : 'single';
  }

  function populateMonths() {
    ['birth-month', 'spouse-birth-month'].forEach((id) => {
      const el = $(id);
      if (!el || el.options.length) return;
      MONTHS.forEach((m, i) => {
        const opt = document.createElement('option');
        opt.value = String(i + 1);
        opt.textContent = m;
        el.appendChild(opt);
      });
    });
  }

  function fullRetirementAgeMonths(birthYear) {
    const y = Number(birthYear);
    if (y <= 1937) return 65 * 12;
    if (y === 1938) return 65 * 12 + 2;
    if (y === 1939) return 65 * 12 + 4;
    if (y === 1940) return 65 * 12 + 6;
    if (y === 1941) return 65 * 12 + 8;
    if (y === 1942) return 65 * 12 + 10;
    if (y <= 1954) return 66 * 12;
    if (y === 1955) return 66 * 12 + 2;
    if (y === 1956) return 66 * 12 + 4;
    if (y === 1957) return 66 * 12 + 6;
    if (y === 1958) return 66 * 12 + 8;
    if (y === 1959) return 66 * 12 + 10;
    return 67 * 12;
  }

  function claimFactor(age, birthYear) {
    const fra = fullRetirementAgeMonths(birthYear);
    const claim = Math.round(Number(age) * 12);
    const diff = claim - fra;
    if (diff === 0) return 1;
    if (diff < 0) {
      const early = -diff;
      const first36 = Math.min(36, early);
      const later = Math.max(0, early - 36);
      return Math.max(0, 1 - first36 * (5 / 9 / 100) - later * (5 / 12 / 100));
    }
    const delayedMonths = Math.min(diff, Math.max(0, 70 * 12 - fra));
    return 1 + delayedMonths * (2 / 3 / 100);
  }

  function piaFromKnown(amount, knownAge, birthYear) {
    const factor = claimFactor(knownAge, birthYear);
    return factor > 0 ? amount / factor : amount;
  }

  function personFromInputs(prefix = '') {
    const isSpouse = prefix === 'spouse-';
    return {
      birthMonth: numberValue(`${prefix}birth-month`, 1, 12),
      birthYear: numberValue(`${prefix}birth-year`, 1930, 1970),
      retireAge: numberValue(`${prefix}retire-age`, 62, 75),
      wages: numberValue(isSpouse ? 'spouse-wages' : 'wages', 0, 10000000),
      known: numberValue(isSpouse ? 'spouse-ss-known' : 'ss-known', 0, 100000),
      knownAge: numberValue(isSpouse ? 'spouse-ss-known-age' : 'ss-known-age', 62, 70)
    };
  }

  function monthlyAt(age, person) {
    const pia = piaFromKnown(person.known, person.knownAge, person.birthYear);
    return pia * claimFactor(age, person.birthYear);
  }

  function currentAge(person) {
    let age = TODAY.year - person.birthYear;
    if (TODAY.month < person.birthMonth) age -= 1;
    return clamp(age, 0, 120);
  }

  function annualSsAt(age, state, applyTest = false) {
    const primary = monthlyAt(age, state.you) * 12;
    const spouse = state.household === 'couple' ? monthlyAt(age, state.spouse) * 12 : 0;
    const primaryAfter = applyTest ? Math.max(0, primary - earningsWithheld(age, monthlyAt(age, state.you), state)) : primary;
    return { primary, spouse, total: primaryAfter + spouse, primaryAfter };
  }

  function earningsWithheld(age, monthly, state) {
    const fra = fullRetirementAgeMonths(state.you.birthYear) / 12;
    if (age >= fra) return 0;
    const excess = Math.max(0, state.countableEarnings - state.earningsLimit);
    return Math.min(monthly * 12, excess / 2);
  }

  function effectiveMonthlyAfterFra(claimAge, person, totalWithheldMonths) {
    const fra = fullRetirementAgeMonths(person.birthYear) / 12;
    if (claimAge >= fra || totalWithheldMonths <= 0) return monthlyAt(claimAge, person);
    const originalEarlyMonths = Math.max(0, Math.round((fra - claimAge) * 12));
    const remaining = Math.max(0, originalEarlyMonths - totalWithheldMonths);
    const adjustedClaimAge = fra - remaining / 12;
    const pia = piaFromKnown(person.known, person.knownAge, person.birthYear);
    return pia * claimFactor(adjustedClaimAge, person.birthYear);
  }

  function cumulativeBenefits(claimAge, throughAge, state) {
    if (throughAge < claimAge) return 0;
    const fra = fullRetirementAgeMonths(state.you.birthYear) / 12;
    let primaryMonthly = monthlyAt(claimAge, state.you);
    const spouseMonthly = state.household === 'couple' ? monthlyAt(claimAge, state.spouse) : 0;
    let withheldMonths = 0;
    let adjusted = false;
    let total = 0;

    for (let age = claimAge; age <= throughAge; age += 1) {
      let primaryAnnual = primaryMonthly * 12;
      const spouseAnnual = spouseMonthly * 12;
      const stillWorking = age < state.you.retireAge;
      if (stillWorking && age < fra) {
        const withheld = earningsWithheld(age, primaryMonthly, state);
        primaryAnnual = Math.max(0, primaryAnnual - withheld);
        withheldMonths += primaryMonthly > 0 ? withheld / primaryMonthly : 0;
      }
      if (!adjusted && age >= Math.ceil(fra) && withheldMonths > 0) {
        primaryMonthly = effectiveMonthlyAfterFra(claimAge, state.you, withheldMonths);
        primaryAnnual = primaryMonthly * 12;
        adjusted = true;
      }
      total += primaryAnnual + spouseAnnual;
    }
    return total;
  }

  function crossoverAge(baseAge, laterAge, state) {
    if (laterAge <= baseAge) return null;
    for (let age = laterAge; age <= 100; age += 1) {
      if (cumulativeBenefits(laterAge, age, state) >= cumulativeBenefits(baseAge, age, state)) return age;
    }
    return null;
  }

  function projectedBalance(state) {
    let balance = state.portfolio;
    const startAge = currentAge(state.you);
    const years = Math.max(0, Math.round(state.you.retireAge - startAge));
    const r = state.returnRate / 100;
    for (let i = 0; i < years; i += 1) balance = balance * (1 + r) + state.annualContrib;
    return balance;
  }

  function stateFromForm() {
    const household = selectedHousehold();
    return {
      household,
      you: personFromInputs(''),
      spouse: personFromInputs('spouse-'),
      portfolio: numberValue('portfolio', 0, 100000000),
      annualContrib: numberValue('annual-contrib', 0, 1000000),
      otherIncome: numberValue('other-income', 0, 10000000),
      returnRate: numberValue('return-rate', 0, 12),
      annualSpending: numberValue('annual-spending', 0, 10000000),
      horizon: numberValue('horizon', 70, 110),
      earningsLimit: numberValue('earnings-limit', 0, 1000000),
      countableEarnings: numberValue('countable-earnings', 0, 10000000),
      partBStart: $('part-b-start').value,
      hsa: $('hsa').checked,
      activeEmployerCoverage: $('active-employer-coverage').checked,
      creditableDrug: $('creditable-drug').checked
    };
  }

  function setValue(id, value) {
    const el = $(id);
    if (!el) return;
    if (el.type === 'checkbox') el.checked = Boolean(value);
    else el.value = String(value);
  }

  function resetForm() {
    const radio = document.querySelector(`input[name="household"][value="${defaults.household}"]`);
    if (radio) radio.checked = true;
    setValue('birth-month', defaults.birthMonth);
    setValue('birth-year', defaults.birthYear);
    setValue('retire-age', defaults.retireAge);
    setValue('wages', defaults.wages);
    setValue('ss-known', defaults.ssKnown);
    setValue('ss-known-age', defaults.ssKnownAge);
    setValue('spouse-birth-month', defaults.spouseBirthMonth);
    setValue('spouse-birth-year', defaults.spouseBirthYear);
    setValue('spouse-retire-age', defaults.spouseRetireAge);
    setValue('spouse-wages', defaults.spouseWages);
    setValue('spouse-ss-known', defaults.spouseSsKnown);
    setValue('spouse-ss-known-age', defaults.spouseSsKnownAge);
    setValue('portfolio', defaults.portfolio);
    setValue('annual-contrib', defaults.annualContrib);
    setValue('other-income', defaults.otherIncome);
    setValue('return-rate', defaults.returnRate);
    setValue('annual-spending', defaults.annualSpending);
    setValue('horizon', defaults.horizon);
    setValue('earnings-limit', defaults.earningsLimit);
    setValue('countable-earnings', defaults.countableEarnings);
    setValue('part-b-start', defaults.partBStart);
    setValue('hsa', defaults.hsa);
    setValue('active-employer-coverage', defaults.activeEmployerCoverage);
    setValue('creditable-drug', defaults.creditableDrug);
    render();
  }

  function householdLabel(state) {
    return state.household === 'couple' ? 'combined household' : 'individual';
  }

  function chooseFocusAge(state) {
    return clamp(Math.round(state.you.retireAge), 62, 67);
  }

  function renderSummary(state) {
    const focus = chooseFocusAge(state);
    const focusAnnual = annualSsAt(focus, state, false).total;
    const age65 = annualSsAt(65, state, false).total;
    const balance = projectedBalance(state);
    const be65 = crossoverAge(62, 65, state);
    const gap = Math.max(0, state.annualSpending - age65 - state.otherIncome);
    $('focus-age').textContent = String(focus);
    $('projected-balance').textContent = money0(balance);
    $('ss-at-65').textContent = `${money0(age65)}/yr`;
    $('break-even-65').textContent = be65 ? `about age ${be65}` : 'after 100';
    $('spending-gap').textContent = money0(gap);
    $('summary-title').textContent = state.household === 'couple' ? 'Your household strategy at a glance' : 'Your retirement strategy at a glance';
    $('summary-copy').textContent = `At a claim age of ${focus}, this model estimates ${money0(focusAnnual)} a year of ${householdLabel(state)} Social Security before taxes. The balance projection assumes ${pct(state.returnRate)} annual growth.`;
  }

  function renderTable(state) {
    const focus = chooseFocusAge(state);
    const rows = AGES.map((age) => {
      const monthlyPrimary = monthlyAt(age, state.you);
      const monthlySpouse = state.household === 'couple' ? monthlyAt(age, state.spouse) : 0;
      const monthly = monthlyPrimary + monthlySpouse;
      const annual = monthly * 12;
      const after = Math.max(0, monthlyPrimary * 12 - earningsWithheld(age, monthlyPrimary, state));
      const cross = age === 62 ? 'Baseline' : (crossoverAge(62, age, state) ? `About age ${crossoverAge(62, age, state)}` : 'After 100');
      const cumulative = cumulativeBenefits(age, state.horizon, state);
      return `<tr class="${age === focus ? 'rsm-focus-row' : ''}">
        <td>${age}${age === focus ? '<br><span class="rsm-tag">Retirement-age focus</span>' : ''}</td>
        <td>${money0(monthly)}/mo</td>
        <td>${money0(annual)}</td>
        <td>${money0(after)}${state.countableEarnings > state.earningsLimit && age < fullRetirementAgeMonths(state.you.birthYear)/12 ? '<br><small>your benefit only</small>' : ''}</td>
        <td>${cross}</td>
        <td>${money0(cumulative)} by ${state.horizon}</td>
      </tr>`;
    }).join('');
    $('strategy-body').innerHTML = rows;
  }

  function niceMax(n) {
    if (n <= 0) return 1;
    const exp = Math.pow(10, Math.floor(Math.log10(n)));
    return Math.ceil(n / exp) * exp;
  }

  function renderChart(state) {
    const svg = $('crossover-chart');
    const W = 820, H = 360, p = { l: 72, r: 22, t: 22, b: 44 };
    const endAge = Math.max(80, Math.min(100, state.horizon));
    const ages = [];
    for (let a = 62; a <= endAge; a += 1) ages.push(a);
    const defs = [
      { age: 62, cls: 'var(--pine)', dash: '' },
      { age: 65, cls: 'var(--gold)', dash: '9 5' },
      { age: 67, cls: 'var(--ink-soft)', dash: '3 4' }
    ];
    const series = defs.map((d) => ({ ...d, vals: ages.map((a) => a < d.age ? 0 : cumulativeBenefits(d.age, a, state)) }));
    const maxVal = niceMax(Math.max(...series.flatMap((s) => s.vals), 1));
    const x = (a) => p.l + ((a - 62) / (endAge - 62)) * (W - p.l - p.r);
    const y = (v) => H - p.b - (v / maxVal) * (H - p.t - p.b);
    let out = '';
    for (let i = 0; i <= 4; i += 1) {
      const v = maxVal * i / 4;
      const yy = y(v);
      out += `<line x1="${p.l}" y1="${yy}" x2="${W-p.r}" y2="${yy}" stroke="var(--line)"/><text x="${p.l-10}" y="${yy+4}" text-anchor="end" font-size="12" fill="var(--ink-faint)">${Math.round(v/1000)}k</text>`;
    }
    const labels = Array.from(new Set([62, 65, 70, 75, 80, 85, 90, 95, endAge].filter((a) => a >= 62 && a <= endAge))).sort((a,b) => a-b);
    labels.forEach((a) => { out += `<text x="${x(a)}" y="${H-16}" text-anchor="middle" font-size="12" fill="var(--ink-faint)">${a}</text>`; });
    series.forEach((s) => {
      let d = '';
      ages.forEach((a, i) => { d += `${i ? 'L' : 'M'}${x(a).toFixed(1)} ${y(s.vals[i]).toFixed(1)} `; });
      out += `<path d="${d}" fill="none" stroke="${s.cls}" stroke-width="3" stroke-dasharray="${s.dash}" vector-effect="non-scaling-stroke"/>`;
    });
    const be65 = crossoverAge(62, 65, state);
    if (be65 && be65 <= endAge) {
      const cy = y(cumulativeBenefits(62, be65, state));
      out += `<circle cx="${x(be65)}" cy="${cy}" r="5" fill="var(--ink)"/><text x="${Math.min(W-170,x(be65)+10)}" y="${cy-10}" font-size="12" fill="var(--ink-soft)">62 vs 65: ~${be65}</text>`;
    }
    out += `<text x="${W/2}" y="${H-2}" text-anchor="middle" font-size="12" fill="var(--ink-faint)">Age</text>`;
    svg.innerHTML = out;
  }

  function renderRoadmap(state) {
    const fraAge = fullRetirementAgeMonths(state.you.birthYear) / 12;
    const retire = Math.round(state.you.retireAge);
    const rows = AGES.map((age) => {
      const ss = annualSsAt(age, state, false).total;
      const parts = [];
      if (age < retire) parts.push(`<strong>Work and save.</strong> If cash flow allows, continue retirement contributions. Claiming now would produce about ${money0(ss)}/yr before any earnings-test withholding.`);
      if (age === retire) parts.push(`<strong>Retirement target.</strong> This is the natural decision point in your inputs. Claiming at ${age} would produce about ${money0(ss)}/yr before taxes.`);
      if (age > retire) parts.push(`<strong>Delay option.</strong> Waiting to ${age} increases estimated annual Social Security to about ${money0(ss)}, but gives up earlier checks.`);
      if (age === 63) parts.push('For workers ages 60–63, recheck the current year’s enhanced 401(k) catch-up limit before setting payroll elections.');
      if (age === 64) parts.push('The enhanced age-60–63 catch-up window has ended. Start detailed Medicare and employer-coverage planning about a year before 65.');
      if (age === 65) parts.push('Medicare eligibility becomes a separate enrollment decision. Social Security claiming and Medicare enrollment do not have to start together.');
      if (Math.abs(age - fraAge) < 0.6) parts.push(`<strong>Full Retirement Age is about ${fraAge % 1 ? fraAge.toFixed(2) : fraAge}.</strong> The retirement earnings test no longer applies after FRA.`);
      return `<div class="rsm-roadmap-item"><div class="rsm-age">Age ${age}</div><div class="rsm-rail"><span class="rsm-dot"></span></div><div class="rsm-roadmap-copy">${parts.join(' ')}</div></div>`;
    }).join('');
    $('roadmap').innerHTML = rows;
  }

  function formatMonthDate(year, month, end = false) {
    const d = end ? new Date(Date.UTC(year, month, 0)) : new Date(Date.UTC(year, month - 1, 1));
    return d.toLocaleDateString('en-US', { timeZone: 'UTC', month: 'long', day: 'numeric', year: 'numeric' });
  }

  function shiftYearMonth(year, month, delta) {
    const d = new Date(Date.UTC(year, month - 1 + delta, 1));
    return { year: d.getUTCFullYear(), month: d.getUTCMonth() + 1 };
  }

  function renderMedicare(state) {
    const y65 = state.you.birthYear + 65;
    const m65 = state.you.birthMonth;
    const iepStart = shiftYearMonth(y65, m65, -3);
    const iepEnd = shiftYearMonth(y65, m65, 3);
    const irmaaYear = y65 - 2;
    const cards = [];
    cards.push(`<div class="rsm-medicare-card"><strong>Initial Enrollment Period</strong><p>For a ${MONTHS[m65-1]} birthday month, your 7-month Medicare Initial Enrollment Period runs approximately <b>${formatMonthDate(iepStart.year, iepStart.month)}</b> through <b>${formatMonthDate(iepEnd.year, iepEnd.month, true)}</b>. Exact timing can differ for a birthday on the first of a month.</p></div>`);
    cards.push(`<div class="rsm-medicare-card"><strong>IRMAA lookback</strong><p>Medicare generally looks back two tax years for income-related Part B and Part D surcharges. Your age-65 premium year ${y65} may initially look to your <b>${irmaaYear}</b> tax return. Retirement can qualify as a life-changing event for an IRMAA reconsideration.</p></div>`);
    if (state.activeEmployerCoverage) {
      cards.push(`<div class="rsm-medicare-card"><strong>Active employer coverage</strong><p>You may be able to delay Part B without a late penalty while covered by qualifying active-employer group coverage. The standard employment-based Part B Special Enrollment Period generally ends 8 months after employment or group coverage ends, whichever happens first.</p></div>`);
    } else {
      cards.push(`<div class="rsm-medicare-card rsm-alert"><strong>No active-employer coverage entered</strong><p>Do not assume COBRA or retiree coverage lets you postpone Part B. Plan around the Initial Enrollment Period unless you confirm another Special Enrollment Period applies.</p></div>`);
    }
    if (state.partBStart) {
      const [py, pm] = state.partBStart.split('-').map(Number);
      const medigapEnd = shiftYearMonth(py, pm, 5);
      cards.push(`<div class="rsm-medicare-card"><strong>Your Medigap window</strong><p>With Part B starting ${MONTHS[pm-1]} ${py}, the federal 6-month Medigap open enrollment window runs from <b>${formatMonthDate(py, pm)}</b> through <b>${formatMonthDate(medigapEnd.year, medigapEnd.month, true)}</b>.</p></div>`);
    } else {
      cards.push(`<div class="rsm-medicare-card"><strong>Medigap 6-month window</strong><p>Your one-time federal Medigap open enrollment begins the first month you are 65 or older and enrolled in Part B. Enter a Part B start month under Advanced assumptions to calculate the dates.</p></div>`);
    }
    if (state.hsa) {
      cards.push(`<div class="rsm-medicare-card rsm-alert"><strong>HSA timing warning</strong><p>Medicare Part A can be retroactive for up to 6 months when you enroll after 65, but not before the month you turned 65. Coordinate the final HSA contribution carefully and consider stopping HSA contributions at least 6 months before a delayed Medicare or Social Security enrollment after 65.</p></div>`);
    }
    if (state.creditableDrug) {
      cards.push(`<div class="rsm-medicare-card"><strong>Prescription coverage</strong><p>You entered creditable employer drug coverage. That can allow Part D to be delayed without the normal late-enrollment penalty while the creditable coverage continues. Keep the annual creditable-coverage notice.</p></div>`);
    } else {
      cards.push(`<div class="rsm-medicare-card rsm-alert"><strong>Part D gap warning</strong><p>A gap of 63 days or more without Medicare drug coverage or other creditable prescription coverage after you become eligible can trigger a Part D late-enrollment penalty.</p></div>`);
    }
    $('medicare-results').innerHTML = cards.join('');
  }

  function renderNotes(state) {
    const notes = [];
    const currentIncome = state.you.wages + (state.household === 'couple' ? state.spouse.wages : 0) + state.otherIncome;
    const focus = chooseFocusAge(state);
    const earlyWithheld = earningsWithheld(62, monthlyAt(62, state.you), state);
    if (state.countableEarnings > state.earningsLimit) notes.push(`<div class="rsm-note"><strong>Early claiming while working:</strong> using the 2026 earnings-test assumption entered, a claim at 62 could have about ${money0(earlyWithheld)} of your first-year benefit withheld. Your spouse’s wages do not count against your earnings test.</div>`);
    if (currentIncome > 100000) notes.push(`<div class="rsm-note"><strong>High-income working years:</strong> with about ${money0(currentIncome)} of current household income entered, early Social Security may be less useful for cash-flow purposes and may be taxable. That is one reason the model highlights your retirement-age claim point rather than automatically favoring 62.</div>`);
    notes.push(`<div class="rsm-note"><strong>Portfolio effect:</strong> with ${money0(state.portfolio)} already saved, ${money0(state.annualContrib)} of annual contributions and a ${pct(state.returnRate)} assumption, the projected balance at age ${state.you.retireAge} is about ${money0(projectedBalance(state))}. This is a straight-line illustration, not a guarantee.</div>`);
    if (state.household === 'couple') notes.push(`<div class="rsm-note"><strong>Couple strategy:</strong> the main table intentionally compares both spouses claiming at the same age. A full household optimization should also compare staggered claim dates and survivor income, especially when one spouse has the larger benefit.</div>`);
    notes.push(`<div class="rsm-note"><strong>Current model focus:</strong> age ${focus} matches the retirement age you entered. That is a comparison point, not a directive. Change retirement age, spending, savings or benefit estimates and the report recalculates.</div>`);
    $('strategy-notes').innerHTML = notes.join('');
  }

  function updateVisibility(state) {
    $('spouse-inputs').classList.toggle('rsm-hidden', state.household !== 'couple');
  }

  function render() {
    const state = stateFromForm();
    updateVisibility(state);
    renderSummary(state);
    renderTable(state);
    renderChart(state);
    renderRoadmap(state);
    renderMedicare(state);
    renderNotes(state);
  }

  function init() {
    populateMonths();
    setValue('birth-month', defaults.birthMonth);
    setValue('spouse-birth-month', defaults.spouseBirthMonth);
    document.querySelectorAll('.rsm-page input, .rsm-page select').forEach((el) => {
      el.addEventListener('input', render);
      el.addEventListener('change', render);
    });
    $('rsm-reset').addEventListener('click', resetForm);
    $('print-report').addEventListener('click', () => window.print());
    render();
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init, { once: true });
  else init();
})();
