# Batch 18: URL mapping (GSC cleanup, 2026-10-07)

Fetched live as Googlebot. `www.` sources take one extra hop (Shopify's www → apex domain redirect runs first); unavoidable on Shopify.

| URL | Now | Planned |
| --- | --- | --- |
| `/home/p/maty-car-coat` | 200 → /products/vera-car-coat?variant=46124608356586 | keep (already 1 hop to 200) |
| `/home/p/maty-car-coat-pffhg` | 404 (noindex) | **301 → /products/vera-car-coat?variant=46124608356586** (new, batch 18) |
| `/home/p/maty-slip-dress` | 200 → /products/kati-slip-dress-in-matyo-floral | keep (already 1 hop to 200) |
| `/home/p/maty-slip-dress-nwg8z` | 200 → /products/jessie-slip-dress-in-twilight-plumes | keep (already 1 hop to 200) |
| `/home/p/magnolia-one-piece` | 200 → /products/margit-one-piece?variant=46124606882026 | keep (already 1 hop to 200) |
| `/home/p/magnolia-kaftan-dress` | 200 → /products/esther-kaftan?variant=46124608127210 | keep (already 1 hop to 200) |
| `/home/p/moonillusion-onepiece` | 200 → /products/margit-one-piece?variant=46124606095594 | keep (already 1 hop to 200) |
| `/home/p/pastel-asterisk-one-piece` | 200 → /products/margit-one-piece?variant=46124606488810 | keep (already 1 hop to 200) |
| `/home/p/orange-asterisk-one-piece` | 200 → /products/margit-one-piece?variant=46124606685418 | keep (already 1 hop to 200) |
| `/home/p/presale-linen-slip-dress-in-grapefruit-tartan` | 200 → /products/zadie-linen-dress?variant=46124607537386 | keep (already 1 hop to 200) |
| `/home/p/presale-linen-slip-dress-in-grapefruit-tartan-2x9xt` | 404 (noindex) | **301 → /products/zadie-linen-dress?variant=46124607537386** (new, batch 18) |
| `/home/p/presale-wildflowers-one-piece-maillot` | 404 (noindex) | **301 → /products/margit-one-piece?variant=46124607209706** (new, batch 18) |
| `/home/p/wildflowers-linen-slip-dress` | 200 → /products/zadie-linen-dress?variant=46124607340778 | keep (already 1 hop to 200) |
| `/home/p/twilight-blue-silky-slip-dress` | 404 (noindex) | **301 → /products/jessie-slip-dress-in-twilight-plumes** (new, batch 18) |
| `/home/p/twilight-blue-silk-scarf` | 404 (noindex) | **301 → /products/bodie-scarf-in-twilight-plumes** (new, batch 18) |
| `/home/p/good-vibrations-kaftan-dress` | 200 → /products/esther-kaftan?variant=46124607930602 | keep (already 1 hop to 200) |
| `/home/p/good-vibrations-kaftan-dress-csytw` | 404 (noindex) | **301 → /products/esther-kaftan?variant=46124607930602** (new, batch 18) |
| `/home/p/good-vibrations-one-piece` | 200 → /products/margit-one-piece?variant=46124606292202 | keep (already 1 hop to 200) |
| `/home/p/good-vibrations-one-piece-8kal6` | 404 (noindex) | **301 → /products/margit-one-piece?variant=46124606292202** (new, batch 18) |
| `/home/p/dahlia-seed-kaftan-dress` | 200 → /products/esther-kaftan?variant=46124608028906 | keep (already 1 hop to 200) |
| `/home/p/dahlia-seed-scarf` | 200 → /collections/accessories | keep (already 1 hop to 200) |
| `/home/p/midnight-gingko-twill-coat` | 404 (noindex) | **301 → /products/vera-car-coat?variant=46124608225514** (new, batch 18) |
| `/home/p/rattlesnake-scarf` | 200 → /collections/accessories | keep (already 1 hop to 200) |
| `/home/p/rattlesnake-scarf-k2afd` | 200 → /products/goldie-bandana-in-matyo-floral | keep (already 1 hop to 200) |
| `/home/p/rattlesnake-scarf-k2afd-8wz8j` | 200 → /collections/accessories | keep (already 1 hop to 200) |
| `/home/p/rattlesnake-scarf-3l62x` | 200 → /products/bodie-scarf-in-twilight-plumes | keep (already 1 hop to 200) |
| `/home/p/hampui-x-kg-lavender-cowboy-hat` | 404 (noindex) | **301 → /collections/accessories** (new, batch 18) |
| `/home/p/apkzi93scxf8ppzkdm53czi4vvpr3d` | 404 (noindex) | 404 (Saffron Damask Linen Napkin Set, discontinued; no home-goods collection) |
| `/home/p/jzpd3aexzcec3hafzzw7ph7dshc040` | 404 (noindex) | 404 (Retro Stripe Linen Napkin Set, discontinued; no home-goods collection) |
| `/home/p/a1ogkdunwrp6hwigpywndfntng96sr` | 404 (noindex) | 404 (unidentified) |
| `/home/p/1995smpszq5ysdlp94s5691scfrcg5` | 404 (noindex) | 404 (unidentified) |
| `/home/p/8obazrlhk1qbrc5m4zp5ni1l6r8r6j` | 404 (noindex) | 404 (unidentified) |
| `/home/p/o6s0c8y09agq8nhgft75wti2yf9mtm` | 404 (noindex) | 404 (unidentified) |
| `/home/p/oycpr7s44mlixppo0oa5o49h949ho4` | 404 (noindex) | 404 (unidentified) |
| `/home/shop-all` | 404 (noindex) | **301 → /collections/all** (new, batch 18) |
| `/home/home-goods` | 404 (noindex) | 404 (home goods discontinued; no matching collection) |
| `/home/accessories` | 200 → /collections/accessories | keep (already 1 hop to 200) |
| `/home/accessories/scarves` | 404 (noindex) | **301 → /collections/accessories** (new, batch 18) |
| `/home/accessories/hats` | 404 (noindex) | **301 → /collections/accessories** (new, batch 18) |
| `/home/womenswear/dresses` | 200 → /collections/dresses | keep (already 1 hop to 200) |
| `/home/womenswear/kaftans` | 200 → /collections/kaftans | keep (already 1 hop to 200) |
| `/home/womenswear/coats` | 200 → /collections/coats | keep (already 1 hop to 200) |
| `/home/womenswear/swimwear` | 200 → /collections/swimwear | keep (already 1 hop to 200) |
| `/happenings/embroidery-pop-up-riverco` | 404 (noindex) | **301 → /pages/events** (new, batch 18) |
| `/products/8690544312554` | 200 → /products/margit-one-piece | keep (already 1 hop to 200) |
| `/products/8690544378090` | 200 → /products/esther-kaftan | keep (already 1 hop to 200) |
| `/blogs/news` | 200 (noindex) | **301 → /blogs/journal** (new, batch 18) |
| `/shop` | 200 | 200 thin redirect page → /collections/all or /collections/<category> (instant meta refresh + JS; Shopify reserves /shop, no 301 possible) |
| `/stockists` | 404 (noindex) | 404 (retired on purpose) |
