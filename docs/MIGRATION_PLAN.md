# Kambric Goods: Shopify theme migration plan (draft v0.1)

**Status:** first draft for owner review, 2026-09-28. Decisions are marked **⚠️ D-n** and collected in [§5](#5-open-decisions).
**Scope:** rebuild kambricgoods.com (React/Vite on Replit, Shopify Storefront API + checkout) as the Online Store 2.0 theme in this repo (`kambric26`), then cut over the domain.
**Owner checklist:** every owner/admin step from this plan, sorted by whether it can touch kambricgoods.com, lives in [`OWNER_TASKS.md`](./OWNER_TASKS.md).
**Environments:** kambricgoods.com (Replit) is live and reads catalog + checkout from the same store, so **catalog, collection-publication, metafield and checkout changes are shared and immediate**. The Shopify-hosted Online Store (`kambric-goods-2.myshopify.com`) is the playground: theme and Online-Store-only content work there is low risk. **Cutover = DNS**, once the Shopify-hosted site is production-ready. Blast-radius table: CLAUDE.md guardrail 1.
**Sources:** `../replit site/` (export) and `../liquid/` (Liquid supplement: 24 captured HTML pages, `SECTIONS.md`, `COMPONENTS.md`, `BEHAVIOR.md`, `SEO.md`, `content/`, and a read-only live Admin catalog audit in `shopify/`: 40 products (10 active, 30 draft), 4 collections, `DATA_ISSUES.md`).

Cross-cutting requirements for every phase: CLAUDE.md "Definition of done", **SEO/AEO**, **Core Web Vitals** (LCP < 2.5s, CLS < 0.05, INP < 200ms, mobile), and a `docs/CONTENT_GUIDE.md` update.

---

## 1. Theme build phases

### Phase 0: Foundation ✅ (this session)
Skeleton scaffold, repo hygiene, CLAUDE.md, design tokens, self-hosted fonts with metric-matched fallbacks, `picture` snippet (the responsive image standard), SEO head + Organization/WebSite JSON-LD, header/announcement/footer section groups, content guide.

### Phase 1: Global components
Parity targets: every screenshot's header and footer; `404-*`, `contact-*` (simplest pages) to prove the shell.
- Shared snippets: buttons (outline / text-arrow variants from the hero), eyebrow + ornament label, section heading (serif + italic "em" line, which replaces the `*italic*` convention), product card (with print swatch row), collection card, price (compare-at), rich-text wrapper (typography for journal/pages), breadcrumbs (visible + BreadcrumbList JSON-LD).
- Theme blocks (`blocks/`): text, heading, button, image (`picture`), group, reusable across later sections.
- `404` template matching `404-1440/390.png`.
- `templates/robots.txt.liquid`: keep Shopify defaults and add the current site's explicit AI-crawler allowances (GPTBot, ClaudeBot, PerplexityBot, Google-Extended, OAI-SearchBot).
- Verify on the dev theme: whether CDN `crop` honours the admin focal point (else prefer CSS `object-fit` + focal `object-position`, already emitted by `picture`).
- Performance baseline: Lighthouse mobile on home, product and collection shells, recorded in this doc.

**Phase 1 status (2026-09-28): built.** Snippets: `button`, `eyebrow`, `section-heading`, `rte`, `price`, `product-card` (standard/archive layouts), `product-prints` (print expansion + visibility guard; see its LiquidDoc for the calling pattern), `print-summary`, `print-swatches`, `collection-card`, `breadcrumbs`. Blocks: `heading`, `text`, `button`, `eyebrow`, `image`, `group`. `sections/404.liquid`, `templates/robots.txt.liquid`. Verified: Theme Check clean; card counts match the source (shop 22, psychedelics 9, sale 6). Still to do: Chrome check of the cards and 404 at 1440/390, and the Lighthouse baseline.
- **Wire in later:** `{% render 'breadcrumbs' %}` in the product, collection, article, page, blog, list-collections and search sections as they're built.
- **Remove before launch (dev-only previews):** `sections/phase1-{ui,cards,breadcrumbs}-preview.liquid`, `templates/index.phase1-ui.json`, `templates/collection.phase1-cards.json`, `templates/{product,collection}.phase1-breadcrumbs.json`.
- **Open from Phase 1:** keep the hover second image on cards (desktop only)? Card zoom uses the source values (1.05/1000ms standard, 1.04/700ms archive), not `--image-hover-scale`. Card image alt is empty (the link text names the product).

### Phase 2: Product page (highest risk)
**Decided:** D-7 `?variant=` + `?print=` fallback · D-9 linked cart lines · D-12 native notify form · D-22 `kambric.archive_label`. Draft redirect list: `docs/redirects-draft.csv`.
Parity: `product-1440/390.png`; `../liquid/html/product-{multi-print,single-print,arielle,monogrammable,sold-out-variant}.html`. Arielle has real `Colorway` × `Size` options: no special case.
- **Print model** (see SHOPIFY_DATA_MAP): merged products (option `Print`/`Colorway`) vs single-print (`kambric.print_name`/`print_story`); per-print data from `kambric.prints` JSON (`story`, `collection`, `featured`, `newArrival`, `legacyId`). **⚠️ D-6, D-7, D-8, D-14**
- Server-rendered first paint of the selected print (Liquid can't read `?print=`, so the default print is rendered and `<kg-product-form>` switches on load **without layout shift**: same-size gallery, preloaded first image). **⚠️ D-7**
- Size selection, per-print price/compare-at/availability, sold-out state and **back-in-stock** entry point. **⚠️ D-12**
- **Chainstitch monogram**: 10-character text + colour, fee product `chainstitch-monogram` (hidden) linked to the parent line; quantity and removal stay in sync. **⚠️ D-9**
- JSON-LD: extend `structured_data` output with brand, per-print `ProductGroup`/`hasVariant` (variesBy pattern/size), `BreadcrumbList`. AEO: size/fit/fabric/care as real text (`<dl>`), not images.
- LCP: first gallery image is `priority`; the rest lazy; thumbnails sized via `sizes`.

**Phase 2 status (2026-09-28): built.** `sections/main-product.liquid` (+ `templates/product.json`), `assets/component-product.js` (`<kg-product>`, `<kg-gallery>`; ~13 KB unminified), snippets `product-gallery`, `product-print-media`, `product-monogram`, `product-price`, `back-in-stock` (+ `component-back-in-stock.js`), `product-specs`. Verified on the dev theme: all product types render, one h1 and one priority image per page, ProductGroup + BreadcrumbList JSON-LD, clean canonicals, atomic garment+fee add (sold-out garment → 422, cart unchanged). Chrome pass pending.
- **Remove before launch:** `sections/phase2-components-preview.liquid`, `templates/product.phase2-components.json`.
- **Follow-ups:** align `print-summary` card image rule with the gallery (variant media + filename matches) so cards and galleries agree; optional `variesBy`/`url` in ProductGroup JSON-LD; visible breadcrumbs read "Home › Collection › Product" (source: "Shop · Collection · Product"), so confirm; after a print swap, `?variant=` preselects that print's first available size on reload.
- **Store data (owner):** create product metafield definition `kambric.archive_label` (single-line text), set "Parlor Rose" on Arielle (D-22).

### Phase 3: Collection, shop and category pages
**Architecture (2026-09-28):** shop page = `/collections/all` (Shopify can't assign it a template, so its sections switch on via a `show_on: all_only` setting in `collection.json`); category pages = automated collections using template **`collection.category`**; sale = automated collection using **`collection.sale`**; collection detail = default `collection.json`. Sections: `product-listing` (one section, merged 2026-09-28: a **Collection block** per collection on shop/category pages, drag to reorder; no blocks = single grid on collection/sale pages), `collection-hero`, `catalog-heading`, `category-nav` (menu `shop-categories`), `main-collections` (`/collections`), `text-cta`. Source's hard-coded "Arielle first" rule → a "Show these first" product list setting. Collection/category copy → `docs/store-data/collection-copy.csv` (owner pastes).
Parity: `shop-*`, `category-*`, `collection-index-*`, `collection-*`.
- `/collections` index with cover-image override metafield; collection page with header-image override; season/year eyebrow from `kambric.season`/`kambric.year`.
- **Per-print product cards** (merged products expand into one card per print, filtered to prints whose collection handle matches). **⚠️ D-17**
- Category pages = automated collections by product type. **⚠️ D-10**
- `/sale` = automated collection (compare-at price > price). Filters/sort via native Search & Discovery if needed.
- Exclusions everywhere: tag `hidden`, handle `chainstitch-monogram`, collection `frontpage`.
- JSON-LD: `CollectionPage` + `ItemList`, BreadcrumbList. First row of cards `eager`, rest `lazy`.

**Phase 3 status (2026-09-28): built.** Sections `product-listing` (grouped by collection blocks on shop/category pages; single grid on collection/sale pages), `collection-hero`, `catalog-heading`, `category-nav`, `main-collections`, `text-cta`; templates `collection.json`, `collection.category.json`, `collection.sale.json`, `list-collections.json`. Verified on the dev theme: card counts match the source (shop 22, dresses 7 simulated, psychedelics 9, sale 6 simulated); one h1 and one CollectionPage (+ nested ItemList) per page; titles match SEO.md ("Shop All", "Heritage Print Collections"). Home-collection lookup now skips `frontpage`, `all` and category/sale-template collections everywhere. Chrome pass and live category/sale tests are pending the store data.
- **Remove before launch:** `templates/collection.phase3-category-test.json`, `templates/collection.phase3-sale-test.json`.
- **Store data (owner):** create the category/sale collections and assign templates `category`/`sale` (§3a-A1 + collection-copy.md); create menu `shop-categories`; simplify per-print collections (§3 item 3; fixes the empty Whimsy page); set collection Card/Header images.
- **Open:** one collection description serves both the detail hero and the shop group text (the source used separate long copy for groups); keep one, or add a `kambric.group_description` metafield? Shop page emits CollectionPage JSON-LD (the source emitted none). Orphan group has no heading by default (source parity). Suggested helper to de-duplicate the "first available variant of a print" logic (print-swatches, both grids).

### Phase 4: Home, about, events, journal (+ info pages)
Parity: `home-*`, `about-*`, `events-*`, `journal-index-*`, `journal-post-*`, `wholesale-*`, `size-guide-*`, `contact-*`.
- **Home** (`index.json`): hero (image `priority`, mobile art-direction), marquee strip (reuses the announcement marquee CSS), new arrivals, story, quote band, lookbook (5-col/6-row composition), featured. Framer Motion entrances become CSS/`IntersectionObserver` reveal (reduced-motion safe, no CLS: transform/opacity only).
- **About** (`page.about.json`): hero, "On the name", Kati and Daisy story blocks, value cards (blocks, now add/remove/reorder), closing CTA.
- **Events** (`page.events.json`): upcoming/past split from the Events metaobject by date; Event JSON-LD per event. **⚠️ D-6b**
- **Journal**: blog `journal`, `article` template (cover `priority`, rich-text typography, related products from linked handles), `BlogPosting` JSON-LD, author/date `<time>`.
- **Info pages**: `page.json` rich text for contact/shipping/returns/wholesale (JOOR link + mailto); `page.size-guide.json` with table blocks (AEO: real `<table>` with `<caption>`, `scope`). Optional FAQ block → `FAQPage` JSON-LD only where visible.
- Policies: privacy/terms move to Shopify policies (`/policies/*`).

### Phase 5: Search, cart, newsletter pop-up
Parity: `cart-page-*`, `email-popup-*`, search overlay (rendered HTML).
- **Search overlay** `<kg-search>` using the native Predictive Search API (`/search/suggest.json`), with a full `/search` results page fallback (noindex). **⚠️ D-15**
- **Cart page** (the site has no drawer): Cart AJAX API for quantity/remove with monogram-line sync (D-9); header count updates via Section Rendering API.
- **Newsletter pop-up** `<kg-promo-popup>`: native `<dialog>`, 6s delay, dismissal in localStorage (`kambric_promo_dismissed`), native customer form, and no CLS (overlay only). **⚠️ D-11**
- Meta Pixel via the Meta sales channel app (no theme code). **⚠️ D-13**

---

## 2. Content model

All definitions below are **proposals**. Creating them is a store-data change: the developer writes the exact definitions, and the owner reviews and runs them.

| Content | Shopify home | Fields / notes | Source |
| --- | --- | --- | --- |
| Announcement | Section settings (header group) | enabled, text, CTA label, link, style | `data/settings.json` ✅ built |
| Home copy/images | `index.json` section settings/blocks | hero (image, mobile image, eyebrow, title, em-title, subtitle, 2 CTAs), story, quote image | `data/homepage.json` |
| About | `page.about.json` sections/blocks | all `about_content` fields; value cards → blocks | `data/about.json` |
| **Events** | Metaobject `kambric_event` | `title`, `start_date` (date, required for sorting + JSON-LD), `date_label` (text, e.g. "TBA"), `time_label` ("6–8pm"), `venue`, `city`, `description` (rich text), `image` (optional), `url` (optional). **Status is derived from the date**, with a manual override boolean for undated events. Hero image → section setting. | `data/events*.json` (3 + hero) |
| **Prints** | Metaobject `kambric_print` **⚠️ D-6** | `name` (= option value), `story` (rich text), `swatch` (image), `default_collection` (collection ref) | `kambric.prints`, `print_story`, local swatches |
| Product ↔ print data | Keep `kambric.prints` JSON (v1) **⚠️ D-6** | per-product: `value`, `collection`, `legacyId`, `featured`, `newArrival` | Shopify (existing) |
| **Journal** | Blog `journal` (articles) | title, handle = old slug, image = cover, excerpt, body HTML (from `body_html`), tags = category, published date | `data/journal-posts.json` (5) |
| Info pages | Pages: `contact`, `wholesale`, `size-guide`, `shipping`, `returns` | body rich text; size-guide tables | `liquid/content/hardcoded.json` (pending) |
| Policies | Settings → Policies | privacy, terms | hard-coded today |
| Collection images | Collection metafields `kambric.card_image`, `kambric.header_image` (file_reference, image) | overrides; fallback to Shopify collection image | `data/collections-extra.json` (6, 4 files missing) |
| Collection season/year | Existing `kambric.season`, `kambric.year` | no change | Shopify |
| Category intro/SEO | Collection description + SEO fields on the category collections (D-10) | | `categoryMeta.ts`, `Shop.tsx` copy |
| Menus | `main-menu`, `footer`, `footer-info` **⚠️ D-3** | | `liquid/content/navigation.json` (pending) |
| Newsletter subscribers | Customers (email marketing consent, tag `newsletter`) | import with consent state; 48 rows | DB (not exported, PII) |
| Back-in-stock requests | **⚠️ D-12** | 39 rows | DB (not exported, PII) |

---

## 3. Data cleanup (before or at cutover)

Owner-run changes, each written as a reviewed script/plan first:

From `../liquid/shopify/DATA_ISSUES.md` (live audit 2026-09-28) plus the export. ⚠️ = **shared with the live Replit site**: stage these so they don't break it before cutover.

1. ~~Arielle uses `Size` as its colorway~~ **Resolved:** the live Admin record already has `Colorway` [Terracotta, Olive] × `Size` [2XS–2XL] (14 variants). The theme treats Arielle like any other multi-print product, with no special case. Only its images still rely on the old app's filename matching; fold that into item 2.
2. ⚠️ **Print image grouping via image alt text.** The Replit app groups gallery images by `altText == print value`, and **95 images have empty alt text** (21 products). Target: variant media for grouping plus descriptive alt text. Don't rewrite alt text until the Replit site is retired, or its galleries break; add new grouping data first. **⚠️ D-8**
3. ⚠️ **Per-print collections: keep them only where a product spans collections (simplification agreed 2026-09-28).** Every active product except **Margit** has its prints in a single collection that matches its normal Shopify collection, so the per-print `collection` field is redundant there, and redundant copies drift (that's how 4 active prints ended up pointing at the non-existent `botanicals`, leaving Whimsy empty).
   - **Zadie, Esther, Vera:** delete the `collection` key from each `kambric.prints` entry. Both the theme and the live Replit site then fall back to the product's own Shopify collection (Zadie → whimsy, Esther → psychedelics, Vera → folklore). **This fixes Whimsy on both sites.**
   - **Margit** (psychedelics ×6, folklore ×1, whimsy ×1): keep its entries; change its one `"botanicals"` to `"whimsy"` (Wildflowers).
   - Draft linens also reference `botanicals`; fix when they're activated.
   - Before running, confirm each product's Shopify collections: Zadie in `whimsy`, Esther in `psychedelics`, Vera in `folklore` (true in the 2026-09-28 audit). Shared with the live site, but this is the same fallback it already uses.
   - Later (D-6): a Prints metaobject with a collection field would make a print's collection a property of the print everywhere and retire these overrides.
4. **Drafts never appear.** Shopify never renders draft products on the Online Store, and the theme adds no bypass. 30 drafts are the old per-print products (`margit-one-piece-in-*`, `zadie-…-in-*`, `esther-…-in-*`, `vera-coat-in-*`) and unreleased linens. Keep them as drafts (their old handles get redirects, §4.1) or archive them. Owner decision per product line.
5. **Monogram fee product** `chainstitch-monogram` ($25, type `Add-on`, tags `hidden` + `monogram-fee`) **must stay published**, because unpublished products can't be added to the cart. The theme keeps it out of listings, search and predictive search (filter by the `hidden` tag) and marks its page `noindex` (done). **Sitemap exclusion needs store data:** set the product metafield `seo.hidden = 1` (it also hides it from Shopify search). It has no image, so the cart line needs a theme fallback (Phase 5). ⚠️ `seo.hidden` isn't read by the Replit site, so it's safe to set now.
6. **`hidden`-tagged products:** only the monogram today. The theme treats the tag as "not browsable"; don't unpublish tagged products that must stay purchasable.
7. **The four "missing" collection images need no replacement.** All four 404 paths belong to collection IDs `517595562279`, `517595791655` and `517595824423`, which **don't exist in this store** (orphaned rows). All six images for the live collections (Folklore, Psychedelics, Whimsy: cover + header) were exported. Drop the orphaned rows.
8. **Collection image overrides:** upload the six exported images (`../replit site/assets/uploads/`; suggested names in `../liquid/assets/usage-map.csv`) to Files and set `kambric.card_image` / `kambric.header_image` on the three collections. Safe: new metafields the Replit site doesn't read.
9. **Swatches:** 14 code-owned swatch images, plus 5 prints with none (Retro Stripe, Sunset Plumes, Saffron Damask, Amber Orchard, Sunrise Plumes, all on draft linens). Upload to Files / Prints metaobjects (D-14).
10. **Blank SKUs** on variants of every product (e.g. all 10 active ones). Not a theme blocker; set SKUs if operations need them (⚠️ shared, but harmless to the Replit site).
11. **Products without images:** the monogram plus 14 drafts. Fine while they're drafts; they need images before being activated.
12. **`frontpage` collection** has no season/year. It's excluded from all listings; no change needed.
13. **Category collections** (steps in CONTENT_GUIDE §3a-A1, restricted to the Online Store channel so the live Replit site doesn't list them): automated collections `dresses`, `kaftans`, `coats`, `swimwear`, `accessories` (product type equals…) and `sale`. The monogram's type `Add-on` keeps it out automatically. **⚠️ D-10**
14. **Journal categories** have inconsistent casing ("The Archive" vs "the archive"; "craft") → normalise as tags.
15. **Collection copy** hard-coded in `Shop.tsx` and `categoryMeta.ts` (titles/descriptions in `../liquid/SEO.md`) → collection descriptions + SEO fields, so titles like `Heritage Print Dresses | Kambric Goods` carry over.
16. **Store SEO title/description** (Online Store → Preferences): `Kambric Goods | Heritage Prints, Modern Womenswear` + the home description from `../liquid/SEO.md`.
17. **Events** use free-text dates → real `date` values plus display labels.
18. **Policies** (privacy/terms) → Shopify policy pages (⚠️ also shown at checkout).
19. **Menus:** `main-menu`, `footer`, `footer-info`: step-by-step in CONTENT_GUIDE §3a (Part A now, Part B in Phase 4).
20. **Personal data** (subscribers, back-in-stock) is migrated separately with consent preserved. It's never committed to this repo.
21. **Search listings:** check every product, collection and page for a unique SEO title/description, and write alt text for all product media (after item 2).

---

## 4. Redirects and cutover

### 4.1 URL map
Shopify URL redirects only fire when the source path would 404 in Shopify, and they are path-only. Query-string sources are **⚠️ to verify** on the dev store. The list is imported as a CSV (Online Store → Navigation → URL redirects) by the owner.

| Current URL | New URL | Mechanism |
| --- | --- | --- |
| `/`, `/collections`, `/collections/{handle}`, `/products/{handle}`, `/cart`, `/search` | same | native, no redirect |
| `/shop` | `/collections/all` | redirect |
| `/shop/{dresses,kaftans,coats,swimwear,accessories}` | `/collections/{same}` | redirect ×5 (needs D-10 collections) |
| `/shop?category=Dresses` etc. | `/collections/dresses` | ⚠️ query-source redirect; if unsupported, `/shop` → `/collections/all` covers it (low traffic) |
| `/sale` | `/collections/sale` | redirect |
| `/about`, `/events`, `/contact`, `/wholesale`, `/size-guide`, `/shipping`, `/returns` | `/pages/{same}` | redirect ×7 |
| `/privacy-policy`, `/terms-of-service` | `/policies/privacy-policy`, `/policies/terms-of-service` | redirect ×2 |
| `/journal` | `/blogs/journal` | redirect |
| `/journal/{slug}` (5) | `/blogs/journal/{slug}` | redirect ×5 (no wildcards in Shopify; add one per future post, or keep new posts on /blogs only) |
| `/products/kati-slip-dress-in-sunset-plumes` | `/products/jessie-slip-dress-in-twilight-plumes` | redirect (Shopify auto-creates these on handle change) |
| `/collections/botanicals` | `/collections/whimsy` | redirect |
| `/products/{old per-print handle}` → `?variant=` (e.g. `margit-one-piece-in-dahlia-seed`; 17 draft products: margit ×8, zadie ×3, esther ×3, vera-coat ×3) | `/products/{merged handle}?print={Print}` (or the plain merged handle when the print isn't on it, e.g. Sunrise Plumes) | redirect ×17 ⚠️ verify Shopify fires redirects for handles of *draft* products (they 404 publicly); if not, archive/rename the drafts' handles first |
| `/products/{legacy numeric id}` (8 product IDs) | `/products/{handle}` | redirect ×8 |
| `/products/{legacy per-print id}` (18, from `kambric.prints[].legacyId`) | `/products/{handle}?variant={first available variant of the print}` | redirect ×18 (D-7) |
| `/products/{handle}?print=X` | same URL; theme JS resolves it to the print's variant; canonical stays `/products/{handle}` | theme (D-7) |
| `/api/sitemap.xml` | `/sitemap.xml` | redirect |
| `/admin` | `/` | redirect (optional) |
| `www.` → apex, trailing slash, mixed case | Shopify primary-domain redirect handles www; trailing-slash/case behaviour **⚠️ to verify** | domain settings |

The final CSV is generated from `urls/redirects.csv` + `current-urls.csv` + the live `kambric.prints` metafields right before launch, then re-crawled after cutover for 200/301 parity.

### 4.2 SEO/AEO launch safeguards
- Canonicals, titles and descriptions match or improve on the current ones (compare against `current-urls.csv`).
- JSON-LD validated (Rich Results Test) on home, product, collection, article and events.
- robots.txt keeps AI crawlers allowed; the sitemap is submitted in Google Search Console and Bing Webmaster Tools the same day.
- Core Web Vitals checked on the unpublished theme preview (Lighthouse mobile ×3 runs, median) before publishing.

### 4.3 Readiness and cutover

**Before cutover (on the playground, any time):**
1. Publish the Kambric26 theme on the Shopify-hosted Online Store once it's stable, so editors can enter content that carries over at cutover (**⚠️ D-21**). From then on, editors own its JSON; pull before every push (CLAUDE.md guardrail 9).
2. Enter content on the playground: pages, journal, events, menus, theme editor sections.
3. Run the reviewed data plan (§2 definitions, §3 cleanup), staging every **shared** change so it doesn't break the live Replit site (e.g. keep `kambric.prints` JSON intact while adding new fields, keep alt text grouping until the Replit site is retired, publish new collections to the Online Store channel only).
4. Import the redirect CSV (Online Store only, so it's safe early), then spot-check 10 legacy URLs on the `myshopify.com` domain.
5. Production-readiness review on the playground domain: every page type at 1440/390, Theme Check, Lighthouse (median of 3 mobile runs), console, a checkout test order (refund/cancel), JSON-LD validation.
6. Configure the Meta channel (D-13), email/newsletter (D-11) and back-in-stock (D-12). Where these touch checkout or notifications they're **shared**, so time them for cutover.

**Cutover (DNS):**
7. Content freeze on Replit `/admin`; final export (content JSON, subscribers, back-in-stock) and import of any late changes.
8. Remove the Online Store password (if set) and confirm the Kambric26 theme is published.
9. DNS: point `kambricgoods.com` + `www` to Shopify, set it as the primary domain (www → apex), and wait for SSL.
9a. **Restore the publish/live-push deny rules** in `.claude/settings.json` (list in CLAUDE.md, "Pre-cutover exception") and commit. From here on the published theme is the real site.
10. Post-launch: crawl all old URLs (expect 200/301), submit the sitemap to GSC and Bing, watch coverage and 404s daily for 2 weeks, compare CrUX after 28 days.
11. Rollback: keep the Replit deployment running for 14 days; rolling back means reverting DNS. Avoid irreversible shared-data changes in this window.
12. After the rollback window: decommission the Replit Storefront/Admin tokens and webhooks, then remove Replit-only workarounds from the catalog (e.g. alt-text print grouping, `hidden` tag logic if unpublished instead).

---

## 5. Open decisions

| ID | Decision | Options (recommendation first) | Needed by |
| --- | --- | --- | --- |
| **D-1** | Announcement bar style | ✅ **Decided:** static by default + optional marquee (built) | Done |
| **D-2** | Where announcement settings live | ✅ **Decided:** section settings in the header group; how-to in CONTENT_GUIDE §3 | Done |
| **D-3** | Footer menu handles | ✅ **Decided:** `footer` (Shop) + `footer-info` (Information); owner setup steps in CONTENT_GUIDE §3a | Done |
| **D-4** | Fraunces font weight (bytes) | ✅ **Decided:** `SOFT` pinned to 0 (never used; −44%, 270 → 149 KB, visually identical). Revert: re-download with `SOFT@0..100` | Done |
| **D-5** | Contrast below WCAG AA | ✅ **Decided:** announcement bar darkened 6% toward cocoa (4.32 → 4.63:1); mobile "Menu" label at 70% opacity (5.4:1) | Done |
| **D-6** | Print data model | **Keep `kambric.prints` JSON for per-product data + add `kambric_print` metaobjects for shared story/swatch** · all-metaobject · JSON only (swatches stay in theme assets) | Phase 2 |
| **D-6b** | Events storage | **Metaobject `kambric_event`** · page blocks | Phase 4 |
| **D-7** | Print selection URL | ✅ **Decided (2026-09-28):** cards, swatches and redirects use native `?variant=<first available variant of the print>` (server-rendered, no flash or CLS); legacy `?print=` still works via JS on load; canonical stays `/products/{handle}` | Done |
| **D-8** | Print ↔ image mapping | **Variant media (native) for new grouping; alt text becomes descriptive after the Replit site is retired** · print metafield on media · keep alt-text matching (hurts a11y/SEO; 95 images have empty alt today) | Phase 2 |
| **D-9** | Monogram fee linking | ✅ **Decided:** linked cart lines (garment + $25 fee line share `_monogramGroup`; one atomic `/cart/add.js` request; cart keeps them in sync). Not enforced at checkout (same as today) | Done |
| **D-10** | Category pages | **Automated collections by product type** (`/collections/dresses`…) · `/collections/all?filter.p.product_type=` (weaker SEO). Owner creating them now (Online Store channel only) per CONTENT_GUIDE §3a-A1 | Phase 3 |
| **D-11** | Newsletter + WELCOME15 | **Shopify customer form + Shopify Email welcome automation sending the code** · show the code on-screen (current; code is public) · third-party ESP (Klaviyo) | Phase 5 |
| **D-12** | Back-in-stock | ✅ **Decided:** native "Notify me" dialog using Shopify's contact form (emails the store; owner notifies by hand); swap in an app later without changing the page | Done (app: post-launch) |
| **D-13** | Meta Pixel | **Facebook & Instagram by Meta channel (Customer Events, no theme JS)** · custom pixel | Phase 5 |
| **D-14** | Print swatches | **Swatch image on `kambric_print` metaobject** · theme assets keyed by print name · Shopify's native swatch (option value swatches in the admin: native, simplest if the option is linked to a metaobject/category) | Phase 2 |
| **D-15** | Search | **Overlay using Predictive Search API + `/search` page** · `/search` page only | Phase 5 |
| **D-16** | Journal URLs | `/blogs/journal/*` is required by Shopify; accept + redirects | Phase 4 |
| **D-17** | Per-print cards and pagination | **Render print cards per product; paginate by products (card count varies per page)** · combined listings (Shopify Plus only) | Phase 3 |
| **D-18** | Dark palette from source CSS | **Drop (unused by the storefront)** · keep as tokens | Phase 1 |
| **D-19** | `llms.txt` | **Skip for now** (Shopify can't serve root files without an app proxy; AEO is covered by structured data + clean HTML) · app proxy | Post-launch |
| **D-22** | Archive label (e.g. Arielle's "Parlor Rose Archive Print") | ✅ **Decided:** new product metafield `kambric.archive_label` (single-line text); empty = normal label. No handle special-cases | Done (owner creates the definition) |
| **D-21** | When to publish Kambric26 on the Shopify-hosted Online Store | ✅ **Decided:** publish once the Phase 1 shell is stable so editors can pre-load content; publish/live-push deny rules lifted until DNS cutover (restore at step 9a) | Phase 1 |
| **D-20** | Newsletter form on the dev theme | ✅ **Decided:** test with `+test` addresses; owner deletes test customers | Done |
