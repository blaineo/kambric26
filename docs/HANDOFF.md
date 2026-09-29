# Handoff: where the Kambric Goods theme build stands

*Written 2026-09-28 at the end of the first long working session, so a fresh session (or person) can pick up without the chat history. Read this, then `CLAUDE.md`, then whichever doc the next task needs.*

## 1. The project in one paragraph
kambricgoods.com is a React/Vite site on Replit that uses Shopify only through the Storefront API and checkout. We're replacing it with a custom Online Store 2.0 theme, **`kambric26`**, built on Shopify's Skeleton theme with hand-written CSS on design tokens and small vanilla-JS custom elements (no build step). The live Replit site and the Shopify-hosted storefront **share one store** (catalog, collections, checkout). The Shopify-hosted site is the playground; **launch = DNS cutover**. The owner does **not** change anything that can affect kambricgoods.com before cutover.

## 2. Where everything is
| What | Where |
| --- | --- |
| Theme repo | `~/Code/kambric/kambric26/` · remote `git@github.com:blaineo/kambric26.git` · branch `main` |
| Rules for agents and humans | `CLAUDE.md` (guardrails 1–10, conventions, definition of done) |
| Phase plan, decisions (D-1…D-22), data cleanup, redirects, cutover | `docs/MIGRATION_PLAN.md` |
| Editor-facing guide (retailer) | `docs/CONTENT_GUIDE.md` (§2b "How the shop is organized", §3…§3i per area) |
| Owner pre-launch checklist (🟢 safe / 🟡 careful / 🔴 cutover only) | `docs/OWNER_TASKS.md` |
| Store-change batches (snapshots, apply, rollback, logs) | `docs/store-changes/` (README = the procedure) |
| Import-ready content | `docs/store-data/` (collection copy CSV; `phase4/` journal, events, pages, policies; `phase4/owner-notes/`, `phase5/`) |
| Redirect list | `docs/redirects-draft.csv` (67 rows, **imported**) |
| Reference export (read-only) | `~/Code/kambric/replit site/` (screenshots = visual spec) and `~/Code/kambric/liquid/` (rendered HTML, SEO.md, BEHAVIOR.md, SECTIONS.md, catalog audit) |
| React source (read-only) | `~/Code/kambric/liquid/source-snapshot.zip`. Unzip into a scratch folder when needed (the previous unzip was in a temporary scratchpad and is gone) |
| Tools | `tools/page_check.py` (per-page QA), `tools/live_site_snapshot.py` (kambricgoods.com snapshot/diff), `tools/merge_locales.py` (merge locale fragments) |
| Memory | `~/.claude/projects/-Users-blaine-Code-kambric/memory/` (the "no live-site changes before cutover" rule) |

**Store:** Kambric Goods, Shop ID **71406846186**, permanent domain **`7u2dfq-xf.myshopify.com`** (display `kambric-goods-2.myshopify.com`). Admin API via `shopify store execute --store 7u2dfq-xf.myshopify.com` (authenticated as kambricgoods@gmail.com; scopes `write_products, write_files, write_online_store_navigation, write_publications`). Metaobjects, pages and blogs need `write_metaobject_definitions, write_metaobjects, write_content` added (re-run `shopify store auth … --scopes …`).

**Dev:** `shopify theme dev -e development` → http://127.0.0.1:9292 (development theme id 145427988714 at the time of writing). `shopify theme check` must stay at 0 offenses.

## 3. Status
**Git:** 67 commits; **origin/main is at `2d4c82e`** (Phase 2 swatches), so the last ~40 local commits (Phase 3 onward, store batches, docs) are **not pushed yet**. The owner pushes; Claude doesn't.

**Theme (all five build phases done; Theme Check 106 files / 0 offenses; `tools/page_check.py --preset all` 19/19 pass):**
| Phase | Built |
| --- | --- |
| 0 Foundation | tokens (`assets/critical.css`), self-hosted Fraunces (SOFT pinned) + Jost with metric-matched fallbacks, `picture` snippet (the image standard), SEO head + JSON-LD, header/announcement/footer groups |
| 1 Global | buttons, eyebrow, headings, rte (with real tables), theme blocks, product/collection cards, print expansion (`product-prints`, `print-summary`), swatches, breadcrumbs, 404, robots.txt |
| 2 Product | `main-product`: `?variant=` print URLs (D-7, `?print=` fallback), gallery, sizes, monogram as linked cart lines (D-9), notify-me via contact form (D-12), archive label (D-22), taxonomy specs |
| 3 Listings | one `product-listing` section (a **Collection block** per group on shop/category pages; single grid on collection/sale), collection hero, catalog heading, category strip, `/collections` index, CTA strip. Shop = `/collections/all`; categories use template `collection.category`; sale `collection.sale` |
| 4 Content | home (hero, marquees, rails with "show first" blocks, story, lookbook, quote), About, Events (metaobject `kambric_event`), Journal (blog `journal`), info pages + size-guide table |
| 5 Utility | cart (D-9 grouping, works without JS), search overlay + `/search`, newsletter pop-up (off by default; `discount_code` setting) |

**Store batches (all verified with a clean kambricgoods.com diff):**
| # | Batch | State |
| --- | --- | --- |
| 01 | Custom fields (`kambric.archive_label`, `card_image`, `header_image`, `seo.hidden`; Arielle "Parlor Rose"; monogram hidden) | ✅ done |
| 02 | Collection card/header images (6 Files) | ✅ done |
| 03 | Category + sale collections | ⏳ **cutover only** (the live site reads the Online Store channel; prepared + dry-run tested) |
| 04 | Menus (main-menu Shop + Collections; `footer-info`, `shop-categories` created) | ✅ done (category/info links later) |
| 05 | Collection search listings | ✅ done |
| 06 | 67 URL redirects (all firing, incl. draft-product handles; `/shop` handled in the theme) | ✅ done |
| 07 | Home page title/description (Online Store → Preferences) | ⏸ **paused**: Chrome typing went to admin keyboard shortcuts (nothing saved). Owner types the two values, or retry with a focus check per field. Values in `docs/store-changes/07-admin-settings/plan.md`. |
| 08 | Content import: pages, journal, events, menu Part B (`08-content-import/`) | ✅ done 2026-09-29 (see `log.md`) |
| 09 | Publish kambric26 on the Shopify-hosted store (D-21) | not started (publish deny rules are lifted until DNS cutover; publish only on explicit request) |

## 4. Decisions still needed (owner)
- ~~Cart (Phase 5)~~ **decided 2026-09-28 and built:** all options on cart lines; missing monogram fee blocks checkout; fee sold out → garment sold out; header counts garments only.
- **D-11** newsletter: show WELCOME15 on screen vs Shopify Email sends it (both supported by the pop-up's `discount_code` setting; the discount itself is 🔴 cutover).
- **Copy/data:** Whimsy's description (the sheet's text was the old Botanicals copy; flagged); lookbook look 3 caption names the renamed product; one collection description serves both the collection hero and shop-group text (keep, or add a group-text field?); shop page emits CollectionPage JSON-LD (source didn't).
- **Later:** D-6/D-14 Prints metaobject (shared story/swatch/collection per print); D-8 variant media + descriptive alt text (after cutover, because the live site groups photos by alt text); larger hero original (current is 1448 px).

## 5. Next steps (suggested order)
1. **Push** the local commits.
2. **Verification pass** (last "definition of done" gate): Lighthouse mobile (SEO 100, a11y ≥ 95, CLS < 0.05, LCP < 2.5 s) on the preview URL, and a true 390 px check (Chrome here won't narrow below ~606 px and Shopify blocks iframes, so use DevTools device mode or Lighthouse's mobile emulation).
4. **Content batches (🟢):** photos into templates (home 11, About/Events 5, pop-up 1; set as `shopify://shop_images/<file>` in template JSON after uploading to Files); then, with the extra scopes, the `kambric_event` definition + entries, pages, and the journal import (`docs/store-data/phase4/`).
5. **Batch 07** (home SEO title/description) and **batch 09** (publish on the Shopify-hosted store) when the owner says.
6. **Pre-launch cleanup:** delete the dev-only preview templates (`templates/*phase*.json`: 9 files) and their preview sections (`sections/phase*-preview.liquid`); re-run page_check and Theme Check.
7. **Cutover** (`docs/MIGRATION_PLAN.md` §4.3 + OWNER_TASKS C): batch 03, per-print collection clean-up (fixes Whimsy), policies, WELCOME15, Meta channel, remove password, DNS, restore publish deny rules (step 9a).

## 6. How the work was run (repeat this pattern)
- **Parallel agents, model by task:** Opus for risky logic (print model, product page, listings, cart), Sonnet for standard sections/templates, Haiku for mechanical work (assets, extraction, scripts). Each agent owns a disjoint file list, never commits, and writes locale keys/content-guide notes/owner tasks to scratch files that the main session merges (`tools/merge_locales.py`) and commits per workstream.
- **Store changes:** only 🟢/🟡 OWNER_TASKS items, one approved batch at a time, via `docs/store-changes/README.md` (store + live snapshots, reviewed apply, generated rollback, live diff; any live change → stop, roll back, report).
- **Every change an editor would notice** goes into CONTENT_GUIDE, and every owner step into OWNER_TASKS, in the same commit.

## 7. Gotchas learned the hard way
- `image_tag`'s `preload: true` emits a malformed HTTP Link header (unquoted `imagesrcset`/`imagesizes`), so the browser preloads the wrong file. `picture.liquid` writes its own `<link rel="preload">` instead (LCP on product/collection pages went from 5–6 s to 3–4 s in Lighthouse mobile).
- Inside `{% for w in … %}`, `assign w = …` does **not** change `w` (the loop variable wins). Use a different name.
- A literal `}` inside `{{ … }}` breaks the upload (Theme Check misses it); build such strings in `{% liquid %}`.
- `render` named arguments can't take filters (assign first); inside `{% liquid %}` keep each `render` on one line.
- Sections use `{% comment %}`, not `{% doc %}`; schema `name` ≤ 25 characters.
- Equal-specificity CSS loses to Shopify's bundle order: prefix overrides with the owning snippet's class (`.rte.product__description`, `.btn.back-in-stock__submit`).
- Undefined CSS variables silently void the declaration: all `--space-*` etc. must exist in `critical.css`.
- A template referencing a missing section breaks the **whole** dev upload ("Failed to Upload"); create sections first. Occasional 502s from the dev proxy are transient; retry.
- Shopify reserves `/shop` as a home alias (redirects can't fire there); the theme meta-refreshes it to `/collections/all`.
- The live site reads the **Online Store** channel: "Online Store only" does **not** hide anything from kambricgoods.com.
- Background jobs may run in another folder: call tools with absolute paths.
- In the Shopify admin, typing before a field has focus triggers keyboard shortcuts; confirm focus (screenshot) before typing, or prefer the Admin API.
- Usage limits can stop agents mid-task: resume them with SendMessage (files on disk survive).
