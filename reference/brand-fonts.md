# Brand fonts — Braze CDN (production)

These are the production font assets uploaded to Braze. Use these URLs in any HTML in-app message, Content Block, or custom HTML email template.

## Review (body typeface)

| Weight  | font-weight | URL |
|---------|-------------|-----|
| Regular | 400         | `https://braze-images.com/appboy/communication/assets/font_assets/files/69f167a116c74d00887c750f/original.otf?1777428385` |
| Bold    | 700         | `https://braze-images.com/appboy/communication/assets/font_assets/files/69f167a028ccd700880080e7/original.otf?1777428384` |

## Review Wide (display typeface)

| Weight | font-weight | URL |
|--------|-------------|-----|
| Black  | 900         | `https://braze-images.com/appboy/communication/assets/font_assets/files/69f167a024a17e008a3616f1/original.otf?1777428383` |

## Usage

```css
@font-face {
  font-family: 'Review';
  src: url('...regular URL...') format('opentype');
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: 'Review';
  src: url('...bold URL...') format('opentype');
  font-weight: 700;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: 'Review Wide';
  src: url('...wide-black URL...') format('opentype');
  font-weight: 900;
  font-style: normal;
  font-display: swap;
}
```

Assign via CSS variables:
- `--font-body: 'Review', system-ui, sans-serif;`
- `--font-display: 'Review Wide', 'Review', system-ui, sans-serif;`
