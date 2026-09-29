# Batch 09 log: Kambric26 published on the Shopify-hosted store ✅

- **Requested:** owner, 2026-09-29 ("publish Kambric26 on the Shopify-hosted store"). D-21: the publish deny rules are lifted until DNS cutover.
- **Before:** live theme **Horizon #144358441194**; dev theme #145427988714.
- **Pushed:** `shopify theme push -e development --unpublished --theme "Kambric26"` from commit `1841b3e` → **Kambric26 #145439097066** (unpublished).
- **Preview check:** 15 pages (home, collections, Shop, Folklore, 2 products, About, Events, Contact, Size Guide, Journal, a post, cart, search, 404): correct status, one H1, titles, og:image, no Liquid errors.
- **Published:** 2026-09-29T16:02:17Z, `shopify theme publish --theme 145439097066`. Horizon is now unpublished (kept for rollback).
- **After:** public storefront (no preview) serves Kambric26; `/about`, `/journal/<post>` redirects work.
- **kambricgoods.com:** `live-after.json` vs `live-before.json` at 16:04:26Z: **no change** (8 endpoints).

**Rollback:** `shopify theme publish -e development --theme 144358441194 --force` (re-publishes Horizon).

**From now on (guardrail 9):** editors may customise the live Kambric26 theme in the admin. Before any push to it, pull its JSON (`shopify theme pull --theme 145439097066 --only templates/*.json --only sections/*-group.json --only config/settings_data.json`), commit, then push. Day-to-day development stays on the dev theme; pushing to the live theme only when the owner asks.
