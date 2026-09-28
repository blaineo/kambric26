# Batch 07: Online Store preferences (🟢, admin UI in Chrome)

**Where:** Online Store → Preferences → *Social sharing image and SEO* (no Admin API for these fields).

**Before** (read in the admin, 2026-09-28):
| Field | Current value |
| --- | --- |
| Home page title | *(empty; placeholder shows the domain)* |
| Meta description | *(empty)* |
| Social sharing image | *(none; the theme falls back to its bundled `og-default.jpg`)* |
| Password protection | **off** (the Shopify-hosted site is publicly reachable) |

**Change** (values from `liquid/SEO.md`, the current site's home head):
| Field | New value |
| --- | --- |
| Home page title | `Kambric Goods | Heritage Prints, Modern Womenswear` (51/70) |
| Meta description | `Kambric Goods pairs original mid-century hand-painted prints from the Hartmann Studio archive with modern womenswear and home goods. Designed in the Bay Area, made in limited quantities.` |

**Why it's 🟢:** these feed only the Shopify-hosted storefront's `<title>` / meta description (and the Storefront API `shop.description`). The live site's code never queries the shop object (checked in its source), and it renders its own head.

**Dropped from this batch** (docs corrected):
- *Contact-form recipients*: there's no separate setting. Contact-form messages (incl. "Notify me") go to the store contact email, already **kambricgoods@gmail.com**. Changing it would be shared (order emails), so it stays.
- *Staff notification recipients* are order notifications, shared with the live site's checkout: not touched.

**Optional (your call):** turn **Password protection** on so the Shopify-hosted preview isn't public before launch. 🟢 (the live site doesn't use the Online Store storefront). Staff theme previews keep working. It must be turned off at cutover (already in OWNER_TASKS C4).

**Rollback:** re-open Preferences and clear the two fields (their "before" values were empty); turn password protection back off if it was turned on.

**Verify:** the Shopify-hosted home page `<title>` and meta description; the live diff.
