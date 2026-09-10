(() => {
'use strict';

function ensureInteriorNavigation(){
  const nav=document.querySelector('.topbar .topnav');
  if(!nav)return;
  let home=nav.querySelector('.topbar-home');
  if(!home){
    home=document.createElement('a');
    home.className='topbar-home';
    home.href='/';
    home.textContent='Home';
    const search=nav.querySelector('.topbar-search');
    nav.insertBefore(home,search||nav.firstChild);
  }
  const wordmark=document.querySelector('.topbar .wordmark');
  if(wordmark)wordmark.setAttribute('href','/');
}

function setupModes(){
  const quick=document.getElementById('rsm-quick-mode');
  const advanced=document.getElementById('rsm-advanced-mode');
  const details=document.getElementById('advanced-customization')||document.querySelector('.rsm-inputs .rsm-advanced');
  if(!quick||!advanced||!details)return;

  document.querySelectorAll('.rsm-inputs .btn.btn-primary').forEach(btn=>{
    if(btn!==quick&&btn!==advanced&&btn.textContent.trim()==='Advanced customization')btn.remove();
  });

  const setMode=(mode,scroll=false)=>{
    const isAdvanced=mode==='advanced';
    details.open=isAdvanced;
    quick.classList.toggle('is-active',!isAdvanced);
    advanced.classList.toggle('is-active',isAdvanced);
    quick.setAttribute('aria-pressed',String(!isAdvanced));
    advanced.setAttribute('aria-pressed',String(isAdvanced));
    if(scroll){
      (isAdvanced?details:document.getElementById('calculator-title'))?.scrollIntoView({behavior:'smooth',block:'start'});
    }
  };

  quick.addEventListener('click',()=>setMode('quick',true));
  advanced.addEventListener('click',()=>setMode('advanced',true));
  details.addEventListener('toggle',()=>setMode(details.open?'advanced':'quick',false));
  setMode('quick',false);
}

function init(){
  ensureInteriorNavigation();
  setupModes();
}

if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init,{once:true});else init();
})();
