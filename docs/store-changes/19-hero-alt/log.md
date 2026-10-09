# Batch 19 log: home hero alt text on the file ✅ (2026-10-09)

- **Requested:** owner ("can we put the info in the shopify admin?").
- **Applied:** `fileUpdate` alt on `home-hero-background.png` (MediaImage 34839559176426): "" → "Arielle Slip Dress in Olive, worn in a field of teasels".
- **Theme:** `templates/index.json` hero `image_alt` cleared, so `sections/home-hero.liquid` uses the photo's own alt text (`s.image_alt | default: hero_image.alt`). A new hero photo brings its own description.
- **Rollback:** `fileUpdate` alt back to "" (and refill the section setting if needed).
