# Longevity Launch — Flow Review + Pressure Test

**Date:** 2026-06-15
**Launch target:** Wednesday 2026-06-17
**Flows reviewed:** Welcome (3 emails), Questionnaire Abandon (3 emails), Cart Abandon (3 emails)
**Status:** Pre-launch review — not yet mapped to playbook (known gap)
**References:** Ready flow analyses (06-13-26), Email Marketing Bible v2.0, Rugiet Copywriting Skill, Lifecycle Conversion Flow Framework

---

## Executive summary

The Longevity flows are visually on-brand and the copy is in the correct optimization register. No compliance showstoppers. But when tested against the Ready playbook and EMB framework, structural gaps emerge — particularly in the Welcome series (too thin) and Questionnaire Abandon (no job differentiation between emails). The Cart flow is the most structurally sound of the three.

**Verdict: Ship Wednesday with must-fixes applied. Build the post-launch roadmap now so the team knows what's coming.**

---

## Part 1: Must-fix before Wednesday

These are blocking items. All are quick.

| # | Flow | Issue | Fix | Owner |
|---|---|---|---|---|
| 1 | Welcome 1 + 3 | `[CODE]`, `[XX%]`, `xx/xx/xxxx` placeholders | Fill in actual values | Lifecycle |
| 2 | All 9 emails | "Performance Medicine For Men™" in footer | Remove ™ per trademark-usage.md — this phrase gets no symbol | Design |
| 3 | Questionnaire 2 | CTA "FINISH MY ASSESSMENT" in all caps | Sentence case: "Finish my assessment" | Design |
| 4 | Welcome 2 | "NAD+ powers energy production" / "Glutathione defends against oxidative stress" | Add conditional verbs: "helps power" / "helps defend" | Copy |
| 5 | All cart footers | ©2025 | Update to ©2026 | Design |

---

## Part 2: Pressure test by series

### A. Welcome Flow — 3 emails

#### What's here

| # | Headline | Job |
|---|---|---|
| 1 | "Let's get you to optimal levels" | Hook + product overview + discount |
| 2 | "Treat the systems, not the symptoms" | Mechanism education |
| 3 | "Normal is not enough" | Process transparency + offer close |

#### What works

- **Optimization register is correct throughout.** "Let's get you to optimal levels," "Treat the systems, not the symptoms," and "Normal is not enough" all frame capability, never deficiency. This is exactly right per the longevity positioning rules.
- **Product descriptions use conditional language well.** "Supports," "Helps," "Signals your body to produce" — the compliance audit on Ready found "as fast as" and "miracle" violations everywhere. The longevity team clearly learned from that.
- **Email 2's mechanism structure is strong.** Three systems (Hormones, Metabolism, Cellular health) mapped to specific products with photos. This is the kind of educational depth that belongs in a longevity welcome flow.
- **Email 3's process timeline** (Questionnaire → Provider review → Receive treatment) is a proven converter. The Ready cart test variant T3 ("Here's what the visit looks like") was the strongest email in that entire flow. Good to see it here in the welcome series.

#### Where it falls short vs. the playbook

**The series is too thin.** The Ready welcome was optimized from 11→8 emails. EMB §4 recommends 4-6 emails for a welcome series. This flow has 3. That means several proven conversion jobs are completely absent:

| Missing job | Why it matters | Playbook reference |
|---|---|---|
| **No reply prompt in email 1** | Replies are the strongest signal for Gmail primary tab placement. Every Ready flow analysis flagged this. | EMB §7: "Ask for replies in welcome email." |
| **No dedicated trust/doctor email** | The doctor email was the single best-performing email in the Ready cart flow. It was promoted from position 8 to position 2 because it addresses the core objection: "Is this legit?" | Ready Cart analysis: "The VIP/doctor email is the best thing in the cart flow." |
| **No social proof email** | Expected for launch (no longevity testimonials yet), but there's no placeholder slot for when they arrive. The Ready welcome consolidates all social proof into one strong email at position 5. | EMB §4: "Email 3 (Day 4): Social proof." |
| **No personalization email** | "Doctor-designed, built around your biology" is the strongest Rugiet differentiator for any Rx product. The Ready welcome dedicates email 6 to this. | Owned-channels.md: "TRT: Personalization first." Applies equally to longevity. |
| **No preference center link** | Deliverability hygiene. Every email past position 4 should offer frequency control. | EMB §4: "Email 6 (Day 14): Set expectations + preference centre link." |
| **No behavioral branching** | If a subscriber clicks in email 1, they should enter a shorter path rather than receiving all emails. The current flow is a straight-line sequence. | EMB §4, Ready Welcome analysis §7 |

**Offer architecture is undefined.** Two of three emails have discount placeholders (`[CODE]`, `[XX%]`) but there's no documented:
- What the code and percentage actually are
- Which emails carry the offer vs. which are trust emails
- Whether the code has an expiry, and if so, whether it's enforced

Per the Ready playbook, the welcome offer architecture was:

| Email | Job | Discount? |
|---|---|---|
| 1 — Hook | YES (15%) | Conversion email |
| 2 — Differentiation | YES (15%) | Still converting |
| 3 — Mechanism | NO | Trust email |
| 4 — Expectation-setting | NO | Trust email |
| 5 — Social proof | YES (15%) | Social proof + offer = natural pair |
| 6 — Personalization | NO | Trust email |
| 7 — Confidence/partner | NO | Trust email |
| 8 — Closer | YES (15%) | Real urgency + expiry |

The Longevity flow has no equivalent architecture. Email 1 has a discount, email 2 doesn't (good — mechanism), email 3 has a discount. But with only 3 emails, there's no room for trust emails that don't carry a coupon. This concentrates every send around "buy now," which is the opposite of how longevity products sell. These are commitment purchases — the buyer needs education and trust before price becomes relevant.

**Multiple CTAs per email.** Welcome 1 has at least two CTA buttons (hero + mid-body), and all three emails have a "Contact us" button at the bottom. Per owned-channels.md: "One CTA per email." The Ready analyses flagged this in every flow. Keep one primary CTA; make "Contact us" a text link.

**No cadence/timing documented.** The Figma designs show email content but no send timing. Per EMB §4, the recommended welcome cadence is:
- Email 1: Immediate
- Email 2: Day 2
- Email 3: Day 4
- Email 4: Day 7
- Email 5: Day 10
- Email 6: Day 14

#### Next steps — Welcome series roadmap

**Phase 1 (ship Wednesday with 3 emails):**
- Fill all placeholders
- Fix conditional verbs in email 2
- Define and document discount code + percentage
- Strip one CTA per email, make "Contact us" a text link
- Add reply prompt to email 1: "Questions about longevity therapies? Reply to this email — our care team reads every one."

**Phase 2 (Week 1 post-launch — expand to 5-6 emails):**

| Position | Timing | Job | Discount? | Status |
|---|---|---|---|---|
| 1 | Immediate | Hook + product overview | YES | Exists — refine |
| 2 | Day 2 | Mechanism education | NO | Exists — strip discount banner if one was added |
| 3 | Day 4 | Doctor trust / clinical credibility | NO | **Build new.** Model on Ready cart email 2 (Dr. Khanpara). Name a real physician. Photo. "A licensed provider reviews your intake, designs a protocol around your biology, and monitors your progress." |
| 4 | Day 7 | Expectation-setting + process | NO | Exists (current email 3, resequenced) — strip offer, make pure trust |
| 5 | Day 10 | Social proof + offer | YES | **Build new.** Placeholder for when longevity testimonials arrive. Until then, run a "results patients report" email with the Month 1/2/3 timeline from Cart email 1 + offer. |
| 6 | Day 14 | Closer + preference center | YES | **Build new.** Code with real expiry. "Your code [X] expires in 48 hours." Preference center link. |

**Phase 3 (Month 1 post-launch):**
- Add behavioral branching — subscribers who click CTA in emails 1-3 skip to offer email
- Commission longevity-specific photography (current imagery is good but will fatigue at scale)
- Build out social proof email once patient testimonials are collected
- Add compounding disclaimer to footer of all emails with benefit claims

---

### B. Questionnaire Abandon Flow — 3 emails

#### What's here

| # | Headline | Job |
|---|---|---|
| 1 | "You're almost there" | Urgency — complete your assessment |
| 2 | "Get your personalized treatment" | Value — what completion unlocks |
| 3 | "Get answers" | Simplicity — designed to be simple |

#### What works

- **The three-email count is right.** Questionnaire abandoners are low-to-mid intent — they started the intake but dropped. 3 emails is appropriate per the browse abandon framework (Ready browse: 8→4; questionnaire abandon is even lower priority than browse since these users never reached product selection).
- **"What completion unlocks" (email 2) is a smart reframe.** Instead of nagging, it flips the ask into a reward. This is the strongest concept in the flow.
- **No discount in any email.** Correct — these users haven't even seen pricing. A discount would be premature and confusing.
- **"It takes less than five minutes" time-anchoring** reduces perceived friction.

#### Where it falls short vs. the playbook

**All 3 emails do the same job.** The Ready browse flow was restructured so every email has a distinct job: intent hook → micro-commitment → doctor trust → mechanism + offer. The longevity questionnaire flow has three variations of "please come back and finish":

| Email | Headline | Actual message |
|---|---|---|
| 1 | "You're almost there" | Come back and complete your assessment |
| 2 | "Get your personalized treatment" | Come back and complete your assessment |
| 3 | "Get answers" | Come back and complete your assessment |

A subscriber receiving all 3 gets the same nudge rephrased three times. By email 3, they've either decided to come back or they've decided the message isn't relevant. Rephrasing the same ask won't change that.

Per the Ready browse analysis: "The test variants are better than the main flow" because they addressed different objections in sequence. Same principle applies here.

**No objection-handling.** Why do people drop mid-intake? Likely reasons:
1. **Time** — "I didn't have time to finish" → Email 1 addresses this ("less than five minutes")
2. **Privacy** — "I'm not comfortable sharing health details online" → **Not addressed in any email**
3. **Skepticism** — "Is this actually personalized or just a quiz that ends in 'buy this'?" → Email 2 partially addresses this
4. **Uncertainty** — "I don't know if longevity therapy is for me" → **Not addressed in any email**

The Ready browse analysis identified that the cart test variant T3 ("Here's what the visit looks like") was the strongest converter because it answered "What happens if I click this button?" That same question is the primary blocker for a questionnaire abandoner — and none of the 3 emails answer it.

**Email 3 CTA is off-register.** "TAKE BACK YOUR EDGE" is deficiency language ("take back" implies something was lost) and all caps. Per owned-channels.md: sentence case on all CTAs. Per longevity positioning rules: optimization register, never deficiency.

**No process transparency.** None of the 3 emails explain what happens between completing the questionnaire and receiving treatment. The Ready flow's strongest emails were the ones that made the medical process visible — "Your provider reviews your case," "A U.S. compounding pharmacy prepares your prescription." This transparency is even more important for longevity products, which are newer and less familiar to most men.

#### Next steps — Questionnaire Abandon series roadmap

**Phase 1 (ship Wednesday with 3 emails):**
- Fix email 3 CTA: "TAKE BACK YOUR EDGE" → "See what's possible" or "Start my assessment" (sentence case, optimization register)
- Fix email 2 CTA casing: sentence case
- Reduce to one primary CTA per email

**Phase 2 (Week 1-2 post-launch — resequence with distinct jobs):**

| Position | Timing | Job | Model |
|---|---|---|---|
| 1 | Hours after drop | **Reminder + time anchor** — "Pick up where you left off. It takes about 5 minutes." | Keep current email 1, tighten. Add: "Your answers are saved." |
| 2 | Day 1 | **Process transparency** — "Here's what happens after you complete the questionnaire." Three steps: provider reviews → protocol designed → Rx ships. | Model on Ready cart T3 ("Here's what the visit looks like"). This email needs to be built — it doesn't exist yet. |
| 3 | Day 3 | **Value + address skepticism** — "Get your personalized treatment" + privacy reassurance. "Your health data is reviewed only by your licensed provider. It's never shared, sold, or used for marketing." | Rework current email 2. Add privacy/HIPAA trust copy. |

Email 3 of the current flow ("Get answers" / "Designed to be simple") can be cut — its job overlaps with the rewritten email 1.

**Phase 3 (Month 1 post-launch):**
- Monitor conversion by email position — if email 2 (process transparency) outperforms, test moving it to position 1
- Add a Day 5-7 "what other men are choosing" email once longevity product mix data exists
- Test a micro-commitment CTA in email 2 (e.g., "See your recommended protocol" quiz-style element)

---

### C. Cart Abandon Flow — 3 emails

#### What's here

| # | Headline | Job |
|---|---|---|
| 1 | Cart reminder + timeline | Expectation-setting (Month 1 / Month 2 / Ongoing) |
| 2 | Trust + clinical credibility | Doctor-guided protocols, Rx-based care, compounding pharmacy |
| 3 | Benefits summary + offer close | Product benefits grid + hero |

All three are marked 🚧 (work in progress).

#### What works

- **The 3-email structure aligns with EMB §4.** "Email 1: Simple reminder. Email 2: Address objections. Email 3: Small incentive." This is the tightest of the three flows and closest to the playbook.
- **The timeline in email 1 is the best single element in all 9 longevity emails.** Month 1 ("subtle shifts"), Month 2 ("sustainable wellness habits"), Ongoing ("benefits compound") — this is how longevity products actually work, and pre-setting those expectations is the single most effective churn prevention tool available. The Ready flow had nothing equivalent because sexual health results are immediate. Longevity results build over months. This timeline acknowledges that honestly.
- **Email 2's trust pillars hit the right objections.** "Doctor-guided protocols (not DIY or supplements)" is the best competitive differentiation line in any of the 9 emails. It separates Rugiet longevity from the supplement aisle in one sentence.
- **Conditional language is consistent.** "Many patients experience," "Helps support," "Benefits compound" — all properly conditional.

#### Where it falls short vs. the playbook

**Email 1 leads with education, not a reminder.** Per EMB §4: "Email 1 (1-4h): Simple reminder. NO discount." The Ready cart restructure made this email extremely simple — "Your provider is waiting" + cart contents + single CTA. The longevity cart email 1 leads with a Month 1/2/Ongoing timeline, which is valuable content but is doing the wrong job at hour 2-4. The cart abandoner's first thought is "oh right, I forgot" — not "tell me what month 3 looks like."

The timeline should move to email 2 or 3. Email 1 should be a simple reminder:
- "You started your longevity consultation. Pick up where you left off."
- Dynamic product name/image from cart
- Single CTA: "Continue my consultation"

**No discount in any email — and no documented decision about it.** The Ready cart restructure defined a clear offer architecture:
- Emails 1-3: no discount (trust)
- Email 4: CART15 (15%) with stated expiry
- Email 5: CART15 or CART20 with hard expiry (final)

The longevity cart has no offer anywhere. This is either intentional (longevity margins are different, or the product sells on value not price) or an oversight. Either way, it needs to be a documented decision.

Per the Ready analysis: "Cart abandoners are the highest-intent audience. They've already browsed, selected a product, and started the purchase process." If any flow in the longevity system deserves an offer, it's cart. If the team decides against discounting, then email 3 needs a different conversion lever — urgency via provider availability ("Your provider has limited openings this week"), scarcity ("Limited enrollment for new longevity patients"), or a non-discount incentive ("Free shipping on your first month").

**No cart contents shown.** Per EMB §4: "The first email should be a simple reminder with cart contents." Dynamic product name, image, and price pulled from Braze. None of the 3 emails reference the specific product(s) the subscriber had in their cart. For longevity, this matters more than for Ready — a subscriber considering NAD+ should see NAD+ in the email, not a generic five-product benefits grid.

**Email 2's product benefit section is overwhelming.** The trust pillars at the top are strong, but below them sits a detailed benefit breakdown for 5 individual products (Glutathione, L-Carnitine, Lipo-C, Sermorelin, NAD+) with 4-6 bullet points each. That's 25+ benefit claims in a single cart abandon email.

Per EMB §5: "Write, then cut 30%." Per owned-channels.md: "One idea per email." The trust pillars are the idea — the product catalog belongs elsewhere.

**No "Questions?" or contact fallback in the hero/body.** The "Questions? Our team is here to help" block appears at the bottom of every email, which is good. But none of the cart emails offer a reply prompt or a phone number in the body copy. For a longevity purchase — which may be the subscriber's first experience with compounded injectables — a mid-email "Have questions about the process? Call us at (855) 581-9620 or reply to this email" could be a stronger conversion lever than another benefits list.

#### Next steps — Cart Abandon series roadmap

**Phase 1 (ship Wednesday with 3 emails):**
- Fix ©2025 → ©2026 in footers
- Remove ™ from "Performance Medicine For Men" in footers
- Make a documented decision on cart discount strategy (see below)
- Reduce "Questions?" to a text link, not a button-style CTA competing with primary

**Phase 2 (Week 1-2 post-launch — resequence with distinct jobs):**

| Position | Timing | Job | Discount? | Action |
|---|---|---|---|---|
| 1 | Hours 2-4 | **Simple cart reminder** — "You started your longevity consultation." Dynamic cart product. Single CTA. | NO | **Rewrite.** Move the current email 1 content (timeline) out. Replace with a clean reminder modeled on Ready cart T1 ("Your provider is waiting"). |
| 2 | Day 1 | **Trust + timeline** — Doctor-guided, Rx-based care + "Here's what the first 3 months look like" (the current email 1 timeline). | NO | **Merge** current emails 1 and 2. Keep the trust pillars from email 2. Move the timeline from email 1 here. Cut the 5-product benefit catalog — that belongs on the PDP. |
| 3 | Day 3 | **Value summary + offer** — The strongest benefits from across all products + discount with stated expiry (if using one). | Decide | **Rework** current email 3. Add a discount code with real expiry if the offer strategy is approved. If no discount, use a non-discount conversion lever. |

**Cart discount decision (needs input):**

| Option | Pros | Cons | Recommendation |
|---|---|---|---|
| A: No discount | Protects margins; longevity sells on value/commitment | Loses the conversion lever that works for Ready | Acceptable if conversion rate holds. Monitor for 2 weeks. |
| B: 10-15% in email 3 only | One discount, one email, stated expiry | Cost | **Recommended.** Aligns to Ready playbook (CART15 in email 4-5). One offer, one email, one expiry. |
| C: Escalating discount | Deeper discount in a potential email 4 | Trains bad behavior — lessons from Ready cart analysis apply directly | Do not do this. |

**Phase 3 (Month 1 post-launch):**
- Add dynamic cart contents (product name, image, price) via Braze personalization
- Implement cross-flow suppression: Cart abandon > Questionnaire abandon > Welcome. If a subscriber enters a higher-intent flow, suppress lower-intent sends.
- Add reply prompt to email 1: "Questions about longevity treatments? Reply to this email."
- Monitor email 2 length — if CTR is low, the 5-product section is the likely culprit. Test a short version (trust pillars + single featured product from cart) against the current long version.
- Add compounding disclaimer to footer per compliance.md §1

---

## Part 3: Cross-flow architecture

### Suppression / waterfall

Per EMB §3 (Waterfall Segmentation): Cart abandon > Post-purchase > Browse/Questionnaire abandon > Welcome > Promotional.

| Scenario | Rule | Implemented? |
|---|---|---|
| Subscriber enters Cart flow | Suppress Questionnaire Abandon and Welcome sends | **Verify in Braze** |
| Subscriber enters Questionnaire flow | Suppress Welcome sends | **Verify in Braze** |
| Subscriber completes purchase from any flow | Suppress all acquisition flows immediately, enter Onboarding | **Verify in Braze** |
| Subscriber is active in Welcome flow | Suppress Questionnaire sends if same product | **Verify in Braze** |

### Discount architecture

| Flow | Code | Discount | Status |
|---|---|---|---|
| Welcome | TBD | TBD | Placeholders — define before Wednesday |
| Questionnaire Abandon | None | None | Correct — too early in funnel for discounting |
| Cart Abandon | TBD | TBD | Decision pending (see above) |

**Cross-flow overlap risk (from Ready analysis):** The Ready flows had 4 different promo codes at 3 different discount levels targeting overlapping audiences, which trained subscribers to wait for the best deal. Define the longevity discount map now, before it accrues the same debt.

Recommended longevity discount map:

| Flow | Code | Discount | Logic |
|---|---|---|---|
| Welcome | LONGEV15 (example) | 15% | Medium intent → moderate incentive |
| Questionnaire Abandon | None | None | Low intent → education, not price |
| Cart Abandon (email 3 only) | LONGCART (example) | 10-15% | High intent → one offer, one expiry |

**One code per subscriber, max.** If a subscriber sees LONGEV15 in the welcome flow and later enters the cart flow, they should not see LONGCART — the welcome code should carry over. This prevents the "wait for the better deal" behavior.

### Send timing

No timing is documented for any of the 3 flows. Define now:

| Flow | Email 1 | Email 2 | Email 3 |
|---|---|---|---|
| Welcome | Immediate | Day 2 | Day 5 |
| Questionnaire Abandon | 2-4 hours after drop | Day 1 | Day 3 |
| Cart Abandon | 2-4 hours after abandon | Day 1 | Day 3 |

---

## Part 4: Compliance checklist (all 9 emails)

Run before Wednesday:

- [ ] All placeholder values filled (`[CODE]`, `[XX%]`, `xx/xx/xxxx`, `[X] days`)
- [ ] ™ removed from "Performance Medicine For Men" in all footers
- [ ] ©2025 updated to ©2026 in all footers
- [ ] Conditional verbs on all benefit claims ("helps power," "helps defend," "supports," "signals")
- [ ] All CTAs in sentence case — no all-caps buttons
- [ ] One primary CTA per email — "Contact us" converted to text link
- [ ] Subject lines reviewed for 6-word limit
- [ ] No exclamation points anywhere
- [ ] No puns or wordplay anywhere
- [ ] Longevity copy in optimization register throughout (no deficiency framing)

### Post-launch compliance (add when expanding flows):

- [ ] FDA compounding disclaimer in footer of any email with benefit claims
- [ ] "Individual results may vary" alongside any effectiveness claims
- [ ] Rugiet® first mention in body copy (or confirm logo satisfies requirement)
- [ ] Testimonial disclaimer on any future social proof ("Customer's results have not been independently verified. Individual results may vary.")
- [ ] Stated and enforced expiry on all discount offers

---

## Part 5: Voice & tone scorecard

| Dimension | Rating | Notes |
|---|---|---|
| **Optimization register** | Strong | Consistently frames upgrade/capability, never deficiency. Best-in-class for the category. |
| **Dinner-party-guy archetype** | Strong | Direct, matter-of-fact, comfortable. The copy doesn't hedge or apologize. |
| **Clinical credibility** | Strong | Product descriptions are mechanism-first. Doctor and pharmacy references feel earned. |
| **Conditional language** | Mostly good | Two mechanism claims need softening ("powers" → "helps power"). The rest is clean. |
| **Format compliance** | Mostly good | Sentence case is consistent. No exclamation points. CTA casing needs fixes. |
| **Humor / wordplay** | Clean | None present. Appropriate for lifecycle email channel. |
| **Customer mindset** | Strong | Aspirational mirror throughout. The reader is underserved by "fine," not broken by decline. |

## Part 6: Design scorecard

| Dimension | Rating | Notes |
|---|---|---|
| **Photography** | Good | Editorial, warm tones, not stock. Consistent with brand direction. |
| **Typography** | Consistent | Review font family used throughout. Clear hierarchy. |
| **Color** | On-brand | Black heroes, white body, Rugiet Orange CTAs + footer. |
| **Layout** | Clean | Good white space. Product vial imagery is distinctive to longevity. |
| **Component consistency** | Strong | Inbox Preview, Hero, Listicle, Footer reused across all 9 emails. |
| **Footer** | Needs updates | New footer design with category nav (For Sleep, For Sex, etc.) is good. Fix ™ and ©2025. |

---

## Summary: what to do, in order

### Before Wednesday (2-3 hours of work)

1. Fill all placeholders (codes, percentages, dates)
2. Remove ™ from "Performance Medicine For Men" in all footers
3. Fix ©2025 → ©2026
4. Fix "powers" → "helps power" and "defends" → "helps defend" in Welcome 2
5. Fix all CTA casing to sentence case
6. Fix Questionnaire 3 CTA from "TAKE BACK YOUR EDGE" to optimization-register phrasing
7. Document discount codes and send timing for Braze implementation
8. Verify cross-flow suppression rules in Braze

### Week 1 post-launch

9. Resequence Cart flow: simple reminder → trust + timeline → offer
10. Resequence Questionnaire flow: reminder → process transparency → value + privacy
11. Build Welcome email 3 (doctor trust) — model on Ready cart Dr. Khanpara email
12. Add reply prompt to Welcome email 1

### Month 1 post-launch

13. Expand Welcome to 5-6 emails (add social proof slot, personalization, closer with expiry)
14. Add compounding disclaimer to all email footers
15. Implement dynamic cart contents in Cart email 1
16. Commission longevity-specific photography
17. Build social proof email once patient testimonials are available
18. Add behavioral branching to Welcome flow

---

## Change log

| Date | Change | Author |
|---|---|---|
| 2026-06-15 | Initial Longevity launch flow review | lifecycle-creative |
| 2026-06-15 | Added pressure test vs. Ready playbook + EMB framework. Expanded to include next steps by series, cross-flow architecture, and phased roadmap. | lifecycle-creative |
