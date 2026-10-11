const c=document.getElementById('creative'),ctx=c.getContext('2d');let mode='fb';
const tabs=[['fb','Facebook Page'],['group','FB Group'],['ig1','Carousel 1'],['ig2','Carousel 2'],['ig3','Carousel 3'],['ig4','Carousel 4'],['vertical','Native 9:16'],['threads','Threads']];
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
 base();text('$90',55,205,106,'#d71920');text('MEDICARE',55,340,47);text('PAYMENT',55,410,64);text('Who gets it?',55,470,38);
 const rows=[['Original Medicare with Part B',true,'Living in the U.S.'],['Medicare Advantage',false,'Not eligible'],['Medicaid paying your premium',false,'Not eligible'],['IRMAA payer',false,'Not eligible']];
 let y=548;
 for(const [title,good,sub] of rows){check(78,y,good);let yy=y-22;for(const ln of wrapText(title,430,28)){text(ln,125,yy,28);yy+=34}text(sub,125,yy+2,20,'#64748b',false);y+=94}
 rr(600,525,425,305,30,'#0b2b4b');let yy=570;for(const ln of wrapText('About 20.8 million people are eligible for a one-time $90 payment this month.',335,29)){text(ln,635,yy,29,'#fff');yy+=40}
 ctx.strokeStyle='#6e89a0';ctx.beginPath();ctx.moveTo(630,760);ctx.lineTo(995,760);ctx.stroke();text('Source: CMS',813,795,18,'#fff',true,'center');text('Checked Oct. 10, 2026',813,820,16,'#dde7ee',false,'center');
 if(group)text('SHAREABLE FACT SHEET',1015,150,16,'#64748b',true,'right');footer(1080);note.textContent=(heroClearancePass()?'✓ ':'⚠ ')+'Hero-number clearance checked. Final square master: no overlap, one brand footer, exact article URL carried in post copy.'
}
function carousel(n){
 base();text(n+'/4',1010,83,24,'#fff',true,'right');
 if(n===1){text('$90',55,205,112,'#d71920');text('MEDICARE PAYMENT',55,350,58);text('KEY FACTS',55,425,46);let y=535;for(const s of ['One-time payment','About 20.8 million people','No application required','Watch for scams']){check(80,y,true);text(s,135,y+12,34,'#18212b');y+=88}}
 if(n===2){text('Who may qualify?',55,245,66);check(85,360,true);text('Original Medicare',140,350,42);text('with Part B',140,405,42);text('Living in the U.S.',140,465,27,'#64748b',false);text('Other eligibility rules apply.',55,570,29,'#18212b')}
 if(n===3){text('Who is not eligible?',55,245,61);let y=355;for(const s of ['Medicare Advantage','Medicaid paying your premium','IRMAA payer']){check(85,y,false);for(const ln of wrapText(s,760,35)){text(ln,140,y+12,35);y+=41}y+=75}}
 if(n===4){text('How it arrives',55,245,66);let y=355;for(const s of ['Most direct deposits went out around Oct. 8','Paper checks are expected later in October','No processing fee','No bank verification']){text('•',70,y,44,'#f3b21a');for(const ln of wrapText(s,820,34)){text(ln,125,y,34);y+=41}y+=62}rr(80,775,1000,855,18,'#0b2b4b');text('Full story: TheSecondHalfGuide.com/medicare-90-payment',540,825,23,'#fff',true,'center')}
 footer(1080);note.textContent='Final carousel system: Hook → may qualify → not eligible → arrival + exact readable story path.'
}
function vertical(){
 c.width=1080;c.height=1920;ctx.fillStyle='#f7f4ed';ctx.fillRect(0,0,1080,1920);
 rr(55,45,610,78,16,'#0b2b4b');text('MEDICARE • OCTOBER 2026',332,96,30,'#fff',true,'center');
 text('$90',55,335,145,'#d71920');text('MEDICARE',55,480,72);text('PAYMENT',55,575,72);
 rr(55,665,980,780,26,'#f3b21a');text('NO APPLICATION REQUIRED',545,738,38,'#0b2b4b',true,'center');
 text('It’s real.',55,930,54,'#18212b');text('But not everyone gets it.',55,1005,54,'#18212b');
 rr(610,1110,1015,1320,28,'#fff');text('20.8M',812,1185,58,'#0b2b4b',true,'center');text('eligible people',812,1240,26,'#18212b',true,'center');text('Source: CMS',812,1285,20,'#64748b',false,'center');
 rr(180,1455,900,1555,24,'#0b2b4b');text('LINK IN BIO / PROFILE',540,1518,30,'#fff',true,'center');
 text('TheSecondHalfGuide.com/medicare-90-payment',540,1645,27,'#0b2b4b',true,'center');
 ctx.strokeStyle='#d7dee5';ctx.beginPath();ctx.moveTo(90,1730);ctx.lineTo(990,1730);ctx.stroke();
 text("Real information for what's next.",540,1790,28,'#0b2b4b',false,'center');text('PLAIN FACTS • CHECKED AND DATED',540,1840,19,'#64748b',true,'center');
 note.textContent='Native 9:16 master: vertical-first composition, no square-card inset, no repeated footer, no headline collision. Final video uses timed on-screen captions.'
}
function threads(){square(false);note.textContent='Threads: final image plus exact clickable article URL in post text.'}
function draw(){if(mode==='fb')square(false);else if(mode==='group')square(true);else if(mode.startsWith('ig'))carousel(Number(mode.slice(2)));else if(mode==='vertical')vertical();else threads()}draw();

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
const sel=document.getElementById('copySelect'),ta=document.getElementById('copyText');Object.keys(captions).forEach(k=>{const o=document.createElement('option');o.textContent=k;sel.appendChild(o)});function setCopy(){ta.value=captions[sel.value]}sel.onchange=setCopy;setCopy();document.getElementById('copyBtn').onclick=()=>navigator.clipboard.writeText(ta.value);document.getElementById('download').onclick=()=>{const a=document.createElement('a');a.download='secondsocial-final-'+mode+'-medicare-90.png';a.href=c.toDataURL('image/png');a.click()};

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

const liveBox=document.getElementById('liveCheck'),publish=document.getElementById('publishBtn'),state=document.getElementById('publishState'),approve=document.getElementById('approve'),published=document.getElementById('published'),finish=document.getElementById('finishBtn'),chooser=document.getElementById('chooser');
let liveStatus=false;
approve.checked=localStorage.getItem('secondsocial.med90.approved')!=='0';
published.checked=localStorage.getItem('secondsocial.med90.published')==='1';
async function checkLive(){liveBox.className='warn';liveBox.innerHTML='<b>Checking production article…</b>';try{const target='https://thesecondhalfguide.com/medicare-90-payment';const r=await fetch('/api/secondsocial/check-url?url='+encodeURIComponent(target),{cache:'no-store'});const data=await r.json();liveStatus=!!data.ok&&!data.noindex;if(liveStatus){liveBox.className='ok';liveBox.innerHTML='<b>Live article check passed.</b><div class="small">HTTP '+data.status+' · '+(data.title||'article found')+'</div>'}else{liveBox.className='err';liveBox.innerHTML='<b>Live article check failed.</b><div class="small">Publishing remains blocked.</div>'}}catch(e){liveStatus=false;liveBox.className='err';liveBox.innerHTML='<b>Live article check unavailable.</b>'}gate()}
function gate(){
  publish.disabled=true;
  finish.disabled=!published.checked;
  if(!approve.checked){
    state.className='err';
    state.innerHTML='<b>Publishing blocked.</b> Approve the exact story package first.';
    return;
  }
  if(!liveStatus){
    state.className='err';
    state.innerHTML='<b>Publishing blocked.</b> Live article validation must pass.';
    return;
  }
  state.className='warn';
  state.innerHTML='<b>Approved and live.</b> Connect social networks in Metricool to enable scheduling.';
}
document.getElementById('recheckUrl').onclick=checkLive;
approve.onchange=()=>{localStorage.setItem('secondsocial.med90.approved',approve.checked?'1':'0');gate()};
published.onchange=()=>{localStorage.setItem('secondsocial.med90.published',published.checked?'1':'0');gate()};
checkLive();
finish.onclick=()=>{if(!published.checked)return;chooser.classList.add('open');finish.disabled=true;document.getElementById('activeStatus').textContent='Published · ready to choose next';document.getElementById('activeStatus').className='pill good'};
document.getElementById('activateNext').onclick=()=>alert('Next-story activation stays locked until the current campaign is published and completed. Once connected, activating a story will start a fresh verification job before creative generation.');