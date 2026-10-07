# Batch 18 log: GSC cleanup ✅ (2026-10-07)

- **Approved:** owner ("approve batch 18").
- **Applied:** 2026-10-07T17:11:43Z (`apply-log.json`):
  - 14 URL redirects (`redirects.csv`), all verified live in one hop. `/blogs/news` → `/blogs/journal` live since the owner deleted the empty News blog (2026-10-07).
  - `seo.hidden = 1` on the automatic `frontpage` collection: gone from the sitemap.
  - Article field definition `kambric.products` ("Products in this story", list of products, storefront-readable) + values: arielle-dress → Arielle Slip Dress; chainstitch → Goldie Bandana, Bodie Scarf.
- **Verified (dev theme, live after the theme push):** Chainstitch post shows Goldie + Bodie under "Products in this story"; Arielle, Goldie and Bodie product pages show a "From the Journal" link to their post.
- **Still 404 by decision:** 2 napkin sets, 5 unidentified random-ID URLs, `/home/home-goods`, `/stockists` (see `url-mapping.md`).
- **Rollback:** `python3 rollback.py`.
