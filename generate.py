from pathlib import Path
from html import escape as e
import json

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'docs'
data = json.loads((ROOT / 'content/site.json').read_text())
favicon = 'data:image/svg+xml,%3Csvg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"%3E%3Crect width="64" height="64" rx="12" fill="%23111111"/%3E%3Ctext x="32" y="43" text-anchor="middle" font-family="Arial,sans-serif" font-size="36" font-weight="bold" fill="%23ff7900"%3EE%3C/text%3E%3C/svg%3E'

def head(title, description):
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#111111"><title>{e(title)}</title><meta name="description" content="{e(description,quote=True)}"><meta property="og:title" content="{e(title,quote=True)}"><meta property="og:description" content="{e(description,quote=True)}"><meta property="og:type" content="website"><link rel="icon" href='{favicon}'><link rel="stylesheet" href="/style.css"></head><body><a class="skip" href="#main">Skip to content</a>'''

def nav():
    return '''<header class="wrap"><nav class="nav" aria-label="Main navigation"><a class="wordmark" href="/" aria-label="Ege Akgün home">ea<span>.</span></a><div class="nav-links"><a href="/#work"><small>01</small>Work</a><a href="/#mathematics"><small>02</small>Mathematics</a><a href="/#about"><small>03</small>About</a><a class="nav-contact" href="mailto:egekgn@berkeley.edu">Get in touch ↗</a></div></nav></header>'''

def footer():
    return f'''<footer class="wrap footer"><div><div class="footer-name">Ege Akgün</div><div class="footnote">Berkeley, California · 2026</div></div><div class="footer-links"><a href="mailto:{data['email']}">Email ↗</a><a href="{data['github']}" rel="noopener noreferrer" target="_blank">GitHub ↗</a><a href="{data['linkedin']}" rel="noopener noreferrer" target="_blank">LinkedIn ↗</a></div></footer></body></html>'''

def project_card(p, featured=False):
    inner = f'''<div class="project-top"><span><span class="project-number">{p['number']}</span>{e(p['organization'])}</span><span>{e(p['period'])}</span></div><h3>{e(p['title'])}</h3><p class="project-summary">{e(p['summary'])}</p><div class="project-bottom"><strong>{e(p['category'])}</strong><span class="project-open">View work <span aria-hidden="true">↗</span></span></div>'''
    metrics = f'''<div class="feature-metrics"><div class="feature-metric"><strong>{e(p['stat'])}</strong><span>{e(p['statLabel'])}</span></div><div class="feature-metric"><strong>{e(p['secondStat'])}</strong><span>{e(p['secondLabel'])}</span></div></div>'''
    return f'''<a class="project{' featured' if featured else ''}" href="/work/{p['slug']}/">{('<div>'+inner+'</div>'+metrics) if featured else inner}</a>'''

home = head('Ege Akgün — Mathematics, AI & Selected Work', 'Selected work in frontier AI mathematics, cryptography, quantitative research, and education. UC Berkeley. Two-time IMO silver medalist.') + nav()
home += f'''<main id="main"><section class="wrap hero" aria-labelledby="name"><div class="hero-top"><p class="eyebrow">Berkeley, California</p><p class="eyebrow">Mathematics · Research · Building</p></div><h1 id="name">Ege Akgün<span>.</span></h1><div class="hero-bottom"><div><p class="lead">{e(data['intro'])}</p><p class="sublead">{e(data['interests'])}</p><div class="intro-links"><a class="text-link" href="#work">Explore my work ↓</a><a class="text-link" href="mailto:{data['email']}">Get in touch ↗</a></div></div><div class="credentials"><div class="credential"><span class="label">Olympiads</span><strong>2× IMO silver · 2× BMO gold</strong></div><div class="credential"><span class="label">Previously</span><strong>Mercor · TÜBİTAK BİLGEM</strong></div><div class="credential"><span class="label">Now</span><strong>Mathematics & RL research at Berkeley</strong></div></div></div></section><section class="wrap section" id="work"><div class="section-head"><h2>Selected work</h2><span class="section-label">01 / PROJECTS & EXPERIENCE</span></div><div class="work-grid">'''
home += ''.join(project_card(p,i==0) for i,p in enumerate(data['projects']))
home += '''</div></section><section class="honors section" id="mathematics"><div class="wrap"><div class="section-head"><h2>A foundation in mathematics</h2><span class="section-label">02 / OLYMPIADS</span></div><div class="honors-grid"><article class="honor"><div class="honor-top"><span class="times">2×</span><span class="medal">Silver medal</span></div><h3>International Mathematical Olympiad</h3><p>Represented Türkiye in 2025 and 2026.</p><a class="text-link" href="https://www.imo-official.org/results/individual/country/TUR/" target="_blank" rel="noopener noreferrer">Official results ↗</a></article><article class="honor"><div class="honor-top"><span class="times">2×</span><span class="medal">Gold medal</span></div><h3>Balkan Mathematical Olympiad</h3><p>2025 and 2026. Second among official contestants in both editions.</p></article></div></div></section><section class="wrap section" id="about"><div class="about-layout"><div><p class="eyebrow">03 / ABOUT</p><h2>From mathematics<br>to research.</h2></div><div class="about-copy"><p>I study Applied Mathematics and Computer Science at UC Berkeley. My work spans mathematical reasoning, AI evaluation, cryptography, and quantitative research.</p><p>I have also co-organized a national olympiad mathematics camp and delivered more than 50 advanced lectures.</p><div class="education"><div class="education-row"><div><strong>University of California, Berkeley</strong><p>Applied Mathematics & Computer Science</p></div><time>2026 — Expected 2028</time></div><div class="education-row"><div><strong>TÜBİTAK Science High School</strong><p>Kocaeli, Türkiye</p></div><time>2021 — 2026</time></div></div></div></div></section></main>'''
(OUT/'index.html').write_text(home+footer())

for i,p in enumerate(data['projects']):
    page = head(p['title']+' — Ege Akgün',p['summary'])+nav()
    page += f'''<main id="main"><section class="wrap detail-hero"><a class="back" href="/#work">← Selected work</a><p class="eyebrow">{p['number']} / {e(p['category'])}</p><h1>{e(p['title'])}</h1><p class="lead">{e(p['summary'])}</p><div class="detail-meta"><div><span>Organization</span>{e(p['organization'])}</div><div><span>Role</span>{e(p['role'])}</div><div><span>Period</span>{e(p['period'])}</div></div></section><div class="wrap detail-body"><aside class="detail-aside" aria-label="Work at a glance"><div class="aside-stat"><strong>{e(p['stat'])}</strong><span>{e(p['statLabel'])}</span></div><div class="aside-stat"><strong>{e(p['secondStat'])}</strong><span>{e(p['secondLabel'])}</span></div></aside><article class="detail-article"><section><h2>My contribution</h2>'''
    page += ''.join('<p>'+e(s)+'</p>' for s in p['contribution'])
    page += f'''</section><section><h2>{e(p['challengeTitle'])}</h2><p>{e(p['challenge'])}</p></section><section><h2>{'Current stage' if p['slug']=='four-color-research' else 'Results & scope'}</h2><p>{e(p['outcome'])}</p>'''
    if p.get('results'):
        page += '<div class="table-scroll" role="region" aria-label="Reference backtest results" tabindex="0"><table class="results"><thead><tr><th scope="col">Strategy</th><th scope="col">Return</th><th scope="col">Sharpe</th><th scope="col">Max drawdown</th></tr></thead><tbody>'
        for row in p['results']:
            page += '<tr>'+''.join('<td>'+e(row[k])+'</td>' for k in ['strategy','return','sharpe','drawdown'])+'</tr>'
        page += '</tbody><caption>Reference test, August 2024–July 2025. Results reproduced in the linked repository.</caption></table></div>'
    page += '<p class="scope">'+e(p['scope'])+'</p></section>'
    if p.get('limitations'):
        page += '<section><h2>Limitations</h2><p>'+e(p['limitations'])+'</p></section>'
    if p['links']:
        page += '<div class="detail-links">'+''.join(f'''<a class="button" href="{e(link['url'],quote=True)}" target="_blank" rel="noopener noreferrer">{e(link['label'])}<span aria-hidden="true">↗</span></a>''' for link in p['links'])+'</div>'
    nxt=data['projects'][(i+1)%len(data['projects'])]
    page += f'''</article></div><div class="wrap detail-foot"><a class="next-work" href="/work/{nxt['slug']}/"><div><span>NEXT WORK</span><strong>{e(nxt['title'])}</strong></div><div aria-hidden="true">→</div></a></div></main>'''
    folder=OUT/'work'/p['slug']; folder.mkdir(parents=True,exist_ok=True)
    (folder/'index.html').write_text(page+footer())

(OUT/'404.html').write_text(head('Page not found — Ege Akgün','Return to the portfolio of Ege Akgün.')+nav()+'<main id="main" class="wrap detail-hero"><p class="eyebrow">404</p><h1>Page not found.</h1><p><a href="/">Return to selected work →</a></p></main>'+footer())
print('Generated homepage, 5 work pages, and 404 page.')
