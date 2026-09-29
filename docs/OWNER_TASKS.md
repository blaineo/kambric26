# Owner task list: everything you need to do before launch

**Rule:** until the DNS cutover, **nothing here may change kambricgoods.com** (the live Replit site). Every task is sorted by what it touches:

- **🟢 Safe now:** affects only the Shopify-hosted site (`kambric-goods-2.myshopify.com`) or data the live site never reads.
- **🟡 Safe now if done exactly as written:** touches shared data, but in a way the live site can't see. Each has a check step. Skip any you're unsure about; they can all wait for cutover.
- **🔴 At cutover only:** would change the live site. Do these in the cutover window (§C), not before.

How "safe" was decided: the live site reads products (title, description, type, tags, options, variants, prices, stock, images and **image alt text**), collections (title, description, image, and whichever collections its sales channel can see), five custom fields (`kambric.prints`, `kambric.print_name`, `kambric.print_story`, `kambric.season`, `kambric.year`), and uses Shopify **checkout** (so discounts, shipping, taxes, payments, policies and notifications are shared). Everything else (theme, menus, pages, blog, URL redirects, new custom fields, SEO fields, Online Store preferences) is Shopify-hosted only. Verified against the live site's source, 2026-09-28.

Status: ☐ to do · ◐ partly done (rest at a later step) · ☑ done · ⏳ waiting on the theme build. Tick items here (or tell Claude and it will).

---

## A. Safe now 🟢

### A1. Menus (Content → Menus): guide §3a
- ◐ **Main menu** (`main-menu`): Shop → All products, Collections (+ Folklore, Psychedelics, Whimsy nested, as *collection* links). The category links (Dresses … Sale) wait for the collections to be published at cutover (C2). *(Done, batch 04, 2026-09-28; category links at cutover.)*
- ☐ **Footer menu** (`footer`): the five categories + Sale, at cutover once they're published (C2). Until then leave the default or use All products.
- ☑ **Footer info** (`footer-info`): Contact Us, Wholesale, Size Guide, Shipping, Returns & Exchanges. *(Created batch 04; links added batch 08, 2026-09-29.)*
- ◐ **Shop categories** (`shop-categories`): create now with **All**; add the five categories at cutover (C2). *(Created with All, batch 04.)*
- ☑ Main menu Part B (Story, Events, Journal). *(Batch 08, 2026-09-29.)*

### A2. New custom fields (Settings → Custom data)
New definitions the live site doesn't read.
- ☑ **Product** `kambric.archive_label`, single-line text. Then set **"Parlor Rose"** on Arielle (D-22). *(Done by Claude, batch 01, 2026-09-28.)*
- ☑ **Collection** `kambric.card_image`, file (image). **Collection** `kambric.header_image`, file (image). *(Done, batch 01.)*
- ☑ Upload the six collection images (`../replit site/assets/uploads/`, names in `../liquid/assets/usage-map.csv`) to **Content → Files**, then set Card image + Header image on Folklore, Psychedelics, Whimsy. *(Done, batch 02, 2026-09-28. Whimsy's card image is only 808 px wide; replace with a larger original when you have one.)*
- ☑ **Monogram fee product** (`chainstitch-monogram`): Settings → Custom data → Products → **Add definition**, namespace and key **`seo.hidden`**, type **Integer**; then on the monogram product set it to **1**. This keeps it out of the Shopify-hosted sitemap and search (the theme already hides it from listings). The live site doesn't read this field. *(Done, batch 01.)*

### A3. Search listings (not read by the live site)
- ☑ *(owner, 2026-09-29; social sharing image: not needed, the theme now shares a crop of each page's hero, owner decision 2026-09-29)* **Online Store → Preferences** (🟢, **you type these**: automation can't reach this form; see `store-changes/07-admin-settings/log.md`): *Home page title* `Kambric Goods | Heritage Prints, Modern Womenswear`; *Meta description* `Kambric Goods pairs original mid-century hand-painted prints from the Hartmann Studio archive with modern womenswear and home goods. Designed in the Bay Area, made in limited quantities.` → Save.
- ◐ **Collection search listings** (each collection → *Search engine listing*): titles and descriptions from `docs/store-data/collection-copy.csv` (`seo_title`, `seo_description`). **Don't touch the collection *Description* field yet** (that's 🔴 C2). *(Folklore, Psychedelics, Whimsy done in batch 05, 2026-09-28; the category/sale collections get theirs when batch 03 runs at cutover.)*
- ☐ Product search listings: unique title and description per product (optional before launch).

### A4. Theme editor (Online Store → Themes → Kambric Goods → Customize)
- ☐ **Sale heading:** write current promotion copy (the old "20% off … end of August" is stale). Guide §3d.
- ☐ Review the 404 page, footer text, announcement bar (off by default). Guide §3, §3b.
- ☐ Home, About, Events, Journal content: see A7.

### A5. Store settings that only affect the Shopify-hosted site
- ☑ **Contact form recipients:** nothing to set. Shopify sends contact-form messages (incl. the "Notify me" requests) to the store contact email, already **kambricgoods@gmail.com** (checked 2026-09-28). Changing that email is 🔴 (it's also used for order emails shared with the live site).
- ☑ **URL redirects:** import `docs/redirects-draft.csv` (search "URL redirects" in the admin → Import). They only fire on the Shopify-hosted site. Then spot-check a few old links on `kambric-goods-2.myshopify.com`, including a draft-product one (e.g. `/products/margit-one-piece-in-dahlia-seed`). *(Done, batch 06, 2026-09-28: 67 redirects, all firing, including draft-product handles. `/shop` is handled in the theme.)*
- ☐ **Online Store password:** keep it on until cutover (Online Store → Preferences) if you don't want the preview site public.
- ☐ Testing the footer or pop-up signup creates real customers; use `+test` addresses and delete them after.

### A6. Theme
- ☐ **Publish Kambric26 on the Shopify-hosted Online Store** once the Phase 1 shell is stable (D-21), so content entered there carries over. Tell Claude when; it can run it, or you can use Online Store → Themes → Publish. From then on, the theme editor on the published theme is where editors work.

---

## B. Safe now if done exactly as written 🟡

### B1. Category and sale collections → one step at cutover
The live site reads the **Online Store** channel (no separate Replit channel), so these can't be published early, and creating them unpublished wouldn't save meaningful work. **Decision (2026-09-28): create and publish them in one step at cutover** (C2). The script is ready and dry-run tested: `docs/store-changes/03-category-collections/` (rules verified against the live catalog read-only: Dresses 4, Kaftans 1, Coats 1, Swimwear 1, Accessories 2, Sale 1).
- Until then, preview a category page on the Shopify-hosted site with `/collections/all?view=phase3-category-test`.

### B2. Taxonomy details for the "Product details" list (guide §3c)
- ☐ ⚠️ **Wait until cutover (move to C) unless you've confirmed tax won't change.** Setting a product's **Product category** can change how Shopify calculates tax at checkout, and checkout is shared with the live site. The Category metafields themselves (fabric, neckline, …) are not read by the live site.

---

## C. At cutover only 🔴 (these change the live site)

Do these in the cutover window, just before or right after DNS moves (MIGRATION_PLAN §4.3), in this order.

### C1. Freeze and export
- ☐ Stop editing in the Replit `/admin`; take the final export (content, newsletter subscribers, back-in-stock requests).

### C2. Catalog and collection data (shared)
- ☐ **Category and sale collections:** Claude runs batch 03 (`apply.py --dry-run`, then `apply.py`): creates Dresses, Kaftans, Coats, Swimwear, Accessories and Sale with their templates, copy and rules, and publishes them to Online Store. Then add their links to the menus (A1) and write the Sale copy (A4).
- ☐ **Per-print collections** (MIGRATION_PLAN §3 item 3): delete the `collection` key from Zadie's, Esther's and Vera's `kambric.prints` entries; change Margit's one `"botanicals"` to `"whimsy"`. Fixes the empty Whimsy page. *(It would fix the live site's Whimsy too, so it's the one 🔴 item you might choose to do early.)*
- ☐ **Collection descriptions** for Folklore, Psychedelics, Whimsy: paste `description_to_set` from `docs/store-data/collection-copy.csv`.
- ☐ **Product Category** (taxonomy) and category metafields, if deferred from B2.
- ☐ Normalise journal/product tags if needed (MIGRATION_PLAN §3).

### C3. Checkout, marketing and policies (shared)
- ☐ **Privacy policy and Terms** (Settings → Policies): shown at checkout.
- ☐ **Newsletter and WELCOME15** (D-11): create the WELCOME15 discount (the pop-up shows it after sign-up; blank its *Discount code* setting instead if Shopify Email will send it), welcome email, import subscribers with their consent state.
- ☐ **Back-in-stock** (D-12): stays manual (contact-form emails) at launch; an app is optional later. Import the old requests list and handle it by hand.
- ☐ **Meta Pixel** (D-13): install the Facebook & Instagram channel. It affects checkout events, so do it at cutover.
- ☐ **Cookie banner** (Settings → Customer privacy): decide to keep it or restyle it.

### C4. Go live (MIGRATION_PLAN §4.3)
- ☐ Remove the Online Store password.
- ☐ DNS: point `kambricgoods.com` and `www` to Shopify; set the primary domain (www → apex); wait for SSL.
- ☐ Claude restores the publish/live-push safety rules in the repo (step 9a).
- ☐ Google Search Console: verify with the **HTML tag** method (the tag is already on the home page, theme setting *Google Search Console verification code*), then submit the sitemap (`/sitemap.xml`); same for Bing; watch 404s for 2 weeks.

### C5. After the rollback window (about 14 days)
- ☐ Decommission the Replit tokens and webhooks.
- ☐ Now safe: rewrite product image **alt text** descriptively and move print grouping to variant media (D-8). The Replit site used alt text to group photos.
- ☐ Remove the `hidden`-tag reliance if you prefer unpublishing (MIGRATION_PLAN §3).

---

### A7. Phase 4 content (all 🟢: new Shopify-hosted data the live site never reads)
Full detail and exact values: `docs/store-data/phase4/owner-notes/{home,about-events,journal-info}.md`; import files in `docs/store-data/phase4/`. Claude can run these as batches.
- ☑ *(batch 10, 2026-09-29)* **Photos:** upload the 11 home + 5 About/Events photos to Files; Claude sets them in the templates (`shopify://shop_images/…`), so nothing to pick by hand.
- ☑ **Events:** `kambric_event` definition + the 3 exported events *(batch 08)*. ☐ Add real upcoming events when known (Content → Metaobjects → Event).
- ☑ *(batch 08; info pages each have their own template: `page.contact`, `page.wholesale`, `page.shipping`, `page.returns`)* **Pages:** About (`about`, template `page.about`) and Events (`events`, `page.events`) with empty bodies; Contact, Wholesale, Size Guide (`page.size-guide`), Shipping, Returns with bodies from `pages/*.html`.
- ☑ *(batch 08)* **Journal:** create blog `journal`, import the 5 posts from `journal/posts.json` (cover images, normalised category tags).
- ☑ *(batch 08)* **Menus Part B:** Story, Events, Journal in `main-menu`; the five info pages in `footer-info` (A1).
- **Scopes:** metaobjects, pages and blogs need extra Admin API scopes (`write_metaobject_definitions`, `write_metaobjects`, `write_content`); you'd re-run `shopify store auth` with them added.

### A8. Phase 5 (cart, search, pop-up)
Full notes: `docs/store-data/phase5/owner-tasks-{cart,search,popup}.md`.
- ◐ 🟢 *(image uploaded and pop-up turned on, batch 11)* **Pop-up:** upload its image (`replit site/assets/uploads/57e0fcb8-…jpg`; Claude can set it in the template), review the copy, turn **Newsletter pop-up** on when ready (Customize → Footer).
- ☐ 🟢 Optional: Shopify's **Search & Discovery** app for synonyms and search analytics.
- Cart: nothing to do (checkout settings are shared 🔴 and untouched).

## Coming later (added as phases land)

*Maintained by Claude alongside the build: any phase that creates owner work adds it here in the same commit.*
