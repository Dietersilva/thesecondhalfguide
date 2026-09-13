(() => {
'use strict';
const $=id=>document.getElementById(id);
function setupModes(){
  const quick=$('rsm-quick-mode'),advanced=$('rsm-advanced-mode'),help=$('rsm-mode-help');
  if(!quick||!advanced)return;
  const setMode=(mode,scroll=false)=>{const isAdvanced=mode==='advanced';document.body.classList.toggle('is-advanced',isAdvanced);document.body.classList.toggle('is-quick',!isAdvanced);quick.classList.toggle('is-active',!isAdvanced);advanced.classList.toggle('is-active',isAdvanced);quick.setAttribute('aria-pressed',String(!isAdvanced));advanced.setAttribute('aria-pressed',String(isAdvanced));if(help)help.textContent=isAdvanced?'Advanced mode keeps every planning control visible. Your Quick-mode entries stay in place.':'Quick mode keeps the inputs short. Advanced mode adds contributions, pensions, return assumptions, Medicare and exact SSA estimates.';if(scroll)$('calculator-title')?.scrollIntoView({behavior:'smooth',block:'start'});};
  quick.addEventListener('click',()=>setMode('quick',true));advanced.addEventListener('click',()=>setMode('advanced',true));setMode('quick',false);
}
function preservePreviewLinks(){const token=new URLSearchParams(location.search).get('_vercel_share');if(!token)return;document.querySelectorAll('a[href^="/"]').forEach(a=>{const u=new URL(a.getAttribute('href'),location.origin);u.searchParams.set('_vercel_share',token);a.href=u.pathname+u.search+u.hash;});}
function cells(row){return row?[...row.children].map(x=>x.textContent.trim()):[];}
function syncAuditedSecondary(){
  const rows=[...document.querySelectorAll('#strategy-body tr')];if(rows.length<3)return;
  const a=cells(rows[0]),b=cells(rows[1]),c=cells(rows[2]),meaning=$('meaning-results');
  if(meaning){const be65=$('break-even-65')?.textContent||'—',be67=$('break-even-67')?.textContent||'—';meaning.innerHTML=`<div class="rsm-note"><strong>Household monthly Social Security:</strong> The audited comparison shows <b>${a[1]}</b> at 62, <b>${b[1]}</b> at 65 and <b>${c[1]}</b> at 67.</div><div class="rsm-note"><strong>When waiting catches up:</strong> 62 vs. 65 is ${be65}; 62 vs. 67 is ${be67}.</div><div class="rsm-note"><strong>Portfolio consequence:</strong> At the planning horizon, the audited model shows <b>${a[5]}</b> for claim age 62, <b>${b[5]}</b> for 65 and <b>${c[5]}</b> for 67.</div>`;}
  const earnings=$('earnings-results');if(earnings)earnings.innerHTML='<div class="rsm-note"><strong>2026 earnings test:</strong> Before full retirement age, the annual limit is $24,480 and benefits are generally withheld $1 for each $2 above the limit. In the year full retirement age is reached, a separate $65,160 limit and $1-for-$3 rule applies before the FRA month. This planner uses annualized whole-age scenarios, so confirm an exact filing month with SSA before relying on an earnings-test amount.</div>';
  const stress=$('stress-body');if(stress)stress.innerHTML='<tr><td colspan="4"><strong>Stress-test figures temporarily withheld.</strong><br><small>The main 62/65/67 portfolio results above are audited. Alternate-return figures will return after that secondary engine uses the same couple timing rules.</small></td></tr>';
  const chart=$('crossover-chart');if(chart&&!chart.dataset.audited){chart.dataset.audited='1';chart.replaceChildren();const t=document.createElementNS('http://www.w3.org/2000/svg','text');t.setAttribute('x','410');t.setAttribute('y','175');t.setAttribute('text-anchor','middle');t.setAttribute('font-size','18');t.setAttribute('fill','currentColor');t.textContent='Use the audited break-even ages above.';chart.appendChild(t);}
}
function scheduleAudit(){setTimeout(()=>requestAnimationFrame(syncAuditedSecondary),360);}
function init(){setupModes();preservePreviewLinks();scheduleAudit();const body=$('strategy-body');if(body)new MutationObserver(scheduleAudit).observe(body,{childList:true,subtree:true});document.querySelectorAll('.rsm-page input,.rsm-page select').forEach(e=>{e.addEventListener('input',scheduleAudit);e.addEventListener('change',scheduleAudit);});}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init,{once:true});else init();
})();