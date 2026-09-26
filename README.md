# Thumb Fin — Shopify theme (homepage redesign)

This repo is the thumbfin.com theme (**Dawn 12.0.0**, live "Thumb Fin" theme exported 25 Sep 2026) with the homepage redesign from `docs/thumbfin-redesign.html` built in. The original brief is in `docs/thumbfin-redesign-notes.md`.

The baseline commits hold the unmodified export, so `git diff` against it shows exactly what the redesign changed:

| File | Change |
| --- | --- |
| `sections/thumbfin-home.liquid` | **New.** The redesigned homepage as one section |
| `templates/index.json` | New section added at the top. The sections it replaces are **hidden, not deleted**: the "Experience Playing Like Never Before" rich text, the Judge.me carousel section (moved into the new section), the "Not sure which one?" Combo text, the featured Combo product and the video. The photo banner, Instagram heading + Instafeed, featured products, About and blog stay. Featured products, About and blog switched to the new dark colour scheme |
| `config/settings_data.json` | Adds one colour scheme, **"scheme-thumbfin"** (walnut `#241408` background, cream `#f4ecdd` text, neon `#c3ff5c` buttons). Existing schemes are untouched |
| `sections/header-group.json`, `sections/footer-group.json` | Announcement bar, header, menu and footer switched to the new scheme |

## What the section does

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
3. On that theme, click **Customize** → Home page → **Thumb Fin homepage** section → **Single Thumb Fin** → pick your $20 single product. This is the one setting I couldn't fill in: the export doesn't include its product handle. The Combo is already set, and the contact paper is found by its handle `contact-paper-for-matte-finish`. If the paper card doesn't show, pick it under **Add-on (contact paper)**.
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
- [ ] Check that a sold-out colour is crossed out.
- [ ] Look at the header on the dark background. If the logo is hard to see, change *Header* and *Announcement bar* back to their old colour scheme ("Accent 2", your blue) in the editor, or upload a light version of the logo.
- [ ] Check the hero photo. It uses `IMG_0004.jpg`, the first slide of the old slideshow, cropped to fit. Swap it under *Hero image* if another photo crops better.
- [ ] Confirm the rating badge. If it shows the fallback 4.84 / 145, Judge.me isn't syncing to Shopify's review metafields. Either turn that on in Judge.me's settings or keep the text settings up to date.
- [ ] Look at the Instagram block. The heading and Instafeed widget were left on your white scheme so they stay together as one band. If you'd rather have it dark, set the heading's colour scheme to "scheme-thumbfin"; Instafeed's own colours are set in the Instafeed app.
- [ ] Check on a phone.
- [ ] **Publish.** Themes → the uploaded copy → Publish.

## Keep in mind

- **The zip is a snapshot of 25 Sep 2026.** Customizer changes made to the live theme after that export won't be in the copy. Settings you edit on the copy are saved in Shopify, not in this repo, unless you use the GitHub integration (Option B), which commits them back.
- The swatch picker is used when the single product has one option named *Color* or *Colour*. Any other option setup falls back to a dropdown.
