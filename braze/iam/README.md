# Rugiet — Braze In-App Message templates

Templates for in-app messages delivered via Braze, styled to the Rugiet
brand. Each template is a single self-contained HTML file because Braze
inlines the message contents into the host app's webview; external
stylesheet links are not reliable.

## Files

| Path | Role |
|---|---|
| `carousel.html` | Three-slide carousel modal (preserves Braze's Siema + `appboyBridge` integration). The first template in this folder, rebranded against the Rugiet design system. |
| `tokens.css` | Brand tokens (colors, type roles, button + pill primitives). **Not loaded by templates** — it is a copy-from-here reference for designers building new IAMs. |
| `fonts/` | Rugiet brand webfonts (Pangram Pangram: Review, Review Wide Black, Redward Mono). Committed for local preview; production deployment needs each `.otf` uploaded to Braze's Media Library so every template can reference the Braze-hosted URL. |
| `assets/logo/logomark.svg` | The Rugiet logomark (single SVG, paints with `currentColor`). |
| `assets/products/*.webp` | Compressed product render placeholders used by `carousel.html`. Real campaign assets get uploaded to Braze and swapped in by URL. |

## Brand foundations (short version)

The full design system is the Rugiet handoff at
`https://api.anthropic.com/v1/design/h/T02dC9U85lCuEhqO5GDQVA`. The
pieces an IAM typically uses:

- **Color** — black ink on warm cream (`#FFFCF9`), orange (`#FFA202`)
  as the single accent. Product accent colors live on SKU surfaces
  only.
- **Type** — Review Wide Black for display headlines (UPPERCASE, line
  height 0.9, tracking −2%); Review for editorial body and bold
  emphasis; Redward Mono for eyebrows and captions (UPPERCASE, tracking
  +6%).
- **Buttons** — sharp corners (`border-radius: 0`). Pills are the only
  place fully rounded radii appear. Primary CTA is solid orange on
  black text; secondary CTA is outline black on cream.
- **Hover / press** — opacity shifts only (0.88 / 0.78). No transforms,
  no shadows, no gradients on UI.
- **Voice** — performance medicine, not wellness. Direct, confident,
  serious. Compliance language: "designed to support", "may help",
  "as fast as 15 minutes for many men". Never name-brand drug
  comparisons; never "treats psychological ED"; never "guaranteed".

`tokens.css` is the single-page condensed version of all of the above
that designers can scan or paste into a new template.

## Deploying `carousel.html` to Braze

1. **Upload the brand fonts to Braze** (Settings → Media Library →
   Font Assets). Upload these four files from `./fonts/`:
   - `Review-Regular-Web.woff2` (or `Review-Regular.otf`)
   - `Review-Bold.otf`
   - `ReviewWide-Black.otf`
   - `Redward-Mono-Regular.woff2` (or `Redward-Mono-Regular.otf`)
2. **Replace the four `REPLACE_*` placeholders** in `carousel.html`'s
   `@font-face` blocks with the `appboy-images.com/.../original.*`
   URLs Braze assigns. The local `./fonts/…` fallbacks can stay (Braze
   won't serve them; they are only used during local preview), or you
   can strip them to keep the template lean.
3. **Upload each slide image** to Braze and swap the
   `./assets/products/*.webp` paths with the hosted CDN URLs.
4. **Replace every `href="#"`** on the CTAs with the destination URL
   or deep link (`https://rugiet.com/…` or `rugiet://…`).
5. **Edit slide copy** — eyebrows, headlines, body, and button labels
   for the actual campaign. Keep voice and compliance language tight.
6. **Paste the final HTML** into the Braze Dashboard IAM message
   composer.

The template logs clicks through `appboyBridge.logClick('0' | '1')`
(primary = `'0'`, secondary = `'1'`) and closes through
`appboyBridge.closeMessage()`, matching the Braze convention for
multi-CTA carousel modals.

## Adding a new IAM template

1. Start a new self-contained HTML file in `braze/iam/`.
2. Copy the `<style>` block from `carousel.html` or paste the relevant
   sections from `tokens.css` — `:root` tokens, `@font-face`
   declarations, and the button / pill primitives are usually enough
   to bootstrap a new layout.
3. Reuse the four `appboy-images.com/REPLACE_*` font URL pattern so
   the deployment swap is consistent across templates.
4. Update this README's table with the new file.

## Caveats

- The bundled product PNGs were downscaled from the design system
  originals (originally 2–5 MB each) to keep the repo small. Use the
  full-resolution files from the Rugiet design system for any real
  marketing surface.
- Pangram Pangram fonts are licensed — keep the font assets inside
  Rugiet's Braze account; do not redistribute.
