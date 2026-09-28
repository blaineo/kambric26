# Shopify URL Redirects Draft

Generated from `redirects.csv`, `current-urls.csv`, `products.json`, and MIGRATION_PLAN §4.1 rules (2026-09-28).

## Summary

| Category | Count | Notes |
| --- | --- | --- |
| **Static routes** | 25 | `/shop` → `/collections/all`, category paths, info pages, policies, blog, etc. |
| **Legacy numeric product IDs** | 25 | From `current-urls.csv` and `kambric.prints[].legacyId` |
| **Draft per-print handles** | 18 | DRAFT products matching `<merged-handle>-in-<print-slug>` (vera-coat, margit, esther, zadie). The 3 zadie-linen-dress-in-* rows were added in review: the linen skip rule had wrongly caught them |
| **Total** | **68** | |

## Skipped / Unresolved (14 items)

### Draft linen products (no active merged product) — 13 items
- `zadie-linen-dress-in-wildflowers`
- `zadie-linen-dress-in-candied-plaid`
- `zadie-linen-dress-in-cherry-coupe`
- `linen-napkins-in-retro-stripe`
- `linen-napkins-in-sunset-plumes`
- `linen-napkins-in-saffron-damask`
- `linen-napkins-in-amber-orchard`
- `linen-tea-towel-in-amber-orchard`
- `linen-tea-towel-in-saffron-damask`
- `linen-tea-towel-in-sunrise-plumes`
- `linen-tablecloth-in-saffron-damask`
- `linen-tablecloth-in-amber-orchard`
- `linen-tablecloth-in-sunrise-plumes`

**Reason:** No active merged product exists for these linen product lines.

### Draft vera-coat with unmatched print — 1 item
- `vera-coat-in-sunrise-plumes`

**Reason:** No "Sunrise Plumes" print exists in the active `vera-car-coat` merged product; redirects to `/products/vera-car-coat` (no variant).

## Query-String Sources (not importable)

Shopify URL redirects cannot have query-string sources. The following patterns from `redirects.csv` are **not included** in the import CSV; `/shop` → `/collections/all` covers the category redirects (low traffic):

| Pattern | Notes |
| --- | --- |
| `/shop?category=Dresses` | Covered by `/shop` → `/collections/all` |
| `/shop?category=Kaftans` | Covered by `/shop` → `/collections/all` |
| `/shop?category=Coats` | Covered by `/shop` → `/collections/all` |
| `/shop?category=Swimwear` | Covered by `/collections/all` |
| `/shop?category=Accessories` | Covered by `/collections/all` |
| `/products/{handle}?print={invalid-or-duplicate}` | Invalid print selection; theme JS handles cleanup |

## Next steps

**Draft.** Owner imports via **Online Store → Navigation → URL redirects → Import** at readiness step 4 (MIGRATION_PLAN §4.3).

**After import, verify:**
- Redirects fire for draft product handles (Shopify must fire redirects for 404 paths of draft products, or the draft handles must be archived/renamed first).
- A sample of 5–10 legacy numeric IDs resolve correctly.
- `/shop?category=*` URLs now land on `/collections/all` (fallback coverage).

## Technical notes

- The CSV uses path-only redirects (no domain); Shopify handles `www.` and trailing-slash normalization separately.
- Draft per-print product variants target the first available variant matching the Print/Colorway value, or the first variant with that value if none are available.
- Vera-coat draft products redirect to `vera-car-coat` (the active merged product handle, not the draft base name).
