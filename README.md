# Thumb Fin — Shopify theme redesign

**Status: live.** This branch is the published thumbfin.com theme, connected through Shopify's GitHub integration: pushes here go straight to the live store, and edits made in the theme editor are committed back by `shopify[bot]`. Pull before editing, and space out pushes that touch the same file (two pushes seconds apart can sync out of order).

This repo is the thumbfin.com theme (**Dawn 12.0.0**, live "Thumb Fin" theme exported 25 Sep 2026) with the homepage redesign from `docs/thumbfin-redesign.html` built in. The original brief is in `docs/thumbfin-redesign-notes.md`.

The baseline commits hold the unmodified export, so `git diff` against it shows exactly what the redesign changed:

| File | Change |
| --- | --- |
| `sections/thumbfin-hero.liquid`, `thumbfin-trust`, `thumbfin-steps`, `thumbfin-shop`, `thumbfin-video` | **New.** The redesigned homepage, as five separate sections you can reorder or hide in the editor |
| `sections/thumbfin-product-extras.liquid` | **New.** Under the product on every product page: trust strip, "Complete your setup" offers (Combo with live savings + contact paper), how it works, demo video |
| `sections/thumbfin-cart-upsell.liquid` | **New.** On the cart page: offers the contact paper and the Combo, only when they aren't already in the cart |
| `snippets/thumbfin-*.liquid` | **New.** Shared pieces: version card, offer card, swatch colours, trust strip, steps, video, and the product-page buy-box note |
| `assets/thumbfin.css`, `assets/thumbfin.js` | **New.** Shared styles and scripts for all of the above |
| `templates/product.json`, `templates/product.remote.seller.json` | Product-extras section added under the product. A buy-box note ("Can't pick a version? The Combo… saving $10" / "Satin or matte bass? Add contact paper…") added under Add to cart as a Custom liquid block |
| `templates/cart.json` | Cart add-ons section added between the items and the totals |
| `templates/index.json` | Homepage rebuilt: hero → trust strip → three steps → shop → your Judge.me reviews section (restyled) → video, then your photo banner, Instagram, featured products, About and blog. Replaced sections are **hidden, not deleted**: the "Experience Playing Like Never Before" rich text, the "Not sure which one?" Combo text, the featured Combo product and the old video. Featured products, About and blog use the new dark scheme |
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

## The homepage

Hero (pain-point headline, rating badge, "Shop Thumb Fin — $20" + "Watch it in action", your existing hero photo) → trust strip → Three steps, no tools → **Pick your Thumb Fin** → Combo + contact paper → your Judge.me reviews → demo video with your existing cover image.

**Pick your Thumb Fin** has one card per version, set up as blocks in the *Thumb Fin shop* section:

| Card | Products |
| --- | --- |
| Original | The six colour products: `thumb-fin-black`, `-neon`, `-red`, `-sky-blue`, `-yellow`, `-pink`. Each swatch adds that colour's product |
| Low Profile | `low-profile-thumb-fin-black-thumb-rest` (its *Colors* variants) |
| Contoured Low Profile | `contoured-low-profile-thumb-fin-thumb-rest` (its *Color* variants) |

- **Add to cart** goes through Dawn's own `<product-form>`, so the "added to cart" pop-up appears just like on product pages. Sold-out colours are crossed out. Picking a colour updates the name, price and photo.
- **Swatch colours** are matched by name (Black, Neon, Red, Sky Blue, Yellow, Pink), from variant names or product titles. Add more under *Swatch colours* if you add a colour.
- **Cards have no descriptions yet.** Each version block has a *Description* field if you want to say how the shapes differ.
- **"Save $10"** is calculated from live prices: 3 × `thumb-fin-black`'s price − the combo price, shown with "vs $60 buying 3 separately".
- **Rating badge** (4.84 from 145 bassists) is text in the hero settings. It's store-wide, so update it there when the numbers change.
- **Video** loads only when the visitor clicks play.
- **CSS scoping:** every class starts with `tfr-` and every rule sits under `.tfr`, so none of this can affect the rest of the theme.

## Try it on an unpublished copy

**Option A: upload the zip (easiest)**
1. Get `thumbfin-theme-redesign.zip`, or build it with the command below.
2. Shopify admin → Online Store → Themes → **Add theme → Upload zip file**. It arrives as a new, **unpublished** theme. The live site is untouched.
3. Click **Preview** and go through the checklist below. All products are already filled in.

**Option B: Shopify's GitHub integration**
Online Store → Themes → Add theme → **Connect from GitHub** → this repo → branch `claude/shopify-theme-redesign-ywsffv`. The theme then stays in sync with every push.

Build the zip yourself with:

```sh
zip -r thumbfin-theme-redesign.zip assets blocks config layout locales sections snippets templates
```

## Before publishing

- [ ] Add each colour to the cart and confirm the popup and cart show the right colour. Also add the Combo and the contact paper.
- [ ] On a product page: check the note under Add to cart, and add the Combo and the paper from "Complete your setup".
- [ ] On the cart page: the add-ons show, disappear once added, and adding one updates the totals.
- [ ] Check that a sold-out colour is crossed out.
- [ ] Look at the header on the dark background. If the logo is hard to see, change *Header* and *Announcement bar* back to their old colour scheme ("Accent 2", your blue) in the editor, or upload a light version of the logo.
- [ ] Check the hero photo. It uses `IMG_0004.jpg`, the first slide of the old slideshow, cropped to fit. Swap it under the hero's *Image* if another photo crops better.
- [ ] Confirm the rating badge numbers (hero section settings).
- [ ] Click through the other pages in preview: a product, a collection, the cart, search, a blog post, the contact page and a standard page.
- [ ] **Judge.me on the product page** (review widget and star badge): if any text is dark-on-dark, go to Judge.me → Settings → Widget and set text to light, or pick its dark theme.
- [ ] **Withdrawal (Widerruf) form on standard pages** keeps its own white box. That's readable; restyle it in that app's block settings if you want it dark.
- [ ] **Checkout:** match it under Settings → Checkout → Customize (background `#241408`, accent `#c3ff5c`) if you want the new look to carry through.
- [ ] Check on a phone.
- [ ] **Publish.** Themes → the uploaded copy → Publish.

## Keep in mind

- **The zip is a snapshot of 25 Sep 2026.** Customizer changes made to the live theme after that export won't be in the copy. Settings you edit on the copy are saved in Shopify, not in this repo, unless you use the GitHub integration (Option B), which commits them back.
- A version product gets swatches when its one option is named *Color*, *Colour*, *Colors* or *Colours*. Any other option setup falls back to a dropdown.
- On a combo or paper product page, "Complete your setup" offers a single only if *Single Thumb Fin* is picked in the product-extras section. It's left empty because the single comes in three versions.

## Changes after the first preview

- **Header:** light scheme `scheme-thumbfin-light` (`#FFD59A`) so the black logo lettering reads; the announcement bar stays dark.
- **Announcement bar:** "Try all three versions: save $10 with the Combo 3 Pack" (links to the combo) and "No drilling. No adhesive. Moves between instruments."
- **Pick your Thumb Fin:** each version card has a description and a "Learn more" link that follows the selected colour; the Combo and contact paper cards have "Learn more" too.
- **Copy:** the three steps are Clean the surface / Press it on / Play, relaxed. Step 3 and the About Thumb Fin text avoid health claims ("less tendon strain", "joint health") that would need scientific substantiation.
- **Product pages:** colour swatches linking the Original's six per-colour products (`snippets/thumbfin-sibling-swatches.liquid`, navigation only, so reviews stay per product); Add to cart always in the primary style (`snippets/buy-buttons.liquid`); Judge.me stars under the title; phone-only sticky Add to cart bar (`snippets/thumbfin-sticky-atc.liquid`).
- **Judge.me:** `assets/thumbfin-apps.css` (loaded site-wide from `layout/theme.liquid`) forces dark text on the white review pop-ups and Reviews side tab.
- **Settings gotcha:** Dawn's radius settings only accept even numbers. An odd value makes Shopify drop the whole `config/settings_data.json` (no colours, default fonts).

## Store changes made outside the theme (Shopify admin, via the Shopify connector)

These live in Shopify, not in this repo. Recorded here with the previous values so they can be reverted.

**Product merge:** the Original is now one product, `thumb-fin-original` (Color variants), carrying the Judge.me reviews. The six old per-colour products (`thumb-fin-black`, `-neon`, `-red`, `-sky-blue`, `-yellow`, `-pink`) are **Draft; do not delete** (they hold the original reviews). Their URLs 301-redirect to the matching `thumb-fin-original?variant=…`.

**Product SEO (title / description):**

| Product | New SEO title | Previous SEO title |
| --- | --- | --- |
| thumb-fin-original | Thumb Fin Original – Suction-Cup Bass Thumb Rest | (none) |
| low-profile-thumb-fin-black-thumb-rest | Low Profile Bass Thumb Rest – 4mm Lower | Low Profile Thumb Fin \| Slimmer Thumb Rest |
| contoured-low-profile-thumb-fin-thumb-rest | Contoured Low Profile Bass Thumb Rest | Contoured Low Profile Thumb Fin \| Thumb Rest |
| combo-3-pack-one-of-each-version | Bass Thumb Rest 3 Pack – Try All Three Versions | Thumb Fin 3 Pack \| Try All Three Thumb Rests |
| contact-paper-for-matte-finish | Contact Paper for Matte-Finish Basses | (none) |

Previous SEO descriptions: Low Profile "Get a slimmer feel with the Low Profile Thumb Fin, about 4 mm lower than the original, with adjustable comfort for bass, guitar, ukulele, and more."; Contoured "Try a lower-profile thumb rest with a more concave side curve. Contoured Thumb Fin is about 4 mm lower than the original."; Combo "Try all three Thumb Fin versions in one bundle: original, low-profile, and contoured low-profile thumb rests for comfortable, adjustable playing."; Original and contact paper had none.

**Collection:** `bass-thumb-rests` ("Bass Thumb Rests", manual, 4 products, intro description; SEO title "No-Drill Bass Thumb Rests – Suction-Cup Mount"). Added to the main menu between Home and Catalog.

**Homepage (Online Store → Preferences, set by the owner):** new title/description and a social sharing image.

**Product names and category (renamed via the connector; URLs/handles unchanged):**

| Handle | New title | Previous title |
| --- | --- | --- |
| thumb-fin-original | Thumb Fin Original – Bass Thumb Rest | Thumb Fin Original |
| low-profile-thumb-fin-black-thumb-rest | Thumb Fin Low Profile – Bass Thumb Rest | LOW PROFILE Thumb Fin  Thumb Rest |
| contoured-low-profile-thumb-fin-thumb-rest | Thumb Fin Contoured Low Profile – Bass Thumb Rest | CONTOURED LOW PROFILE Thumb Fin  Thumb Rest |
| combo-3-pack-one-of-each-version | Thumb Fin Combo 3 Pack – One of Each Version | Combo 3 Pack - One of Each version |
| contact-paper-for-matte-finish | Thumb Fin Contact Paper for Matte Finishes | Contact Paper For Matte Finish |

All five use the category *String Instrument Accessories > Guitar Accessories > Guitar Fittings & Parts* (the contact paper was previously *Guitar Slides*).


**Discount codes:** `NEWSITE10` and `THANKYOU10` (10%, all customers, 27–29 Sep 2026, for the two campaign emails); `WELCOME10` (10%, one use per customer, no end date, combines only with shipping discounts) for the signup popup.

## Email signup popup and emails

- **Popup:** `sections/thumbfin-signup-popup.liquid`, in the footer group so it loads on every page (styles and the `thumbfin-signup` element are in `assets/thumbfin.css` / `assets/thumbfin.js`). It uses Shopify's customer form tagged `newsletter,signup-popup`, so signups join the Shopify Email list. It opens after 10 s or on desktop exit intent, stays hidden for 14 days after closing and for good after signing up, and is skipped on the cart and account pages and for subscribed customers. After submitting, the page reloads and the popup shows the code. Switch it on or edit it in the theme editor (footer → *Thumb Fin signup popup* → *Show popup to visitors*). Add `?signup-preview` to any URL to see it while it's off.
- **Emails:** `emails/build.py` generates the Shopify Email custom-HTML files: `email-1-non-buyers.html` (NEWSITE10), `email-2-past-buyers.html` (THANKYOU10) and `email-3-welcome.html` (WELCOME10, for the welcome automation). Shopify Email needs `{{ open_tracking_block }}` and `{{ unsubscribe_link }}` (which renders a whole link, so it isn't wrapped in `<a>`), and `&` in URLs written as `&amp;`.
