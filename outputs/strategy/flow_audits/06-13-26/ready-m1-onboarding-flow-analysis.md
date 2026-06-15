# Rugiet Ready M1 Onboarding Flow Analysis

**Date:** 2026-06-13
**Source:** [M1 Onboarding Emails](https://www.figma.com/design/luQdtOfoEljv6TPkwegtFR/LCM-Rebrand-System?node-id=1601-1936)
**References:** Email Marketing Bible v2.0, Rugiet Copywriting Skill (compliance, tone-of-voice, owned-channels, trademark-usage), Lifecycle Conversion Flow Framework
**Related:** [Ready Welcome](./ready-welcome-flow-analysis.md) · [Ready Cart](./ready-cart-abandon-flow-analysis.md) · [Ready Browse](./ready-browse-abandon-flow-analysis.md)
**Status:** Analysis complete — pending implementation

---

## Current state: 10 emails

| # | Email | Trigger/timing | Primary job |
|---|---|---|---|
| 1 | Order confirmed | Purchase event | Confirmation + "what happens next" |
| 2 | The Rugiet app is here | Post-purchase | App download + Sex Score quiz |
| 3 | Prescription approved | Rx event | Status update + "what to expect" + Sex Score quiz |
| 4 | Shipment on its way | Ship event | Tracking + how-to + storage |
| 5 | Ready™ has arrived | Delivery event | Dosing instructions + when to take |
| 6 | Time to put Ready to work | ~Day 1-2 post-delivery | First-dose expectations + testimonials — **"Ready®" standalone is wrong per trademark guide; should be Ready™ on first mention** |
| 7 | It's the apomorphine | ~Day 5 | Mechanism education / reinforcement |
| 8 | ONE WEEK IN | Day 7-10 | Check-in + dosing adjustment guidance |
| 9 | Get a free month of Ready | Mid-flow (currently) | Upsell: 3-month subscription — **"Ready®" standalone is wrong per trademark guide; should be Ready™ on first mention or "Rugiet Ready®" for full name** |
| 10 | Stay ready. Stay confident. | Pre-refill | Refill reminder + stats |

---

## Critical issues

### 1. 400k vs 500k social proof contradiction

Email 6 ("Time to put Ready to work") uses "Over 500k+ men have made the switch" while the CEO reports seeing "Over 400k+" in a version of this email. Every acquisition flow uses "500,000+." If any live version still says 400k, it contradicts every other touchpoint the customer has already seen. This is a trust leak to paying customers — they already bought and are now seeing a lower number than what sold them.

**Fix:** Audit Braze for any live version referencing 400k. Standardize to "Over 500,000 men trust Ready" everywhere. Add to the claims sheet (see item 6 below).

### 2. Duration claim inconsistency: "24-36 hours" vs "up to 36 hours"

The Rx-approved email (3) says: "85% of Rugiet Ready users report feeling effects in 15 minutes or less.* Effects typically last 24-36 hours."

Every upstream flow uses "up to 36 hours." Stating "24-36 hours" is a different claim — it implies a guaranteed minimum of 24 hours, which is not substantiated.

| Source | Duration language |
|---|---|
| Welcome flow | "up to 36 hours" |
| Cart flow | "up to 36 hours" |
| Browse flow | "up to 36 hours" |
| Rx-approved email | "24-36 hours" ← inconsistent |
| Delivered email | "last up to 36 hours" ← correct |

**Fix:** Change to "up to 36 hours" in the Rx-approved email. Add to claims sheet.

### 3. The 85% stat means two different things

| Location | 85% claim |
|---|---|
| Welcome flow (email 04) | "85% of men feel more confident in bed" |
| Rx-approved email (3) | "85% of Rugiet Ready users report feeling effects in 15 minutes or less" |
| Refill email (10) | "85%" (appears as stat without full context) |

These are two completely different claims sourced from the same number. A customer seeing both will notice the inconsistency. One stat measures confidence, the other measures onset speed. Pick one canonical phrasing, cite one source, and enforce it.

**Fix:** Develop a claims sheet with one canonical phrasing per stat, one disclaimer, enforced across all flows. This is a systemic issue that affects every product.

### 4. Two over-claims requiring immediate fix

**Email 6** — "Making Ready more fast, effective and reliable than every other generic ED med"
- This is a superiority claim against the entire drug class
- Requires head-to-head clinical evidence that doesn't exist
- "More fast" is also bad grammar in a headline position
- Per compliance.md §4: comparative claims must be substantiated; "stronger," "better," "faster" require trial data
- **Fix:** Change to "Works differently than generic ED meds" — factual differentiation without superiority claim

**Email 6 testimonial** — "IT WORKS EVERY TIME"
- Efficacy absolute — prohibited per testimonial standards
- Per compliance.md §2: avoid "guaranteed," "always works," and similar certainty language
- **Fix:** Remove or replace with a testimonial that doesn't make absolute efficacy claims

### 5. Upsell email lands too early — gate behind check-in

The 3-month upgrade email ("Get a free month of Ready") currently arrives mid-flow, before the customer has finished validating the product. Asking someone to triple their commitment before the week-1 check-in has resolved is asking too soon.

**Recommended gating:**
- Move upsell to ~Day 21 (after check-in window closes)
- Only send to subscribers who did NOT contact support with problems during the check-in period
- Pitched after a good first month, "free month if you go quarterly" converts better
- Keep "Prefer monthly? No problem" — this is good no-pressure framing

### 6. Three overlapping education emails need merging

Emails 5 (delivered/how-to), 6 (first-dose expectations), and 7 (apomorphine) share heavy content overlap:

| Content block | Email 5 (delivered) | Email 6 (first dose) | Email 7 (apomorphine) |
|---|---|---|---|
| Sublingual instructions | ✓ | ✓ | |
| Onset timing (15 min) | ✓ | ✓ | |
| Duration (36 hours) | ✓ | ✓ | |
| "Fast onset, long duration" | ✓ | ✓ (headline) | |
| Apomorphine mechanism | | | ✓ |
| Brain + body angle | | ✓ | ✓ |

Emails 5 and 6 arrive close together and cover the same material. Merge them: the delivered/how-to email absorbs the "fast onset, long duration" block from email 6. Let the apomorphine email stand alone later as "you made a smart choice" reinforcement.

### 7. Sex Score quiz appears 3 times

The quiz/Sex Score CTA appears in:
- Email 1 (order confirmed)
- Email 2 (app email)
- Email 3 (Rx approved)

Once is a feature, three times is annoying. Keep it only in the app email (2) where it belongs — the quiz is a product feature of the app, not a standalone acquisition tool at this stage.

### 8. Stock doctor photo

The Rx-approved email uses a stock doctor image. Rugiet has real physicians (Dr. Khanpara, Dr. Sanchez) with real photos. A paying customer receiving a "prescription approved" email with a stock photo undermines the clinical trust that the cart flow's Dr. Khanpara email just built.

**Fix:** Replace with a real Rugiet physician photo. Use Dr. Khanpara (CMO) or another named physician from the medical advisory board.

### 9. Apomorphine email names Viagra and Cialis

Email 7 says: "Viagra, Cialis, and every generic sildenafil or tadalafil you've used work the same way: they increase blood flow."

Per compliance.md §4: naming competitors is prohibited — "naming competitors (e.g., Viagra, Cialis) or saying Rugiet products definitively work 'better' or are 'safer' than other products without head-to-head data."

The current usage is informational/factual rather than comparative ("they work the same way" is not a superiority claim), but it's borderline. Safer phrasing: "Traditional ED medications — generic sildenafil and tadalafil — work the same way: they increase blood flow."

---

## Recommended sequence: 10 → 9 emails

| # | Email | Timing | Change |
|---|---|---|---|
| 1 | Order confirmed | Purchase event | Remove Sex Score quiz CTA. Keep as confirmation only. |
| 2 | The Rugiet app | Post-purchase | Keep Sex Score quiz here only. |
| 3 | Rx approved | Rx event | Fix "24-36 hours" → "up to 36 hours." Fix 85% stat to canonical phrasing. Remove Sex Score quiz. Swap stock doctor for real physician. |
| 4 | Shipped | Ship event | Keep as-is. |
| 5 | Delivered + first dose (merged) | Delivery event | Merge current emails 5+6. Absorb "fast onset, long duration" into the delivered email. Add SMS companion. |
| 6 | Apomorphine | ~Day 5 | Keep as standalone. Review Viagra/Cialis naming. Fix "reliable" → conditional. |
| 7 | Check-in | Day 7-10 | Keep as-is. This is a strong email. |
| 8 | Upsell (gated) | ~Day 21, engagement-gated | Move from mid-flow to post-check-in. Only send to subscribers who did not contact support. Keep "Prefer monthly? No problem." |
| 9 | Refill | T-minus 7 days | Keep. Fix 85% stat to canonical phrasing. |

**Emails merged:** 1 pair (delivered + first dose → single delivered/how-to + expectations email)
**Emails moved:** 1 (upsell: mid-flow → Day 21, engagement-gated)
**Quiz removed from:** 2 emails (order confirmed, Rx approved — kept only in app email)

---

## Immediate flips — fix before the next send

| Email | Issue | Fix | Severity |
|---|---|---|---|
| 6 | "Making Ready more fast, effective and reliable than every other generic ED med" — superiority claim + bad grammar | Change to "Works differently than generic ED meds" | Compliance — urgent |
| 6 | "IT WORKS EVERY TIME" testimonial — efficacy absolute | Remove or replace | Compliance — urgent |
| 3 | "Effects typically last 24-36 hours" — inconsistent with "up to 36 hours" everywhere else | Change to "up to 36 hours" | Compliance — urgent |
| 3 | "85% report feeling effects in 15 minutes or less" — different claim than "85% feel more confident" | Pick one canonical phrasing, enforce everywhere | Claims consistency — urgent |
| 6 | "Over 400k+ men" (if live) vs "500,000+" everywhere else | Standardize to "Over 500,000 men trust Ready" | Claims consistency |
| 3 | Stock doctor photo | Replace with real Rugiet physician | Trust |
| 1, 3 | Sex Score quiz in order confirmed + Rx approved emails | Remove from both — keep only in app email | UX (3x is annoying) |
| 6, 9 | "Ready®" used standalone in email titles/hero | Per trademark-usage.md: standalone "Ready" gets ™ on first mention only, never ®. "Rugiet Ready®" for full product name. | Trademark |
| 6 | "Ready®" preheader: "How Ready® works..." | Same rule — standalone "Ready" never gets ® | Trademark |
| 7 | "Ready®" in "making Ready® a fast-acting and reliable option" | Same rule | Trademark |

---

## Systemic action: develop a claims sheet

This analysis exposes a cross-flow problem that no single flow fix can solve. The 85% stat, the 500k stat, the 36-hour duration, and the 15-minute onset all appear in different forms across different flows with different phrasings.

**Required:** A canonical claims sheet with:
- One phrasing per stat
- One disclaimer per stat
- Source citation
- Enforced across all flows, all products

| Claim | Canonical phrasing | Disclaimer |
|---|---|---|
| Social proof anchor | "Over 500,000 men trust Ready" | None required (factual count) |
| Onset | "Works in as little as 15 minutes" | "*on average, after medication dissolves. Based on an internal survey..." |
| Duration | "Up to 36 hours" | "Individual results may vary" |
| Confidence stat | TBD — pick one: "85% feel more confident" OR "85% report effects in 15 minutes" | Source citation required |
| Product descriptor | "3 medications. 5 benefits. 1 dose." | None (factual) |

**This claims sheet should live in the rugiet-copywriting skill references** alongside compliance.md and trademark-usage.md, loaded on every drafting task.

---

## Compliance checklist for revised onboarding flow

- [ ] No superiority claims without head-to-head data ("more fast, effective and reliable" removed)
- [ ] No efficacy absolutes in testimonials ("IT WORKS EVERY TIME" removed)
- [ ] Duration language is "up to 36 hours" everywhere — not "24-36 hours"
- [ ] 85% stat uses one canonical phrasing everywhere
- [ ] Social proof anchor is "Over 500,000 men" — not "400k+"
- [ ] Sex Score quiz appears only in the app email
- [ ] Stock doctor photo replaced with real physician
- [ ] Upsell email gated behind check-in (Day 21, support-engagement filtered)
- [ ] Delivered + first-dose emails merged
- [ ] Standalone "Ready" uses ™ on first mention only (never ®). Full "Rugiet Ready" uses ® on first mention only. After first mention, no symbol needed. Per trademark-usage.md.
- [ ] "Performance Medicine For Men" in footer carries no ™ or ® symbol — pending, contested per trademark guide
- [ ] Viagra/Cialis naming in apomorphine email reviewed for compliance
- [ ] Conditional verbs on all benefit claims

---

## Change log

| Date | Change | Author |
|---|---|---|
| 2026-06-13 | Initial analysis incorporating CEO feedback, compliance review, and claims consistency audit | lifecycle-creative |
