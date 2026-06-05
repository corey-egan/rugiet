# In-App Message Patterns

Reference for agents building Braze HTML in-app messages. Describes the available template types, when to use each, and the structural conventions that keep templates reusable and campaign outputs clean.

---

## Template library location

Reusable IAM templates live in `braze/iam/`. These are generic scaffolding — placeholder copy, placeholder images, no product-specific content. Campaign-specific versions go to `outputs/creative/`.

## Available templates

### 1. Carousel (`carousel.html`)

Multi-slide modal with left image / right content panels (desktop) that stack vertically on mobile. Uses the Siema library hosted on Braze's CDN for slide transitions.

**When to use:**
- Onboarding or education sequences (multiple messages in one surface)
- Product lineup showcases (slide per product)
- Multi-step value props before a hard CTA on the final slide

**Structure:**
- 2–4 slides, each with an image panel and a content panel
- Carousel dots + prev/next chevrons below the slides
- Each slide has its own eyebrow, headline, subtitle, body, and CTA pair

**JS bridge:** `appboyBridge` (legacy; works in current SDKs)

### 2. Single-panel (`single-panel.html`)

Stacked hero-image-over-content layout. One screen, no slides.

**When to use:**
- Product announcements and upgrades
- Upsell / cross-sell offers
- Single-message promotions with a clear primary CTA
- Any IAM where the message fits in one screen without scrolling

**Structure:**
- Hero image panel (top ~62%) with:
  - Full-bleed lifestyle or product image
  - 10deg gradient overlay (black → transparent) for headline legibility
  - Display headline (Review Wide Black, white, uppercase)
  - Optional circular product shot (bottom-right, 114px)
  - Close X (top-right, white)
- Content panel (bottom ~38%) with:
  - Body copy (Review Regular, 19px)
  - Optional offer/value-prop line with 1px divider above it
  - CTA row: primary (orange filled) + secondary (ghost text)

**JS bridge:** `brazeBridge` (current standard)

---

## Shared conventions across all IAM templates

### Fonts
Five brand font faces are registered. Four have production Braze CDN URLs hardcoded in all templates; Redward Mono still has a `REPLACE_*` placeholder (upload when an eyebrow/caption is needed).

| Font | Weight / Style | Braze CDN URL | Role |
|---|---|---|---|
| Review Regular | 400 normal | `https://braze-images.com/appboy/communication/assets/font_assets/files/69f167a116c74d00887c750f/original.otf?1777428385` | Body copy, editorial text |
| Review Regular Italic | 400 italic | `https://braze-images.com/appboy/communication/assets/font_assets/files/69f167a0df9d180088c42cba/original.otf?1777428383` | Emphasis, disclaimers |
| Review Bold | 700 normal | `https://braze-images.com/appboy/communication/assets/font_assets/files/69f167a028ccd700880080e7/original.otf?1777428384` | Subtitles, emphasis, button labels |
| Review Wide Black | 900 normal | `https://braze-images.com/appboy/communication/assets/font_assets/files/69f167a024a17e008a3616f1/original.otf?1777428383` | Display headlines (uppercase) |
| Redward Mono Regular | 400 normal | `https://braze-images.com/appboy/communication/assets/font_assets/files/69f167a0c08e29008ad72571/original.otf?1777428383` | Eyebrows, captions (uppercase) |
| Redward Mono Light | 300 normal | `https://braze-images.com/appboy/communication/assets/font_assets/files/69f167a093c3c90088050a48/original.otf?1777428383` | Light-weight captions, fine print |

### Colors
Black ink on white/cream backgrounds. Orange (`#FFA202`) is the single accent color. Product-specific colors only appear on product surfaces (image panels, not UI chrome).

### Buttons
Sharp corners (`border-radius: 0`) on all buttons. Primary CTA is solid orange with black text. Secondary CTA is either outline-black (carousel) or ghost-gray text (single-panel). Hover/press uses opacity shifts only (0.88 / 0.78).

### Interaction model
- Primary CTA: `brazeBridge.logClick('0')` (or `appboyBridge` in older templates)
- Secondary CTA: `brazeBridge.logClick('1')`
- Close: `brazeBridge.closeMessage()`
- The secondary CTA typically also fires `closeMessage()` after logging the click

### Responsive breakpoints
- Desktop: full template width (900px carousel, 495px single-panel)
- Mobile portrait: 330px max-width
- Mobile landscape: 660px (carousel only)

### Image handling
All image `src` values use `REPLACE_*` placeholders. Upload final assets to Braze Media Library and swap in the CDN URLs before deployment. Local `./assets/` paths exist for design preview only.

---

## Agent workflow: producing an IAM from a brief

1. **Identify the template.** Read the brief to determine which template type fits. Single message → `single-panel.html`. Multi-step story → `carousel.html`.
2. **Fork the template.** Copy the chosen template from `braze/iam/` into the campaign output folder under `outputs/creative/{date}_{brief-name}/iam.html`.
3. **Write the copy.** Replace placeholder text with campaign-specific copy. Load `rugiet-copywriting` skill and run the compliance checklist.
4. **Note image requirements.** Specify which images need to be uploaded. Do not embed base64 images — use `REPLACE_*` placeholders and document the swap in `notes.md`.
5. **Write notes.md.** Document copy decisions, compliance flags, deployment checklist items, and anything that needs human review.
6. **Never modify the template in `braze/iam/`.** Templates are reusable infrastructure. Campaign-specific changes belong in `outputs/creative/` only.

---

## Adding a new template type

If a brief calls for a layout that doesn't match carousel or single-panel:

1. Create a new self-contained HTML file in `braze/iam/`.
2. Use generic placeholder copy — no product names, no campaign-specific content.
3. Follow the font/color/button/interaction conventions above.
4. Update `braze/iam/README.md` with the new file.
5. Add a section to this document describing the template and when to use it.
