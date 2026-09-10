(() => {
'use strict';
function setupModes(){
  const quick=document.getElementById('rsm-quick-mode');
  const advanced=document.getElementById('rsm-advanced-mode');
  const help=document.getElementById('rsm-mode-help');
  if(!quick||!advanced)return;
  const setMode=(mode,scroll=false)=>{
    const isAdvanced=mode==='advanced';
    document.body.classList.toggle('is-advanced',isAdvanced);
    document.body.classList.toggle('is-quick',!isAdvanced);
    quick.classList.toggle('is-active',!isAdvanced);
    advanced.classList.toggle('is-active',isAdvanced);
    quick.setAttribute('aria-pressed',String(!isAdvanced));
    advanced.setAttribute('aria-pressed',String(isAdvanced));
    if(help)help.textContent=isAdvanced?'Advanced mode keeps every planning control visible. Your Quick-mode entries stay in place.':'Quick mode keeps the inputs short. Advanced mode adds contributions, pensions, return assumptions, Medicare and exact SSA estimates.';
    if(scroll)document.getElementById('calculator-title')?.scrollIntoView({behavior:'smooth',block:'start'});
  };
  quick.addEventListener('click',()=>setMode('quick',true));
  advanced.addEventListener('click',()=>setMode('advanced',true));
  setMode('quick',false);
}
function preservePreviewLinks(){
 const token=new URLSearchParams(location.search).get('_vercel_share');
 if(!token)return;
 document.querySelectorAll('a[href^="/"]').forEach(a=>{const u=new URL(a.getAttribute('href'),location.origin);u.searchParams.set('_vercel_share',token);a.href=u.pathname+u.search+u.hash;});
}
function init(){setupModes();preservePreviewLinks();}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init,{once:true});else init();
})();