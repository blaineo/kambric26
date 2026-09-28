# Batch 03 finding (2026-09-28): "Online Store only" does NOT hide collections from kambricgoods.com

Read-only queries (`before.json` + the channel check below) found:

| Collection | Published to | Listed on kambricgoods.com |
| --- | --- | --- |
| frontpage | Online Store, Point of Sale, Facebook & Instagram | no (filtered out in the live site's code) |
| psychedelics | Online Store, Facebook & Instagram | yes |
| folklore | Online Store, Facebook & Instagram | yes |
| whimsy | Online Store, Facebook & Instagram | yes |

The store's sales channels are Online Store, Point of Sale, Shop, and Facebook & Instagram. There is **no separate channel for the Replit site**, so the live site's Storefront API token reads what's published to the **Online Store** channel. A collection published to Online Store (the only way the Shopify-hosted theme can show it) **appears on kambricgoods.com**.

**Consequence:** creating the category/sale collections *published* is 🔴, not 🟡. Batch 03 was not run. Docs that said "Online Store only protects the live site" were corrected (OWNER_TASKS B1, CONTENT_GUIDE §3a-A1 and §2b).

**Safe alternative:** create them **unpublished** (no channel at all). Invisible to both sites, so the setup (conditions, templates, descriptions, SEO) is done ahead of time; publishing them to Online Store becomes a one-step 🔴 cutover task. Category pages can still be previewed on the Shopify-hosted site with `/collections/all?view=phase3-category-test`.
