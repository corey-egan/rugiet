# Lifecycle Conversion Flow Framework

**Date:** 2026-06-13
**Status:** Approved baseline — all product flows measured against this framework
**Products in scope:** Rugiet Ready, Go Long (extensible to future products)
**Supporting analyses:** [Ready Welcome](./ready-welcome-flow-analysis.md) · [Ready Cart](./ready-cart-abandon-flow-analysis.md) · [Go Long](./golong-flow-analysis.md) · [Ready Exec Summary](./exec-summary-ready.md) · [Go Long Exec Summary](./exec-summary-golong.md)

---

## Purpose

This document establishes the unified structure, messaging hierarchy, and operating rules for all Rugiet lifecycle conversion flows. Every flow — current and future, across every product — is built from this framework and critiqued against it. The per-product executive summaries contain the implementation details. This document contains the strategy.

---

## Part 1: Touchpoint hierarchy by flow

Each flow type has a defined number of touchpoints, a fixed message sequence, and rules governing which touchpoints carry an offer. The sequence is not arbitrary — it follows a trust arc that mirrors how a prescription buyer actually makes a decision: hook → differentiate → explain → set expectations → prove → personalize → connect → close.

### Welcome flow — 8 touchpoints

| Touchpoint | Job | Message | Carries offer? |
|---|---|---|---|
| 1 — Hook | Acknowledge intent, deliver first value | "You looked at [product] for a reason. Here's what it does and why it's different." Light offer with stated expiry. | Yes |
| 2 — Differentiation | Answer the competitive question | "Why not just buy generic for $2?" Comparison table: [product] vs. generic alternatives. | Yes |
| 3 — Mechanism | Explain how it works | Ingredient breakdown, dual/triple action, how the science translates to outcomes. Clinical credibility. | No |
| 4 — Expectation-setting | Build trust through honesty | Dosing instructions, onset timeline, side effects (honest and specific). This is the strongest trust lever in the flow. | No |
| 5 — Social proof | Let other men speak | Curated, compliant testimonials anchored by a product-specific stat. One email, not four. | Yes |
| 6 — Personalization | "Built for your body" | Compounding, doctor-designed, customized dosing. The angle no competitor can claim. | No |
| 7 — Confidence / partner | The relationship impact | Frame around what the partner notices, what changes beyond the physical. Product-specific framing required (PE for Go Long, ED for Ready). | No |
| 8 — Closer | Final offer with real urgency | Pure conversion. Code with hard expiry. No product education — that was emails 1-7. | Yes |

**Trust arc:** Touchpoints 3, 4, 6, and 7 are trust emails. They carry no discount banner. The offer concentrates in touchpoints 1, 2, 5, and 8.

---

### Browse / questionnaire abandon flow — 4 touchpoints

| Touchpoint | Job | Message | Carries offer? |
|---|---|---|---|
| 1 — Intent hook | Reference curiosity, not abandonment | "You checked out [product] for a reason." Product hero image. No accusatory language ("Don't stop," "You left," "Don't give up" are prohibited). | No |
| 2 — Low-commitment CTA | Give them a next step that isn't purchase | Quiz, assessment, educational content — something that re-engages without asking for money. Micro-commitment. | No |
| 3 — Doctor / trust | Named physician, clinical credibility | A real doctor, by name, with stated credentials. Answers the unspoken question: "Is this a pill mill or is this real?" Clinical hero image. | No |
| 4 — Mechanism + offer | Explain the product + first (and only) offer | How the product works, what's in it, why it's different. Discount code with stated expiry. This is the only email in the flow that carries an offer. | Yes |

**Intent calibration:** Browse/questionnaire abandoners are the lowest-intent audience. They need fewer touches and lighter pressure. Sending 9 emails to someone who couldn't finish a form damages deliverability and trains the list to ignore the brand.

---

### Cart abandon flow — 5 touchpoints

| Touchpoint | Job | Message | Carries offer? |
|---|---|---|---|
| 1 — Cart reminder | Simple nudge, process clarity | "Your place is saved." Explain what happens next (online visit, provider review, prescription ships). No discount — let the product sell itself first. | No |
| 2 — Doctor / trust | Clinical credibility | Named physician, board certification, "a real doctor personally reviews your case." Promoted to position 2 because the cart abandoner's objection is "is this safe and legit?" not "is it cheap enough?" | No |
| 3 — Personalization | "Built around you" | Compounding, customized dosing, doctor-designed. Collapse any repeated personalization messaging into this single email. | No |
| 4 — Social proof + offer | Curated testimonials with the first discount | Best compliant quotes. Single discount tier with a stated expiry ("Your code expires in 48 hours"). | Yes |
| 5 — Last chance | Final offer with enforced expiry | The only email in any flow permitted to use "last chance" language — because it is, in fact, the last email. Code dies after this. | Yes |

**Intent calibration:** Cart abandoners are the highest-intent audience. They selected the product and started checkout. They usually need a trust signal and a nudge, not a deeper discount. The first three emails carry no offer. Discounting is a last resort, introduced only after trust has been established.

---

## Part 2: Consistent rules across all flows

### Claims consistency

Every product needs a locked canonical descriptor that appears consistently across every email in every flow. The descriptor must be factually anchored to the product's ingredients and benefits — not a marketing tagline that drifts between emails.

| Product | Canonical descriptor | Anchored to |
|---|---|---|
| Ready | "3 medications. 5 benefits. 1 dose." | 3 ingredients (sildenafil, tadalafil, apomorphine), 5 benefit claims, sublingual dose |
| Go Long | TBD — recommend "2 ingredients. 2 problems solved. 1 dose." | 2 ingredients (paroxetine, tadalafil), 2 PE causes addressed, single dose |

**Rules:**
- The canonical descriptor appears in at least 3 of 8 welcome emails (hook, mechanism, closer at minimum)
- Never use shorthand ("3-in-1," "5-in-1," "2-in-1") alone — these create the inconsistency problem we found in Ready where the same flow said both "3-in-1" and "5-in-1"
- The descriptor is a factual statement, not a claim — it doesn't require conditional verbs
- Future products must define and lock a canonical descriptor before any flow is built

**Onset and duration claims:**
- "Works in as little as 15 minutes" — never "as fast as," never "in less than"
- "Up to 36 hours" — never "for several days," never without "up to"
- These exact phrasings are non-negotiable per compliance.md

---

### Testimonial and review standards

Every testimonial across every product, every flow, every email must meet all of the following:

| Standard | Rule |
|---|---|
| Attribution | First name + last initial (e.g., "Michael R.") — not "Verified Patient" |
| Specificity | Must reference a concrete outcome: timing, confidence, partner reaction, comparison to alternatives |
| Compliance | No efficacy absolutes: "always works," "cured me," "miracle," "every time," "guaranteed" are all prohibited |
| Quality | Typo-free. Audited before any send. No exceptions. |
| Tone | Warm and human — reads like a real person, not a marketing script |
| Disclaimer | Every email containing testimonials carries: "Customer's results have not been independently verified. Individual results may vary." |
| Prohibited content | No sexually explicit language, no language that objectifies partners ("addicted playmates"), no exclamation-heavy quotes ("Holy crap!!!") |

**Social proof anchors:**
- Each product uses its own stat — do not borrow across products
- Ready: "Over 500,000 men trust Ready" (confirmed)
- Go Long: TBD — source a Go Long-specific number before building social proof emails
- The anchor stat must be substantiated and on file. Unsubstantiated claims ("2.5 million satisfied partners") are prohibited.

---

### Brand alignment

**Voice:** Every email, regardless of flow or product, must pass the owned-channels.md self-check:
- Does this sound like the dinner-party-guy — confident, direct, matter-of-fact, adult?
- Is there one CTA per email? (Multiple CTAs = no CTAs)
- Is the subject line 6 words or fewer?
- Are there zero exclamation points?
- Is the provocation aimed at a convention or lie, never at the customer?
- Is the customer addressed as an aspirational mirror, not a broken patient?

**Product positioning guard rails:**

| Product | Marquee benefit | Headline/subject line rule |
|---|---|---|
| Ready | ED (erectile dysfunction) | ED framing permitted in headlines. "3 medications. 5 benefits. 1 dose." |
| Go Long | PE (premature ejaculation) | PE is the marquee. ED is body copy only — never in headlines, subject lines, or hero copy. Partner angle must be about timing/endurance, never erections. |

**Trademark:** Ready™ (trademark symbol) consistently. Never Ready® unless and until the trademark is registered. Audit every email for stray ® symbols.

**Format:**
- Sentence case everywhere — headlines, subheads, buttons, CTAs
- No exclamation points, anywhere, ever
- No puns or idiomatic expressions in email (per owned-channels.md)
- No humor tactics — humor dilutes credibility in email
- No accusatory abandon language ("Don't stop," "You left," "Don't give up") — use intent-referencing language ("You checked out [product] for a reason")

---

### Offer codes: approach, escalation, suppression, and placement

#### Approach

- One discount tier per flow. The tier does not escalate across emails within a flow.
- Every discount code must carry a stated expiry date. "For a limited time" with no date is prohibited.
- Body copy sells the product. The banner and CTA carry the offer. These are separate jobs — never combine an emotional benefit and a discount in the same sentence. "Get confidence you can depend on. Get 15% off." violates this rule.

#### Escalation rules

- Within a single flow, the discount does not increase. A subscriber who ignores a 15% code should not be rewarded with a 20% code later in the same sequence.
- If a deeper discount is used (e.g., CART20 in the cart closer), it appears only in the final email, is framed as final ("this code dies tomorrow"), and it actually dies.
- First-time abandoner flag: any escalated discount should only fire for first-time cart abandoners, not repeat abandoners who have already received the deeper code.

#### Suppression

- **Flow priority waterfall (confirmed in place):** When a subscriber enters a higher-intent flow, they are removed from the prior flow. Cart > Welcome > Browse. Codes are not overlapping.
- Code expiry enforcement: expired codes must fail at checkout, not silently succeed. (Verify.)
- Re-entry suppression: purchase from any flow immediately suppresses remaining emails in that flow. (Verify.)

#### Placement by touchpoint

**Welcome flow (8 emails):**

| Touchpoint | Has discount banner? | Rationale |
|---|---|---|
| 1 — Hook | Yes | Conversion email — subscriber just arrived with intent |
| 2 — Differentiation | Yes | Early flow, still converting |
| 3 — Mechanism | No | Trust email — coupon undermines clinical credibility |
| 4 — Expectation-setting | No | Trust email — side-effect honesty + coupon is tone-deaf |
| 5 — Social proof | Yes | Social proof + offer is a natural conversion pair |
| 6 — Personalization | No | Trust email — "built for your body" + coupon cheapens the message |
| 7 — Confidence / partner | No | Trust email — relationship angle must not feel transactional |
| 8 — Closer | Yes | Pure offer email — this is the coupon's job |

**Browse abandon flow (4 emails):**

| Touchpoint | Has discount banner? | Rationale |
|---|---|---|
| 1 — Intent hook | No | Lowest-intent audience — discount in email 1 signals desperation |
| 2 — Low-commitment CTA | No | Re-engagement, not conversion |
| 3 — Doctor / trust | No | Clinical credibility email |
| 4 — Mechanism + offer | Yes | First and only offer in the flow, with stated expiry |

**Cart abandon flow (5 emails):**

| Touchpoint | Has discount banner? | Rationale |
|---|---|---|
| 1 — Cart reminder | No | Highest-intent audience — they need a nudge, not a coupon |
| 2 — Doctor / trust | No | Clinical credibility email |
| 3 — Personalization | No | Trust/education email |
| 4 — Social proof + offer | Yes | First offer, introduced after 3 trust emails |
| 5 — Last chance | Yes | Final email, hard expiry, only email that can say "last chance" |

---

### Imagery direction

The same couple photo set cannot appear across multiple flows. Each flow gets its own distinct creative. Image direction varies by email type:

| Email type | Hero image direction |
|---|---|
| Hook / offer emails | Product hero (the pill, the packaging, the dose) |
| Mechanism emails | Product hero or ingredient/chemistry visuals |
| Trust / doctor emails | Named physician in clinical context — doctor photo, not lifestyle |
| Social proof emails | Real patient context (not stock couple imagery) |
| Expectation-setting emails | Solo male portrait — serious, direct, no lifestyle staging |
| Couple / lifestyle | Maximum 1 per flow, unique to that flow |

---

## Part 3: How to use this framework

### For existing flows (Ready, Go Long)

The per-product executive summaries ([Ready](./exec-summary-ready.md), [Go Long](./exec-summary-golong.md)) contain the specific immediate flips and restructure plans. Those are the implementation documents. This framework is the standard they were built against.

### For new product flows

When building a lifecycle flow for a new product (e.g., a new longevity SKU, a new sexual health product):

1. Define the product's canonical descriptor before writing any email
2. Source a product-specific social proof anchor before building the social proof email
3. Identify the product positioning guard rail (what's the marquee benefit? what's body-copy-only?)
4. Build the flow using the touchpoint hierarchy tables above — same structure, same offer placement logic
5. Run every email through the compliance checklist and brand alignment self-check before any send
6. Commission flow-unique photography — do not recycle from other flows

### For flow audits

When auditing any existing flow against this framework, check:

- [ ] Does the flow follow the touchpoint hierarchy for its type (welcome, browse, cart)?
- [ ] Is the product canonical descriptor consistent across all emails?
- [ ] Are trust emails free of discount banners?
- [ ] Does "last chance" appear only in the actual final email?
- [ ] Does every discount code have a stated and enforced expiry?
- [ ] Do all testimonials meet the review standards (attribution, specificity, compliance, quality)?
- [ ] Is onset/duration language compliant ("as little as," "up to")?
- [ ] Is there one CTA per email?
- [ ] Are subject lines 6 words or fewer?
- [ ] Is imagery unique to this flow?
- [ ] Is the product positioning guard rail enforced in all headlines and subject lines?

---

## Change log

| Date | Change | Author |
|---|---|---|
| 2026-06-13 | Initial framework established from Ready and Go Long flow analyses | lifecycle-creative |
