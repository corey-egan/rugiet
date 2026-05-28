# Rugiet Lifecycle

Operating repo for Rugiet's lifecycle and retention work. Powers the copywriting and creative agents used by the lifecycle team.

## Getting set up

1. Clone the repo and open it in Cursor (or your editor of choice).
2. Install Claude Code if you haven't: `npm install -g @anthropic-ai/claude-code`
3. From the repo root, run `claude` to start an interactive session.
4. The `lifecycle-creative` agent and the `rugiet-copywriting` / `rugiet-design-system` skills load automatically when relevant.

## Repo structure

```
rugiet-lifecycle/
├── CLAUDE.md                      ← the front door, loaded into every session
├── README.md                      ← this file
├── .gitignore
├── .claude/
│   ├── agents/
│   │   └── lifecycle-creative.md
│   └── skills/
│       ├── rugiet-copywriting/
│       │   ├── SKILL.md
│       │   └── references/
│       │       ├── compliance.md
│       │       ├── tone-of-voice.md
│       │       └── owned-channels.md
│       └── rugiet-design-system/
│           ├── SKILL.md
│           └── references/        ← (empty for now; fill in as needed)
├── briefs/                        ← drop briefs here for the creative agent
│   └── _template.md
├── outputs/
│   ├── creative/                  ← agent-generated drafts
│   ├── analyses/                  ← future analyst output
│   └── strategy/                  ← future strategy output
└── reference/
    └── decisions.md               ← log durable decisions here
```

## Day-to-day workflow

1. Copy `briefs/_template.md` to `briefs/YYYY-MM-DD_campaign-name.md` and fill it in.
2. Open Claude Code in the repo: `claude`
3. Ask: "Run the lifecycle-creative agent on the latest brief."
4. Review the drafts in `outputs/creative/`.
5. Iterate. Commit good work.

## Adding to the system

- **New brand rule:** edit the right file in `.claude/skills/rugiet-copywriting/references/`. Commit.
- **New channel (push, SMS, in-app):** add a reference file (e.g., `lifecycle-channels.md`) and update the SKILL.md routing table.
- **New agent:** add a markdown file in `.claude/agents/`.
- **New durable decision:** append to `reference/decisions.md`.

## Source of truth

- Brand voice, compliance, channel docs: **this repo** (canonical).
- Visual design system: **Figma** — linked in `CLAUDE.md`, referenced via Figma MCP.
- Patient data, campaign data: **Snowflake / Braze**, referenced via MCP.

## Notes on connectors

This repo is designed to work with the following Cursor MCPs:
- **Figma** — live design tokens, component specs, layout values
- **Notion** — long-form brand docs that are still maintained in Notion
- **Google Drive** — signed-off creative, brand assets
- **Braze** — campaign management, sends, canvases (when MCP is set up)
- **Snowflake** — analytical work for the future analyst agent

Credentials for any of these go in `.claude/settings.local.json` (gitignored), never in the repo itself.
