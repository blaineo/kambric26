# Batch 13 log: search tags ✅ (2026-09-29)

- **Approved:** owner ("approve batch 13").
- **Applied:** 2026-09-29T18:09:52Z, `tagsAdd` only (nothing removed). Added per product (`apply-log.json`):
  Kati + Goldie: Matyó Floral, Matyo Floral, Folklore · Jessie + Bodie: Twilight Plumes, Folklore · Margit: Matyo Floral, Psychedelics, Folklore, Whimsy · Zadie: Whimsy · Esther: Psychedelics · Vera: Matyo Floral, Folklore · Arielle: Parlor Rose, Folklore.
- **Why:** Shopify search ignores custom fields (single-print names, archive labels) and collection names; tags are indexed. The unaccented "Matyo Floral" lets part-typed "maty" match (Shopify doesn't accent-fold prefixes).
- **Rollback:** `python3 rollback.py` (tagsRemove of exactly the added tags).
