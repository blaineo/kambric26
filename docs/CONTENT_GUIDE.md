# Kambric Goods: content guide for the new Shopify site

**Who this is for:** anyone who updates words, photos, events, journal posts or menus on kambricgoods.com.
**What's happening:** the site is moving from the custom Replit app (with its own `/admin` page) to a Shopify theme. After the switch, **everything is edited in the Shopify admin**, the same place products are managed today. There is one login, one place to look, and no separate website admin.

This guide is updated with every build phase. The [change log](#change-log) at the bottom lists what's new each time.

> **Status:** the new theme is in development. Keep using the current `/admin` page for the live site until launch day.
>
> **Two websites, one Shopify store (until launch):**
> - **kambricgoods.com** is still the current (Replit) site, and it **reads products, collections and checkout from this Shopify store**. Changing a product, price, product photo, collection or discount in Shopify changes the live site **immediately**.
> - **kambric-goods-2.myshopify.com** is the new Shopify-hosted site. It's our **practice space**: no customers go there, so theme edits, menus, pages and blog posts there are safe to experiment with.
> - **Launch = switching the web address.** On launch day kambricgoods.com is pointed at the Shopify-hosted site. Everything you set up there beforehand carries over as-is.

**Safe to change now** (only affects the practice site): the theme editor (Customize), menus, pages, blog posts, theme settings.
**Also changes the live site right away:** products (text, prices, photos, **photo alt text**, tags, product type), collections (new ones, and their *Publishing* channels), discounts, checkout, shipping and policies. The steps in this guide call these out with ⚠️.

---

## 1. The short version

New to the shop's structure? Start with **§2b How the shop is organized**. The one-time setup before launch is a checklist in [`OWNER_TASKS.md`](./OWNER_TASKS.md).

| You used to… (Replit `/admin`) | After launch you'll… (Shopify admin) | Ready? |
| --- | --- | --- |
| Toggle and edit the **announcement banner** | **Online Store → Themes → Customize** → the *Announcement bar* at the top of any page | ✅ Now |
| (Couldn't edit) the **header and footer links** | **Content → Menus**: `Main menu`, `Footer` (Shop column), `Footer info` (Information column) | ✅ Now |
| (Couldn't edit) the **footer blurb, "Stay close" heading, location line** | **Customize** → *Footer* | ✅ Now |
| Upload a **footer logo** | **Customize → Theme settings → Logo and brand** (one logo for header and footer) | ✅ Now |
| (Couldn't edit) **colours, social links, favicon, sharing image** | **Customize → Theme settings** | ✅ Now |
| Edit the **homepage hero, story, quote image** | **Customize** → Home page sections | Phase 4 |
| Edit the **About page** text, photos, value cards | **Customize** → About page sections | Phase 4 |
| Add, edit and reorder **events** | **Content → Metaobjects → Events** | Phase 4 |
| Write **journal posts** (Markdown) | **Content → Blog posts → Journal** (visual editor, no Markdown) | Phase 4 |
| Set **collection cover and header images** | **Products → Collections → (collection) → Metafields**: *Card image* and *Header image* | ✅ Phase 3 |
| Edit **info pages** (contact, shipping, returns, size guide, wholesale) | **Online Store → Pages** (these were locked in code before; now you can edit them) | Phase 4 |
| Edit **privacy policy and terms** | **Settings → Policies** | Phase 4 |
| Change the **newsletter pop-up** image | **Customize** → Pop-up section | Phase 5 |
| Download **newsletter subscribers** | **Customers** → filter *Email subscribed* (or the tag `newsletter`) → Export | ✅ Footer form now; pop-up Phase 5 |
| Manage **back-in-stock requests** | Requests arrive as contact-form emails; you notify customers by hand (an app can automate this later) | ✅ Phase 2 |
| Edit **products, prices, inventory, print names/stories** | Same as today: **Products** | No change |

---

## 2. How editing works in Shopify

- **Theme editor** ("Customize"): **Online Store → Themes → (Kambric Goods theme) → Customize**. You see the page as visitors will and can click any section to edit it. Changes are saved as a draft until you press **Save**. On the live theme, Save publishes immediately.
- **Sections and blocks:** each page is a stack of *sections* (e.g. Header, Footer). Some sections contain *blocks* (e.g. each footer column is a block) that can be added, removed, reordered or hidden with the eye icon.
- **Menus:** **Content → Menus**. Drag links to reorder. Drag a link *under and to the right of* another to nest it (that makes a dropdown).
- **Files:** **Content → Files** holds uploaded images. Images you pick in the theme editor are stored here.
- **Before launch:** you'll work on the Shopify-hosted practice site (`kambric-goods-2.myshopify.com`). The developer will tell you when the new theme is ready there to receive content. Until then the developer may replace it, so hold off on entering real content. Please leave publishing and theme switching to the developer.

---

## 2b. How the shop is organized

Read this once; the rest of the guide builds on it.

### The building blocks
```
Collection (Folklore, Psychedelics, Whimsy)   ← a family of prints, curated by you
   └── Print (Matyó Floral, Dahlia Seed, …)    ← shown as its own card
          └── Product (Margit One-Piece, Kati Slip Dress, …) in sizes

Category (Dresses, Kaftans, Coats, Swimwear, Accessories)  ← automatic, from the product's "Type"
Sale                                                      ← automatic, from compare-at prices
```
- **Product**: what you sell, managed under **Products** as today. A product either has several prints (a *Print* or *Colorway* option, like Margit or Arielle) or is a single print (like Kati Slip Dress in Matyó Floral).
- **Print**: every print gets its **own card** in listings, with its own photo, price and sale or sold-out badge. Clicking it opens the product with that print selected.
- **Collection**: an editorial family of prints (Folklore, Psychedelics, Whimsy). **You** decide which products belong, on the product or collection page in the admin. A print shows up in its product's collection. Only a product whose prints belong to *different* collections (today: Margit) sets the collection per print.
- **Category**: a collection Shopify fills **automatically** from each product's **Type** field (Dresses, Kaftans, …). You never add products to a category by hand; set the product's Type and it appears.
- **Sale**: also automatic. A print appears on the sale page when its price is lower than its **compare-at price**.

### Where each one appears on the site
| Page | Address | What it shows | How it's organized |
| --- | --- | --- | --- |
| Shop | `/collections/all` | Every print | Grouped by collection, one **Collection block** per group, in the order you drag them |
| Category | `/collections/dresses` … | That category's prints | Grouped by collection, the same way |
| Collection | `/collections/folklore` … | That collection's prints | One grid, collection header on top |
| Sale | `/collections/sale` | Prints on sale, any collection | One grid |
| Collections | `/collections` | A card per collection (those with a *Season*) | Alphabetical, unless you pick collections and their order in the section's *Collections to show* |

### Common tasks
⚠️ = before launch, this also changes the live kambricgoods.com (products, collections and prices are shared).

**Add a new collection** (e.g. "Garden Party")
1. ⚠️ **Products → Collections → Create collection**: title, description (shown as the group text on the shop page and in the collection header), *Manual* type. Under *Publishing*: **before launch, no channels at all** (the live site reads the Online Store channel); after launch, **Online Store**. Set **Season** and **Year**, then **Card image** and **Header image**.
2. Add products: on each product, add the collection under **Collections**, or add them from the collection page.
3. Show it as a group: **Online Store → Themes → Customize** → template picker at the top → **Collections → Default collection** → *Product listing* (the one shown on the shop page) → **Add block → Collection** → pick it → drag it into place. Repeat on the **category** template. Until you do this, its prints still appear at the end of those pages under "other pieces", so nothing goes missing.
4. It appears on `/collections` automatically once it has a Season.

**Put a product in a collection or move it** ⚠️
Edit the product → *Collections*. If a product's prints belong to different collections (like Margit), ask the developer; that's set per print.

**Reorder collections on the shop and category pages**
Customize → **Default collection** (and **category**) template → *Product listing* → drag the Collection blocks.

**Change the order of cards inside a collection** ⚠️
Products → Collections → the collection → **Sort** (e.g. *Manually*, then drag). To put one product first on a single page without changing the collection, use **Show these first** in that page's *Product listing*.

**Rename or retire a collection** ⚠️
- Rename: edit the title. If you also change its web address (*Search engine listing → URL handle*), keep **"Create a URL redirect"** ticked.
- Retire: remove its Collection block from the templates, then set the collection's *Publishing* to off (or delete it). Add a URL redirect (search "URL redirects" in the admin) from its old address to `/collections` so old links still work.

**Add a new category** (e.g. "Tops") ⚠️
1. Create an **automated** collection "Tops": condition *Product type is equal to Tops* plus *Product tag is not equal to hidden*. Publishing: unpublished before launch, Online Store after (see §3a-A1).
2. Set its **Theme template** to **category**, then add its description and search listing.
3. Add it to the **Shop categories** menu (Content → Menus) so it appears in the category strip, and to the footer menu if you like.
4. Set **Type = Tops** on the products.

**Put something on sale or take it off** ⚠️
On the product's variants, set a **compare-at price** higher than the price (on sale) or clear it (off sale). Sale badges, the sale page and struck-through prices update automatically. The sale page's heading is set in Customize (a *sale* collection).

**Hide or remove a product** ⚠️
- **Draft** (product *Status*): gone from the site entirely, including its page. Use this for products that aren't ready or are discontinued.
- **Tag `hidden`**: stays purchasable by link but never appears in listings or search (used for the monogram fee). Rarely needed otherwise.
- **Archived**: like Draft, but kept out of your product list.

### What happens automatically (no setting to look for)
Sold-out and Sale badges, "N pieces" counts, which photo a print card shows (see §3b), search-engine descriptions of every listing, and the "other pieces" safety net for collections that don't have a block yet.

## 3. What you can edit right now (Phase 0)

### Announcement bar

The thin terracotta strip above the header, on every page. It's **off** today, matching the current site.

> **Where you edit it:** on the Kambric Goods theme (**Online Store → Themes → Kambric Goods → Customize**). Before launch, that only changes the practice site; after launch, it's the real site. The live kambricgoods.com bar is still edited in the Replit `/admin` until launch.

**Turn it on**
1. Go to **Online Store → Themes**. On the *Kambric Goods* theme, click **Customize**.
2. In the left sidebar under **Header**, click **Announcement bar**. (If you don't see it, click the eye icon next to it: the section itself might be hidden.)
3. Tick **Show announcement**.
4. Fill in **Message** (see "Change what it says" below).
5. Click **Save** (top right). On the live theme, it's on the site immediately.

**Turn it off**
1. Open **Customize → Announcement bar** as above.
2. Untick **Show announcement** and click **Save**.

Your message, link and style are kept, so next time you only need to tick the box again. (Don't use the eye icon to hide it; the checkbox is the switch.)

**Change what it says**

| Field | What to enter | Example |
| --- | --- | --- |
| **Message** | The announcement. Aim for under ~45 characters so it fits on one line on phones. Use " · " to separate phrases. | `Summer Sale · 20% Off Select Styles` |
| **Link label** | Optional underlined words after the message. Shown only when there's a link, and hidden on small phones (the whole bar is still clickable). | `Shop Now` |
| **Link** | Where a click goes. Click the field and search for a collection, product, page or blog post, or paste a web address. Leave empty for a bar that isn't a link. | *Sale* collection |
| **Style** | **Static** (centred, like today) or **Scrolling** (moves slowly right to left). | Static |

Tips:
- **Scrolling** repeats your message across the bar, pauses when someone hovers over it, and stays still for visitors whose device is set to reduce motion. Screen readers read it once.
- There's no built-in scheduler. For a sale that starts or ends at a set time, set yourself a reminder to switch it on and off.
- The colour is the theme's terracotta, slightly darkened so the small text passes accessibility contrast. Changing *Theme settings → Colors → Secondary* changes it too.
- Discount codes in the bar are visible to everyone, so only put public codes there.

### Header menu
*Content → Menus → Main menu* (handle `main-menu`). One-time setup is in [section 3a](#3a-setting-up-the-menus-one-time-before-launch).

- Top-level links appear across the header on desktop and in the full-screen **Menu** on phones.
- Links nested under a top-level link become its **dropdown**.
- If a dropdown contains **only collections**, it's shown in the large italic style (like "Collections" today). Otherwise it uses the small uppercase style (like "Shop").
- On phones, a dropdown of plain links (e.g. Shop → Dresses, Kaftans…) is listed directly in the menu, just like today.

### Footer
*Customize → Footer*

- **Brand text and social:** the short description under the logo, plus Instagram and Pinterest icons. Their web addresses are under *Theme settings → Social media*.
- **Menu columns:** each column shows one menu. Today's site has **Shop** (menu `footer`) and **Information** (menu `footer-info`: Contact Us, Wholesale, Size Guide, Shipping, Returns & Exchanges). Leave the heading blank to use the menu's own name.
- **Newsletter signup:** the "Stay close" heading. Sign-ups become **customers** in Shopify with email marketing consent and the tag `newsletter`.
- **Location text:** "Northern California" in the bottom line. The Privacy Policy and Terms links appear automatically once those policies are filled in under *Settings → Policies*.

### Theme settings
*Customize → ⚙ Theme settings*

| Group | Settings | Notes |
| --- | --- | --- |
| Logo and brand | Logo, logo height (desktop/mobile), favicon, default social sharing image | Leave the logo empty to use the built-in bronze wordmark. The sharing image is used when a page has none (1200 × 630 px). |
| Colors | Ivory background, cocoa text, ochre, terracotta, olive, linen, dark band | Pre-set to today's palette. **Change with care:** text must stay readable against its background. |
| Social media | Instagram URL, Pinterest URL | Also tells Google these profiles belong to Kambric Goods. |

---

## 3a. Setting up the menus (one time, before launch)

The theme reads three menus. Shopify identifies each by its **handle** (a fixed internal name), so the handles must be exactly:

| Menu | Handle | Used for |
| --- | --- | --- |
| Main menu | `main-menu` | Header navigation and the phone menu |
| Footer menu | `footer` | Footer column **Shop** |
| Footer info | `footer-info` | Footer column **Information** |
| Shop categories | `shop-categories` | The category strip on the shop and category pages: **All** (`/collections/all`), **Dresses**, **Kaftans**, **Coats**, **Swimwear**, **Accessories** (the category collections from A1). Create it after A1, top-level links only. |

Some links point at things that don't exist in Shopify yet (category collections, the About/Events pages, the Journal). Do **Part A** now and **Part B** when those pages are built (Phase 4).

> ⚠️ **Protect the live site.** Today's kambricgoods.com (the Replit site) reads collections through the same **Online Store** sales channel as this theme, so **any collection published to Online Store appears on the live site right away.** Before launch, create new collections **unpublished** (no sales channels) and publish them at launch. Menus and pages are safe: the live site doesn't read them.

> ℹ️ Menus only affect the Shopify-hosted practice site, so editing them is safe.

### Part A: now

**A1. Create the category collections** (needed for the Shop links; decision D-10). Repeat for each row:

| Title | Condition |
| --- | --- |
| Dresses | Product type · is equal to · `Dresses` |
| Kaftans | Product type · is equal to · `Kaftans` |
| Coats | Product type · is equal to · `Coats` |
| Swimwear | Product type · is equal to · `Swimwear` |
| Accessories | Product type · is equal to · `Accessories` |
| Sale | Compare-at price · is greater than · `0` |

1. Go to **Products → Collections → Create collection**.
2. **Title:** as in the table (e.g. `Dresses`).
3. **Collection type:** choose **Automated**.
4. **Conditions:** "Products must match **all conditions**". Add the condition from the table, then **Add another condition**: *Product tag · is not equal to · `hidden`*.
5. ⚠️ **Publishing** (right-hand card) → **Manage** → **untick every channel**, so the collection is unpublished. Before launch it must stay unpublished: publishing to Online Store would show it on kambricgoods.com. Publish it to **Online Store** on launch day.
6. Scroll to **Search engine listing** → **Edit**. Check the URL ends in `/collections/dresses` (lowercase, matching the title). Fix the handle there if needed.
7. Click **Save**.
8. Check that https://kambricgoods.com/collections does **not** list the new collection. If it does, it's published somewhere: untick its channels, and tell the developer.

**A2. Main menu** (`main-menu`: it already exists in every Shopify store)
1. Go to **Content → Menus** and click **Main menu**.
2. Delete the default items (e.g. *Home*, *Catalog*, *Contact*): click the item's **⋯** (or trash) icon → **Delete**.
3. Click **Add menu item**:
   - **Label** `Shop`, **Link** → click the field → **Collections** → **All products** (`/collections/all`) → **Add**.
4. Click **Add menu item** under *Shop* ("Add menu item to Shop"), or add it at the top level and drag it **under and slightly to the right of** *Shop* to nest it. Add, in order:
   `Dresses`, `Kaftans`, `Coats`, `Swimwear`, `Accessories`, `Sale`, each linked to its collection from A1.
5. Add top-level **Label** `Collections` → **Link** → **Collections** → **All collections** (`/collections`).
6. Nest under *Collections*: `Folklore`, `Whimsy`, `Psychedelics`, each linked to its **collection**. They must be collection links (not typed web addresses): that's what gives them the large italic dropdown style.
7. Click **Save menu**.
8. Check the **Handle**: on the menu's page, it should read `main-menu`. If there's no Handle field, it's fine, because the default Main menu always has that handle.

**A3. Footer menu** (`footer`: also exists by default)
1. **Content → Menus → Footer menu**.
2. Delete the default items (e.g. *Search*).
3. Add, top level and in order: `Dresses`, `Kaftans`, `Coats`, `Swimwear`, `Accessories`, `Sale`, linked to the collections from A1.
4. **Save menu.** (The column heading "Shop" is set in the theme, not by the menu's name.)

**A4. Footer info menu** (`footer-info`: new)
1. **Content → Menus → Create menu**.
2. **Title:** `Footer info`. Shopify creates the handle `footer-info` from the title. If a Handle field is shown, make sure it reads exactly `footer-info`.
3. Leave it without items for now (the pages arrive in Phase 4). An empty menu is simply hidden in the footer.
4. **Save menu.**

**A5. Check it**
Open the theme preview link the developer shares (or **Customize** on the Kambric Goods theme). You should see *SHOP ⌄* and *COLLECTIONS ⌄* in the header with working dropdowns, a Shop column in the footer, and the same list in the phone **Menu**.

### Part B: when the pages exist (Phase 4)

The developer will confirm when these exist; then add:

| Menu | Label | Link to |
| --- | --- | --- |
| Main menu (top level, after Collections) | `Story` | Pages → *About* |
|  | `Events` | Pages → *Events* |
|  | `Journal` | Blogs → *Journal* |
| Footer info | `Contact Us` | Pages → *Contact* |
|  | `Wholesale` | Pages → *Wholesale* |
|  | `Size Guide` | Pages → *Size guide* |
|  | `Shipping` | Pages → *Shipping* |
|  | `Returns & Exchanges` | Pages → *Returns* |

After that, the header and footer match today's site exactly.

---

## 3b. Page building blocks, product cards and the 404 page (Phase 1)

### Blocks you can add to sections
Where a section says **Add block**, these are available:

| Block | What it's for | Key settings |
| --- | --- | --- |
| **Heading** | Serif headings, with an optional italic second line (e.g. "Her legacy," / *"carried on."*). This replaces the old `*italic*` trick. | **Heading level (SEO):** use H1 once per page for the page title, H2/H3 everywhere else. **Size** is separate, so pick whatever looks right. |
| **Text** | Paragraphs with bold, italic, links and lists | Style: body / lead (larger) / small |
| **Button** | Links styled as buttons | Style: *Outline* (boxed), *Solid* (filled), *Text with arrow* ("Shop the Collection →"), *Underline* (404 links). Turn on **Use light text** on dark photos or bands. |
| **Eyebrow** | The small uppercase label above headings | **Show ornament** adds the dashes: "— New Arrivals —" |
| **Image** | A photo | **Loading:** leave *Lazy* unless the image is at the top of the page. Use **Priority** for the single biggest image at the top of a page, at most once per page. **Crop:** natural, square, portrait, landscape, wide. |
| **Group** | Puts blocks side by side or stacked | Direction, gap, padding, alignment |

Rich text in pages and journal posts is styled automatically, including **real tables** (use them for size charts: search engines and AI assistants can read tables, not pictures of tables).

### How products appear as cards
- **One card per print.** A product with a *Print* or *Colorway* option shows one card for each value, in the order listed on the product. Reorder the values to reorder the cards.
- A product without that option shows one card, named by its **Print name** field.
- A card's price, **Sale** badge and **Sold out** badge come from that print's sizes. It says "Sold out" only when every size of that print is gone.
- **Which collection a print appears in:** normally the product's own collection (set on the product as usual). Only a product whose prints belong to *different* collections (today: **Margit**) sets it per print, in the product's *Prints* data (`collection`). ⚠️ Shared with the live site. The developer's data plan removes the old per-print settings that aren't needed, which also fixes the empty **Whimsy** page.
- **Which photo a card shows:**
  1. Photos whose alt text is exactly the print name (e.g. `Dahlia Seed`). ⚠️ Leave these alt texts alone until launch; the live site uses them too.
  2. Otherwise, the photo assigned to that print's variants (safe to set).
  3. Otherwise, the product's first photos.
  The second photo fades in on hover (desktop only). Cards are cropped to 3:4, so set a **focal point** to move the crop.
- Products tagged **hidden** (such as the chainstitch monogram fee) and **draft** products never appear.

### Print swatches
The small fabric squares on product pages use built-in images for the 14 current prints (Dahlia Seed, Orange Asterisk, Pastel Asterisk, Matyó Floral, Cherry Coupe, Wildflowers, Magnolia, Moon Illusion, Good Vibrations, Candied Plaid, Midnight Plumes, Twilight Plumes, Olive, Terracotta). Names must match exactly, including the accent in "Matyó". A new print shows a close-up crop of its photo until a swatch is added; ask the developer for now (making swatches editable is decision D-14).

### Collection cards (the Collections page)
Image: the collection's **Card image** field (`kambric.card_image`) if set, otherwise the collection image, otherwise the first product photo. **Set Card image on Folklore, Psychedelics and Whimsy** (safe: the live site doesn't read it). Title, description (first two lines) and "N pieces" come from the collection.

### 404 page
*Customize* → choose the **404 page** template from the page picker at the top. You can edit the small "404" label, the heading ("This page seems to have wandered off.") and the two links. Leave a link's label empty to hide it.

### Breadcrumbs and robots.txt
Nothing to set up. Breadcrumbs ("Home › Folklore › Arielle Slip Dress") use your product, collection and page titles, and tell Google where each page sits. `robots.txt` keeps Shopify's defaults and explicitly welcomes the AI assistants the current site allows (ChatGPT, Claude, Perplexity, Google's AI).

---

## 3c. Product page (Phase 2)

*Customize → Products → Default product.* One template serves every product: products with several prints (a **Print** or **Colorway** option), single-print products, monogrammable and sold-out products.

### What you can change in the editor
- **Section settings:** *Show breadcrumbs* (the trail is still given to search engines when hidden), *Desktop gallery layout* (one image with thumbnails, like today, or all images stacked; phones always swipe), *Show the print name on the image*.
- **Blocks in the right-hand column** can be reordered, hidden or removed: Archive print label, Title, Price, Print swatches, Description, Print story, Divider, Sizes (optional *Size guide link*), Chainstitch monogram, Add to cart, Product details, Category and collection, plus extra **Text** blocks and app blocks. Don't remove **Sizes** or **Add to cart** unless you mean to stop sales from this page.

### Where each piece of text comes from
| On the page | Where to edit it |
| --- | --- |
| Title, description, price, sale price (compare-at), sizes, stock | The product and its variants in the admin ⚠️ shared with the live site |
| "Wildflowers Archive Print" label | The active print's name. To show a fixed name instead (Arielle: **"Parlor Rose"** → "Parlor Rose Archive Print"), fill the product's new **Archive label** field (`kambric.archive_label`, single-line text). Safe: the live site doesn't read it. The developer's data plan creates the field; set it on Arielle after that. |
| "The Wildflowers Print" story | Products with prints: that print's `story` in the product's *Prints* data (`kambric.prints`). Single-print products (and prints without a story): **Print story** (`kambric.print_story`). ⚠️ Both are shared with the live site. |
| Category · Collection | Product type; the print's `collection` in *Prints* data, otherwise the product's first collection. |

### Photos per print
The gallery shows every photo of the selected print:
1. photos whose **alt text is exactly the print name** (e.g. `Magnolia`); otherwise
2. photos **assigned to that print's variants** plus photos whose **file name contains the print name** (e.g. `ArielleDress_Olive_2.jpg`); otherwise
3. all the product's photos.
Single-print products always show all their photos. ⚠️ Don't change product image alt text before launch; the live site groups photos with it. The first photo loads first, so put the best one first.

### Links to a print
Each print swatch links to `/products/<handle>?variant=<id>` (Shopify's own variant link), and the page opens on that print. Choosing a size updates the link, so a copied link keeps the size too. Old links such as `?print=Magnolia` still work. Search engines always see the plain `/products/<handle>` address.

### Chainstitch monogram
- Shown when the product has the tag **`monogrammable`**, the selected print is in stock, and the **Chainstitch Monogram** product (`chainstitch-monogram`, $25) is active and in stock. To offer it on a product, add the tag. To pause it everywhere, set the fee product out of stock (⚠️ shared with the live site).
- Customers tick the box, type up to 10 characters and pick one of 10 thread colours (Black, Ivory, Gray, Brown, Red, Light pink, Sage green, Navy blue, Gold, Lavender). The garment and a separate $25 line are added together; both show the text and colour, and the fee line says which product it's for. Colours and the 10-character limit are set by the developer.
- It needs JavaScript. Without it, the option is shown greyed out, and the plain garment can still be added.

### Sold-out sizes
Sold-out sizes are crossed out. Choosing one (or the button when every size of a print is sold out) opens the "Notify me" form (below).

### "Notify me when it's back"
When a shopper picks a sold-out size, a small form asks for their email and sends it to you through Shopify's **contact form**.
- **Where it arrives:** your contact-form email. Change the recipients under **Settings → Notifications → Staff notifications → Contact form** (it usually defaults to the store email in *Settings → General*). Submissions aren't listed in the admin; they're only emailed.
- **What it says:** "Please notify me when Margit One-Piece is back in stock", then the print, size, variant ID and product link.
- **Nothing emails the customer automatically when stock returns (yet).** For now, you reply by hand. An app can take this over later without changing the page (decision D-12).
- Shopify occasionally shows shoppers a captcha on contact forms; the form handles that by itself.

### Product details (fabric, neckline, …)
A short list of facts under the description, written as plain text that search engines and AI assistants can quote. It fills itself from the product's **Category metafields**:
1. Open the product and set its **Product category** (e.g. *Apparel & Accessories › Clothing › Dresses*).
2. In the **Category metafields** that appear, pick values for Fabric, Color/Pattern, Neckline, Sleeve length, Dress style, Skirt/dress length, Hemline or Outerwear features, whichever apply.
3. Save. Only filled fields are shown; today no products have them, so the list is hidden everywhere.
These are Shopify's standard fields, so they also improve Shopify search, filters and the Shop app. ⚠️ Product data is shared with the live site, but the live site doesn't use these fields, so filling them in is safe.

---

## 3d. Shop, category, collection and sale pages (Phase 3)

**One-time setup:** create the category collections and assign their templates (table below), paste the copy from `docs/store-data/collection-copy.csv` (instructions in `collection-copy.md`), and create the **Shop categories** menu (§3a, menu `shop-categories`) for the category strip. Until that menu exists, the strip is simply hidden.

### Product listings

**Which template each page uses**
| Page | Address | Template to assign |
| --- | --- | --- |
| Shop all | `/collections/all` | Nothing to assign. Shopify always uses the default collection template here, and the sections switch on for this page by themselves (their **Show on** setting). |
| Category (Dresses, Kaftans, Coats, Swimwear, Accessories) | `/collections/dresses` … | Open the collection in the admin → *Theme template* → **category**. |
| Sale | `/collections/sale` | Open the collection → *Theme template* → **sale**. |
| Collection (Folklore, Psychedelics, Whimsy) | `/collections/folklore` … | **Default collection** (nothing to change). |

⚠️ Creating the category and sale collections is shared with the live site; see §3a-A1 (Online Store channel only).

**One section, two ways of listing: _Product listing_**

Every listing page uses the **Product listing** section. What it shows depends on whether it has blocks:

- **With Collection blocks (shop and category pages): cards grouped by collection.** Each **Collection** block is one group: pick the collection, and the group shows the page's prints that belong to it. On a category page that means only that category's pieces (e.g. the Dresses page groups dresses by Psychedelics, Folklore, Whimsy). The group's heading and text are the collection's **title** and **description**. You can override the heading in the block, and turn the description or the "N pieces" count off per block. Groups with no cards are hidden automatically.
  - **Order:** drag the blocks in the sidebar. The block order is the order on the page.
  - **New collection?** Add a Collection block for it on the default *collection* template (the shop page) and on the *category* template, then drag it into place. Until you do, its prints still appear under **other pieces** (below), so nothing goes missing.
  - **Show other pieces** (on by default): prints whose collection has no block are listed after the groups. Today these are a few prints with an outdated collection setting; the developer's data plan fixes them. They have no heading unless you fill in *Heading for other pieces*. Turn this off only if you really want those prints hidden.
  - Where the shop and category templates already exist, the blocks are set up (Psychedelics, Folklore, Whimsy). If you add a new Product listing section, it starts with no blocks.
- **With no blocks (collection and sale pages): a single grid** of the page's prints.
  - *Only prints from this collection* (on by default): a product with several prints shows only the prints that belong to this collection. It's turned off on the sale template, where prints of any collection qualify.
  - *Show → Prints on sale* (sale template): keeps only prints with a compare-at price above their price. A product can have some prints on sale and others at full price.
  - *Label above the grid* ("The Pieces") on collection pages; empty on sale. *Card style* and *Width* also apply only here (grouped listings always use the archive card style at full width).

**Both ways**
- Every print is its own card (see §3b).
- **Show these first**: pick products to lead the list, e.g. Arielle on the Dresses page or the Folklore page. The current site always put Arielle first on Dresses and Folklore; this setting replaces that rule. It's empty by default. In a grouped listing a pinned product leads every group it appears in.
- Otherwise cards follow the collection's **sort order** (set it on each collection in the admin). `/collections/all` has no sort setting in the admin; Shopify lists it alphabetically.

**Pages of results**
- *Products per page* (default 24) counts **products, not cards**. A product with six prints makes six cards, so pages can hold different numbers of cards. Page links appear at the bottom only when there's more than one page.
- In a grouped listing, groups are formed per page, so a group can continue on the next page.

**Empty pages**
- Category: "Nothing in this category yet." Collection: "No pieces yet." plus a line of text. Sale: "No pieces are on sale right now." with a *Shop All Pieces* link. Each has editable heading, text and link settings under *When there's nothing to show*.

**Other settings**
- *Only this product type* (under *Testing*): leave empty. It's for previewing a category on `/collections/all`, or for a category collection whose conditions let other products in.
- *Describe the list for search engines*: leave on. It lists the cards on the page for Google and AI assistants.

**Where did it move?** *Products grouped by collection* and *Product grid* were merged into **Product listing**. The old *Group order* list is now the order of the Collection blocks. Collections you haven't added as a block no longer get their own automatic group (they used to follow alphabetically); their prints appear under *other pieces* until you add a block. *Show piece count per group* is now *Show piece count* on each block.

### Collection header (collection detail pages)

Each collection's page (`/collections/folklore` etc.) opens with:

- **Header image**, in order: the collection's **Header image** field
  (`kambric.header_image`), then its **Card image** field
  (`kambric.card_image`), then its Shopify collection image, then no image at
  all (a plain dark header with just text — still fully usable).
- **Season eyebrow**, e.g. "Fall 2024" — from that collection's **Season**
  and **Year** fields. Shown only when at least one is set.
- **Title and description** — the collection's own title/description.
- **Piece count** ("N pieces") — this is new: it counts print cards the same
  way the product grid does, so it always matches what's below it.

All four (image, season, description, count) can be turned off per-section
in the theme editor if a particular collection page shouldn't show one.

### Shop / category / Sale heading

The "All Pieces" / "Dresses" / etc. heading block above the product grid:

- **Category pages** (Dresses, Kaftans, Coats, Swimwear, Accessories): leave
  the section's Title and Intro fields blank. They pull the collection's own
  title and **description** automatically — so a category's intro paragraph
  is edited the same way as any collection's description, in the Shopify
  admin, not in the theme editor.
- **Shop (/collections/all)**: defaults to "All" / *"Pieces"* with no intro,
  matching the current site. Override the Title/Second line fields if that
  ever needs to change.
- **Sale**: do **not** leave this one on the automatic fallback — a page
  titled literally "Sale" (the collection's own title) reads thin. Set this
  instance's Title / Second line / Intro directly. Suggested starting copy,
  carried over from the current site (confirm the "20% off" figure still
  matches your actual promotion before publishing — the section itself never
  hard-codes a discount number):
  - Title: **End of Summer**
  - Second line (italic): **Sale**
  - Intro: **20% off a selection of archive pieces through the end of
    August. When a print is gone, it doesn't always return.**

### Collections index (`/collections`)

- Eyebrow/heading/intro at the top are editable (defaults: "Curated
  Chapters" / "Collections" / the current intro paragraph).
- **Which collections appear:** by default, every collection with a
  **Season** set — today that's Folklore, Psychedelics and Whimsy. The
  category collections (Dresses, …) and Sale never appear here, automatically
  (they don't carry a Season). To show a specific set/order instead, use the
  section's **Collections to show** list — when it's non-empty it takes over
  completely.
- **Empty state** ("Coming soon." / "The archive is being curated…") only
  shows if that resolves to zero collections.
- Each card's image is still the collection's **Card image** field
  (`kambric.card_image`) → collection image → title-only placeholder, exactly
  as already documented in CONTENT_GUIDE §3b "Collection cards".

### Closing strips (text-cta)

A small reusable strip used in two places, each its own instance with its
own message/link — editing one doesn't affect the other:

- **Bottom of every collection detail page:** "Explore more of the
  archive." → All Collections (`/collections`).
- **Bottom of Shop/category pages:** the limited-quantity message → "The
  Archive →" (`/pages/about`).

### Sale page copy
Set the Sale heading's title and intro in the theme editor (Customize → a sale collection). The theme never hard-codes a discount. The old site's text ("End of Summer *Sale*", "20% off … through the end of August") is out of date; rewrite it for the current promotion.

---

## 4. Photos: getting the best quality and speed

The new theme automatically resizes every photo for each screen size and serves modern formats (WebP/AVIF) to browsers that support them. **You don't need to resize or compress photos yourself.**

- **Upload the best original you have**: JPEG or PNG, ideally **2400 px or more on the long edge** for full-width photos (heroes, banners) and **2000 px** for product photos. Shopify's limit is 20 MB per image.
- **Alt text (new, and important):** in the Shopify admin you can now describe each image (in *Files*, on product media, or next to image pickers). Write what's in the photo in plain words, e.g. *"Model in the Arielle slip dress in olive, standing in a field of teasels."* This helps visually-impaired visitors, Google Images and AI search. Leave it empty only for purely decorative images.
- **Focal point (new):** in *Content → Files* (or product media) you can set the focal point, so crops on phones keep the important part of the photo in frame.
- **Don't put text inside images.** Search engines and screen readers can't read it. Use the section's text fields instead.
- **Product image alt text** also groups photos by print on merged products (the alt text must equal the print name, e.g. `Dahlia Seed`). This will be reviewed in Phase 2 (see the migration plan). Until then, don't change product image alt text.

---

## 5. Being found on Google and AI assistants (SEO and AEO)

The theme adds the technical pieces automatically: page titles, descriptions, sharing previews, structured data for products, articles and the brand, fast loading, and accessible markup. Your part:

1. **Search engine listing:** every product, collection, page and blog post has a *Search engine listing* box at the bottom of its admin page. Write a unique title (≤ 60 characters) and description (≤ 155 characters) that say what the page is and who it's for.
2. **Answer questions in plain text.** AI assistants and Google quote pages that answer clearly. Put facts (sizes, materials, care, shipping times, return window, event date/time/place) in real text near the top, not in images or PDFs.
3. **Use headings in order** in the rich-text editor (Heading 2 for main sections, Heading 3 inside them). Don't pick a heading just for its size.
4. **Keep web addresses stable.** If you rename a product or page handle, Shopify offers "Create a URL redirect". Keep that box ticked.
5. **Alt text on every meaningful image** (see above).

---

## 6. What's different (heads-up)

- **Web addresses change** for some pages, e.g. `/journal/...` becomes `/blogs/journal/...`, `/about` becomes `/pages/about`, and `/shop/dresses` becomes a collection address. Old links are **redirected automatically**, so bookmarks and Google results keep working. The redirect list is in the migration plan.
- **Journal posts** use Shopify's visual editor (bold, italic, links, images, headings) instead of Markdown. Existing posts are converted for you.
- **Newsletter subscribers** are stored as Shopify customers, so you'll see and export them under *Customers*. Existing subscribers are imported at launch, keeping their opt-in status.
- **Info pages** (shipping, returns, size guide, etc.) become editable Shopify pages. Before, they needed a developer.
- **No more separate `/admin` password.** Staff access is managed in Shopify (*Settings → Users*).

---

## 7. Open questions that affect editors

These are tracked as decisions in `docs/MIGRATION_PLAN.md`. They're listed here so you know they're coming:

- Where the **newsletter/pop-up** emails are sent from (Shopify Email vs. another provider) and how the **WELCOME15** code is issued.
- Whether **print swatches** (the small fabric squares) become editable in the admin.

---

## Change log

| Date | Phase | What changed for editors |
| --- | --- | --- |
| 2026-09-28 | 3: Listings (update) | New **§2b How the shop is organized**: products, prints, collections, categories and sale, where each appears, and step-by-step recipes to add, edit, reorder, retire and hide. Listings now use one **Product listing** section with a **Collection block** per group (drag to reorder); the *Group order* setting is gone (§3d). Per-print collections are only needed for products spanning collections (Margit). |
| 2026-09-28 | 3: Listings | Shop, category, collection and sale pages; template assignment; group order and "Show these first"; collection header image, season, piece count; `/collections` index; category strip menu `shop-categories`; collection copy sheet (§3d). |
| 2026-09-28 | 2: Product page | Product page blocks and settings, archive label, print photos and links, chainstitch monogram, notify-me form, product details (§3c). |
| 2026-09-28 | 1: Global components | Blocks (heading, text, button, eyebrow, image, group), product and collection cards, print swatches, 404 page, breadcrumbs, robots.txt (§3b). |
| 2026-09-28 | 0: Foundation (update) | Step-by-step announcement bar how-to; one-time menu setup (§3a). Announcement bar slightly darker for readability. |
| 2026-09-28 | 0: Foundation | Announcement bar, header menu (`main-menu`), footer (brand text, menu columns `footer` and `footer-info`, newsletter heading, location), theme settings (logo, favicon, sharing image, colours, social links). Guide created. |
