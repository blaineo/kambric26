# Owner tasks: About / Events (Phase 4)

Merge into `docs/OWNER_TASKS.md` §A (all 🟢 — everything below is new Shopify-hosted data: a new metaobject type, two new pages, and image uploads. The live kambricgoods.com Replit site doesn't read any of it).

---

## 🟢 1. Create the `kambric_event` metaobject definition

**Content → Metaobjects → Add definition**, or run this as an Admin GraphQL batch (`metaobjectDefinitionCreate`). Either way, use this exact shape:

```json
{
  "name": "Event",
  "type": "kambric_event",
  "fieldDefinitions": [
    {
      "key": "title",
      "name": "Title",
      "type": "single_line_text_field",
      "required": true
    },
    {
      "key": "start_date",
      "name": "Start date",
      "type": "date",
      "required": false,
      "description": "Leave blank for a TBA / undated event."
    },
    {
      "key": "date_label",
      "name": "Date label override",
      "type": "single_line_text_field",
      "required": false,
      "description": "Shown instead of the formatted Start date — e.g. \"TBA\" or \"Summer 2026\". Leave blank to show Start date formatted as \"June 20, 2026\"."
    },
    {
      "key": "time_label",
      "name": "Time",
      "type": "single_line_text_field",
      "required": false,
      "description": "e.g. \"6–8pm\". Only shown on upcoming events."
    },
    {
      "key": "venue",
      "name": "Venue",
      "type": "single_line_text_field",
      "required": false
    },
    {
      "key": "city",
      "name": "City",
      "type": "single_line_text_field",
      "required": false
    },
    {
      "key": "description",
      "name": "Description",
      "type": "rich_text_field",
      "required": false
    },
    {
      "key": "image",
      "name": "Image",
      "type": "file_reference",
      "required": false,
      "validations": [
        { "name": "file_type_options", "value": "[\"Image\"]" }
      ],
      "description": "Not shown on the page today (the source design doesn't show event photos) but included in the event's structured data (JSON-LD) when set."
    },
    {
      "key": "url",
      "name": "URL",
      "type": "url",
      "required": false,
      "description": "Optional — an RSVP page, Instagram post, or venue link."
    },
    {
      "key": "status_override",
      "name": "Status override",
      "type": "single_line_text_field",
      "required": false,
      "validations": [
        { "name": "choices", "value": "[\"upcoming\",\"past\"]" }
      ],
      "description": "Only needed for an undated event that should list as past, or to force a dated event into the other list. Leave blank otherwise — the theme derives status from Start date vs. today."
    }
  ],
  "access": { "storefront": "PUBLIC_READ" },
  "capabilities": { "publishable": { "enabled": false } }
}
```

Notes for whoever runs the batch:
- No `resolvable`/`renderable` capability is needed — the theme reads all entries via `metaobjects.kambric_event.values` in `sections/events-list.liquid`, not via a dedicated metaobject page.
- `status_override`'s `choices` validation restricts the admin field to a dropdown with exactly `upcoming` / `past`.
- Until this definition exists, `templates/page.events.json` renders its empty state ("Nothing on the calendar right now.") — that's expected, not a bug.

## 🟢 2. Add event entries

Add entries under **Content → Metaobjects → Event**. The 3 events from the old CMS export (all already in the past relative to today, 2026-09-28 — add fresh upcoming ones when you have real dates; these are here for parity/testing):

| Title | Start date | Time | Venue | City | Description |
| --- | --- | --- | --- | --- | --- |
| Embroidery Pop-up | 2026-06-20 | 6–8pm | The Box Office | San Anselmo, CA | Celebrate the Grand opening of The Box Office and get something embroidered! |
| Pop-Up Shop | 2026-06-27 | 11am–4pm | River Electric | Guerneville, CA | Join us by the pool at River Electric in Guerneville, Saturday June 27th for their Adults Only weekend. Grab a day pass, lounge by the pool and shop some of our newest swim styles and summer linens. |
| Summer Soiree | 2026-07-11 | 11am–4pm | House of Still | San Rafael, CA | Come shop from local designers and makers, enjoy live music, food and drinks at the gorgeous new space curated by The Still Collective. |

Leave `date_label`, `image`, `url` and `status_override` blank for all three (none are needed — real dates classify them as past automatically).

## 🟢 3. Create the About and Events pages

**Online Store → Pages → Add page**:
- **About** — handle `about` (so it replaces the legacy `/about` URL cleanly), Theme template **`page.about`**. Body content can stay empty; every section's content lives in the template/section settings, not the page body.
- **Events** — handle `events`, Theme template **`page.events`**. Same — leave the page body empty.

Then in **Customize**, open each page and review the section settings (all defaults already match the old site's copy — see `docs/CONTENT_GUIDE.md` for how to edit them). Add the images below while you're there.

Add both to **Content → Menus → main-menu** ("Story" → `/pages/about`, "Events" → `/pages/events`) — this is the "Main menu Part B" item already flagged ⏳ in `docs/OWNER_TASKS.md` §A1.

## 🟢 4. Upload images and set them on the sections

Image pickers can't be pre-filled by Claude (they need a Shopify file ID, and nothing in this export is uploaded to Files yet), so every image below defaults to empty and both pages currently render text-only bands — intentional, not a bug. Upload each file once to **Content → Files**, then set it on the named section/setting in Customize.

| Source file (`../replit site/assets/uploads/`) | Suggested Files name | Page → Section → Setting |
| --- | --- | --- |
| `f0f9ec76-6f34-4b8e-a0b2-191598aa6c1f.png` | `about-hero-background.png` | About → **About hero** → Background image |
| `8e398c1e-121c-4dd4-8fda-ad93ab09deb6.png` | `about-kati-portrait.png` | About → **About: story block** (Kati instance, "Art brought her solace.") → Image |
| `6a111639-c498-4c46-b9fe-be9fda9234b4.jpg` | `about-daisy-portrait.jpg` | About → **About: story block** (Daisy instance, "The youngest sister.") → Image |
| `6918a3aa-ee1b-4f88-8017-4221ec6801ce.jpg` | `about-closing-banner.jpg` | About → **CTA banner** → Image |
| `90918ee5-4c80-4575-be36-979fce68dd93.jpg` | `events-hero-background.jpg` | Events → **Events hero** → Background image |

All five are already-downloaded exports (`../liquid/assets/usage-map.csv` confirms the mapping); none need re-shooting or cropping before upload. Once each is set, that section automatically becomes the page's priority (LCP) image — no other setting change needed.

## 🟢 5. Double-check after publishing

- View `/pages/about` and `/pages/events` at 1440 and 390px against `../replit site/design/screenshots/{about,events}-{1440,390}.png`.
- Confirm exactly one `<h1>` per page (the hero heading) and that the images load with no layout shift.
- Once 3+ events exist, check Google's Rich Results Test on `/pages/events` for the `Event` JSON-LD (only entries with a real Start date emit it).
