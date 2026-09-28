# Batch 05 log: collection search listings ✅ done

- **Approved:** owner, 2026-09-28 ("approve batch 05"). **Store:** Shop 71406846186. **Applied:** started 2026-09-28T21:24:49Z; no userErrors.

| Collection | SEO title | Meta description |
| --- | --- | --- |
| Folklore | Folklore \| Kambric Goods | fuller copy from the old site's code |
| Psychedelics | Psychedelics \| Kambric Goods | fuller copy from the old site's code |
| Whimsy | Whimsy \| Kambric Goods | its own current Shopify description |

**Verified**
- Admin `after.json` vs `before.json`: **title and description unchanged byte-for-byte** on all three (the fields the live site reads); only `seo` changed.
- Shopify-hosted pages: `<title>` and meta description show the new values, with no doubled store name.
- **kambricgoods.com:** `live-after.json` vs `live-before.json`: **no change** (8 endpoints). The first, timed check never reached the site (the background job ran from the wrong folder, so the script path failed); it was re-run with absolute paths after the 2-minute window.

**Rollback (if ever needed):** `rollback.graphql` clears the three SEO fields back to empty.
