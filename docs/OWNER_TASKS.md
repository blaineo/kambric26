# Owner task list: everything you need to do before launch

**Rule:** until the DNS cutover, **nothing here may change kambricgoods.com** (the live Replit site). Every task is sorted by what it touches:

- **🟢 Safe now:** affects only the Shopify-hosted site (`kambric-goods-2.myshopify.com`) or data the live site never reads.
- **🟡 Safe now if done exactly as written:** touches shared data, but in a way the live site can't see. Each has a check step. Skip any you're unsure about; they can all wait for cutover.
- **🔴 At cutover only:** would change the live site. Do these in the cutover window (§C), not before.

How "safe" was decided: the live site reads products (title, description, type, tags, options, variants, prices, stock, images and **image alt text**), collections (title, description, image, and whichever collections its sales channel can see), five custom fields (`kambric.prints`, `kambric.print_name`, `kambric.print_story`, `kambric.season`, `kambric.year`), and uses Shopify **checkout** (so discounts, shipping, taxes, payments, policies and notifications are shared). Everything else (theme, menus, pages, blog, URL redirects, new custom fields, SEO fields, Online Store preferences) is Shopify-hosted only. Verified against the live site's source, 2026-09-28.

Status: ☐ to do · ☑ done · ⏳ waiting on the theme build. Tick items here (or tell Claude and it will).

---

## A. Safe now 🟢

### A1. Menus (Content → Menus): guide §3a
- ☐ **Main menu** (`main-menu`): Shop (+ Dresses, Kaftans, Coats, Swimwear, Accessories, Sale nested), Collections (+ Folklore, Psychedelics, Whimsy nested, as *collection* links). The category links need the collections from B1; add those after.
- ☐ **Footer menu** (`footer`): the five categories + Sale (after B1).
- ☐ **Footer info** (`footer-info`): create now, empty. ⏳ Add Contact, Wholesale, Size Guide, Shipping, Returns once the pages exist (Phase 4).
- ☐ **Shop categories** (`shop-categories`): All + the five categories (after B1).
- ⏳ Main menu Part B (Story, Events, Journal) once Phase 4 pages exist.

### A2. New custom fields (Settings → Custom data)
New definitions the live site doesn't read.
- ☑ **Product** `kambric.archive_label`, single-line text. Then set **"Parlor Rose"** on Arielle (D-22). *(Done by Claude, batch 01, 2026-09-28.)*
- ☑ **Collection** `kambric.card_image`, file (image). **Collection** `kambric.header_image`, file (image). *(Done, batch 01.)*
- ☑ Upload the six collection images (`../replit site/assets/uploads/`, names in `../liquid/assets/usage-map.csv`) to **Content → Files**, then set Card image + Header image on Folklore, Psychedelics, Whimsy. *(Done, batch 02, 2026-09-28. Whimsy's card image is only 808 px wide; replace with a larger original when you have one.)*
- ☑ **Monogram fee product** (`chainstitch-monogram`): Settings → Custom data → Products → **Add definition**, namespace and key **`seo.hidden`**, type **Integer**; then on the monogram product set it to **1**. This keeps it out of the Shopify-hosted sitemap and search (the theme already hides it from listings). The live site doesn't read this field. *(Done, batch 01.)*

### A3. Search listings (not read by the live site)
- ☐ **Online Store → Preferences:** homepage title `Kambric Goods | Heritage Prints, Modern Womenswear` and the description from `../liquid/SEO.md`.
- ☐ **Collection search listings** (each collection → *Search engine listing*): titles and descriptions from `docs/store-data/collection-copy.csv` (`seo_title`, `seo_description`). **Don't touch the collection *Description* field yet** (that's 🔴 C2).
- ☐ Product search listings: unique title and description per product (optional before launch).

### A4. Theme editor (Online Store → Themes → Kambric Goods → Customize)
- ☐ **Sale heading:** write current promotion copy (the old "20% off … end of August" is stale). Guide §3d.
- ☐ Review the 404 page, footer text, announcement bar (off by default). Guide §3, §3b.
- ⏳ Home, About, Events, Journal content (Phase 4).

### A5. Store settings that only affect the Shopify-hosted site
- ☐ **Contact form recipients** (Settings → Notifications → Staff notifications → Contact form): the "Notify me" back-in-stock requests arrive here. The live site doesn't use Shopify's contact form.
- ☐ **URL redirects:** import `docs/redirects-draft.csv` (search "URL redirects" in the admin → Import). They only fire on the Shopify-hosted site. Then spot-check a few old links on `kambric-goods-2.myshopify.com`, including a draft-product one (e.g. `/products/margit-one-piece-in-dahlia-seed`).
- ☐ **Online Store password:** keep it on until cutover (Online Store → Preferences) if you don't want the preview site public.
- ☐ Testing the footer or pop-up signup creates real customers; use `+test` addresses and delete them after.

### A6. Theme
- ☐ **Publish Kambric26 on the Shopify-hosted Online Store** once the Phase 1 shell is stable (D-21), so content entered there carries over. Tell Claude when; it can run it, or you can use Online Store → Themes → Publish. From then on, the theme editor on the published theme is where editors work.

---

## B. Safe now if done exactly as written 🟡

### B1. Create the category and sale collections (guide §3a-A1, §2b)
Safe **only** if each new collection is published to the **Online Store channel only**; the live site lists every collection its own channel can see.
- ☐ Automated collections **Dresses, Kaftans, Coats, Swimwear, Accessories** (Product type is equal to …, plus Product tag is not equal to `hidden`) and **Sale** (Compare-at price is greater than 0, plus the `hidden` rule).
- ☐ In each collection's **Publishing** card: **Online Store only**; untick every other channel.
- ☐ **Theme template:** `category` for the five, `sale` for Sale.
- ☐ Paste descriptions and search listings from `docs/store-data/collection-copy.csv` (these are new collections, so their descriptions are safe to fill).
- ☐ **Check:** open https://kambricgoods.com/collections and the header's Collections menu. **None of the new collections may appear.** If one does, set its Publishing back to Online Store only (or delete it) and tell Claude.

### B2. Taxonomy details for the "Product details" list (guide §3c)
- ☐ ⚠️ **Wait until cutover (move to C) unless you've confirmed tax won't change.** Setting a product's **Product category** can change how Shopify calculates tax at checkout, and checkout is shared with the live site. The Category metafields themselves (fabric, neckline, …) are not read by the live site.

---

## C. At cutover only 🔴 (these change the live site)

Do these in the cutover window, just before or right after DNS moves (MIGRATION_PLAN §4.3), in this order.

### C1. Freeze and export
- ☐ Stop editing in the Replit `/admin`; take the final export (content, newsletter subscribers, back-in-stock requests).

### C2. Catalog and collection data (shared)
- ☐ **Per-print collections** (MIGRATION_PLAN §3 item 3): delete the `collection` key from Zadie's, Esther's and Vera's `kambric.prints` entries; change Margit's one `"botanicals"` to `"whimsy"`. Fixes the empty Whimsy page. *(It would fix the live site's Whimsy too, so it's the one 🔴 item you might choose to do early.)*
- ☐ **Collection descriptions** for Folklore, Psychedelics, Whimsy: paste `description_to_set` from `docs/store-data/collection-copy.csv`.
- ☐ **Product Category** (taxonomy) and category metafields, if deferred from B2.
- ☐ Normalise journal/product tags if needed (MIGRATION_PLAN §3).

### C3. Checkout, marketing and policies (shared)
- ☐ **Privacy policy and Terms** (Settings → Policies): shown at checkout.
- ☐ **Newsletter and WELCOME15** (D-11): discount code, welcome email, import subscribers with their consent state.
- ☐ **Back-in-stock** (D-12): stays manual (contact-form emails) at launch; an app is optional later. Import the old requests list and handle it by hand.
- ☐ **Meta Pixel** (D-13): install the Facebook & Instagram channel. It affects checkout events, so do it at cutover.
- ☐ **Cookie banner** (Settings → Customer privacy): decide to keep it or restyle it.

### C4. Go live (MIGRATION_PLAN §4.3)
- ☐ Remove the Online Store password.
- ☐ DNS: point `kambricgoods.com` and `www` to Shopify; set the primary domain (www → apex); wait for SSL.
- ☐ Claude restores the publish/live-push safety rules in the repo (step 9a).
- ☐ Submit the sitemap to Google Search Console and Bing; watch 404s for 2 weeks.

### C5. After the rollback window (about 14 days)
- ☐ Decommission the Replit tokens and webhooks.
- ☐ Now safe: rewrite product image **alt text** descriptively and move print grouping to variant media (D-8). The Replit site used alt text to group photos.
- ☐ Remove the `hidden`-tag reliance if you prefer unpublishing (MIGRATION_PLAN §3).

---

## Coming later (added as phases land)
- ⏳ Phase 4: create Pages (About, Events, Contact, Wholesale, Size guide, Shipping, Returns) 🟢, the Journal blog and its 5 posts 🟢, Events metaobjects 🟢.
- ⏳ Phase 5: pop-up and search settings 🟢, cart copy 🟢.

*Maintained by Claude alongside the build: any phase that creates owner work adds it here in the same commit.*
