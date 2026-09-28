# Kambric Goods: Shopify theme migration plan (draft v0.1)

**Status:** first draft for owner review, 2026-09-28. Decisions are marked **⚠️ D-n** and collected in [§5](#5-open-decisions).
**Scope:** rebuild kambricgoods.com (React/Vite on Replit, Shopify Storefront API + checkout) as the Online Store 2.0 theme in this repo (`kambric26`), then cut over the domain.
**Sources:** `../replit site/` (export). Page-level blueprints will come from `../replit site/liquid/` (rendered HTML, `COMPONENTS.md`, `SECTIONS.md`, `hardcoded.json`, `navigation.json`, `BEHAVIOR.md`) once it lands.

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

### Phase 2: Product page (highest risk)
Parity: `product-1440/390.png`; rendered-HTML variants for merged multi-print, single-print, Arielle, monogrammable and sold-out.
- **Print model** (see SHOPIFY_DATA_MAP): merged products (option `Print`/`Colorway`) vs single-print (`kambric.print_name`/`print_story`); per-print data from `kambric.prints` JSON (`story`, `collection`, `featured`, `newArrival`, `legacyId`). **⚠️ D-6, D-7, D-8, D-14**
- Server-rendered first paint of the selected print (Liquid can't read `?print=`, so the default print is rendered and `<kg-product-form>` switches on load **without layout shift**: same-size gallery, preloaded first image). **⚠️ D-7**
- Size selection, per-print price/compare-at/availability, sold-out state and **back-in-stock** entry point. **⚠️ D-12**
- **Chainstitch monogram**: 10-character text + colour, fee product `chainstitch-monogram` (hidden) linked to the parent line; quantity and removal stay in sync. **⚠️ D-9**
- JSON-LD: extend `structured_data` output with brand, per-print `ProductGroup`/`hasVariant` (variesBy pattern/size), `BreadcrumbList`. AEO: size/fit/fabric/care as real text (`<dl>`), not images.
- LCP: first gallery image is `priority`; the rest lazy; thumbnails sized via `sizes`.

### Phase 3: Collection, shop and category pages
Parity: `shop-*`, `category-*`, `collection-index-*`, `collection-*`.
- `/collections` index with cover-image override metafield; collection page with header-image override; season/year eyebrow from `kambric.season`/`kambric.year`.
- **Per-print product cards** (merged products expand into one card per print, filtered to prints whose collection handle matches). **⚠️ D-17**
- Category pages = automated collections by product type. **⚠️ D-10**
- `/sale` = automated collection (compare-at price > price). Filters/sort via native Search & Discovery if needed.
- Exclusions everywhere: tag `hidden`, handle `chainstitch-monogram`, collection `frontpage`.
- JSON-LD: `CollectionPage` + `ItemList`, BreadcrumbList. First row of cards `eager`, rest `lazy`.

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

1. **Arielle uses `Size` as its colorway** (Olive/Terracotta), with images matched by filename. Rename the option to `Colorway` and give it real sizes (or a single `One size`), and attach images per colour (D-8). This removes both code special cases.
2. **Print image grouping via image alt text.** Alt text currently equals the print name, which is poor for accessibility, SEO and AEO. Move grouping to variant media or a print metafield, then write descriptive alt text. **⚠️ D-8**
3. **Category collections:** create automated collections `dresses`, `kaftans`, `coats`, `swimwear`, `accessories` (product type equals…) and `sale`. Audit for product types outside the five labels. **⚠️ D-10**
4. **Monogram product** `chainstitch-monogram`: keep it unpublished from collections, and set `seo.hidden = 1` so it's out of search and the sitemap.
5. **`hidden`-tagged products:** at cutover, prefer unpublishing them from the Online Store channel. The theme keeps filtering the tag as a safety net.
6. **Journal categories** have inconsistent casing ("The Archive" vs "the archive"; "craft") → normalise as tags.
7. **Four collection images return 404** (IDs in `assets/EXPORT_NOTES.md`). Re-upload or drop them.
8. **Collection image overrides** are keyed by numeric collection ID → map to handles, upload to Files, set the metafields.
9. **Swatches** are code-owned local images (14 prints) → upload to Files / Prints metaobjects (D-14).
10. **Collection copy** hard-coded in `Shop.tsx` (Folklore, Botanicals→Whimsy, Psychedelics) and `categoryMeta.ts` → collection descriptions + SEO fields.
11. **Events** use free-text dates → real `date` values plus display labels.
12. **Policies** (privacy/terms) → Shopify policy pages.
13. **Menus:** create `main-menu`, `footer`, `footer-info` with the links in CONTENT_GUIDE §3.
14. **Personal data** (subscribers, back-in-stock) is migrated separately with consent preserved. It's never committed to this repo.
15. **Search listings:** check every product, collection and page for a unique SEO title/description, and write alt text for all product media.

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
| `/products/{legacy numeric id}` (8 product IDs) | `/products/{handle}` | redirect ×8 |
| `/products/{legacy per-print id}` (18, from `kambric.prints[].legacyId`) | `/products/{handle}?print={Print}` | redirect ×18; target query supported |
| `/products/{handle}?print=X` | same URL; theme JS selects the print; canonical stays `/products/{handle}` | theme (D-7) |
| `/api/sitemap.xml` | `/sitemap.xml` | redirect |
| `/admin` | `/` | redirect (optional) |
| `www.` → apex, trailing slash, mixed case | Shopify primary-domain redirect handles www; trailing-slash/case behaviour **⚠️ to verify** | domain settings |

The final CSV is generated from `urls/redirects.csv` + `current-urls.csv` + the live `kambric.prints` metafields right before launch, then re-crawled after cutover for 200/301 parity.

### 4.2 SEO/AEO launch safeguards
- Canonicals, titles and descriptions match or improve on the current ones (compare against `current-urls.csv`).
- JSON-LD validated (Rich Results Test) on home, product, collection, article and events.
- robots.txt keeps AI crawlers allowed; the sitemap is submitted in Google Search Console and Bing Webmaster Tools the same day.
- Core Web Vitals checked on the unpublished theme preview (Lighthouse mobile ×3 runs, median) before publishing.

### 4.3 Cutover checklist (owner runs store and DNS steps)
1. Content freeze on Replit `/admin`; take a final export (content JSON, subscribers, back-in-stock).
2. Run the reviewed data plan (§2 definitions, §3 cleanup, content import) on the store.
3. `shopify theme push --unpublished` the release commit, then review the preview: every page type at 1440/390, Theme Check, Lighthouse, console, checkout test order (then refund/cancel).
4. Import the redirect CSV; spot-check 10 random legacy URLs on the preview domain.
5. Install and configure the Meta channel (D-13), email/newsletter (D-11) and back-in-stock (D-12).
6. **Owner publishes the theme.**
7. DNS: point `kambricgoods.com` + `www` to Shopify, set the primary domain (www → apex), and wait for SSL.
8. Post-launch: crawl all old URLs (expect 200/301), submit the sitemap, watch GSC coverage and 404s daily for 2 weeks, compare CrUX after 28 days.
9. Rollback: keep the Replit deployment running read-only for 14 days; rolling back means reverting DNS.
10. Decommission the Replit Storefront API token, Admin token and webhooks after the rollback window.

---

## 5. Open decisions

| ID | Decision | Options (recommendation first) | Needed by |
| --- | --- | --- | --- |
| **D-1** | Announcement bar style | **Static by default + optional marquee (built)** · marquee by default | Phase 0 review |
| **D-2** | Where announcement settings live | **Section settings in the header group (built)** · global theme settings | Phase 0 review |
| **D-3** | Footer menu handles | **`footer` (Shop) + `footer-info` (Information) (built)** · one `footer` menu with nested groups | Phase 0 review |
| **D-4** | Fraunces font weight (bytes) | Ship full axes as briefed (270 KB for both files) · **pin `SOFT=0` (never used by the site; −44%, 149 KB, visually identical)** | Phase 1 |
| **D-5** | Contrast below WCAG AA | Terracotta announcement bar text is 4.32:1 (needs 4.5): **darken bar ~4% L** · keep. Mobile "Menu" label raised 60%→70% opacity already (4.0→5.4:1) | Phase 1 |
| **D-6** | Print data model | **Keep `kambric.prints` JSON for per-product data + add `kambric_print` metaobjects for shared story/swatch** · all-metaobject · JSON only (swatches stay in theme assets) | Phase 2 |
| **D-6b** | Events storage | **Metaobject `kambric_event`** · page blocks | Phase 4 |
| **D-7** | Print selection URL | **Keep `?print=` (preserves 18 legacy redirects + shared links); canonical without query** · switch to native `?variant=` | Phase 2 |
| **D-8** | Print ↔ image mapping | **Variant media (native)** · print metafield on media · keep alt-text matching (hurts a11y/SEO) | Phase 2 |
| **D-9** | Monogram fee linking | **Two cart lines linked by a hidden `_monogram_for` line-item property + theme-side sync** (simple; not enforced at checkout) · Cart Transform function (robust, needs a custom app) · single product with a monogram variant/option | Phase 2 |
| **D-10** | Category pages | **Automated collections by product type** (`/collections/dresses`…) · `/collections/all?filter.p.product_type=` (weaker SEO) | Phase 3 |
| **D-11** | Newsletter + WELCOME15 | **Shopify customer form + Shopify Email welcome automation sending the code** · show the code on-screen (current; code is public) · third-party ESP (Klaviyo) | Phase 5 |
| **D-12** | Back-in-stock | Lightweight app (e.g. a Shopify-built or well-reviewed notify-me app) · Klaviyo back-in-stock · drop feature | Phase 2 |
| **D-13** | Meta Pixel | **Facebook & Instagram by Meta channel (Customer Events, no theme JS)** · custom pixel | Phase 5 |
| **D-14** | Print swatches | **Swatch image on `kambric_print` metaobject** · theme assets keyed by print name · Shopify's native swatch (option value swatches in the admin: native, simplest if the option is linked to a metaobject/category) | Phase 2 |
| **D-15** | Search | **Overlay using Predictive Search API + `/search` page** · `/search` page only | Phase 5 |
| **D-16** | Journal URLs | `/blogs/journal/*` is required by Shopify; accept + redirects | Phase 4 |
| **D-17** | Per-print cards and pagination | **Render print cards per product; paginate by products (card count varies per page)** · combined listings (Shopify Plus only) | Phase 3 |
| **D-18** | Dark palette from source CSS | **Drop (unused by the storefront)** · keep as tokens | Phase 1 |
| **D-19** | `llms.txt` | **Skip for now** (Shopify can't serve root files without an app proxy; AEO is covered by structured data + clean HTML) · app proxy | Post-launch |
| **D-20** | Newsletter form on the dev theme | Submitting creates a real customer on `kambric-goods-2`: **use `+test` addresses and delete after testing (owner)** | Phase 0 review |
