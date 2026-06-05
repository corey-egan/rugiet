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

---

_(Add new entries above this line.)_
