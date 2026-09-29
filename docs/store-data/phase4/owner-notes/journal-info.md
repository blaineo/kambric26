# Phase 4 additions for OWNER_TASKS.md — Journal and info pages

(Draft for whoever merges Phase 4 into `docs/OWNER_TASKS.md`. Tagged per
CLAUDE.md guardrail 10: 🟢 safe now [Shopify-hosted only] / 🟡 safe if done
exactly as written / 🔴 cutover only. None of these are 🔴 except the
policies step, which is called out separately.)

## 🟢 1. Create the Journal blog

**Online Store → Blog posts → Manage blogs → Add blog.**

- Title: `Journal`
- Handle: `journal` (Shopify may need this typed manually — the theme and
  every redirect in the migration plan assume `/blogs/journal`, not
  `/blogs/news`)
- Template: leave as the default `blog` template (already wired to the new
  `main-blog` section — nothing else to pick)
- Comments: off (matches the current site; there's no comment UI ported)

Safe now: this only affects the Shopify-hosted playground until DNS
cutover, and creating a blog is explicitly 🟢 in guardrail 10.

## 🟢 2. Import the 5 journal posts

Source: `../liquid/../replit site/data/journal-posts.json` (already reviewed
by the developer). For each of the 5 posts (`first-look-ss27`,
`where-kambric-began`, `arielle-dress`, `chainstitch`,
`gearing-up-for-dallas`):

1. **Content → Blog posts → Journal → Add blog post.**
2. Title: the post's `title`.
3. **Handle** (under the post's "Search engine listing" section, or the
   URL/handle field): set to the post's `slug` exactly, so
   `/blogs/journal/{slug}` matches the redirect list in the migration plan.
4. **Tag**: one tag only, the post's `category` — but **normalize casing
   first** (migration plan item 3.14): use "The Archive" (not "the
   archive") for `where-kambric-began` and `arielle-dress`, and "Craft" (not
   "craft") for `chainstitch`. `first-look-ss27` → "Photoshoot",
   `gearing-up-for-dallas` → "Development" (already correctly cased).
5. **Content**: switch the editor to **Show HTML** (the `</>` icon) and
   paste the post's `body_html` value directly — it's already valid HTML,
   so this preserves paragraphs/links exactly. Switch back to the visual
   editor afterward to confirm it renders as expected.
6. **Featured image**: upload the image the `cover_image_url` field points
   to (download it once from that URL, then upload to Files/the post).
7. **Published date**: set to the post's `published_at` date so the posts
   sort the same as they do today.
8. **Search engine listing** (bottom of the page): title can be left blank
   (the theme composes "*Title* \| Kambric Goods Journal" automatically —
   see the note to the developer below); description → the post's
   `seo.description` value.

## 🟢 3. Create the info pages

**Online Store → Pages → Add page**, five pages:

| Title | Handle | Template |
| --- | --- | --- |
| Contact Us | `contact` | `page` (default) |
| Wholesale | `wholesale` | `page` (default) |
| Size Guide | `size-guide` | `page.size-guide` |
| Shipping | `shipping` | `page` (default) |
| Returns & Exchanges | `returns` | `page` (default) |

Copy for each page (eyebrow, intro, section headings/paragraphs, button
labels/links) is in `liquid/content/hardcoded.json` under `infoPages`, and
was already ported into this phase's dev notes
(`content-guide-journal-info.md`) — follow that for exactly which field
each piece of copy goes in and how to add the CTA buttons. The size-guide
row data (XS–XL) is pre-filled as section defaults; only the fit-note CTA
link needs to be set (defaults to `mailto:howdy@kambricgoods.com`).

Set the **Template** dropdown (right sidebar) to `page.size-guide` for the
Size Guide page only; the other four use the default `page` template.

## 🟢 4. Link the new pages into the menus (CONTENT_GUIDE §3a "Part B")

Now that the Journal blog and info pages exist, finish the footer-info menu
that Part A of the menu setup left pointing at nothing:

- **Content → Menus → footer-info** — point `Contact Us`, `Wholesale`,
  `Size Guide`, `Shipping`, `Returns & Exchanges` at the pages created in
  step 3 (search by page title instead of pasting a URL).
- **Content → Menus → main-menu** (or wherever "Journal" was left
  unlinked) — point it at the Journal blog created in step 1.

## 🔴 5. Policies (out of scope for this phase — do not do yet)

Privacy Policy and Terms of Service move to **Settings → Policies**
eventually, but that page is shown at checkout, which is shared with the
live Replit site (CLAUDE.md guardrail 1). **Don't touch Settings →
Policies before DNS cutover.** The current privacy-policy/terms-of-service
copy is preserved in `liquid/content/hardcoded.json` for whenever that
step is scheduled.

## For the developer, not the owner

The Journal post title pattern (`{title} | Kambric Goods Journal`) and the
"noindex the Journal index until it has posts" rule both need a small
change to `snippets/meta-tags.liquid`, which this phase doesn't own —
flagged in the Phase 4 report with the exact Liquid to add. Once that
lands, step 2's "Search engine listing" title fields can stay blank as
written above.
