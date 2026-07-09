# Decisions Log

When a session produces a durable insight, calibration, or rule that should outlive the conversation, write it here. The lifecycle-creative and future agents read this freely — so anything you write becomes part of the working context for every future session.

Format: short, dated entries. One decision per entry.

---

## 2026-MM-DD — [Title of the decision]

**Context:** [What were we doing when this came up?]
**Decision:** [What did we decide?]
**Why:** [The reasoning — the most important field. Future sessions will respect the decision more if they understand why.]
**Implications:** [What does this change going forward?]

## 2026-06-04 — IAM templates are reusable scaffolding, not campaign outputs

**Context:** Built the first single-panel IAM (Go Long upgrade) and realized the HTML was living in `braze/iam/` alongside the carousel template, mixing reusable infrastructure with campaign-specific content.

**Decision:** `braze/iam/` holds only generic, reusable templates with placeholder copy. Campaign-specific IAMs (real product names, real copy, real offer lines) go to `outputs/creative/{date}_{brief-name}/iam.html` alongside a `notes.md`. The design-system skill's `references/in-app-patterns.md` documents which templates exist, when to use each, and the agent workflow for forking a template into a campaign output.

**Why:** Without this separation, the lifecycle-creative agent has to guess which files in `braze/iam/` are templates vs. past campaigns. That ambiguity compounds as more IAMs get built. Clean separation means the agent always knows: read from `braze/iam/` for structure, write to `outputs/creative/` for the deliverable.

**Implications:**
- New IAM templates go in `braze/iam/` with generic placeholder content only.
- The agent workflow for IAM briefs: identify template → fork to outputs → write campaign copy → notes.md.
- `in-app-patterns.md` is the bridge reference that tells agents what templates exist and how to use them.

## 2026-06-13 — Touchpoint hierarchy is the canonical flow structure

**Context:** Audited Ready welcome, cart abandon, browse abandon, and Go Long flows end-to-end. Found inconsistent touchpoint counts, duplicated messaging jobs, and offer placement that contradicted the trust arc.
**Decision:** All lifecycle conversion flows use a fixed touchpoint hierarchy: Welcome = 8 touchpoints, Browse/Questionnaire Abandon = 4, Cart Abandon = 5. Each touchpoint has a defined job and a fixed offer/no-offer designation. The full hierarchy lives in `outputs/strategy/flow_audits/06-13-26/exec-summary-flow-optimization.md`.
**Why:** Without a locked structure, flows drift — emails get added opportunistically, the same message job gets repeated across multiple touchpoints, and offer placement becomes arbitrary. A fixed hierarchy means every future product flow starts from the same blueprint.
**Implications:** New product flows must map to this hierarchy before any copy is written. Flow audits check touchpoint count and message-job assignment first.

---

## 2026-06-13 — Trust emails never carry discount banners

**Context:** Found discount banners on mechanism, expectation-setting, and personalization emails in existing flows — emails whose job is to build clinical credibility and trust.
**Decision:** Touchpoints designated as "trust" (mechanism, expectation-setting, personalization, partner/confidence) must never contain a discount banner, promo code, or offer CTA. Offers concentrate only in designated conversion touchpoints.
**Why:** A coupon on a side-effects-honesty email or a "built for your body" personalization email undermines the credibility the email is trying to build. The trust arc only works if it's uninterrupted by transactional pressure.
**Implications:** Every flow audit checks offer placement against the touchpoint hierarchy. If a trust email has a discount, it fails the audit.

---

## 2026-06-13 — One discount tier per flow, no escalation within a flow

**Context:** Found escalating discount patterns in cart abandon flows (15% → 20%) that trained subscribers to wait for the deeper discount.
**Decision:** A single discount tier is used throughout a flow. The discount does not increase from one email to the next within the same sequence. If a deeper discount is introduced (e.g., in the final email), it fires only for first-time abandoners and is framed as genuinely final.
**Why:** Discount escalation within a flow teaches subscribers that patience is rewarded. It erodes margins on buyers who would have converted at the first tier and creates a race to the bottom.
**Implications:** Flow builds define one discount tier upfront. QA checks that no later email in the sequence offers a higher percentage than an earlier one.

---

## 2026-06-13 — Every product must lock a canonical descriptor before any flow is built

**Context:** Found the same Ready flow using both "3-in-1" and "5-in-1" in different emails, creating a factual contradiction within a single sequence.
**Decision:** Every product must define a single canonical descriptor — a factual statement anchored to ingredients and benefits (e.g., "3 medications. 5 benefits. 1 dose.") — before any lifecycle flow is created. The descriptor appears consistently across the flow and is never abbreviated to shorthand alone.
**Why:** Inconsistent claims within a flow signal carelessness to the reader and create compliance risk. A locked descriptor eliminates drift.
**Implications:** New product onboarding checklist now requires a canonical descriptor as step 1. The descriptor is reviewed by compliance before lock.

---

## 2026-06-13 — No accusatory abandon language in any flow

**Context:** Found "Don't stop," "You left something behind," and "Don't give up" copy across browse and cart abandon flows.
**Decision:** Accusatory or guilt-based abandon language is prohibited in all flows. Use intent-referencing language instead: "You checked out [product] for a reason."
**Why:** Accusatory language positions the brand as desperate and the customer as negligent. Intent-referencing acknowledges the customer's curiosity without shame, which is consistent with the dinner-party-guy voice.
**Implications:** Compliance checklist now includes an abandon-language check. Any email containing "you left," "don't stop," "don't give up," or similar phrasing fails review.

---

## 2026-06-13 — "Last chance" language only in the actual last email of a flow

**Context:** Found "last chance" and urgency language in non-final emails across multiple flows, diluting the signal.
**Decision:** The phrase "last chance" (and equivalent urgency framing) is permitted only in the actual final touchpoint of a flow — the email after which no further emails are sent.
**Why:** If "last chance" appears in email 3 of 5, the subscriber learns the brand lies about urgency. When the real final email arrives, the language has no power. Reserving it for the true final touch preserves its credibility.
**Implications:** Copy review flags any "last chance" / "final" / "expires today" language in non-terminal emails as a hard fail.

---

## 2026-06-13 — Every discount code must have a stated and enforced expiry

**Context:** Found "for a limited time" with no date, and codes that likely still worked past their stated expiry.
**Decision:** Every discount code in every email must include a specific expiry date or window (e.g., "expires June 20" or "expires in 48 hours"). Codes must actually fail at checkout after expiry.
**Why:** Vague expiry ("limited time") creates no urgency. Codes that work past their stated expiry train subscribers to ignore deadlines. Both undermine the conversion architecture.
**Implications:** Flow builds must specify code expiry per touchpoint. Engineering/ops must confirm code enforcement at checkout before launch.

---

_(Add new entries above this line.)_
