# Rugiet Lifecycle Workspace

## What this repo is

This is the operating system for Rugiet's lifecycle and retention work. It contains the agents, skills, and reference knowledge that drive day-to-day creative and analytical execution across email, push, SMS, and in-app messaging.

## About Rugiet

Rugiet is a men's health brand offering prescription treatments across sexual health (Go Long, Rugiet Ready, Daily Boost, Grower), TRT, longevity (NAD+, Sermorelin, Lipo-C, L-Carnitine, Glutathione), sleep, weight loss, and hair.

Patients are typically men 45–65 who have built something — a career, a family, a life that matters — and have noticed a gap between how they feel and how they're capable of feeling. They don't want sympathy; they want facts and tools.

The brand voice is the dinner-party-guy: confident, direct, matter-of-fact, comfortable with topics other men avoid.

The emotional contract underneath every customer touch: **you haven't peaked, you've been underserved.**

## The stack

- **ESP:** Braze (workspace: _[TBD]_)
- **Warehouse:** Snowflake (account: _[TBD]_, primary schemas: _[TBD]_)
- **Product surfaces:** iOS app _[name TBD]_, web checkout
- **Patient support tool:** _[TBD]_
- **Design source of truth:** Figma — _[file URL TBD]_
- **Brand voice / compliance source of truth:** this repo (canonical)

## What "retention" means here

_[Define explicitly. Example: "90-day repeat purchase rate across Rx products, with subscription continuation past month 3 as the primary secondary metric." Without this definition, every agent will optimize for the wrong thing. Fill this in before doing any analytical work.]_

## Products at a glance

Product-specific rules that apply across every channel:

- **Go Long** — PE is the marquee benefit. ED is body copy only, never in headlines, subject lines, or hero copy.
- **Rugiet Ready** — onset language is exactly "works in as little as 15 minutes." Always paired with the full 15-minute disclaimer (see compliance ref).
- **TRT** — personalization first. Doctor-designed, built around the patient's biology. Lab testing is a feature, not the headline.
- **Longevity products** — optimization register, not deficiency. Frame upgrade and capability, never lack and decline.
- **Sexual health products** — plain language about sex and erections is permitted in owned channels (email, web); not in paid social.

## Agents in this repo

- `lifecycle-creative` — turns briefs in `briefs/` into draft copy for email, push, SMS, in-app. Output goes to `outputs/creative/`.

Future agents (not yet built):
- `lifecycle-analyst` — Braze + Snowflake data work
- `lifecycle-strategy` — cross-channel retention direction

## Skills in this repo

- `rugiet-copywriting` — voice, tone, compliance, channel rules for any patient-facing copy. Reference files: compliance, tone-of-voice, owned-channels.
- `rugiet-design-system` — visual design tokens, layout, photography direction. Pulls live from Figma via MCP when current values are needed.

## How to work in this repo

- Briefs go in `briefs/` — use `briefs/_template.md` as the starting structure.
- Agent outputs go in `outputs/creative/`, organized by date and brief.
- Durable knowledge goes in `reference/` — patient personas, retention goals, the decisions log. Agents read these freely.
- When a session produces a durable insight or decision, write it down in `reference/decisions.md` so the next session benefits.

## What's not in this repo

- Credentials (Braze API tokens, Snowflake creds, etc.) — these go in `.claude/settings.local.json` or `.env`, both gitignored.
- Live design tokens — Figma is the source of truth; we pull via MCP.
- PII or customer data — never commit this.
- Files synced from Claude.ai team projects — those aren't a durable source of truth. If something matters, copy it here.
