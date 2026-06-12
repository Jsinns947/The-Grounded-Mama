# The Grounded Mama

Warm, honest, science-backed maternal-wellness guides — and the sales landing page that sells them. Written by a certified postpartum & child-development professional and mother of three.

## Project structure

```
the-grounded-mama/
├─ index.html   # single-file sales landing page (vanilla HTML/CSS/JS)
├─ guides/                  # the 6 final guide PDFs (gitignored — products, not source)
├─ src/                     # build scripts
│  ├─ guide6_content.py     #   EQ Toolkit manuscript (structured content)
│  ├─ build_guide6.py       #   builds the EQ Toolkit PDF (fpdf2 + DM Sans)
│  └─ swap_bylines.py       #   rebrands existing guide covers → "The Grounded Mama" (PyMuPDF)
└─ marketing/
   └─ SEO-PACK.md           # SEO/AI-SEO: titles, metas, slugs, keywords, FAQ + schema
```

## Products & live Gumroad links

| Guide | Price | Link |
|---|---|---|
| 🌙 Sleep Reset | $27 | gumroad.com/l/rvajzd |
| 🪞 Identity Reset | $27 | gumroad.com/l/hpovjii |
| 🧸 Toddler Discipline | $47 | gumroad.com/l/jjorif |
| 📵 Screen Detox | $27 | gumroad.com/l/tdmrb |
| 🌈 EQ Toolkit | $47 | gumroad.com/l/xbshe |
| 💚 Postpartum Recovery | $47 | gumroad.com/l/tgndlv |
| **Fourth Trimester Bundle** (Sleep+Identity+Postpartum) | $79 | gumroad.com/l/mhytk |
| **Gentle Parenting Bundle** (Toddler+Screens+EQ) | $89 | gumroad.com/l/lmjnz |
| **Complete Library** (all 6) | $147 | gumroad.com/l/gvxxty |

Buy buttons on the landing page link to these via the `LINKS` map in the page's `<script>`. Single-guide buttons show an upsell to the relevant bundle before checkout.

## Run locally

```bash
python -m http.server 8000 --directory the-grounded-mama
# then open http://localhost:8000/index.html
```

## Deploy

Static site, no build step. **Cloudflare Pages** (recommended):

1. Cloudflare dashboard → **Workers & Pages → Create → Pages → Connect to Git** → pick `Jsinns947/The-Grounded-Mama`.
2. Build settings → **Framework preset: None**, **Build command: blank**, **Build output directory: `/`**. Save & Deploy.
3. Live at `https://<project>.pages.dev` in ~1 min; every `git push` auto-deploys.

**Custom domain:** Pages project → Custom domains → add your domain, then find-replace `https://thegroundedmama.com` in `index.html`, `robots.txt`, `sitemap.xml`, `llms.txt`.

Cloudflare/SEO files included: `_headers`, `robots.txt`, `sitemap.xml`, `llms.txt`, `404.html`.

## Notes

- The 6 guide PDFs are **gitignored** to keep paid products out of version control.
- Images currently load from Unsplash; for production, swap in curated/licensed images or the Unsplash API (see comments in the HTML).
