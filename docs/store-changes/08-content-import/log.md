# Batch 08 log: content import ✅ done

- **Approved:** owner, 2026-09-28 ("approve batch 08"), after re-authenticating with `write_content, write_metaobject_definitions, write_metaobjects`.
- **Applied:** 2026-09-29T05:55Z; `apply.py` exit 0, no userErrors. All created IDs are in `apply-log.json`.

| Created / changed | IDs |
| --- | --- |
| Pages about, events, wholesale, size-guide, shipping, returns | 114867831018, 114867863786, 114867896554, 114867929322, 114867962090, 114867994858 |
| Page contact (updated: title "Contact Us", body, SEO) | 113644699882 (previous state in `before-contact.json`) |
| Blog `journal` | 94613962986 |
| Articles where-kambric-began, first-look-ss27, arielle-dress, chainstitch, gearing-up-for-dallas | 590518747370, 590518780138, 590518812906, 590518845674, 590518878442 |
| Metaobject definition `kambric_event` | 7286161642 |
| Events (3) | 188747317482, 188747350250, 188747383018 |
| Menus updated | `main-menu` (+ Story, Events, Journal), `footer-info` (5 pages) |

**Verified**
- Admin `after.json`: 8 pages published with the expected templates; `journal` has 5 posts, each with cover image, original publish date and one tag; 3 events (the definition's `metaobjectsCount` lagged at 1 right after creation, while the list query returned all 3); both menus as planned.
- Shopify-hosted site: all 7 pages, `/blogs/journal` and posts return 200; `/about` and `/journal/<slug>` redirect correctly; the header shows Shop, Collections, Story, Events, Journal and the footer shows the Information links. `page_check.py`: the 19 preset pages plus 8 new ones all PASS (one H1 each; Event ×3 and Article JSON-LD).
- **kambricgoods.com:** `live-after.json` vs `live-before.json`: **no change** (8 endpoints), re-checked after the 2-minute window.

**Rollback (if ever needed):** `python3 rollback.py` (`--dry-run` first).
