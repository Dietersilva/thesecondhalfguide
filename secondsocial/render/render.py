#!/usr/bin/env python3.13
"""Render /SECONDSOCIAL creative from a campaign JSON file.

usage: python3.13 secondsocial/render/render.py medicare-90-payment

One template set, one source of truth: the PNGs written to secondsocial/out/<id>/
are the exact files that get posted and the exact files the dashboard shows.
Fails (non-zero exit) if any automated check fails.
"""
import hashlib, html, json, sys, datetime, pathlib
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parents[2]
MIN_FONT = 26          # px on the 1080-wide canvas; smaller is unreadable on a phone
FONTS = ROOT / 'fonts'
e = html.escape

CSS = '''
@font-face{font-family:Atk;font-weight:400;src:url("file://%(f)s/atkinson-400.woff2")}
@font-face{font-family:Atk;font-weight:700;src:url("file://%(f)s/atkinson-700.woff2")}
@font-face{font-family:Fra;font-weight:700;src:url("file://%(f)s/fraunces-700.woff2")}
:root{--navy:#0b2b4b;--red:#c8161d;--gold:#f3b21a;--green:#12713f;--ink:#18212b;--muted:#4b5a6a;--paper:#f7f4ed;--line:#cfd9df}
*{box-sizing:border-box;margin:0;padding:0}
.page>*{flex:none}.page>.gap{flex:1 1 auto}
body{width:1080px;background:var(--paper);font-family:Atk,Arial,sans-serif;color:var(--ink);position:relative;overflow:hidden}
body:before{content:"";position:absolute;left:0;top:0;bottom:0;width:18px;background:var(--navy)}
.page{padding:36px 56px 0 64px;display:flex;flex-direction:column;height:100%%}
.badge{align-self:flex-start;background:var(--red);color:#fff;font-weight:700;font-size:30px;letter-spacing:.04em;padding:14px 28px;border-radius:10px}
.kicker{margin-top:18px;font-weight:700;font-size:28px;letter-spacing:.08em;color:var(--navy);text-transform:uppercase}
.rule{flex:none;width:240px;height:7px;background:var(--gold);margin-top:12px}
.hero{display:flex;align-items:baseline;gap:30px;margin-top:10px}
.hero b{font-family:Fra,serif;font-size:172px;line-height:.98;color:var(--red)}
.hero .l1{font-weight:700;font-size:52px;line-height:1.05;color:var(--navy);text-transform:uppercase}
.hero .l2{font-size:36px;color:var(--ink);margin-top:10px;display:block;text-transform:none;font-weight:400}
.stat{display:flex;align-items:center;gap:28px;border:2px solid var(--line);background:#fff;padding:12px 28px}
.stat b{font-family:Fra,serif;font-size:84px;line-height:1;color:var(--navy)}
.stat span{font-size:36px;font-weight:700;color:var(--ink);line-height:1.15}
.stat small{display:block;font-size:28px;font-weight:400;color:var(--muted);margin-top:4px}
.cols{display:grid;grid-template-columns:1fr 1fr;gap:36px}
.col h3{font-size:30px;letter-spacing:.06em;text-transform:uppercase;padding-bottom:8px;border-bottom:6px solid;margin-bottom:14px}
.col.y h3{color:var(--green);border-color:var(--green)}.col.n h3{color:var(--red);border-color:var(--red)}
.row{display:flex;align-items:center;gap:16px;font-size:32px;font-weight:700;color:var(--navy);line-height:1.15;margin:9px 0}
.ic{flex:none;width:44px;height:44px;border-radius:50%%;color:#fff;font-size:30px;line-height:44px;text-align:center;font-weight:700}
.y .ic{background:var(--green)}.n .ic{background:var(--red)}
.strip{background:#e8eef3;padding:12px 26px;display:grid;grid-template-columns:1fr 1fr 1fr;gap:20px}
.strip div{font-size:28px;line-height:1.2;color:var(--ink)}.strip b{display:block;font-size:30px;color:var(--navy);text-transform:uppercase;letter-spacing:.03em}
.foot{margin:auto -56px 0 -64px;padding:14px 56px 16px 64px;background:#fff;border-top:2px solid var(--line);text-align:center}
.foot .site{font-size:42px;font-weight:700;color:var(--navy)}
.foot .tag{font-size:28px;color:var(--navy)}
.foot .src{font-size:28px;font-weight:700;letter-spacing:.06em;color:var(--muted);margin-top:4px}
.gap{flex:1;min-height:20px}
.big .hero b{font-size:260px}.big .stat b{font-size:100px}
.slide{font-size:70px;font-weight:700;color:var(--navy);font-family:Fra,serif;line-height:1.1;margin-top:34px}
.sub{font-size:38px;margin-top:18px;line-height:1.25}
.num{position:absolute;right:56px;top:56px;color:#fff;font-weight:700;font-size:30px;background:var(--navy);padding:14px 22px;border-radius:10px}
.link{white-space:nowrap;background:var(--navy);color:#fff;font-size:32px;font-weight:700;text-align:center;padding:22px;border-radius:10px}
'''

def icon(ok): return '<span class="ic">%s</span>' % ('✓' if ok else '×')
def rows(items, ok): return ''.join('<div class="row">%s<span>%s</span></div>' % (icon(ok), e(i)) for i in items)

def footer(c, with_src=True):
    return ('<div class="foot"><div class="site">TheSecondHalfGuide.com</div><div class="tag">%s</div><div class="src">%s</div></div>'
            % (e(c['tagline']), e(c['trust'])))

def hero(c, big=False):
    return ('<div class="hero"><b>%s</b><div class="l1">%s<span class="l2">%s</span></div></div>'
            % (e(c['hero']), e(c['heroLabel']), e(c['heroSub'])))

def stat(c):
    s = c['stat']
    return '<div class="stat"><b>%s</b><span>%s<small>%s</small></span></div>' % (e(s['value']), e(s['label']), e(s['source']))

def timing(c):
    t = c['timing']
    return ('<div class="strip"><div><b>%s</b></div>' % e(c['noApplication']) +
            ''.join('<div><b>%s</b>%s</div>' % (e(x['head']), e(x['text'])) for x in t) + '</div>')

def cols(c):
    q, n = c['qualify'], c['notEligible']
    return ('<div class="cols"><div class="col y"><h3>%s</h3>%s</div><div class="col n"><h3>%s</h3>%s</div></div>'
            % (e(q['title']), rows(q['items'], True), e(n['title']), rows(n['items'], False)))

def page(inner, h, cls=''):
    return '<html><head><meta charset="utf-8"><style>%s</style></head><body class="%s" style="height:%dpx"><div class="page">%s</div></body></html>' % (CSS % {'f': FONTS}, cls, h, inner)

def square(c):
    return 1080, page('<div class="badge">%s</div><div class="kicker">The Second Half Guide · %s</div><div class="rule"></div>%s<div style="height:22px"></div>%s<div style="height:16px"></div>%s<div style="height:16px"></div>%s<div class="gap"></div>%s'
        % (e(c['badge']), e(c['kicker']), hero(c), stat(c), cols(c), timing(c), footer(c)), 1080)

def car1(c):
    return 1080, page('<div class="num">1/4</div><div class="badge">%s</div><div class="kicker">The Second Half Guide · %s</div><div class="rule"></div>%s<div style="height:30px"></div>%s<div class="gap"></div><div class="strip" style="grid-template-columns:1fr"><div><b>%s</b>%s</div></div><div class="gap"></div>%s'
        % (e(c['badge']), e(c['kicker']), hero(c), stat(c), e(c['noApplication']), e(c['otherRules']), footer(c)), 1080, 'big')

def car2(c):
    q = c['qualify']
    return 1080, page('<div class="num">2/4</div><div class="badge">%s</div><div class="slide">Who may qualify?</div><div class="sub" style="font-size:30px;color:var(--muted);margin-top:10px">%s</div><div class="gap"></div><div class="cols" style="grid-template-columns:1fr"><div class="col y"><h3>%s</h3><div style="font-size:0"></div>%s</div></div><div class="sub">%s</div><div class="gap"></div>%s'
        % (e(c['badge']), e(c['stat']['source']), e(q['title']), ''.join('<div class="row" style="font-size:56px;margin:44px 0;gap:26px">%s<span>%s</span></div>' % (icon(True), e(i)) for i in q['items']), e(c['otherRules']), footer(c)), 1080)

def car3(c):
    n = c['notEligible']
    return 1080, page('<div class="num">3/4</div><div class="badge">%s</div><div class="slide">Who is not eligible?</div><div class="sub" style="font-size:30px;color:var(--muted);margin-top:10px">%s</div><div class="gap"></div><div class="cols" style="grid-template-columns:1fr"><div class="col n"><h3>%s</h3>%s</div></div><div class="gap"></div>%s'
        % (e(c['badge']), e(c['stat']['source']), e(n['title']), ''.join('<div class="row" style="font-size:56px;margin:44px 0;gap:26px">%s<span>%s</span></div>' % (icon(False), e(i)) for i in n['items']), footer(c)), 1080)

def car4(c):
    items = c['arrives']
    return 1080, page('<div class="num">4/4</div><div class="badge">%s</div><div class="slide">How it arrives</div><div class="sub" style="font-size:30px;color:var(--muted);margin-top:10px">%s</div><div class="gap"></div>%s<div class="gap"></div><div class="link">Full story: %s</div><div style="height:28px"></div>%s'
        % (e(c['badge']), e(c['stat']['source']), ''.join('<div class="row" style="font-size:42px;margin:26px 0"><span class="ic" style="background:var(--gold);color:var(--navy)">•</span><span>%s</span></div>' % e(i) for i in items), e(c['_display']), footer(c)), 1080)

def story(c):
    # Instagram Story: keep key content between y=250 and y=1670 (UI overlays top and bottom ~250px)
    inner = ('<div style="height:210px"></div><div class="badge">%s</div><div class="kicker">The Second Half Guide \u00b7 %s</div><div class="rule"></div>%s<div class="gap"></div>%s<div class="gap"></div>%s<div class="gap"></div>%s<div class="gap"></div>%s'
        % (e(c['badge']), e(c['kicker']), hero(c), stat(c), cols(c), timing(c), footer(c).replace('class="foot"', 'class="foot" style="padding-bottom:270px;margin-top:0"')))
    return 1920, page(inner, 1920, 'big')

ASSETS = [('facebook_page_1080', square), ('facebook_group_1080', square), ('threads_1080', square),
          ('instagram_carousel_1', car1), ('instagram_carousel_2', car2), ('instagram_carousel_3', car3),
          ('instagram_carousel_4', car4), ('instagram_story_1080x1920', story)]

CHECK_JS = '''(min)=>{const out=[];const W=document.documentElement.clientWidth,H=document.body.clientHeight;
const els=[...document.querySelectorAll('body *')].filter(el=>[...el.childNodes].some(n=>n.nodeType===3&&n.textContent.trim()));
const boxes=[];
for(const el of els){const cs=getComputedStyle(el),r=el.getBoundingClientRect(),fs=parseFloat(cs.fontSize),t=el.textContent.trim().slice(0,40);
 if(fs<min)out.push('font '+fs+'px < '+min+': '+t);
 if(r.left<0||r.right>W||r.top<0||r.bottom>H)out.push('outside canvas: '+t);
 if(el.scrollWidth>el.clientWidth+1&&cs.display!=='inline')out.push('clipped: '+t);
 boxes.push([el,r,t]);}
for(let i=0;i<boxes.length;i++)for(let j=i+1;j<boxes.length;j++){const[a,ra,ta]=boxes[i],[b,rb,tb]=boxes[j];
 if(a.contains(b)||b.contains(a))continue;
 const ox=Math.min(ra.right,rb.right)-Math.max(ra.left,rb.left),oy=Math.min(ra.bottom,rb.bottom)-Math.max(ra.top,rb.top);
 if(ox>2&&oy>2)out.push('overlap: '+ta+' / '+tb);}
const foot=document.querySelector('.foot');if(foot){const fr=foot.getBoundingClientRect();for(const [el,r,t] of boxes){if(!foot.contains(el)&&r.bottom>fr.top+1)out.push('content runs into footer: '+t)}}
return out}'''

def main():
    cid = sys.argv[1]
    camp = json.load(open(ROOT / ('secondsocial/campaigns/%s.json' % cid)))
    c = dict(camp['content']); c['_display'] = camp['displayUrl']
    exp = camp.get('expires', {}).get('timing')
    if exp and datetime.date.today().isoformat() > exp:
        sys.exit('EXPIRED: timing wording expired %s. Update the campaign content first.' % exp)
    out = ROOT / 'secondsocial/out' / cid; out.mkdir(parents=True, exist_ok=True)
    manifest, failed = {}, False
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path='/opt/pw-browsers/chromium')
        for name, fn in ASSETS:
            h, doc = fn(c)
            pg = b.new_page(viewport={'width': 1080, 'height': h})
            tmp = out / ('_%s.html' % name); tmp.write_text(doc, encoding='utf-8')
            pg.goto('file://%s' % tmp); pg.evaluate('document.fonts.ready')
            issues = pg.evaluate(CHECK_JS, MIN_FONT)
            pg.screenshot(path=str(out / (name + '.png')), full_page=False)
            tmp.unlink(); pg.close()
            data = (out / (name + '.png')).read_bytes()
            manifest[name] = {'sha256': hashlib.sha256(data).hexdigest(), 'size': [1080, h], 'issues': issues}
            print(('FAIL ' if issues else 'ok   ') + name, *issues, sep='\n   ' if issues else '')
            failed |= bool(issues)
        b.close()
    manifest = {'campaign': cid, 'generated': datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds'), 'minFontPx': MIN_FONT, 'assets': manifest}
    (out / 'manifest.json').write_text(json.dumps(manifest, indent=2))
    sys.exit(1 if failed else 0)

main()
