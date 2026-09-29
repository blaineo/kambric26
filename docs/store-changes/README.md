# Store-change batches (🟢/🟡 tasks from OWNER_TASKS.md)

Claude runs these **only** after the owner has (1) cleared the permission gate (see "Enabling" below) and (2) approved the specific batch. Each batch lives in its own folder, `docs/store-changes/NN-name/`:

| File | What it is |
| --- | --- |
| `plan.md` | Scope, every record touched, why it's 🟢/🟡, expected result, rollback steps |
| `before.json` | Read-only Admin API snapshot of every record the batch touches (current values, IDs) |
| `apply.graphql` (+ variables) | The exact mutations, reviewed before running |
| `rollback.graphql` | Generated from `before.json`: deletes what the batch created, restores what it changed |
| `after.json` | The same query as `before.json`, run after |
| `log.md` | What ran, when, the IDs created, the live-site diff result |

## Target store (verified 2026-09-28)
Store ID **71406846186** ("Kambric Goods"): permanent domain **`7u2dfq-xf.myshopify.com`**, display domain `kambric-goods-2.myshopify.com` (the permanent domain 301-redirects to it; both report the same ID in `/meta.json`). `shopify store` commands must use the permanent domain. Every batch's first read-only query checks the shop ID is `71406846186` and aborts otherwise.

## The procedure (every batch)
1. **Live baseline:** `tools/live_site_snapshot.py snapshot docs/store-changes/NN/live-before.json`. This reads only kambricgoods.com's public endpoints.
2. **Store snapshot:** read-only Admin queries → `before.json`. Generate `rollback.graphql` from it **before** applying anything.
3. **Owner approves** the batch (plan + apply + rollback reviewed).
4. **Apply** with `shopify store execute` (mutations exactly as reviewed). Record created IDs in `log.md`.
5. **Verify on the Shopify-hosted site** (the change did what it should) and in the Admin (`after.json`).
6. **Live check** (use absolute paths to `tools/live_site_snapshot.py`; background jobs may run from another folder): wait 2 minutes (the live site refreshes on Shopify webhooks), snapshot again → `live-after.json`, then `tools/live_site_snapshot.py diff live-before.json live-after.json`.
   - **No change** → batch done; tick the items in OWNER_TASKS.md; commit the batch folder.
   - **Any change** → **stop**, run `rollback.graphql`, re-snapshot until the diff is clean again, and report to the owner with the diff.
7. Batches never mix 🟢/🟡 with 🔴 work, and never touch records outside `plan.md`.

The live site caches pages for up to a day, but its **JSON API** reflects Shopify changes within minutes (webhook-driven), which is why the diff uses the API rather than page HTML.

## Enabling (owner steps, one time)
Claude can't change its own permission settings, so:
1. **Unblock the Admin CLI:** in `.claude/settings.json`, delete the line `"Bash(shopify store:*)",` from the `deny` list.
2. **Update guardrail 3 in `CLAUDE.md`**, or tell Claude "you may edit guardrail 3 to add the batch exception" (the wording is below).
3. **Authenticate:** run `! shopify store auth --store 7u2dfq-xf.myshopify.com --scopes write_products,write_files,write_online_store_navigation,write_publications` in the Claude Code prompt and complete the login in your browser. Claude never handles your password.

Proposed guardrail 3 wording:
> 3. **Store data: the owner approves every change.** By default Claude doesn't create, edit or delete store data. **Exception (owner decision 2026-09-28):** Claude may run 🟢 and 🟡 tasks from `docs/OWNER_TASKS.md`, one batch at a time, each explicitly approved by the owner, only through the process in `docs/store-changes/README.md` (snapshots, reviewed change, generated rollback, live-site diff). Any difference on kambricgoods.com → stop, roll back, report. 🔴 tasks stay owner-only.

## Batches (status: 01, 02, 04, 05, 06, 08, 10, 11 ✅ done; 03 at cutover; 07, 09 planned)
| # | Batch | Tier | Creates / changes | Rollback |
| --- | --- | --- | --- | --- |
| 01 ✅ | Custom-field definitions | 🟢 | Definitions `kambric.archive_label` (product), `kambric.card_image`, `kambric.header_image` (collection), `seo.hidden` (product); values: Arielle archive label "Parlor Rose", monogram `seo.hidden = 1` | `metafieldDefinitionDelete` (with its values) for each definition created; `metafieldsDelete` for the two values |
| 02 ✅ | Collection images | 🟢 | Upload 6 images to Files; set `card_image`/`header_image` on Folklore, Psychedelics, Whimsy | `metafieldsDelete` the 6 values; `fileDelete` the 6 files |
| 03 ⏳ cutover | Category and sale collections | 🔴 (at cutover) | 6 automated collections, templates `category`/`sale`, copy + SEO from `store-data/collection-copy.csv`, **created and published to Online Store in one step**; prepared + dry-run tested, see `03-category-collections/plan.md` | `rollback.py`: `collectionDelete` ×6 (IDs from `apply-log.json`) |
| 04 ✅ | Menus | 🟢 | `main-menu`, `footer` (replace items), `footer-info`, `shop-categories` (new) | Restore `main-menu`/`footer` items from `before.json`; `menuDelete` the two new menus |
| 05 ✅ | Search listings | 🟢 | SEO title/description on the 3 existing collections (not their Description field) | Restore previous SEO values from `before.json` |
| 06 ✅ | URL redirects | 🟢 | 67 redirects from `redirects-draft.csv` | `urlRedirectDelete` by the IDs recorded in `log.md` |
| 07 ✅ owner typed | Admin UI settings | 🟢 | Homepage title/description; contact-form recipients (Chrome, owner logged in) | Previous values recorded in `log.md` before editing; re-enter them |
| 08 ✅ | Content import | 🟢 | Pages (About, Events, 5 info pages; `contact` updated), `journal` blog + 5 posts, `kambric_event` definition + 3 events, Story/Events/Journal in `main-menu`, `footer-info` links; see `08-content-import/plan.md` | `rollback.py` (IDs from `apply-log.json`; menus + contact page restored from `before*.json`) |
| 09 | Publish Kambric26 on the Shopify-hosted store | 🟢 | Theme publish (CLI) | Re-publish the previously published theme (ID recorded in `log.md`) |
| 10 ✅ | Photos | 🟢 | Upload 16 home/About/Events photos to Files; the theme templates reference them (`10-photos/plan.md`) | `git revert` the template change; `rollback.py` (fileDelete) |
| 11 ✅ | Pop-up photo | 🟢 | Upload `newsletter-signup-popup.jpg`; the pop-up section references it (`11-popup-photo/plan.md`) | `git revert` the theme change; `rollback.py` (fileDelete) |

**Batch 03 (2026-09-28):** the live site reads the Online Store channel itself, so "Online Store only" is not a safeguard (`03-category-collections/finding.md`). Owner decision: create and publish in one step at cutover.
