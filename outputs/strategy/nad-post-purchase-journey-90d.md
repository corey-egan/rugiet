# NAD+ Post-Purchase Onboarding Journey — Days 0 to 90

**Date:** 2026-06-16
**Owner:** Lifecycle
**Status:** Draft for review
**Related:**
- [NAD+ Post-Purchase Strategy (Notion)](https://app.notion.com/p/37b50c58808480279dd3ed03fe72180e) — Provider-amplified hybrid approach
- [MDI Thank You Message (Notion)](https://app.notion.com/p/38150c588084803e9bfadc1b763ecbaf) — Prescription approval message with injection instructions + dosing protocol
- [Longevity Post-Purchase Strategy](../../reference/longevity/post-purchase-strategy.md) — Master framework
- [NAD+ Touchpoint Brief](../../reference/longevity/nad-plus-touchpoint-brief.md) — Therapy-specific messaging reference
- [Longevity Launch Flow Review](../strategy/flow_audits/06-15-26/longevity-launch-review.md) — Pre-launch audit

---

## Brief

**Audience**
- **Segment:** First-time customers who completed a purchase of NAD+ injections on the Rugiet digital website.
- **Estimated size:** A few hundred per week.
- **Lifecycle stage:** Onboarding (Days 0–90).

**Objective**
- **What we want them to do:** Engage with onboarding content — click, read material about their product, learn how to use it, absorb the science, and build confidence in their treatment. Ultimately, refill.
- **Success metric:** First refill rate (patients who purchase a second time). This is the only metric that matters; opens and clicks are instrumentation, not outcomes.
- **Time horizon:** 28-day and 90-day measurement windows.

**Channels**
- [x] Email — primary education and milestone channel
- [x] Push — lightweight engagement nudges and milestone acknowledgments
- [x] SMS — high-signal moments only (check-ins, refill reminders)
- [ ] In-app / Portal — flagged as nice-to-have / future use case (see appendix)

**Product(s) involved**
- Longevity — specifically NAD+ liquid injections (SQ injectable, 100mg/ml, 10ml vial).
- **Supply cycle:** 28-day supply per vial. Vial must be discarded 28 days after first puncture.
- **Dosing protocol:** Week 1: 34mg 3x/week → Week 2: 50mg 3x/week → Week 3+: 100mg 3x/week.
- **Product-specific rules:** Optimization register only. Never deficiency or decline framing. Conditional verbs on all benefit claims. No individual outcome promises tied to a timeline. Clinical literature cited as "what research shows," not "what you'll feel."

**Key message**
You made a long-term investment in how you feel and function. We're going to make sure you know exactly what you're taking, why it matters, and what to watch for — so you can decide for yourself whether to keep going.

**Supporting points**
- NAD+ levels measurably rise with supplementation, with significant elevation typically observed by week 4 (Yi et al., Katayoshi et al.).
- Your provider is a real clinician who reviews your case individually — this isn't a supplement subscription, it's guided therapy.
- Consistency over the first 28 days is the single most important variable. NAD+ levels return to baseline approximately 4 weeks after stopping.

**Constraints**
- **Compliance:** No individual outcome promises. All benefit claims use conditional verbs. FDA compounding disclaimer required on emails with benefit claims. NMN is a lawful dietary supplement (FDA September 2025); disease treatment claims are still prohibited.
- **Brand:** Optimization register throughout. Dinner-party-guy tone. No exclamation points. Sentence case on all CTAs.
- **Technical:** SMS opt-in status must be confirmed before first SMS send. Push permission required before first push. Refill timing assumes a 28-day supply cycle. Refill reminders must account for 5–7 business day shipping lead time.

**Reference**
- MDI thank you message — source of truth for injection instructions, dosing protocol, post-injection care, storage, and side effects
- Dr. Nabity clinical handouts (cellular health, longevity categories)
- Clinical evidence audit (9 human trials — see post-purchase strategy Appendix A)
- Longevity launch flow review (06-15-26) — structural best practices from the Welcome, Cart, and Questionnaire flows
- Ready flow audit playbook — touchpoint hierarchy and offer architecture decisions

**Out of scope for this brief**
- Win-back or churn intervention (post-lapse). The cessation rebound message (Katayoshi et al.) is noted here as a future asset but is not part of this onboarding sequence.
- Cross-sell to other longevity products (Sermorelin, Glutathione, etc.). Month 2–3 content introduces the longevity pillars conceptually but does not push specific SKUs.
- Portal/app features (self-assessment, biological age tracking, provider messaging). These are flagged as future use cases in the appendix.

---

## Background

### The strategic framework

This journey is built on the Provider-Amplified Educational Identity framework defined in the [Notion strategy doc](https://app.notion.com/p/37b50c58808480279dd3ed03fe72180e). The core insight: NAD+ clinical evidence is directionally promising but not strong enough to anchor hard outcome claims on specific milestones. The trials are small (n=15–108), short (6–24 weeks), and heterogeneous. The science confirms the mechanism — NAD+ levels rise with supplementation. It does not confirm the specific lived experience we can promise individual customers.

This means the onboarding sequence cannot be structured as a "here's what you'll feel by week 2, week 4, week 8" benefit-milestone track. That approach would overpromise, underdeliver for many patients, and erode trust. Instead, we use education as the backbone — teaching patients what NAD+ does biologically, what the research has studied, and what to observe (not expect) — with the provider relationship as the differentiator.

### What the evidence supports

| We can defensibly say | We cannot defensibly say |
|---|---|
| NAD+ levels in the blood rise with NMN supplementation, with significant elevation typically observed by week 4 | "You will feel more energy by week 4" |
| Clinical research has studied NAD+ in relation to sleep, aerobic capacity, insulin sensitivity, and biological age | "NMN improves your sleep" or "NMN reverses aging" |
| NMN is safe and well-tolerated at recommended doses | Any disease treatment claim |
| NAD+ levels return to baseline approximately 4 weeks after cessation | "Stopping is dangerous" or fear-based framing |

Sources: Yi et al. (2022), Katayoshi et al. (2023), Kim et al. (2022), full audit in post-purchase strategy Appendix A.

### Why the first 90 days matter

The NAD+ customer is different from the sexual health customer. Ready and Go Long patients feel the product working within days — the evaluation window is short and the evidence is visceral. NAD+ patients may not feel anything obvious for weeks, and the benefits that do emerge (sleep quality, sustained energy, recovery) are gradual and diffuse. This means:

1. **The early churn risk is higher.** Without a noticeable "it's working" signal, patients evaluate based on trust in the science and trust in the provider — not on felt experience.
2. **Education is the primary retention lever.** If a patient understands what NAD+ is doing at the cellular level, they're more likely to stay through the ambiguous early weeks.
3. **The refill decision is the moment of truth.** Around Day 20, the patient decides whether to order again (shipping lead time is 5–7 business days). Everything before that point should build toward the confidence needed to make that decision.
4. **Self-injection is a high-anxiety barrier.** This is a subcutaneous injectable with a 9-step injection process and a dosing ramp over 3 weeks. The welcome email must prioritize practical confidence.

### The product

NAD+ liquid, compounded by Olympia Pharmacy. 100mg/ml, 10ml vial, 28-day supply.

**Dosing protocol:**
- Week 1: Inject 34 units (34mg) subcutaneously 3x/week
- Week 2: Inject 50 units (50mg) subcutaneously 3x/week
- Week 3+: Inject 100 units (100mg) subcutaneously 3x/week

**Storage:** Refrigerate (2–8°C / 36–46°F). Do not freeze. Keep away from light. Discard unused medication 28 days after first puncture.

**Injection sites:** Abdomen or thigh. Rotate injection sites with each dose.

**Post-injection:** Slight redness or discomfort at the injection site is normal. Apply a cool compress if needed.

The dosing ramp means the journey has natural built-in touchpoint moments at the Week 1→2 and Week 2→3 transitions, which are used to anchor the Day 7 and Day 14 emails.

### Dr. Nabity's clinical framing

Per Dr. Nabity's reference materials (Michigan Center for Regenerative Medicine), NAD+ is positioned as a cornerstone of cellular health and regenerative medicine. Key framing that informs this journey:

- NAD+ is a coenzyme in every cell, involved in energy production, DNA repair, and cell signaling
- Supplementation addresses the natural decline that occurs with aging
- The six benefit domains from the clinical handout: energy metabolism, cellular repair, circadian rhythm regulation, brain health support, anti-aging effects, weight management support
- NMN as a precursor converts to NAD+ within cells, supporting mitochondrial function

All of this language requires conditional framing before use in patient-facing content (see compliance constraints above).

---

## High-level summary

### Journey architecture

The 90-day journey divides into three phases, each with a distinct job:

| Phase | Days | Job | Touches | Primary channel |
|---|---|---|---|---|
| **First month** | 0–28 | Teach injection, build scientific confidence, first refill | 6 | Email + SMS |
| **Lifestyle integration** | 29–60 | Deepen the longevity identity, self-assessment, second refill | 4 | Email + SMS |
| **Provider deepening** | 61–90 | Introduce clinician voice, deepen science, third refill, celebrate commitment | 5 | Email + SMS + Push |

**Total touchpoints across 90 days: 15**
- Email: 10
- SMS: 4
- Push: 1

Average cadence: ~1.2 touches per week. Heaviest in weeks 1–2 (4 touches in 14 days), then ~1 per week through month 3.

### Three refill windows

The 28-day supply cycle and 5–7 day shipping lead time define three refill decisions:

| Refill | Vial expires | Order by | Key touchpoints |
|---|---|---|---|
| **Refill 1** | ~Day 28 | ~Day 21 | Full-dose + consistency email (Day 14), refill SMS (Day 20), milestone + refill email (Day 25) |
| **Refill 2** | ~Day 56 | ~Day 49 | Pillar content builds ongoing value; refill SMS (Day 49) |
| **Refill 3** | ~Day 84 | ~Day 77 | Provider perspective deepens commitment; refill SMS (Day 77), 90-day milestone (Day 85) |

---

## Touchpoint map — Days 0 to 90

### First month (Days 0–28) — 6 touchpoints

Each of the 4 emails in this phase carries more weight. Content that previously lived in standalone touchpoints is absorbed into these larger, richer emails.

| Day | Touchpoint | Channel | Key message | Supporting material | Notes |
|---|---|---|---|---|---|
| **0** | Welcome + how to inject | **Email** | You made a long-term investment in yourself. Here's exactly how to use your NAD+ injections, your dosing schedule, and how to reach us. | **Injection how-to guide** (9-step process with photos, sourced from MDI note): wash hands, gather supplies, clean vial stopper, draw dose, choose site (abdomen or thigh), clean site, pinch skin, inject at 90° slowly, dispose in sharps container. **Dosing schedule card**: Week 1: 34mg 3x/week → Week 2: 50mg 3x/week → Week 3+: 100mg 3x/week. **Storage**: refrigerate, no freezing, away from light, discard 28 days after first puncture. **Post-injection care**: slight redness/discomfort is normal, cool compress, rotate sites. **Dosing log** (PDF attachment): 4-week tracking grid — date, dose (pre-filled for ramp), injection site (L/R abdomen, L/R thigh), vial open date. **FAQ**: common early questions ("Is it normal to feel nothing?" — yes. "When do I increase my dose?" — Week 2). Dr. Nabity introduction. | The densest email in the sequence. Patients will return to it through Week 1 as a reference. Lead with practical utility. Include a reply prompt: "Questions about your NAD+ injections? Reply to this email — our care team reads every one." |
| **0** | Welcome confirmation | **SMS** | Welcome to Rugiet. Your NAD+ injections ship within 5–7 business days. Questions anytime: [support link] | — | Opt-in confirmation + shipping expectation. Under 160 characters. |
| **7** | Week 1 complete | **Email** | First week done. Whether you feel something or not — both are completely normal. Here's what NAD+ is actually doing at the cellular level, and what changes this week. | **Reassurance block**: "Some patients notice subtle shifts in the first week. Most don't. Neither means anything yet — NAD+ works at the cellular level before it works at the level you can feel. Both responses are normal." **NAD+ 101**: NMN → NAD+ → mitochondrial energy, DNA repair, sirtuin activation. Mechanism visual or animation. **Dose increase reminder**: "Starting this week, increase to 50mg (50 units) 3x/week. Same injection process, same sites." | Carries the job of two former emails — Day 4 reassurance + Day 7 education. The dose change gives it a practical reason to open beyond "congrats on week 1." Tone: fascinating, not clinical. No discount. |
| **14** | Full protocol + what to observe | **Email** | Your dose reaches the full protocol this week. Here's what consistency does from here — and something worth paying attention to. | **Dose increase**: "Starting this week, increase to 100mg (100 units) 3x/week. This is your ongoing dose — no more ramp." **Consistency section**: "Why consistency beats optimization" — patients who tinker before establishing a baseline undermine the foundation. Katayoshi pharmacokinetics: blood NAD+ rises starting around week 4 with consistent use. **Sleep/circadian awareness**: "Many people start paying attention to sleep quality around now. Worth observing — not expecting. NAD+ helps regulate circadian enzymes — the mechanism is established. Individual experiences vary." Awareness prompts: sleep onset, morning alertness, afternoon energy. | Carries the job of three former emails — Day 10 sleep awareness + Day 14 full-dose transition + Day 18 consistency. The dose ramp completion creates a natural "you've arrived" moment. The sleep content earns its place because it gives patients something specific to observe. |
| **20** | Refill reminder | **SMS** | Your NAD+ refill window is open. Same protocol, no new consultation needed: [refill link] | — | Pure utility. The patient who's going to refill just needs the link. Timed for 5–7 day shipping before Day 28 vial expiry. |
| **25** | Week 4 milestone + refill | **Email** | Clinical research shows NAD+ levels reach significant elevation around now. You're past the foundation phase — and your next month is ready. | **Clinical milestone**: Yi et al. (2022) trial summary, accessible framing. Katayoshi pharmacokinetics confirmation. "Clinical research shows NAD+ levels typically reach significant elevation around week 4. You've built the foundation." **Self-reflection prompt**: "What have you noticed? Energy, sleep, recovery, focus — any shift, even subtle, is signal." **Refill CTA**: "Your next shipment keeps that trajectory going." Optional provider check-in offer (async message or brief call). | Carries the job of two former emails — Day 23 refill + Day 28 milestone. The milestone context gives the refill CTA a reason beyond "your supply is running out." The self-reflection prompt creates a conscious moment of attribution. Moved from Day 28 to Day 25 to align with refill shipping lead time. |

### Lifestyle integration (Days 29–60) — 4 touchpoints

The patient has refilled at least once. The work shifts from "should I keep doing this?" to "what else supports what I'm doing?" — connecting NAD+ to broader longevity practices, then prompting self-reflection.

| Day | Touchpoint | Channel | Key message | Supporting material | Notes |
|---|---|---|---|---|---|
| **35** | Longevity pillars: sleep + movement | **Email** | NAD+ is one piece of a longevity foundation. Sleep and movement are two others — and they're biologically connected. | Provider-authored content on NAD+ and circadian biology. How sleep quality compounds the benefits of NAD+ supplementation. How exercise and NAD+ both support mitochondrial function. Practical, actionable guidance. Liao et al. context on exercise if appropriate. | First of two pillar emails. Each connects back to NAD+ through established mechanisms without making product claims. Keep movement advice grounded: "Walk more, lift something heavy twice a week" not a training protocol. |
| **44** | Longevity pillars: nutrition + stress | **Email** | The metabolic machinery NAD+ supports runs on what you eat — and stress burns through it faster than almost anything. | NAD+ and metabolic health connection. Practical nutrition framing around metabolic efficiency, not dieting. NAD+ and the stress response — sirtuin activation, DNA repair demand under chronic stress. Recovery as a longevity tool. Dr. Nabity's framing: "NAD+ is involved in DNA repair and cellular health maintenance." Tease Month 3: "Next month, we're going to hear directly from the clinicians." | Second pillar email. Wraps up the lifestyle integration series. |
| **49** | Month 2 refill reminder | **SMS** | Your NAD+ refill is ready. Continue your protocol: [refill link] | — | Timed for shipping lead time before Day 56 vial expiry. |
| **55** | Two-month self-assessment | **Email** | Two months in. You've built a real protocol. What have you noticed? | Self-assessment prompt: structured reflection on energy, sleep, recovery, focus, mood, physical performance. "This isn't a quiz — it's for you. The patients who notice the most are the ones who pay attention." Optional: link to a short survey (3–5 questions) whose anonymized results fuel future content. Preview of Month 3: "Next up — how the clinicians actually think about NAD+." | Creates a moment of conscious reflection. Patients who stop and think about what's changed are more likely to attribute value. Survey data fuels future "what patients report" content (with proper disclaimers). |

### Provider deepening (Days 61–90) — 5 touchpoints

The patient has refilled twice. They've decided to stay. The work shifts to deepening the relationship — Dr. Nabity's clinical voice, deeper science, and celebrating the 90-day commitment.

| Day | Touchpoint | Channel | Key message | Supporting material | Notes |
|---|---|---|---|---|---|
| **63** | Provider perspective | **Email** | Here's how clinicians actually think about NAD+ — not the marketing version, the clinical one. | Dr. Nabity-authored or attributed content. How providers evaluate longevity therapies. What they watch for in NAD+ patients. The difference between "clinically guided" and "direct-to-consumer supplement." Compounding pharmacy quality context (503-A/503-B standards, USP compliance). | The email where the provider relationship is sold as the differentiator. "Most supplement brands compete on formulation and price. We compete on the relationship between you and a licensed clinician." Tone: authoritative, transparent, un-salesy. |
| **70** | Deeper science | **Email** | Let's go deeper — biological age, DNA repair, and what "cellular health" actually means. | Deep science content: NAD+ role in sirtuin activation, DNA repair (PARPs), mitochondrial biogenesis. Yi et al. Aging.AI 3.0 finding: "In one trial, biological age remained stable in supplemented groups while increasing in placebo over 60 days." Biological age testing as a concept (not a hard sell). | For the patient who's stayed 70 days, the appetite for depth is real. This email rewards long-term engagement with substance. |
| **77** | Month 3 refill reminder | **SMS** | Your third month of NAD+ is ready. Same protocol: [refill link] | — | Timed for shipping before Day 84 vial expiry. By Month 3, the patient either has a rhythm or doesn't. Keep it clean. |
| **78** | Community signal | **Push** | You've been on NAD+ for 11 weeks. That's commitment. Here's what other members are noticing. | — | Light-touch social proof. Links to community content or member spotlight if available. If none exists yet, simple milestone acknowledgment. |
| **85** | 90-day milestone | **Email** | Three months. You've built a longevity practice — not just a supplement habit. Here's what's ahead. | 90-day reflection: what the research says about sustained NAD+ supplementation. Katayoshi finding: "Your consistent use has kept NAD+ levels elevated through the most critical window." What's next: deeper science content, provider consultations, the broader longevity portfolio. Bridge to the next 90 days (retention arc). Loyalty acknowledgment — not a discount, a recognition. | Transition email from onboarding to retention. |

---

## Channel strategy

### Email (10 sends over 90 days)

Email carries all education, mechanism content, clinical references, provider voice, and pillar series. Each email does more work than it would in a higher-frequency sequence — the trade-off for fewer touches is richer individual sends.

- One CTA per email. "Contact us" is a text link, not a competing button.
- Sentence case on all headlines, subheads, and CTAs.
- No exclamation points.
- Optimization register throughout — capability and upgrade, never deficiency.
- Conditional verbs on every benefit claim.
- Reply prompt in Email #1 (Gmail primary tab placement signal).
- FDA compounding disclaimer in footer of any email containing benefit claims.

**Cadence:**

| Phase | Emails | Average gap |
|---|---|---|
| First month (Days 0–28) | 4 | 8 days |
| Integration (Days 29–60) | 3 | 10 days |
| Deepening (Days 61–90) | 3 | 11 days |

### SMS (4 sends over 90 days)

SMS has two jobs: welcome confirmation and refill utility. Every SMS is under 160 characters.

| SMS | Day | Job |
|---|---|---|
| Welcome | 0 | Shipping expectation + support link |
| Refill 1 | 20 | Utility — refill link |
| Refill 2 | 49 | Utility — refill link |
| Refill 3 | 77 | Utility — refill link |

### Push (1 send over 90 days)

One send at Day 78 — community/milestone acknowledgment. If push permissions aren't granted, this touchpoint doesn't fire and isn't replaced.

### In-app / Portal (future use cases)

| Feature | When it would fire | Value | Status |
|---|---|---|---|
| **Onboarding checklist** | Day 0–7 | Step-by-step setup: account, dosing log, first injection tracking | Future |
| **Dosing tracker** | Ongoing | Digital dosing log — injection dates, sites, dose, vial open date, refill reminders | Future |
| **Self-assessment prompts** | Day 7, 25, 55, 85 | "What have you noticed?" — structured reflection tied to milestones | Future |
| **Provider async messaging** | Day 25+ | Patient can message their provider with questions post-milestone | Future |
| **Biological age dashboard** | Month 4+ | Display biological age testing results with provider interpretation | Future |
| **Refill management** | Ongoing | One-tap refill from the portal, tied to 28-day supply cycle | Future |
| **Community feed** | Month 3+ | Member spotlights, provider commentary, anonymized patient stories | Future |

---

## Suppression and orchestration rules

| Rule | Logic |
|---|---|
| **Purchase suppresses acquisition flows** | If the patient is in Welcome, Cart Abandon, or Questionnaire Abandon flows at time of NAD+ purchase, suppress all acquisition sends immediately and enter this onboarding flow. |
| **Refill purchase suppresses refill reminders** | If the patient refills before the refill reminder fires, suppress the SMS and any refill-related email content. |
| **Active support ticket pauses sends** | If the patient has an open support ticket, pause all non-transactional sends until resolved. |
| **Unsubscribe from email does not suppress SMS/Push** | Channel preferences are independent. An email unsubscribe doesn't affect SMS or push. |
| **No overlap with promotional sends** | While a patient is in the onboarding flow (Days 0–90), suppress all promotional/blast emails for longevity products. Cross-category promos (sexual health, TRT) can still send. |

---

## Content production requirements

### Must-have for launch (Days 0–28)

| Asset | Touchpoint | Source / Owner | Status |
|---|---|---|---|
| Injection how-to guide (9-step, with photos) | Day 0 Email | MDI thank you note (copy source) + Content (photos) + Medical review | Needed — copy exists in MDI note, needs reformatting |
| Dosing schedule card (Week 1→2→3 ramp) | Day 0 Email | MDI thank you note (source) + Design | Needed |
| **Dosing log** (PDF, 4-week tracking grid) | Day 0 Email attachment | Design + Medical review | Needed — fields: date, dose (pre-filled per ramp), injection site, notes, vial open date |
| Storage + post-injection care guide | Day 0 Email | MDI thank you note (source) | Needed — copy exists, needs reformatting |
| NAD+ FAQ (early questions) | Day 0 Email | Content + Medical review | Needed |
| Dr. Nabity provider introduction copy | Day 0 Email | Medical | Needed |
| NAD+ 101 mechanism explainer | Day 7 Email | Content + Medical review | Needed |
| Sleep/circadian awareness content | Day 14 Email | Content + Medical review | Needed |
| "Consistency beats optimization" piece | Day 14 Email | Content | Needed |
| Yi et al. trial summary (patient-accessible) | Day 25 Email | Content + Medical review | Needed |

### Build post-launch (Days 29–90)

| Asset | Touchpoint | Owner | Status |
|---|---|---|---|
| Two longevity pillar articles (sleep + movement; nutrition + stress) | Days 35, 44 | Content + Medical review | Needed |
| Self-assessment survey (3–5 questions) | Day 55 Email | Content + Product | Needed |
| Dr. Nabity-authored clinician perspective piece | Day 63 Email | Medical + Content | Needed |
| Deep science content (biological age, sirtuins, PARPs) | Day 70 Email | Content + Medical review | Needed |
| 90-day milestone content | Day 85 Email | Content | Needed |
| Community/member spotlight content | Day 78 Push | Content | Needed (or skip until available) |

---

## Measurement

### Primary metric
**First refill rate** — percentage of first-time NAD+ customers who purchase a second time.

| Window | Benchmark target | Notes |
|---|---|---|
| 28-day | TBD (set after 2 weeks of baseline data) | Measures whether first-month content drives the refill decision |
| 90-day | TBD | Measures full onboarding arc effectiveness |

### Secondary metrics

| Metric | What it tells us | Watchlist threshold |
|---|---|---|
| Email open rate by position | Which emails are earning attention | Below 30% → subject line or timing issue |
| Click rate on educational content | Whether patients are engaging with the science | Below 3% → content or framing issue |
| SMS refill link click rate | Whether utility SMS is driving action | Below 10% → timing or friction issue |
| Unsubscribe rate by position | Whether any touchpoint is causing fatigue | Above 1% on any single send → investigate |
| Time to first refill (median days) | Whether the sequence is accelerating or delaying the decision | If median > 25 → refill messaging needs to move earlier |
| Day 55 survey completion rate | Whether patients are reflecting on their experience | Below 10% → survey too long or poorly timed |

### What we'll learn in the first 28 days

1. Whether the Day 20 SMS + Day 25 Email refill window is timed correctly (are patients refilling before or after these sends?)
2. Whether the Day 7 email carrying both reassurance and mechanism education feels like too much or just right (watch CTR and unsub rate)
3. Whether the Day 14 email carrying dose change + consistency + sleep awareness holds together or needs to be split in v2
4. Whether 4 emails in 28 days is enough onboarding support for a self-injection product (watch support ticket volume in Week 1)

---

## Appendix: Key clinical references by touchpoint

| Touchpoint | Reference | Framing guidance |
|---|---|---|
| Day 0 (Welcome) | MDI thank you note — injection instructions, dosing, storage, side effects | Source of truth for all how-to content. Reformat for email, do not editorialize medical instructions. |
| Day 7 (Week 1) | Established biochemistry — NMN → NAD+ biosynthesis | No specific trial citation needed. Mechanism education. |
| Day 14 (Full protocol) | Kim et al. (2022) — circadian/sleep connection; Katayoshi et al. (2023) — pharmacokinetics | Sleep: "Research has studied NAD+ in relation to sleep quality." Consistency: "Blood NAD+ levels rise starting around week 4 with consistent use." |
| Day 25 (Milestone + refill) | Yi et al. (2022) + Katayoshi et al. (2023) | "Clinical research shows NAD+ levels reach significant elevation around now." Observational framing. |
| Day 44 (Stress pillar) | Dr. Nabity handout — DNA repair, sirtuin activation under stress | "NAD+ is involved in DNA repair and cellular health maintenance." Conditional language required. |
| Day 63 (Provider perspective) | Compounding pharmacy standards (503-A, USP compliance) | "Doctor-guided protocols, not DIY or supplements." Differentiation messaging. |
| Day 70 (Deeper science) | Yi et al. (2022) — Aging.AI 3.0 biological age finding | "In one trial, biological age remained stable in supplemented groups while increasing in placebo." Observational. |
| Day 85 (90-day milestone) | Katayoshi et al. (2023) — cessation rebound | "Your consistent use has kept NAD+ levels elevated." Positive framing of the retention data. |

---

## Change log

| Date | Change | Author |
|---|---|---|
| 2026-06-16 | Initial 90-day journey map with brief, touchpoint table, channel strategy, and content requirements | Lifecycle |
| 2026-06-16 | Rebalanced Foundation phase with injection check-in and adaptation email. Consolidated 4 pillar emails to 2. Added self-assessment at Day 55. Integrated MDI thank you note. Added dosing log. Updated to 28-day supply cycle. | Lifecycle |
| 2026-06-16 | Reduced first 28 days from 10 to 6 touchpoints. Cut: Day 2 injection check-in SMS (covered by Day 0 email), Day 4 adapting email (absorbed into Day 7), Day 10 sleep email (absorbed into Day 14), Day 23 refill email (merged with Day 25 milestone). Consolidated phases 1+2 into single "First month" phase. Total journey: 15 touchpoints (10 email, 4 SMS, 1 push). | Lifecycle |
