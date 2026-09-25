# Thumb Fin — Homepage Redesign: Handoff Notes

## Context
Site: https://thumbfin.com/ (Shopify store)
Product: Thumb Fin — a suction-cup ergonomic thumb rest for bass/guitar, no instrument modification required. $20 single unit, $50 combo 3-pack (one of each color), $2 matte-finish contact paper add-on. 6 colors: Black, Neon, Red, Sky Blue, Yellow, Pink. 4.84★ from 145 reviews. Patented design.

## Problem with the current homepage
- Hero leads with generic feature list ("Ergonomic. Adjustable. Universal.") instead of the actual pain point (drilling into an expensive instrument, thumb/tendon fatigue).
- Star rating and review count are buried at the bottom of the page instead of near the hero.
- Homepage jumps straight to the $50 Combo 3-Pack before explaining what the product is or showing the $20 single unit.
- Demo video is placed after the product block instead of near the top.
- No bundle savings messaging ("$50 vs $60 buying separately" is never stated).
- No cross-sell of the $2 contact paper alongside the main product.
- Visual design is an untouched default Shopify theme look — flat black/white, doesn't reflect the product's bold color range or the "instrument hardware" subject matter.

## Design direction used in the mockup
- **Palette**: deep walnut/mahogany background (`#241408`, `#2f1c0e` panels), parchment/cream text (`#f4ecdd`), brass hardware accent (`#cf9d3e`), neon lime CTA accent (`#c3ff5c`) — echoes the product's own neon color option and amp/instrument-hardware materials rather than a generic SaaS palette.
- **Type**: Oswald (condensed, headline/display) + Work Sans (body).
- **Motif**: a simple suction-disc + fin shape (CSS-drawn) stands in for product photography — replace with real photos/video in production.
- **Structure**: sticky nav → hero (pain-point headline + rating badge + dual CTA) → trust ticker strip → 3-step "how it works" (Press / Place / Play) → product spotlight (single $20 unit with color swatches) → bundle row (Combo 3-Pack with "Save $10" tag + $2 contact paper cross-sell) → testimonial strip (paraphrased reviews) → video CTA band → footer.

## Deliverable
The finished static mockup is `thumbfin-redesign.html` (in this same folder / uploads). It's a **self-contained, static HTML/CSS file** — no JS framework, no Shopify Liquid, no live cart or product data. Published preview: https://claude.ai/artifact/5pj7BWuBGPuenoFaB8crMw

## What's needed from here (the actual Claude Code task)
1. **Duplicate the live Shopify theme** first (Online Store > Themes > "..." > Duplicate) so this can be tested safely before publishing.
2. **Convert the static mockup into a Shopify section** (e.g. `sections/custom-hero-redesign.liquid`):
   - Keep the CSS as-is (namespaced/scoped so it doesn't collide with the existing theme's classes).
   - Strip the outer `<html>`, `<head>`, `<body>` tags — only the inner content + a `<style>` block belong in the section file.
3. **Replace static placeholders with real Shopify Liquid bindings**:
   - Price → `{{ product.price | money }}`
   - Color swatches → loop over `product.variants` (or a linked metafield/option) instead of the hardcoded circles
   - Add to Cart → wrap in `{% form 'product', product %}...{% endform %}` with a real `line_item_properties`/variant ID so it actually adds to cart
   - Bundle / combo product and the $2 contact paper cross-sell → pull real product handles from the store (`combo-3-pack-one-of-each-version`, `contact-paper-for-matte-finish`)
   - Testimonial quotes → either hardcode from real reviews (get owner's permission on exact wording) or pull from the store's installed review app if it exposes Liquid objects/snippets
   - Video section → swap the CSS placeholder for the real YouTube embed (existing video: https://www.youtube.com/watch?v=Y_QRGtpZdyI)
4. **Add the new section to the homepage** via `templates/index.json` or the theme customizer, positioned at the top in place of (or above) the existing hero.
5. **Test**: verify Add to Cart works for each variant/color, confirm mobile responsiveness, confirm existing theme styles don't leak into/conflict with the new section's CSS.
6. **Publish** the duplicate theme once verified.

## Notes / open questions for the store owner
- Confirm real review quotes/attribution before using them live (the mockup's testimonials are paraphrased placeholders, not verbatim copy).
- Confirm which Shopify apps (if any) power reviews/UGC currently, since that affects how to pull real review data into the new section.
- Decide whether "Save $10" bundle messaging should be dynamic (calculated from live prices) or hardcoded — dynamic is safer if prices ever change.
