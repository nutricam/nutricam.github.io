#!/usr/bin/env python3
"""Generate the comparison and listicle pages from scripts/pages.py.

Usage: python3 scripts/build.py

Each page is one dict. The visible FAQ and the FAQPage schema come from the
same list, so they cannot drift. Hand-written pages (home, what-is-nutricam,
what-should-i-eat-next, nutricam-vs-cronometer) are not touched.
"""
import json
import os

from build_helpers import esc
from pages import PAGES

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://nutricam.app"
APP_STORE = "https://apps.apple.com/us/app/nutricam-ai-nutrient-tracker/id6745231558"
OG_IMAGE = SITE + "/assets/App%20Store%20Screenshot%206.png"
REL = ' rel="noopener noreferrer"'
ORG = {"@type": "Organization", "name": "LAYERTWO, LLC", "url": SITE + "/"}

FOOT_LINKS = [
    ("/", "Home"),
    ("/what-is-nutricam/", "What is NutriCam?"),
    ("/what-should-i-eat-next/", "What should I eat next"),
    ("/best-ai-calorie-tracker-apps/", "Best AI calorie trackers"),
    ("/nutricam-vs-cronometer/", "NutriCam vs Cronometer"),
    ("/nutricam-vs-cal-ai/", "NutriCam vs Cal AI"),
    ("/cal-ai-alternatives/", "Cal AI alternatives"),
    ("/cronometer-alternatives/", "Cronometer alternatives"),
    ("/privacy.html", "Privacy"),
    ("/terms.html", "Terms"),
    (APP_STORE, "App Store"),
    ("mailto:support@nutricam.app", "Support"),
]


def schema(page):
    url = f"{SITE}/{page['slug']}/"
    graph = [
        {
            "@type": "Article",
            "@id": url + "#article",
            "mainEntityOfPage": url,
            "headline": page["h1"],
            "description": page["description"],
            "datePublished": page["published"],
            "dateModified": page["updated"],
            "author": ORG,
            "publisher": ORG,
            "image": OG_IMAGE,
            "about": [{"@type": "Thing", "name": n, "url": u} for n, u in page.get("about", [])],
        },
        {
            "@type": "SoftwareApplication",
            "@id": url + "#app",
            "name": "NutriCam: AI Nutrient Tracker",
            "operatingSystem": "iOS 16.4+",
            "applicationCategory": "HealthApplication",
            "downloadUrl": APP_STORE,
            "url": SITE + "/",
            "identifier": "id6745231558",
            "author": ORG,
            "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
            "availableOnDevice": "iPhone",
        },
        {
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "NutriCam", "item": SITE + "/"},
                {"@type": "ListItem", "position": 2, "name": page["h1"], "item": url},
            ],
        },
        {
            "@type": "FAQPage",
            "@id": url + "#faq",
            "mainEntity": [
                {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
                for q, a in page["faq"]
            ],
        },
    ]
    if page.get("item_list"):
        graph.append(
            {
                "@type": "ItemList",
                "name": page["h1"],
                "itemListElement": [
                    {"@type": "ListItem", "position": i, "name": name, "url": link}
                    for i, (name, link) in enumerate(page["item_list"], 1)
                ],
            }
        )
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, indent=2, ensure_ascii=False)


def render(page, css, analytics):
    url = f"{SITE}/{page['slug']}/"
    title, desc = esc(page["title"]), esc(page["description"])
    sections = "\n".join(
        f'<section class="{"wrap-wide" if s.get("wide") else "wrap"}"><h2>{s["h2"]}</h2>\n{s["html"]}\n</section>'
        for s in page["sections"]
    )
    faq = "\n".join(
        f'<details{" open" if i == 0 else ""}><summary>{esc(q)}</summary><p class="a">{esc(a)}</p></details>'
        for i, (q, a) in enumerate(page["faq"])
    )
    sources = "".join(f'<li><a href="{esc(u)}" rel="noopener noreferrer">{esc(n)}</a></li>' for n, u in page["sources"])
    foot = "\n".join(
        f'<a href="{esc(h)}"{REL if h.startswith("https://") else ""}>{esc(t)}</a>'
        for h, t in FOOT_LINKS
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>{title}</title>
    <meta name="description" content="{desc}">
    <link rel="canonical" href="{url}">
    <meta name="robots" content="index,follow">
    <meta name="author" content="LAYERTWO, LLC">
    <meta property="og:type" content="article">
    <meta property="og:locale" content="en_US">
    <meta property="og:url" content="{url}">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{desc}">
    <meta property="og:image" content="{OG_IMAGE}">
    <meta property="og:site_name" content="NutriCam">
    <meta property="article:modified_time" content="{page['updated']}">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title}">
    <meta name="twitter:description" content="{desc}">
    <meta name="twitter:image" content="{OG_IMAGE}">
    <link rel="icon" href="../assets/icon.png">
    <script type="application/ld+json">
{schema(page)}
    </script>
    <style>
{css}
        .updated {{ color: var(--muted); font-size: 0.9rem; margin-bottom: 1.5rem; }}
        .sources {{ color: var(--ink-soft); font-size: 0.95rem; padding-left: 1.2rem; }}
        section ul, section ol {{ padding-left: 1.2rem; margin: 0 0 1rem; }}
        section li {{ margin-bottom: 0.45rem; }}
        h3 {{ font-size: 1.15rem; letter-spacing: -0.02em; margin: 1.6rem 0 0.5rem; }}
    </style>
{analytics}
</head>
<body>
    <a class="skip" href="#content">Skip to content</a>
    <header class="site-header">
        <a class="logo" href="/">
            <img src="../assets/icon.png" alt="">
            NutriCam
        </a>
    </header>

    <main id="content">
        <header class="wrap">
            <p class="eyebrow">{esc(page['eyebrow'])}</p>
            <h1>{esc(page['h1'])}</h1>
            <p class="lede">{page['lede']}</p>
            <p class="updated">Updated <time datetime="{page['updated']}">{esc(page['updated_label'])}</time> · Written by LAYERTWO, the makers of NutriCam. {page['disclosure']}</p>
            <div class="cta-row">
                <a class="btn btn-primary" href="{APP_STORE}" rel="noopener noreferrer" id="download-ios-button">
                    Download NutriCam on the App Store
                    <span class="mark" aria-hidden="true">↗</span>
                </a>
                <a class="btn btn-secondary" href="/what-is-nutricam/">
                    Read what NutriCam is
                    <span class="mark" aria-hidden="true">→</span>
                </a>
            </div>
        </header>

{sections}

        <section class="wrap faq" id="faq">
            <h2>FAQ</h2>
{faq}
        </section>

        <section class="wrap">
            <h2>Sources</h2>
            <p>Every fact about another app on this page comes from that app’s own site, help center, or store listing, checked {esc(page['updated_label'])}. Prices and features change. Check the live listing before you buy.</p>
            <ul class="sources">{sources}</ul>
        </section>
    </main>

    <footer class="site-footer">
        <p class="identity">NutriCam: AI Nutrient Tracker · LAYERTWO, LLC · App Store id6745231558 · iPhone only · nutricam.app</p>
        <nav class="foot-links" aria-label="Footer">
{foot}
        </nav>
    </footer>

    <script>
      document.getElementById("download-ios-button").addEventListener("click", function () {{
        if (window.posthog) posthog.capture("download_ios_button_clicked");
      }});
    </script>
</body>
</html>
"""


def main():
    with open(os.path.join(ROOT, "scripts", "page.css")) as f:
        css = f.read().rstrip()
    with open(os.path.join(ROOT, "scripts", "analytics.html")) as f:
        analytics = f.read().rstrip()
    for page in PAGES:
        out = os.path.join(ROOT, page["slug"], "index.html")
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, "w") as f:
            f.write(render(page, css, analytics))
        print("wrote", os.path.relpath(out, ROOT))


if __name__ == "__main__":
    main()
