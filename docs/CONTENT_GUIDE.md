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
| Set **collection cover and header images** | **Products → Collections → (collection) → Metafields** | Phase 3 |
| Edit **info pages** (contact, shipping, returns, size guide, wholesale) | **Online Store → Pages** (these were locked in code before; now you can edit them) | Phase 4 |
| Edit **privacy policy and terms** | **Settings → Policies** | Phase 4 |
| Change the **newsletter pop-up** image | **Customize** → Pop-up section | Phase 5 |
| Download **newsletter subscribers** | **Customers** → filter *Email subscribed* (or the tag `newsletter`) → Export | ✅ Footer form now; pop-up Phase 5 |
| Manage **back-in-stock requests** | To be decided (see "Open questions") | Phase 2/5 |
| Edit **products, prices, inventory, print names/stories** | Same as today: **Products** | No change |

---

## 2. How editing works in Shopify

- **Theme editor** ("Customize"): **Online Store → Themes → (Kambric Goods theme) → Customize**. You see the page as visitors will and can click any section to edit it. Changes are saved as a draft until you press **Save**. On the live theme, Save publishes immediately.
- **Sections and blocks:** each page is a stack of *sections* (e.g. Header, Footer). Some sections contain *blocks* (e.g. each footer column is a block) that can be added, removed, reordered or hidden with the eye icon.
- **Menus:** **Content → Menus**. Drag links to reorder. Drag a link *under and to the right of* another to nest it (that makes a dropdown).
- **Files:** **Content → Files** holds uploaded images. Images you pick in the theme editor are stored here.
- **Before launch:** you'll work on the Shopify-hosted practice site (`kambric-goods-2.myshopify.com`). The developer will tell you when the new theme is ready there to receive content. Until then the developer may replace it, so hold off on entering real content. Please leave publishing and theme switching to the developer.

---

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

Some links point at things that don't exist in Shopify yet (category collections, the About/Events pages, the Journal). Do **Part A** now and **Part B** when those pages are built (Phase 4).

> ⚠️ **Protect the live site.** Today's kambricgoods.com (the Replit site) shows every Shopify collection it can see. When you create a new collection in step A1, restrict it to the **Online Store** sales channel as described, or it will appear on the live site right away. Menus and pages are safe: the live site doesn't read them.

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
5. ⚠️ **Publishing** (right-hand card) → **Manage** → leave **only "Online Store"** ticked and untick every other channel (e.g. *Headless* or the Replit app's channel). **Save** the dialog.
6. Scroll to **Search engine listing** → **Edit**. Check the URL ends in `/collections/dresses` (lowercase, matching the title). Fix the handle there if needed.
7. Click **Save**.
8. Check that https://kambricgoods.com/collections does **not** list the new collection. If it does, re-check step 5 and tell the developer.

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
- **Which collection a print appears in:** set per print in the product's *Prints* data (`collection`). Otherwise it's the product's first collection. ⚠️ Shared with the live site: four prints still point to the old **botanicals** collection, so **Whimsy currently shows no products**. The developer's data plan fixes this.
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

- How **back-in-stock** requests will be collected and sent (a Shopify app vs. a simpler built-in option).
- Where the **newsletter/pop-up** emails are sent from (Shopify Email vs. another provider) and how the **WELCOME15** code is issued.
- Whether **print swatches** (the small fabric squares) become editable in the admin.

---

## Change log

| Date | Phase | What changed for editors |
| --- | --- | --- |
| 2026-09-28 | 1: Global components | Blocks (heading, text, button, eyebrow, image, group), product and collection cards, print swatches, 404 page, breadcrumbs, robots.txt (§3b). |
| 2026-09-28 | 0: Foundation (update) | Step-by-step announcement bar how-to; one-time menu setup (§3a). Announcement bar slightly darker for readability. |
| 2026-09-28 | 0: Foundation | Announcement bar, header menu (`main-menu`), footer (brand text, menu columns `footer` and `footer-info`, newsletter heading, location), theme settings (logo, favicon, sharing image, colours, social links). Guide created. |
