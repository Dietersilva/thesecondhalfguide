const c=document.getElementById('creative'),ctx=c.getContext('2d');let mode='fb';
const tabs=[['fb','Facebook Page'],['group','FB Group'],['ig1','Carousel 1'],['ig2','Carousel 2'],['ig3','Carousel 3'],['ig4','Carousel 4'],['cover','Story / Cover'],['video','Reels / TikTok / Shorts Video'],['threads','Threads']];
const tabWrap=document.getElementById('tabs');const note=document.getElementById('previewNote');
tabs.forEach(([id,label])=>{const b=document.createElement('button');b.className='tab'+(id===mode?' on':'');b.textContent=label;b.onclick=()=>{mode=id;[...tabWrap.children].forEach(x=>x.classList.remove('on'));b.classList.add('on');draw()};tabWrap.appendChild(b)});

function font(size,bold=true){return (bold?'800 ':'500 ')+size+'px Arial'}
function text(t,x,y,size,color='#0b2b4b',bold=true,align='left'){ctx.font=font(size,bold);ctx.fillStyle=color;ctx.textAlign=align;ctx.fillText(t,x,y)}
function textMetrics(t,size,bold=true){ctx.font=font(size,bold);const m=ctx.measureText(t);return {ascent:m.actualBoundingBoxAscent||size*.8,descent:m.actualBoundingBoxDescent||size*.2}}
function verticalGap(upperText,upperY,upperSize,lowerText,lowerY,lowerSize){const a=textMetrics(upperText,upperSize,true),b=textMetrics(lowerText,lowerSize,true);const upperBottom=upperY+a.descent;const lowerTop=lowerY-b.ascent;return lowerTop-upperBottom}
function heroClearancePass(){return verticalGap('$90',205,106,'MEDICARE',340,47)>=36}
function wrapText(t,max,size,bold=true){ctx.font=font(size,bold);const words=t.split(' '),lines=[];let line='';for(const w of words){const test=(line+' '+w).trim();if(ctx.measureText(test).width<=max)line=test;else{if(line)lines.push(line);line=w}}if(line)lines.push(line);return lines}
function rr(x,y,w,h,r,fill){ctx.fillStyle=fill;ctx.beginPath();ctx.roundRect(x,y,w,h,r);ctx.fill()}
function base(h=1080){c.width=1080;c.height=h;ctx.fillStyle='#f7f4ed';ctx.fillRect(0,0,1080,h);rr(55,45,555,75,14,'#d71920');text('MEDICARE • OCTOBER 2026',332,95,30,'#fff',true,'center')}
function check(x,y,good){ctx.fillStyle=good?'#168746':'#d71920';ctx.beginPath();ctx.arc(x,y,24,0,Math.PI*2);ctx.fill();text(good?'✓':'×',x,y+11,32,'#fff',true,'center')}
function footer(h){ctx.fillStyle='#fff';ctx.fillRect(0,h-180,1080,180);ctx.strokeStyle='#d7dee5';ctx.beginPath();ctx.moveTo(45,h-180);ctx.lineTo(1035,h-180);ctx.stroke();text('TheSecondHalfGuide.com',540,h-112,42,'#0b2b4b',true,'center');text("Real information for what's next.",540,h-73,24,'#0b2b4b',false,'center');text('PLAIN FACTS • CHECKED AND DATED',540,h-36,17,'#64748b',true,'center')}

function square(group=false){
  base();
  ctx.fillStyle='#0b2b4b';ctx.fillRect(0,0,16,1080);

  // publication kicker
  text('THE SECOND HALF GUIDE',55,158,17,'#64748b',true);
  text('MEDICARE EXPLAINER',55,190,22,'#0b2b4b',true);
  ctx.fillStyle='#f3b21a';ctx.fillRect(55,205,240,6);

  // hero
  text('$90',55,340,118,'#d71920');
  text('MEDICARE PAYMENT',55,415,48,'#0b2b4b');
  text('Who gets it?',55,462,30,'#18212b');

  // big stat module
  ctx.strokeStyle='#cfd9df';ctx.lineWidth=2;ctx.strokeRect(610,145,415,220);
  text('20.8M',817,245,70,'#0b2b4b',true,'center');
  text('eligible people',817,292,23,'#18212b',true,'center');
  text('Source: CMS',817,330,16,'#64748b',false,'center');

  // two-column eligibility infographic
  text('MAY QUALIFY',55,545,20,'#168746',true);
  ctx.fillStyle='#168746';ctx.fillRect(55,560,430,5);
  check(78,625,true);
  text('Original Medicare',125,617,26,'#0b2b4b',true);
  text('with Part B',125,650,24,'#0b2b4b',true);
  text('Living in the U.S.',125,683,18,'#64748b',false);

  text('NOT ELIGIBLE',560,545,20,'#d71920',true);
  ctx.fillStyle='#d71920';ctx.fillRect(560,560,465,5);
  const noRows=['Medicare Advantage','Medicaid premium help','IRMAA payer'];
  let ny=615;
  for(const item of noRows){check(585,ny,false);text(item,632,ny+8,23,'#0b2b4b',true);ny+=68}

  // process strip / action facts
  ctx.fillStyle='#eef3f6';ctx.fillRect(55,765,970,92);
  text('NO APPLICATION',95,808,21,'#0b2b4b',true);
  ctx.fillStyle='#f3b21a';ctx.fillRect(340,787,5,48);
  text('DIRECT DEPOSITS',390,808,21,'#0b2b4b',true);
  text('went out around Oct. 8',390,835,16,'#64748b',false);
  ctx.fillStyle='#f3b21a';ctx.fillRect(690,787,5,48);
  text('PAPER CHECKS',735,808,21,'#0b2b4b',true);
  text('later in October',735,835,16,'#64748b',false);

  if(group)text('SHAREABLE FACT SHEET',1015,120,15,'#64748b',true,'right');
  footer(1080);
  note.textContent='Infographic master: eligibility, exclusions, timing and action facts are structured as data modules instead of generic cards.';
}
function carousel(n){
 base();text(n+'/4',1010,83,24,'#fff',true,'right');
 if(n===1){
  ctx.fillStyle='#0b2b4b';ctx.fillRect(0,0,16,1080);
  text('THE SECOND HALF GUIDE',55,160,17,'#64748b',true);
  text('MEDICARE EXPLAINER',55,190,22,'#0b2b4b',true);
  ctx.fillStyle='#f3b21a';ctx.fillRect(55,205,240,6);
  text('$90',55,340,118,'#d71920');
  text('MEDICARE PAYMENT',55,415,48);
  ctx.strokeStyle='#cfd9df';ctx.lineWidth=2;ctx.strokeRect(55,500,970,190);
  text('20.8M',110,610,70,'#0b2b4b');
  text('people are eligible',480,595,31,'#18212b');
  text('Source: CMS',480,635,17,'#64748b',false);
  ctx.fillStyle='#eef3f6';ctx.fillRect(55,745,970,110);
  text('NO APPLICATION REQUIRED',540,808,31,'#0b2b4b',true,'center');
}
 if(n===2){text('Who may qualify?',55,245,66);check(85,360,true);text('Original Medicare',140,350,42);text('with Part B',140,405,42);text('Living in the U.S.',140,465,27,'#64748b',false);text('Other eligibility rules apply.',55,570,29,'#18212b')}
 if(n===3){text('Who is not eligible?',55,245,61);let y=355;for(const s of ['Medicare Advantage','Medicaid paying your premium','IRMAA payer']){check(85,y,false);for(const ln of wrapText(s,760,35)){text(ln,140,y+12,35);y+=41}y+=75}}
 if(n===4){text('How it arrives',55,245,66);let y=355;for(const s of ['Most direct deposits went out around Oct. 8','Paper checks are expected later in October','No processing fee','No bank verification']){text('•',70,y,44,'#f3b21a');for(const ln of wrapText(s,820,34)){text(ln,125,y,34);y+=41}y+=62}rr(80,775,1000,855,18,'#0b2b4b');text('Full story: TheSecondHalfGuide.com/medicare-90-payment',540,825,23,'#fff',true,'center')}
 footer(1080);note.textContent='Final carousel system: Hook → may qualify → not eligible → arrival + exact readable story path.'
}
function cover(){
  c.width=1080;c.height=1920;
  ctx.fillStyle='#f7f4ed';ctx.fillRect(0,0,1080,1920);
  ctx.fillStyle='#0b2b4b';ctx.fillRect(0,0,20,1920);

  rr(55,55,610,130,16,'#d71920');
  text('MEDICARE • OCTOBER 2026',332,96,30,'#fff',true,'center');

  text('THE SECOND HALF GUIDE',58,205,18,'#64748b',true);
  text('MEDICARE EXPLAINER',58,240,24,'#0b2b4b',true);
  ctx.fillStyle='#f3b21a';ctx.fillRect(58,258,280,7);

  text('$90',58,500,180,'#d71920');
  text('MEDICARE PAYMENT',58,620,72,'#0b2b4b');
  text('Who gets it?',58,690,36,'#18212b');

  // hero statistic as outlined infographic
  ctx.strokeStyle='#cfd9df';ctx.lineWidth=3;ctx.strokeRect(58,785,1022,1015);
  text('20.8M',120,900,100,'#0b2b4b');
  text('people are eligible',575,885,38,'#18212b');
  text('Source: CMS',575,940,20,'#64748b',false);

  // eligibility split
  text('MAY QUALIFY',58,1110,22,'#168746',true);
  ctx.fillStyle='#168746';ctx.fillRect(58,1128,420,6);
  check(85,1200,true);
  text('Original Medicare with Part B',142,1190,30,'#0b2b4b',true);
  text('Living in the U.S.',142,1230,22,'#64748b',false);

  text('NOT ELIGIBLE',58,1345,22,'#d71920',true);
  ctx.fillStyle='#d71920';ctx.fillRect(58,1363,420,6);
  const noRows=['Medicare Advantage','Medicaid premium help','IRMAA payer'];
  let y=1435;
  for(const item of noRows){check(85,y,false);text(item,142,y+10,28,'#0b2b4b',true);y+=82}

  // action ribbon
  ctx.fillStyle='#eef3f6';ctx.fillRect(58,1680,1022,1765);
  text('NO APPLICATION REQUIRED',540,1730,30,'#0b2b4b',true,'center');

  text('TheSecondHalfGuide.com',540,1820,38,'#0b2b4b',true,'center');
  text("Real information for what's next.",540,1865,22,'#0b2b4b',false,'center');
  text('PLAIN FACTS • CHECKED AND DATED',540,1900,16,'#64748b',true,'center');

  note.textContent='Story / cover: infographic-first vertical adaptation of the Facebook/Threads master.';
}
function videoPanel(){
  c.width=1080;c.height=1080;
  ctx.fillStyle='#eef3f6';ctx.fillRect(0,0,1080,1080);
  rr(90,85,990,995,34,'#fff');
  rr(140,140,940,250,24,'#0b2b4b');
  text('ANIMATED VIDEO ASSET',540,205,46,'#fff',true,'center');
  text('24 sec • 9:16 • captioned',540,320,42,'#0b2b4b',true,'center');

  rr(160,390,920,540,28,'#f3b21a');
  text('INSTAGRAM REELS',540,455,38,'#0b2b4b',true,'center');

  rr(160,575,920,725,28,'#d71920');
  text('TIKTOK',540,640,44,'#fff',true,'center');

  rr(160,760,920,910,28,'#0b2b4b');
  text('YOUTUBE SHORTS',540,825,38,'#fff',true,'center');

  text('Use the animated file, not the cover image.',540,965,28,'#64748b',true,'center');
  note.textContent='This tab represents the actual animated social-video asset. The static Story / Cover tab is only the thumbnail/cover companion.';
}
function threads(){square(false);note.textContent='Threads: final image plus exact clickable article URL in post text.'}
function draw(){if(mode==='fb')square(false);else if(mode==='group')square(true);else if(mode.startsWith('ig'))carousel(Number(mode.slice(2)));else if(mode==='cover')cover();else if(mode==='video')videoPanel();else threads();const d=document.getElementById('download');if(d){d.disabled=mode==='video';d.textContent=mode==='video'?'Animated video asset':'Download current PNG'}}draw();

const captions={
'Facebook Page':`A one-time $90 Medicare payment is going out this month — but not everyone with Medicare qualifies.

CMS says about 20.8 million people are eligible. Eligible beneficiaries are in Original Medicare Part B, live in the U.S., are not receiving Medicaid premium assistance, and do not pay IRMAA. Medicare Advantage members are not eligible. No application is required.

Full sourced story:
https://thesecondhalfguide.com/medicare-90-payment

Source: CMS • Checked Oct. 10, 2026`,
'Facebook Group':`For anyone seeing posts about the $90 Medicare payment: it is real, but it is not for everyone.

CMS says it is a one-time October payment for certain people in Original Medicare Part B. Medicare Advantage members, people receiving Medicaid premium assistance, and people paying IRMAA are not eligible. No application is required.

Full sourced explanation:
https://thesecondhalfguide.com/medicare-90-payment

Source: CMS • Checked Oct. 10, 2026`,
'Instagram Carousel':`The $90 Medicare payment is real — but eligibility is narrower than many posts make it sound.

Swipe for who may qualify, who is not eligible, and how the payment arrives.

Full sourced story: LINK IN BIO
TheSecondHalfGuide.com/medicare-90-payment

Source: CMS • Checked Oct. 10, 2026

#Medicare #Retirement #Medicare2026 #SecondHalfGuide`,
'Instagram Story':`Use native Link sticker.

Sticker label: READ THE FULL SOURCED STORY
Destination:
https://thesecondhalfguide.com/medicare-90-payment`,
'Instagram Reel':`The $90 Medicare payment is real — but not everyone gets it.

Who may qualify, who is not eligible, how it arrives, and what to watch for.

Full sourced story: LINK IN BIO
TheSecondHalfGuide.com/medicare-90-payment

Source: CMS • Checked Oct. 10, 2026`,
'Threads':`A one-time $90 Medicare payment is going out this month.

CMS says about 20.8 million people are eligible. It is for certain people in Original Medicare Part B — not Medicare Advantage — and there is no application.

Full sourced story:
https://thesecondhalfguide.com/medicare-90-payment

Source: CMS • Checked Oct. 10, 2026`,
'TikTok':`The $90 Medicare payment is real — but not everyone gets it.

Who may qualify, who is excluded, how it arrives, and what to watch for.

Full sourced story: LINK IN BIO / PROFILE
TheSecondHalfGuide.com/medicare-90-payment

Source: CMS • Checked Oct. 10, 2026`,
'YouTube Short':`TITLE: $90 Medicare Payment: Who Gets It?

The $90 Medicare payment is real, but eligibility is limited. This Short explains who may qualify, who does not, how the payment arrives, and what to watch for.

Full sourced story: first link on our channel profile.
TheSecondHalfGuide.com/medicare-90-payment

Source: CMS • Checked Oct. 10, 2026`
};
const sel=document.getElementById('copySelect'),ta=document.getElementById('copyText');Object.keys(captions).forEach(k=>{const o=document.createElement('option');o.textContent=k;sel.appendChild(o)});function setCopy(){ta.value=captions[sel.value]}sel.onchange=setCopy;setCopy();document.getElementById('copyBtn').onclick=()=>navigator.clipboard.writeText(ta.value);document.getElementById('download').onclick=()=>{if(mode==='video')return;const a=document.createElement('a');a.download='secondsocial-final-'+mode+'-medicare-90.png';a.href=c.toDataURL('image/png');a.click()};

const topical=[
 {title:'2027 Medicare Star Ratings',score:98,why:'Released Oct. 8; Open Enrollment starts Oct. 15',state:'recommended'},
 {title:'DME rule changes Oct. 15',score:96,why:'Rule takes effect in 5 days',state:''},
 {title:'Medicare GLP-1 Bridge',score:93,why:'High-interest $50/month program; active now',state:''},
 {title:'2027 Medicare plan numbers',score:91,why:'Plan Finder / AEP timing',state:''},
 {title:'Medicare search-ad scam',score:89,why:'FTC warning + enrollment-season traffic',state:''},
 {title:'2027 Roth catch-up',score:82,why:'2027 change; strong 60–63 audience fit',state:''},
 {title:'Medicare Advantage plan exits',score:80,why:'Plan-change season',state:''},
 {title:'Medicare marketing rules',score:76,why:'Oct. 1 rule change; still current',state:''},
 {title:'2027 Social Security COLA',score:74,why:'Update after Oct. 14 CPI release',state:''}
];
const q=document.getElementById('queueList');topical.forEach((s,i)=>{const row=document.createElement('div');row.className='qrow '+(s.state||'');row.innerHTML='<div class="rank">'+(i+1)+'</div><div><b>'+s.title+'</b><div class="why">'+s.why+'</div></div><div class="score">'+s.score+'/100</div>';q.appendChild(row)});
const nextSelect=document.getElementById('nextSelect');topical.forEach(s=>{const o=document.createElement('option');o.value=s.title;o.textContent=s.title+' · '+s.score+'/100';nextSelect.appendChild(o)});

const liveBox=document.getElementById('liveCheck'),publish=document.getElementById('publishBtn'),state=document.getElementById('publishState'),approve=document.getElementById('approve'),published=document.getElementById('published'),finish=document.getElementById('finishBtn'),chooser=document.getElementById('chooser'),connectBtn=document.getElementById('connectBtn'),publishedTop=document.getElementById('publishedTop');
let liveStatus=false,networksConnected=false;
approve.checked=localStorage.getItem('secondsocial.med90.approved')!=='0';
published.checked=localStorage.getItem('secondsocial.med90.published')==='1';
async function checkLive(){liveBox.className='warn';liveBox.innerHTML='<b>Checking production article…</b>';try{const target='https://thesecondhalfguide.com/medicare-90-payment';const r=await fetch('/api/secondsocial/check-url?url='+encodeURIComponent(target),{cache:'no-store'});const data=await r.json();liveStatus=!!data.ok&&!data.noindex;if(liveStatus){liveBox.className='ok';liveBox.innerHTML='<b>Live article check passed.</b><div class="small">HTTP '+data.status+' · '+(data.title||'article found')+'</div>'}else{liveBox.className='err';liveBox.innerHTML='<b>Live article check failed.</b><div class="small">Publishing remains blocked.</div>'}}catch(e){liveStatus=false;liveBox.className='err';liveBox.innerHTML='<b>Live article check unavailable.</b>'}gate()}
function gate(){
  const alreadyPublished=published.checked;
  if(publishedTop){
    publishedTop.textContent=alreadyPublished?'PUBLISHED':'NOT PUBLISHED';
    publishedTop.className='pill '+(alreadyPublished?'good':'bad');
  }
  finish.disabled=!alreadyPublished;
  if(alreadyPublished){
    publish.disabled=true;
    publish.textContent='Published';
    state.className='ok';
    state.innerHTML='<b>Story marked published.</b> Finish the campaign to unlock the next story.';
    if(connectBtn) connectBtn.style.display='none';
    return;
  }
  publish.textContent='Publish Story';
  if(!approve.checked){
    publish.disabled=true;
    state.className='err';
    state.innerHTML='<b>Publishing blocked.</b> Approve the exact story package first.';
    return;
  }
  if(!liveStatus){
    publish.disabled=true;
    state.className='err';
    state.innerHTML='<b>Publishing blocked.</b> Live article validation must pass.';
    return;
  }
  if(!networksConnected){
    publish.disabled=true;
    state.className='warn';
    state.innerHTML='<b>Ready to publish once networks are connected.</b> Use Connect networks to finish setup.';
    if(connectBtn) connectBtn.style.display='';
    return;
  }
  publish.disabled=false;
  state.className='ok';
  state.innerHTML='<b>Ready to publish.</b> The exact package is approved, the article is live, and social networks are connected.';
  if(connectBtn) connectBtn.style.display='none';
}
async function loadConnections(){
  try{
    const r=await fetch('/secondsocial/connections.json',{cache:'no-store'});
    const data=await r.json();
    networksConnected=Array.isArray(data?.metricool?.networks)&&data.metricool.networks.length>0;
  }catch(e){networksConnected=false}
  gate();
}
document.getElementById('recheckUrl').onclick=checkLive;
approve.onchange=()=>{localStorage.setItem('secondsocial.med90.approved',approve.checked?'1':'0');gate()};
published.onchange=()=>{localStorage.setItem('secondsocial.med90.published',published.checked?'1':'0');gate()};
publish.onclick=()=>{if(publish.disabled)return;alert('Publishing is ready to hand off to Metricool. Final scheduler wiring will execute the approved package when network connections are present.');};
checkLive();
loadConnections();
finish.onclick=()=>{if(!published.checked)return;chooser.classList.add('open');finish.disabled=true;document.getElementById('activeStatus').textContent='Published · ready to choose next';document.getElementById('activeStatus').className='pill good'};
document.getElementById('activateNext').onclick=()=>alert('Next-story activation stays locked until the current campaign is published and completed. Once connected, activating a story will start a fresh verification job before creative generation.');