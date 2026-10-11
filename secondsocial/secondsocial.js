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
function videoPanel(){
  c.width=1080;c.height=1080;
  ctx.fillStyle='#eef3f6';ctx.fillRect(0,0,1080,1080);
  rr(90,85,900,910,34,'#fff');
  text('ANIMATED VIDEO ASSET',540,200,46,'#0b2b4b',true,'center');
  text('24 sec \u2022 9:16 \u2022 captioned',540,260,32,'#64748b',true,'center');
  const rows=[['INSTAGRAM REELS','#f3b21a','#0b2b4b'],['TIKTOK','#d71920','#fff'],['YOUTUBE SHORTS','#0b2b4b','#fff']];
  rows.forEach((r,i)=>{rr(160,320+i*130,760,100,24,r[1]);text(r[0],540,383+i*130,40,r[2],true,'center')});
  text('Use the animated file, not the cover image.',540,800,28,'#64748b',true,'center');
  note.textContent='This tab lists where the animated video is used. The static Story / Cover tab is only the thumbnail companion.';
}
const FILES={fb:'facebook_page_1080',group:'facebook_group_1080',ig1:'instagram_carousel_1',ig2:'instagram_carousel_2',ig3:'instagram_carousel_3',ig4:'instagram_carousel_4',cover:'instagram_story_1080x1920',threads:'threads_1080'};
const NOTES={fb:'Facebook Page: square infographic, exact article URL in the post text.',group:'Facebook Group: same square; post the exact URL only where group rules allow.',ig1:'Carousel 1 of 4: hook.',ig2:'Carousel 2 of 4: who may qualify.',ig3:'Carousel 3 of 4: who is not eligible.',ig4:'Carousel 4 of 4: how it arrives and the exact story path.',cover:'Instagram Story / cover, 9:16 with platform-safe margins. Not the animated video.',threads:'Threads: square image plus the exact clickable URL in the post text.'};
const img=document.getElementById('creativeImg');
function draw(){const d=document.getElementById('download');
  if(mode==='video'){img.style.display='none';c.style.display='block';videoPanel();if(d){d.disabled=true;d.textContent='Animated video asset'}return}
  c.style.display='none';img.style.display='block';img.src='/secondsocial/out/medicare-90-payment/'+FILES[mode]+'.png';img.alt=NOTES[mode];note.textContent=NOTES[mode]+' Rendered from the campaign file; these are the exact files you post.';
  if(d){d.disabled=false;d.textContent='Download current PNG'}}
draw();

let captions={};const sel=document.getElementById('copySelect'),ta=document.getElementById('copyText');function setCopy(){ta.value=captions[sel.value]||''}sel.onchange=setCopy;fetch('/secondsocial/campaigns/medicare-90-payment.json',{cache:'no-store'}).then(r=>r.json()).then(d=>{captions=d.captions||{};sel.innerHTML='';Object.keys(captions).forEach(k=>{const o=document.createElement('option');o.textContent=k;sel.appendChild(o)});setCopy();renderLinks(d.linkPlacement||[]);gate()}).catch(()=>{ta.value='Could not load captions from the campaign file.'});document.getElementById('copyBtn').onclick=()=>navigator.clipboard.writeText(ta.value);document.getElementById('download').onclick=()=>{if(mode==='video')return;const a=document.createElement('a');a.download=FILES[mode]+'.png';a.href=img.src;a.click()};

const topical=[
 {title:'2027 Medicare Star Ratings',score:98,why:'Released Oct. 8; Open Enrollment starts Oct. 15',state:'recommended'},
 {title:'DME rule changes Oct. 15',score:96,why:'CMS rule starts Oct. 15',state:''},
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
let liveStatus=false,networksConnected=false,linksDone=false;
const PKG='med90-2026-10-11';
let saved=null;try{saved=localStorage.getItem('secondsocial.med90.approved')}catch(e){}
approve.checked=saved===PKG;
try{published.checked=localStorage.getItem('secondsocial.med90.published')==='1'}catch(e){}
function setArticlePill(ok){document.querySelectorAll('.js-article-pill').forEach(e=>{e.textContent=ok?'Article live':'Article not verified';e.className=e.className.replace(/\b(good|bad|gold)\b/g,'')+' '+(ok?'good':'bad')})}
async function checkLive(){liveBox.className='warn';liveBox.innerHTML='<b>Checking production article…</b>';try{const target='https://thesecondhalfguide.com/medicare-90-payment';const r=await fetch('/api/secondsocial/check-url?url='+encodeURIComponent(target),{cache:'no-store'});const data=await r.json();liveStatus=!!data.ok&&!data.noindex&&data.canonical===target&&data.finalOk;setArticlePill(liveStatus);if(liveStatus){liveBox.className='ok';liveBox.innerHTML='<b>Live article check passed.</b><div class="small">HTTP '+data.status+' · '+(data.title||'article found')+'</div>'}else{liveBox.className='err';liveBox.innerHTML='<b>Live article check failed.</b><div class="small">Publishing remains blocked.</div>'}}catch(e){liveStatus=false;setArticlePill(false);liveBox.className='err';liveBox.innerHTML='<b>Live article check unavailable.</b>'}gate()}
function renderLinks(list){
  const box=document.getElementById('linkPanel');box.innerHTML='';let saved={};
  try{saved=JSON.parse(localStorage.getItem('secondsocial.med90.links.'+PKG)||'{}')}catch(e){}
  list.forEach(it=>{const row=document.createElement('label');row.className='check linkrow';
    row.innerHTML='<input type="checkbox" data-id="'+it.id+'"><span><b>'+it.platform+'</b><div class="small">'+it.rule+'</div><div class="small muted">&#9744; '+it.check+'</div></span>';
    const cb=row.querySelector('input');cb.checked=!!saved[it.id];
    cb.onchange=()=>{saved[it.id]=cb.checked;try{localStorage.setItem('secondsocial.med90.links.'+PKG,JSON.stringify(saved))}catch(e){}updateLinks(list);gate()};
    box.appendChild(row)});
  updateLinks(list)}
function updateLinks(list){linksDone=list.length>0&&[...document.querySelectorAll('#linkPanel input')].every(i=>i.checked)}
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
  if(!linksDone){
    publish.disabled=true;
    state.className='err';
    state.innerHTML='<b>Publishing blocked.</b> Confirm every link placement above.';
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
approve.onchange=()=>{try{localStorage.setItem('secondsocial.med90.approved',approve.checked?PKG:'0')}catch(e){}gate()};
published.onchange=()=>{try{localStorage.setItem('secondsocial.med90.published',published.checked?'1':'0')}catch(e){}gate()};
publish.onclick=()=>{if(publish.disabled)return;alert('Publishing is ready to hand off to Metricool. Final scheduler wiring will execute the approved package when network connections are present.');};
checkLive();
loadConnections();
finish.onclick=()=>{if(!published.checked)return;chooser.classList.add('open');finish.disabled=true;document.getElementById('activeStatus').textContent='Published · ready to choose next';document.getElementById('activeStatus').className='pill good'};
document.getElementById('activateNext').onclick=()=>alert('Next-story activation stays locked until the current campaign is published and completed. Once connected, activating a story will start a fresh verification job before creative generation.');