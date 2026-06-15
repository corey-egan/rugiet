# Rugiet Ready Browse Abandon Flow Analysis

**Date:** 2026-06-13
**Source:** [Browse Abandon](https://www.figma.com/design/luQdtOfoEljv6TPkwegtFR/LCM-Rebrand-System?node-id=3669-10199)
**References:** Email Marketing Bible v2.0, Rugiet Copywriting Skill (compliance, tone-of-voice, owned-channels), Lifecycle Conversion Flow Framework
**Related:** [Ready Welcome](./ready-welcome-flow-analysis.md) · [Ready Cart](./ready-cart-abandon-flow-analysis.md) · [Framework](./exec-summary-flow-optimization.md)
**Status:** Analysis complete — pending implementation

---

## Current state: 8 emails

| # | Figma name | Subject line | Primary job |
|---|---|---|---|
| 01 | Browse_Abandoned_01 | Still thinking about it? Ready is 10% off right now. | Social proof + cart language (wrong) |
| 02 | Browse_Abandoned_02 | You were so close | Social proof (duplicate) + quiz |
| 03 | Browse_Abandoned_03 | Get 10% off personalized ED treatment | Doctor / Dr. Sanchez trust |
| 04 | Browse_Abandoned_04 | Save 10% on the breakthrough ED med | Mechanism + offer |
| 05 | Browse_Abandoned_05 | Stop waiting, save 10% on Ready™ now | Mechanism + offer ("Don't wait") |
| 06 | Browse_Abandoned_06 | Take 10% off, then take it all off | Mechanism + offer ("Get your head in the game") |
| 07 | Browse_Abandoned_07 | Get 10% off the ED med that's custom-designed for you | Personalization + offer |
| 08 | Browse_Abandoned_08 | Get 10% off the 5-star ED med | Social proof + offer |

### Flow composition breakdown

- **Mechanism + discount emails:** 4 (04, 05, 06, 07) — four variations of the same email
- **Social proof / testimonials:** 3 (01, 02, 08) — emails 01 and 02 use the same three quotes
- **Doctor / trust:** 1 (03) — the strongest email, buried at position 3
- **Quiz / micro-commitment:** 1 (embedded in email 02) — the only non-purchase CTA, buried
- **Every email carries the discount banner** — no trust emails exist without a coupon

---

## Critical issues

### 1. Browse email says "your cart" — these people never carted anything

Email 01 body copy: "Ready is still in your cart. Come back now and save 10%." CTA: "FINISH CHECKING OUT."

This is a browse abandon flow. These subscribers looked at a product page and left. They never added anything to a cart and never started checkout. Telling someone about a cart they don't have does one of two things: confuses them, or signals that the emails are automated spam wallpaper. Per TOV: "assume the sale" — but don't assume actions the subscriber never took.

**Fix:** Reframe all copy from cart/checkout language to browsing/intent language. "You checked out Ready for a reason" replaces "Ready is still in your cart."

### 2. Eight emails for the lowest-intent audience

Browse abandoners are the lowest-intent audience in the lifecycle. They visited a page. They didn't start an intake form, didn't add to cart, didn't create an account. Per the lifecycle framework, browse abandon flows should be 4 emails maximum.

Per EMB §3 (Engagement-Based Sending): sending 8 emails to someone who merely browsed a page actively damages deliverability and trains the list to ignore the brand. Each additional email past 4 for this intent tier costs more in list health than it recovers in conversions.

### 3. RUGIET10 (10%) vs 5XFAST (15%) overlap

The browse flow uses RUGIET10 (10% off). The welcome flow uses 5XFAST (15% off). These audiences overlap heavily — most browse abandoners are also on the welcome list.

Anyone receiving both learns: the price is negotiable, and they should ignore the 10% because 15% exists.

**Braze suppression (confirmed in place):** Subscribers entering a higher-intent flow are removed from the prior flow. However, a subscriber could receive RUGIET10 from browse, then later enter the welcome flow and see 5XFAST at a higher discount — the sequence still exposes the price negotiability.

**Fix options:**
- Suppress browse abandon sends for anyone who has received or is active in the welcome flow in the last 30 days
- Unify the offer to a single code/discount across both flows

### 4. "Get hard in 15 minutes" — flat efficacy guarantee

Emails 04 and 05 use "Get hard in 15 minutes" as a standalone headline. This is more aggressive than the welcome flow's compliant "works in as little as 15 minutes" and constitutes a flat efficacy guarantee.

| Email | Phrasing | Compliant? |
|---|---|---|
| Welcome flow | "works in as little as 15 minutes" | Yes — conditional, qualified |
| Browse 04 | "Rugiet Ready® helps you get hard in 15 minutes on average.*" | Borderline — "helps" is conditional but "get hard in 15 minutes" as a headline is an absolute claim |
| Browse 05 | "Get hard in 15 minutes*" (standalone headline) | No — flat efficacy guarantee |

Per compliance.md §4: onset language must be "works in as little as 15 minutes" — never "get hard in 15 minutes."

### 5. "RD-37™" — unexplained, cut it

Email 05 introduces "RD-37™" with zero explanation: "RD-37™ delivers it like no other, dissolving under your tongue and bypassing digestion to get you ready fast."

No other email in any flow uses "RD-37™." A browse abandoner seeing this for the first time has no idea what it means. It reads as an internal code name that leaked into production copy.

**Fix:** Cut "RD-37™" entirely. Replace with "Ready™'s sublingual formula" or similar.

### 6. Trademark usage violations (per trademark-usage.md)

Per the trademark guide: standalone "Ready" is unregistered and gets ™ on first mention only. "Rugiet Ready" is registered and gets ® on first mention only. After first mention in any email, no symbol is needed.

| Email | Current usage | Correct per trademark guide |
|---|---|---|
| 02 | "Ready®" in "Over 500k+ guys have switched to Ready®" | "Ready™" on first mention, no symbol on subsequent — standalone "Ready" never gets ® |
| 04 | "Rugiet Ready®" in body | **Correct** — full product name is registered, ® on first mention is right |
| 05 | "Ready®" in body (standalone) | "Ready™" on first mention — standalone "Ready" never gets ® |
| 06 | "Ready®" (3 standalone instances) | First mention → "Ready™", remaining 2 → no symbol |
| 07 | No ® (clean) | ✓ |

**Note:** Email 04 is the only one using the trademark correctly — "Rugiet Ready®" as the full registered product name.

### 7. Same couple imagery 8 times

Every email except 03 (Dr. Sanchez) uses the same silver-haired couple in soft-lit bed embrace. The result:
- Emails become visually indistinguishable — the 8-email flow feels like one email resent
- The repetition drags every email's tone toward "sex ad" — exactly wrong for trust and mechanism emails
- By email 3-4, the imagery has zero stopping power

Per the lifecycle framework (imagery direction): product hero for mechanism/offer emails, doctor photo for trust emails, max 1 couple image per flow.

### 8. Same testimonials appear in emails 01 and 02 with different attribution

Both emails use the same three quotes:
- "You will not regret getting it"
- "A much more natural legacy effect" / "Recovery between shots is much quicker"
- "All I can say is this stuff works"

Email 01 attributes them to Thomas, Micha, and WB. Email 02 relabels all three as "VERIFIED PATIENT." A subscriber who reads both emails back-to-back sees the same quotes with different attribution — it makes the testimonials look fabricated.

Additionally, "a much more natural legacy effect" is patient-speak that means nothing to a new reader.

**Fix:** Use different testimonials in each email. Apply the testimonial standard: first name + last initial, specific outcome, no efficacy absolutes.

### 9. Subject line pun violates owned-channels rules

Email 06: "Take 10% off, then take it all off"

Per owned-channels.md: "No puns. Including product-name puns. This is the buttoned-up channel." This subject line is a double-entendre pun.

### 10. Multiple CTAs per email

| Email | CTA count | CTAs |
|---|---|---|
| 01 | 2 | FINISH CHECKING OUT, TRY FOR YOURSELF |
| 04 | 2 | GET STARTED, GET MY SAVINGS |
| 05 | 2 | SAVE 10% NOW, GET MY OFFER |
| 06 | 3 | SAVE 10% NOW, GET MY SAVINGS, GET STARTED |
| 07 | 2 | GET STARTED & SAVE, SHOP NOW |

Per owned-channels.md: "One CTA per email."

### 11. Emails 04-07 are four variations of the same email

| Email | Headline | Body message |
|---|---|---|
| 04 | "Live your best sex life" | Mechanism (15 min onset) + 10% off |
| 05 | "DON'T WAIT" | Mechanism (15 min onset) + 10% off |
| 06 | "GET YOUR HEAD IN THE GAME" | Mechanism (brain + body) + 10% off |
| 07 | "Dose smarter, get harder" | Personalization + 10% off |

All four follow the same pattern: couple hero → mechanism/personalization section → 10% discount CTA. A subscriber receiving all four gets the same message rephrased four times.

---

## Recommended 4-email structure

The CEO's proposed resequence aligns with the lifecycle framework's browse abandon touchpoint hierarchy (4 emails max for lowest-intent audience).

### Email 1: Intent hook — hours after browse

**Current closest:** Email 01 (structure), but needs complete copy rewrite
**Action:** Rewrite copy, swap imagery

**Structure:**
- Subject: "You checked out Ready for a reason" (6 words)
- Hero: Product hero (the black-background "Three medications. One little dose." treatment from the welcome flow is the strongest visual available — use it or the pill close-up)
- Body: "You looked at Ready for a reason. Three medications. One sublingual dose. Works in as little as 15 minutes." Light social proof in body: "Over 500,000 men trust Ready™."
- CTA: GET STARTED
- No discount — this is the lowest-intent audience; a discount in email 1 signals desperation

**Key fixes vs current:**
- Remove all cart/checkout language ("still in your cart," "finish checking out")
- Replace couple hero with product hero
- No discount code or banner

**Image:** Product hero — not the couple

---

### Email 2: Process transparency — low-commitment CTA (Day 1)

**Current closest:** No direct equivalent in the browse flow. Modeled on the Ready cart test variant T3 ("Here's what the visit looks like"), which was one of the strongest emails we reviewed across all flows.
**Action:** New email — build from the cart T3 template

**Decision (2026-06-13):** Keeping the Sex Score quiz at position 2. The micro-commitment value outweighs the deliverability risk. Monitor inbox placement and complaint rates after launch.

The quiz ("See where your sexual performance peaks") is the only CTA in the flow that doesn't ask for a purchase. That's the right job for a low-intent browser — a micro-commitment that warms them into the intake funnel.

**Structure:**
- Subject: needs review — current "Get your FREE sex score" subject may need softening for deliverability
- Hero: "Better sex starts with Ready" + quiz visual
- CTA: GET MY FREE SEX SCORE (or softened variant)
- No discount

**Remaining fixes for this email:**
- Fix "built by sexual health experts" — name the experts or rephrase to "developed with licensed sexual health physicians"
- Fix "Ready®" standalone → Ready™ per trademark guide
- Fix "half a million men" → "500,000" for consistency with other flows
- Monitor deliverability post-launch

**Image:** Quiz/assessment visual — not the couple

---

### Email 3: Dr. Sanchez — trust and consultation CTA (Day 3)

**Current:** Email 03 — keep as the foundation
**Action:** Fix body copy, update CTA

This is the best email in the flow. A named physician with stated clinical experience directly answers the browse abandoner's actual question: "Is this a pill mill or is this real?" Dr. Sanchez's photo does more trust work than any couple shot.

**Structure:**
- Subject: "Your doctor is standing by" (5 words) — keep current
- Hero: Dr. Sanchez photo — keep (this is clinical credibility, not lifestyle)
- Body: "Meet Dr. Carlos Sanchez — One of the licensed physicians behind every Rugiet treatment plan. 25+ years of experience, applied directly to your health history and goals."
- **Critical copy fix:** Change "we design a medication for you and the results you want" to "we design a medication around your health history and goals." The original is an efficacy promise; the fix is a personalization statement.
- CTA: "START YOUR CONSULTATION" (replaces generic "GET STARTED")
- No discount banner — a doctor's face next to a coupon undermines clinical credibility

**Image:** Dr. Sanchez clinical photo — keep as-is

---

### Email 4: Mechanism + offer with expiry (Day 5-7)

**Current closest:** Email 06 ("Get your head in the game")
**Action:** Keep as the surviving mechanism email; add real expiry to RUGIET10

The CEO correctly identifies "Get your head in the game" as having the best concept-to-copy fit in the flow because it ties the apomorphine brain angle to the headline. This is the one email where the couple image could be acceptable (the only one in the flow), but ideally swap to the product hero.

**Structure:**
- Subject: "Get your head in the game" (6 words)
- Hero: Product hero preferred, or the one permissible couple image (B&W treatment only)
- Body: "Most ED meds only help with blood flow. 3-in-1 Ready™ combines sildenafil, tadalafil, and apomorphine to not just enhance blood flow — but to help boost arousal signals in your brain."
- Offer: "Save 10% with code RUGIET10. Your code expires [specific date]."
- CTA: GET MY SAVINGS (single CTA — cut the other two)

**Key fixes vs current:**
- Fix all "Ready®" to "Ready™"
- Cut "RD-37™" if any remnant copy references it
- Add real expiry date to RUGIET10 — "for a limited time" is not urgency
- Reduce from 3 CTAs to 1
- Fix pun subject line ("Take 10% off, then take it all off") — not applicable since we're using "Get your head in the game" instead

**Image:** Product hero or single B&W couple (the only one in the flow)

---

## Emails to cut

| Email | Subject | Why cut |
|---|---|---|
| 01 | Still thinking about it? | Cart language in browse flow — needs full rewrite → becomes new email 1 |
| 02 | You were so close | Quiz extracted to email 2; duplicate testimonials; accusatory subject |
| 04 | Save 10% on the breakthrough ED med | Same message as 05, 06, 07 — "get hard in 15 minutes" is non-compliant |
| 05 | Stop waiting, save 10% | Same message as 04, 06, 07 — "RD-37™," non-compliant headline |
| 07 | Get 10% off the custom-designed ED med | Same message as 04, 05, 06 — personalization angle covered elsewhere |
| 08 | Get 10% off the 5-star ED med | Duplicate social proof; hyperbolic testimonials ("literally nothing," "best product on the market") |

---

## Revised flow at a glance

| Position | Timing | Job | Discount? | Source |
|---|---|---|---|---|
| 1 | Hours after browse | Intent hook + product hero | No | Rewritten from Browse 01 |
| 2 | Day 1 | Quiz / micro-commitment (Sex Score) | No | Keeping quiz — monitor deliverability |
| 3 | Day 3 | Doctor trust (Dr. Sanchez) | No | Browse 03 (fixed copy + CTA) |
| 4 | Day 5-7 | Mechanism + offer with expiry | Yes (RUGIET10, 10%) | Browse 06 ("Get your head in the game") |

**Offer concentration:** Only email 4 carries a discount. Emails 1-3 are trust/engagement emails with no coupon. The discount appears once, with a stated and enforced expiry.

---

## Immediate flips — fix before the next send

| Email | Issue | Fix |
|---|---|---|
| 01 | "Ready is still in your cart" — browse abandoners never carted | Rewrite to intent-referencing language |
| 01 | CTA "FINISH CHECKING OUT" — they never started checkout | Change to "GET STARTED" |
| 02 | Same 3 testimonials as email 01 with different attribution | Use different testimonials or remove |
| 03 | "we design a medication for you and the results you want" | Change to "around your health history and goals" |
| 03 | CTA "GET STARTED" — generic | Change to "START YOUR CONSULTATION" |
| 04 | "get hard in 15 minutes" — flat efficacy guarantee | Reframe to "works in as little as 15 minutes" |
| 05 | "Get hard in 15 minutes*" — flat efficacy headline | Reframe to "works in as little as 15 minutes" |
| 05 | "RD-37™" — unexplained internal code name | Cut entirely |
| 06 | Subject "Take 10% off, then take it all off" — pun | Remove if this email is kept; already cut in restructure |
| 02, 04, 05, 06 | "Ready®" — should be Ready™ | Change all to Ready™ |
| All emails | Same couple image used 8 times | Commission flow-unique imagery |

---

## Compliance checklist for revised flow

- [ ] No cart/checkout language in browse abandon emails — "your cart," "finish checking out" are removed
- [ ] Onset language is "works in as little as 15 minutes" everywhere — not "get hard in 15 minutes"
- [ ] "RD-37™" does not appear anywhere
- [ ] Standalone "Ready" uses ™ on first mention only (never ®). Full "Rugiet Ready" uses ® on first mention only. After first mention, no symbol needed. Per trademark-usage.md.
- [ ] Dr. Sanchez body copy says "health history and goals" not "results you want"
- [ ] Quiz email names the experts or uses "licensed sexual health physicians"
- [ ] Testimonials are unique per email — no duplicates with different attribution
- [ ] Every testimonial has first name + last initial, specific outcome, no efficacy absolutes
- [ ] One CTA per email
- [ ] Subject lines 6 words or fewer
- [ ] No puns in subject lines or body
- [ ] Discount code has stated and enforced expiry
- [ ] Discount only in the final email (position 4)
- [ ] FDA compounding disclaimer in every footer
- [ ] Imagery is unique to this flow — not recycled from welcome or cart

---

## Change log

| Date | Change | Author |
|---|---|---|
| 2026-06-13 | Initial analysis incorporating CEO feedback, EMB best practices, rugiet-copywriting compliance/tone/channel rules, and lifecycle conversion flow framework | lifecycle-creative |
