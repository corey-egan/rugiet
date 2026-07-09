# Rugiet Ready Cart Abandon Flow Analysis

**Date:** 2026-06-13
**Source:** [Cart Emails](https://www.figma.com/design/luQdtOfoEljv6TPkwegtFR/LCM-Rebrand-System?node-id=3669-10200)
**References:** Email Marketing Bible v2.0, Rugiet Copywriting Skill (compliance, tone-of-voice, owned-channels), Email Sequences Skill (rugiet-marketing-claude)
**Related:** [Ready Welcome Flow Analysis](./ready-welcome-flow-analysis.md)
**Status:** Analysis complete — pending implementation

---

## Current state: 9 emails + 3 test variants

### Main cart flow (9 emails)

| # | Subject line | Discount | Primary job |
|---|---|---|---|
| 01 | Don't miss out on your exclusive 15% savings | CART15 / 15% | Social proof (85% stat) + urgency |
| 02 | You're about to miss out on 15% off | CART15 / 15% | Mechanism (ingredient breakdown) |
| 03 | Ready™ works in 15 minutes* | CART15 / 15% | Personalization ("Customized to you") |
| 04 | Get better performance, get 15% off | CART15 / 15% | Social proof (testimonials) — **says "Last chance"** |
| 05 | Seize the moment with 15% off | CART15 / 15% | Confidence angle + discount |
| 06 | Don't miss the savings. Get Ready. | CART15 / 15% | Mechanism + personalization ("tailored to you") |
| 07 | Confidence is in your cart. Save 20% when you purchase. | CART20 / 20% | Social proof (testimonials) — **escalated discount** |
| 08 | Ready™ works in 15 minutes | CART20 / 20% | VIP/doctor email ("Treatment on your terms") |
| 09 | Get Ready™. Make moves tonight. | CART20 / 20% | Personalization ("Personalize your approach") |

### Test variants (testing against emails 01-03)

| # | Subject line | Discount | Primary job |
|---|---|---|---|
| T1 | Your provider is waiting | CART15 / 15% | Provider-focused reminder |
| T2 | Don't forget about your online consultation | CART15 / 15% | Follow-up reminder |
| T3 | Here's what the visit looks like | CART15 / 15% | Process transparency |

### Flow composition breakdown

- **Personalization ("tailored/customized/built around you"):** 4 emails (03, 06, 08, 09) — four versions of the same message
- **Social proof (testimonials + stats):** 3 emails (01, 04, 07)
- **Mechanism (ingredient breakdown):** 2 emails (02, 06)
- **Pure urgency/discount:** 2 emails (04 "Last chance", 05 "Seize the moment")
- **VIP/doctor:** 1 email (08) — the strongest email, buried at position 8

---

## Critical issues

### 1. "Last chance" at email 4 of 9

Email 04 leads with "Last chance: Get Ready® for 15% off." Five more emails follow — three of which offer a *better* deal at 20%.

This does two things:
- It teaches the subscriber that Rugiet's urgency language is meaningless. Every future "last chance" across every flow will be read as "more emails are coming."
- It actively rewards ignoring the urgency. The subscriber who waits past "last chance" gets CART20 instead of CART15.

Per EMB §4 (Abandoned Cart): the recommended structure is 3 emails — reminder, objection-handling, small incentive — not 9 emails with escalating offers. "Last chance" can only ever appear in the actual last email about an offer.

### 2. The discount escalation ladder trains bad behavior

The flow currently runs:

| Emails 1-6 | CART15 (15% off) |
|---|---|
| Emails 7-9 | CART20 (20% off) |

Combined with the welcome flow (5XFAST / 15%) and browse flow (RUGIET10 / 10%), the brand now has **4 different promo codes at 3 different discount levels** targeting the same person. A repeat customer will quickly discover that the optimal buying strategy is: browse → ignore → add to cart → ignore → wait a week → get 20% off.

**Cross-flow discount map:**

| Flow | Code | Discount | Emails using it |
|---|---|---|---|
| Browse abandon | RUGIET10 | 10% | Unknown |
| Welcome | 5XFAST | 15% | All 11 emails |
| Cart abandon (early) | CART15 | 15% | Emails 1-6 |
| Cart abandon (late) | CART20 | 20% | Emails 7-9 |

Per EMB §4 (Abandoned Cart): "Email 1 (1-4h): Simple reminder. NO discount. Email 2 (24h): Address objections. Reviews, shipping, guarantee. Email 3 (48h): Small incentive if margins allow. First-time abandoners only." The discount should be a single step, not a two-tier escalation held across six emails.

**The fix is not killing the escalation entirely** — it's making it truthful:
- One discount tier, introduced once, with a stated and enforced expiry
- Suppression rules so no subscriber sees two different codes in the same week
- **Open question:** Do we currently have suppression rules preventing a subscriber from seeing CART15 and 5XFAST in the same week? If not, this is a priority Braze configuration item.

### 3. Cart abandoners may not need a deeper discount at all

Cart abandoners are the highest-intent audience in any ecommerce funnel. They've already browsed, selected a product, and started the purchase process. Per EMB §4: the most effective cart abandonment emails "either address specific objections (Tuft and Needle), use founder-personal tone (Ugmonk), deploy scarcity without discounting (Alo Yoga), or lead with personality (Allbirds). Discounting should be the last resort, not the first email."

The test variants (T1-T3) demonstrate this insight. They focus on the *process* — "your provider is waiting," "here's what the visit looks like" — and the discount is a single line at the bottom. They read as more credible than any of the 9 main cart emails.

### 4. Only 4 unique emails across 9

The personalization message appears in four different forms:

| Email | Headline | Message (same) |
|---|---|---|
| 03 | "Customized to you" | Rugiet doctors build treatment around you |
| 06 | "Next-gen medicine, tailored to you" | Ready takes a mind and body approach |
| 08 | "Treatment on your terms" | Doctors formulate treatment specifically for you |
| 09 | "Personalize your approach" | Your ED treatment should be built around you |

A subscriber receiving all 9 emails sees the same "your dose is custom" message four times with different headlines. By the third repetition, the reader stops reading.

### 5. Testimonial problems

**Email 04:**
- "IT WORKED WELL... LIKE REALLY WELL... 10/10 would recommend to anyone who wants stronger erections, longer performance time, addicted playmates." — The phrase "addicted playmates" is inappropriate, off-brand, and creates compliance risk. Remove this testimonial entirely.

**Email 07:**
- "ONE OF THE DEW THAT HAS CONSISTENTLY WORKED FOR ME" — "DEW" is a typo. Should be "FEW." This has been published with a typo visible to every cart abandoner who reaches email 7.

**Email 07 (body text contradiction):**
- The banner says CART20 (20% off) but the body text says "Join the thousands of men who have experienced the Rugiet difference, and save 15% today." — The discount percentage contradicts itself within the same email.

**Underused testimonials the CEO flagged as strong:**
- "(and tastes better)" — specific, memorable, distinctive detail
- "The comments from my wife made it the absolute perfect evening" — partner-angle testimonial that is warm and specific

### 6. Compliance violations

| Location | Issue | Rule violated | Fix |
|---|---|---|---|
| Email 01 body | "as fast as 15 minutes" | compliance.md §4: must be "as little as" | Replace |
| Email 04 hero | "Ready®" standalone | Per trademark-usage.md: "Ready" alone is unregistered → ™ on first mention only, never ® | Change to Ready™ on first mention, no symbol after |
| Email 05 body | "Ready's®" standalone | Same rule — standalone "Ready" never gets ® | Change to Ready's on subsequent mention (or Ready™'s on first) |
| Email 06 body | "Ready®" standalone (2x) | Same rule | Change to Ready™ on first mention, no symbol after |
| Email 09 body | "Ready®" standalone (4x) | Same rule — first mention gets ™, subsequent mentions get no symbol | Change first to Ready™, drop symbol from remaining 3 |
| Email 09 features | "Starts working in as fast as 15 minutes*" | compliance.md §4: must be "as little as" | Replace |
| Email 07 body | "save 15% today" with CART20 banner | Internal contradiction | Fix to 20% or remove |
| Multiple emails | "this offer won't last forever" / "for a limited time" | No actual expiry stated or enforced | Add real expiry or remove |

### 7. Emotion + discount blending

Email 05 exemplifies a pattern across the flow: "Get confidence you can depend on. Get 15% off." When headline copy melds an emotional benefit with a discount, it cheapens both. The body copy should sell the product while the banner/CTA handles the offer.

Compare:
- Email 05: "Get confidence you can depend on. Get 15% off." — reads as a coupon ad
- Email 08: "Treatment on your terms" (hero) → doctor credential section → "Save 20%" (only at bottom CTA) — reads as premium

Per owned-channels.md: "One idea per email — if there are two ideas, split into two emails." Confidence and discount are two ideas.

### 8. Multiple CTAs per email

| Email | CTA count | CTAs |
|---|---|---|
| 02 | 3 | COMPLETE MY ORDER NOW, SAVE 15% NOW, SAVE 15% TODAY |
| 03 | 3 | GET READY™, GET STARTED, GET YOURS NOW |
| 04 | 2 | FINISH CHECKOUT, TRY FOR YOURSELF |
| 05 | 2 | GO ALL THE WAY, SAVE 15% |
| 09 | 3 | GET STARTED (×2), GET STARTED (discount section) |

Per owned-channels.md and EMB §5: "One CTA per email. Multiple CTAs = no CTAs."

### 9. Same-couple imagery (global issue, again)

The recycled couple from the welcome flow appears in emails 01, 04, 05, and 07. By this point in the customer journey, they've potentially seen this couple in browse emails, welcome emails, and now cart emails. The visual has zero stopping power left.

The test variants (T1-T3) use no couple imagery at all — just the Rugiet wordmark and clean text. They read as more trustworthy.

---

## The test variants are better than the main flow

The three test emails in the "Cart Test" frame are cleaner, more focused, and more in line with both EMB best practices and Rugiet's own brand guidelines than any of the 9 main flow emails.

| Quality | Test emails | Main flow |
|---|---|---|
| CTAs per email | 1 | 2-3 |
| Discount placement | Single line at bottom | Banner + hero + body + CTA |
| Imagery | None (clean text) | Same recycled couple |
| Tone | Provider-focused, matter-of-fact | Sales-y urgency |
| Voice match to TOV | Strong ("Your provider is waiting") | Weak ("Don't miss out") |

**Test email highlights:**
- T1 ("Your provider is waiting"): leads with the clinical process, positions the discount as an afterthought. Per TOV: "Let the product speak."
- T3 ("Here's what the visit looks like"): explains the three-step process (questions → provider review → prescription ships). This addresses the actual objection blocking purchase — "What happens if I click this button?" — rather than offering another discount.

The test variants align with EMB §17 (Cart Abandonment Design): "The most effective cart abandonment emails do not just remind. They either address specific objections (Tuft and Needle), use founder-personal tone (Ugmonk), deploy scarcity without discounting (Alo Yoga), or lead with personality."

---

## Recommended 5-email structure

The CEO's proposed restructure is sound and aligns with EMB best practices. Here it is with layered guidance.

### Email 1: Cart reminder (Hours 2-4)

**Based on:** Test email T1 ("Your provider is waiting") — promoted from test to lead position
**Action:** Use the test email format as the primary, strip the discount

The first cart email should be a simple reminder. Per EMB §4: "Email 1 (1-4h): Simple reminder. NO discount."

**Structure:**
- Subject: "Your provider is waiting" (from T1 — strong, concise, 4 words per owned-channels rule)
- Body: "You're a few questions away from a licensed provider reviewing your health privately and recommending a treatment plan — if it's right for you."
- Process clarity: "The visit happens online, on your schedule. No waiting room, no pharmacy counter, no insurance needed."
- Cart saved confirmation: "Your place is saved."
- CTA: COMPLETE VISIT
- No discount code. No banner. No coupon. Just the reminder.

**Why no discount here:** Cart abandoners are the highest-intent audience. They selected the product. A discount in email 1 signals desperation and anchors the subscriber to expect a deal. The objection at this stage is usually friction ("what does the process look like?") not price.

**Image:** None or product-only. The clean text format from the test emails is stronger than the couple imagery.

---

### Email 2: VIP / doctor credential (Day 1)

**Based on:** Email 08 ("Treatment on your terms") — promoted from position 8 to position 2
**Action:** Move up dramatically; this is the best email in the flow

The CEO is right: the doctor email is the best thing in the cart flow. It features Dr. Vipul Khanpara by name and photo, establishes that a real board-certified physician reviews every case, and frames the product as medical, not supplement. This is the single most powerful trust signal available.

**Structure:**
- Subject: "Treatment on your terms" (keep — strong, 4 words)
- Hero: keep current hero
- Lead with doctor credential: "Rugiet treatments are prescribed by a real doctor who personally reviews your case, like Dr. Vipul Khanpara — board-certified with over 20 years in Emergency Medicine."
- Doctor photo: keep (this is the one piece of unique imagery in the flow)
- Personalization angle: "With Rugiet, doctors formulate treatment specifically for you."
- CTA: GET MY CUSTOM DOSE
- No discount. This is a trust email. The doctor's face next to a coupon banner undermines the clinical credibility.

**Why position 2:** Per EMB §4 (Abandoned Cart): "Email 2 (24h): Address objections. Reviews, shipping, guarantee." The doctor email addresses the core objection for a prescription product: "Is this legit? Is a real doctor involved?" It belongs at Day 1, not Day 8.

**Image:** Dr. Khanpara photo (unique to this email, not the recycled couple)

---

### Email 3: Built around you (Day 2-3)

**Based on:** Merge of emails 03, 06, 08 (personalization angle), and 09 (ingredient breakdown) — the four "tailored to you" emails collapsed into one
**Action:** Consolidate; use email 09's visual format with the tumbling product shots

The CEO's direction is right: the "Personalize your approach" version (email 09) with the tumbling product shots is the strongest frame for this consolidated email.

**Structure:**
- Subject: "Built around you" (3 words — per owned-channels rule)
- Hero: tumbling product shots from email 09 (visually distinctive)
- Headline: "Personalize your approach" or "Built around you"
- Lead: "One formula doesn't fit every man. Ready™ is compounded to your specifications, so you get a treatment that matches how your body actually works."
- Feature grid:
  - Three ingredients: sildenafil, tadalafil, and apomorphine
  - Doctor-designed: custom-compounded in the U.S.A.
  - Customized doses: supports personalized performance
  - Rapid onset: works in as little as 15 minutes* (**fix the "as fast as" phrasing**)
- CTA: GET STARTED
- No discount. This is a trust/education email.

**Key fixes:**
- Fix all "Ready®" to "Ready™"
- Fix "as fast as" to "as little as"
- One CTA only (currently email 09 has 3)
- Drop the "Save 20%" section at the bottom — let the product sell itself

**Image:** Tumbling product shots (email 09's format). Not the couple.

---

### Email 4: Social proof (Day 4-5)

**Based on:** Consolidation of emails 01, 04, and 07 testimonials — curated and cleaned
**Action:** Build new from the best compliant testimonials; introduce CART15 with a stated expiry

This is the first email in the flow that carries a discount. Four trust-building emails have preceded it. Now social proof + an offer is the natural conversion pair.

**Structure:**
- Subject: "500,000 men made the switch" (5 words)
- Hero: "Over 500,000 men trust Ready™"
- Curated testimonials (4-5 max):

**Testimonials to keep (after compliance cleaning):**
- "I am harder than I have been in years." (from email 04 — specific, credible)
- "The comments from my wife made it the absolute perfect evening." (from email 04 — partner angle, warm, per CEO preference)
- "One of the few that has consistently worked for me. The product speaks for itself; very dependable results, highly effective & easily digested." (from email 07 — **fix "dew" typo to "few"**)
- "Rugiet has changed my life. My wife and I now enjoy a wonderful love life once again." (from email 07 — relationship-focused)
- "Other brands work, but Rugiet definitely works much better and faster (and tastes better)." (from email 07 — **CEO specifically likes the "tastes better" detail**)

**Testimonials to remove:**
- "IT WORKED WELL... LIKE REALLY WELL... 10/10 would recommend to anyone who wants stronger erections, longer performance time, addicted playmates." — **Remove entirely.** "Addicted playmates" is off-brand, potentially offensive, and compliance-risky.
- Any testimonial with efficacy absolutes ("works every time," "guaranteed")

**Discount in this email:**
- Banner: "Save 15% with code CART15"
- Body: "Your code CART15 expires in 48 hours." — **stated, enforced expiry**
- CTA: TRY FOR YOURSELF

**Each testimonial needs:** "Customer's results have not been independently verified. Individual results may vary."

**Image:** Multiple different men/couples — this email needs visual diversity most

---

### Email 5: Last chance (Day 6-7)

**Based on:** New closer email — the only place "last chance" is permitted
**Action:** Build new with real urgency and real expiry

This is the only email that can use "last chance" language because it is, in fact, the last email. If the 20% tier is kept, it lives here and only here. If it's cut (and there's a strong argument for cutting it — see below), then this email is the final CART15 with a hard deadline.

**Structure (if keeping 20% tier):**
- Subject: "This code expires tomorrow" (4 words)
- Hero: direct, no imagery needed — text-focused urgency
- Body: "We've held your spot. We've shown you the doctor, the science, the results. Now it's your call."
- Offer: "Save 20% with code CART20. This code expires [specific date/time]."
- "After tomorrow, this code is gone. No extensions."
- CTA: COMPLETE YOUR ORDER
- **The code must actually expire.** If Braze cannot enforce code expiry, use a time-limited offer page instead.

**Structure (if cutting 20% and staying at 15%):**
- Subject: "Your 15% expires tomorrow"
- Same structure, CART15, real expiry
- This is the cleaner option because it doesn't reward waiting

**The case for cutting 20% entirely:**
- Cart abandoners are highest-intent — they often need a nudge and a trust signal, not a deeper discount
- 20% for the most engaged audience while welcome gets 15% is backwards pricing
- Every 20% code that converts teaches that customer to abandon cart again next time
- Per EMB §4: "Small incentive if margins allow. First-time abandoners only."

**Recommendation:** Cap at 15% (CART15) across the entire cart flow. Reserve any deeper discounts for win-back flows targeting lapsed customers (lower intent, higher incentive needed). If 20% is kept, it appears only in this final email, framed as final, with a hard expiry.

**Image:** Product shot or clean text format. Not the couple.

---

## Revised flow at a glance

| Position | Timing | Job | Discount? | Source |
|---|---|---|---|---|
| 1 | Hours 2-4 | Cart reminder | NO | Test email T1 |
| 2 | Day 1 | VIP / doctor trust | NO | Email 08 (promoted) |
| 3 | Day 2-3 | Built around you | NO | Merge of 03/06/09 |
| 4 | Day 4-5 | Social proof + offer | CART15 (15%) with stated expiry | Curated from 04/07 |
| 5 | Day 6-7 | Last chance (real) | CART15 or CART20 with hard expiry | New |

**Offer concentration:** Only emails 4 and 5 carry a discount. Emails 1-3 are trust/process emails with no coupon.

---

## Cross-flow discount architecture (systemic issue)

This analysis cannot be complete without addressing the cross-flow discount problem the CEO raised. The cart flow doesn't exist in isolation — the same subscriber may be in browse, welcome, and cart flows simultaneously.

### Current state (broken)

| Flow | Code | Discount | Problem |
|---|---|---|---|
| Browse | RUGIET10 | 10% | Low-intent audience gets lowest discount (okay) |
| Welcome | 5XFAST | 15% | Medium-intent audience gets medium discount (okay) |
| Cart (early) | CART15 | 15% | High-intent audience gets same as welcome (confusing) |
| Cart (late) | CART20 | 20% | Highest-intent audience gets deepest discount (backwards) |

### Recommended state

| Flow | Code | Discount | Logic |
|---|---|---|---|
| Browse | RUGIET10 | 10% | Lowest intent → smallest nudge |
| Welcome | 5XFAST | 15% | Medium intent → moderate incentive |
| Cart | CART15 | 15% | High intent → same incentive, trust-focused |
| Cart (last email only, if kept) | CART20 | 20% | Final chance only, hard expiry, first-time abandoners only |

### Required Braze configuration

**Open question from CEO: "Do we have suppression rules so nobody sees two codes in the same week?"**

This must be verified and implemented:

- [ ] **Flow priority waterfall:** Cart abandon > Welcome > Browse abandon. If a subscriber enters cart flow, suppress browse and welcome sends.
- [ ] **Code mutual exclusion:** A subscriber should never receive CART15 and 5XFAST in the same 7-day window.
- [ ] **First-time abandoner flag:** If 20% is kept, it should only fire for first-time cart abandoners, not repeat abandoners who have already received CART20.
- [ ] **Code expiry enforcement:** Verify that expired codes actually return an error at checkout, not a silent success.
- [ ] **Re-entry suppression:** If a subscriber completes purchase from the cart flow, suppress remaining cart emails immediately (this should already exist but verify).

---

## Test variant assessment

The three test emails in the "Cart Test" frame are being tested against the first three main flow emails. Assessment:

### Test T1: "Your provider is waiting"
**Verdict: Significantly better than Cart 01**

Cart 01 leads with a stat (85% confidence), a discount banner, and urgency language ("this offer won't last"). Test T1 leads with "Your provider is waiting" — a process-focused nudge that addresses the actual friction point (completing the consultation) without discounting.

Per TOV: "assume the sale. Our tone says: of course you'd address this." T1 does exactly this. Cart 01 says "please come back, here's a coupon."

**Recommendation:** Replace Cart 01 with T1 as the permanent email 1.

### Test T2: "We've held your place"
**Verdict: Good follow-up cadence for T1**

Clean, simple, one CTA. "Come back when you're ready" is the right tone per TOV — confident, not desperate. The "consultaiton" typo in the subject line (visible in the inbox preview) needs fixing.

**Recommendation:** Keep as a 24h follow-up if email 1 doesn't convert, or merge the best elements into email 1.

### Test T3: "Here's what the visit looks like"
**Verdict: Strong process-transparency email**

This email answers "What happens next?" — three steps, all online, all private. Per EMB §4 (Cart Abandonment): "Treat cart abandonment as a conversation, not a reminder. Address specific objections in sequence." The objection this email addresses is "I don't know what happens if I click the button."

**Recommendation:** This content belongs in the recommended 5-email flow, either integrated into email 1 or as a standalone position. The three-step process explanation is more conversion-relevant than any of the personalization emails.

---

## Testimonial audit

### Testimonials to remove immediately

| Source email | Quote | Reason |
|---|---|---|
| Cart 04 | "...stronger erections, longer performance time, addicted playmates" | "Addicted playmates" is inappropriate, off-brand, and creates compliance risk |
| Cart 07 | "ONE OF THE DEW THAT HAS CONSISTENTLY WORKED FOR ME" | Typo — "DEW" should be "FEW." Fix before re-publishing |

### Testimonials to keep (after cleaning)

| Quote (cleaned) | Why it works |
|---|---|
| "I am harder than I have been in years." | Specific, credible, no absolutes |
| "The comments from my wife made it the absolute perfect evening." | Partner angle, warm, specific moment |
| "One of the few that has consistently worked for me. Very dependable results, highly effective & easily digested." | **Fix typo.** Then strong — "one of the few" is honest framing |
| "Rugiet has changed my life. My wife and I now enjoy a wonderful love life once again." | Relationship-focused, emotional without being hyperbolic |
| "Other brands work, but Rugiet definitely works much better and faster (and tastes better)." | CEO likes the "tastes better" detail — specific, memorable, differentiating |
| "There is definitely a difference with Rugiet. The comments from my wife made it the absolute perfect evening." | Partner angle, specific |

### Testimonial selection criteria going forward

Per compliance.md and CEO direction, every testimonial in any Rugiet flow should be:
- **Specific:** names a detail (partner reaction, duration, comparison to alternatives)
- **Warm:** reads like a real person, not a marketing script
- **Compliant:** no efficacy absolutes ("guaranteed," "every time," "miracle"), conditional framing
- **Typo-free:** basic QA before publishing
- **No efficacy absolutes:** "works great" is fine; "works every single time" is not
- **Disclaimered:** "Customer's results have not been independently verified. Individual results may vary."

---

## Additional best practice gaps

### 1. No cart contents shown

None of the 9 emails show the subscriber what's actually in their cart. Per EMB §4 (Abandoned Cart): the first email should be a "simple reminder" with cart contents. The product name, image, and price should be dynamically pulled from Braze.

### 2. No objection-handling email

Per EMB §4: "Email 2 (24h): Address objections. Reviews, shipping, guarantee." None of the 9 emails explicitly address the common objections for a prescription ED product:
- "Is this safe?"
- "What if it doesn't work for me?"
- "What does a real doctor think?"

Email 08 (the VIP/doctor email) partially addresses the last one, which is why promoting it to position 2 is critical.

### 3. Subject lines exceed 6-word rule

Per owned-channels.md: "Six words or fewer wherever possible."

| Current | Words | Recommended |
|---|---|---|
| Don't miss out on your exclusive 15% savings | 9 | Your cart is waiting |
| You're about to miss out on 15% off | 9 | Ready is waiting |
| Confidence is in your cart. Save 20% when you purchase. | 10 | Your dose is ready |
| Get Ready™. Make moves tonight. | 5 | Make moves tonight (4) |

### 4. No send-time optimization

The flow has no documented send-time strategy. Per EMB §4: "Cart abandonment: Send within 1 hour, then 24 hours, then 72 hours." The recommended cadence for 5 emails:
- Email 1: 2-4 hours after abandon
- Email 2: 24 hours (Day 1)
- Email 3: 48-72 hours (Day 2-3)
- Email 4: Day 4-5
- Email 5: Day 6-7

---

## Immediate action items (do first)

1. **Remove the "addicted playmates" testimonial** — this is live and a brand risk
2. **Fix the "dew/few" typo** — published typo visible to customers
3. **Fix the 15%/20% contradiction in email 07 body text** — says "save 15%" when the code is 20%
4. **Fix all "Ready®" to "Ready™"** — appears in emails 04, 05, 06, 09 (4 emails)
5. **Fix "as fast as" to "as little as"** — emails 01 and 09
6. **Move "Last chance" to the actual last email** — currently at position 4 of 9
7. **Verify Braze suppression rules** — confirm cross-flow code collision prevention exists; if not, build it immediately

---

## Compliance checklist for revised flow

- [ ] Standalone "Ready" uses ™ on first mention only (never ®). Full "Rugiet Ready" uses ® on first mention only. After first mention, no symbol needed. Per trademark-usage.md.
- [ ] Onset language is "works in as little as 15 minutes" everywhere
- [ ] No "Last chance" except in the final email
- [ ] Discount code percentages match between banner, body, and CTA in every email
- [ ] "Addicted playmates" testimonial removed
- [ ] "Dew" typo fixed to "few"
- [ ] Every testimonial carries the standard disclaimer
- [ ] No emotion + discount blending in headlines
- [ ] One CTA per email
- [ ] Subject lines 6 words or fewer
- [ ] Stated expiry on every discount offer
- [ ] FDA compounding disclaimer in every footer
- [ ] Conditional verbs on all benefit claims

---

## Change log

| Date | Change | Author |
|---|---|---|
| 2026-06-13 | Initial analysis incorporating CEO feedback, EMB best practices, rugiet-copywriting compliance/tone/channel rules | lifecycle-creative |
