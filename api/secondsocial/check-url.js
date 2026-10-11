module.exports = async function handler(req,res){
  try{
    const raw = (req.query && req.query.url) || '';
    if(!raw) return res.status(400).json({ok:false,error:'Missing url'});
    let u;
    try{u=new URL(raw)}catch{return res.status(400).json({ok:false,error:'Invalid url'})}
    if(u.hostname!=='thesecondhalfguide.com' && u.hostname!=='www.thesecondhalfguide.com'){
      return res.status(400).json({ok:false,error:'Only TheSecondHalfGuide.com URLs are allowed'});
    }
    const controller=new AbortController();
    const timer=setTimeout(()=>controller.abort(),8000);
    const r=await fetch(u.toString(),{method:'GET',redirect:'follow',signal:controller.signal,headers:{'user-agent':'SecondHalfGuide-SECONDSOCIAL/1.0'}});
    clearTimeout(timer);
    const text=await r.text();
    const titleMatch=text.match(/<title[^>]*>([^<]+)<\/title>/i);
    const canonicalMatch=text.match(/<link[^>]+rel=["']canonical["'][^>]+href=["']([^"']+)["']/i);
    const noindex=/<meta[^>]+name=["']robots["'][^>]+content=["'][^"']*noindex/i.test(text);
    return res.status(200).json({
      ok:r.ok,
      status:r.status,
      finalUrl:r.url,
      title:titleMatch?titleMatch[1].trim():null,
      canonical:canonicalMatch?canonicalMatch[1]:null,
      noindex,
      hasArticleSignals:/article|story|checked|sources/i.test(text)
    });
  }catch(e){
    return res.status(500).json({ok:false,error:e && e.name==='AbortError'?'Timeout':'Check failed'});
  }
};