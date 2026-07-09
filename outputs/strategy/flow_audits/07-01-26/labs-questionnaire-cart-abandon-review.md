# Labs by Rugiet — Questionnaire Abandon + Cart Abandon Copy Review

**Date:** 2026-07-01
**Flows reviewed:** Questionnaire Abandon (3 emails), Cart Abandon (3 emails)
**Source (Figma):** [Questionnaire Abandon](https://www.figma.com/design/P4Plx6tHNU9Op1D8bFqgSM/email-review?node-id=6504-114) · [Cart Abandon](https://www.figma.com/design/P4Plx6tHNU9Op1D8bFqgSM/email-review?node-id=6504-273) (file key `P4Plx6tHNU9Op1D8bFqgSM`)
**GTM source:** [Labs PAT — Project Alignment Tracker](https://app.notion.com/p/Labs-PAT-Project-Alignment-Tracker-38850c58808480889f2bde7b5c5eccab) (Marketing & Positioning Strategy, Category Framing, Growth Marketing, Strategic Watchouts)
**References:** [Lifecycle Conversion Flow Framework](../06-13-26/exec-summary-flow-optimization.md) · [Longevity Launch Review](../06-15-26/longevity-launch-review.md) · Email Marketing Bible v2.0 · Rugiet Copywriting Skill (compliance, trademark, tone, owned-channels)
**Status:** Copy review + proposed updates — pending design + Braze implementation

---

## Executive summary

Both flows are visually on-brand and structurally close to the playbook — the questionnaire flow already runs the correct 3-email count with no discount, and the cart flow follows the reminder → differentiation → offer arc. The copy is also, in places, already carrying the PAT's core positioning almost verbatim (Cart 2's "Most lab companies stop at the data / we built Rugiet Labs to go further" is the PAT's #1 differentiator; the questionnaire "Test. Understand. Act." is the closed-loop story). That's a strong starting point.

The gap is not strategy — it's **discipline and infusion**. Three patterns repeat across all six emails:

1. **Two or three competing CTAs per email** — every email has a hero CTA plus a second (and sometimes third) button. This violates the one-CTA rule in both the framework and EMB §5, and dilutes the single above-the-fold action you asked to protect.
2. **The Labs GTM positioning is present but thin** — the emails reference the loop and personalization, but don't fully infuse the PAT's differentiators (Test → Understand → Act, lower-friction/higher-quality, the "diagnostic layer not a barrier," trust-over-conversion) or the panel positioning language.
3. **Launch hygiene debt carried over from the Longevity flows** — `Performance Medicine For Men™` (should carry no symbol), `©2025`, placeholder discount values (`XX%`, `$69`), placeholder cart contents ("Lab Option 1–4" with Recharge pill-bottle imagery), and all-caps CTAs.

**Verdict: Ship with the must-fixes applied. The proposed copy below keeps every strong line already in the drafts, cuts the second CTA on all six emails, and infuses the PAT positioning so each email carries exactly one message + one benefit + one above-the-fold CTA aligned to that message.**

---

## The Labs positioning to infuse (from the PAT)

Everything proposed below pulls from these PAT sections. This is the source of truth for what "Labs by Rugiet" means in copy.

**Category frame (PAT → Category Framing):**
- Labs is *the diagnostic layer for Rugiet* — "the new starting point for personalized men's health," **not a standalone commodity test and not a barrier to care.**
- Support line: moves Rugiet "from symptom-based care to biomarker-informed optimization."

**The three core differentiators (PAT → Marketing & Positioning Strategy):**
1. **Test → Understand → Act.** Competitors stop at "understand." Rugiet closes the loop with a plain-language interpretation, a personalized action plan, and a route to action (supplements, lifestyle, or care through Rugiet *if medically applicable*).
2. **Lower friction, higher-quality care.** Easier funnel, test on your terms (no pre-set schedule), no membership required, clear panels, **no scare tactics**, built for men who want an edge — not for biohackers.
3. **Existing trust in men's performance.** Lean on the 500k+ credibility, but word it **gender-neutral** ("500k+ patients") and keep the core male consumer in mind.

**Panel positioning (PAT → Hero Products):**
| Panel | One-line positioning |
|---|---|
| Essential Men's Health Panel | "The best first step if you're not feeling like yourself." |
| Performance + Hormone Panel | "See the markers behind performance, drive, and recovery." |
| Advanced Optimization Panel | "A deeper look at the markers that shape long-term performance and health." |

**Audience angles (PAT → Growth Marketing personas):**
- Symptom-first: "Your symptoms may be telling you something."
- Performance seekers: "Stop guessing. See what's actually driving your performance."
- Aging optimization: "Track the markers that change as men age — and what to do about them."

**Labs-specific compliance guardrails (PAT → Strategic Watchouts §1, FAQs):**
- Labs do **not** require a prescription; **cash-pay**; results are **not a diagnosis**; Labs **complements, does not replace** primary care.
- Use: "may be associated with," "can help inform," "consider discussing with a clinician," "eligible customers may be connected to care," "this is not a diagnosis."
- Avoid: "you have X condition," "you need X medication," "this will fix your [marker]," "your results mean you should take X," "**Rugiet treats X**." Labs are **panels/tests**, never "treatments."
- **Trust > conversion.** Customers should feel "I understand my results" before "someone is selling me something." Don't push products in the first touch.

**Naming / trust open items (do not hard-code in copy yet):**
- The AI interpretation layer is **not** to be called "Nadia" in customer copy (naming/trademark exploration pending). Use generic "plain-language interpretation."
- Trust model (named Rugiet Labs Medical Advisor vs. Medical Advisory Board) is **undecided.** Keep credibility copy generic ("ordered through a licensed physician, reviewed by Rugiet's medical team") until the decision lands.

---

## Proposed canonical descriptor for Labs

Per the framework, every product locks a canonical descriptor before flows are built. Labs already has one hiding in the copy and the PAT:

> **Test. Understand. Act.**

It is factual (three product stages, not a claim), it is the PAT's #1 differentiator, and it separates Rugiet from every competitor who "stops at the data." Recommend locking it and using it in at least one email per flow (it currently appears in Questionnaire 3 and, in spirit, Cart 2).

---

# Flow 1 — Questionnaire Abandon (3 emails)

**Audience intent:** lowest in the funnel — started the intake, never reached panel selection or checkout. Per the framework's browse/questionnaire hierarchy, these are reminder + micro-commitment + value emails with **no discount**. The current flow correctly carries no offer — keep it that way (reinforced by the PAT's "trust > conversion" stance).

## Current state

| # | Hero (H1) | Body / message | CTAs (current) | Job |
|---|---|---|---|---|
| 1 | "You were onto something" | "Most men think about getting labs done. You actually started. Rugiet labs tests the markers that matter, tells you what they mean, and gives you a clear plan for what to do next. Takes 5 minutes to complete." + a second block: "Over 500k+ guys have trusted Rugiet." | `COMPLETE QUESTIONNAIRE` + `PICK UP WHERE YOU LEFT OFF` + `CONTACT US` (3) | Intent hook + social proof |
| 2 | "Two minutes between you and answers" | "The intake you started matches you to the right panel based on your goals. Hormones, metabolism, energy, recovery – we narrow it so you don't have to guess." + "What happens next" 3-step | `FINISH YOUR QUESTIONNAIRE` + `GET STARTED` + `CONTACT US` (3) | Process transparency |
| 3 | "Numbers are useless without a plan" | "Rugiet labs doesn't stop at data." + "Test. Understand. Act." section: "Every result comes with a plain-language interpretation and a personalized action plan, What your markers mean. Where they fall. What to do next." | `COMPLETE YOUR INTAKE` + `FINISH NOW` + `CONTACT US` (3) | The loop / value of action |

**What's already working (keep it):**
- "You were onto something" is an excellent intent hook — it references curiosity and momentum, never abandonment ("Don't stop," "You left" are prohibited by the framework). Do not touch the concept.
- The "What happens next" 3-step in Email 2 is the single strongest structural element — process transparency is the highest-converting pattern in the Ready and Longevity reviews.
- "Test. Understand. Act." in Email 3 is the PAT differentiator, verbatim. Keep it as the anchor.

**Issues to fix:**
1. **Two-to-three CTAs per email.** Collapse to one primary above-the-fold CTA aligned to the hero message. Convert "Contact us" to the text link already in the "Have questions?" footer block.
2. **"500k+ guys"** → gender-neutral "Over 500,000 patients" per the PAT, and demote it from a competing CTA block to a static trust line (no button).
3. **Thin infusion.** Email 2 can carry the "test on your terms / no guessing" friction message; Email 3 can add the generic trust line to close the PAT's "trust gap."
4. **Hygiene:** `Performance Medicine For Men™` → remove ™; `©2025` → `©2026`; all-caps CTAs → sentence case; footer nav says "For Testosterone" (cart flow says "For Hormones" — standardize, see cross-flow).
5. **Subject lines undefined** (no inbox-preview component in the drafts) — proposed below, ≤6 words per owned-channels.

## Proposed copy

### Questionnaire — Email 1 (2–4 hours after drop) · Intent hook
**Key message:** you already made the smart move — finish it. **Benefit:** markers that matter + a plan. **No offer.**

```
S: You were onto something

Prev: You started your labs. Finish the questionnaire and see what your markers mean.

H1: You were onto something

Most men just think about getting labs done. You actually started.

Rugiet Labs tests the markers that matter, explains what they mean in
plain language, and gives you a personalized plan for what to consider
next. It takes about 5 minutes to finish.

[ Finish my questionnaire ]   ← single CTA, above the fold

—
Over 500,000 patients trust Rugiet.   ← static trust line, no button
```
*Rationale:* one message, one CTA. "What to consider next" (not "what to do") stays compliant with the PAT's Nadia/action-plan guardrails. 500k moves to a trust strip so the hero CTA is the only button.

### Questionnaire — Email 2 (Day 1) · Process transparency
**Key message:** finishing is fast and it removes the guesswork. **Benefit:** matched to the right panel. **No offer.**

```
S: Two minutes to answers

Prev: The intake you started matches you to the right panel — no guessing required.

H1: Two minutes between you and answers

The questions you started match you to the right panel for your goals —
hormones, metabolism, energy, recovery, or a full baseline. We narrow it
down so you don't have to guess, and you test on your terms.

[ Finish my questionnaire ]   ← single CTA, above the fold

What happens next
 01  Answer a few questions
 02  Get matched to your panel
 03  See what your body is telling you
```
*Rationale:* keeps the winning 3-step. Infuses PAT differentiator #2 ("test on your terms," "so you don't have to guess"). Drops the duplicate `GET STARTED` button — the hero CTA and the numbered list do the job.

### Questionnaire — Email 3 (Day 3) · The loop + trust
**Key message:** data alone changes nothing — Rugiet closes the loop. **Benefit:** interpretation + action plan, backed by real clinicians. **No offer.**

```
S: Test. Understand. Act.

Prev: Every Rugiet Labs result comes with plain-language answers and a personalized action plan.

H1: Numbers are useless without a plan

Rugiet Labs doesn't stop at the data. Every result comes with a
plain-language interpretation and a personalized action plan — what your
markers mean, where they fall, and what to consider next.

Your labs are ordered through a licensed physician and reviewed by
Rugiet's medical team. This is optimization, not a diagnosis.

[ Complete my intake ]   ← single CTA, above the fold

Test. Understand. Act.
```
*Rationale:* anchors on the PAT's #1 differentiator and canonical descriptor. Adds a generic clinical-credibility line to close the PAT's "trust gap" (who ordered this? who reviews it? are these real labs?) without naming a doctor (pending MAB decision). "Optimization, not a diagnosis" is straight from the PAT compliance guardrails.

---

# Flow 2 — Cart Abandon (3 emails)

**Audience intent:** highest in the funnel — selected a panel, reached checkout. Per the framework's cart hierarchy, lead with a trust/reminder, and reserve any offer for the final email only. The current flow does this (offer appears only in Email 3), which is correct. The PAT's "Labs is not an acquisition driver / trust > conversion" stance means the discount should be modest, single-tier, and possibly reconsidered in favor of a non-discount lever (see open decisions).

## Current state

| # | Subject / preview | Hero (H1) | Body / message | CTAs (current) | Job |
|---|---|---|---|---|---|
| 1 | "Take your labs. Find the right treatment for you." / "Your labs are still waiting." | "You're close" | "You selected your panel and made it to checkout. Complete your order, book your draw at a lab near you or get a kit sent to your door, and see what your body has to say." + "Your lab options are waiting" (Lab Option 1–4, placeholder descriptions, Recharge pill-bottle imagery) | `COMPLETE YOUR ORDER` + `GET MY LAB TEST` (2) | Cart reminder |
| 2 | "Your labs are waiting in your cart" / "Complete them, then pay one price for all four treatments." | "Most lab companies stop at the data" | "We built Rugiet labs to go further." + "Your panel is still in your cart" 3-step (Test the markers that matter / Understand plain language results / Get a personalized next step). Orange banner: "Get started for $69" | `GET MY LABS` + `COMPLETE YOUR ORDER` (2) | Differentiation |
| 3 | Banner: "Use code RUGIETLABS for XX% off your first panel" | "This panel was built for you" | "The questionnaire you completed matched you to a panel based on what you're trying to understand – hormones, metabolic health, energy, recovery, or a full baseline. Not generic. Not one-size-fits-all." + "Stop guessing. Start knowing." | `COMPLETE YOUR ORDER` + `SAVE XX% NOW` (2) | Personalization + offer |

**What's already working (keep it):**
- Cart 2's "Most lab companies stop at the data / we built Rugiet Labs to go further" **is the PAT's #1 differentiator, near-verbatim.** Best line in either flow. Protect it.
- Cart 2's 3-step ("Test the markers that matter / Understand plain-language results / Get a personalized next step") is the Test → Understand → Act loop rendered as a list. Keep.
- Cart 3's "This panel was built for you" is the personalization differentiator; "Stop guessing. Start knowing." is the PAT Performance-Seeker angle. Keep both.
- Cart 1 correctly names both fulfillment paths (lab draw + at-home kit), which matches Phase 1 (Quest in-person + Tasso at-home).

**Issues to fix:**
1. **Two CTAs on every email.** Collapse to one.
2. **"treatment" / "treatments" language** (Cart 1 subject "find the right treatment," Cart 2 preview "one price for all four treatments"). Labs are **panels/tests, never treatments** (PAT compliance). Remove.
3. **Placeholder debt:** "Lab Option 1–4" + "Placeholder description" + **Recharge pill-bottle imagery** in Cart 1 (labs are not an Rx bottle — use vial/panel imagery and real panel names or dynamic cart contents per EMB §4). `$69` and `XX%` need real, stated values.
4. **Cart 1 shows no real cart contents.** EMB §4: the first cart email should show what's actually in the cart. Pull the selected panel dynamically, or list the three real panels with their PAT positioning lines.
5. **Hygiene:** `Performance Medicine For Men™`, `©2025`, all-caps CTAs, footer nav consistency.

## Proposed copy

### Cart — Email 1 (2–4 hours after abandon) · Reminder + process, no offer
**Key message:** you're one step from done — here's how it finishes. **Benefit:** two easy ways to test. **No offer.**

```
S: Your labs are waiting

Prev: You picked your panel and reached checkout. Finish up and choose how you test.

H1: You're close

You selected your panel and made it to checkout. Finish your order, then
book a blood draw at a lab near you or have an at-home kit sent to your
door. Either way, you'll see what your body is telling you.

[ Complete my order ]   ← single CTA, above the fold

Your panel is waiting
 • [Dynamic: panel name]        [panel one-line description]
 (fallback if dynamic isn't ready — list the three panels:)
 • Essential Men's Health Panel   The best first step if you're not feeling like yourself.
 • Performance + Hormone Panel    See the markers behind performance, drive, and recovery.
 • Advanced Optimization Panel    A deeper look at the markers that shape long-term health.
```
*Rationale:* simple reminder + process clarity, no discount (framework cart touchpoint 1). Replaces "Lab Option 1–4"/Recharge imagery with the real PAT panel names + positioning, or dynamic cart contents (preferred). Kills "treatment." One CTA.

### Cart — Email 2 (Day 1) · Differentiation + value, no offer
**Key message:** most labs stop at data; Rugiet goes further. **Benefit:** the closed loop. **No offer.**

```
S: Most labs stop at data

Prev: We built Rugiet Labs to go further — from results to a real action plan.

H1: Most lab companies stop at the data

We built Rugiet Labs to go further. You get the markers that matter,
results explained in plain language, and a personalized action plan that
connects to real next steps — supplements, lifestyle, or care through
Rugiet if it's right for you.

[ Complete my order ]   ← single CTA, above the fold

Your panel is still in your cart
 01  Test the markers that matter
 02  Understand plain-language results
 03  Get a personalized next step
```
*Rationale:* the strongest PAT line stays. Body now spells out the full Test → Understand → Act loop and the "route to action" ("care through Rugiet *if it's right for you*" — conditional, PAT-compliant, avoids "treats"). Removes the `$69` and "four treatments" placeholders; if a value anchor is wanted, use a real, stated price (see open decisions). One CTA.

### Cart — Email 3 (Day 3) · Personalization + offer close
**Key message:** this panel was built for you specifically. **Benefit:** stop guessing. **The only email in the flow that carries an offer.**

```
Banner: Use code RUGIETLABS for [X]% off your first panel. Expires [date].

S: This panel was built for you

Prev: You reached checkout. Your matched panel — and your code — are waiting.

H1: This panel was built for you

The questionnaire you completed matched you to a panel based on what
you're trying to understand — hormones, metabolic health, energy,
recovery, or a full baseline. Not generic. Not one-size-fits-all.

[ Complete my order ]   ← single CTA, above the fold

Stop guessing. Start knowing.
[ Save [X]% now ]   ← if the offer is approved; otherwise remove and keep one CTA
```
*Rationale:* personalization is the differentiator no competitor can claim (PAT). "Stop guessing. Start knowing." is the Performance-Seeker angle. **Discount decision required:** fill `[X]%` with a real value and a stated, enforced expiry, *or* replace with a non-discount lever (free at-home kit, complimentary doctor-review add-on) per the PAT's "trust > conversion" and "Labs is not an acquisition driver" positioning. Keep one primary body CTA — the banner and hero button both route to checkout, so drop the duplicate `SAVE XX% NOW` unless the offer close is a distinct destination.

---

## Cross-flow items (apply to all 6 emails)

### Offer architecture
| Flow | Offer? | Code | Placement | Notes |
|---|---|---|---|---|
| Questionnaire Abandon | **None** | — | — | Correct. Lowest intent, pre-pricing. Reinforced by PAT "trust > conversion." |
| Cart Abandon | **One, final email only** | `RUGIETLABS` | Email 3 only | Single tier, stated + enforced expiry, first-time abandoners. Decide %-off vs. non-discount lever. |

Do not let `RUGIETLABS` collide with other Rugiet flow codes in the same window — confirm the cross-flow suppression waterfall (Cart > Questionnaire > Welcome) in Braze, per the framework and the Longevity review's open item.

### Trademark + legal hygiene (per trademark-usage.md + compliance.md)
- **Remove ™ from "Performance Medicine For Men"** in all footers — this phrase carries no symbol (pending co-use). Same fix flagged in the Longevity review; it has carried into the Labs footer.
- **`©2025` → `©2026`** in all footers.
- Include **Rugiet®** on first textual mention (or confirm the logomark satisfies the requirement). "Rugiet® Labs" on first mention, "Rugiet Labs" / "Labs" after.
- Add the **cash-pay / not-a-diagnosis** microcopy where appropriate and, when benefit claims appear, the standard disclaimer footer.

### Footer nav consistency
Questionnaire footer lists "For Testosterone"; Cart footer lists "For Hormones." Standardize to one taxonomy across both flows — recommend **For Sleep / For Sex / For Weight / For Hormones** (matches the cart flow and the PAT's hormone/optimization framing). Consider adding a **For Labs** (or Longevity) entry now that Labs is a category.

### Imagery
- Replace the **Recharge Rx pill-bottle** thumbnails in Cart 1's "lab options" with vial/panel imagery or dynamic panel cards. An Rx bottle misrepresents a lab panel and muddies the "labs ≠ treatment" line.
- The phone-dashboard hero (Questionnaire 1, Cart 3) and the blood-vial heroes are on-brand and distinctive to Labs — keep.
- Per the framework, keep flow-unique imagery — don't recycle the same hero across both flows beyond the shared dashboard motif.

### CTAs (all six emails)
- **One primary CTA per email**, sentence case, above the fold, aligned to the hero message. Convert "Contact us" / "Get my labs" / "Finish now" secondary buttons to the existing "Have questions?" text link.
- Active + specific verbs: "Finish my questionnaire," "Complete my order," "Complete my intake" — never "Click here" / "Learn more."

### Subject lines + cadence
- Subject lines ≤6 words, sentence case, no terminal punctuation unless integral (proposed per email above).
- Cadence (per EMB §4, matching the Longevity review): both flows send at **2–4 hours after drop → Day 1 → Day 3.**

### Naming / trust (open, do not hard-code)
- Keep the AI layer generic ("plain-language interpretation") — do **not** print "Nadia" (naming/trademark decision pending).
- Keep clinical credibility generic ("ordered through a licensed physician, reviewed by Rugiet's medical team") until the named-advisor vs. Medical Advisory Board decision lands.

---

## Immediate must-fixes (do before send)

1. Cut every email to **one primary CTA** (removes 2–3 competing buttons across all six).
2. Remove **™** from "Performance Medicine For Men"; update **©2025 → ©2026**.
3. Remove **"treatment/treatments"** language from Cart 1 subject and Cart 2 preview (labs are panels/tests).
4. Fill or remove placeholders: **`$69`, `XX%`, "Lab Option 1–4," "Placeholder description," Recharge pill-bottle imagery.**
5. Add a **stated, enforced expiry** to the `RUGIETLABS` code (Cart 3).
6. Change **"500k+ guys" → "Over 500,000 patients"** (gender-neutral per PAT); demote to a trust line, not a button.
7. All **CTAs to sentence case.**
8. Standardize **footer nav** across both flows; add cash-pay/not-a-diagnosis microcopy.

## Open decisions needing input

| Decision | Options | Recommendation |
|---|---|---|
| **Cart discount** | (a) `RUGIETLABS` %-off in Cart 3 only; (b) non-discount lever (free at-home kit / complimentary doctor review); (c) no offer | **(b) or (a)** — the PAT positions Labs as an LTV/trust play, not an acquisition driver. A non-discount value-add fits "trust > conversion" better than a coupon. If discounting, single tier + stated expiry, Cart 3 only. |
| **Real pricing** | Fill `$69` / `[X]%` with launch-approved values | Blocked on the "pricing reviewed closer to launch" item in the PAT. Do not ship placeholders. |
| **AI naming** | "Nadia" vs. new trademarkable name | Keep generic in copy until resolved. |
| **Trust model** | Named Labs Medical Advisor vs. Medical Advisory Board | Keep credibility copy generic until resolved; affects Questionnaire 3 + all trust lines. |
| **Gender-neutral reach** | How far to push beyond core male consumer | PAT says test into it, don't dilute. These lifecycle emails go to a mostly-male list — keep "men" in body copy, "patients" in the trust stat. |

---

## Compliance checklist (proposed copy)

- [x] Conditional language on all benefit/claim copy ("can help inform," "what to consider next," "if it's right for you")
- [x] No prohibited Labs claims ("treats," "you need X," "your results mean you should take X," "this will fix your [marker]")
- [x] "This is optimization, not a diagnosis" present; cash-pay / complements-not-replaces posture respected
- [x] Optimization register throughout — no deficiency framing, no scare tactics (PAT)
- [x] One CTA per email, sentence case, above the fold, aligned to the hero message
- [x] Subject lines ≤6 words, sentence case, no exclamation points
- [x] No puns, idioms, or humor tactics (owned-channels email hard-nos)
- [x] Gender-neutral trust stat ("500,000 patients")
- [ ] **Design/Braze to resolve:** ™ removal, ©2026, real pricing/discount values, dynamic cart contents, imagery swap, footer nav, disclaimer footer

---

## Change log

| Date | Change | Author |
|---|---|---|
| 2026-07-01 | Initial Labs Questionnaire + Cart abandon copy review. Pulled current copy from Figma (`P4Plx6tHNU9Op1D8bFqgSM`, nodes 6504:114 / 6504:273), infused Labs PAT marketing & positioning, aligned to Lifecycle Conversion Flow Framework + EMB v2.0. One message + one benefit + one above-the-fold CTA per email. | lifecycle-creative |
