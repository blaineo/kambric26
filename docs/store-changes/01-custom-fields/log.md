# Batch 01 log: custom-field definitions ✅ done

- **Approved:** owner, 2026-09-28 ("approve batch 01").
- **Store:** 7u2dfq-xf.myshopify.com (Shop 71406846186), verified in before.json.
- **Applied:** started 2026-09-28T20:55:14Z.

| Step | Result | IDs (for rollback) |
| --- | --- | --- |
| Definition `kambric.archive_label` (product) | created | `MetafieldDefinition/81135534314` |
| Definition `kambric.card_image` (collection) | created | `MetafieldDefinition/81135567082` |
| Definition `kambric.header_image` (collection) | created | `MetafieldDefinition/81135599850` |
| Definition `seo.hidden` (product) | created (the `seo` namespace accepted a definition) | `MetafieldDefinition/81135632618` |
| Arielle `archive_label` = "Parlor Rose" | set | `Metafield/37404735471850` |
| Monogram `seo.hidden` = 1 | set | `Metafield/37404735504618` |

**Verified**
- Admin `after.json`: 4 new definitions, 2 values, nothing else changed.
- Shopify-hosted site: Arielle's page shows "Parlor Rose Archive Print"; the product sitemap lists Arielle and no longer lists the monogram fee.
- **kambricgoods.com:** `live-after.json` vs `live-before.json`: **no change** (8 endpoints incl. `/api/monogram`). The first timed check was interrupted by a usage-limit pause; the diff ran later, well after the 2-minute webhook window.

**Rollback (if ever needed):** `rollback.graphql` (delete the 2 values), then `metafieldDefinitionDelete(id, deleteAllAssociatedMetafields: true)` for each ID in `rollback-vars.json`.
