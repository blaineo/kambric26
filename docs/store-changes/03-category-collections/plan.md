# Batch 03: category and sale collections (🔴, runs at cutover)

**Status:** prepared and dry-run tested on 2026-09-28; **run at cutover only** (OWNER_TASKS C2), after owner approval. Doing it early wouldn't save meaningful work: it's one scripted step either way, and the theme can't show unpublished collections. The owner chose one step at cutover.

**Why 🔴:** the live site reads the Online Store channel (`finding.md`), so publishing these makes them appear on kambricgoods.com as well as the Shopify-hosted site. At cutover that's intended.

**What it does** (`apply.py`): for each of Dresses, Kaftans, Coats, Swimwear, Accessories (rule *Product type = X*) and Sale (rule *compare-at price > 0*), each plus *tag ≠ hidden*:
`collectionCreate` (title, handle, template `category`/`sale`, description + search listing from `store-data/collection-copy.csv`), then `publishablePublish` to Online Store (`Publication/134219858154`). Sale gets **no description** and only a plain search title: its old promo copy is stale, and the owner writes new copy.

**Expected membership** (read-only check, `rule-check-products.json`): Dresses 4 (Kati, Jessie, Zadie, Arielle), Kaftans 1 (Esther), Coats 1 (Vera), Swimwear 1 (Margit), Accessories 2 (Bodie, Goldie), Sale 1 (Margit). Re-check before running if products changed.

**Run at cutover:** `python3 apply.py --dry-run` (review) → `python3 apply.py` → verify on the site → then add the category links to the menus (batch 04b).

**Rollback:** `python3 rollback.py` deletes the created collections (IDs in `apply-log.json`); none existed before (`before.json`).
