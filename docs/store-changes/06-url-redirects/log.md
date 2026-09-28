# Batch 06 log: URL redirects ✅ done

- **Approved:** owner, 2026-09-28 ("approve batch 06"). **Store:** Shop 71406846186 (checked by apply.py). **Applied:** started 2026-09-28T21:35:24Z.
- **Result:** 67 created, **0 rejected** (IDs in `apply-log.json`); the store now has exactly 67 redirects (`after.json`).

**Verified on the Shopify-hosted site** (`curl`, all `301`):
| Old path | → |
| --- | --- |
| `/about` | `/pages/about` |
| `/journal/chainstitch` | `/blogs/journal/chainstitch` |
| `/collections/botanicals` | `/collections/whimsy` |
| `/shop/dresses` | `/collections/dresses` |
| `/products/8681284370666` (legacy per-print ID) | `/products/margit-one-piece?variant=46124605898986` (opens with **Dahlia Seed** selected) |
| `/products/8681284272362` (legacy product ID) | `/products/kati-slip-dress-in-matyo-floral` |
| `/products/margit-one-piece-in-dahlia-seed` (**draft** product handle) | `/products/margit-one-piece?variant=46124605898986` |
| `/products/zadie-linen-dress-in-wildflowers` (**draft** product handle) | `/products/zadie-linen-dress?variant=46124607373546` (opens with **Wildflowers**) |
| `/products/kati-slip-dress-in-sunset-plumes` | `/products/jessie-slip-dress-in-twilight-plumes` |
| `/api/sitemap.xml` | `/sitemap.xml` |

**Open question answered:** Shopify accepts **and fires** redirects on the handles of draft products, so the 18 old per-print drafts don't need archiving or renaming at cutover.

**kambricgoods.com:** `live-after.json` vs `live-before.json`: **no change** (8 endpoints, after the 2-minute window).

**Rollback (if ever needed):** `python3 rollback.py` bulk-deletes the 67 IDs in `apply-log.json`.
