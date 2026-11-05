# Ege Akgün — personal portfolio

A static personal homepage covering mathematics, AI evaluation, cryptography, quantitative research, and education. A white background, system serif typography, and muted burgundy links keep the focus on the writing. No build dependencies, external font requests, or paid services.

## Edit and preview

Edit the introduction and project information in `content/site.json`, then run `python3 generate.py`. The generated website and its assets live in `docs/`. Edit `docs/style.css` to change the visual design. The homepage links to five detailed work pages; existing project URLs are preserved.

Run `python3 -m http.server 4173 --bind 127.0.0.1 --directory docs` for a local preview.

## Publish

Publish this repository as `egeakgun/egeakgun.github.io`, with GitHub Pages configured to use the `main` branch and `/docs` folder. The website's intended address is `https://egeakgun.github.io/`. The address is live only after the GitHub Pages deployment succeeds.

Research in progress is labeled as such, and the crypto project reports limitations alongside its reference results.
