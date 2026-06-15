# Rugiet Ready Welcome Flow Analysis

**Date:** 2026-06-13
**Source:** [Welcome Emails_6/12](https://www.figma.com/design/luQdtOfoEljv6TPkwegtFR/LCM-Rebrand-System?node-id=3669-9443)
**References:** Email Marketing Bible v2.0, Rugiet Copywriting Skill (compliance, tone-of-voice, owned-channels), Email Sequences Skill (rugiet-marketing-claude)
**Status:** Analysis complete — pending implementation

---

## Current state: 11 emails

| # | Figma name | Subject line | Primary job |
|---|---|---|---|
| 01 | Ready_Welcome_01 | You're one step away. Save 15% now. | Hook / abandoned browse |
| 02 | Ready_Welcome_02 | I've used every ED product out there. Nothing comes close. | Social proof (testimonials) |
| 03 | Ready_Welcome_03 | Get 5-in-1 performance, have more sex | Comparison + differentiation |
| 04 | Ready_Welcome_04 | Get confident. Get the performance to back it up. | Social proof (85% stat) |
| 05 | Ready_Welcome_05 | More satisfaction for you and for your partner | Partner satisfaction / social proof |
| 06 | Ready_Welcome_06 | Get 15% off Ready™ | Pure discount |
| 07 | Ready_Welcome_07 | Your sex life, now with more enjoyment | Mechanism (apomorphine + ingredients) |
| 08 | Ready_Welcome_08 | Your dose, built around you | Personalization (compounding) |
| 09 | Ready_Welcome_09 | Apomorphine changes everything | Mechanism (three medications + comparison) |
| 10 | Ready_Welcome_10 | What over 500,000 men already know about better sex | Social proof + benefits summary |
| 11 | Ready_Welcome_11 | Here's how Ready™ works | Expectation-setting (dosing, side effects) |

### Flow composition breakdown

- **Social proof emails:** 4 (02, 04, 05, 10) — overdone; the reader sees a new stat or testimonial grid almost every other email
- **Mechanism/science emails:** 3 (07, 09, and partly 03) — redundant; emails 07 and 09 both explain the three-ingredient formula and apomorphine
- **Comparison/differentiation:** 2 (03, 09) — both include Ready vs. generic comparison tables
- **Discount/conversion:** 2 (01, 06) — plus every other email has the same 15% banner
- **Expectation-setting:** 1 (11) — buried last, where it does the least good
- **Personalization:** 1 (08) — the genuinely distinct angle in the flow

---

## Critical issues

### 1. The "3-in-1" vs "5-in-1" inconsistency

The flow contradicts itself on Rugiet Ready's core claim.

| Email | What it says |
|---|---|
| 02 | "5 benefits in 1, targeting both the physical and neurological sides of arousal" |
| 03 | Subject line: "Get 5-in-1 performance." Hero section: "The 5-in-1 difference" |
| 09 | Comparison table: "3-in-1 formula" (vs single ingredient) |
| 09 | "Ready™'s 3-in-1 formula addresses what's happening in your body and your brain" |

A reader receiving these 11 emails over 2-3 weeks sees the product called two different things. It reads as either careless or uncertain about the product itself.

**Resolution:** Adopt "3 medications. 5 benefits. 1 dose." as the canonical line. The number 3 is factually anchored to the ingredients (sildenafil, tadalafil, apomorphine). The number 5 maps to the benefit claims. Use consistently everywhere. Never say "3-in-1" or "5-in-1" alone again.

### 2. Compliance violations

| Location | Issue | Rule violated | Fix |
|---|---|---|---|
| Email 04 body | "as fast as 15 minutes" | compliance.md §4: onset language must be "as little as," never "as fast as" | Replace with "as little as 15 minutes" |
| Email 04 hero | "Ready®" used standalone | Per trademark-usage.md: "Ready" alone is unregistered and gets ™ only. ® is reserved for "Rugiet Ready®" (full product name). | Change standalone "Ready®" to "Ready™" on first mention, then no symbol |
| Email 05 hero | "2.5 million satisfied partners agree" | Unsubstantiated claim; no data source for 2.5M partners | Replace with "Over 500,000 men trust Ready" |
| Email 05 testimonial | "This medication has been an honest to God miracle for me" | compliance.md §2: "miracle" is prohibited | Remove testimonial or edit to remove "miracle" |
| Email 05 testimonial | "Holy crap!!! Need I say more?" | owned-channels.md: no exclamation points, ever | Remove or replace testimonial |
| Email 10 hero | "It works quick, and it keeps working for several days" | compliance.md §4-5: "works quick" is non-compliant onset language; "several days" overstates the "up to 36 hours" claim | Replace with compliant customer quote using conditional language |
| Email 06 preheader | "For a limited time" | No actual expiration — weakest possible urgency; technically misleading | Either set a real expiry or remove the claim |

### 3. Structural problems

**The expectation-setting email (11) is buried at the end.** This is the strongest trust-builder in the flow. It answers the three questions that block purchase:
- How does it work? (sublingual, dissolves in 5-10 minutes)
- What will I feel? (kicks in fast, as little as 15 minutes)
- What are the side effects? (headaches, nasal congestion, flushing — typically mild)

Per the Email Marketing Bible §4 (Welcome Series framework): "Email 4 (Day 7): Best content/product using segmentation data." The expectation email should land mid-flow (position 4-5), not at the end. Side-effect honesty is the single most effective conversion lever for a hesitant pharma buyer because it demonstrates transparency.

**Two mechanism emails say the same thing.** Email 07 ("Sex just got more enjoyable") and Email 09 ("Apomorphine changes everything") both explain the three-ingredient formula, both break down apomorphine/sildenafil/tadalafil, and both include an ingredient section with the same information. One strong mechanism email is better than two repetitive ones.

**Social proof is scattered without narrative arc.** Emails 02, 04, 05, and 10 all lean on "500,000 men" or "500k+" with slight variations. The reader sees the same anchor number four times with diminishing returns. Per EMB §5 (Copywriting): specificity creates credibility, but repetition of the same stat erodes it.

**The 15% discount banner on every email undermines trust emails.** When an email's job is to build credibility (mechanism, expectation-setting, personalization), stapling a coupon to the top says "this is a sales email" before the reader even gets to the content. Per EMB §4 (Abandoned Cart): "Email 1: Simple reminder. NO discount." and "Treat cart abandonment as a conversation, not a reminder." The same principle applies to trust-building emails in a welcome flow.

### 4. Same-couple imagery

Every email except 07 (which has some ingredient/pill close-ups) and 11 (which has a solo older man) uses the same couple in the same intimate setting. By email 4-5, the reader has seen this couple enough that the imagery stops registering. Per EMB §17 (Email Design Best Practices): "Product photography is the highest-performing visual element in email" and diverse visual language is more engaging than repetitive stock.

**This is a global issue across the brand**, not just the welcome flow. Needs a dedicated photo shoot or curated stock library showing different couples, ages, and settings.

---

## Recommended 8-email structure

The CEO's proposed restructure is sound. Here it is with best-practice layering from the Email Marketing Bible and Rugiet's own copywriting/compliance rules.

### Email 1: Welcome / Set the hook
**Current:** Email 01 ("You're close, finish what you started")
**Action:** Keep, refine

This email works — a browse-abandon-style hook is the right opener for someone who signed up while browsing Ready. Keep it short.

**Adjustments:**
- Keep the 15% offer here — this is a conversion email, the discount belongs
- Clean up the body copy: "You looked at Ready for a reason. Your best sex is waiting, and right now it's 15% off" is fine but can be tighter
- Ensure the product descriptor section uses the canonical "3 medications. 5 benefits. 1 dose." line
- Per EMB §4: welcome email should include a reply prompt or segmentation question (currently missing). Consider adding "Reply with any questions — our team reads every one" above the Questions CTA

**Discount banner:** YES — this is a conversion email
**Image:** Keep current hero, but start differentiating from email 2 onward

---

### Email 2: Differentiation
**Current:** Email 03 ("Don't settle for good enough") — resequenced to position 2
**Action:** Move up, refine

The comparison table (Ready vs. generic sildenafil/tadalafil) answers the real competitive question early: "Why wouldn't I just get a $2 generic?" This belongs in position 2, not buried mid-flow.

**Adjustments:**
- Fix the "5-in-1" language throughout. The comparison table row should read "3 medications, 5 benefits" not "Multi benefit (5-in-1)"
- The "Works in <15 mins*" row needs the asterisk and compliant phrasing "Works in as little as 15 minutes*"
- Remove the body testimonials (social proof belongs in its own email, not here — this email's job is differentiation)
- Remove the repeated "Start having better sex / 500,000+ men trust Rugiet" section at the bottom — it dilutes the comparison message
- Per owned-channels.md: one CTA per email. This email currently has UPGRADE YOUR PERFORMANCE + GET READY™ NOW. Pick one

**Discount banner:** YES — early in the flow, still converting
**Image:** New couple or product-focused shot (the comparison table IS the visual)

---

### Email 3: Mechanism
**Current:** Merge of Email 07 ("Sex just got more enjoyable" / apomorphine) and Email 09 ("Three medications. One little dose.")
**Action:** Merge into one strong mechanism email

These are the same email told twice. One strong mechanism email with the ingredient breakdown and chemical structure visuals (from email 07's format) is better than two redundant ones.

**Structure for the merged email:**
- Hero: "Three medications. One little dose." (from email 09 — cleaner headline)
- Lead: apomorphine differentiation ("Unlike traditional ED meds, Ready™ activates your dopamine pathways with apomorphine")
- Ingredient breakdown: apomorphine, sildenafil, tadalafil with images (from email 07's format)
- Sublingual absorption section (from email 07)
- Close: "3 medications. 5 benefits. 1 dose." (canonical line)
- Single CTA: GET STARTED WITH READY™

**Adjustments:**
- Drop the comparison table (it already appeared in email 2)
- Drop "Trusted by over 500,000 men" (that stat belongs in email 5)
- Per compliance.md: conditional verbs on all benefit claims ("helps prime the brain" not "primes the brain")
- Per owned-channels.md: no discount banner on trust emails

**Discount banner:** NO — this is a trust/education email. The coupon undermines clinical credibility.
**Image:** Product close-ups, ingredient/chemistry visuals — not the couple

---

### Email 4: Expectation-setting
**Current:** Email 11 ("What you can expect") — moved from position 11 to position 4
**Action:** Move dramatically forward in the flow

This is the best email in the flow and it is wasted at the end. Move it to mid-flow. The side-effect honesty ("headaches, nasal congestion, flushing — typically mild") is what makes a hesitant purchaser trust the brand, and it answers the questions that block purchase.

**Adjustments:**
- Per compliance.md: verify that "Works in as little as 15 minutes*" has the full disclaimer
- The "Dosing is simple" section is strong and practical. Keep it
- The "Side effects are mild" section is the star. Lead with it more prominently — consider making it higher in the email
- The orange CTA box ("Experiences may vary, so talk to your doctor...") is good compliance language
- Per EMB §4: this email should "set expectations + preference centre link"
- Per owned-channels.md: no humor tactics, no multiple CTAs — this email nails both

**Discount banner:** NO — this is the primary trust email. A coupon stapled to a side-effects-honesty email is tone-deaf.
**Image:** The solo older man image (email 11 current) is the right choice here — serious, direct

---

### Email 5: Social proof blowout
**Current:** Consolidation of emails 02, 04, 05, and 10 into one curated testimonial email
**Action:** Build new from best pieces

Four emails doing social proof is three too many. One email with the best curated (compliant) testimonials anchored by "Over 500,000 men trust Ready" is the right format.

**Structure:**
- Hero: "Over 500,000 men trust Ready™" (the right anchor, per CEO)
- 4-6 of the strongest compliant testimonials, curated from the existing pool
- Each testimonial with "— Verified patient" attribution
- Close with CTA

**Testimonials to keep (after compliance cleaning):**
- "This is the only medication that has ever worked for me. And it works every single time." (strong, specific)
- "I've used every ED product out there. Nothing comes close." (comparative, credible)
- "Like turning the clock back 30 years. I'm 74, and it works great." (age-specific, relatable)
- "I've tried every form, every brand. Nothing holds a candle to Rugiet..." (the apomorphine mention is strong clinical detail)

**Testimonials to cut:**
- "I feel like a teenager again...honest to God miracle for me" — "miracle" is prohibited per compliance.md
- "Holy crap!!! Need I say more?" — exclamation points violate format rules; low-information content
- "Outstanding service and outstanding medication. Works everytime and it's long lasting." — generic, no specificity
- Any testimonial referencing "2.5 million satisfied partners" — unsubstantiated claim

**Adjustments:**
- Each testimonial needs: "Customer's results have not been independently verified. Individual results may vary." (per compliance.md §1)
- Drop the "2.5 million satisfied partners" claim entirely. The "500,000 men" number is strong enough
- Per EMB §17: "Specificity creates credibility" — favor testimonials with specific details (age, duration of use, named comparison)

**Discount banner:** YES — social proof + offer is a natural conversion pair
**Image:** Multiple different couples/men — this is the email that most needs visual diversity

---

### Email 6: Personalization
**Current:** Email 08 ("Compounded Precision / Your dose, built around you")
**Action:** Keep as-is with minor refinements

This is a genuinely distinct angle that no other email covers. The compounding/personalization message is Rugiet's strongest TRT-adjacent differentiator applied to sexual health. Per owned-channels.md: "TRT: Personalization first — doctor-designed, built around your biology."

**Adjustments:**
- The headline "COMPOUNDED PRECISION" is strong. Keep it
- The body copy is clean: "Standard ED prescriptions come in fixed doses. Ready™ is different. Our doctors compound each formula based on your health profile to match what your body actually needs." — this is exactly the right register per tone-of-voice.md
- Remove the "Take control today. Get 15% off with code 5XFAST" text block at the bottom — it cheapens the personalization message
- Per owned-channels.md: one CTA. Currently has GET YOUR CUSTOM RX + GET STARTED. Pick one (GET YOUR CUSTOM RX is better — more specific, per channel guidelines)

**Discount banner:** NO — this is a trust/personalization email. The personalization pitch ("built for your body") is undermined when paired with a generic coupon.
**Image:** Needs a new image — currently the same couple again. A doctor/pharmacy/lab visual would reinforce the "custom Rx" message

---

### Email 7: Confidence / partner angle
**Current:** Merge of Email 04 (85% confidence stat) and Email 05 (partner satisfaction)
**Action:** Collapse into one relationship-focused email

The CEO's framing is right: "this is about your relationship, not just your equipment." The 85% stat and the partner angle are two halves of the same story.

**Structure:**
- Hero: lead with the relationship angle, not the stat
- Headline direction: "It's not just about you" or "She noticed first" (per TOV boldness test — is there something true here nobody else says? Yes: men don't buy ED meds for themselves alone)
- The 85% stat as supporting proof, not the headline
- 1-2 partner-focused testimonials (clean up any that reference "2.5 million")
- Close with emotional register: the dinner-party-guy is comfortable talking about the relationship impact

**Adjustments:**
- Drop the "2.5 million satisfied partners" line entirely
- Fix the stray "Ready®" — change to "Ready™"
- Fix "as fast as 15 minutes" — change to "as little as 15 minutes"
- Per tone-of-voice.md: "The emotional contract underneath every Rugiet communication: you haven't peaked. You've just been underserved." This email should embody that
- Per compliance.md: the 85% stat needs a source citation and "Individual results may vary"

**Discount banner:** NO — trust email. Concentrate the offer in emails 1, 5, and 8.
**Image:** A different couple than email 1. Ideally a photo that communicates connection, not just physicality

---

### Email 8: Closer
**Current:** Email 06 ("Get 15% off Ready™") — moved to final position
**Action:** Strengthen with real urgency

The pure discount email belongs at the end, but it needs urgency it currently lacks. "For a limited time" with no actual limit is the weakest urgency possible.

**Adjustments:**
- Either the code expires (say when — "Your code 5XFAST expires in 72 hours") or this email needs a reason to exist beyond repetition
- Per EMB §4 (Conversion sequence): "Urgency — only if authentic" and "Email 7: Direct Pitch — create urgency if authentic"
- The mood lighting joke ("The best thing to happen to your sex life since you discovered mood lighting") violates owned-channels.md: "No humor tactics. Humor dilutes credibility here."
- Rewrite the body to be direct: summarize what they've learned across the flow, restate the core value prop ("3 medications. 5 benefits. 1 dose."), give the offer with a real deadline
- Per owned-channels.md: the CTA should be active and specific. "START SAVING NOW" is okay. "Get your first month of Ready — 15% off" is better
- Consider: "Buy 2 months of Ready, get 1 free" as an alternative to the percentage discount (higher perceived value, commitment-based)

**Discount banner:** YES — this IS the discount email
**Image:** Product shot or new couple. Not the same hero from email 1

---

## Revised flow at a glance

| Position | Job | Discount banner? | Notes |
|---|---|---|---|
| 1 | Welcome / hook | YES | Short. Set the tone. 15% offer. |
| 2 | Differentiation | YES | Comparison table. Why not generic? |
| 3 | Mechanism | NO | One strong science email. Ingredients + apomorphine. |
| 4 | Expectation-setting | NO | The trust anchor. Side effects, dosing, timeline. |
| 5 | Social proof | YES | Curated testimonials. "Over 500,000 men trust Ready." |
| 6 | Personalization | NO | Compounded Precision. Your dose, your body. |
| 7 | Confidence/partner | NO | Relationship angle. 85% stat as proof, not headline. |
| 8 | Closer | YES | Real urgency. Code expires. Clear CTA. |

**Offer concentration:** Emails 1, 2, 5, and 8 carry the discount. Emails 3, 4, 6, and 7 are trust emails — no coupon banner.

---

## Additional best practice gaps (beyond CEO feedback)

### 1. No reply prompt in the welcome email
Per EMB §4 and §7: "Ask for replies in welcome email" — replies are the strongest signal for Gmail primary tab placement. Email 01 should include a reply prompt ("Questions? Reply to this email — our care team reads every one").

### 2. No preference center link
Per EMB §4: Welcome email 6 (Day 14) should "set expectations + preference centre link." None of the 11 emails offer a preference center or frequency control. This is a missed opportunity and a deliverability risk.

### 3. Subject lines exceed the 6-word rule
Per owned-channels.md: "Six words or fewer wherever possible." Most subject lines in the current flow are 8-12 words. Examples:
- "I've used every ED product out there. Nothing comes close." (12 words)
- "What over 500,000 men already know about better sex" (9 words)

Recommended rewrites:
- "Nothing else comes close" (4 words)
- "500,000 men switched. Here's why" (5 words)

### 4. Multiple CTAs in several emails
Per owned-channels.md: "One CTA per email." Several emails have 2-3 CTAs (GET STARTED + GET READY + CONTACT US). Pick one primary action per email.

### 5. "Performance Medicine For Men™" tagline in every footer — trademark risk
Per trademark-usage.md: "Performance Medicine For Men" is **pending and contested** — another party has already claimed it. The guide says: "Do not add ® or ™ to this phrase anywhere." The current emails show it with ™, which is incorrect. Remove the ™ symbol. Additionally, the guide warns against prominent placement until permission is confirmed — monitor legal status.

### 6. Missing send timing and cadence data
The Figma designs show email content but no cadence/timing information. Per EMB §4:
- Welcome series should span 1-2 weeks (not longer)
- Recommended timing: Day 0, 1, 3, 5, 7, 9, 12, 14
- B2C best send times: 7-9 AM or 7-9 PM recipient timezone

### 7. No behavioral branching
Per EMB §4 (Sequence Architecture — The Branch pattern): if a subscriber clicks a CTA in email 2 or 3, they should enter a shorter conversion path rather than receiving all 8 emails. The current flow is a straight-line sequence with no behavioral logic.

---

## Immediate action items (do first)

1. **Fix compliance violations now** — the "as fast as" phrasing, "miracle" testimonial, "2.5M partners" claim, and "Ready®" trademark are live compliance risks
2. **Adopt "3 medications. 5 benefits. 1 dose."** as the canonical product descriptor — update every email where "3-in-1" or "5-in-1" appears alone
3. **Move email 11 (expectation-setting) to position 4** — this change alone will likely improve conversion from the flow
4. **Strip the discount banner from emails 3, 4, 6, 7** (mechanism, expectation-setting, personalization, confidence) — trust emails should not have coupons
5. **Set a real expiry on the closer email** — "Your code expires [date]" or remove the urgency language entirely
6. **Commission new photography** — the same-couple problem is a global brand issue that undermines every email past the second one

---

## Compliance checklist for revised flow

Run before publishing any revised email:

- [ ] Standalone "Ready" uses ™ on first mention only (never ®). Full "Rugiet Ready" uses ® on first mention only. After first mention, no symbol needed. Per trademark-usage.md.
- [ ] Onset language is "works in as little as 15 minutes" — never "as fast as," never "in less than"
- [ ] Duration claims use "up to 36 hours"
- [ ] Product descriptor is "3 medications. 5 benefits. 1 dose." — not "3-in-1" or "5-in-1" alone
- [ ] Social proof anchor is "Over 500,000 men" — not "2.5 million partners"
- [ ] "Miracle" does not appear in any testimonial
- [ ] No exclamation points anywhere
- [ ] Conditional verbs on all benefit claims (can, may, helps, designed to)
- [ ] Testimonials carry "Customer's results have not been independently verified. Individual results may vary."
- [ ] FDA compounding disclaimer present in footer
- [ ] No absolute or guaranteed claims
- [ ] One CTA per email
- [ ] Subject lines 6 words or fewer

---

## Change log

| Date | Change | Author |
|---|---|---|
| 2026-06-13 | Initial analysis incorporating CEO feedback, EMB best practices, rugiet-copywriting compliance/tone/channel rules, and email-sequences methodology | lifecycle-creative |
