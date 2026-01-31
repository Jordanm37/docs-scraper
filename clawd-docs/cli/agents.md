---
title: Agents - Clawdbot
url: https://docs.clawd.bot/cli/agents
---

# [​](#clawdbot-agents) `clawdbot agents`

Manage isolated agents (workspaces + auth + routing).
Related:

* Multi-agent routing: [Multi-Agent Routing](/concepts/multi-agent)
* Agent workspace: [Agent workspace](/concepts/agent-workspace)

## [​](#examples) Examples

Copy

```
clawdbot agents list
clawdbot agents add work --workspace ~/clawd-work
clawdbot agents set-identity --workspace ~/clawd --from-identity
clawdbot agents set-identity --agent main --avatar avatars/clawd.png
clawdbot agents delete work
```

## [​](#identity-files) Identity files

Each agent workspace can include an `IDENTITY.md` at the workspace root:

* Example path: `~/clawd/IDENTITY.md`
* `set-identity --from-identity` reads from the workspace root (or an explicit `--identity-file`)

Avatar paths resolve relative to the workspace root.

## [​](#set-identity) Set identity

`set-identity` writes fields into `agents.list[].identity`:

* `name`
* `theme`
* `emoji`
* `avatar` (workspace-relative path, http(s) URL, or data URI)

Load from `IDENTITY.md`:

Copy

```
clawdbot agents set-identity --workspace ~/clawd --from-identity
```

Override fields explicitly:

Copy

```
clawdbot agents set-identity --agent main --name "Clawd" --emoji "🦞" --avatar avatars/clawd.png
```

Config sample:

Copy

```
{
  agents: {
    list: [
      {
        id: "main",
        identity: {
          name: "Clawd",
          theme: "space lobster",
          emoji: "🦞",
          avatar: "avatars/clawd.png"
        }
      }
    ]
  }
}
```