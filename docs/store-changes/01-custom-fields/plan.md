# Batch 01: custom-field definitions (🟢)

**Goal:** create the fields the theme reads and set Arielle's archive label and the monogram's search-hiding flag. OWNER_TASKS A2 (items 1, 2, 4).

| # | Change | Record | Before (before.json) |
| --- | --- | --- | --- |
| 1 | Create product field `kambric.archive_label` (single-line text) | definition | doesn't exist |
| 2 | Create collection field `kambric.card_image` (file, images only) | definition | doesn't exist |
| 3 | Create collection field `kambric.header_image` (file, images only) | definition | doesn't exist |
| 4 | Create product field `seo.hidden` (integer) | definition | doesn't exist |
| 5 | Arielle Slip Dress (`Product/8721345642730`): `kambric.archive_label` = "Parlor Rose" | value | empty |
| 6 | Chainstitch Monogram (`Product/8690060460266`): `seo.hidden` = 1 | value | empty |

**Why it's 🟢:** the live site reads only `kambric.prints`, `print_name`, `print_story`, `season`, `year` through the Storefront API. These definitions are new keys with **no Storefront API access**, so they're invisible to it. `seo.hidden` affects only the Shopify-hosted sitemap and search; the live site's monogram lookup (`/api/monogram`) is added to the live diff to prove it.

**Expected result:** Arielle's page on the Shopify-hosted site shows "Parlor Rose Archive Print"; the monogram product disappears from `/sitemap.xml` on the Shopify-hosted site; nothing changes on kambricgoods.com.

**Run:** step 1 `apply-1-definitions.graphql`, then step 2 `apply-2-values.graphql` (`--allow-mutations`), then `after.graphql` (= before.graphql) → `after.json`.

**Rollback:** `rollback.graphql`: delete the two values, then `metafieldDefinitionDelete(deleteAllAssociatedMetafields: true)` for each definition ID recorded in `log.md`. Returns the store exactly to before.json (nothing existed).

**If `seo.hidden` can't have a definition** (reserved namespace), skip item 4 and set the value in step 2 without one; that's how Shopify documents it.
