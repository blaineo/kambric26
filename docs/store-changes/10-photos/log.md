# Batch 10 log: photos ✅ done

- **Approved:** owner, 2026-09-29 ("approve batch 10"). **Store:** Shop 71406846186 (checked by apply.py).
- **Applied:** 2026-09-29T06:04Z; 16 Files created, all READY with the planned filenames and alt text.
  (The first run's CDN-filename parse was wrong; `apply-log.json` was corrected from a read-only query and `apply.py` fixed.)

| File | MediaImage id |
| --- | --- |
| `home-hero-background.png` | `34839559176426` |
| `home-founder-quote-background.jpg` | `34839559209194` |
| `home-story-kati-portrait.png` | `34839559241962` |
| `home-story-kati-painting.png` | `34839559274730` |
| `home-story-kati-laughing.png` | `34839559307498` |
| `lookbook-01.jpg` | `34839559340266` |
| `lookbook-02.jpg` | `34839559373034` |
| `lookbook-03.jpg` | `34839559405802` |
| `lookbook-04.jpg` | `34839559438570` |
| `lookbook-05.jpg` | `34839559471338` |
| `lookbook-06.jpg` | `34839559504106` |
| `about-hero-background.png` | `34839559536874` |
| `about-kati-portrait.png` | `34839559569642` |
| `about-daisy-portrait.jpg` | `34839559602410` |
| `about-closing-banner.jpg` | `34839559635178` |
| `events-hero-background.jpg` | `34839559667946` |

**Theme:** `set_templates.py` set the 16 image settings in `templates/index.json`, `page.about.json`, `page.events.json` (`shopify://shop_images/…`).

**Found while verifying:** Shopify reports a default focal point (`50.0% 50.0%`) for every new file, and `snippets/picture.liquid` wrote it inline, overriding each section's own image-position setting (the hero cropped the model's head). The snippet now ignores the default focal point.

**Verified**
- Home 11, About 4, Events 1 photos render; one priority image per page; `page_check.py` PASS on all three.
- **kambricgoods.com:** `live-after.json` vs `live-before.json` at 06:07:18Z: **no change** (8 endpoints).

**Rollback:** `git revert` the template commit, then `python3 rollback.py` (fileDelete by the IDs above).
