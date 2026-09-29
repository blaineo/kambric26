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
| Edit the **homepage hero, story, quote image** | **Customize** → Home page sections (§3e) | ✅ Phase 4 |
| Edit the **About page** text, photos, value cards | **Customize** → About page sections (§3f) | ✅ Phase 4 |
| Add, edit and reorder **events** | **Content → Metaobjects → Event** (§3g) | ✅ Phase 4 |
| Write **journal posts** (Markdown) | **Content → Blog posts → Journal** (visual editor, no Markdown; §3h) | ✅ Phase 4 |
| Set **collection cover and header images** | **Products → Collections → (collection) → Metafields**: *Card image* and *Header image* | ✅ Phase 3 |
| Edit **info pages** (contact, shipping, returns, size guide, wholesale) | **Online Store → Pages** (these were locked in code before; now you can edit them; §3h) | ✅ Phase 4 |
| Edit **privacy policy and terms** | **Settings → Policies** | Phase 4 |
| Change the **newsletter pop-up** image and copy | **Customize** → Footer → **Newsletter pop-up** (§3i) | ✅ Phase 5 |
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
| Logo and brand | Logo, logo height (desktop/mobile), favicon, default social sharing image | Leave the logo empty to use the built-in bronze wordmark. The default sharing image is the **home hero photo**; it's used for pages without a hero of their own (see *Social sharing images* below). |
| Google Search Console | **Theme settings → Logo and brand → Google Search Console verification code** | Holds the code from Google's *HTML tag* verification method (just the `content` value); it's output on the home page only. Already set for kambricgoods.com. |
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
- **Where it arrives:** the store's contact email (*Settings → General → Store contact email*, currently kambricgoods@gmail.com). There's no separate contact-form recipient setting. Submissions aren't listed in the admin; they're only emailed.
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

⚠️ Publishing the category and sale collections is shared with the live site (it reads the same Online Store channel). The developer creates and publishes them in one step on launch day (script ready). See §3a-A1.

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
- **Show these first**: pick products to lead the list, e.g. Arielle on the Dresses page or the Folklore page. The current site always put Arielle first on Dresses and Folklore; this setting replaces that rule. It's set to **Arielle Slip Dress** on the collection and category templates (so Arielle leads Folklore and Dresses, as today); clear it to drop the rule. In a grouped listing a pinned product leads every group it appears in. Unpinned products on Shop and category pages are listed oldest first, like the current site.
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
- **Eyebrow** "Collections" (editable in the section's **Eyebrow** setting),
  as on the current site. A **Season** eyebrow ("Fall 2024", from the
  collection's Season and Year fields) and a visible **breadcrumb** trail are
  available but switched off (owner decision 2026-09-29); tick **Show
  season/year** or **Show breadcrumbs** to bring them back.
- **Title and description** — the collection's own title/description.
- **Piece count** ("N pieces") — this is new: it counts print cards the same
  way the product grid does, so it always matches what's below it.

Image, description and count can be turned off per-section
in the theme editor if a particular collection page shouldn't show one.

### Shop / category / Sale heading

The "All Pieces" / "Dresses" / etc. heading block above the product grid:

- **Category pages** (Dresses, Kaftans, Coats, Swimwear, Accessories): leave
  the section's Title and Intro fields blank. They pull the collection's own
  title and **description** automatically — so a category's intro paragraph
  is edited the same way as any collection's description, in the Shopify
  admin, not in the theme editor.
  - **Where it shows (2026-09-29):** only the description's **first sentence**
    appears under the title (section setting *Intro length*: Full / First
    sentence / Hidden). The **full description** appears below the products in
    the **About this collection** section, under the heading "About our
    dresses" (editable; blank = "About our [collection name]"). It's still
    visible text with its own heading, so search engines and AI assistants read
    it as before. Write the description so its first sentence works on its own.
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

## 3e. Home page (Phase 4)

Edit it in **Online Store → Themes → Customize** (the home page opens first). Top to bottom, the sections are:

| # | Section | What you can change |
| --- | --- | --- |
| 1 | **Home hero** | Photo, phone photo, alt text, crop position, shading, text position, small label, headline + italic second line, headline size, subtitle, two buttons (label + link), "Scroll" cue on/off |
| 2 | **Scrolling strip** (filled) | The items (one per line), style, direction, speed |
| 3 | **Product rail**: "New Arrivals / Just Arrived" (dark band) | Label, heading, link, which pieces (see below) |
| 4 | **Home story** | Label, heading + italic line, text, button, up to 3 **Photo** blocks (collage) |
| 5 | **Product rail**: "Featured Pieces / From the Collections" | Same as 3 |
| 6 | **Lookbook** | Label, heading + italic word, intro line, **Look** blocks |
| 7 | **Quote** | Quote, attribution, ornaments, optional background photo (strength and cream wash) |
| 8 | **Scrolling strip** (plain, reversed) | Same as 2 |

Sections can be hidden, reordered or added again from **Add section** (all six are available anywhere).

### Home hero
- **Photo**: the biggest image on the page and the first one to load. Use a wide photo at least 2400 px wide. **Phone photo** (optional) replaces it on screens under 768 px: use a portrait crop.
- **Crop position** (e.g. `65% 20%`) decides what stays in view when the photo is cropped. A **focal point** set on the image in *Content → Files* takes priority.
- **Headline** is the page's main heading for Google (the only H1 on the page). Leave both headline lines empty only if the photo says it all; the shop name is then used for screen readers.
- **Headline size**: *Medium* suits a product name like "Arielle Slip Dress" (the current site shrinks the headline automatically when it contains "Arielle"; this setting replaces that rule). *Large* suits a short phrase.
- **Alt text**: leave empty (decorative photo, like today) or describe it.
- Without a photo, the dark band shows on its own and the text still reads well.
- The text fades in when the page opens and the photo drifts slightly as you scroll. Both are switched off for visitors who ask their device for reduced motion.

### Scrolling strips
One item per line. They loop continuously, pause on mouse-over, and stand still (wrapped onto lines) for visitors who prefer reduced motion. The two strips on the home page share the same six items; edit both if you change them.

### Product rails (New Arrivals and Featured Pieces)
Each card is one **print**, as everywhere else (§3b). A rail is filled in two steps:

1. **Show first** blocks: pick a **product**, and optionally a **print** (exact name, e.g. `Matyó Floral`). With no print, every print of the product is shown. These slots are always kept.
2. **Fill with**: flagged prints fill the slots left up to **Maximum cards**: *Prints flagged featured*, *Prints flagged new arrival*, *Any print*, or *Nothing*. Flags are set per print in the product's *Prints* data (`featured` / `newArrival`), or with the tags `featured` / `new-arrival` on single-print products. ⚠️ Shared with the live site: leave the flags alone until launch.
   - **From collection** (optional) limits the pool; empty = every product, alphabetical.
   - **Exclude product types** (comma-separated, e.g. `Swimwear`) leaves those types out of the flagged prints. It never removes a Show first block.
   - **Show first pieces go**: before or after the flagged pieces.

A print never appears twice. If the rail ends up empty it's hidden on the site.

**These settings replace rules that were hard-coded on the current site:**

| Rail | Old hard-coded rule | Now set up as |
| --- | --- | --- |
| New Arrivals | Up to 1 flagged new arrival that isn't Swimwear and isn't Arielle, then every Arielle print, max 3 | Fill with *new arrival*, Exclude product types `Swimwear`, one Show first block **Arielle Slip Dress** (no print), *after*, Maximum 3, 3 columns |
| Featured Pieces | First 4 featured prints, but Esther Kaftan / Good Vibrations is swapped for Margit One-Piece / Wildflowers and Margit / Dahlia Seed for Margit / Matyó Floral | Four Show first blocks, in order: **Kati Slip Dress**, **Margit One-Piece / Matyó Floral**, **Zadie Linen Dress / Wildflowers**, **Margit One-Piece / Wildflowers**; Fill with *featured*, Maximum 4, 4 columns. Delete a block and the next featured print takes its place. |

### Home story
Text on the left (label, heading with its italic line, two short paragraphs, button to the story page), collage on the right. **Photo** blocks: the first is the tall photo, the next two stack beside it (max 3). Each has alt text and a crop position. On phones the collage sits under the text. Without any photos the collage is left out and the text spans the band.

### Lookbook
Each **Look** block is one photo: image, alt text, crop position, number label ("No. 01"), caption, link and a link description for screen readers ("Shop the Vera Car Coat"). The whole photo is the link. On desktop, look 1 is the large photo, looks 2 and 3 stack beside it, and looks 4 onward sit three to a row. On phones they stack. Drag blocks to reorder. A look without a photo only shows in the editor (as a placeholder); until at least one look has a photo, the whole Lookbook is hidden on the site.

### Quote
The quote, attribution and ✦ ornaments are editable now (they were fixed in code). The background photo is optional: without it the band is plain.

### Photos: where the current ones go
The home photos can't be pre-filled by the theme; they're uploaded once (owner task list, "Home page photos"), then picked in each setting:

| Setting | File (from the export) |
| --- | --- |
| Home hero → Photo | `home-hero-background.png` (`assets/uploads/9de4a6ef-…fc41.png`) |
| Quote → Background photo | `home-founder-quote-background.jpg` (`assets/uploads/cd6532ac-…56f1.jpg`) |
| Home story → Photo 1 | `IMG_8800_1780590151823.png` |
| Home story → Photo 2 | `kati_hands_painting.png` |
| Home story → Photo 3 | `IMG_6961_1780589947013.png` |
| Lookbook → Look 1 … 6 | `DSCF1744…`, `DSCF1600…`, `DSCF1931…`, `DSCF1688…`, `DSCF1680…`, `DSCF2023…` (`_Original_*.jpg`) |

Alt texts and crop positions from the current site are already filled in on each block.

**Where did it move?** *Homepage Hero*, *Homepage Story* and *Homepage Quote background* in the old `/admin` are now the **Home hero**, **Home story** and **Quote** sections. The strip items, rail headings and links, lookbook and quote text used to be fixed in code and are now editable.

## 3f. About page (Phase 4)

*Customize → choose the page **About** (template `page.about`) from the page picker at the top.*

The page is six sections, each editable independently — nothing is hard-coded copy anymore:

| Section | What it is | Notes |
| --- | --- | --- |
| **About hero** | Dark band, eyebrow, three-line headline (the middle line is the gold accent), subtitle, optional background photo | This is the page's only heading (H1). With no photo the band shows as a plain dark text band — still fully readable. |
| **About: On the Name** | Centered eyebrow + rich text | Use the toolbar's *italic* button for emphasis — you don't need to type `*asterisks*` like the old site did. |
| **About: story block** (×2, "Kati" and "Daisy") | Eyebrow, one-line italic heading, biography, photo, optional caption, optional button | Add this section twice — once per person. **Image side (desktop)** controls which side the photo sits on; on phones the photo always shows above the text either way. |
| **About: values** | "What We Stand For" eyebrow + value cards | Value cards are **blocks**: click **Add block → Value card** to add one, or use the block menu to remove/reorder. Unlike the old CMS, you can have any number of cards, not just three. |
| **CTA banner** | Closing full-bleed photo band with a heading and one button | Use Shift+Enter (or the line-break option in the heading field) for a two-line heading like the default "It began with / the archive." |

### Adding a value card
1. Open the **About: values** section.
2. **Add block → Value card.**
3. Fill in **Number** (e.g. "04"), **Title**, **Body**.
4. Drag to reorder; use the block's menu to remove one.

### Images
None of the photos (hero, Kati, Daisy, CTA banner) can be pre-loaded — upload them once to **Content → Files** and set each on its section. The exact files and where they go are in the owner task list (`owner-tasks-about-events.md` §4, to be merged into `docs/OWNER_TASKS.md`). Until then every image-backed section renders gracefully as a text-only band.

---

## 3g. Events page (Phase 4)

*Customize → choose the page **Events** (template `page.events`) from the page picker at the top.*

Two sections:

| Section | What it is |
| --- | --- |
| **Events hero** | Dark band, eyebrow, two-line heading, italic subtitle, optional background photo (this page's only H1) |
| **Events list** | Upcoming list, past list, empty state, and the "Hosting · Press · Collaborations" contact block — all in one section |

### Events themselves aren't page content — they're a separate list you manage once, for every page
Events live in **Content → Metaobjects → Event**, not in the page editor. Add, edit, reorder-by-date or remove events there; the Events page always reflects the current list automatically. The metaobject definition and how to add entries are in `owner-tasks-about-events.md` §1–2 (owner sets this up once; after that it's an ordinary content type like Pages or Blog posts).

**Fields on each event:**
- **Title** (required)
- **Start date** — a real date. This is what decides upcoming vs. past (see below). Leave blank for a "TBA" event.
- **Date label override** — type something here (e.g. "TBA", "Summer 2026") to show that instead of the formatted Start date. Most events don't need this.
- **Time** — e.g. "6–8pm". Only shown on upcoming events.
- **Venue**, **City**
- **Description** — rich text
- **Image** — optional. Not shown visually on the page (the design doesn't show event photos), but it's included in the event's structured data for search engines if you add one.
- **URL** — optional link (RSVP page, Instagram post, etc.); makes the event's title clickable.
- **Status override** — leave blank almost always. Only set this to force an event into the other list — e.g. an undated ("TBA") event that should actually show as past, or a dated event you want to keep under Upcoming past its date.

### Upcoming vs. past, and sorting
- An event is **past** once its Start date is before today. **Status override always wins** when set.
- An event with **no Start date and no override** counts as **upcoming** (that's the "TBA" case — you don't know the date yet, but you know it's coming).
- **Upcoming** events are listed soonest-first; undated ("TBA") ones sort to the end of that list.
- **Past** events are listed most-recent-first, and only the most recent few show (**Events list** section → **Past events to show**, default 4 — the old site also kept 4). Older ones simply stop appearing; nothing needs to be deleted.
- No events yet? The page shows an empty-state message instead of a blank space — its heading/body text are both editable in the **Events list** section settings.

### Checking the layout before any events exist
The **Events list** section has a setting, **Show sample events in the editor**, off by default. Turn it on to preview both the upcoming and past card layouts with sample content **while you're in Customize** — shoppers on the live site never see this either way; it only appears inside the theme editor. While it's on, the editor shows the samples instead of your real events, so turn it back off once you've added real entries you want to check.

## 3h. Journal and info pages (Phase 4)

### Writing a journal post

**Content → Blog posts → Journal** (create the post under the `journal`
blog — see OWNER_TASKS for one-time blog setup).

| Field | What it does | Notes |
| --- | --- | --- |
| Title | The post's H1 and its browser-tab title | Title appears as "*Title* \| Kambric Goods Journal" |
| Tags | The category shown on the card and the post itself (e.g. "Craft", "The Archive") | **Use exactly one tag per post.** Shopify sorts tags alphabetically, and the theme shows the *first* one as the category — a second tag could jump ahead of the one you meant. |
| Excerpt | The teaser text on the Journal index card, and the fallback meta description | Keep it to 1–2 sentences |
| Featured image | The post's cover photo | Shows on the index card and at the top of the post; also used as the social-share image |
| Content | The body of the post | Use the rich text editor's headings/links/images as normal — no Markdown |
| Published date | Controls sort order and the date shown | |

**Products in this story:** open the post's page in the theme editor
(**Customize**) and, under the article section, add products to **Products
in this story**. This shows a small "Products in this story" grid under the
post body. It's optional — leave it empty and nothing shows, there's no
automatic guess at which products a post is "about".

**Search engine listing:** fill in the title/description box at the bottom
of the post's admin page so the post has a distinct summary for search
results (the theme composes the browser title for you; this affects the
description search engines show and the two are independent).

### Editing info pages (Contact, Wholesale, Shipping, Returns, Size Guide)

These live under **Online Store → Pages**. Five pages: `contact`,
`wholesale`, `shipping`, `returns`, `size-guide`. (Privacy Policy and Terms
of Service move to **Settings → Policies** instead — see OWNER_TASKS, 🔴.)

Every one of these pages uses the same building blocks:

- **Eyebrow:** open the page in **Customize** and set the small label above
  the title (e.g. "Say Hello", "For Stockists") in the section's settings.
  Each info page has **its own template** (`page.contact`, `page.wholesale`,
  …), so changing one page's eyebrow or buttons doesn't touch the others.
- **Title:** the page's own **Title** field (Online Store → Pages) — this is
  the page's H1.
- **Body:** the page's **Content** field. Write the intro paragraph, then
  any additional sections as ordinary headings (Heading 2) and paragraphs —
  e.g. a "Customer Care" or "Become a Stockist" heading followed by its
  paragraphs. A thin rule appears above each heading automatically; you
  don't need to add one.
- **Buttons ("Email Us", "Ask About Fit", "Shop Wholesale on JOOR", …):**
  in **Customize**, add a **Button** block under the page content. Set:
  - **Label**: the button text
  - **Link**: `mailto:howdy@kambricgoods.com` for an email button, or a full
    web address for an external link (e.g. the JOOR page)
  - **Style**: choose **Solid** to match the site's dark CTA buttons
  - **Open in new tab**: on, for external links like JOOR

  Add more than one button if a page needs two (Wholesale has "Shop
  Wholesale on JOOR" and "Request Our Line Sheet").

Which template each page uses (set under **Template** in the page's admin
sidebar):

| Page | Template |
| --- | --- |
| Contact | `page.contact` |
| Wholesale | `page.wholesale` |
| Shipping | `page.shipping` |
| Returns & Exchanges | `page.returns` |
| Size Guide | `page.size-guide` |
| Any new info page | `page` (the default: no eyebrow or buttons until you add them in Customize) |

### Editing the Size Guide table

The Size Guide page uses a second section, **Size table**, below the usual
page content. Open the page in **Customize** to edit it:

- **Table caption** — the heading above the table (default "Womenswear
  (inches)").
- **Size row blocks** — one block per row (XS–XL are pre-filled). Each has
  four fields: **Size**, **Bust**, **Waist**, **Hip**. Add, remove, or
  drag-reorder rows the same way you would any other block.
- **Fit note heading / body** — the "Need a Hand?" text under the table.
- **Ask About Fit button** — label + link fields in the same section
  (defaults to a `mailto:` link); leave the link blank to hide the button.

This renders as a real, accessible HTML table (not a picture of one), which
is what lets search engines and AI assistants answer "what size should I
get" questions directly from the page.

If a future page ever needs a one-off table that isn't worth a whole
section, you can also paste a table directly into a normal page/article's
Content field — `rte.liquid`'s styling covers any real `<table>`, not just
this one.

### Behind the scenes (for the record, not something you need to do)

- The Journal blog and its posts, and the info pages, all render through
  theme sections (`main-blog`, `main-article`, `main-page`, `size-table`) —
  the same JSON-template pattern as every other page type in this theme.
- Journal web addresses are `/blogs/journal/...` (Shopify requires the
  `/blogs/` prefix). The old `/journal/...` links redirect automatically —
  see the migration plan's redirect list.

> **Photos on the home, About and Events pages:** the developer uploads them to Files and sets them in the templates (a store batch), so you don't have to pick them one by one. To change one later, select the section in Customize and choose a different image.


---

## Social sharing images (links in iMessage, Instagram, Pinterest, Facebook, X)

Nothing to upload: each page shares a **1200 × 630 crop of its own hero photo**, made automatically.

| Page | Photo used |
| --- | --- |
| Home, About, Events | That page's hero photo |
| A collection | Its header image |
| A product | Its first photo (the selected print's) |
| A journal post | Its featured image |
| Anything else (Shop, info pages, cart…) | The default in **Theme settings → Logo and brand → Default social sharing image** (the home hero) |

**How the crop is chosen:** portrait and square photos keep their upper part (where faces usually are); landscape photos stay centred; the home hero follows its *Image position* setting. If a crop cuts off something important, open the photo in **Content → Files**, set a **focal point** on it, and every crop (on the page and when shared) follows it. The Shopify **Preferences → Social sharing image** field isn't needed.

Shared previews are cached by each app; after changing a photo, use Facebook's Sharing Debugger or just wait a day to see the new one.

## 3i. Cart, search and newsletter pop-up (Phase 5)

### Cart page

*Customize → Cart.* One section, **Cart**.

- **Editable:** eyebrow ("Your Selection"), heading ("Cart"), and the empty-cart heading, text, link label and link (leave the link empty to point at all products).
- **Not editable here (fixed copy, in the theme's language file):** Order Summary, Subtotal (n items), Shipping "Calculated at checkout", Estimated Total, Checkout and the notes under it, "Sold out — please remove", "Qty 1 · Personalized", "Chainstitch Monogram" and "+$25.00 personalization".
- **Chainstitch monogram in the cart:** the $25 fee is never shown as its own item. It appears under the garment it belongs to (monogram text, thread colour, fee) and is included in that garment's price. Monogrammed pieces are always quantity 1; removing one removes its fee too. The item count leaves the fee out; the subtotal includes it. The header bag icon uses the same count, so a monogrammed dress shows as 1.
- If a monogram fee somehow ends up in a cart without its garment, the cart removes it automatically. If a monogrammed garment is missing its fee, the cart shows a "Personalization fee missing" note and **checkout stays disabled** until that piece is removed (and added again from its product page), so a monogram is never free.
- A piece that sells out while in someone's cart is marked "Sold out — please remove" and checkout stays disabled until it's removed.
- Checkout itself (Shopify's hosted checkout) is shared with the live site and is **not** part of the theme.

### Search

Kambric26 uses Shopify's own search, in two places:

- **The search icon in the header** opens an overlay right under the header, the same
  as the old site: type a few letters and up to 8 matching pieces appear instantly
  (thumbnail, print, category, price). Enter, or "See all results", goes to a full
  results page.
- **`/search`** is the full results page: the same search, as a normal page with
  pagination. It's set to `noindex` (search-engine results pages don't belong in
  Google), so you'll never see it show up in search itself.

### What search looks at

Shopify indexes product **titles**, **types**, **tags**, and **variant** data, plus
page/article titles and content. It does **not** know about the print-level fields
(`kambric.print_name`, `kambric.prints`) the way the rest of the theme does — a search
match is always a whole product, never a specific print. If a shopper searches a print
name that's only recorded in metafields (not in the title), it may not match. Practical
ways to make a piece easier to find:

- **Product title**: if a print name matters for search (e.g. "Dahlia Seed"), put it in
  the product title alongside the piece name, as most already do ("Margit One-Piece in
  Dahlia Seed" (or a version of it) — it's already there for single-print products via
  the title; for merged products the print lives in the `Print`/`Colorway` option, which
  Shopify also indexes).
- **Type**: keep the product's **Type** field set (Dresses, Kaftans, Coats, Swimwear,
  Accessories) — searches for a category word match against it.
- **Tags**: tags are searched too. Adding a tag for a print name, fabric, or occasion
  ("floral", "linen", "wedding guest") gives shoppers another way in.
- **SEO title/description**: doesn't affect on-site search ranking, but does affect how
  the piece appears in Google — worth filling in regardless (see the SEO checklist
  elsewhere in this guide).

### Hidden products never appear in search

The **`hidden` tag** (used today only by the $25 monogram add-on,
`chainstitch-monogram`) is filtered out of both the overlay and the `/search` page, the
same as it's filtered from every listing. A **draft** product never appears either —
Shopify doesn't index drafts at all.

### Improving match quality (optional, no theme change needed)

Shopify's **Search & Discovery** app (free, from the Shopify App Store, likely already
installed) lets you, without any developer work:
- Add **synonyms** (e.g. "jumpsuit" → "one-piece", a colorway nickname → its official
  print name) so more of what shoppers actually type finds the right piece.
- **Pin or boost** specific products for specific search terms.
- See a **search analytics** report of what's been searched with zero results — the
  best source of new synonyms and new tags.

None of this requires a theme change; it improves results automatically. See
`docs/OWNER_TASKS.md` for the specific optional step.

### Newsletter pop-up

*Customize → Newsletter pop-up* (it lives in the footer group, so it's on
every page; open it from any page in the theme editor).

**Turning it on**
1. Tick **Enable pop-up** (untick it to switch the pop-up off). It's **on**
   (owner decision 2026-09-29), matching the current site.
2. Set **Delay before showing (seconds)** (default 6 — matches the current
   site).
3. Set **Show on** to *All pages* or *Home page only*.
4. Click **Save**.

**What it does:** after the delay, a small card appears (bottom-left on
desktop, a bottom sheet on phones) asking for an email address, unless the
visitor already closed it or signed up before (their browser remembers
this — it won't nag repeat visitors). Signing up adds them to
**Customers** with the tag `newsletter, popup` and email marketing
consent, the same as the footer sign-up form, so subscribers from both
places land in the same place: **Customers → filter *Email subscribed*
or tag `newsletter`**.

**Copy fields:** Heading, Body text, Button label, Success heading,
Success body text — all editable, defaulting to the current site's "Take
15% off" copy.

**Image:** optional (the current site shows the bandana photo,
`newsletter-signup-popup.jpg`). Leave it blank for a text-only card. If set, it's cropped to a fixed
strip above the text; set a **focal point** on the image (Content → Files)
if it needs recropping. The image is never downloaded until a visitor
actually sees the pop-up, so it never slows down the page for anyone who
doesn't.

**Discount code:** the code shown after a successful sign-up (default
`WELCOME15`).
- **Before it goes live, the code must exist as an active discount in
  Shopify** (Discounts → Create discount, code `WELCOME15` or whatever you
  put here). This is a 🔴 cutover-only task — see OWNER_TASKS — because
  discounts are shared with the live kambricgoods.com.
- **Leave this field blank to hide the code line entirely.** Use this if
  the plan is for a Shopify Email welcome automation to send the code by
  email instead of showing it on screen (decision D-11 — see below).

**"Show on" and page targeting:** *All pages* shows it everywhere except
the theme editor's own preview quirks; *Home page only* restricts it to
the homepage. There's no per-page exclusion list beyond that.

---

### Open decision this pop-up depends on (D-11)

The migration plan tracks this as **D-11**: whether the discount code is
shown on-screen (built now, described above) or sent by a **Shopify Email
welcome automation** triggered by the `newsletter`/`popup` tag, with the
on-screen code line turned off (blank the **Discount code** setting).
Both options use the exact same sign-up form and settings — switching
between them is just a Shopify Email flow (owner/marketing sets up
later) plus blanking one field, no theme change needed.

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
| 2026-09-28 | 5 (update) | Cart: a personalized piece whose $25 fee line is missing now blocks checkout until it's removed and added again; the cart icon's count now matches the cart page (garments only, the fee isn't counted separately). |
| 2026-09-28 | 5: Cart, search, pop-up | Cart page (monogram lines grouped under their garment), search overlay and results page, newsletter pop-up with optional code (§3i). |
| 2026-09-28 | 4: Home, About, Events, Journal, info pages | Home page sections and rails ("show first" blocks replace the old hard-coded picks), About sections and value cards, Events from the **Event** metaobject (upcoming/past automatic), Journal index and posts, info pages and the Size Guide table (§3e–§3h). |
| 2026-09-28 | 3: Listings (update) | New **§2b How the shop is organized**: products, prints, collections, categories and sale, where each appears, and step-by-step recipes to add, edit, reorder, retire and hide. Listings now use one **Product listing** section with a **Collection block** per group (drag to reorder); the *Group order* setting is gone (§3d). Per-print collections are only needed for products spanning collections (Margit). |
| 2026-09-28 | 3: Listings | Shop, category, collection and sale pages; template assignment; group order and "Show these first"; collection header image, season, piece count; `/collections` index; category strip menu `shop-categories`; collection copy sheet (§3d). |
| 2026-09-28 | 2: Product page | Product page blocks and settings, archive label, print photos and links, chainstitch monogram, notify-me form, product details (§3c). |
| 2026-09-28 | 1: Global components | Blocks (heading, text, button, eyebrow, image, group), product and collection cards, print swatches, 404 page, breadcrumbs, robots.txt (§3b). |
| 2026-09-28 | 0: Foundation (update) | Step-by-step announcement bar how-to; one-time menu setup (§3a). Announcement bar slightly darker for readability. |
| 2026-09-28 | 0: Foundation | Announcement bar, header menu (`main-menu`), footer (brand text, menu columns `footer` and `footer-info`, newsletter heading, location), theme settings (logo, favicon, sharing image, colours, social links). Guide created. |
