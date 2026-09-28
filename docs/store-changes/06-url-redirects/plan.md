# Batch 06: URL redirects (🟢)

**Goal:** import the 67 redirects from `docs/redirects-draft.csv` so every old kambricgoods.com URL lands on the right page of the new site after cutover. OWNER_TASKS A5.

**Why it's 🟢:** Shopify URL redirects only fire on the Shopify-hosted storefront (`kambric-goods-2.myshopify.com`, and later the domain once DNS moves). kambricgoods.com is still served by the Replit app, which never consults Shopify redirects. The live diff proves it.

**Before (`before.json`):** the store has **0** URL redirects, so none of the 68 paths clash.

| Group | Rows | Example |
| --- | --- | --- |
| Static routes | 24 | `/about` → `/pages/about`, `/journal/chainstitch` → `/blogs/journal/chainstitch` |
| Legacy numeric product IDs | 25 | `/products/8681284370666` → `/products/margit-one-piece?variant=…` |
| Draft per-print handles | 18 | `/products/margit-one-piece-in-dahlia-seed` → `/products/margit-one-piece?variant=…` |

**Known unknowns (reported, not failures):**
- **Draft product handles:** Shopify may refuse or ignore a redirect whose path belongs to an existing (draft) product. Any rejected row is listed in `apply-log.json`; the fix is then to archive or rename those drafts at cutover.
- **Targets that don't exist yet** (`/pages/about`, `/blogs/journal/…`, `/collections/dresses` …) will show the 404 page on the Shopify-hosted site until Phase 4 pages and the cutover collections exist. That's expected and harmless.

**Run:** `python3 apply.py` → `after.graphql` → spot-check on the Shopify-hosted site (`curl -sI` shows `301` + `location`): `/shop`, `/about`, `/collections/botanicals`, `/products/8681284370666`, `/products/margit-one-piece-in-dahlia-seed` → live diff.

**Rollback:** `python3 rollback.py`: bulk-deletes every created redirect (IDs in `apply-log.json`); the store had none before.

**`/shop` isn't in the list:** Shopify serves the home page at `/shop`, so a redirect there can't fire. The theme now sends `/shop` to `/collections/all` with an instant meta refresh + canonical (theme change, not store data).
