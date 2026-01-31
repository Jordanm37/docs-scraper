---
title: Config - Clawdbot
url: https://docs.clawd.bot/cli/config
---

# [​](#clawdbot-config) `clawdbot config`

Config helpers: get/set/unset values by path. Run without a subcommand to open
the configure wizard (same as `clawdbot configure`).

## [​](#examples) Examples

Copy

```
clawdbot config get browser.executablePath
clawdbot config set browser.executablePath "/usr/bin/google-chrome"
clawdbot config set agents.defaults.heartbeat.every "2h"
clawdbot config set agents.list[0].tools.exec.node "node-id-or-name"
clawdbot config unset tools.web.search.apiKey
```

## [​](#paths) Paths

Paths use dot or bracket notation:

Copy

```
clawdbot config get agents.defaults.workspace
clawdbot config get agents.list[0].id
```

Use the agent list index to target a specific agent:

Copy

```
clawdbot config get agents.list
clawdbot config set agents.list[1].tools.exec.node "node-id-or-name"
```

## [​](#values) Values

Values are parsed as JSON5 when possible; otherwise they are treated as strings.
Use `--json` to require JSON5 parsing.

Copy

```
clawdbot config set agents.defaults.heartbeat.every "0m"
clawdbot config set gateway.port 19001 --json
clawdbot config set channels.whatsapp.groups '["*"]' --json
```

Restart the gateway after edits.