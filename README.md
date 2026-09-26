# Thumb Fin — Shopify theme (homepage redesign)

This repo is the thumbfin.com theme (**Dawn 12.0.0**, live "Thumb Fin" theme exported 25 Sep 2026) with the homepage redesign from `docs/thumbfin-redesign.html` built in. The original brief is in `docs/thumbfin-redesign-notes.md`.

The baseline commits hold the unmodified export, so `git diff` against it shows exactly what the redesign changed:

| File | Change |
| --- | --- |
| `sections/thumbfin-home.liquid` | **New.** The redesigned homepage as one section |
| `sections/thumbfin-product-extras.liquid` | **New.** Under the product on every product page: trust strip, "Complete your setup" offers (Combo with live savings + contact paper), how it works, demo video |
| `sections/thumbfin-cart-upsell.liquid` | **New.** On the cart page: offers the contact paper and the Combo, only when they aren't already in the cart |
| `snippets/thumbfin-*.liquid` | **New.** Shared pieces: offer card, trust strip, steps, video, and the product-page buy-box note |
| `assets/thumbfin.css`, `assets/thumbfin.js` | **New.** Shared styles and scripts for all of the above |
| `templates/product.json`, `templates/product.remote.seller.json` | Product-extras section added under the product. A buy-box note ("Can't pick a version? The Combo… saving $10" / "Satin or matte bass? Add contact paper…") added under Add to cart as a Custom liquid block |
| `templates/cart.json` | Cart add-ons section added between the items and the totals |
| `templates/index.json` | New section added at the top. The sections it replaces are **hidden, not deleted**: the "Experience Playing Like Never Before" rich text, the Judge.me carousel section (moved into the new section), the "Not sure which one?" Combo text, the featured Combo product and the video. The photo banner, Instagram heading + Instafeed, featured products, About and blog stay. Featured products, About and blog switched to the new dark colour scheme |
| `config/settings_data.json` | **Site-wide restyle.** The theme's five built-in colour schemes are recoloured to the redesign palette (see below), fonts changed from Assistant to Oswald (headings) + Work Sans (body), and buttons, inputs, cards, images and pop-ups get slightly rounded corners (3–6px). Also adds "scheme-thumbfin" |
| `sections/header-group.json`, `sections/footer-group.json` | Announcement bar, header, menu and footer switched to the new scheme |

## Every page gets the new look

Dawn draws every page from the same global colour schemes and fonts, so the redesign is applied there once instead of copied into each template. Every template in `templates/` picks it up:
home, product (both templates), collection, all collections, cart and cart pop-up, search, blog, article, standard page, contact, collabs, 404, password, gift card, and the customer account pages (login, register, account, orders, addresses, reset/activate password).

| Scheme (as named in the editor) | Used for | Now |
| --- | --- | --- |
| Background 1 | Page background on every page, cart pop-up | Walnut `#241408`, cream text, neon buttons |
| Background 2 | Product / collection / blog cards | Panel brown `#2f1c0e`, cream text, neon buttons |
| Inverse | Sold-out badge, image banner | Dark `#1a0e05`, cream text |
| Accent 1 | Accent | Brass `#cf9d3e`, dark text |
| Accent 2 | Sale badge | Neon `#c3ff5c`, dark text |

All five pass WCAG AA contrast for text and buttons (lowest is 7.7:1; AA needs 4.5:1). The pages keep their existing content and layout; only the look changes. The homepage is the one page whose content was rebuilt.

**Not controlled by the theme:** checkout and Shopify's new customer accounts are styled under Settings → Checkout → Customize. App widgets use their own colour settings (see checklist).

## Product and cart pages

**Product pages** (every product, both product templates):
- Under **Add to cart**, a short note: "Can't pick a version? The Combo 3-Pack gets you one of each for $50, saving $10." plus "Satin or matte bass? Add the contact paper ($2)…". The combo line is hidden on the combo's own page, and the whole note is hidden on the paper's page.
- Below the product: trust strip → **Complete your setup** (Combo with "Save $10" + contact paper, each with its own Add to cart that opens the cart pop-up) → Three steps, no tools → demo video → then your existing "You may also like" and Judge.me reviews.
- The page never offers the product you're already looking at. On the combo or paper page it offers the single instead, once *Single Thumb Fin* is picked in the section.

**Cart page:** "Add to your order" shows the contact paper and the Combo, each hidden once it's in the cart, and nothing at all when the cart is empty. Adding reloads the cart page, so items and totals update.

## What the homepage section does

Hero (pain-point headline, rating badge, dual CTA, your existing hero photo) → trust strip → 3-step "how it works" → single-product spotlight with colour swatches → Combo 3-Pack + contact-paper cross-sell → **your real Judge.me reviews** → your demo video with its existing cover image.

- **Add to cart** goes through Dawn's own `<product-form>`, so the "added to cart" popup appears just like on product pages.
- **Swatches:** one per colour variant, using Shopify's variant swatch colour if set, otherwise the "Swatch colours" setting. Sold-out colours are crossed out and can't be picked. Choosing a colour updates the price, the colour name and the photo.
- **"Save $10":** calculated from live prices (3 × single price − combo price), shown with "vs $60 buying 3 separately".
- **Rating badge:** reads the rating Judge.me syncs to Shopify's standard review metafields. Falls back to the text settings (4.84 / 145).
- **Reviews:** the Judge.me cards carousel from the old homepage, moved into the section and restyled for the dark background. The mockup's paraphrased quotes are **not** used.
- **Video:** loads only when the visitor clicks play.
- **CSS scoping:** every class starts with `tfr-` and every rule sits under `.tfr`, so the section can't affect the rest of the theme.

## Try it on an unpublished copy

**Option A: upload the zip (easiest)**
1. Get `thumbfin-theme-redesign.zip`, or build it with the command below.
2. Shopify admin → Online Store → Themes → **Add theme → Upload zip file**. It arrives as a new, **unpublished** theme. The live site is untouched.
3. On that theme, click **Customize** and pick your $20 single product under **Single Thumb Fin** in three places: Home page → *Thumb Fin homepage*; Products → any product → *Thumb Fin product extras*; Cart → *Thumb Fin cart add-ons*. This is the one setting I couldn't fill in: the export doesn't include its product handle. (Product pages still work without it; it's needed for the homepage spotlight, the cart's savings tag, and offering the single on the combo's page.) The Combo is already set, and the contact paper is found by its handle `contact-paper-for-matte-finish`. If the paper card doesn't show, pick it under **Add-on (contact paper)**.
4. Click **Preview** and go through the checklist below.

**Option B: Shopify's GitHub integration**
Online Store → Themes → Add theme → **Connect from GitHub** → this repo → branch `claude/shopify-theme-redesign-ywsffv`. The theme then stays in sync with every push. Then do step 3 above.

Build the zip yourself with:

```sh
zip -r thumbfin-theme-redesign.zip assets blocks config layout locales sections snippets templates
```

## Before publishing

- [ ] Pick the single product (step 3).
- [ ] Add each colour to the cart and confirm the popup and cart show the right colour. Also add the Combo and the contact paper.
- [ ] On a product page: check the note under Add to cart, and add the Combo and the paper from "Complete your setup".
- [ ] On the cart page: the add-ons show, disappear once added, and adding one updates the totals.
- [ ] Check that a sold-out colour is crossed out.
- [ ] Look at the header on the dark background. If the logo is hard to see, change *Header* and *Announcement bar* back to their old colour scheme ("Accent 2", your blue) in the editor, or upload a light version of the logo.
- [ ] Check the hero photo. It uses `IMG_0004.jpg`, the first slide of the old slideshow, cropped to fit. Swap it under *Hero image* if another photo crops better.
- [ ] Confirm the rating badge. If it shows the fallback 4.84 / 145, Judge.me isn't syncing to Shopify's review metafields. Either turn that on in Judge.me's settings or keep the text settings up to date.
- [ ] Click through the other pages in preview: a product, a collection, the cart, search, a blog post, the contact page and a standard page.
- [ ] **Judge.me on the product page** (review widget and star badge): if any text is dark-on-dark, go to Judge.me → Settings → Widget and set text to light, or pick its dark theme.
- [ ] **Withdrawal (Widerruf) form on standard pages** keeps its own white box. That's readable; restyle it in that app's block settings if you want it dark.
- [ ] **Checkout:** match it under Settings → Checkout → Customize (background `#241408`, accent `#c3ff5c`) if you want the new look to carry through.
- [ ] Check on a phone.
- [ ] **Publish.** Themes → the uploaded copy → Publish.

## Keep in mind

- **The zip is a snapshot of 25 Sep 2026.** Customizer changes made to the live theme after that export won't be in the copy. Settings you edit on the copy are saved in Shopify, not in this repo, unless you use the GitHub integration (Option B), which commits them back.
- The swatch picker is used when the single product has one option named *Color* or *Colour*. Any other option setup falls back to a dropdown.
