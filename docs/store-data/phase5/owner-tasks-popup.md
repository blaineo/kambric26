# OWNER_TASKS.md addition — Newsletter pop-up (Phase 5)

Paste into `docs/OWNER_TASKS.md` under the appropriate colour sections.

---

## 🔴 Cutover only (would change kambricgoods.com / checkout)

- **Create the `WELCOME15` discount** (Discounts → Create discount): a
  code discount named/coded `WELCOME15` (or whatever the pop-up's
  **Discount code** setting is set to), matching whatever the business
  wants it to actually do (15% off, first-order only, etc. — not
  specified by the theme). Discounts are shared with the live Replit
  site's checkout, so this must wait for cutover. **Until this exists,
  the pop-up will show a code that doesn't work at checkout** — the
  section itself has no way to verify the code exists, so treat this as a
  hard launch blocker if the pop-up is enabled with a code showing.
  - Alternative: leave the pop-up's **Discount code** setting blank
    (hides the code line entirely) and set up a Shopify Email welcome
    automation to send it instead — see D-11 below. That still needs the
    discount created at cutover, just not referenced by the theme.

- **Decide D-11** (newsletter code delivery): on-screen code (built,
  default) vs. Shopify Email automation vs. a third-party ESP (Klaviyo).
  Both of the first two options use the same sign-up form; switching is a
  one-field change (blank the discount code setting) plus, for the email
  option, building the Shopify Email flow triggered off the `newsletter`
  tag.

## 🟢 Safe now (Shopify-hosted playground only)

- **Upload the pop-up image** (optional — the pop-up works fine with no
  image, matching the 1440px screenshot):
  file `../replit site/assets/uploads/57e0fcb8-7716-4d64-b6cc-4e860f67b28b.jpg`
  (referenced in `data/settings.json` as `promo_popup_image`). Upload it
  to **Content → Files**, then set it on the pop-up section's **Image**
  setting in Customize. It can also be set directly in a template's JSON
  via `"shopify://shop_images/<filename-after-upload>"` if you're editing
  JSON by hand instead of the theme editor.
- **Turn the pop-up on and set copy/delay** in Customize whenever you're
  ready to test it on the practice site (`kambric-goods-2.myshopify.com`)
  — it's off by default, like the announcement bar.

## Where sign-ups land

No new admin surface: pop-up sign-ups become **Customers** with email
marketing consent and the tags `newsletter, popup` — same place as the
existing footer sign-up form (which is tagged `newsletter` only), so
**Customers → filter *Email subscribed* or tag `newsletter`** shows both.
