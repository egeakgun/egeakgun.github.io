from pathlib import Path
from html import escape
from urllib.parse import quote
import json

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'docs'
DATA = json.loads((ROOT / 'content/site.json').read_text())
PROJECTS = {p['slug']: p for p in DATA['projects']}
RESEARCH = ['four-color-research', 'frontier-mathematics', 'encrypted-computation']
PROJECT_WORK = ['crypto-portfolio-ml', 'leva-math-camp']
ORDER = RESEARCH + PROJECT_WORK
ORIGIN = 'https://egeakgun.github.io'


def e(value):
    return escape(str(value), quote=True)


def head(title, description, path='/'):
    icon = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="10" fill="white"/><text x="32" y="46" text-anchor="middle" font-family="Georgia,serif" font-size="46" fill="#903d62">e</text></svg>'
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#ffffff">
<title>{e(title)}</title>
<meta name="description" content="{e(description)}">
<link rel="canonical" href="{ORIGIN}{e(path)}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(description)}">
<meta property="og:type" content="website">
<meta property="og:url" content="{ORIGIN}{e(path)}">
<link rel="icon" href="data:image/svg+xml,{quote(icon)}">
<link rel="stylesheet" href="/style.css">
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
<div class="page" id="top">
'''


def graph():
    # An original four-colored graph, a small nod to the research on this page.
    return '''<svg class="graph-sketch" aria-hidden="true" width="94" height="62" viewBox="0 0 94 62" fill="none"><g stroke="#aaa19f" stroke-width="1.3"><path d="M12 32 37 9 77 17 82 48 45 53 12 32 77 17 45 53 37 9 82 48"/></g><g stroke="white" stroke-width="2"><circle cx="12" cy="32" r="5" fill="#9b4f73"/><circle cx="37" cy="9" r="5" fill="#508371"/><circle cx="77" cy="17" r="5" fill="#bc974e"/><circle cx="82" cy="48" r="5" fill="#9b4f73"/><circle cx="45" cy="53" r="5" fill="#687fa5"/></g></svg>'''


def contact_links():
    return f'''<a href="{e(DATA['github'])}">github</a><span aria-hidden="true"> / </span><a href="{e(DATA['linkedin'])}">linkedin</a>'''


def footer():
    return f'''<footer class="footer"><span>Ege Akgün · Berkeley, California</span><a href="#top">back to top ↑</a></footer>
</div>
</body>
</html>'''


def entry(slug):
    p = PROJECTS[slug]
    direct = ''.join(f'<span aria-hidden="true"> · </span><a href="{e(link["url"])}">{e(link["label"])}</a>' for link in p['links'])
    return f'''<article class="entry">
<h3><a class="entry-title" href="/work/{e(slug)}/">{e(p['title'])}</a></h3>
<p class="entry-meta">{e(p['organization'])} · {e(p['period'])}</p>
<p>{e(p['home_summary'])}</p>
<p class="entry-links"><a href="/work/{e(slug)}/">more about this work</a>{direct}</p>
</article>
'''


current = e(DATA['home']['current'])
for text, slug in [
    ('reinforcement learning and graph coloring', 'four-color-research'),
    ('mathematical AI evaluation at Mercor', 'frontier-mathematics'),
    ('cryptography at TÜBİTAK BİLGEM', 'encrypted-computation'),
]:
    current = current.replace(e(text), f'<a href="/work/{slug}/">{e(text)}</a>')

home = head('Ege Akgün', 'Math, AI, research, and things I have worked on. Undergraduate at UC Berkeley; two-time IMO silver medalist.')
home += f'''<main id="main">
<header class="intro" id="about">
<h1>{e(DATA['name'])}</h1>
<p>{e(DATA['home']['opening'])}</p>
<p>{current}</p>
<p>{e(DATA['home']['personal'])}</p>
<div class="contact"><div><a class="email" href="mailto:{e(DATA['email'])}">egekgn [at] berkeley [dot] edu</a><p class="social-links">{contact_links()}</p></div>{graph()}</div>
</header>
<section class="home-section" id="research" aria-labelledby="research-title">
<h2 id="research-title">Research &amp; work.</h2>
<p class="section-intro">{e(DATA['home']['research_intro'])}</p>
{''.join(entry(slug) for slug in RESEARCH)}
</section>
<section class="home-section" id="mathematics" aria-labelledby="math-title">
<h2 id="math-title">Mathematics.</h2>
<p>I represented Türkiye at the International Mathematical Olympiad and competed at the Balkan Mathematical Olympiad.</p>
<ul class="honors-list">
<li><strong>International Mathematical Olympiad</strong> — silver medals, 2025 and 2026. <a href="https://www.imo-official.org/results/individual/country/TUR/">Official results</a></li>
<li><strong>Balkan Mathematical Olympiad</strong> — gold medals, 2025 and 2026. Second among official contestants in both editions.</li>
</ul>
</section>
<section class="home-section" id="work" aria-labelledby="projects-title">
<h2 id="projects-title">Projects &amp; teaching.</h2>
<p class="section-intro">{e(DATA['home']['projects_intro'])}</p>
{''.join(entry(slug) for slug in PROJECT_WORK)}
</section>
<section class="home-section education" aria-labelledby="education-title">
<h2 id="education-title">Education.</h2>
<p><strong>UC Berkeley</strong> · Applied Mathematics &amp; Computer Science<br><span class="muted">2026 — expected 2028</span></p>
<p><strong>TÜBİTAK Science High School</strong> · Kocaeli, Türkiye<br><span class="muted">2021 — 2026</span></p>
</section>
</main>
'''
OUT.mkdir(exist_ok=True)
(OUT / 'index.html').write_text(home + footer())

for index, slug in enumerate(ORDER):
    p = PROJECTS[slug]
    section = 'research' if slug in RESEARCH else 'work'
    section_name = 'research & work' if slug in RESEARCH else 'projects & teaching'
    page = head(p['title'] + ' — Ege Akgün', p['summary'], '/work/' + slug + '/')
    page += f'''<nav class="breadcrumb" aria-label="Breadcrumb"><a href="/">Ege Akgün</a><span aria-hidden="true"> / </span><a href="/#{section}">{section_name}</a></nav>
<main id="main" class="detail">
<header class="detail-header"><h1>{e(p['title'])}</h1><p class="entry-meta">{e(p['organization'])} · {e(p['period'])}</p><p>{e(p['summary'])}</p><p class="role">{e(p['role'])}</p></header>
<article class="detail-article">
<section><h2>What I worked on</h2>
{''.join('<p>' + e(text) + '</p>' for text in p['contribution'])}
</section>
<section><h2>{e(p['challengeTitle'])}</h2><p>{e(p['challenge'])}</p></section>
<section><h2>{'Where it stands' if slug == 'four-color-research' else 'Results & scope'}</h2><p>{e(p['outcome'])}</p>
'''
    if p.get('results'):
        page += '<div class="table-scroll" role="region" aria-label="Reference backtest results" tabindex="0"><table class="results"><caption>Reference test: August 2024–July 2025. Results reproduced in the linked repository.</caption><thead><tr><th scope="col">Strategy</th><th scope="col">Return</th><th scope="col">Sharpe</th><th scope="col">Max drawdown</th></tr></thead><tbody>'
        for row in p['results']:
            page += '<tr>' + ''.join('<td>' + e(row[key]) + '</td>' for key in ['strategy', 'return', 'sharpe', 'drawdown']) + '</tr>'
        page += '</tbody></table></div>'
    page += f'<p class="scope">{e(p["scope"])}</p></section>\n'
    if p.get('limitations'):
        page += f'<section><h2>Limitations</h2><p>{e(p["limitations"])}</p></section>\n'
    if p['links']:
        page += '<p class="detail-links">' + ' / '.join(f'<a href="{e(link["url"])}">{e(link["label"])}</a>' for link in p['links']) + '</p>\n'
    nxt = PROJECTS[ORDER[(index + 1) % len(ORDER)]]
    page += f'''</article>
<nav class="detail-end" aria-label="More work"><a href="/#{section}">← back to {section_name}</a><a href="/work/{e(nxt['slug'])}/">{e(nxt['title'])} →</a></nav>
</main>'''
    folder = OUT / 'work' / slug
    folder.mkdir(parents=True, exist_ok=True)
    (folder / 'index.html').write_text(page + footer())

(OUT / '404.html').write_text(head('Page not found — Ege Akgün', 'Return to Ege Akgün’s personal website.', '/404.html') + '<main id="main" class="detail"><h1>Page not found.</h1><p><a href="/">Back to my homepage →</a></p></main>' + footer())
print('Generated homepage, five work pages, and 404 page.')
