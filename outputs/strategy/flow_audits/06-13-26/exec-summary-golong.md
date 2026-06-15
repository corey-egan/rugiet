# Go Long — Flow Optimization Executive Summary

**Date:** 2026-06-13
**Flows covered:** Welcome, Browse/Questionnaire Abandon, Cart Abandon
**Supporting analyses:** [Go Long Analysis](./golong-flow-analysis.md) · [Team Notion Report](https://app.notion.com/p/37e50c58808480299d5bec1ff4b35342)

---

## Immediate flips — fix before the next send

### Compliance / copy

| Flow | Email | Issue | Fix |
|---|---|---|---|
| Cart | 01 | Promo code mismatch — banner says GOLONG15, body says GOLONG | Unify to GOLONG15 |
| Welcome | 02, 03 | Placeholder dates visible: "Offer Valid through 0x/xx/2025" | Replace with real date or remove |
| Cart | 03 | CTA "GET SOME" — fails the smirk test, college-bro register | Replace with "Finish your order" |
| All flows | Footer | Copyright reads ©2025 | Update to ©2026 |
| Browse | 01 | Footer nav says "For Hormones" while others say "For Testosterone" | Unify |

**Total Go Long immediate flips: 5 items.** All are copy or asset swaps — no structural flow changes required.

---

## Ongoing changes — flow restructure

### Welcome: 9 emails → 8

| Slot | Job | Discount? | Key change |
|---|---|---|---|
| 1 | Hook + offer | Yes (10%) | Keep. Add hard expiry. |
| 2 | Differentiation | Yes (10%) | New email — needs design. Comparison table: why not generic? |
| 3 | Mechanism (brain-body) | No | Strip discount banner. |
| 4 | Expectation-setting | No | Move from end to mid-flow. Strip banner. Honest side-effect disclosure mid-flow is the strongest conversion lever. |
| 5 | Social proof | Yes (10%) | Source Go Long-specific stat. Do not use Ready's "500,000 men." |
| 6 | Personalization | No | Keep standalone. Strip banner. |
| 7 | Partner / confidence | No | Add PE-first guard rail — partner angle about timing/endurance, never erections. |
| 8 | Closer | Yes (10%) | Pure offer with real expiry. |

**Team report (Notion) recommendation approved** with modifications:
- Email 5 social proof must use a Go Long-specific anchor, not Ready's "500,000 men"
- Email 7 partner angle needs an explicit PE-first guard rail per owned-channels.md
- Standardize a Go Long product descriptor across all emails (see below)

---

### Browse/Questionnaire Abandon: 9 emails → 4

| Slot | Job | Key change |
|---|---|---|
| 1 | Intent-referencing hook | Rewrite. "You checked out Go Long for a reason" — not "Don't stop." |
| 2 | Quiz — low-commitment CTA | Move to slot 2. Fix "built by sexual health experts" — name them or rephrase. |
| 3 | Doctor trust (Dr. Sanchez) | Promote. Fix body copy efficacy promise. Use clinical hero image. |
| 4 | Mechanism + offer with expiry | Final email. RUGIET10 with stated expiry date. Spell out "premature ejaculation" — don't assume the reader knows "PE." |

**Emails cut:** 5
**Accusatory language removed:** "Don't stop," "Don't give up," "Don't stop halfway" replaced with intent-referencing copy

**Team report (Notion) recommendation approved** with modifications:
- Email 4 must spell out "premature ejaculation" — the abbreviation "PE" is not universally understood
- Cross-flow suppression with welcome flow confirmed as in place

---

### Cart Abandon: 9 emails → 5

| Slot | Timing | Job | Key change |
|---|---|---|---|
| 1 | Hours 2-4 | Cart reminder | No discount. Fix code mismatch (GOLONG15 vs GOLONG). |
| 2 | Day 1 | Doctor / trust | Promote to slot 2. Same pattern as Ready cart — answers "is this legit?" |
| 3 | Day 2-3 | Mechanism | Frame 36-hour tadalafil window as "be ready when the moment happens." |
| 4 | Day 4-5 | Social proof + offer | Replace "GET SOME" CTA. Single discount tier with expiry. |
| 5 | Day 6-7 | Last chance | Only email that can say "last chance." Hard expiry. |

**Team report (Notion) recommendation approved** with modifications:
- The 36-hour window is a tadalafil feature, not a PE feature — frame accordingly
- Replace "GET SOME" with an active, specific CTA per owned-channels rules

---

## Go Long-specific standards

### Product positioning: PE is the marquee

Per CLAUDE.md and owned-channels.md: "Go Long — PE is the marquee benefit. ED is body copy only — never in headlines, subject lines, or hero copy."

The current Figma emails are mostly correct ("Make sex last," "the science of lasting longer," "delay ejaculation"). Enforce this across the restructured flows, especially in the partner/confidence email (slot 7) which must frame around timing/endurance confidence, never erections.

### Product descriptor

**Canonical line: TBD — recommend "2 ingredients. 2 problems solved. 1 dose."**

Go Long has 2 active ingredients (paroxetine + tadalafil) addressing 2 causes of PE (timing control + blood flow) in 1 dose. This mirrors the Ready approach ("3 medications. 5 benefits. 1 dose.") and gives Go Long a consistent product descriptor to lock in across all emails.

**Action required:** Select and approve the canonical line. Enforce across all flows.

### Social proof anchor

**Do not borrow Ready's "500,000 men" stat for Go Long.** Source a Go Long-specific number (prescriptions filled, patients treated) or use a Rugiet-wide claim ("Over 500,000 men trust Rugiet") that covers both products.

### Discount architecture

| Flow | Code | Discount |
|---|---|---|
| Welcome | GOLONG10 | 10% |
| Browse | RUGIET10 | 10% |
| Cart | GOLONG15 | 15% |

**Braze suppression (confirmed):** When a subscriber enters a higher-intent flow, they are removed from the prior flow. Codes are not overlapping.

**Remaining:** Verify code expiry enforcement for GOLONG10 and GOLONG15.

**Note:** The team Notion report correctly flags the inconsistency between GOLONG10 (welcome) and RUGIET10 (browse) — both are 10% but use different codes. Consider unifying to a single code.

### Banner architecture

| Email type | Has discount banner? |
|---|---|
| Welcome hook (1) | Yes |
| Differentiation (2) | Yes |
| Mechanism (3) | No |
| Expectation-setting (4) | No |
| Social proof (5) | Yes |
| Personalization (6) | No |
| Partner / confidence (7) | No |
| Closer (8) | Yes |

Same architecture as Ready. Trust emails carry no coupon.

---

## Figma gap: designs vs. live emails

The Figma frame shows only 3 emails per flow, but the team Notion report references 9 existing emails per flow being cut down. This means either emails exist in Braze without corresponding Figma designs, or the Figma was never updated to reflect the full flow.

**Action required:** Before implementing the restructure, conduct a Braze audit to inventory every active Go Long email across all three flows. Map each Braze email to a Figma design. If an email is live but not in Figma, either design it or confirm it should be cut.

---

## Go Long scorecard

| Metric | Welcome | Browse | Cart |
|---|---|---|---|
| Current emails | 9 | 9 | 9 |
| Recommended emails | 8 | 4 | 5 |
| Emails cut | 1 | 5 | 4 |
| Compliance violations found | 3 | 3 | 2 |
| Immediate flips | 2 | 1 | 2 |

**Total Go Long emails:** 27 currently → 17 recommended (37% reduction)

---

## Implementation sequence

| Phase | What | Owner | When |
|---|---|---|---|
| **Phase 0** | Ship 5 immediate flips | Lifecycle + Copy | This week |
| **Phase 1** | Braze audit — map every live Go Long email to a Figma design | Lifecycle Ops | This week |
| **Phase 2** | Verify code expiry enforcement for GOLONG10 and GOLONG15 | Lifecycle Ops | This week |
| **Phase 3** | Welcome restructure (9→8) — mirror Ready pattern, design new differentiation email | Lifecycle + Design | Following sprint |
| **Phase 4** | Browse cut (9→4) + Cart restructure (9→5) | Lifecycle + Design | Following sprint |
| **Phase 5** | Commission new flow-unique photography | Creative + Brand | Parallel with Phase 3-4 |
| **Phase 6** | Select and lock Go Long product descriptor + social proof anchor | Copy + Brand | Before Phase 3 |

---

## Change log

| Date | Change | Author |
|---|---|---|
| 2026-06-13 | Initial executive summary compiled from Go Long flow analysis and team Notion report review | lifecycle-creative |
