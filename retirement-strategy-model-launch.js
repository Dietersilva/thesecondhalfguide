(() => {
'use strict';
const moneyText=s=>s||'—';
function updatePathCards(){
  const rows=[...document.querySelectorAll('#strategy-body tr')];
  const cards=[...document.querySelectorAll('#path-cards .rsm-path-card')];
  if(rows.length<3||cards.length<3)return;
  rows.slice(0,3).forEach((row,i)=>{
    const c=[...row.children].map(x=>x.textContent.trim());
    const age=(c[0].match(/\d+/)||[''])[0];
    const monthly=c[1]||'—',horizon=c[5]||'—';
    cards[i].innerHTML=`<span>Claim at</span><strong>${age}</strong><span class="rsm-path-money">${moneyText(monthly)}</span><div class="rsm-path-meta"><span>Annual benefit: ${moneyText(c[2])}</span><span>Portfolio at retirement: ${moneyText(c[4])}</span><span>Portfolio at horizon: ${moneyText(horizon)}</span></div>`;
  });
}
function schedule(){requestAnimationFrame(updatePathCards);}
function init(){
  schedule();
  document.querySelectorAll('.rsm-page input,.rsm-page select').forEach(e=>{e.addEventListener('input',schedule);e.addEventListener('change',schedule);});
  const body=document.getElementById('strategy-body');
  if(body)new MutationObserver(schedule).observe(body,{childList:true,subtree:true,characterData:true});
}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init,{once:true});else init();
})();