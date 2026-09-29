'use strict';
// Drives the REAL built calculator page (not a copy of its logic) through
// each scenario in scenarios.js, reads the rendered strategy-table numbers,
// and reconciles them against ssa-reference.js -- an independently written
// implementation of the same SSA methodology. Divergences beyond tolerance
// are reported as failures for manual investigation (see RESULTS.md).
const path = require('path');
const {chromium} = require('playwright-core');
const ref = require('./ssa-reference.js');
const {SCENARIOS, personFields} = require('./scenarios.js');

const BASE_URL = process.env.RSM_TEST_URL || 'http://localhost:8931/retirement-strategy-model.html';
const CHROME_PATH = process.env.RSM_CHROME_PATH || '/opt/pw-browsers/chromium-1194/chrome-linux/chrome';
const MAIN_AGES = [62, 65, 67];
const DOLLAR_TOLERANCE = 3; // absolute dollars; formatting rounds to whole dollars

function parseMoney(text) {
  const m = String(text).replace(/[^0-9.\-]/g, '');
  return m === '' || m === '-' ? NaN : Number(m);
}

async function setScenario(page, scenario) {
  await page.goto(BASE_URL, {waitUntil: 'networkidle'});
  await page.click('#rsm-advanced-mode');

  // Household type
  await page.evaluate((household) => {
    const el = document.querySelector(`input[name="household"][value="${household}"]`);
    el.checked = true;
    el.dispatchEvent(new Event('change', {bubbles: true}));
  }, scenario.household);

  // SS-known toggles (default 'no' unless scenario overrides)
  await page.evaluate((v) => {
    const el = document.querySelector(`input[name="ss-known"][value="${v}"]`);
    el.checked = true;
    el.dispatchEvent(new Event('change', {bubbles: true}));
  }, scenario.ssKnown || 'no');
  if (scenario.household === 'couple') {
    await page.evaluate((v) => {
      const el = document.querySelector(`input[name="spouse-ss-known"][value="${v}"]`);
      el.checked = true;
      el.dispatchEvent(new Event('change', {bubbles: true}));
    }, scenario.spouseSsKnown || 'no');
  }

  // Early-SS-use radio
  await page.evaluate((v) => {
    const el = document.querySelector(`input[name="early-ss-use"][value="${v}"]`);
    el.checked = true;
    el.dispatchEvent(new Event('change', {bubbles: true}));
  }, scenario.earlyUse || 'spend');

  // Plain fields. For a <select>, verify the requested value actually
  // matches one of its <option>s -- silently failing to match leaves the
  // element at its default value, which produced misleading diffs before
  // this check existed (see RESULTS.md history).
  const mismatches = await page.evaluate((fields) => {
    const problems = [];
    for (const [id, value] of Object.entries(fields)) {
      const el = document.getElementById(id);
      if (!el) {problems.push(`missing field #${id}`); continue;}
      el.value = String(value);
      if (el.tagName === 'SELECT' && el.value !== String(value)) {
        problems.push(`#${id}: requested "${value}" is not a valid <option>; left at "${el.value}"`);
      }
      el.dispatchEvent(new Event('input', {bubbles: true}));
      el.dispatchEvent(new Event('change', {bubbles: true}));
    }
    return problems;
  }, scenario.fields);
  if (mismatches.length) {
    throw new Error(`${scenario.id}: invalid field value(s):\n  ${mismatches.join('\n  ')}`);
  }

  await page.waitForTimeout(250);
}

async function readStrategyTable(page) {
  return page.evaluate(() => {
    const cellsOf = tr => [...tr.querySelectorAll('td')].map(td => td.textContent.trim());
    const rows = [...document.querySelectorAll('#strategy-body tr')].map(tr => {
      const cells = cellsOf(tr);
      return {monthly: cells[1], annual: cells[2], atRetire: cells[4], horizon: cells[5]};
    });
    const snapshot = [...document.querySelectorAll('#snapshot-body tr')].map(tr => {
      const cells = cellsOf(tr);
      return {bridge: cells[2], gap: cells[3]};
    });
    const matrix = [...document.querySelectorAll('#couple-body tr')].map(tr => cellsOf(tr).slice(1));
    return {rows, snapshot, matrix};
  });
}

function buildReferenceInputs(scenario) {
  const f = scenario.fields;
  const you = personFields('', f);
  const spouse = scenario.household === 'couple' ? personFields('spouse-', f) : personFields('spouse-', {});
  const isCouple = scenario.household === 'couple';
  const householdInputs = {
    traditional: f['traditional-balance'] || 0,
    roth: f['roth-balance'] || 0,
    taxable: f['taxable-balance'] || 0,
    contrib: f['annual-contrib'] || 0,
    employer: f['employer-contrib'] || 0,
    spouseContrib: f['spouse-contrib'] || 0,
    spouseEmployer: f['spouse-employer-contrib'] || 0,
    earlyUse: scenario.earlyUse || 'spend',
    pension: f['pension-income'] || 0,
    other: f['other-income'] || 0,
    horizon: f.horizon,
    spending: f['annual-spending'],
    earningsLimit: ref.EARNINGS_LIMIT_STANDARD,
  };
  return {you, spouse, isCouple, householdInputs};
}

function computeExpected(scenario) {
  const {you, spouse, isCouple, householdInputs} = buildReferenceInputs(scenario);
  const startAge = ref.currentAge(you);
  const rate = (scenario.fields['return-rate'] || 0) / 100;
  const out = {};
  for (const age of MAIN_AGES) {
    const steady = ref.household(you, spouse, isCouple, age, age, null, false, 0);
    const portfolio = ref.projectPortfolio(you, spouse, isCouple, age, householdInputs, startAge, rate);
    const readyAge = ref.householdReadyAge(you, spouse, isCouple, age);
    const income = ref.household(you, spouse, isCouple, age, age, readyAge, false, 0).total
      + householdInputs.pension + householdInputs.other;
    out[age] = {
      monthly: steady.monthly,
      annual: steady.total,
      atRetire: portfolio.atRetire,
      horizon: portfolio.horizon,
      bridgeCost: ref.bridge(you, spouse, isCouple, age, householdInputs).cost,
      ongoingGap: Math.max(0, householdInputs.spending - income),
    };
    if (isCouple) {
      out.matrix = MAIN_AGES.map(a => MAIN_AGES.map(b => ref.household(you, spouse, true, a, b, null, false, 0).total));
    }
  }
  return out;
}

function compareValue(label, expected, actualText, failures, scenarioId, tolerance = DOLLAR_TOLERANCE) {
  const actual = parseMoney(actualText);
  if (!Number.isFinite(actual)) {
    failures.push(`${scenarioId}: ${label} -- could not parse rendered value "${actualText}"`);
    return;
  }
  const diff = Math.abs(actual - expected);
  const relOk = expected !== 0 && diff / Math.abs(expected) < 0.005;
  if (diff > tolerance && !relOk) {
    failures.push(`${scenarioId}: ${label} -- expected ${expected.toFixed(2)}, rendered ${actual} (diff ${diff.toFixed(2)})`);
  }
}

async function runAll() {
  const browser = await chromium.launch({executablePath: CHROME_PATH});
  const page = await browser.newPage();
  const consoleErrors = [];
  page.on('pageerror', e => consoleErrors.push(e.message));
  page.on('console', m => {if (m.type() === 'error') consoleErrors.push(m.text());});

  const results = [];
  for (const scenario of SCENARIOS) {
    const failures = [];
    await setScenario(page, scenario);
    const table = await readStrategyTable(page);
    const rows = table.rows;
    const expected = computeExpected(scenario);

    MAIN_AGES.forEach((age, i) => {
      const row = rows[i];
      const exp = expected[age];
      if (!row) {failures.push(`${scenario.id}: missing strategy-table row for age ${age}`); return;}
      compareValue(`age ${age} monthly SS`, exp.monthly, row.monthly, failures, scenario.id);
      compareValue(`age ${age} annual SS`, exp.annual, row.annual, failures, scenario.id);
      compareValue(`age ${age} portfolio at retirement`, exp.atRetire, row.atRetire, failures, scenario.id);
      compareValue(`age ${age} portfolio at horizon`, exp.horizon, row.horizon, failures, scenario.id, 10);
      const snap = table.snapshot[i];
      compareValue(`age ${age} snapshot bridge`, exp.bridgeCost, snap.bridge === '\u2014' ? '0' : snap.bridge, failures, scenario.id);
      compareValue(`age ${age} snapshot ongoing gap`, exp.ongoingGap, snap.gap === 'Fully covered' ? '0' : snap.gap, failures, scenario.id);
    });
    if (expected.matrix) {
      expected.matrix.forEach((line, ri) => line.forEach((val, ci) => {
        const text = (table.matrix[ri] || [])[ci] || '';
        const m = text.match(/\$[\d,]+/);
        compareValue(`couple matrix you ${MAIN_AGES[ri]} / spouse ${MAIN_AGES[ci]}`, val, m ? m[0] : text, failures, scenario.id);
      }));
    }

    // Invariant: with earlyUse='spend' (the default), portfolio at retirement
    // must not depend on which claim age is being compared.
    if ((scenario.earlyUse || 'spend') === 'spend') {
      const atRetireVals = rows.map(r => parseMoney(r.atRetire));
      const spread = Math.max(...atRetireVals) - Math.min(...atRetireVals);
      if (spread > DOLLAR_TOLERANCE) {
        failures.push(`${scenario.id}: portfolio-at-retirement varied across claim ages (${rows.map(r => r.atRetire).join(', ')}) despite earlyUse=spend`);
      }
    }
    // Note: under earlyUse='invest', portfolio-at-retirement is NOT
    // guaranteed to be monotonic in claim age -- fewer years of reinvested
    // benefit at a higher post-reduction rate (claiming closer to
    // retirement) can outweigh more years at a lower rate (claiming early).
    // The reference model's atRetire values (checked per-age above) are the
    // real cross-check here, not a monotonicity assumption.

    results.push({id: scenario.id, description: scenario.description, pass: failures.length === 0, failures, rows, expected});
  }

  await browser.close();
  return {results, consoleErrors};
}

runAll().then(({results, consoleErrors}) => {
  let passCount = 0;
  const lines = [];
  for (const r of results) {
    if (r.pass) passCount++;
    lines.push(`${r.pass ? 'PASS' : 'FAIL'}  ${r.id} -- ${r.description}`);
    if (!r.pass) r.failures.forEach(f => lines.push(`       ${f}`));
  }
  lines.push('');
  lines.push(`${passCount}/${results.length} scenarios passed.`);
  if (consoleErrors.length) {
    lines.push('');
    lines.push('Browser console/page errors observed during the run:');
    consoleErrors.forEach(e => lines.push(`  - ${e}`));
  }
  console.log(lines.join('\n'));

  const fs = require('fs');
  fs.writeFileSync(path.join(__dirname, 'last-run.json'), JSON.stringify(results, null, 2));
  process.exit(results.every(r => r.pass) ? 0 : 1);
}).catch(err => {
  console.error('Regression runner crashed:', err);
  process.exit(2);
});
