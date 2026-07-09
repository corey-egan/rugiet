# Go Long — 15% off email capture modal

**Created:** 2026-06-18
**Surface:** In-app message (Braze Custom Code HTML)
**Placement:** Go Long landing pages / PDP
**Template type:** Single-column email capture modal (new layout — not derived from existing templates)

---

## Copy decisions

- **Eyebrow:** "Go Long — sexual health" in Redward Mono, using the Go Long product accent color (`#6C8A6A`). Gives product + category context without burning headline space.
- **Discount headline:** "15% off" in Review Wide Black at 56px — largest element on the modal, designed to stop the scroll. Paired with "Your first order" as a secondary headline to set the offer scope.
- **Sub copy:** Leads with the PE benefit ("last longer") per Go Long positioning rules. "Perform with confidence" as the secondary framing. No mention of ED in the headline or hero. Uses conditional language ("formulated to help").
- **CTA:** "Get 15% off" — active, specific, tells the visitor exactly what they get. No "Learn more" or "Click here."
- **Dismiss:** "No thanks" as a low-friction secondary option that still logs a click event for analytics.

## Compliance checklist

- [x] Conditional verbs on benefit claims — "formulated to help"
- [x] No absolute or guaranteed language
- [x] No "ED" in headline, subject line, or hero copy (Go Long rule)
- [x] PE is the marquee benefit — "last longer" leads
- [x] No exclamation points
- [x] Sentence case throughout (eyebrow is uppercase per Redward Mono convention)
- [x] "Go Long" has no registered trademark — no symbol needed
- [x] No puns, wordplay, or idiomatic expressions
- [x] Discount terms disclosed in legal footer ("first Go Long order only")
- [x] Privacy and terms links included

## Self-check (owned-channels.md)

- [x] Channel match — in-app modal on owned landing page, warm/intent audience
- [x] Voice match — direct, confident, no cleverness or humor tactics
- [x] Format match — sentence case, no exclamation, single CTA action
- [x] Product positioning — PE-first for Go Long, ED nowhere in sight
- [x] Customer mindset — aspirational framing ("perform with confidence"), not deficiency

## Design notes

- **Layout:** Single column, centered. No hero image — the discount itself is the visual anchor. Clean, focused, fast to scan.
- **Accent bar:** 6px Go Long green (`#6C8A6A`) at the top ties the modal to the product without needing a product image.
- **Divider:** 40px green rule between headline and sub copy creates visual hierarchy without adding weight.
- **Form:** Email input with cream background (`#FFFCF9`), focus state uses the Go Long green border. Black CTA button (not orange) — keeps the modal clean and lets the discount headline remain the dominant color moment.
- **Typography hierarchy:** Discount (56px Review Wide Black) → secondary headline (22px Review Wide Black) → body (15px Review Regular) → CTA (13px Review Bold uppercase)
- **No images required** — this template is entirely typographic, which means zero image upload dependencies for deployment.

## Braze deployment

1. Paste the HTML into Braze Dashboard → In-App Message → Custom Code.
2. Set the campaign trigger to fire on the Go Long PDP/landing page.
3. **Custom attribute on submit:** `golong_15_email_capture` = `true` — use this for the follow-up email segment.
4. **Click tracking:**
   - Button 0 (primary): email submit
   - Button 1 (secondary): dismiss / "No thanks"
   - Close X: `closeMessage()` only (no click logged)
5. Frequency cap recommendation: once per user, with a 30-day re-eligibility window for users who dismissed without submitting.
6. No image uploads needed — template is fully self-contained.

## Braze bridge

Uses `brazeBridge` with `appboyBridge` fallback (`var bridge = window.brazeBridge || window.appboyBridge`).

## Open questions

- [ ] Confirm 15% discount code or whether Braze should auto-apply via URL parameter on the follow-up email CTA.
- [ ] Confirm whether the custom attribute name `golong_15_email_capture` aligns with existing Braze naming conventions.
- [ ] Determine follow-up email timing — immediate welcome with code, or drip sequence?
