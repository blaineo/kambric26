#!/usr/bin/env python3
"""Mobile Lighthouse for the theme's key pages, summarised against the definition of done.

Runs `npx lighthouse@12` (mobile emulation, headless Chrome) on the Shopify-hosted preview of a
theme and blocks Shopify's preview bar, which customers never get, so the numbers approximate
production. Targets (CLAUDE.md): SEO 100, accessibility >= 95, performance >= 90, CLS < 0.05,
LCP < 2.5 s.

Usage:
  tools/lighthouse_pages.py --theme 145427988714 [--out DIR] [PATH ...]
  (no PATHs = the default set below)
"""
import argparse
import json
import os
import subprocess
import sys

STORE = "https://kambric-goods-2.myshopify.com"
DEFAULT_PATHS = [
    "/", "/collections", "/collections/all", "/collections/folklore",
    "/products/margit-one-piece", "/products/arielle-dress",
    "/cart", "/search?q=dress", "/pages/contact", "/blogs/news",
]
CATEGORIES = "performance,accessibility,seo,best-practices"


def run(path, theme, out_dir):
    sep = "&" if "?" in path else "?"
    url = f"{STORE}{path}{sep}preview_theme_id={theme}"
    name = path.strip("/").replace("/", "_").replace("?", "_").replace("=", "-") or "home"
    report = os.path.join(out_dir, f"{name}.json")
    subprocess.run(
        ["npx", "--yes", "lighthouse@12", url, "--quiet", "--chrome-flags=--headless=new",
         "--blocked-url-patterns=*preview-bar*", f"--only-categories={CATEGORIES}",
         "--output=json", f"--output-path={report}"],
        check=False, capture_output=True,
    )
    if not os.path.exists(report):
        return {"path": path, "error": "no report"}
    data = json.load(open(report))
    audits = data["audits"]
    scores = {k: round((v["score"] or 0) * 100) for k, v in data["categories"].items()}
    failing = sorted({
        ref["id"] for cat in data["categories"].values() for ref in cat["auditRefs"]
        if ref.get("weight", 0) > 0 and audits[ref["id"]]["score"] is not None
        and audits[ref["id"]]["score"] < 0.9
        and ref["id"] not in ("first-contentful-paint", "largest-contentful-paint",
                              "speed-index", "total-blocking-time", "cumulative-layout-shift")
    })
    return {
        "path": path, **scores,
        "lcp": audits["largest-contentful-paint"]["numericValue"] / 1000,
        "cls": audits["cumulative-layout-shift"]["numericValue"],
        "tbt": audits["total-blocking-time"]["numericValue"],
        "failing": failing,
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--theme", required=True, help="preview theme id")
    ap.add_argument("--out", default="lighthouse-reports", help="folder for the JSON reports")
    ap.add_argument("paths", nargs="*")
    args = ap.parse_args()
    os.makedirs(args.out, exist_ok=True)
    rows = [run(p, args.theme, args.out) for p in (args.paths or DEFAULT_PATHS)]
    print(f"{'path':28} perf a11y  seo  bp    LCP    CLS   TBT  failing audits")
    for r in rows:
        if "error" in r:
            print(f"{r['path']:28} ERROR {r['error']}")
            continue
        print(f"{r['path']:28} {r['performance']:4} {r['accessibility']:4} {r['seo']:4} {r['best-practices']:3}"
              f" {r['lcp']:5.1f}s {r['cls']:6.3f} {r['tbt']:5.0f}  {', '.join(r['failing'])}")
    json.dump(rows, open(os.path.join(args.out, "summary.json"), "w"), indent=1)


if __name__ == "__main__":
    sys.exit(main())
