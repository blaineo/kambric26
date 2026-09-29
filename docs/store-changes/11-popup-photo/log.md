# Batch 11 log: pop-up photo ✅ done

- **Approved:** owner, 2026-09-29 ("approve batch 11"). **Store:** Shop 71406846186 (checked by apply.py).
- **Applied:** 2026-09-29T07:16Z; 1 File created, READY: `newsletter-signup-popup.jpg` (MediaImage `34839684481258`), empty alt.
- **Theme:** `sections/footer-group.json` → `newsletter_popup.image` = `shopify://shop_images/newsletter-signup-popup.jpg`.

**Verified**
- Pop-up markup references the new file; `page_check.py` PASS on / and /pages/about.
- **kambricgoods.com:** `live-after.json` vs `live-before.json` at 07:18:36Z: **no change** (8 endpoints).

**Rollback:** `git revert` the theme commit, then `python3 rollback.py`.
