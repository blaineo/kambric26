# Batch 02: collection images (🟢)

**Goal:** upload the six exported collection images to **Content → Files** (with descriptive alt text) and attach them as **Card image** / **Header image** on Folklore, Psychedelics and Whimsy. OWNER_TASKS A2 item 3.

| Collection | Field | Source (export) | File name in Shopify | Size |
| --- | --- | --- | --- | --- |
| Folklore (`Collection/451384180970`) | Card image | `76bdc047…jpg` | collection-folklore-cover.jpg | 1288×1932 |
| Folklore | Header image | `a4d624d7…png` | collection-folklore-header.png | 2040×924 |
| Psychedelics (`Collection/451384148202`) | Card image | `4ae0a17c…jpg` | collection-psychedelics-cover.jpg | 2325×3487 |
| Psychedelics | Header image | `db14140a…png` | collection-psychedelics-header.png | 1776×632 |
| Whimsy (`Collection/451384213738`) | Card image | `52d857e4…png` | collection-whimsy-cover.png | 808×1100 ⚠️ small |
| Whimsy | Header image | `44ac7a54…png` | collection-whimsy-header.png | 2470×820 |

Alt text for each is in `manifest.json`.

**Before (`before.json`):** all three collections have no image, no card image and no header image; no Files with these names exist.

**Why it's 🟢:** Files aren't read by the live site, and `kambric.card_image` / `kambric.header_image` are new fields with no Storefront API access (batch 01). The live site's collection data (title, description, `collection.image`) is untouched: we do **not** set the native collection image.

**Expected result (Shopify-hosted site):** `/collections` cards show the card images; each collection page's header shows its header image (priority-loaded, the page's LCP). kambricgoods.com unchanged.

**Run:** `python3 apply.py` (stages, uploads, creates Files, waits until READY, sets the 6 fields; logs IDs to `apply-log.json`; aborts on any error), then `after.graphql` → `after.json`, then the live diff.

**Rollback:** `python3 rollback.py`: deletes the 6 field values and the 6 Files (IDs from `apply-log.json`). Store returns to before.json.

**Note:** the Whimsy card image is only 808 px wide; on high-density screens the card may look slightly soft. Fine for now; replace it with a larger original when you have one (edit the Card image field).
