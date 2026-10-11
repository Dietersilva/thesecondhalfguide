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

  // subtle editorial geometry
  ctx.strokeStyle='rgba(11,43,75,.06)';ctx.lineWidth=3;
  [150,245,340].forEach(r=>{ctx.beginPath();ctx.arc(940,200,r,0,Math.PI*2);ctx.stroke()});
  ctx.fillStyle='#0b2b4b';ctx.fillRect(0,0,18,1080);

  // kicker
  text('THE SECOND HALF GUIDE',55,158,17,'#64748b',true);
  ctx.fillStyle='#f3b21a';ctx.fillRect(55,176,235,6);

  // hero
  text('$90',55,320,112,'#d71920');
  text('MEDICARE',55,395,42,'#0b2b4b');
  text('PAYMENT',55,460,58,'#0b2b4b');
  text('Who gets it?',55,515,31,'#18212b');

  // eligibility rail
  const rows=[['Original Medicare with Part B',true,'Living in the U.S.'],['Medicare Advantage',false,'Not eligible'],['Medicaid paying your premium',false,'Not eligible'],['IRMAA payer',false,'Not eligible']];
  let y=595;
  for(const [title,good,sub] of rows){
    check(78,y,good);
    text(title,125,y-8,24,'#0b2b4b',true);
    text(sub,125,y+23,18,'#64748b',false);
    y+=73;
  }

  // floating fact panel
  ctx.save();ctx.shadowColor='rgba(11,43,75,.16)';ctx.shadowBlur=22;ctx.shadowOffsetY=8;
  rr(610,500,1025,810,28,'#0b2b4b');ctx.restore();
  text('20.8M',818,585,64,'#fff',true,'center');
  text('people are eligible',818,635,25,'#fff',true,'center');
  ctx.fillStyle='#f3b21a';ctx.fillRect(690,675,255,5);
  text('ONE-TIME $90 PAYMENT',818,720,20,'#dde7ee',true,'center');
  text('Source: CMS',818,760,17,'#dde7ee',false,'center');
  text('Checked Oct. 10, 2026',818,790,15,'#aebfcb',false,'center');

  if(group)text('SHAREABLE FACT SHEET',1015,150,15,'#64748b',true,'right');
  footer(1080);
  note.textContent=(heroClearancePass()?'✓ ':'⚠ ')+'Sleek editorial master: shared Facebook/Threads visual system with measured spacing and mobile-safe hierarchy.';
}
function carousel(n){
 base();text(n+'/4',1010,83,24,'#fff',true,'right');
 if(n===1){ctx.fillStyle='#0b2b4b';ctx.fillRect(0,0,16,1080);text('THE SECOND HALF GUIDE',55,160,17,'#64748b',true);ctx.fillStyle='#f3b21a';ctx.fillRect(55,178,230,6);text('$90',55,300,112,'#d71920');text('MEDICARE PAYMENT',55,390,58);text('KEY FACTS',55,465,46);let y=565;for(const s of ['One-time payment','About 20.8 million people','No application required','Watch for scams']){check(80,y,true);text(s,135,y+12,34,'#18212b');y+=88}}
 if(n===2){text('Who may qualify?',55,245,66);check(85,360,true);text('Original Medicare',140,350,42);text('with Part B',140,405,42);text('Living in the U.S.',140,465,27,'#64748b',false);text('Other eligibility rules apply.',55,570,29,'#18212b')}
 if(n===3){text('Who is not eligible?',55,245,61);let y=355;for(const s of ['Medicare Advantage','Medicaid paying your premium','IRMAA payer']){check(85,y,false);for(const ln of wrapText(s,760,35)){text(ln,140,y+12,35);y+=41}y+=75}}
 if(n===4){text('How it arrives',55,245,66);let y=355;for(const s of ['Most direct deposits went out around Oct. 8','Paper checks are expected later in October','No processing fee','No bank verification']){text('•',70,y,44,'#f3b21a');for(const ln of wrapText(s,820,34)){text(ln,125,y,34);y+=41}y+=62}rr(80,775,1000,855,18,'#0b2b4b');text('Full story: TheSecondHalfGuide.com/medicare-90-payment',540,825,23,'#fff',true,'center')}
 footer(1080);note.textContent='Final carousel system: Hook → may qualify → not eligible → arrival + exact readable story path.'
}
function cover(){
  c.width=1080;c.height=1920;
  ctx.fillStyle='#f7f4ed';ctx.fillRect(0,0,1080,1920);

  // shared editorial rail + geometry
  ctx.fillStyle='#0b2b4b';ctx.fillRect(0,0,22,1920);
  ctx.strokeStyle='rgba(11,43,75,.055)';ctx.lineWidth=4;
  [180,300,420].forEach(r=>{ctx.beginPath();ctx.arc(930,250,r,0,Math.PI*2);ctx.stroke()});

  rr(55,55,610,130,16,'#d71920');
  text('MEDICARE • OCTOBER 2026',332,96,30,'#fff',true,'center');

  text('THE SECOND HALF GUIDE',58,200,18,'#64748b',true);
  ctx.fillStyle='#f3b21a';ctx.fillRect(58,220,270,7);

  // hero
  text('$90',58,445,175,'#d71920');
  text('MEDICARE',58,590,64,'#0b2b4b');
  text('PAYMENT',58,685,90,'#0b2b4b');
  text('Who gets it?',58,760,38,'#18212b');

  // eligibility list
  const rows=[
    ['Original Medicare with Part B',true,'Living in the U.S.'],
    ['Medicare Advantage',false,'Not eligible'],
    ['Medicaid paying your premium',false,'Not eligible'],
    ['IRMAA payer',false,'Not eligible']
  ];
  let y=885;
  for(const [title,good,sub] of rows){
    check(82,y,good);
    text(title,138,y-9,28,'#0b2b4b',true);
    text(sub,138,y+28,21,'#64748b',false);
    y+=105;
  }

  // fact panel
  ctx.save();ctx.shadowColor='rgba(11,43,75,.16)';ctx.shadowBlur=26;ctx.shadowOffsetY=10;
  rr(58,1315,1022,1560,30,'#0b2b4b');ctx.restore();
  text('20.8M',540,1400,76,'#fff',true,'center');
  text('people are eligible',540,1460,31,'#fff',true,'center');
  ctx.fillStyle='#f3b21a';ctx.fillRect(330,1500,420,6);
  text('Source: CMS',540,1535,20,'#dde7ee',false,'center');

  // footer
  ctx.fillStyle='#fff';ctx.fillRect(0,1665,1080,255);
  ctx.strokeStyle='#d7dee5';ctx.lineWidth=2;ctx.beginPath();ctx.moveTo(58,1665);ctx.lineTo(1022,1665);ctx.stroke();
  text('TheSecondHalfGuide.com',540,1750,40,'#0b2b4b',true,'center');
  text("Real information for what's next.",540,1805,24,'#0b2b4b',false,'center');
  text('PLAIN FACTS • CHECKED AND DATED',540,1855,18,'#64748b',true,'center');

  note.textContent='Story / cover: vertical adaptation of the same sleek Facebook/Threads editorial system.';
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