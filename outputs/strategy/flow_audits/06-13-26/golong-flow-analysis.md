# Go Long Email Flow Analysis — Review of Team Optimization Report

**Date:** 2026-06-13
**Source Figma:** [Go Long Conversion Series](https://www.figma.com/design/luQdtOfoEljv6TPkwegtFR/LCM-Rebrand-System?node-id=1728-2531)
**Source Notion:** [Go Long — Email Flow Optimization Report](https://app.notion.com/p/37e50c58808480299d5bec1ff4b35342)
**References:** Email Marketing Bible v2.0, Rugiet Copywriting Skill (compliance, tone-of-voice, owned-channels), Ready Welcome/Cart analyses
**Status:** Review of team recommendations — critique and additional actions

---

## Summary verdict

The team's Notion report is structurally sound and directionally correct. The recommended cuts (9→8 welcome, 9→4 questionnaire abandon, 9→5 cart abandon), the banner-stripping logic, the "last chance" discipline, and the cross-flow discount flag are all good calls backed by the same principles we applied to the Ready flows. The report is the strongest team-produced lifecycle document I've seen.

That said, there are specific gaps, a few blind spots, and several issues in the current Figma designs that the report doesn't catch. This review layers those on.

---

## Part 1: What the report gets right — keep these

1. **Expectation-setting email moved to mid-flow** — exactly right. This is the same pattern we applied to Ready's welcome flow. Honest side-effect disclosure mid-flow is the strongest conversion lever for pharma buyers.

2. **Discount banners stripped from trust emails (3, 4, 6, 7)** — correct. A coupon next to clinical content reads as desperation. Concentrating offers in emails 1, 5, and 8 is the right architecture.

3. **Questionnaire abandon cut from 9 to 4** — aggressive and appropriate. This is the lowest-intent audience. Per EMB §3: "Tier 4: No engagement 90-180 days → re-engagement flow only." Nine emails to someone who couldn't finish a form is actively damaging deliverability.

4. **Doctor email promoted to cart position 2** — consistent with the Ready cart analysis. The unresolved objection for cart abandoners is "is this legit?" not "is the price right?"

5. **"Last chance" discipline** — correctly limits urgency language to the final email only. This is non-negotiable across all flows.

6. **Copy standard: emotion and discount must be separated** — "Get confidence you can depend on. Get 15% off" violates this rule. Body copy sells the product; banner/CTA carries the offer.

7. **Testimonial standards: first name + last initial** — better than "Verified Patient." More specific, more human, more compliant.

---

## Part 2: What the report misses or gets wrong

### 2.1 Go Long is PE-first — the report doesn't enforce this strictly enough

Per CLAUDE.md, owned-channels.md, and the product positioning shortcuts: **"Go Long — PE is the marquee benefit. ED is body copy only — never in headlines, subject lines, or hero copy. Do not put 'ED' in subject lines for Go Long."**

The current Figma emails are mostly correct here — "Make sex last," "the science of lasting longer," "delay ejaculation" are all PE framing. But the report's recommended email 7 ("Confidence/partner angle") doesn't specify that this must remain PE-focused. The Ready welcome flow has a similar email, but Ready is an ED product. For Go Long, the partner angle must be framed around timing and endurance, not erections.

**Action:** Add explicit guard rail to the email 7 brief: "Partner angle must reference PE outcomes (lasting longer, confidence in timing, control) — never frame around erections or ED. ED is body copy only for Go Long."

### 2.2 "500,000+ men trust Ready" is a Ready stat, not a Go Long stat

The report's recommended email 5 uses "500,000+ men trust Ready" as the social proof anchor. This is the Ready product's number. Go Long needs its own social proof anchor — either a Go Long-specific stat or a Rugiet-wide stat ("Over 500,000 men trust Rugiet" — broader brand claim that covers both products).

**Action:** Source a Go Long-specific number (prescriptions filled, patients treated, etc.) or use the Rugiet-wide anchor. Do not borrow Ready's stat for a different product.

### 2.3 The "2-in-1" message needs the same rigor as Ready's "3 medications. 5 benefits. 1 dose."

The report recommends "'Get hard faster and last longer' must appear in every email" as the canonical Go Long tagline. This is fine directionally but needs the same precision treatment we gave Ready:

- Go Long has **2 active ingredients** (paroxetine + tadalafil)
- It addresses **2 causes** (timing control + blood flow)
- It delivers **1 dose**

**Recommended canonical line:** "2 ingredients. 2 problems solved. 1 dose." or "Two causes of PE. One prescription." — pick one and lock it in across all emails, all flows.

**Action:** Standardize a Go Long product descriptor comparable to Ready's "3 medications. 5 benefits. 1 dose." and enforce consistency.

### 2.4 Cross-product discount architecture is unaddressed

The report correctly flags the Go Long internal inconsistency (GOLONG10 in welcome vs RUGIET10 in browse abandon). But it doesn't address the broader cross-product problem:

| Product | Flow | Code | Discount |
|---|---|---|---|
| Ready | Welcome | 5XFAST | 15% |
| Ready | Cart (early) | CART15 | 15% |
| Ready | Cart (late) | CART20 | 20% |
| Go Long | Welcome | GOLONG10 | 10% |
| Go Long | Browse | RUGIET10 | 10% |
| Go Long | Cart | GOLONG15 | 15% |

A subscriber interested in both products can receive up to **6 different promo codes** across flows. This is chaotic. The systemic fix (from the Ready cart analysis) applies here too: one discount per flow, enforced expiry, suppression rules preventing code collisions within 7 days.

**Action:** Unify discount architecture across products. Consider a single brand-wide approach: one code per flow type (welcome, browse, cart) regardless of product.

### 2.5 The report says 9→8 for welcome but the Figma only shows 3 emails

The Figma frame contains only 3 welcome email designs. The report references 9 current emails being cut to 8. This means either:
- (a) 5-6 emails exist in Braze but not in the Figma design file, or
- (b) The Figma was never updated to reflect the full flow

Either way, the gap creates risk: the team is recommending restructuring emails that haven't been visually designed. The same applies to browse abandon (3 in Figma, but report references 9 being cut to 4) and cart abandon (3 in Figma, report references 9 being cut to 5).

**Action:** Before implementing the report's recommendations, conduct a full Braze audit to inventory every active Go Long email across all three flows. Map each Braze email to a Figma design (or flag as undesigned). The Figma file should be the design source of truth — if an email isn't in Figma, it shouldn't be in production.

---

## Part 3: Issues in the current Figma designs the report doesn't catch

### 3.1 Placeholder dates are visible

Welcome email 2 shows "Offer Valid through 0x/xx/2025" and email 3 shows "Offer Valid through 0x/xx/2026" — clearly placeholder text that was never replaced. If these are live, they're visible to customers. If they're drafts, they need to be flagged for QA before any send.

### 3.2 Promo code inconsistency in cart email 1

The banner says "Get 15% OFF with code GOLONG15" but the body text says "Use GOLONG at checkout to save 15%." The code is either GOLONG15 or GOLONG — they're different codes. This needs to be unified.

### 3.3 CTA "GET SOME" in cart email 3

Per tone-of-voice.md humor rules: "The reference is 70s Playboy editorial. Cultured, confident, adult." The smirk test: "would a confident fifty-year-old smirk at this or roll his eyes?" He'd roll his eyes at "GET SOME." This is college-bro register, not dinner-party-guy.

Per owned-channels.md: "No puns. No idiomatic expressions. No humor tactics. Humor dilutes credibility here."

**Replace with:** "FINISH YOUR ORDER" or "GET YOUR PRESCRIPTION" — active, specific, per channel guidelines.

### 3.4 Browse abandon language is accusatory

The report correctly flags "Don't stop" and "Don't give up" as accusatory. But the Figma shows these are currently the live designs:

| Email | Subject | Hero text | Problem |
|---|---|---|---|
| Browse 1 | "You've come this far" | "DON'T STOP" | Accusatory — implies the user is quitting |
| Browse 2 | "Don't stop halfway" | "GO ALL THE WAY" | Subject is accusatory; hero is sexually loaded |
| Browse 3 | "Time to get to the good part" | "Finish your form" | Cleanest of the three — keep this framing |

Per owned-channels.md: "No 'just checking in,' 'wanted to follow up,' or other filler." And per tone-of-voice.md: "Provocation is aimed at conventions and lies, never at the customer."

"Don't stop" and "Don't give up" aim at the customer. Replace with intent-referencing language: "You checked out Go Long for a reason" or "Your intake is saved."

### 3.5 Footer navigation inconsistency

- Welcome emails use: For Sleep / For Sex / For Weight / **For Testosterone**
- Browse email 3 uses: For Sleep / For Sex / For Weight / **For Testosterone**
- Browse email 1 uses: For Sleep / For Sex / For Weight / **For Hormones**

"For Hormones" vs "For Testosterone" needs to be unified. Per the site navigation, determine which is canonical and enforce it.

### 3.6 Copyright year is ©2025

All emails in the Figma show "©2025 Rugiet Health. All rights reserved." — should be ©2026. Minor but visible.

### 3.7 Welcome email 1 subject line violates the Go Long PE-first rule

Subject: "Make sex last, save 10%." This is fine for PE framing. But the preheader says "Save 10% on a PE treatment that does more." The preheader uses the clinical abbreviation "PE" which most men won't know. Per tone-of-voice.md: "We use words like ED, testosterone, sildenafil, serotonin the way a well-read friend uses them — conversationally, accurately."

PE is less universally known than ED. Consider "Save 10% on treatment for premature ejaculation" or "A treatment built for lasting longer" — spell it out the first time the subscriber sees it.

---

## Part 4: Specific recommendations by flow

### Welcome flow — approve report structure with modifications

The report's 8-email structure is sound. Modifications:

| Slot | Report recommendation | Modification |
|---|---|---|
| 1 | Finish On Your Terms — hook + offer | Approve as-is. Add hard expiry date. |
| 2 | What Sets Go Long Apart — differentiation | Approve. Need to design this email — it doesn't exist in Figma. |
| 3 | The Brain-Body Approach — mechanism | Approve. Strip discount banner per report. |
| 4 | Take Back Your Health — expectation-setting | Approve the move to mid-flow. Strip banner. Verify side-effect copy is medically accurate. |
| 5 | Social proof blowout | **Modify:** Do not use "500,000+ men trust Ready" — source Go Long-specific stat. |
| 6 | More Benefits, Less Commitment — personalization | Approve. Strip banner. |
| 7 | Confidence/partner angle | **Modify:** Add explicit PE-first guard rail. Partner angle must be about timing/endurance confidence, not erections. |
| 8 | Closer — pure offer with hard expiry | Approve. Verify code expiry is enforceable in Braze. |

**Add to report:** Standardize "2 ingredients. 2 problems solved. 1 dose." (or equivalent) as the canonical Go Long product descriptor.

### Browse/questionnaire abandon — approve report structure with modifications

The cut from 9 to 4 is correct. Modifications:

| Slot | Report recommendation | Modification |
|---|---|---|
| 1 | Intent-referencing hook + product hero | Approve. "You checked out Go Long for a reason" is better than "Don't stop." |
| 2 | Quiz email — low-commitment CTA | Approve. Fix the "built by sexual health experts" claim — name them or rephrase. |
| 3 | Dr. Sanchez — trust/consultation | Approve. Fix body copy per report. Verify Dr. Sanchez is a real, named Rugiet physician. |
| 4 | Mechanism + offer with expiry | Approve. **Modify:** Spell out "premature ejaculation" in full — don't assume the reader knows "PE." |

**Critical addition:** The report recommends either suppressing browse sends for welcome-flow subscribers or unifying the discount. This must be a Braze configuration item with a specific owner and deadline. It's not a copy task — it's an engineering/ops task.

### Cart abandon — approve report structure with modifications

The cut from 9 to 5 is correct. Modifications:

| Slot | Report recommendation | Modification |
|---|---|---|
| 1 | Peak Performance — cart reminder, no discount | Approve. **Modify:** Fix the promo code inconsistency (GOLONG15 vs GOLONG). |
| 2 | Doctor/clinical trust — promoted | Approve. Use the same promotion pattern as Ready cart. |
| 3 | One Dose Covers the Weekend — mechanism | Approve. **Modify:** The 36-hour window is a tadalafil feature, not a PE feature. Frame it as "be ready whenever the moment happens" not just "36 hours." |
| 4 | Social proof + offer | Approve. **Modify:** Replace "GET SOME" CTA. Collapse discount ladder per report. |
| 5 | Last Call — final offer with hard expiry | Approve. This is the only email that can say "last chance." |

---

## Part 5: Cross-flow standards the report proposes — critique

The report's Part 5 ("How to Manage Flows Going Forward") is good operational guidance. Specific critiques:

### Sequence length by intent tier — approve

| Flow | Report max | Assessment |
|---|---|---|
| Welcome | 8 emails | Reasonable. EMB recommends 4-6 for welcome series; 8 is at the upper bound but acceptable for a prescription product with more trust-building required. |
| Questionnaire abandon | 4 emails | Correct. Low-intent audiences need fewer touches. |
| Cart abandon | 5 emails | Correct. Aligns with EMB guidance (3-email standard expanded for pharma context). |

### Image direction by email type — approve with one concern

The B&W couple image rule ("Max 1 per flow, B&W treatment only") is an interesting creative constraint. It addresses the recycled-imagery problem but may create a new one: if every flow has exactly one B&W couple image, the subscriber will still recognize the aesthetic pattern across flows. Consider whether the couple image is necessary at all — the test variants in the Ready cart flow performed better with no couple imagery.

### Copy standards — approve with additions

The report's copy standards are good. Add:

- **6-word subject line rule** (per owned-channels.md) — the current Go Long subjects run long ("Go Long lets you finish on your terms" is 8 words)
- **No exclamation points** (per owned-channels.md) — verify across all Go Long emails
- **Conditional verbs on benefit claims** (per compliance.md) — "helps delay ejaculation" not "delays ejaculation"
- **Product-specific tagline locked in** — "2 ingredients. 2 problems solved. 1 dose." or equivalent, per the Ready precedent

---

## Immediate action items

### Figma / design

1. Fix placeholder dates ("Offer Valid through 0x/xx/2025") in welcome emails 2 and 3
2. Fix promo code inconsistency in cart email 1 (GOLONG15 vs GOLONG)
3. Replace "GET SOME" CTA in cart email 3
4. Update copyright footer from ©2025 to ©2026
5. Unify footer navigation: "For Testosterone" vs "For Hormones"
6. Commission flow-unique photography per the report's creative direction

### Copy / compliance

7. Spell out "premature ejaculation" in subscriber-facing copy — don't assume "PE" is universally understood
8. Add explicit PE-first guard rail to the partner angle email brief
9. Source a Go Long-specific social proof anchor — don't borrow Ready's "500,000 men" stat
10. Standardize the Go Long product descriptor line across all emails
11. Run the owned-channels.md compliance checklist on every Go Long email (conditional verbs, subject line length, single CTA)

### Braze / ops

12. Audit every live Go Long email in Braze — map to Figma designs, flag any emails live in Braze but not in the design file
13. Implement cross-flow suppression: if subscriber is active in welcome, suppress browse abandon sends
14. Verify code expiry enforcement for GOLONG10 and GOLONG15
15. Unify discount code architecture across Go Long and Ready flows — long-term project with specific owner

---

## Compliance checklist for Go Long flows

- [ ] PE is the marquee benefit in all headlines and subject lines — ED is body copy only
- [ ] Conditional verbs on all benefit claims (helps, can, designed to, supports)
- [ ] "Premature ejaculation" spelled out, not abbreviated as "PE," in subscriber-facing copy
- [ ] Product descriptor is consistent across all emails (choose and lock a canonical line)
- [ ] Social proof uses a Go Long-specific stat, not Ready's
- [ ] Onset and duration claims use "up to" and "as little as" — not absolutes
- [ ] Every testimonial has first name + last initial, specific outcome, no efficacy absolutes
- [ ] Every discount offer has a stated and enforced expiry date
- [ ] One CTA per email
- [ ] Subject lines 6 words or fewer
- [ ] No exclamation points
- [ ] No accusatory abandon language in browse/questionnaire flows
- [ ] "Last chance" only in the final email of each flow
- [ ] FDA compounding disclaimer in every footer
- [ ] Copyright year is current (©2026)

---

## Change log

| Date | Change | Author |
|---|---|---|
| 2026-06-13 | Initial review of team optimization report with critique, additional issues, and action items | lifecycle-creative |
