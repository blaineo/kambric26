"""
Page QA checker for Shopify theme dev server.

Usage:
  python3 page_check.py [--base http://127.0.0.1:9292] [--json] PATH [PATH ...]
  python3 page_check.py --preset all

For each path, performs automated QA checks including status codes, Liquid errors,
JSON-LD validation, image attributes, and more. Outputs a summary table or JSON.
Exit code 1 if any row fails, else 0.
"""

import argparse, json, re, sys, urllib.parse, urllib.request, html as html_module


def fetch_page(url, timeout=30):
    """Fetch page with custom User-Agent, following redirects."""
    req = urllib.request.Request(url, headers={"User-Agent": "kambric26-page-check"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            return response.status, response.geturl(), response.read().decode('utf-8', errors='replace')
    except urllib.error.HTTPError as e:
        # Error pages (e.g. the theme's 404) still have a body worth checking.
        return e.code, url, e.read().decode('utf-8', errors='replace')
    except (urllib.error.URLError, TimeoutError) as e:
        return None, url, ""


def check_page(url):
    status, final_url, html = fetch_page(url)
    if status is None:
        return {"url": url, "status": "ERROR", "final_url": final_url}

    parsed = urllib.parse.urlparse(final_url)
    final_path = parsed.path + ("?" + parsed.query if parsed.query else "")
    result = {"url": url, "status": status, "final_url": final_path, "verdict": "PASS", "reasons": []}

    # Upload failure check
    if "Failed to Upload Theme Files" in html:
        result["upload_fail"] = True
        result["verdict"] = "FAIL"
        result["reasons"].append("Upload failed")
        return result
    result["upload_fail"] = False

    # Liquid errors
    liquid = len(re.findall(r"Liquid (?:error|syntax error)", html, re.IGNORECASE))
    result["liquid_errors"] = liquid
    if liquid > 0:
        result["verdict"] = "FAIL"
        result["reasons"].append(f"Liquid errors: {liquid}")

    # Missing translations
    missing = len(re.findall(r"translation missing", html, re.IGNORECASE))
    result["missing_translations"] = missing
    if missing > 0:
        result["verdict"] = "FAIL"
        result["reasons"].append(f"Missing translations: {missing}")

    # Title
    title_match = re.search(r'<title[^>]*>(.+?)</title>', html, re.IGNORECASE | re.DOTALL)
    title = (re.sub(r'\s+', ' ', title_match.group(1)).strip() if title_match else "")
    result["title"] = html_module.unescape(title)

    # Meta tags
    desc_match = re.search(r'<meta\s+[^>]*name=["\']?description["\']?[^>]*content=["\']?([^"\'>\s]+)', html, re.IGNORECASE)
    result["meta_description"] = len(desc_match.group(1)) if desc_match else 0
    robots_match = re.search(r'<meta\s+[^>]*name=["\']?robots["\']?[^>]*content=["\']?([^"\'>\s]+)', html, re.IGNORECASE)
    result["robots"] = robots_match.group(1) if robots_match else ""
    canonical_match = re.search(r'<link[^>]*rel=["\']?canonical["\']?[^>]*href=["\']?([^"\'>\s]+)', html, re.IGNORECASE)
    result["canonical"] = canonical_match.group(1) if canonical_match else ""

    # H1 count
    h1 = len(re.findall(r'<h1[\s>]', html, re.IGNORECASE))
    result["h1"] = h1
    if h1 != 1:
        result["verdict"] = "FAIL"
        result["reasons"].append(f"h1 count: {h1} (expected 1)")

    # Images
    images = []
    for match in re.finditer(r'<img\s+([^>]*)', html, re.IGNORECASE):
        attrs = match.group(1)
        images.append({
            "width": bool(re.search(r'width=["\']?([^"\'\s>]+)', attrs, re.IGNORECASE)),
            "height": bool(re.search(r'height=["\']?([^"\'\s>]+)', attrs, re.IGNORECASE)),
            "has_alt": bool(re.search(r'alt=["\']([^"\']*)["\']', attrs, re.IGNORECASE)),
            "fetchpriority": (m.group(1) if (m := re.search(r'fetchpriority=["\']?([^"\'\s>]+)', attrs, re.IGNORECASE)) else None)
        })

    # Priority images
    priority = sum(1 for img in images if img.get("fetchpriority") == "high")
    result["priority_images"] = priority
    if priority > 1:
        result["verdict"] = "FAIL"
        result["reasons"].append(f"Priority images: {priority} (expected ≤ 1)")

    # Images without dimensions
    img_no_dims = sum(1 for img in images if not (img.get("width") and img.get("height")))
    result["img_without_dims"] = img_no_dims
    if img_no_dims > 0:
        result["verdict"] = "FAIL"
        result["reasons"].append(f"Images without dims: {img_no_dims}")

    # Images without alt
    img_no_alt = sum(1 for img in images if not img.get("has_alt"))
    result["img_without_alt"] = img_no_alt
    if img_no_alt > 0:
        result["verdict"] = "FAIL"
        result["reasons"].append(f"Images without alt: {img_no_alt}")

    # JSON-LD
    jsonld_types = []
    for match in re.finditer(r'<script\s+type=["\']application/ld\+json["\'][^>]*>(.+?)</script>', html, re.IGNORECASE | re.DOTALL):
        try:
            data = json.loads(match.group(1))
            if isinstance(data, dict) and "@type" in data:
                jsonld_types.append(data["@type"])
            elif isinstance(data, list):
                for item in data:
                    if isinstance(item, dict) and "@type" in item:
                        jsonld_types.append(item["@type"])
        except:
            jsonld_types.append("INVALID")
    result["jsonld"] = jsonld_types
    if "INVALID" in jsonld_types:
        result["verdict"] = "FAIL"
        result["reasons"].append("Invalid JSON-LD")

    # Status code
    expected_404 = url.endswith("/this-page-does-not-exist")
    if status != 200 and not (status == 404 and expected_404):
        result["verdict"] = "FAIL"
        result["reasons"].append(f"Status {status}")

    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", default="http://127.0.0.1:9292", help="Base URL")
    parser.add_argument("--json", action="store_true", help="Output JSON")
    parser.add_argument("--preset", choices=["all"], help="Use preset paths")
    parser.add_argument("paths", nargs="*", help="Paths to check")

    args = parser.parse_args()
    paths = (
        ["/", "/collections", "/collections/all", "/collections/folklore", "/collections/psychedelics", "/collections/whimsy",
         "/products/margit-one-piece", "/products/arielle-dress", "/products/zadie-linen-dress", "/products/bodie-scarf-in-twilight-plumes",
         "/cart", "/search?q=dress", "/pages/contact", "/pages/contact?view=about", "/pages/contact?view=events", "/pages/contact?view=size-guide",
         "/blogs/news", "/this-page-does-not-exist", "/shop"]
        if args.preset == "all" else args.paths
    )

    results = [check_page(args.base + path) for path in paths]

    if args.json:
        print(json.dumps(results, indent=2))
    else:
        print(f"{'Path':<35} {'Verdict':<6} {'H1':<3} {'Prio':<5} {'JSON-LD':<25} {'Title':<50}")
        print("-" * 130)
        for r in results:
            title = r.get("title", "")[:50]
            jsonld = "+".join(r.get("jsonld", [])) if r.get("jsonld") else ""
            print(f"{r['url']:<35} {r['verdict']:<6} {str(r.get('h1', '')):<3} {str(r.get('priority_images', '')):<5} {jsonld:<25} {title:<50}")
        for r in results:
            if r["verdict"] == "FAIL":
                print(f"\n{r['url']}: {', '.join(r['reasons'])}")

    sys.exit(1 if any(r["verdict"] == "FAIL" for r in results) else 0)


if __name__ == "__main__":
    main()
