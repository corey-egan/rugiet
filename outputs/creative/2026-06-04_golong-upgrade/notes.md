# Go Long Upgrade — IAM

**Date:** 2026-06-04
**Template used:** `braze/iam/single-panel.html`
**Source design:** Figma Website file, node `6025:1587`
**Channel:** In-app message (Custom Code)

## What this is

A single-panel modal upsell for existing Go Long subscribers, promoting an upgraded formulation. Stacked layout: lifestyle hero image with gradient overlay, headline over the image, circular product shot bottom-right, then body copy + offer line + dual CTA below.

## Copy decisions

- **Headline:** "We made Go Long better" — product announcement register, not promotional. Matches the Figma source.
- **Body:** Three short declarative lines ("Faster absorption. Stronger formula. Better results.") — benefit-forward without making specific clinical claims.
- **Offer line:** "Upgrade and save XX%." — placeholder percentage; needs real value before deployment.
- **Primary CTA:** "Upgrade Me" — direct, assumes the sale.
- **Secondary CTA:** "Skip For Now" — low-pressure dismiss, implies future opportunity.

## Compliance notes

- No guaranteed outcomes language. "Better results" is vague-positive, not a clinical claim.
- No name-brand drug comparisons.
- Go Long headline does not lead with ED (per product rule in CLAUDE.md).
- Compounding disclaimer not included in IAM — confirm whether the upgrade changes the compounding status; if so, add disclaimer to body copy.

## Deployment checklist

See the HTML comment header in `iam.html` for the full checklist. Key items:

1. Upload brand fonts to Braze (if not already done from carousel deployment)
2. Upload hero lifestyle image and Go Long product shot → swap `REPLACE_HERO_IMAGE` and `REPLACE_PRODUCT_IMAGE`
3. Replace `href="#"` on both CTAs with destination URLs / deep links
4. Fill in the real savings percentage (replace `XX%`)
5. Paste into Braze Dashboard → In-App Message → Custom Code

## Flags for human review

- [ ] Savings percentage needs a real value
- [ ] Hero image needs to be selected and uploaded
- [ ] Product shot needs the updated Go Long packaging (confirm with design)
- [ ] CTA destination URLs need to be set
- [ ] Confirm compounding disclaimer requirement for the upgraded formulation
