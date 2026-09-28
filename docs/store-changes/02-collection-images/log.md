# Batch 02 log: collection images ✅ done

- **Approved:** owner, 2026-09-28 ("approve batch 02"). **Store:** Shop 71406846186 (checked by apply.py).
- **Applied:** started 2026-09-28T21:01:38Z; `apply.py` exit 0: 6 Files created (all READY), 6 fields set.

| Collection | Field | File (MediaImage id) | Metafield id |
| --- | --- | --- | --- |
| folklore | `card_image` | `34838741516522` (collection-folklore-cover.jpg) | `37404770566378` |
| folklore | `header_image` | `34838741549290` (collection-folklore-header.png) | `37404770599146` |
| psychedelics | `card_image` | `34838741582058` (collection-psychedelics-cover.jpg) | `37404770631914` |
| psychedelics | `header_image` | `34838741614826` (collection-psychedelics-header.png) | `37404770664682` |
| whimsy | `card_image` | `34838741647594` (collection-whimsy-cover.png) | `37404770697450` |
| whimsy | `header_image` | `34838741680362` (collection-whimsy-header.png) | `37404770730218` |

**Verified**
- Admin `after.json`: card and header set on all three collections; the native collection image is still unset (the live site reads that one); 6 Files READY with alt text.
- Shopify-hosted site: each collection page's header uses its header image as the page's single priority image; `/collections` cards use the card images.
- **kambricgoods.com:** `live-after.json` vs `live-before.json`: **no change** (8 endpoints, checked after the 2-minute window).

**Rollback (if ever needed):** `python3 rollback.py`: deletes the 6 field values, then the 6 Files (IDs from `apply-log.json`).
