# Batch 04 log: menus ✅ done

- **Approved:** owner, 2026-09-28 ("approve batch 04"). **Store:** Shop 71406846186. **Applied:** started 2026-09-28T21:14:19Z.

| Menu | Result | ID |
| --- | --- | --- |
| `main-menu` | updated: Shop (→ /collections/all) · Collections (→ /collections) with Psychedelics, Folklore, Whimsy | `Menu/224754598122` (existing) |
| `footer-info` | created, empty | `Menu/226777202922` |
| `shop-categories` | created with All | `Menu/226777235690` |
| `footer` | unchanged (Search · Your Privacy Choices) | `Menu/224754630890` |

**Verified**
- Admin `after.json`: exactly the changes above.
- Shopify-hosted site: header Shop · Collections; dropdown lists the three collections in the serif italic style; "Collections" active on collection pages. Chrome at 1440: the toggle opens it (`aria-expanded` true), Escape and outside click close it, focus returns to the toggle. (An apparent "still visible after Escape" was a transition that hadn't painted in a background tab; after a paint it reads hidden.)
- **kambricgoods.com:** `live-after.json` vs `live-before.json`: **no change** (8 endpoints, after the 2-minute window).

**Rollback (if ever needed):** `rollback.graphql` restores main-menu's Home · Catalog · Contact, then `menuDelete` both IDs in `rollback-vars.json`.
