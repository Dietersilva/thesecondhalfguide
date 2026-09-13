from pathlib import Path
import re, subprocess

old = subprocess.check_output(['git','show','origin/feature/retirement-strategy-model:_src/retirement-strategy-model.js'], text=True)

def const(name):
    m=re.search(rf'const {name}=\{{.*?\}};', old, re.S)
    if not m: raise SystemExit(f'missing {name}')
    return m.group(0)
AWI,CBB,BEND=const('AWI'),const('CBB'),const('BEND')

core=f'''{AWI}\n{CBB}\n{BEND}\nconst AWI_CACHE=new Map();
function awi(y){{if(AWI_CACHE.has(y))return AWI_CACHE.get(y);let v;if(AWI[y])v=AWI[y];else if(y<1980)v=AWI[1980]/Math.pow(1.045,1980-y);else v=AWI[2035]*Math.pow(1.038,y-2035);AWI_CACHE.set(y,v);return v;}}
function cbb(y){{if(CBB[y])return CBB[y];if(y<1980)return CBB[1980]/Math.pow(1.05,1980-y);return CBB[2035]*Math.pow(1.04,y-2035);}}
function bendPoints(y){{if(BEND[y])return BEND[y];if(y<2018){{const f=awi(y-2)/awi(2016);return [Math.round(895*f),Math.round(5397*f)];}}const f=awi(y-2)/awi(2033);return [Math.round(1861*f),Math.round(11215*f)];}}
function fra(y){{if(y>=1960)return 67;if(y<=1937)return 65;if(y<=1954)return 66;return 66+(y-1954)*2/12;}}
function factor(age,y){{const f=fra(y),m=Math.round((age-f)*12);if(m===0)return 1;if(m<0){{const e=-m;return 1-Math.min(36,e)*(5/9/100)-Math.max(0,e-36)*(5/12/100);}}return 1+Math.min(m,Math.max(0,(70-f)*12))*(2/3/100);}}
function spouseFactor(age,y){{const m=Math.max(0,Math.round((fra(y)-age)*12));if(!m)return 1;return 1-Math.min(36,m)*(25/36/100)-Math.max(0,m-36)*(5/12/100);}}
'''

pia='''function quickPiaCalc(p,claimAge){
  if(p.override>0)return p.override/Math.max(.1,factor(p.overrideAge,p.birthYear));
  const eligibility=p.birthYear+62,indexYear=eligibility-2,currentYear=TODAY.year;
  const latest=Math.min(Math.max(0,p.wages),cbb(currentYear)),years=Math.max(10,Math.min(45,p.years));
  const start=currentYear-years+1,claimYear=p.birthYear+claimAge,retireYear=p.birthYear+p.retireAge;
  const end=Math.max(currentYear,Math.min(claimYear,retireYear,2035)),vals=[];
  for(let y=start;y<=end;y++){
    let nominal=y<=currentYear?latest*(awi(y)/awi(currentYear))/Math.pow(1.02,currentYear-y):Math.min(p.futureWages||p.wages,cbb(y));
    nominal=Math.min(nominal,cbb(y));vals.push(nominal*(y<indexYear?awi(indexYear)/awi(y):1));
  }
  vals.sort((a,b)=>b-a);const top=vals.slice(0,35);while(top.length<35)top.push(0);
  const aime=Math.floor(top.reduce((a,b)=>a+b,0)/420),[b1,b2]=bendPoints(eligibility);
  let v=.9*Math.min(aime,b1);if(aime>b1)v+=.32*Math.min(aime-b1,b2-b1);if(aime>b2)v+=.15*(aime-b2);
  return Math.floor(v*10)/10;
}
const PIA_CACHE=new Map();
function quickPia(p,claimAge){const k=[p.birthYear,p.retireAge,p.wages,p.futureWages,p.years,p.override,p.overrideAge,claimAge].join('|');if(PIA_CACHE.has(k))return PIA_CACHE.get(k);const v=quickPiaCalc(p,claimAge);PIA_CACHE.set(k,v);return v;}
function monthly(age,p){return quickPia(p,age)*factor(age,p.birthYear);}
function grossAnnual(claimAge,p){return monthly(claimAge,p)*12;}
function withheldAnnual(claimAge,p,limit){const f=fra(p.birthYear);if(claimAge>=f)return 0;const gross=grossAnnual(claimAge,p);if(Math.floor(claimAge)===Math.floor(f))return Math.min(gross,Math.max(0,p.countable-65160)/3);return Math.min(gross,Math.max(0,p.countable-limit)/2);}
function personAnnual(claimAge,p,applyTest,limit){return Math.max(0,grossAnnual(claimAge,p)-(applyTest?withheldAnnual(claimAge,p,limit):0));}
function excessSpouseMonthly(recipientAge,recipient,workerAge,worker){const excess=Math.max(0,.5*quickPia(worker,workerAge)-quickPia(recipient,recipientAge));return excess*spouseFactor(recipientAge,recipient.birthYear);}
function householdComponents(a,b,s,primaryAge=null,applyTest=false){
  const offset=(s.you.birthYear+(s.you.birthMonth-1)/12)-(s.spouse.birthYear+(s.spouse.birthMonth-1)/12);
  const spouseAge=primaryAge===null?Infinity:primaryAge+offset,youStarted=primaryAge===null||primaryAge>=a,spouseStarted=s.household==='couple'&&(primaryAge===null||spouseAge>=b);
  const youOwn=youStarted?personAnnual(a,s.you,applyTest,s.limit):0,spouseOwn=spouseStarted?personAnnual(b,s.spouse,applyTest,s.limit):0;
  let youExcess=0,spouseExcess=0;if(youStarted&&spouseStarted){youExcess=excessSpouseMonthly(a,s.you,b,s.spouse)*12;spouseExcess=excessSpouseMonthly(b,s.spouse,a,s.you)*12;}
  const total=youOwn+spouseOwn+youExcess+spouseExcess;return {youOwn,spouseOwn,youExcess,spouseExcess,total,monthly:total/12};
}
function ssAnnual(claimAge,s,applyTest=false){return householdComponents(claimAge,claimAge,s,null,applyTest).total;}
function ssAnnualMixed(a,b,s,applyTest=false){return householdComponents(a,b,s,null,applyTest).total;}
'''

time='''function contributions(s){return s.contrib+s.employer+(s.household==='couple'?s.spouseContrib+s.spouseEmployer:0);}
function baseAtRetirement(s,rate=s.returnRate){let bal=s.traditional+s.roth+s.taxable,years=Math.max(0,Math.round(s.you.retireAge-ageNow(s.you)));for(let i=0;i<years;i++){bal*=1+rate;bal+=contributions(s);}return bal;}
function annualAtPrimaryAge(age,a,b,s,applyTest=false){return householdComponents(a,b,s,age,applyTest).total;}
function portfolioForClaim(claimAge,s,rate=s.returnRate){let bal=s.traditional+s.roth+s.taxable;const start=ageNow(s.you),retire=s.you.retireAge;for(let age=start;age<retire;age++){bal*=1+rate;bal+=contributions(s);if(s.earlyUse==='invest')bal+=annualAtPrimaryAge(age,claimAge,claimAge,s,true);}const atRetire=bal;for(let age=Math.round(retire);age<s.horizon;age++){bal*=1+rate;const income=annualAtPrimaryAge(age,claimAge,claimAge,s,false)+s.pension+s.other;bal-=Math.max(0,s.spending-income);if(bal<0){bal=0;break;}}return {atRetire,horizon:bal};}
function cumulative(claimAge,through,s){const offset=s.household==='couple'?(s.you.birthYear+(s.you.birthMonth-1)/12)-(s.spouse.birthYear+(s.spouse.birthMonth-1)/12):0;let t=0;for(let age=Math.floor(Math.min(claimAge,claimAge-offset));age<=through;age++)t+=annualAtPrimaryAge(age,claimAge,claimAge,s,age<s.you.retireAge);return t;}
function cumulativeMixed(a,b,through,s){const offset=s.household==='couple'?(s.you.birthYear+(s.you.birthMonth-1)/12)-(s.spouse.birthYear+(s.spouse.birthMonth-1)/12):0;let t=0;for(let age=Math.floor(Math.min(a,b-offset));age<=through;age++)t+=annualAtPrimaryAge(age,a,b,s,age<s.you.retireAge);return t;}
function cross(a,b,s){for(let age=Math.min(a,b);age<=100;age++){if(cumulative(b,age,s)>=cumulative(a,age,s))return age;}return null;}
function incomeAtRetirement(claimAge,s){return annualAtPrimaryAge(s.you.retireAge,claimAge,claimAge,s,false)+s.pension+s.other;}
function spendingCoverage(claimAge,s){if(s.spending<=0)return 100;return incomeAtRetirement(claimAge,s)/s.spending*100;}
'''

for path in [Path('retirement-strategy-model.js'),Path('_src/retirement-strategy-model.js')]:
    s=path.read_text()
    s,n=re.subn(r'const AWI=\{.*?function populateMonths\(\)',core+'function populateMonths()',s,count=1,flags=re.S)
    if n!=1: raise SystemExit(f'core replace failed {path}')
    s,n=re.subn(r'function quickPiaCalc\(p\).*?function contributions\(s\)',pia+'function contributions(s)',s,count=1,flags=re.S)
    if n!=1: raise SystemExit(f'pia replace failed {path}')
    s,n=re.subn(r'function contributions\(s\).*?function spendingCoverage\(claimAge,s\)\{.*?\}\n',time,s,count=1,flags=re.S)
    if n!=1: raise SystemExit(f'time replace failed {path}')
    old="$('survivor-watch').innerHTML=`<div class=\"rsm-note\"><strong>Survivor-income watch:</strong> A two-benefit household can become a one-benefit household after the first death. The exact survivor amount depends on claiming ages and survivor rules, so this matrix intentionally does not pretend the two checks simply continue. Treat survivor planning as a separate decision before choosing a couple strategy.</div>`;"
    new="const c65=householdComponents(65,65,s,null,false);$('survivor-watch').innerHTML=`<div class=\"rsm-note\"><strong>Household Social Security at 65:</strong> Your worker benefit ${money(c65.youOwn/12)}/mo + spouse worker benefit ${money(c65.spouseOwn/12)}/mo${c65.youExcess?` + your spousal excess ${money(c65.youExcess/12)}/mo`:''}${c65.spouseExcess?` + spouse spousal excess ${money(c65.spouseExcess/12)}/mo`:''} = <b>${money(c65.monthly)}/mo household total</b>.</div><div class=\"rsm-note\"><strong>Survivor-income watch:</strong> Survivor benefits follow separate rules and are not treated as two continuing checks here.</div>`;"
    if old not in s: raise SystemExit(f'couple note replace failed {path}')
    path.write_text(s.replace(old,new,1))
