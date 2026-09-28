# Batch 05: collection search listings (🟢)

Sets only the **Search engine listing** (SEO title + meta description) of Folklore, Psychedelics and Whimsy. The live site reads collection **title**, **description** and **image**, never the SEO fields, and the mutation doesn't send title or description at all.

| Collection | Before | SEO title | Meta description |
| --- | --- | --- | --- |
| Folklore | none | **Folklore | Kambric Goods** | Rooted in Kati's earliest work — folk motifs, handwoven references, the geometry of old-world textiles rendered in her unmistakable hand. |
| Psychedelics | none | **Psychedelics | Kambric Goods** | The most vivid prints in the archive. Kati made these in the early '70s — kaleidoscopic colour fields that still feel ahead of their time. |
| Whimsy | none | **Whimsy | Kambric Goods** | Inspiration drawn from fresh fruit on her table and advertisements in the latest women's fashion magazines to bouquets of freshly cut wildflowers in a vase. |

- Folklore / Psychedelics: the fuller copy from the old site's code (`store-data/collection-copy.csv`).
- **Whimsy: its own current Shopify description**, not the sheet's text. The sheet's Whimsy copy came from the old *Botanicals* entry ("garden studies along the St. Lawrence"), but Whimsy's actual description is about fresh fruit and period advertisements, so the Botanicals text would misdescribe it. (Also flagged in the copy sheet for cutover.)
- Titles use the site's `{name} | Kambric Goods` pattern; the theme won't add a second "| Kambric Goods".

**Rollback:** `rollback.graphql` clears the SEO fields back to empty (their state in before.json).
