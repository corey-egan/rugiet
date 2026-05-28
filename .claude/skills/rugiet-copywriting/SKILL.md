---
name: rugiet-copywriting
description: Rugiet's voice, tone, compliance rules, and channel operating logic for any patient-facing copy. Use BEFORE drafting any email, web, push, SMS, in-app, paid, packaging, or support copy. Loads compliance, voice, and channel-specific references on demand, and runs the compliance checklist on every draft.
---

# Rugiet Copywriting

This skill governs every word Rugiet publishes. Load the right references before drafting — don't approximate from memory.

## Order of precedence (non-negotiable)

1. **`references/compliance.md`** — legal floor. Cannot be overridden by tone or channel rules. Load on every drafting task.
2. **`references/tone-of-voice.md`** — authoritative voice. Sets who Rugiet is, who we talk to, and how.
3. **`references/owned-channels.md`** — translates TOV into operating rules for email and website.
4. **`references/lifecycle-channels.md`** *(when added)* — push, SMS, in-app.
5. **`references/paid-channels.md`** *(when added)* — paid social, ads, acquisition.

When voice and channel docs conflict, the channel doc wins (it has dialed TOV for that surface). When anything conflicts with compliance, compliance wins.

## Loading rules

- Any patient-facing copy → load `compliance.md` always.
- Email or website work → also load `owned-channels.md`.
- Push, SMS, in-app → load `lifecycle-channels.md` if it exists; surface the gap if it doesn't.
- Paid social or ads → load `paid-channels.md` if it exists; surface the gap if it doesn't.
- Voice feels off or needs calibration → load `tone-of-voice.md`.

Load files in full.

## Universal rules (always-on)

**Compliance hard rules:**

- Conditional verbs on benefit claims (*can, may, helps, designed to, supports, formulated to*).
- Onset language: "works in as little as 15 minutes" — never "as fast as," never "in less than."
- Rugiet Ready 15-minute claim requires the full disclaimer (see `compliance.md` §1).
- "Up to" on all duration claims.
- Never "guaranteed," "miracle," "fixes," "will solve."
- Never fabricate doctor quotes.
- Compounded products require the FDA compounding disclaimer.
- Testimonials require: "Customer's results have not been independently verified. Individual results may vary."
- Paid actors require "Actor portrayal" on screen for ≥5 seconds.
- On paid social: no 2nd-person health claims ("you have ED"), avoid "sex" in captions and hooks.

**Format rules (true in every channel):**

- Sentence case everywhere — headlines, subheads, buttons, CTAs.
- No exclamation points, anywhere, ever.
- Oxford commas. Active voice. Short sentences. Cut qualifiers.

## Voice essentials (universal)

- Rugiet is the dinner-party-guy: done well, looks good, knows it, doesn't announce it. Confident, direct, matter-of-fact, comfortable with topics other men avoid.
- Reader: man 45–65, has built something, has noticed a gap between how he feels and how he's capable of feeling. Wants facts and tools, not sympathy.
- Customer mindset: aspirational mirror, not a broken patient. **"You haven't peaked. You've been underserved."**
- Provocation is aimed at conventions and lies, never at the customer. Boldness test: *is there something true here that nobody else is willing to say?* If yes, say it. If just loud, cut it.
- Humor reference: 70s Playboy editorial — cultured, confident, adult. Knowing wink, not college bro. Smirk test: would a confident 50-year-old smirk or roll his eyes?

## Product positioning shortcuts

- **Go Long:** PE is the marquee. ED is body copy only — never in headlines, subject lines, or hero copy.
- **TRT:** Personalization first (doctor-designed, built around your biology). Lab testing is a feature, not the headline.
- **Longevity (NAD+, Sermorelin, Lipo-C, L-Carnitine, Glutathione):** Optimization register. Frame upgrade and capability, never deficiency or decline.
- **Rugiet Ready:** Exact onset phrasing is "works in as little as 15 minutes." Always paired with the full 15-minute disclaimer.

## Required workflow on every draft

1. Identify the channel. Load the right references.
2. Draft.
3. Run the **compliance checklist** (§3 of `compliance.md`) — the compliance doc explicitly says to run it on every draft.
4. For email and website work, run the **self-check** at the end of `owned-channels.md`.
5. If any Rugiet Ready copy appears, check it against the **claims cheat-sheet** (§4 of `compliance.md`).
6. If anything fails any check, fix before delivering.
