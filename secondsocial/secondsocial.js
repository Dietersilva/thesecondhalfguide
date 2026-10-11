const c=document.getElementById('creative'),ctx=c.getContext('2d');let mode='fb';
const tabs=[['fb','Facebook Page'],['group','FB Group'],['ig1','Carousel 1'],['ig2','Carousel 2'],['ig3','Carousel 3'],['ig4','Carousel 4'],['vertical','Reel/Story'],['threads','Threads']];
const tabWrap=document.getElementById('tabs');tabs.forEach(([id,label])=>{const b=document.createElement('button');b.className='tab'+(id===mode?' on':'');b.textContent=label;b.onclick=()=>{mode=id;[...tabWrap.children].forEach(x=>x.classList.remove('on'));b.classList.add('on');draw()};tabWrap.appendChild(b)});
function font(size,bold=true){return (bold?'800 ':'500 ')+size+'px Arial'}
function text(t,x,y,size,color='#0b2b4b',bold=true,align='left'){ctx.font=font(size,bold);ctx.fillStyle=color;ctx.textAlign=align;ctx.fillText(t,x,y)}
function wrapText(t,max,size,bold=true){ctx.font=font(size,bold);const words=t.split(' '),lines=[];let line='';for(const w of words){const test=(line+' '+w).trim();if(ctx.measureText(test).width<=max)line=test;else{if(line)lines.push(line);line=w}}if(line)lines.push(line);return lines}
function rr(x,y,w,h,r,fill){ctx.fillStyle=fill;ctx.beginPath();ctx.roundRect(x,y,w,h,r);ctx.fill()}
function base(h=1080){c.width=1080;c.height=h;ctx.fillStyle='#f7f4ed';ctx.fillRect(0,0,1080,h);rr(55,45,555,75,14,'#d71920');text('MEDICARE • OCTOBER 2026',332,95,30,'#fff',true,'center')}
function check(x,y,good){ctx.fillStyle=good?'#168746':'#d71920';ctx.beginPath();ctx.arc(x,y,24,0,Math.PI*2);ctx.fill();text(good?'✓':'×',x,y+11,32,'#fff',true,'center')}
function footer(h){ctx.fillStyle='#fff';ctx.fillRect(0,h-180,1080,180);ctx.strokeStyle='#d7dee5';ctx.beginPath();ctx.moveTo(45,h-180);ctx.lineTo(1035,h-180);ctx.stroke();text('TheSecondHalfGuide.com',540,h-112,42,'#0b2b4b',true,'center');text("Real information for what's next.",540,h-73,24,'#0b2b4b',false,'center');text('PLAIN FACTS • CHECKED AND DATED',540,h-36,17,'#64748b',true,'center')}
function square(group=false){
 base();
 // More breathing room than V1
 text('$90',55,220,132,'#d71920');
 text('MEDICARE',55,292,48,'#0b2b4b');
 text('PAYMENT',55,375,72,'#0b2b4b');
 text('Who gets it?',55,445,42,'#0b2b4b');
 const rows=[['Original Medicare with Part B',true,'Living in the U.S.'],['Medicare Advantage',false,'Not eligible'],['Medicaid paying your premium',false,'Not eligible'],['IRMAA payer',false,'Not eligible']];
 let y=530;
 for(const [title,good,sub] of rows){check(78,y,good);let yy=y-22;for(const ln of wrapText(title,430,29)){text(ln,125,yy,29);yy+=35}text(sub,125,yy+3,21,'#64748b',false);y+=95}
 rr(600,500,425,330,30,'#0b2b4b');let yy=555;
 for(const ln of wrapText('About 20.8 million people will receive a one-time $90 payment this month.',335,30)){text(ln,635,yy,30,'#fff');yy+=41}
 ctx.strokeStyle='#6e89a0';ctx.lineWidth=2;ctx.beginPath();ctx.moveTo(630,760);ctx.lineTo(995,760);ctx.stroke();
 text('Source: CMS',813,795,18,'#fff',true,'center');text('Checked Oct. 10, 2026',813,820,16,'#dde7ee',false,'center');
 if(group)text('SHAREABLE FACT SHEET',1015,150,16,'#64748b',true,'right');footer(1080)
}
function carousel(n){base();text(n+'/4',1010,83,24,'#fff',true,'right');if(n===1){text('$90',55,240,140,'#d71920');text('MEDICARE PAYMENT',55,345,67,'#0b2b4b');text('KEY FACTS',55,425,50,'#0b2b4b');const a=['One-time payment','About 20.8 million people','No application required','Watch for scams'];let y=535;for(const s of a){check(80,y,true);text(s,135,y+12,35,'#18212b');y+=88}}if(n===2){text('Who gets it?',55,245,72);check(85,360,true);text('Original Medicare',140,350,43);text('with Part B',140,405,43);text('Living in the U.S.',140,465,28,'#64748b',false);text('Other eligibility rules apply.',55,570,30,'#18212b');}if(n===3){text("Who doesn't?",55,245,72);let y=355;for(const s of ['Medicare Advantage','Medicaid paying your premium','IRMAA payer']){check(85,y,false);for(const ln of wrapText(s,760,36)){text(ln,140,y+12,36);y+=42}y+=75}}if(n===4){text('What to know',55,245,72);let y=355;for(const s of ['No application','No processing fee','Most deposits around Oct. 8','Paper checks later in October']){text('•',70,y,44,'#f3b21a');for(const ln of wrapText(s,820,35)){text(ln,125,y,35);y+=42}y+=68}}footer(1080)}
function vertical(){base(1920);text('$90',55,300,155,'#d71920');text('MEDICARE PAYMENT',55,420,76);rr(55,485,700,92,24,'#f3b21a');text('NO APPLICATION REQUIRED',405,547,34,'#0b2b4b',true,'center');let yy=700;for(const ln of wrapText("Who qualifies, who doesn't, when it arrives, and the scam angle.",900,54)){text(ln,55,yy,54);yy+=68}rr(55,1030,970,315,30,'#fff');yy=1095;for(const s of ['Original Medicare Part B','Living in the U.S.','No Medicaid premium assistance','No IRMAA']){check(95,yy,true);text(s,150,yy+12,35,'#18212b');yy+=64}text('Source: CMS • Checked Oct. 10, 2026',540,1450,25,'#64748b',true,'center');footer(1920)}
function threads(){square(false)}
function draw(){if(mode==='fb')square(false);else if(mode==='group')square(true);else if(mode.startsWith('ig'))carousel(Number(mode.slice(2)));else if(mode==='vertical')vertical();else threads()}draw();

const captions={
'Facebook Page':`A real one-time $90 Medicare payment is going out this month, but not everyone with Medicare qualifies.

CMS says eligible beneficiaries are in Original Medicare Part B, live in the U.S., are not receiving Medicaid premium assistance, and do not pay IRMAA. Medicare Advantage members are not eligible. There is no application.

Full sourced explanation: https://thesecondhalfguide.com/medicare-90-payment

Source: CMS • Checked Oct. 10, 2026`,
'Facebook Group':`For anyone seeing posts about the new $90 Medicare payment: it is real, but it is not for everyone.

CMS says it is a one-time October payment for certain people in Original Medicare Part B. No application is required. Medicare Advantage members, people receiving Medicaid premium assistance, and people paying IRMAA are not eligible.

Full sourced explanation:
https://thesecondhalfguide.com/medicare-90-payment

Source: CMS (checked Oct. 10, 2026)`,
'Instagram':`The $90 Medicare payment is real — but eligibility is narrower than a lot of posts make it sound.

Swipe for who gets it, who doesn't, and what to know. No application is required.

Full sourced explanation at TheSecondHalfGuide.com
Source: CMS • Checked Oct. 10, 2026

#Medicare #Retirement #Medicare2026 #SecondHalfGuide`,
'Threads':`A one-time $90 Medicare payment is going out this month.

CMS says about 20.8 million people are eligible. It is for certain people in Original Medicare Part B — not Medicare Advantage — and there is no application.

The eligibility rules matter more than the headline:
https://thesecondhalfguide.com/medicare-90-payment

Source: CMS • Checked Oct. 10, 2026`,
'Reel / TikTok / Shorts':`HOOK: A real $90 Medicare payment is going out this month — but not everyone gets it.

CMS says it is a one-time October rebate for certain people in Original Medicare Part B. Medicare Advantage members are excluded. Medicaid premium assistance and IRMAA also affect eligibility. You do not apply.

CLOSE: Full sourced explanation at TheSecondHalfGuide.com.

ON-SCREEN SOURCE: CMS • Checked Oct. 10, 2026`
};
const sel=document.getElementById('copySelect'),ta=document.getElementById('copyText');Object.keys(captions).forEach(k=>{const o=document.createElement('option');o.textContent=k;sel.appendChild(o)});function setCopy(){ta.value=captions[sel.value]}sel.onchange=setCopy;setCopy();document.getElementById('copyBtn').onclick=()=>navigator.clipboard.writeText(ta.value);document.getElementById('download').onclick=()=>{const a=document.createElement('a');a.download='secondsocial-'+mode+'-medicare-90.png';a.href=c.toDataURL('image/png');a.click()};

const topical=[
 {title:'2027 Medicare Star Ratings',score:98,why:'Released Oct. 8; Open Enrollment starts Oct. 15',state:'recommended'},
 {title:'DME rule changes Oct. 15',score:96,why:'Rule takes effect in 5 days',state:''},
 {title:'Medicare GLP-1 Bridge',score:93,why:'High-interest $50/month program; active now',state:''},
 {title:'2027 Medicare plan numbers',score:91,why:'Plan Finder / AEP timing',state:''},
 {title:'Medicare search-ad scam',score:89,why:'FTC warning + enrollment-season traffic',state:''},
 {title:'2027 Roth catch-up',score:82,why:'2027 change; strong 60-63 audience fit',state:''},
 {title:'Medicare Advantage plan exits',score:80,why:'Plan-change season',state:''},
 {title:'Medicare marketing rules',score:76,why:'Oct. 1 rule change; still current',state:''},
 {title:'2027 Social Security COLA',score:74,why:'Update after Oct. 14 CPI release',state:''}
];
const q=document.getElementById('queueList');topical.forEach((s,i)=>{const row=document.createElement('div');row.className='qrow '+(s.state||'');row.innerHTML='<div class="rank">'+(i+1)+'</div><div><b>'+s.title+'</b><div class="why">'+s.why+'</div></div><div class="score">'+s.score+'/100</div>';q.appendChild(row)});
const nextSelect=document.getElementById('nextSelect');topical.forEach(s=>{const o=document.createElement('option');o.value=s.title;o.textContent=s.title+' · '+s.score+'/100';nextSelect.appendChild(o)});

const approve=document.getElementById('approve'),published=document.getElementById('published'),publish=document.getElementById('publishBtn'),finish=document.getElementById('finishBtn'),chooser=document.getElementById('chooser'),state=document.getElementById('publishState'),liveBox=document.getElementById('liveCheck');
let liveStatus=false;
approve.checked=localStorage.getItem('secondsocial.med90.approved')==='1';
published.checked=localStorage.getItem('secondsocial.med90.published')==='1';
function gate(){
 if(!approve.checked||!liveStatus){state.className='err';state.innerHTML='<b>Publishing blocked.</b> The exact package must be approved and the production article must pass the live URL check.';publish.disabled=true;finish.disabled=true;return}
 state.className='warn';state.innerHTML='<b>Creative approved and article live.</b> Publishing remains blocked until social accounts are connected to Metricool.';publish.disabled=true;
 finish.disabled=!published.checked;
}
approve.onchange=()=>{localStorage.setItem('secondsocial.med90.approved',approve.checked?'1':'0');gate()};
published.onchange=()=>{localStorage.setItem('secondsocial.med90.published',published.checked?'1':'0');gate()};
async function checkLive(){
 liveBox.className='warn'; liveBox.innerHTML='<b>Checking production article…</b>';
 try{
   const target='https://thesecondhalfguide.com/medicare-90-payment';
   const r=await fetch('/api/secondsocial/check-url?url='+encodeURIComponent(target),{cache:'no-store'});
   const data=await r.json();
   liveStatus=!!data.ok && !data.noindex;
   if(liveStatus){
     liveBox.className='ok'; liveBox.innerHTML='<b>Live article check passed.</b><div class="small">HTTP '+data.status+' · '+(data.title||'article found')+'</div>';
   }else{
     liveBox.className='err'; liveBox.innerHTML='<b>Live article check failed.</b><div class="small">HTTP '+(data.status||'error')+'. /SECONDSOCIAL will not publish this campaign until the destination is live and indexable.</div>';
   }
 }catch(e){
   liveStatus=false; liveBox.className='err'; liveBox.innerHTML='<b>Live article check unavailable.</b><div class="small">Publishing remains blocked until the check succeeds.</div>';
 }
 gate();
}
document.getElementById('recheckUrl').onclick=checkLive;
checkLive();
finish.onclick=()=>{if(!published.checked)return;chooser.classList.add('open');finish.disabled=true;localStorage.setItem('secondsocial.med90.complete','1');document.getElementById('activeStatus').textContent='Published · ready to choose next';document.getElementById('activeStatus').className='pill good'};
document.getElementById('activateNext').onclick=()=>{alert('Prototype: '+nextSelect.value+' will become the next active story after production publishing is connected. The finished engine will create a fresh verification job before any creative is generated.');};
