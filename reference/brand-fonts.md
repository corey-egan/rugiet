# Brand fonts — Braze CDN (production)

These are the production font assets uploaded to Braze. Use these URLs in any HTML in-app message, Content Block, or custom HTML email template.

Local font files for preview live in `braze/iam/fonts/`. The canonical `@font-face` block with all production URLs is in `braze/iam/tokens.css`.

## Review (body typeface — Pangram Pangram, licensed)

| Weight         | font-weight | Braze CDN URL |
|----------------|-------------|---------------|
| Regular        | 400         | `https://braze-images.com/appboy/communication/assets/font_assets/files/69f167a116c74d00887c750f/original.otf?1777428385` |
| Regular Italic | 400 italic  | `https://braze-images.com/appboy/communication/assets/font_assets/files/69f167a0df9d180088c42cba/original.otf?1777428383` |
| Bold           | 700         | `https://braze-images.com/appboy/communication/assets/font_assets/files/69f167a028ccd700880080e7/original.otf?1777428384` |

## Review Wide (display typeface)

| Weight | font-weight | Braze CDN URL |
|--------|-------------|---------------|
| Black  | 900         | `https://braze-images.com/appboy/communication/assets/font_assets/files/69f167a024a17e008a3616f1/original.otf?1777428383` |

## Redward Mono (eyebrow / caption typeface)

| Weight  | font-weight | Braze CDN URL |
|---------|-------------|---------------|
| Regular | 400         | `https://braze-images.com/appboy/communication/assets/font_assets/files/69f167a0c08e29008ad72571/original.otf?1777428383` |
| Light   | 300         | `https://braze-images.com/appboy/communication/assets/font_assets/files/69f167a093c3c90088050a48/original.otf?1777428383` |

## CSS variable mapping

```css
--rugiet-font-display: 'Review Wide', 'Archivo Black', 'Arial Black', system-ui, sans-serif;
--rugiet-font-text:    'Review', 'Inter', system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
--rugiet-font-mono:    'Redward Mono', 'JetBrains Mono', ui-monospace, monospace;
```

## Licensing

Pangram Pangram fonts are licensed. Keep font assets inside Rugiet's Braze account; do not redistribute.
