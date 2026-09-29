## Home page (Phase 4)

### 🟢 Home page photos (Shopify-hosted only)
The theme can't pre-fill image settings, so the 11 home photos are uploaded once and picked in the editor. Uploading to **Content → Files** and editing the theme don't touch kambricgoods.com (the Replit site serves its own copies).

1. Upload these files from `~/Code/kambric/replit site/assets/` to **Content → Files** (rename as suggested so they're easy to find):

   | Upload | Suggested name | Pixels | Then pick it in Customize → Home page → |
   | --- | --- | --- | --- |
   | `uploads/9de4a6ef-2675-4b91-bc5f-78060918fc41.png` | `home-hero-background.png` | 1448 × 1086 | **Home hero → Photo** |
   | `uploads/cd6532ac-843e-4e91-adc6-fa25642756f1.jpg` | `home-founder-quote-background.jpg` | 1038 × 476 | **Quote → Background photo** |
   | `originals/IMG_8800_1780590151823.png` | `home-story-kati-portrait.png` | 1086 × 1448 | **Home story → Photo 1** |
   | `built/assets/kati_hands_painting-BmQNK_aL.png` | `home-story-kati-painting.png` | 1280 × 896 | **Home story → Photo 2** |
   | `originals/IMG_6961_1780589947013.png` | `home-story-kati-laughing.png` | 1086 × 1448 | **Home story → Photo 3** |
   | `originals/DSCF1744_Original_1779921553541.jpg` | `lookbook-01.jpg` | 2576 × 3864 | **Lookbook → Look 1** (No. 01) |
   | `originals/DSCF1600_Original_1779921553540.jpg` | `lookbook-02.jpg` | 2576 × 3864 | **Look 2** (No. 02) |
   | `originals/DSCF1931_Original_1779921553547.jpg` | `lookbook-03.jpg` | 3864 × 2576 | **Look 3** (No. 03) |
   | `originals/DSCF1688_Original_1779921260400.jpg` | `lookbook-04.jpg` | 1288 × 1932 | **Look 4** (No. 04) |
   | `originals/DSCF1680_Original_1779921307492.jpg` | `lookbook-05.jpg` | 2576 × 3864 | **Look 5** (No. 05) |
   | `originals/DSCF2023_Original_1779921246731.jpg` | `lookbook-06.jpg` | 1288 × 1932 | **Look 6** (No. 06) |

   Note the lookbook order: the source imports are named out of order (`lookbook3` = DSCF1744 is Look 01, etc.). The table follows what's shown on the site.
2. Alt texts and crop positions are already set on each block; no need to type them into Files.
3. **Check:** open the dev/unpublished theme's home page at 1440 px and 390 px and compare with `design/screenshots/home-1440.png` / `home-390.png`. kambricgoods.com is unchanged (nothing there reads Shopify Files).

Optional: the hero photo is only 1448 px wide (as on the current site), so it's slightly soft on large retina screens. A 2400 px+ original, and a portrait crop for **Home hero → Phone photo**, would improve it.

(Claude can do this batch for you through the store-changes process if you approve it: it's a Files upload plus theme-editor JSON, no shared data.)
