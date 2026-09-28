# Kambric Goods: content guide for the new Shopify site

**Who this is for:** anyone who updates words, photos, events, journal posts or menus on kambricgoods.com.
**What's happening:** the site is moving from the custom Replit app (with its own `/admin` page) to a Shopify theme. After the switch, **everything is edited in the Shopify admin**, the same place products are managed today. There is one login, one place to look, and no separate website admin.

This guide is updated with every build phase. The [change log](#change-log) at the bottom lists what's new each time.

> **Status:** the new theme is in development and **not live**. Keep using the current `/admin` page until launch day. Nothing you change in the Shopify theme editor affects the live site yet.

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
- **Preview before launch:** until launch, the developer shares a preview link. Please don't publish any theme; launch is scheduled and done by the developer.

---

## 3. What you can edit right now (Phase 0)

### Announcement bar
*Customize → Announcement bar* (top of every page)

| Setting | What it does |
| --- | --- |
| Show announcement | Turns the bar on or off. It's **off** today, matching the current site. |
| Message | e.g. "Summer Sale · 20% Off Select Styles". Keep it short (under ~45 characters reads well on phones). |
| Link label | The underlined words after the message, e.g. "Shop Now". Hidden on small phones and shown only if there's a link. |
| Link | Where the bar goes when clicked. Pick a collection or page, or paste a URL. |
| Style | **Static** (like today) or **Scrolling**. Scrolling pauses when hovered and stays still for visitors who've asked their device to reduce motion. |

### Header menu
*Content → Menus → Main menu* (handle `main-menu`)

- Top-level links appear across the header on desktop and in the full-screen **Menu** on phones.
- Links nested under a top-level link become its **dropdown**.
- If a dropdown contains **only collections**, it's shown in the large italic style (like "Collections" today). Otherwise it uses the small uppercase style (like "Shop").
- On phones, a dropdown of plain links (e.g. Shop → Dresses, Kaftans…) is listed directly in the menu, just like today.

Recommended structure, matching today's site (the developer supplies exact links at launch):
```
Shop            → Shop all
  Dresses, Kaftans, Coats, Swimwear, Accessories, Sale
Collections     → All collections
  Folklore, Whimsy, Psychedelics   (collection links)
Story           → About page
Events          → Events page
Journal         → Journal blog
```

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
| 2026-09-28 | 0: Foundation | Announcement bar, header menu (`main-menu`), footer (brand text, menu columns `footer` and `footer-info`, newsletter heading, location), theme settings (logo, favicon, sharing image, colours, social links). Guide created. |
