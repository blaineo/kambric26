# Batch 20: product photo descriptions (alt text) 🟢

**Requested:** owner, 2026-10-09 ("draft the descriptions as a batch"). Drafted by Claude from the photos; the owner (and shop owner) review `descriptions.csv`.

## What changes
Alt text on the **102 photos** of the 9 active products with images (`fileUpdate`, one field). Nothing else.
- **Multi-print products** (Margit, Zadie, Esther, Vera): `<current print alt> | <description>`, e.g. `Magnolia | Back view showing the sash tied at the back and the side slit, Magnolia matte viscose kaftan`. The part before ` | ` is the existing alt, so every photo stays with its print.
- **Single-print products and Arielle** (blank alt today; Arielle groups by file name): just the description.
- Style: what the view shows first (front/back/close-up/flat shot, the detail it shows), then print + fabric + garment. Fabric wording comes from the product descriptions (silk viscose, organic linen, recycled nylon, ...).

## Order (important)
1. **Owner pushes the theme first** (commit 51543db: `product-gallery`, `product-print-media`, `print-summary`, `meta-tags`, `share-image`, `en.default.json`). The old live code would show the whole `Print | description` string and stop grouping by alt. `apply.py` refuses to run until the live product page shows the new alt format.
2. Owner approves ("approve batch 20"), with any edits made directly in `descriptions.csv` (`new_alt` column).
3. `python3 apply.py` (stops if any alt changed since `before.json`).
4. `python3 gallery_check.py snapshot gallery-after.json && python3 gallery_check.py diff gallery-before.json gallery-after.json`: every print must show the same photos as before; the new alts are listed.

## Files
- `before.json`: products, media IDs, current alts, variants (2026-10-09)
- `make_csv.py`: the drafts → `descriptions.csv` (re-run after editing drafts there; or edit the CSV directly)
- `descriptions.csv`: handle, photo number, media ID, file, current alt, **new alt**
- `dry-run.txt`: `apply.py --dry-run` output
- `gallery-before.json`: which photos each print's gallery shows on kambricgoods.com now
- `rollback.py`: restores every `current_alt`

## Notes for review
- Kati #4: I read the coat over her shoulder as the Vera coat in Matyó Floral.
- Esther #17 also shows a second model in a solid ivory kaftan (not a listed print).
- Arielle #5 and #10 are print swatches (not shown in the gallery today; described for completeness).
- Kati's *Fabric* field says Viscose; the descriptions follow the product copy ("silk viscose").
