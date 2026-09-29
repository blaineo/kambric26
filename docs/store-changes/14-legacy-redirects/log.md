# Batch 14 log: Squarespace-era redirects ✅ (2026-09-29)

- **Approved:** owner ("approve batch 14").
- **Applied:** 2026-09-29T18:35:53Z, 40 `urlRedirectCreate` (IDs in `apply-log.json`) from `redirects.csv`: old `/home/p/…` products → the same current product and print (`?variant=`), discontinued scarves → Accessories, old `/home/…` categories → current collections, old info pages → current pages. Sources: live search results + Web Archive (basis column).
- **Not redirected:** the two linen napkin sets (no current equivalent: left 404 per Google's guidance), 2020-era Shopify products, `/summer-camp-2022`. **Held:** `/terms-conditions` → `/policies/terms-of-service` until the Terms policy exists (add it then).
- **Verified:** every path returns 301 to its target.
- **Rollback:** `python3 rollback.py`.
