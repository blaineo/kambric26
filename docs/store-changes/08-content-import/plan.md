# Batch 08 (🟢): Phase 4 content import (pages, journal, events, menus)

**Why 🟢:** pages, blogs/articles, a new metaobject type and menus are read only by the Shopify-hosted theme. kambricgoods.com hard-codes its nav and info pages and reads its journal/events from its own CMS (CLAUDE.md guardrail 1; OWNER_TASKS §A7). The live-site diff still runs.

**Needs scopes** `write_content, write_metaobject_definitions, write_metaobjects` (owner re-authenticated 2026-09-28).

## What it does (`apply.py`; `--dry-run` prints every mutation)

| # | Record | Action | Source |
| --- | --- | --- | --- |
| 1 | Page `contact` (exists, id 113644699882: title "Contact", empty body, template `contact`) | **Update:** title "Contact Us", body, SEO title/description | `store-data/phase4/pages/` |
| 1 | Pages `about`, `events` | Create, empty body, templates `page.about` / `page.events`, SEO from `liquid/SEO.md` | owner-notes/about-events.md |
| 1 | Pages `wholesale`, `size-guide`, `shipping`, `returns` | Create, published, template = handle, SEO | `pages.json` + `*.html` |
| 2 | Blog `journal` | Create (comments closed). The empty default `news` blog is left alone | journal-info.md |
| 2 | 5 articles | Create with handle, tags, summary, body, original publish date, author "Kambric Goods", cover image + alt (Shopify copies it from the export URL), SEO description | `journal/posts.json` |
| 3 | Metaobject definition `kambric_event` | Create (storefront PUBLIC_READ) | about-events.md |
| 3 | 3 events | Create (all dated June–July 2026, so they list as past) | `events/events.json` |
| 4 | Menu `main-menu` | Keep Shop + Collections; **append** Story → About, Events → Events page, Journal → blog | |
| 4 | Menu `footer-info` | Set: Contact Us, Wholesale, Size Guide, Shipping, Returns & Exchanges | |

Body clean-up applied by the script: the leading `<h1>` is removed (the theme renders the page title as the H1), and the CTA link paragraphs are removed (they're button blocks in the new `page.contact/wholesale/returns.json` templates, with the eyebrows). The size-guide body keeps only its intro (the table and fit note are the template's Size table section).

Differences from the owner notes: the event **Description** is a multi-line text field, not rich text, because the theme prints it as plain text. Info pages each get their own template, so each has its own eyebrow and buttons.

**Not included:** photos (About/Events/home images: separate batch), the Shop category links (batch 03 at cutover), Privacy/Terms policies (🔴).

## Rollback (`rollback.py`, driven by `apply-log.json`)
Restore both menus from `before.json` → delete the 3 events and the definition → delete the 5 articles and the blog → delete the created pages → restore the contact page from `before-contact.json` (title "Contact", empty body, delete the SEO fields).

## Verify
- Shopify-hosted: `/pages/{about,events,contact,wholesale,size-guide,shipping,returns}`, `/blogs/journal` + 5 posts, `/about` → `/pages/about` redirects, nav shows Story/Events/Journal, footer Information column; `tools/page_check.py --preset all`.
- Admin: `after.json` (same query as `before.graphql`).
- kambricgoods.com: `live_site_snapshot.py` diff clean after 2 minutes.
