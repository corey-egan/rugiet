# Rugiet — Braze In-App Message templates

Reusable template scaffolding for in-app messages delivered via Braze,
styled to the Rugiet brand. Each template is a single self-contained
HTML file because Braze inlines the message contents into the host app's
webview; external stylesheet links are not reliable.

**These are generic templates, not campaign outputs.** Campaign-specific
IAMs (with real copy, real product names, real offer lines) belong in
`outputs/creative/` — see the design-system skill's
`references/in-app-patterns.md` for the full workflow.

## Files

| Path | Role |
|---|---|
| `carousel.html` | Multi-slide carousel modal (Siema + `appboyBridge`). Suited for onboarding, education, and product lineup showcases. |
| `single-panel.html` | Stacked hero-image-over-content modal (`brazeBridge`). Suited for product announcements, upsells, and single-message promotions. Derived from Figma Website file, node `6025:1587`. |
| `side-by-side.html` | Image-left / content-right on desktop (≥ 680px), stacking vertically on mobile (`brazeBridge`). Suited for email capture, seasonal promos, and campaigns where a hero lifestyle image should sit alongside the copy. Includes inline form with email validation. |
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

## Deploying a template to Braze

The deployment flow is the same for all templates:

1. **Fonts are done.** All seven font faces (Review Regular, Regular
   Italic, Bold, Wide Black; Redward Mono Regular, Light) are uploaded
   to Braze with production CDN URLs hardcoded in every template. No
   font placeholders remain.
3. **Upload campaign images** to Braze and swap the `REPLACE_*` image
   placeholders with the hosted CDN URLs.
4. **Replace every `href="#"`** on the CTAs with the destination URL
   or deep link (`https://rugiet.com/…` or `rugiet://…`).
5. **Edit all copy** — headlines, body, button labels, offer lines —
   for the actual campaign. Keep voice and compliance language tight.
6. **Paste the final HTML** into the Braze Dashboard IAM message
   composer → Custom Code.

Click tracking uses `brazeBridge.logClick('0')` (primary) and
`brazeBridge.logClick('1')` (secondary). Closing uses
`brazeBridge.closeMessage()`. The carousel template uses the legacy
`appboyBridge` alias — both work in current Braze SDKs.

## Adding a new IAM template

1. Start a new self-contained HTML file in `braze/iam/`.
2. Copy the `<style>` block from an existing template or paste the
   relevant sections from `tokens.css` — `:root` tokens, `@font-face`
   declarations, and the button primitives are usually enough to
   bootstrap a new layout.
3. Use generic placeholder copy. No product names, no campaign-specific
   content.
4. Reuse the `REPLACE_*` font URL pattern so the deployment swap is
   consistent across templates.
5. Update this README's table with the new file.
6. Add a section to `.claude/skills/rugiet-design-system/references/in-app-patterns.md`
   describing the template and when to use it.

## Caveats

- The bundled product PNGs were downscaled from the design system
  originals (originally 2–5 MB each) to keep the repo small. Use the
  full-resolution files from the Rugiet design system for any real
  marketing surface.
- Pangram Pangram fonts are licensed — keep the font assets inside
  Rugiet's Braze account; do not redistribute.
