# Batch 11 (🟢): newsletter pop-up photo

**Why 🟢:** uploads one image to **Content → Files**; kambricgoods.com never reads Shopify Files (same as batches 02 and 10). Live-site diff still runs.

- **Store:** upload `newsletter-signup-popup.jpg` (the current site's pop-up photo, export `uploads/57e0fcb8-….jpg`, 2 MB), empty alt (decorative, as on the live site). `before.json`: no File with that name.
- **Theme:** `set_templates.py` sets `sections/footer-group.json` → `newsletter_popup.image` to `shopify://shop_images/newsletter-signup-popup.jpg`.
- **Rollback:** `git revert` the theme commit, then `rollback.py` (fileDelete by the ID in `apply-log.json`).
- **Verify:** pop-up shows the photo after 6 s; `page_check.py`; live diff clean after 2 minutes.
