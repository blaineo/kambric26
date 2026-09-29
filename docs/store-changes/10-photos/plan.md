# Batch 10 (🟢): home, About and Events photos

**Why 🟢:** only uploads to **Content → Files**. kambricgoods.com serves its own image copies and never reads Shopify Files (same as batch 02). The live-site diff still runs.

## Store change (`apply.py`)
Upload 16 images from the Replit export (`manifest.json`: source → Files name → alt text) via staged uploads, and create them as Files. `before.json` shows no existing Files with these names.

| Page | Section / block | Files name |
| --- | --- | --- |
| Home | Hero → Photo | `home-hero-background.png` |
| Home | Quote → Background | `home-founder-quote-background.jpg` |
| Home | Story → photos 1–3 | `home-story-kati-portrait.png`, `-painting.png`, `-laughing.png` |
| Home | Lookbook → looks 1–6 | `lookbook-01.jpg` … `lookbook-06.jpg` |
| About | Hero, Kati story, Daisy story, CTA banner | `about-hero-background.png`, `about-kati-portrait.png`, `about-daisy-portrait.jpg`, `about-closing-banner.jpg` |
| Events | Hero | `events-hero-background.jpg` |

Alt text matches the reference site and the alt already set in the templates. The decorative backgrounds (home hero, quote, About banner, Events hero) have empty alt, as on the current site.

## Theme change (`set_templates.py`, committed with the batch)
Sets each image setting in `templates/index.json`, `page.about.json` and `page.events.json` to `shopify://shop_images/<filename>` (the format the theme editor writes). This only affects our dev theme.

## Rollback
`git revert` the template commit, then `rollback.py` (fileDelete by the IDs in `apply-log.json`).

## Verify
Home, About and Events at 1440/390 show the photos; exactly one priority image per page; `page_check.py`; kambricgoods.com diff clean after 2 minutes.
