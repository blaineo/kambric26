# Batch 07 log: paused — owner to type the two fields

**2026-09-29 retry (owner: "go for batch 07"):** the Preferences form lives in a cross-origin frame (`online-store-web.shopifyapps.com`), invisible to Chrome automation's element tools. After clicking the Home page title field, the frame had focus but the input didn't: the typed text went to Shopify's admin keyboard shortcuts and opened **Add page** (same as the 2026-09-28 attempt). Closed without saving.

**Checked after:** no page created (still 8), no product/collection updated since 2026-09-28, Preferences unsaved, kambricgoods.com diff clean. No store change was made by this batch.

**Decision:** don't retry by automation. Owner enters the two values (below) in about a minute. Until then the theme already outputs the target meta description (fallback in `snippets/meta-tags.liquid`); only the home `<title>` differs ("Kambric Goods").

| Field (Online Store → Preferences → Social sharing image and SEO) | Value |
| --- | --- |
| Home page title | `Kambric Goods | Heritage Prints, Modern Womenswear` |
| Meta description | `Kambric Goods pairs original mid-century hand-painted prints from the Hartmann Studio archive with modern womenswear and home goods. Designed in the Bay Area, made in limited quantities.` |
