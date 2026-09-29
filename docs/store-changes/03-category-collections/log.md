# Batch 03 + 03b log: category and sale collections, menus ✅ (cutover step, 2026-09-29)

- **Approved:** owner, 2026-09-29 ("I'm going to publish now, go ahead and start making the changes"). 🔴: publishing to Online Store shows the collections on kambricgoods.com.
- **03 (collections):** Claude's run was blocked by the Claude Code auto-mode safety check, so the **owner ran** `apply.py` (`! python3 …/apply.py`): created + published `dresses`, `kaftans`, `coats`, `swimwear`, `accessories`, `sale` (IDs in `apply-log.json`). Verified: templates `category`/`sale`, one publication each (Online Store).
- **03b (menus, Claude, `apply-menus.py`):** `main-menu` Shop → Dresses, Kaftans, Coats, Swimwear, Accessories, Sale; `shop-categories` → All + 5 categories; `footer` → 5 categories + Sale ("Search" dropped); `footer-info` → + "Your Privacy Choices" (moved from `footer`). Before-state in `menus-before.json`; result in `menus-apply-result.json`.
- **Theme:** `collection.json` / `collection.category.json` category strip now uses menu `shop-categories` (dev theme; push to live pending owner go-ahead).

**Verified (Shopify-hosted, live theme Kambric26):** all six pages 200, one H1, SEO titles from the copy sheet; header Shop dropdown and footer Shop column list the six; piece counts equal kambricgoods.com's category pages (Dresses 7, Kaftans 3, Coats 2, Swimwear 8, Accessories 2, Sale 6).

**kambricgoods.com (expected change):** at 16:34:26Z `/api/collections` gained exactly the six new collections, plus their six endpoints and sitemap entries; folklore/psychedelics/whimsy, `/api/products`, `/api/product-redirects`, `/api/monogram` unchanged.

**Rollback:** `rollback-menus.py` (menus), then `rollback.py` (deletes the six collections by ID).
