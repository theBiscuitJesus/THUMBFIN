# Thumb Fin — homepage redesign (Shopify section)

A drop-in Shopify section that turns the static mockup in `docs/thumbfin-redesign.html` into a live homepage for thumbfin.com, with real prices, variants, add-to-cart forms and the demo video. The original brief is in `docs/thumbfin-redesign-notes.md`.

```
sections/thumbfin-home.liquid   ← the only file that goes into the theme
docs/thumbfin-redesign.html     ← original static mockup (reference)
docs/thumbfin-redesign-notes.md ← handoff notes / brief
```

This repo is **not a full theme**. It adds one section to your existing theme (Dawn or any other Online Store 2.0 theme) and changes nothing else.

## What's in the section

Hero (pain-point headline, rating badge, dual CTA) → trust strip → 3-step "how it works" → single-product spotlight with colour swatches → Combo 3-Pack + contact-paper cross-sell → review quotes → video. The theme's own header and footer stay as they are.

| Mockup placeholder | Now |
| --- | --- |
| `$20` price | `{{ variant.price }}`, updates when a colour is picked |
| Hard-coded colour circles | One swatch per variant. Colour comes from Shopify's variant swatch if set, else the "Swatch colours" setting. Sold-out colours are disabled |
| "Add to cart" link | Real `{% form 'product' %}` posting the selected variant id (works without JavaScript) |
| Combo / contact paper | Product pickers, falling back to the handles `combo-3-pack-one-of-each-version` and `contact-paper-for-matte-finish` |
| "Save $10" | Calculated live: single price × 3 − combo price (plus "vs $60 buying 3 separately"). Can be overridden with fixed text |
| ★ 4.84 / 145 | Read from the standard `reviews.rating` / `reviews.rating_count` product metafields that most review apps write. Falls back to the text settings |
| Testimonials | Editable "Review quote" blocks, plus an **app block** slot so a review app's widget (Judge.me, Yotpo, etc.) can be dropped in |
| Video placeholder | Click-to-load YouTube (`Y_QRGtpZdyI` by default) or Vimeo. Nothing loads from YouTube until the visitor clicks |
| Google Fonts | Oswald + Work Sans served from Shopify's font CDN, changeable in the editor |

The CSS is scoped: every class starts with `tfr-` and every rule sits under `.tfr`, so the section doesn't affect the rest of the theme, and theme styles (including Dawn's 10px root font size) don't distort the section.

## Install

1. **Duplicate the live theme:** Online Store → Themes → `…` → Duplicate. Do all of the following on the copy.
2. **Add the section file** using either method:
   - **Code editor:** on the duplicate, `…` → Edit code → Sections → *Add a new section* → name it `thumbfin-home` → replace its contents with `sections/thumbfin-home.liquid` → Save.
   - **Shopify CLI:** from a local checkout of the theme, copy the file into `sections/`, then run
     `shopify theme push --theme <duplicate-theme-id> --only sections/thumbfin-home.liquid`
3. **Add it to the homepage:** Customize the duplicate → Home page → *Add section* → **Thumb Fin homepage**. Drag it to the top, then hide or remove the old hero, the combo product block and the old video section it replaces.
4. **Pick products** in the section settings: *Single Thumb Fin*, and check that *Combo pack* and *Add-on* resolved to the right products.
5. **Set the colour scheme around it:** set the theme header and footer to a dark scheme (background `#241408`, text `#f4ecdd`) so they match the section.

## Before publishing

- [ ] **Replace the three review quotes.** The defaults are paraphrased placeholders from the mockup. Use the customers' exact words with their permission, or remove the quote blocks and add your review app's block instead.
- [ ] Add each colour to the cart and confirm the cart shows the right variant. Also add the combo and the contact paper.
- [ ] Check that a sold-out colour shows as crossed out and can't be added.
- [ ] Check on a phone: layout, swatches and video.
- [ ] Confirm the rating badge shows the live numbers. If it still shows the fallback 4.84 / 145, your review app doesn't write the standard metafields; either keep the text settings updated or turn off *Use live rating from review app*.
- [ ] Optional: upload real product photos. Set a *Hero image*, and add product/variant images to the single product. The spotlight uses them automatically and swaps the image per colour.
- [ ] Publish the duplicate theme.

## Notes

- Add to cart uses a plain form post to `/cart/add`. That goes to the cart page rather than opening the theme's cart drawer. If you want it to open the drawer, that has to be wired up for your specific theme.
- The swatch picker is used when the single product has one option named *Color* or *Colour*. Any other option setup falls back to a dropdown.
