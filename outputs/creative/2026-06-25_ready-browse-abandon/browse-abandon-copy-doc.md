# Rugiet Ready Browse Abandon — Brief + Copy Doc

**Date:** 2026-06-25
**Owner:** Lifecycle
**Status:** Draft — ready for design handoff
**Strategy source:** [Browse Abandon Flow Analysis](../../strategy/flow_audits/06-13-26/ready-browse-abandon-flow-analysis.md)
**Design system:** [2026 Q2 LCM Emailify Campaigns — Design System Components](https://www.figma.com/design/P8jY5nWxLQRaUSxcUTxx0m/2026-Q2-LCM-Emailify-Campaigns?node-id=237-22442)
**Channel:** Email (lifecycle flow)

---

## Brief

### Audience

Browse abandoners — subscribers who viewed the Rugiet Ready product page and left without starting an intake, adding to cart, or creating an account. This is the lowest-intent audience in the lifecycle. They expressed interest by visiting; they did not express purchase intent.

### Objective

Convert browse abandoners to intake starts through a trust-first, education-led 4-email sequence. Discount appears only in the final email with a hard expiry.

### Flow structure

| Position | Timing | Job | Discount |
|---|---|---|---|
| 1 | Hours after browse | Intent hook + product hero | No |
| 2 | Day 1 | Quiz / micro-commitment (Sex Score) | No |
| 3 | Day 3 | Doctor trust (Dr. Sanchez) | No |
| 4 | Day 5-7 | Mechanism + offer with expiry | Yes (RUGIET10, 10%) |

### Key constraints from strategy

- No cart/checkout language — these people never carted
- No discount until email 4
- One CTA per email
- Subject lines six words or fewer
- No puns or idiomatic expressions
- Imagery unique per email — no repeated couple shots across the flow
- Standalone "Ready" uses ™ on first mention only (never ®)
- "Rugiet Ready" uses ® on first mention only
- Onset language: "works in as little as 15 minutes" — never "get hard in 15 minutes"
- FDA compounding disclaimer in every footer

### Design system notes for the designer

All module references below use the component names from the [Figma design system](https://www.figma.com/design/P8jY5nWxLQRaUSxcUTxx0m/2026-Q2-LCM-Emailify-Campaigns?node-id=237-22442). Typography, color, padding, and button styles should be pulled directly from the design system components.

**Global email structure for all 4 emails:**
- Logo: `Logo_Only_Centered_Dark` or `Wordmark_Only_Center_Dark`
- Footer: `Footer_Dark` (includes `Footer_Header`, `Footer_Categories`, `Footer_Partners`, `Footer_Links`, `Footer_Social_Light`)
- FDA compounding disclaimer in footer using `Disclaimer1` or `Disclaimer2`
- Padding between modules: `Padding40` or `Padding60`
- Body text: `B1_Regular` or `B2_Regular`
- Horizontal rules: Full-width (560px) between major sections, Inset (520px) within sections

---

## Email 1: Intent hook

**Timing:** Hours after browse
**Job:** Acknowledge the browse, introduce the product, plant the seed

### Module layout

| Order | Module | Component reference |
|---|---|---|
| 1 | Logo | `Wordmark_Only_Center_Dark` |
| 2 | Hero | `Hero_TWI_Style_1_1x1.4` — product hero image above, headline below |
| 3 | Description | `Description_Copy_B2_Large_Center` |
| 4 | Listicle | `Listicle_Small_1` x3 — three benefit points with icons |
| 5 | Stats | `Stats_Small_TO_1` — social proof stat |
| 6 | Button | `Button_Style_1_Center` |
| 7 | Disclaimer | `Disclaimer2` — FDA compounding disclaimer |
| 8 | Footer | `Footer_Dark` |

### Copy

```
S: You checked out Ready for a reason

Prev: Three medications. One sublingual dose. Here's what caught your eye.
```

**Hero image direction:** Product hero — the Ready pill on black background or the "Three medications. One little dose." treatment. No couple imagery.

**Headline** `H2`
Three medications. One dose. Works in as little as 15 minutes.*

**Body** `B2_Regular` / `Description_Copy_B2_Large_Center`
You looked at Ready™ for a reason. Most men do. Three active ingredients — sildenafil, tadalafil, and apomorphine — combined in one sublingual dose, personalized by a licensed physician to your health profile.

**Listicle** `Listicle_Small_1` — three items, each with an icon from the design system:
- `15Min` icon — Works in as little as 15 minutes*
- `Compound` icon — Three active ingredients in one dose
- `MedicalTrack` icon — Prescribed by a licensed physician

**Stats** `Stats_Small_TO_1`
500,000+ men trust Ready™

**CTA** `Button_Style_1_Center`
Get started

**Disclaimer** `Disclaimer2`
*On average, after medication dissolves. Based on an internal survey of Rugiet Ready customers. Customer results have not been independently verified. Individual results may vary.

Compounded drugs may be prescribed under federal law but are not FDA-approved and do not undergo FDA safety, effectiveness, or manufacturing review.

---

## Email 2: Sex Score quiz

**Timing:** Day 1
**Job:** Micro-commitment — get the subscriber to take an action that isn't a purchase. The Sex Score quiz warms them into the funnel without asking for money.

### Module layout

| Order | Module | Component reference |
|---|---|---|
| 1 | Logo | `Wordmark_Only_Center_Dark` |
| 2 | Hero | `SexScore_Hero_1` or `SexScore_Hero_2` — Sex Score branded hero |
| 3 | Header | `Heading_Title_H3` |
| 4 | Description | `Description_Copy_B2_Large_Center` |
| 5 | Sex Score listicle | `SS_Listicle_Module_1` — what the score covers |
| 6 | Button | `Button_Style_1_Center` |
| 7 | Disclaimer | `Disclaimer2` |
| 8 | Footer | `Footer_Dark` |

### Copy

```
S: See where you actually stand

Prev: A 2-minute assessment developed with licensed sexual health physicians.
```

**Hero image direction:** Sex Score branded visual from the design system — `SexScore_Hero_1` or `SexScore_Hero_2`. No couple imagery.

**Headline** `H3`
Better sex starts with knowing where you stand

**Body** `Description_Copy_B2_Large_Center`
The Sex Score™ is a 2-minute assessment developed with licensed sexual health physicians. No cost, no commitment — just a clear picture of where your sexual performance peaks and where there's room.

**Listicle** `SS_Listicle_Module_1`
Your score covers:
- Erection quality and consistency
- Stamina and endurance
- Confidence and satisfaction
- Recovery between sessions

**CTA** `Button_Style_1_Center`
Get my free Sex Score

**Disclaimer** `Disclaimer2`
Compounded drugs may be prescribed under federal law but are not FDA-approved and do not undergo FDA safety, effectiveness, or manufacturing review.

---

## Email 3: Dr. Sanchez — trust

**Timing:** Day 3
**Job:** Clinical credibility. A named physician directly answers the browse abandoner's real question: "Is this a pill mill or is this real?"

### Module layout

| Order | Module | Component reference |
|---|---|---|
| 1 | Logo | `Wordmark_Only_Center_Dark` |
| 2 | Hero | `Hero_TWI_Style_2_1x1.6` — Dr. Sanchez photo with text above |
| 3 | Header | `Heading_Title_H3` |
| 4 | Description | `Description_Copy_B2_Large_Left` |
| 5 | Listicle | `Listicle_Medium_1` — what the consultation covers |
| 6 | Button | `Button_Style_1_Center` |
| 7 | Disclaimer | `Disclaimer2` |
| 8 | Footer | `Footer_Dark` |

### Copy

```
S: Your doctor is standing by

Prev: Meet one of the licensed physicians behind every Rugiet treatment plan.
```

**Hero image direction:** Dr. Carlos Sanchez clinical photo. This is clinical credibility, not lifestyle. No couple imagery, no product shot.

**Headline** `H3`
Meet Dr. Carlos Sanchez

**Body** `Description_Copy_B2_Large_Left`
One of the licensed physicians behind every Rugiet Ready® treatment plan. 25+ years of clinical experience, applied directly to your health history and goals.

Every prescription starts with a physician review. Dr. Sanchez and his team evaluate your medical background, current medications, and health objectives — then design a treatment plan around your biology, not a one-size-fits-all formula.

**Listicle** `Listicle_Medium_1` — with icons:
- `License` icon — Licensed physician review of your full health history
- `Compound` icon — Custom-compounded medication tailored to your profile
- `MedicalTrack` icon — Ongoing clinical oversight, not a one-time prescription

**CTA** `Button_Style_1_Center`
Start your consultation

**Disclaimer** `Disclaimer2`
Compounded drugs may be prescribed under federal law but are not FDA-approved and do not undergo FDA safety, effectiveness, or manufacturing review.

---

## Email 4: Mechanism + offer

**Timing:** Day 5-7
**Job:** The mechanism email — explain what makes Ready different and pair it with the only discount in the flow. Hard expiry on the code.

### Module layout

| Order | Module | Component reference |
|---|---|---|
| 1 | Promo banner | `Promo_Banner_Black` — discount code banner |
| 2 | Logo | `Wordmark_Only_Center_Dark` |
| 3 | Hero | `Hero_ID_VT_Style_1_6x7` — "Valid Through" style hero with expiry date |
| 4 | Header | `Heading_Title_H2` |
| 5 | Description | `Description_Copy_B2_Large_Center` |
| 6 | Benefits | `Benefits_1` — three-ingredient breakdown |
| 7 | Stats | `Stats_Large_TI_1` — clinical stat with image |
| 8 | Button | `Button_Style_1_Center` |
| 9 | Disclaimer | `Disclaimer2` |
| 10 | Footer | `Footer_Dark` |

### Copy

```
S: Get your head in the game

Prev: Three active ingredients. One works on your brain. Save 10% before [expiry date].
```

**Promo banner** `Promo_Banner_Black`
Save 10% with code RUGIET10 — expires [date]

**Hero image direction:** Product hero preferred. If using the `Hero_ID_VT_Style_1_6x7` "Valid Through" layout, include the code expiry date in the hero module. Alternatively, the single permissible couple image in the flow (B&W treatment only) could be used here — but product hero is the stronger choice.

**Headline** `H2`
Most ED meds only help with blood flow

**Body** `Description_Copy_B2_Large_Center`
Ready™ goes further. Its sublingual formula combines three active ingredients — including apomorphine, which can help boost arousal signals in your brain. Not just blood flow. Brain and body, working together.

**Benefits** `Benefits_1` — three ingredients, each with icon and short description:

1. `Compound` icon — **Sildenafil**
Supports blood flow for stronger, more consistent erections.

2. `Compound` icon — **Tadalafil**
Extends the window — can support performance for up to 36 hours.

3. `Brain` icon — **Apomorphine**
Helps amplify arousal signals in the brain — something traditional ED medications don't address.

**Stats module** `Stats_Large_TI_1`
Works in as little as 15 minutes*
One sublingual dose. No pills to swallow. No waiting around.

**CTA** `Button_Style_1_Center`
Get my savings

**Disclaimer** `Disclaimer2`
*On average, after medication dissolves. Based on an internal survey of Rugiet Ready customers. Customer results have not been independently verified. Individual results may vary.

Compounded drugs may be prescribed under federal law but are not FDA-approved and do not undergo FDA safety, effectiveness, or manufacturing review.

---

## Compliance checklist

- [x] No cart/checkout language anywhere — "your cart" and "finish checking out" do not appear
- [x] Onset language is "works in as little as 15 minutes" with asterisk and full disclaimer
- [x] "RD-37™" does not appear anywhere
- [x] Standalone "Ready" uses ™ on first mention only (email 1, 2, 4). "Rugiet Ready" uses ® on first mention (email 3). No symbols after first mention.
- [x] Dr. Sanchez copy says "health history and goals" — not "results you want"
- [x] Quiz email references "licensed sexual health physicians" — not unnamed "experts"
- [x] Conditional verbs on all benefit claims (can, helps, supports, designed to)
- [x] One CTA per email
- [x] Subject lines six words or fewer
- [x] No puns in subject lines or body
- [x] Discount code only in email 4, with stated expiry
- [x] FDA compounding disclaimer in every footer
- [x] No exclamation points
- [x] Sentence case throughout
- [x] Apomorphine language is "helps amplify arousal" — not "sparks arousal" or "ignites libido"
- [x] No fabricated doctor quotes — Dr. Sanchez email describes his role, does not quote him
- [x] Imagery direction is unique per email (product hero, Sex Score visual, doctor photo, product/mechanism hero)

## Owned-channels self-check

1. **Channel match:** Lifecycle flow — warm, contextually aware, single point per email.
2. **Voice match:** Direct, matter-of-fact, dinner-party-guy register. No textbook, no punning sales bro, no wellness cliche.
3. **Format match:** Subject lines under six words. Sentence case. No exclamation points. Single CTA per email.
4. **Compliance check:** Conditional verbs on benefit claims. Full disclaimers. "As little as" not "as fast as."
5. **Hard nos clear:** No puns. No idiomatic expressions. No cliches. No fabricated quotes. No filler.
6. **TOV alignment:** Email 4 headline ("Most ED meds only help with blood flow") passes the boldness test — it's something true that the category doesn't say.
7. **Customer-mindset check:** Aspirational mirror throughout. No broken-patient framing.
8. **Product positioning check:** Ready onset language exact. Apomorphine mechanism language compliant.

---

## Design handoff notes

### For the designer

1. **Module references** are exact component names from the [Figma design system](https://www.figma.com/design/P8jY5nWxLQRaUSxcUTxx0m/2026-Q2-LCM-Emailify-Campaigns?node-id=237-22442). Pull each module directly from the design system page.

2. **Imagery needs per email:**
   - Email 1: Ready product hero (pill on black background or "Three medications" treatment)
   - Email 2: Sex Score branded visual (use existing `SexScore_Hero` assets from the design system)
   - Email 3: Dr. Carlos Sanchez clinical photo (existing asset)
   - Email 4: Product mechanism hero or single B&W couple image (only couple image in the flow)

3. **Color palette:** These are browse abandon (pre-purchase) emails. Recommend `PrimaryBlack` background for hero modules and `PrimaryWhite` for body sections to match the clinical credibility register. `PrimaryOrange` for CTAs and promo banner accents.

4. **Typography hierarchy per email:**
   - Headlines: `H2` (emails 1, 4) or `H3` (emails 2, 3)
   - Subheads: `SH1_Bold` for section headers within body
   - Body: `B1_Regular` or `B2_Regular`
   - Disclaimers: `C2` or `Citation`
   - Stats callouts: `H3` or `SH1_Bold`

5. **Button style:** `Button_Style_1` (primary CTA) throughout the flow. No secondary buttons — one CTA per email.

6. **Promo banner:** Only email 4 uses a `Promo_Banner_Black` at the top. Emails 1-3 have no promo banner.

7. **Product card modules:** Not used in this flow. These emails are pre-purchase intent builders, not product catalog sends.

8. **Email width:** 600px per the design system grid (5 columns, 20px L/R margins, 10px gutter).

---

## Change log

| Date | Change | Author |
|---|---|---|
| 2026-06-25 | Initial brief + copy doc with design system module references | lifecycle-creative |
