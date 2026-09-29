# Batch 12 log: print collections `botanicals` → `whimsy` ✅ (2026-09-29)

- **Approved:** owner, 2026-09-29 ("please do"), after the explanation of the empty Whimsy page.
- **Scope changed from OWNER_TASKS C2 on purpose:** only `"collection": "botanicals"` → `"whimsy"`; the plan's "delete the key for Zadie/Esther/Vera" was dropped. With the category collections now published, a key-less print falls back to the product's *first* collection, which could become Dresses/Kaftans/Coats; explicit keys can't. Esther and Vera already had correct keys and weren't touched.
- **Applied:** 2026-09-29T17:01:53Z, `metafieldsSet` on `kambric.prints`: margit-one-piece (1 entry), zadie-linen-dress (3), and drafts linen-napkins (2), linen-tea-towel (2), linen-tablecloth (1). Original values in `before.json`.
- **Context:** DNS had already moved (kambricgoods.com → Shopify 23.227.38.65, serving Kambric26), so there was no separate live site to diff; `live-before.json` couldn't be taken (the Replit API is no longer on the domain).
- **Verified on kambricgoods.com:** Whimsy 4 cards (Margit Wildflowers, Zadie ×3); Folklore 9, Psychedelics 9, Shop 22 unchanged; no product still references `botanicals`.

**Rollback:** `python3 rollback.py` (writes the `before.json` values back).
