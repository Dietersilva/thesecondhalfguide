// Independent reference model for the retirement calculator's Social Security
// and portfolio math, written from SSA methodology directly (not copied from
// retirement-strategy-model.js), so it can catch arithmetic/logic bugs in the
// production code rather than just restating them.
//
// Historical/published tables (AWI, contribution-and-benefit base, bend
// points) are official SSA data, reused as-is since they are facts, not
// calculations -- the independence is in the formulas that consume them.
'use strict';

const CURRENT_YEAR = 2026;
const CURRENT_MONTH = 9;
const TABLE_CAP_YEAR = 2035;
const EARNINGS_LIMIT_STANDARD = 24480; // 2026, below FRA all year
const EARNINGS_LIMIT_FRA_YEAR = 65160; // 2026, the calendar year FRA is reached

const AWI = {1980:12513.46,1981:13773.10,1982:14531.34,1983:15239.24,1984:16135.07,1985:16822.51,1986:17321.82,1987:18426.51,1988:19334.04,1989:20099.55,1990:21027.98,1991:21811.60,1992:22935.42,1993:23132.67,1994:23753.53,1995:24705.66,1996:25913.90,1997:27426.00,1998:28861.44,1999:30469.84,2000:32154.82,2001:32921.92,2002:33252.09,2003:34064.95,2004:35648.55,2005:36952.94,2006:38651.41,2007:40405.48,2008:41334.97,2009:40711.61,2010:41673.83,2011:42979.61,2012:44321.67,2013:44888.16,2014:46481.52,2015:48098.63,2016:48642.15,2017:50321.89,2018:52145.80,2019:54099.99,2020:55628.60,2021:60575.07,2022:63795.13,2023:66621.80,2024:69846.57,2025:72025.07,2026:75246.70,2027:78286.92,2028:81537.43,2029:85047.82,2030:88895.99,2031:92915.31,2032:96989.47,2033:101085.63,2034:105045.59,2035:109064.86};
const CBB = {1980:25900,1981:29700,1982:32400,1983:35700,1984:37800,1985:39600,1986:42000,1987:43800,1988:45000,1989:48000,1990:51300,1991:53400,1992:55500,1993:57600,1994:60600,1995:61200,1996:62700,1997:65400,1998:68400,1999:72600,2000:76200,2001:80400,2002:84900,2003:87000,2004:87900,2005:90000,2006:94200,2007:97500,2008:102000,2009:106800,2010:106800,2011:106800,2012:110100,2013:113700,2014:117000,2015:118500,2016:118500,2017:127200,2018:128400,2019:132900,2020:137700,2021:142800,2022:147000,2023:160200,2024:168600,2025:176100,2026:184500,2027:190200,2028:198900,2029:206700,2030:215400,2031:224700,2032:234900,2033:245400,2034:256200,2035:267000};
const BEND = {2018:[895,5397],2019:[926,5583],2020:[960,5785],2021:[996,6002],2022:[1024,6172],2023:[1115,6721],2024:[1174,7078],2025:[1226,7391],2026:[1286,7749],2027:[1326,7991],2028:[1385,8348],2029:[1441,8686],2030:[1501,9046],2031:[1565,9436],2032:[1636,9863],2033:[1710,10309],2034:[1785,10761],2035:[1861,11215]};

function averageWageIndex(year) {
  if (AWI[year] !== undefined) return AWI[year];
  if (year < 1980) return AWI[1980] / Math.pow(1.045, 1980 - year);
  return AWI[TABLE_CAP_YEAR] * Math.pow(1.038, year - TABLE_CAP_YEAR);
}
function taxableMax(year) {
  if (CBB[year] !== undefined) return CBB[year];
  if (year < 1980) return CBB[1980] / Math.pow(1.05, 1980 - year);
  return CBB[TABLE_CAP_YEAR] * Math.pow(1.04, year - TABLE_CAP_YEAR);
}
function bendPoints(year) {
  if (BEND[year]) return BEND[year];
  if (year < 2018) {
    const ratio = averageWageIndex(year - 2) / averageWageIndex(2016);
    return [Math.round(895 * ratio), Math.round(5397 * ratio)];
  }
  const ratio = averageWageIndex(year - 2) / averageWageIndex(2033);
  return [Math.round(1861 * ratio), Math.round(11215 * ratio)];
}

// Full retirement age, by birth year (SSA table).
function fullRetirementAge(birthYear) {
  if (birthYear <= 1937) return 65;
  if (birthYear >= 1960) return 67;
  if (birthYear <= 1954) return 66;
  return 66 + (birthYear - 1954) * 2 / 12;
}

// Early-claim reduction / delayed-retirement-credit multiplier on a worker's
// own PIA, relative to their own FRA.
function ownBenefitFactor(claimAge, birthYear) {
  const fra = fullRetirementAge(birthYear);
  const monthsFromFra = Math.round((claimAge - fra) * 12);
  if (monthsFromFra === 0) return 1;
  if (monthsFromFra < 0) {
    const early = -monthsFromFra;
    const firstBlock = Math.min(36, early);
    const remainder = Math.max(0, early - 36);
    return 1 - firstBlock * (5 / 9 / 100) - remainder * (5 / 12 / 100);
  }
  const maxDelayMonths = Math.max(0, (70 - fra) * 12);
  const delayMonths = Math.min(monthsFromFra, maxDelayMonths);
  return 1 + delayMonths * (2 / 3 / 100);
}

// Reduction multiplier applied to a spousal *excess* amount when the
// receiving spouse claims before their own FRA. No delayed credit applies to
// spousal amounts, so this is 1 at and after FRA.
function spousalExcessFactor(claimAge, birthYear) {
  const fra = fullRetirementAge(birthYear);
  const monthsEarly = Math.max(0, Math.round((fra - claimAge) * 12));
  if (monthsEarly === 0) return 1;
  const firstBlock = Math.min(36, monthsEarly);
  const remainder = Math.max(0, monthsEarly - 36);
  return 1 - firstBlock * (25 / 36 / 100) - remainder * (5 / 12 / 100);
}

// Builds the person's 35-highest-year wage-indexed earnings history and
// returns AIME (Average Indexed Monthly Earnings), floored per dollar as SSA
// does after averaging.
function computeAIME(person) {
  const age62Year = person.birthYear + 62;
  const indexingYear = age62Year - 2; // the year the person turns 60
  const careerEndYear = Math.min(person.birthYear + person.retireAge, TABLE_CAP_YEAR);
  const careerYears = Math.max(10, Math.min(45, person.yearsWorked));
  const careerStartYear = careerEndYear - careerYears + 1;

  // The back-projection anchor is this year's wage capped at this year's own
  // taxable maximum -- capped BEFORE projecting backward, not after -- so a
  // high earner's past-year estimates scale off the capped figure like the
  // production model does, not off an uncapped current salary.
  const cappedCurrentWages = Math.min(Math.max(0, person.currentWages), taxableMax(CURRENT_YEAR));
  const earningsByYear = [];
  for (let year = careerStartYear; year <= careerEndYear; year++) {
    let nominalEarnings;
    if (year <= CURRENT_YEAR) {
      if (person.avgWages > 0) {
        // A flat career-average figure, expressed in today's dollars, scales
        // with the wage index the same way a single current data point does.
        nominalEarnings = person.avgWages * (averageWageIndex(year) / averageWageIndex(CURRENT_YEAR));
      } else {
        // Assume today's pay was reached gradually: back out a 2%-per-year
        // real earnings curve, then apply wage indexing on top of that.
        const realGrowthAdjusted = cappedCurrentWages / Math.pow(1.02, CURRENT_YEAR - year);
        nominalEarnings = realGrowthAdjusted * (averageWageIndex(year) / averageWageIndex(CURRENT_YEAR));
      }
    } else {
      nominalEarnings = Math.min(person.futureWages || person.currentWages, taxableMax(year));
    }
    nominalEarnings = Math.min(nominalEarnings, taxableMax(year));
    const indexedEarnings = year < indexingYear
      ? nominalEarnings * (averageWageIndex(indexingYear) / averageWageIndex(year))
      : nominalEarnings; // earnings in/after the indexing year count at face value
    earningsByYear.push(indexedEarnings);
  }

  earningsByYear.sort((a, b) => b - a);
  const top35 = earningsByYear.slice(0, 35);
  while (top35.length < 35) top35.push(0);
  const totalIndexedEarnings = top35.reduce((sum, v) => sum + v, 0);
  return Math.floor(totalIndexedEarnings / (35 * 12));
}

// Primary Insurance Amount from AIME via the three-tier bend-point formula,
// rounded down to the nearest dime (SSA's rounding rule).
function computePIA(person) {
  if (person.override > 0) {
    // An entered SSA estimate is itself a benefit AT a stated claim age, so
    // back it out to the age-FRA PIA by undoing that age's own factor.
    return person.override / Math.max(0.1, ownBenefitFactor(person.overrideAge, person.birthYear));
  }
  const aime = computeAIME(person);
  const age62Year = person.birthYear + 62;
  const [bend1, bend2] = bendPoints(age62Year);
  let pia = 0.9 * Math.min(aime, bend1);
  if (aime > bend1) pia += 0.32 * Math.min(aime - bend1, bend2 - bend1);
  if (aime > bend2) pia += 0.15 * (aime - bend2);
  return Math.floor(pia * 10) / 10;
}

function monthlyOwnBenefit(person, claimAge) {
  return computePIA(person) * ownBenefitFactor(claimAge, person.birthYear);
}
function annualGrossOwnBenefit(person, claimAge) {
  return monthlyOwnBenefit(person, claimAge) * 12;
}

// Amount of a year's benefit withheld under the Retirement Earnings Test,
// given the person is under FRA in that year.
function annualWithholding(person, claimAge, standardLimit) {
  const fra = fullRetirementAge(person.birthYear);
  if (claimAge >= fra) return 0;
  const gross = annualGrossOwnBenefit(person, claimAge);
  const isFraYear = fra - claimAge < 1;
  const overage = isFraYear
    ? Math.max(0, person.countableEarnings - EARNINGS_LIMIT_FRA_YEAR) / 3
    : Math.max(0, person.countableEarnings - standardLimit) / 2;
  return Math.min(gross, overage);
}

// The spousal "excess" -- the amount, if positive, that tops up a spouse's
// own reduced worker benefit up to (a reduced) half of the other spouse's
// unreduced PIA. Only the receiving spouse's own early-claim reduction
// applies to the excess; there is no delayed-credit boost on excess amounts.
function spousalExcess(receiver, receiverClaimAge, worker) {
  const raw = Math.max(0, 0.5 * computePIA(worker) - computePIA(receiver));
  return raw * spousalExcessFactor(receiverClaimAge, receiver.birthYear) * 12;
}

// Household Social Security total for a given pair of (hypothetical or
// actual) claim ages. `activeAge`, when given, is "how old is the primary
// person right now" -- used to decide whether each benefit has actually
// started yet and whether the earnings test should still apply.
function household(you, spouse, isCouple, youClaimAge, spouseClaimAge, activeAge, applyEarningsTest, earningsLimit) {
  const ageOffset = birthDecimal(you) - birthDecimal(spouse);
  const spouseCurrentAge = activeAge === null ? Infinity : activeAge + ageOffset;
  const youActive = activeAge === null || activeAge >= youClaimAge;
  const spouseActive = isCouple && (activeAge === null || spouseCurrentAge >= spouseClaimAge);

  const youOwn = youActive
    ? Math.max(0, annualGrossOwnBenefit(you, youClaimAge) - (applyEarningsTest ? annualWithholding(you, youClaimAge, earningsLimit) : 0))
    : 0;
  const spouseOwn = spouseActive
    ? Math.max(0, annualGrossOwnBenefit(spouse, spouseClaimAge) - (applyEarningsTest ? annualWithholding(spouse, spouseClaimAge, earningsLimit) : 0))
    : 0;

  let youExcess = 0, spouseExcess = 0;
  if (youActive && spouseActive) {
    youExcess = spousalExcess(you, youClaimAge, spouse);
    spouseExcess = spousalExcess(spouse, spouseClaimAge, you);
  }
  const total = youOwn + spouseOwn + youExcess + spouseExcess;
  return {youOwn, spouseOwn, youExcess, spouseExcess, total, monthly: total / 12};
}
function birthDecimal(p) {return p.birthYear + (p.birthMonth - 1) / 12;}

function ssAnnualAtSteadyState(you, spouse, isCouple, claimAge) {
  return household(you, spouse, isCouple, claimAge, claimAge, null, false, 0).total;
}

// The household's shared "both retired" age (a couple's retirement dates
// can differ; contributions/withdrawals key off whichever is later, in
// "your" age terms).
function bothRetiredAge(you, spouse, isCouple) {
  if (!isCouple) return you.retireAge;
  const ageOffset = birthDecimal(you) - birthDecimal(spouse);
  return Math.max(you.retireAge, spouse.retireAge - ageOffset);
}
// The household age (in "your" terms) at which Social Security has actually
// started for the whole household, given a hypothetical claim age.
function householdReadyAge(you, spouse, isCouple, claimAge) {
  const ageOffset = isCouple ? birthDecimal(you) - birthDecimal(spouse) : 0;
  return Math.max(you.retireAge, claimAge, claimAge - ageOffset);
}
function currentAge(you) {
  let a = CURRENT_YEAR - you.birthYear;
  if (CURRENT_MONTH < you.birthMonth) a--;
  return a;
}

function incomeOnceStarted(you, spouse, isCouple, claimAge, pension, other) {
  const readyAge = householdReadyAge(you, spouse, isCouple, claimAge);
  return household(you, spouse, isCouple, claimAge, claimAge, readyAge, false, 0).total + pension + other;
}

function contributionsAtAge(you, spouse, isCouple, age, householdInputs) {
  const ageOffset = isCouple ? birthDecimal(you) - birthDecimal(spouse) : 0;
  let c = age < you.retireAge ? householdInputs.contrib + householdInputs.employer : 0;
  if (isCouple && age + ageOffset < spouse.retireAge) c += householdInputs.spouseContrib + householdInputs.spouseEmployer;
  return c;
}

// Projects the portfolio forward from today to retirement, then draws it
// down against any spending gap (spending minus guaranteed income) until the
// planning horizon or depletion.
function projectPortfolio(you, spouse, isCouple, claimAge, householdInputs, startAge, rate) {
  let balance = householdInputs.traditional + householdInputs.roth + householdInputs.taxable;
  const retireAge = bothRetiredAge(you, spouse, isCouple);
  for (let age = startAge; age < retireAge; age++) {
    balance *= 1 + rate;
    balance += contributionsAtAge(you, spouse, isCouple, age, householdInputs);
    if (householdInputs.earlyUse === 'invest') {
      const active = activeAgeForBenefit(you, spouse, isCouple, age, claimAge);
      balance += household(you, spouse, isCouple, claimAge, claimAge, active, true, householdInputs.earningsLimit).total;
    }
  }
  const atRetire = balance;
  for (let age = Math.round(retireAge); age < householdInputs.horizon; age++) {
    balance *= 1 + rate;
    // Whether each spouse's own benefit has actually started is a function
    // of THIS year's age versus their claim age, not a fixed "ready age"
    // snapshot -- a claim age later than retirement must still show $0
    // guaranteed income in the bridge years before it arrives.
    const income = household(you, spouse, isCouple, claimAge, claimAge, age, false, 0).total
      + householdInputs.pension + householdInputs.other;
    balance -= Math.max(0, householdInputs.spending - income);
    if (balance < 0) {balance = 0; break;}
  }
  return {atRetire, horizon: balance};
}
// During the accumulation phase, "how old is the primary person" is just
// `age` itself (this function mirrors the production code's `atAge(age, ...)`
// call, which passes the accumulation-loop age directly as the activeAge).
function activeAgeForBenefit(you, spouse, isCouple, age) {return age;}

module.exports = {
  CURRENT_YEAR, EARNINGS_LIMIT_STANDARD, EARNINGS_LIMIT_FRA_YEAR,
  averageWageIndex, taxableMax, bendPoints, fullRetirementAge,
  ownBenefitFactor, spousalExcessFactor, computeAIME, computePIA,
  monthlyOwnBenefit, annualGrossOwnBenefit, annualWithholding, spousalExcess,
  household, ssAnnualAtSteadyState, bothRetiredAge, householdReadyAge,
  currentAge, incomeOnceStarted, contributionsAtAge, projectPortfolio, birthDecimal,
};
