# Phase 4 Store Data: Extraction Summary

Mechanical extraction of import-ready content files for Shopify store batches from Replit and Liquid template sources.

## File Manifest

### Journal Posts
**File:** `journal/posts.json`
- **Count:** 5 published posts
- **Structure:** Array of post objects with:
  - `handle` (slug for URL)
  - `title` 
  - `tags` (normalized category to Title Case: "craft" → "Craft", "the archive" → "The Archive", "Photoshoot" → "Photoshoot", "Development" → "Development")
  - `summary_html` (excerpt wrapped in `<p>` tags)
  - `body_html` (source HTML from journal-posts.json, with preserved formatting including `<p style="margin:0"></p>` spacers in "Where Kambric Began")
  - `published_at` (ISO 8601 timestamp)
  - `image` object with `local_file` (UUID-based path), `alt` text (factually derived from post context), and `source_url` (Replit API URL)
  - `seo` object with `title` and `description`
  - `product_handles` (empty array; no product links in source data)

**Inline Images:** None detected in body_html. All cover images map to local exported files in `assets/uploads/` directory.

**Source:** `/Users/blaine/Code/kambric/replit site/data/journal-posts.json`

---

### Events
**File:** `events/events.json`
- **Count:** 3 upcoming events
- **Structure:** Array of event objects with:
  - `handle` (slugified: `{title-slugified}-{date}`)
  - `fields` object containing:
    - `title` 
    - `start_date` (ISO YYYY-MM-DD format, parsed from date_label: June 20, 2026 → 2026-06-20)
    - `date_label` (original free-text date string from source)
    - `time_label` (time range from date_line)
    - `venue`
    - `city`
    - `description` (source blurb as plain text)
    - `status_override` (null for all; all events have `status: "upcoming"` in source)
    - `sort_order` (preserved from source)

**File:** `events/hero.json`
- **Structure:** Single hero image object with `hero_image_file` (UUID-based path), `source_uuid`, and `alt` text

**Dates:** All events are from June–July 2026 and were marked as "upcoming" in the source data (created/updated dates predate cutover).

**Source:** `/Users/blaine/Code/kambric/replit site/data/events.json` and `/Users/blaine/Code/kambric/replit site/data/events-content.json`

---

### Info Pages
**Files:**
- `pages/contact.html`
- `pages/wholesale.html`
- `pages/size-guide.html`
- `pages/shipping.html`
- `pages/returns.html`

**Structure:** Page body HTML only (no header/footer wrapper). Contains:
- Headings (`<h1>`, `<h2>`)
- Paragraphs (`<p>`)
- Lists (where applicable)
- **size-guide.html:** Real HTML `<table>` with `<caption>`, `<thead>`, `<th scope="col">`, and `<tbody>` (proper semantic table for size measurements)
- Links preserved: `<a href="mailto:...">` (contact forms) and `<a href="https://...">` (JOOR link in wholesale)

**File:** `pages/pages.json`
- **Count:** 5 pages
- **Structure:** Array of page metadata with:
  - `handle` (URL slug)
  - `title`
  - `template_suffix` ("contact", "wholesale", "size-guide" only where rendered layout has clear extra CTAs; empty string for shipping and returns)
  - `seo` object with `title` and `description`
  - `body_file` (reference to HTML file in same directory)

**Source:** `/Users/blaine/Code/kambric/liquid/content/hardcoded.json`, rendered `/Users/blaine/Code/kambric/liquid/html/info-*.html`, and SEO metadata from `/Users/blaine/Code/kambric/liquid/SEO.md`

---

### Policies
**Files:**
- `policies/privacy-policy.html`
- `policies/terms-of-service.html`

**Structure:** Policy body HTML only. To be imported to Shopify Settings → Policies (shown at checkout, shared with live site). Contains headings, paragraphs, and links.

**Note:** These are hardcoded storefront copy, not customer data or personal information. Contact addresses (hello@kambricgoods.com, howdy@kambricgoods.com) are public business strings from source code.

**Source:** `/Users/blaine/Code/kambric/liquid/content/hardcoded.json` and rendered `/Users/blaine/Code/kambric/liquid/html/info-{privacy-policy,terms-of-service}.html`

---

## Image Assets

All image files referenced in JSON are expected to be present at:
```
assets/uploads/{uuid}.{jpg,png}
```

Example UUIDs from posts and events:
- `b273426a-f5ca-4e62-8a72-ebc264616e1b.jpg` (Where Kambric Began cover)
- `5bb84244-0f3a-46eb-839f-5fac22d20629.jpg` (First Look at SS27 cover)
- `90918ee5-4c80-4575-be36-979fce68dd93.jpg` (Events hero)
- (and 13 others)

**Source:** `/Users/blaine/Code/kambric/replit site/assets/uploads/` (locally exported from Replit object storage)

**Asset Mapping:** `usage-map.csv` documents which UUID belongs to which content field and database table.

---

## Validation & Counts

**JSON Files:**
- `journal/posts.json`: ✓ Valid (5 posts)
- `events/events.json`: ✓ Valid (3 events)
- `events/hero.json`: ✓ Valid (1 object)
- `pages/pages.json`: ✓ Valid (5 pages)

**HTML Files:** 7 files (5 info pages + 2 policies)

**Total Content Objects:**
- Posts: 5
- Events: 3
- Pages: 5
- Policies: 2 (not counted in pages.json)

---

## Review Notes & Caveats

### ✓ Complete & Ready
- Journal posts: all 5 extracted with cover images, SEO data, and body HTML
- Events: 3 events with parsed ISO dates and sort order
- Pages: body copy extracted cleanly with semantic HTML (tables, links preserved)
- SEO metadata: titles and descriptions from source pulled correctly
- Category/tag normalization: applied Title Case transformation to journal categories

### ⚠ Items Requiring Human Review

1. **No Product Links Found**
   - All journal posts have empty `product_handles` arrays
   - Source data includes `product_links: []` for all posts
   - No products were mentioned or linked during extraction
   - Verify manually if product associations should be added post-import

2. **Event Dates: All Past-Relative**
   - Events are dated June–July 2026 (relative to cutover in Sept 2026)
   - All marked `status: "upcoming"` in original DB but are now historical
   - Consider reclassifying to "past events" or archiving in Shopify

3. **Replit API URLs in Image Source**
   - Image `source_url` fields reference Replit object storage: `https://kambricgoods.com/api/storage/objects/uploads/{uuid}`
   - These URLs will become dead links after Replit site cutover
   - **Action:** Confirm images are available locally in `assets/uploads/` before importing
   - **Action:** Plan to host images on Shopify (Files or Media) at cutover

4. **No Inline Images in Post Bodies**
   - Parsed body_html for `/api/storage/...` references: none found
   - All post images are cover images, not embedded in body text
   - Reduces risk of broken inline image links

5. **Contact/Wholesale CTAs**
   - Pages with `template_suffix` ("contact", "wholesale", "size-guide") should receive layout template with email form / CTA buttons in Shopify
   - Email addresses preserved: `howdy@kambricgoods.com`, `hello@kambricgoods.com`
   - JOOR link preserved in wholesale page

6. **Size Guide Table**
   - Real HTML table with proper `<caption>`, `<thead>`, `<th scope="col">`, `<tbody>`
   - Measurements in inches; no unit conversion applied
   - Verify Shopify's rendering matches source layout

7. **Privacy Policy & Terms Email**
   - Privacy policy contact: `hello@kambricgoods.com` (different from other pages; preserved as-is from source)
   - These policy files go to Settings → Policies in Shopify (separate import workflow)

---

## Import Workflow

Import is done later by an approved store batch (`docs/store-changes/`). 

**Shopify Destinations:**
- 🟢 **Blog posts** (from `journal/posts.json`): Blog metaobject or Blog Post collection
- 🟢 **Events** (from `events/events.json`): Custom metaobject or Events list (if available in theme)
- 🟢 **Pages** (from `pages/pages.json` + HTML): Shopify Pages (public, appear in footer/navigation)
- 🔴 **Policies** (from `policies/*.html`): Settings → Policies (shown at checkout, shared with live site) — **cutover only**

---

## File Sizes & Technical Notes

- **journal/posts.json:** ~15 KB (5 posts, with full body HTML)
- **events/events.json:** ~2 KB (3 events)
- **events/hero.json:** <1 KB
- **pages/pages.json:** ~1.5 KB
- **HTML files:** 2–8 KB each (7 files total)

**Character Encoding:** UTF-8 (all files)

**No External Dependencies:** JSON and HTML are self-contained; image files are referenced by path only.

---

Generated: 2026-09-28
Source: Replit site data, Liquid template content, and asset mapping
