# Batch 15 log: product data for Google free listings ✅ (2026-09-29)

- **Approved:** owner ("go ahead and batch them all, I will have the shop owner make edits where necessary").
- **Applied:** 2026-09-29T18:49Z. Before-state in `before.json`, after-state in `after.json`, actions in `apply-log.json`.

| Product | Category (Google) | Fabric (drafted) | Color / pattern (drafted) |
| --- | --- | --- | --- |
| Kati Slip Dress | Dresses (unchanged) | Viscose | Floral, Red |
| Jessie Slip Dress | **Dresses** (was Uncategorized) | Viscose | Blue, Floral |
| Bodie Scarf | **Scarves & Shawls** (was none) | Silk, Cotton | Blue, Floral |
| Goldie Bandana | **Bandanas & Headties** (was none) | Cotton | Floral, Red |
| Margit One-Piece | One-Piece Swimsuits (unchanged) | Nylon, Lycra | Geometric, Floral |
| Esther Kaftan | **Kaftans** (was none) | Viscose | Geometric, Floral |
| Zadie, Vera, Arielle | unchanged | unchanged | unchanged |

- New taxonomy entries created: Fabric **Nylon**, **Lycra**; Color **Blue**.
- **SKUs** on all 106 variants: `KG-<PRODUCT>-<PRINT>-<SIZE>` (e.g. `KG-MARGIT-DAHLIA-XS`, `KG-ESTHER-GOODVIBES-XS-S`, `KG-BODIE-TWILIGHT`, `KG-MONOGRAM`). No duplicates.
- **For the shop owner to review:** the fabric/color values were drafted from the product descriptions ("silk viscose" was read as Viscose; Margit's "recycled nylon/spandex" as Nylon + Lycra). Correct them under each product → *Category metafields*. Category changes can affect tax in some states; confirm with whoever handles tax.
- **Rollback:** `python3 rollback.py` (clears the SKUs, deletes the fields set, restores the 4 categories, deletes Nylon/Lycra/Blue).
