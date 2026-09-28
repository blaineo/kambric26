# Batch 04: menus (🟢)

**Only the Shopify-hosted theme reads Shopify menus**: kambricgoods.com's header and footer links are hard-coded in the Replit app (`liquid/content/navigation.json`), so menus can't affect it.

| Menu | Before (`before.json`) | After |
| --- | --- | --- |
| `main-menu` | Home · Catalog · Contact (`/pages/contact`) | **Shop** (→ `/collections/all`) · **Collections** (→ `/collections`) with **Psychedelics, Folklore, Whimsy** nested (collection links → the large italic dropdown) |
| `footer-info` | doesn't exist | created, **empty** (hidden in the footer) until the Phase 4 pages exist |
| `shop-categories` | doesn't exist | created with **All** (→ `/collections/all`) |
| `footer` | Search · Your Privacy Choices | **unchanged** (see below) |
| `customer-account-main-menu` | Orders · Profile | unchanged |

**Deferred:** the Shop dropdown (Dresses … Sale), the category links in `footer`/`shop-categories`, and Story/Events/Journal all point at pages or collections that don't exist yet → batch 04b at cutover / Phase 4.

**Footer menu left alone:** it holds Shopify's **"Your Privacy Choices"** link (`/pages/data-sharing-opt-out`), which Shopify adds for US state privacy laws. Before replacing the footer's items with the categories at cutover, we'll decide where that link lives (e.g. the Information column or the legal line) so it's never dropped.

**Main menu Contact link:** removed from the header (the current site has no Contact in its header; Contact moves to the footer's Information column in Phase 4). The `/pages/contact` page itself is untouched.

**Run:** `apply.graphql` with `--allow-mutations` → `apply-result.json` (record the 2 new menu IDs) → `after.graphql` (= before) → `after.json` → check the Shopify-hosted header/footer → live diff.

**Rollback:** `rollback.graphql` restores `main-menu`'s three original items, then `menuDelete` the two created menus.
