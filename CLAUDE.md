# CLAUDE.md: Kambric Goods theme (`kambric26`)

## Project context

We're rebuilding **kambricgoods.com** (currently a React/Vite/Tailwind v4 app on Replit) as a custom **Shopify Online Store 2.0 Liquid theme**, starting from Shopify's Skeleton theme.

- Store: `kambric-goods-2.myshopify.com` (CLI env `development` in `shopify.theme.toml`).
- **Two storefronts share one store today:**
  - **kambricgoods.com = the live Replit site.** It reads catalog data through the Storefront API and uses Shopify checkout. Real customers are there.
  - **The Shopify-hosted Online Store (`kambric-goods-2.myshopify.com`) is our playground.** No customer traffic goes there, so theme work there has little or no consequence.
- **Cutover = DNS.** We get the Shopify-hosted site production-ready, then point kambricgoods.com at Shopify.
- The owner is a software engineer and reviews everything. Plan first, commit small, and surface decisions rather than guessing.
- Phase plan and open decisions: `docs/MIGRATION_PLAN.md`. What content editors need to know: `docs/CONTENT_GUIDE.md`.

## Guardrails (non-negotiable)

1. **Know the blast radius** before touching anything in the store:

   | Safe playground (Online Store only) | **Shared with the live Replit site: be careful** |
   | --- | --- |
   | Themes (dev, unpublished, and even the published Online Store theme), theme settings and editor content | Products, variants, prices, inventory, images and **image alt text** (it groups prints), tags, product types |
   | Menus, pages, blogs/articles, new metaobjects, Online Store URL redirects, `robots.txt.liquid` | Collections: creating one, or its **sales-channel publication**; the Replit site lists every collection it can see |
   | | Metafields the Replit site reads: `kambric.prints`, `print_name`, `print_story`, `season`, `year` |
   | | Checkout, discounts, shipping, payments, markets, policies, customer accounts, notifications (one checkout serves both sites) |

2. **Themes: work freely, but publish only on request.** Use `shopify theme dev -e development` and, when asked, `shopify theme push --unpublished`. Publishing or pushing to the published Online Store theme only affects the playground domain, but it still happens **only when the owner explicitly asks in the session**. Never `theme delete`.
3. **Store data: the owner runs changes.** No creating, editing or deleting products, collections, metafields, metaobject definitions/entries, menus, pages, blogs/articles, files, redirects, discounts or settings through the CLI, Admin API or browser. Write a reviewed plan (or step-by-step instructions in `docs/CONTENT_GUIDE.md`) that **flags every shared item** from the table above. Read-only queries are fine when asked.
4. **Never commit secrets:** no `.env*`, tokens, passwords, or `.shopify/` session data. Never print secret values.
5. **Match the current site; don't redesign.** The screenshots in the export are the visual spec. Where the export and the brief disagree, ask.
6. **Native first.** Prefer Shopify features (menus, metafields, metaobjects, blogs, pages, customer forms, predictive search, URL redirects) over apps and custom JS. For interactivity, use vanilla JS in custom elements: no React, no jQuery, no build step.
7. **Accessibility, SEO, AEO and performance are requirements** (see below), not polish.
8. **Every change an editor would notice goes in `docs/CONTENT_GUIDE.md`,** in the same commit. That covers any new setting, section, block, metafield, metaobject, menu handle, or "where did X move to". The goal is a clean, simple transition for content maintainers.
9. **Once editors start entering content on a Shopify theme, they own its JSON** (`config/settings_data.json`, `templates/*.json`, `sections/*-group.json`). Never push over them: pull from that theme and commit first.

`.claude/settings.json` denies the most dangerous commands as a backstop. It's prefix-matched, so it isn't a guarantee: the rules above still apply.

**Pre-cutover exception (owner decision D-21, 2026-09-28):** the deny rules for `shopify theme publish` and `theme push --live/-l/--allow-live/-a` are **temporarily removed** so Kambric26 can be published on the Shopify-hosted playground. Guardrail 2 still applies: only publish or push live when the owner asks in the session. **They must be restored at DNS cutover** (MIGRATION_PLAN §4.3, step 9a):

```json
"Bash(shopify theme publish:*)",
"Bash(shopify theme push --live:*)",
"Bash(shopify theme push -l:*)",
"Bash(shopify theme push --allow-live:*)",
"Bash(shopify theme push -a:*)"
```

## Reference export (read-only, never modify)

`~/Code/kambric/replit site/` (quote the path; it contains a space):

| Path | What it's for |
| --- | --- |
| `README.md` | Export scope, limits, and the five highest-risk migration areas |
| `INVENTORY.md` | Routes, interactions, CMS, integrations, SEO/redirect behaviour |
| `SHOPIFY_DATA_MAP.md` | Product/collection fields used, the **print model** (`kambric.prints` JSON, `print_name`, `print_story`), categories from `product.type`, exclusions (`hidden` tag, `chainstitch-monogram`), collection `kambric.season`/`year` |
| `ADMIN.md` | Every Replit CMS field → where it must live in Shopify |
| `design/DESIGN.md`, `tokens.json`, `global.css` | Design tokens and notes |
| `design/screenshots/` | **Visual spec**: `<page>-1440.png` and `<page>-390.png` viewport captures, plus `admin/` |
| `urls/` | `current-urls.csv` (live crawl) and `redirects.csv` (redirect rules) |
| `data/*.json` | CMS content snapshot (journal, events, about, home, settings, collection images) |
| `assets/` | Built assets (`built/assets/index-*.css` is the **compiled Tailwind**, and `index-*.js` holds the exact markup/classes), original images, uploads, `manifest.csv` |

**Liquid supplement:** `~/Code/kambric/liquid/` (next to the export, not inside it). Prefer it over the JS bundle.

| Path | What it's for |
| --- | --- |
| `README.md` | Scope and boundaries (raw HTML is pre-hydration) |
| `html/*.html` | 24 exact production responses: home, shop, category, collections, product variants (multi-print, single-print, Arielle, monogrammable, sold-out), info pages, journal, cart, 404. **Markup source for porting.** |
| `SECTIONS.md`, `COMPONENTS.md` | Page → section/blocks blueprint; component catalog (static / section / interactive) |
| `BEHAVIOR.md` | Print/size selection, cart, monogram, search, popup, events: JS specs |
| `SEO.md` | Per-route titles, descriptions, robots, JSON-LD examples. **Match these.** |
| `css/compiled.css`, `css/used-classes.txt` | Production Tailwind bundle and the 479 classes in server HTML: the exact-value reference |
| `content/hardcoded.json`, `content/navigation.json` | All code-owned copy (source-line attributed) and menu structures |
| `shopify/` | Read-only live Admin audit: `products.json`, `collections.json`, `metafield-definitions.json`, `chainstitch-monogram.json`, **`DATA_ISSUES.md`** |
| `assets/usage-map.csv` | App Storage images → content field and suggested filename |
| `emails/` | Back-in-stock and campaign templates |
| `source-snapshot.zip` | React source. Unzip only into the scratchpad, never into this repo. |

**Catalog facts (live audit, 2026-09-28):**
- 40 products: 10 active, 30 draft. **Drafts must never appear.** Shopify doesn't render them; never add a bypass.
- Prints: merged products use a `Print`/`Colorway` option; single-print products use `kambric.print_name`/`print_story`. Per-print data lives in the `kambric.prints` JSON. Gallery images are grouped by alt text = print value (legacy; see D-8).
- **Arielle** has real `Colorway` × `Size` options. Treat it like any multi-print product, with no special case.
- Categories = `product.type` (Dresses, Kaftans, Coats, Swimwear, Accessories).
- `chainstitch-monogram`: **published**, $25, type `Add-on`, tags `hidden` + `monogram-fee`, no image. Keep it out of listings, search, predictive search and the sitemap. The theme filters the `hidden` tag everywhere and noindexes its page.
- Collections: `folklore`, `psychedelics`, `whimsy` (+ `frontpage`, always excluded); metafields `kambric.season`, `kambric.year`. `kambric.prints` still references `botanicals` (the old name for whimsy).

## Folder conventions

```
layout/      theme.liquid (the one shell), password.liquid
templates/   JSON templates only (*.json); alternates as product.<suffix>.json
sections/    page regions with settings/blocks; *-group.json for header/footer groups
blocks/      theme blocks (@theme), reusable across sections
snippets/    render-only partials; document params with {% doc %} (LiquidDoc)
assets/      critical.css (tokens + base), *.woff2 fonts, component-*.js (custom elements), static images
locales/     en.default.json (storefront strings), en.default.schema.json (editor labels)
config/      settings_schema.json, settings_data.json
docs/        MIGRATION_PLAN.md, CONTENT_GUIDE.md (not uploaded; see .shopifyignore)
licenses/    third-party licences (not uploaded)
```

## Naming and code conventions

- Files: kebab-case (`announcement-bar.liquid`, `component-header.js`).
- Custom elements: `kg-` prefix (`<kg-header-menu>`), one per `assets/component-<name>.js`, loaded with `<script src type="module" defer>` only from the section that uses it.
- CSS classes: BEM-ish `.block__element--modifier` scoped to the section or snippet name (`.site-header__link--active`). Component CSS goes in the file's `{% stylesheet %}`. Global tokens, reset and utilities go in `assets/critical.css`. Use only token custom properties (`var(--color-foreground)`, `var(--space-6)`, `var(--tracking-label)`), with no raw hex in components. For opacity use `color-mix(in srgb, var(--color-x) 75%, transparent)`.
- Breakpoints (from Tailwind defaults; CSS vars can't be used in media queries): `40rem` sm, `48rem` md, `64rem` lg, `80rem` xl, `96rem` 2xl. Mobile-first `min-width` queries.
- Settings IDs: snake_case. Schema labels are `t:` keys in `en.default.schema.json` (the Skeleton convention). Storefront strings are `'key' | t` in `en.default.json`.
- Metafields/metaobjects: namespace `kambric`; metaobject types `kambric_print`, `kambric_event` (proposed; see the plan).
- Liquid: `{% liquid %}` for logic-heavy blocks, `{% render %}` (never `include`), whitespace control `{%- -%}` where output matters.

## Performance and Core Web Vitals

Targets on mobile (Lighthouse mobile plus field CrUX once live): **LCP < 2.5s, CLS < 0.05, INP < 200ms**.

- **Images: always `{% render 'picture' %}`** (`snippets/picture.liquid`). Never write a bare `<img>` or `image_tag` in sections. The snippet outputs `<picture>` with an optional art-directed mobile `<source>`, and an inner `<img>` (generated with `image_tag`) carrying a `srcset` from `image_url` widths, `sizes`, explicit `width`/`height` so nothing shifts, `alt`, and `decoding="async"`. The Shopify CDN negotiates AVIF/WebP automatically, so don't add format `<source>`s.
- **Loading** uses the snippet's `loading` param:
  - `'priority'`: at most one per page, the LCP image (hero or first product image). It's eager, gets `fetchpriority="high"`, and is preloaded with `imagesrcset` (via `image_tag`'s `preload: true`).
  - `'eager'`: anything else above the fold at 1440 or 390 (e.g. the logo).
  - `'lazy'`: the default, everything else.
- **Size and quality:** pass a realistic `sizes` value, cap widths at what's displayed ×2 (DPR), and crop at the CDN (`crop`/`height`) rather than in CSS. Bundled assets in `assets/` must be optimised before commit (PNG → palette PNG/WebP/SVG where lossless; JPG q≈78–82).
- **Layout shift:** reserve space for everything that loads later (images, embeds, the announcement bar, the sticky header). Fonts use `font-display: swap` plus **metric-matched fallback faces** (`size-adjust`/`ascent-override`) so the swap doesn't shift layout.
- **JS:** none by default. Custom elements are deferred modules and enhance working HTML. No third-party scripts without owner sign-off.
- **CSS:** `critical.css` stays small. Section CSS goes in `{% stylesheet %}` (Shopify bundles it). No `@import`.
- Preload only: the 2 primary fonts, the LCP image, and `critical.css`.

## SEO and AEO (answer-engine optimisation)

- Exactly one `<h1>` per page, a logical heading order, landmarks (`header`, `nav[aria-label]`, `main#MainContent`, `footer`), and descriptive link text.
- `snippets/meta-tags.liquid` owns title, description, canonical, OG/Twitter. Never hard-code canonicals. Keep URLs stable (redirect plan in `docs/MIGRATION_PLAN.md`).
- **Structured data (JSON-LD)** is rendered from Shopify objects, never duplicated by hand: Organization + WebSite (with SearchAction) site-wide, Product (`structured_data` filter, extended with print/brand data), BreadcrumbList on collection, product and article pages, Article/BlogPosting for the journal, Event for events, FAQPage only where visible FAQ content exists. It has to match what's visible on the page.
- **AEO:** answer-first copy blocks (the size guide, shipping, returns and care as real HTML text and tables, not images), descriptive `alt`, `<time datetime>`, `<dl>` for specs. Don't hide primary content behind JS. Keep AI crawlers allowed (the current site explicitly allows GPTBot, ClaudeBot, PerplexityBot, Google-Extended, OAI-SearchBot) via `templates/robots.txt.liquid` when that's added.
- `noindex` on cart, search results and 404 (Shopify handles most of this; verify).

## Accessibility

Semantic HTML first. A skip link to `#MainContent`. A visible `:focus-visible` ring (2px ring colour, 2px offset). Every control keyboard-operable, with `aria-expanded`/`aria-controls` on disclosures and Escape to close. `prefers-reduced-motion` stops marquees and transitions. Colour contrast AA (check muted text on ivory). Form inputs get `<label>`s. Icons are `aria-hidden` with text alternatives.

## Definition of done: a ported page

- [ ] Visual parity with `design/screenshots/<page>-1440.png` and `-390.png` (and the rendered HTML in `liquid/` once available)
- [ ] `shopify theme check` clean (0 errors, 0 warnings, or justified in `.theme-check.yml`)
- [ ] Lighthouse mobile: **SEO 100, Accessibility ≥ 95**, Performance ≥ 90, with CLS < 0.05 and LCP < 2.5s on the dev theme
- [ ] No console errors or warnings
- [ ] All editable content exposed as section settings or blocks (or metafields/metaobjects), with sensible defaults
- [ ] Valid JSON-LD (Rich Results Test / Schema validator) matching the visible content
- [ ] Images via `picture` snippet; exactly one priority image; keyboard and screen-reader pass
- [ ] `docs/CONTENT_GUIDE.md` updated for anything an editor would touch
- [ ] Small commits with clear messages

## Commands

```bash
shopify theme dev -e development      # local preview on a development theme (owner logs in)
shopify theme check                   # lint
shopify theme push --unpublished -e development   # ONLY when asked
```
