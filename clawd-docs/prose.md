---
title: Prose - Clawdbot
url: https://docs.clawd.bot/prose
---

# [​](#openprose) OpenProse

OpenProse is a portable, markdown-first workflow format for orchestrating AI sessions. In Clawdbot it ships as a plugin that installs an OpenProse skill pack plus a `/prose` slash command. Programs live in `.prose` files and can spawn multiple sub-agents with explicit control flow.
Official site: <https://www.prose.md>

## [​](#what-it-can-do) What it can do

* Multi-agent research + synthesis with explicit parallelism.
* Repeatable approval-safe workflows (code review, incident triage, content pipelines).
* Reusable `.prose` programs you can run across supported agent runtimes.

## [​](#install-+-enable) Install + enable

Bundled plugins are disabled by default. Enable OpenProse:

Copy

```
clawdbot plugins enable open-prose
```

Restart the Gateway after enabling the plugin.
Dev/local checkout: `clawdbot plugins install ./extensions/open-prose`
Related docs: [Plugins](/plugin), [Plugin manifest](/plugins/manifest), [Skills](/tools/skills).

## [​](#slash-command) Slash command

OpenProse registers `/prose` as a user-invocable skill command. It routes to the OpenProse VM instructions and uses Clawdbot tools under the hood.
Common commands:

Copy

```
/prose help
/prose run <file.prose>
/prose run <handle/slug>
/prose run <https://example.com/file.prose>
/prose compile <file.prose>
/prose examples
/prose update
```

## [​](#example:-a-simple-prose-file) Example: a simple `.prose` file

Copy

```
# Research + synthesis with two agents running in parallel.

input topic: "What should we research?"

agent researcher:
  model: sonnet
  prompt: "You research thoroughly and cite sources."

agent writer:
  model: opus
  prompt: "You write a concise summary."

parallel:
  findings = session: researcher
    prompt: "Research {topic}."
  draft = session: writer
    prompt: "Summarize {topic}."

session "Merge the findings + draft into a final answer."
context: { findings, draft }
```

## [​](#file-locations) File locations

OpenProse keeps state under `.prose/` in your workspace:

Copy

```
.prose/
├── .env
├── runs/
│   └── {YYYYMMDD}-{HHMMSS}-{random}/
│       ├── program.prose
│       ├── state.md
│       ├── bindings/
│       └── agents/
└── agents/
```

User-level persistent agents live at:

Copy

```
~/.prose/agents/
```

## [​](#state-modes) State modes

OpenProse supports multiple state backends:

* **filesystem** (default): `.prose/runs/...`
* **in-context**: transient, for small programs
* **sqlite** (experimental): requires `sqlite3` binary
* **postgres** (experimental): requires `psql` and a connection string

Notes:

* sqlite/postgres are opt-in and experimental.
* postgres credentials flow into subagent logs; use a dedicated, least-privileged DB.

## [​](#remote-programs) Remote programs

`/prose run <handle/slug>` resolves to `https://p.prose.md/<handle>/<slug>`.
Direct URLs are fetched as-is. This uses the `web_fetch` tool (or `exec` for POST).

## [​](#clawdbot-runtime-mapping) Clawdbot runtime mapping

OpenProse programs map to Clawdbot primitives:

| OpenProse concept | Clawdbot tool |
| --- | --- |
| Spawn session / Task tool | `sessions_spawn` |
| File read/write | `read` / `write` |
| Web fetch | `web_fetch` |

If your tool allowlist blocks these tools, OpenProse programs will fail. See [Skills config](/tools/skills-config).

## [​](#security-+-approvals) Security + approvals

Treat `.prose` files like code. Review before running. Use Clawdbot tool allowlists and approval gates to control side effects.
For deterministic, approval-gated workflows, compare with [Lobster](/tools/lobster).