---
name: rugiet-design-system
description: Rugiet's visual design system — color, typography, layout, photography direction, illustration usage, and component patterns for lifecycle creative (email, push, SMS, in-app). Use whenever generating or reviewing the visual side of a patient-facing asset, or when copy decisions depend on layout context (hero module, CTA placement, image vs. illustration).
---

# Rugiet Design System

## Source of truth

The canonical design system lives in Figma:

**[TODO: add Figma file URL]**

For current tokens, component states, or layout specs, query the Figma MCP rather than relying on cached values in this skill. Examples of what to ask Figma directly:

- "What's the current value of `color/brand/sand`?"
- "What components exist in the `Email/Hero` family?"
- "What's the standard button radius for email CTAs?"
- "What's the spacing token for module padding on PDPs?"

This SKILL.md holds durable visual *opinions* — the rules that don't change frequently and that an AI agent needs to internalize. Live values stay in Figma.

---

## Durable visual principles

_[Fill these in once. Suggested structure below — replace placeholders with actual Rugiet opinions.]_

### Color philosophy

_[Example: "Muted, clinical, never neon. Sand and ink are the workhorses. Accent colors used sparingly, never on primary CTAs."]_

### Typography philosophy

_[Example: "Serif for headlines, sans for body. Headlines never bold italic. Numerals always lining, never old-style."]_

### Photography direction

_[Example: "Real men in real settings. No stock. Natural light. The reader should see himself, not an aspirational stranger. No bedroom scenes in any channel."]_

### Illustration vs. photo

_[Example: "Photo for emotional or aspirational frames. Illustration for mechanism explainers (how the medicine works) and process flows. Never mix the two in a single email."]_

### Layout principles

_[Example: "White space is the primary emphasis tool. Bold sparingly. One CTA per email. PDP modules follow the order defined in owned-channels.md."]_

---

## Universal visual hard nos

- No exclamation points in any visual treatment (matches copy rule).
- No stock photography of "happy older couple" tropes.
- No medical iconography that implies certainty (no checkmarks on benefit claims, no "100%" badges).
- No bedroom or suggestive scenes — applies to all channels, strictest on paid social.
- Compounded products require visible compounding disclaimer in any asset that makes a benefit claim.

---

## When to load which reference

_(References to be added as the system matures.)_

- **Email template work** → `references/email-templates.md` (when created)
- **Push / SMS visual considerations** (sender ID, emoji policy, link preview) → `references/short-form-format.md` (when created)
- **Photography direction for a specific shoot or campaign** → `references/photo-direction.md` (when created)
- **In-app message visual specs** → `references/in-app-patterns.md` (when created)

---

## Cross-references with copywriting

This skill is the visual half. For the verbal half — voice, tone, compliance, what words can appear in headlines vs. body — use the `rugiet-copywriting` skill. The two are designed to work together; agents producing patient-facing assets typically load both.

---

## Workflow

1. Identify the surface (email, push, SMS, in-app, web).
2. Load any relevant references for that surface.
3. For live design tokens, query the Figma MCP — do not approximate from memory.
4. Apply the universal visual hard nos.
5. Cross-check against `rugiet-copywriting` if the deliverable includes copy (it almost always does).
