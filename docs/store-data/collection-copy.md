# Collection Copy Instructions

## What This Is

This spreadsheet contains collection descriptions and SEO metadata that lived as hard-coded text in the React shop application (`artifacts/shop/src/pages/categoryMeta.ts` and `Shop.tsx`). These values are now being migrated to editable Shopify collection data so that the store owner can manage copy in the Shopify admin without code changes.

## Shared-Data Status: Folklore, Psychedelics, and Whimsy

**⚠️ WARNING: Changes to descriptions are shared with the live Replit site.**

The live React app stores collection descriptions in two places:

1. **Hard-coded `COLLECTION_META`** (Shop.tsx, lines 13–17) — used when displaying collections in the shop browse sections
2. **Shopify collection description** — used on collection detail pages and SEO

When you edit the Shopify description for these collections, the changes will affect:

- **Collection detail page** (`/collections/:slug`): The description text is pulled from Shopify and displayed on the page
- **SEO meta description**: The `<meta name="description">` tag for collection detail pages uses the Shopify description (truncated to 160 characters)
- **JSON-LD schema**: Collection schema on detail pages includes the Shopify description

What will **NOT change** on the live site:
- The shop browse sections (e.g., `/shop`, `/shop/dresses`) will still show the hard-coded COLLECTION_META text. These remain in the React code and are independent of Shopify data.

**Practical impact:** Updating these descriptions in Shopify will change the collection detail page and SEO, but shoppers browsing from the main shop page will still see the React-rendered descriptions until the code is updated.

## Steps by Collection

### For Category Collections (Dresses, Kaftans, Coats, Swimwear, Accessories) and Sale

1. In Shopify Admin, go to **Products → Collections**
2. Click **Create collection**
3. Name the collection (e.g., "Dresses") and set Handle to match (e.g., `dresses`)
4. Leave Conditions empty (will configure automated filtering per `docs/CONTENT_GUIDE.md` §3a-A1)
5. Set **Channel availability** to **no channels** (unpublished) until launch. The live site reads the Online Store channel, so publishing now would show the collection on kambricgoods.com. Publish to **Online Store** at cutover.
6. Scroll to **Theme template** card and select:
   - For category collections: `collection.category`
   - For Sale: `collection.sale`
7. In the **Description** field, paste the exact copy from the `description_to_set` column
8. Scroll to **Search engine listing** and click **Edit**
9. Paste the `seo_title` into the title field
10. Paste the `seo_description` into the description field
11. Click **Save**

### For Curated Collections (Folklore, Psychedelics, Whimsy)

These already exist in Shopify. To update:

1. Go to **Products → Collections**
2. Click the collection name
3. Scroll to **Description** field and replace with the exact copy from `description_to_set`
4. Scroll to **Search engine listing**, click **Edit**
5. Update title and description as above
6. Click **Save**

---

## Current Live Shopify Descriptions (for comparison)

### Folklore
**Current (Shopify):**
> Rooted in Kati's earliest work — folk motifs, handwoven references, references to old-world textiles rendered in her unmistakable hand.

**To set (from COLLECTION_META):**
> Rooted in Kati's earliest work — folk motifs, handwoven references, the geometry of old-world textiles rendered in her unmistakable hand.

**Note:** The phrase "the geometry of" replaces "references to".

### Psychedelics
**Current (Shopify):**
> Kaleidoscopic color fields and geometric shapes

**To set (from COLLECTION_META):**
> The most vivid prints in the archive. Kati made these in the early '70s — kaleidoscopic colour fields that still feel ahead of their time.

**Note:** This is a significant change. The new text is much more descriptive.

### Whimsy
**Current (Shopify):**
> Inspiration drawn from fresh fruit on her table and advertisements in the latest women's fashion magazines to bouquets of freshly cut wildflowers in a vase.

**To set (from COLLECTION_META, originally "Botanicals"):**
> Drawn from Kati's garden studies along the St. Lawrence. Lush, saturated, alive — every stem and petal painted from the real thing.

**Note:** The Botanicals collection was renamed to **Whimsy** (handle: `whimsy`). The new description is entirely different and focuses on the source material rather than the inspirations.


> ⚠️ **Sale copy is stale.** The sale description and SEO text come from the old site and still say "20% off … through the end of August". Rewrite them for the current promotion before assigning, and remember the heading on the sale page is a section setting (no discount is hard-coded in the theme).
