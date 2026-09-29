# Parity pass: kambric26 vs kambricgoods.com

**Method (2026-09-29):** full-length captures of 18 page pairs (live site vs dev theme) at 1440 and 390 px, reduced motion, with Shopify's cookie banner and preview bar blocked. Compared side by side, then checked with computed-style probes. Scripts: scratchpad `parity/shoot2.mjs`, `compose.mjs`, `probe.mjs` (Playwright + installed Chrome). Re-run after each round of fixes.

Pages: home, shop (`/shop` vs `/collections/all`), collections index, Folklore, Margit (multi-print), Arielle, Kati (single-print), About, Events, Journal, a journal post, Contact, Wholesale, Size Guide, Shipping, Returns, empty cart, 404.

## ✅ Fixed in this pass

| Area | Gap | Fix |
| --- | --- | --- |
| Everywhere | Text looked thinner and dimmer than live | Removed global `-webkit-font-smoothing: antialiased` (live uses the default) |
| Everywhere | 23 section rules (eyebrow and heading margins, colours, card price size) silently lost to the shared snippets on Shopify's CSS bundle order | `eyebrow`, `section-heading` (base + colour rules) and `price` use `:where()`, so a section's own class always wins |
| Home hero | Overlay strength, secondary CTA colour, faint outline-button border; model's head cropped | Source overlay colours/alphas; CTA colour specificity; solid border; `picture.liquid` ignores Shopify's default 50/50 focal point so the section's position applies |
| Cards | Arielle cards led with the studio shot | Print image rule: file name before variant image (as live) |
| Shop / category | "1 piece"; products alphabetical | Count fixed (filter-order bug); groups list oldest first (live's API order) |
| Collection pages | "1 piece"; hero count included other collections' prints; "Spring 2024 2024"; Arielle not first | Count fixed and scoped to the collection; season no longer repeats the year; Arielle pinned first (as live) |
| `/collections` | Order; heading 76px vs 48px | Creation order; `index` heading size |
| Shop / Journal headings | 76px vs 56px | `page` heading size (48 → 56px) |
| About | Kati/Daisy photos invisible (zero height); italic line colour; values band boxed | 4:5 frame; `--color-hero-accent` (hsl 34 44% 62%); full-width band |
| Events | Heading 76px vs 120px; hero spacing; hosting band boxed | Source heading clamp and gaps; full-width band |
| Info pages | Breadcrumb said "Contact \| Kambric Goods"; text sizes/colours; button size and spacing | Breadcrumb uses the page title; Info.tsx type scale; new `--space-14` |
| Marquee | Wrapped into a tall block under reduced motion | Stays one still, clipped row (as live) |

Verified after the fixes: About hero 682 px (= live), Events within 16 px, Wholesale text positions within a few px, Folklore/Shop orders and counts identical to live.

## 🔧 Still to fix (theme, small)

1. **Home, "From the Collections" at 390:** live wraps the heading onto two lines with "View all pieces" on the right; ours is one line with the link below.
2. **Journal index at 1440:** live grid is full-bleed (wider cards); ours sits in the page container.
3. **Journal post at 1440:** live text column and cover image are narrower (~656 px).
4. **About:** eyebrow "— The Archive" has a leading rule on live; the closing CTA banner is taller with a lighter overlay on live.
5. **Events at 390:** heading breaks "Where / to find us" (live: "Where to find / us").
6. **Footer at 390:** link rows a little taller than live.

## ⏳ Blocked until cutover (store data, 🔴)

- **Shop dropdown, category tabs on Shop, footer "Shop" column** (Dresses … Sale): need the category/sale collections, which appear on kambricgoods.com the moment they're published (batch 03, C2). The footer column currently shows the `footer` menu's Search / Your Privacy Choices.
- **Collection descriptions on Shop** (live uses code-owned copy): the Description field is shared with the live site (C2).
- **"Terms of Service" in the footer bar:** Settings → Policies is shared with checkout (🔴).
- **Whimsy is empty on both sites:** its prints still say `botanicals` in `kambric.prints` (data fix at cutover).

## ❓ Owner decisions (intentional differences from live)

| # | Difference | Why it's different | Options |
| --- | --- | --- | --- |
| P-1 | Visible breadcrumbs (Home › Collection › Product) on collection, product, page, blog pages; live shows "Shop · Collection · Product" on products and a plain "Collections" eyebrow elsewhere | Planned for SEO (BreadcrumbList) in Phase 1 | Keep; or match live wording/visibility and keep only the JSON-LD |
| P-2 | Season eyebrow ("Spring 2024") on collection pages; live shows "Collections" | Phase 3 brief (from `kambric.season`) | Keep; or switch the setting off (Customize → collection hero → Show season) |
| P-3 | Product specs list (Fabric, Neckline, …) from Shopify's category metafields; live doesn't show them | AEO: specs as real text | Keep; or hide |
| P-4 | Size guide as a real table; live shows text rows | AEO requirement (CLAUDE.md) | Keep (recommended) |
| P-5 | Newsletter pop-up is off; live shows "Take 15% off" after a delay | Off by default until you choose | Turn on in Customize (footer group → Newsletter pop-up); sign-ups create real customers |
| P-6 | Hero copy fade-in on home (live does the same) holds back LCP by ~1 s | Parity | Keep, or shorten the delays for performance |
