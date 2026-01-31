---
title: Approvals - Clawdbot
url: https://docs.clawd.bot/cli/approvals
---

# [​](#clawdbot-approvals) `clawdbot approvals`

Manage exec approvals for the **local host**, **gateway host**, or a **node host**.
By default, commands target the local approvals file on disk. Use `--gateway` to target the gateway, or `--node` to target a specific node.
Related:

* Exec approvals: [Exec approvals](/tools/exec-approvals)
* Nodes: [Nodes](/nodes)

## [​](#common-commands) Common commands

Copy

```
clawdbot approvals get
clawdbot approvals get --node <id|name|ip>
clawdbot approvals get --gateway
```

## [​](#replace-approvals-from-a-file) Replace approvals from a file

Copy

```
clawdbot approvals set --file ./exec-approvals.json
clawdbot approvals set --node <id|name|ip> --file ./exec-approvals.json
clawdbot approvals set --gateway --file ./exec-approvals.json
```

## [​](#allowlist-helpers) Allowlist helpers

Copy

```
clawdbot approvals allowlist add "~/Projects/**/bin/rg"
clawdbot approvals allowlist add --agent main --node <id|name|ip> "/usr/bin/uptime"
clawdbot approvals allowlist add --agent "*" "/usr/bin/uname"

clawdbot approvals allowlist remove "~/Projects/**/bin/rg"
```

## [​](#notes) Notes

* `--node` uses the same resolver as `clawdbot nodes` (id, name, ip, or id prefix).
* `--agent` defaults to `"*"`, which applies to all agents.
* The node host must advertise `system.execApprovals.get/set` (macOS app or headless node host).
* Approvals files are stored per host at `~/.clawdbot/exec-approvals.json`.