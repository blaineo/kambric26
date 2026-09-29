# Indexing audit: kambricgoods.com on Shopify (2026-09-29)

Checked live, after DNS cutover, with a Googlebot user agent.

## ✅ Healthy
- **Primary domain** `kambricgoods.com`; `www.` and `kambric-goods-2.myshopify.com` 301 to it.
- **No blocking headers:** no `X-Robots-Tag` on content pages (only Shopify's on `/search`).
- **robots.txt:** Shopify defaults (block cart/checkout/account/search/sort/preview URLs, allow everything else) + explicit allow groups for GPTBot, ClaudeBot, PerplexityBot, Google-Extended, OAI-SearchBot; `Sitemap: https://kambricgoods.com/sitemap.xml`.
- **Sitemap:** 35 content URLs (home, 9 products, 8 pages, 10 collections, journal + 5 posts) + Shopify's `/agents.md`. Every one returns 200, has no noindex, and a self-referencing canonical on kambricgoods.com.
- **Canonicals:** `?variant=` and `/collections/…/products/…` → the product; filtered collections → the unfiltered collection; `/shop` → `/collections/all`; pagination → itself.
- **Legacy Replit URLs** (`/about`, `/shop/dresses`, `/sale`, `/journal/<post>`, `/products/<old id>`) redirect to their new pages (67 URL redirects).
- **Store-level "hide from search" (`seo.hidden`):** only `chainstitch-monogram` (intended). No leftover Replit-era hiding on products, collections, pages or posts.
- **Intentional noindex:** cart, search, 404, password/gift card/captcha, customer pages, an empty blog, hidden products.

## ⚠️ Fixed / to fix
| Item | Issue | Fix |
| --- | --- | --- |
| Theme | `seo.hidden` only produced noindex on products | ✅ Now on products, collections, pages, posts, blogs (Shopify also adds its own `noindex,nofollow`) |
| `/collections/frontpage` | Shopify's automatic "Home page" collection: in the sitemap and indexable, but duplicates products and is linked nowhere | Set `seo.hidden = 1` on it (store change) |
| `/blogs/news` | Shopify's default empty blog: in the sitemap but noindex ("Submitted URL marked noindex" in Search Console) | Delete the empty blog, or add a post / hide it (store change) |
| Policies | `/policies/*` is disallowed by Shopify's default robots.txt | Fine (standard); nothing to do |

## After launch
Verify the domain in Search Console (HTML tag already on the home page), submit `https://kambricgoods.com/sitemap.xml`, use URL Inspection on the home page and one product, and watch *Pages → Not indexed* for two weeks. If the old site had used Search Console removals for the Shopify URLs, check *Removals* and cancel any still active.
