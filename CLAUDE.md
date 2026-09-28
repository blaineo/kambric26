# CLAUDE.md: Kambric Goods theme (`kambric26`)

## Project context

We're rebuilding **kambricgoods.com** (currently a React/Vite/Tailwind v4 app on Replit) as a custom **Shopify Online Store 2.0 Liquid theme**, starting from Shopify's Skeleton theme.

- Store: `kambric-goods-2.myshopify.com` (CLI env `development` in `shopify.theme.toml`).
- Today the live storefront is still the Replit site. It uses Shopify only through the Storefront API and checkout. **This theme isn't live**, and the Online Store theme is only published at cutover, by the owner.
- The owner is a software engineer and reviews everything. Plan first, commit small, and surface decisions rather than guessing.
- Phase plan and open decisions: `docs/MIGRATION_PLAN.md`. What content editors need to know: `docs/CONTENT_GUIDE.md`.

## Guardrails (non-negotiable)

1. **Never publish.** No `shopify theme publish`, no `theme push --live`/`--allow-live`, no pushing to the published theme, no `theme delete`/`rename`. Use `shopify theme dev -e development`. Only when explicitly asked: `shopify theme push --unpublished`.
2. **Never change store data.** No creating, editing or deleting products, collections, metafields, metafield/metaobject definitions, metaobjects, menus, pages, blogs/articles, files, redirects, discounts or settings through the CLI, the Admin API or the browser. Store data changes are written up as a reviewed plan and the owner runs them. Read-only queries are fine when asked.
3. **Never commit secrets:** no `.env*`, tokens, passwords, or `.shopify/` session data. Never print secret values.
4. **Match the current site; don't redesign.** The screenshots in the export are the visual spec. Where the export and the brief disagree, ask.
5. **Native first.** Prefer Shopify features (menus, metafields, metaobjects, blogs, pages, customer forms, predictive search, URL redirects) over apps and custom JS. For interactivity, use vanilla JS in custom elements: no React, no jQuery, no build step.
6. **Accessibility, SEO, AEO and performance are requirements** (see below), not polish.
7. **Every change an editor would notice goes in `docs/CONTENT_GUIDE.md`,** in the same commit. That covers any new setting, section, block, metafield, metaobject, menu handle, or "where did X move to". The goal is a clean, simple transition for content maintainers.

`.claude/settings.json` denies the most dangerous commands as a backstop. It's prefix-matched, so it isn't a guarantee: the rules above still apply.

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
| `liquid/` (coming) | Rendered HTML per page, component catalog, section breakdown, hard-coded copy, nav JSON, behaviour specs. Prefer this over the JS bundle once it exists. |

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
