# OWNER_TASKS.md addition — Search (Phase 5, D-15)

Suggested placement: under the 🟢 (safe now, Shopify-hosted only) section.

---

🟢 **Search & Discovery app — synonyms and search analytics (optional).**
Shopify's free **Search & Discovery** app (Apps → Search & Discovery, or install it
from the App Store if it isn't already there) can improve match quality with zero
theme changes:
- Add synonyms so alternate wording finds the right piece (e.g. "jumpsuit" ↔
  "one-piece"; a colorway's common nickname ↔ its official print name).
- Check the **search analytics** report periodically for searches that returned zero
  results — a direct list of tags/synonyms worth adding.
- Optionally **pin/boost** a product for a specific search term (e.g. keep a
  best-seller near the top for its category name).

This affects only the Shopify-hosted Online Store's search behavior (`/search` and the
predictive search overlay) — it doesn't touch product data, doesn't affect the live
Replit site, and is fully reversible (remove the synonym/rule). Safe to do at any time,
in any batch size, no snapshot/rollback process needed since nothing here is store data
in the CLAUDE.md guardrail-9/10 sense (it's app configuration, not product/collection/
metafield data).

No other owner action is required for Phase 5 search: the monogram add-on is already
excluded from listings/search by its `hidden` tag (existing behavior, unchanged), and
`/search` is already `noindex`.
