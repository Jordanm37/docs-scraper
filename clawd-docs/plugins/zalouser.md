---
title: Zalouser - Clawdbot
url: https://docs.clawd.bot/plugins/zalouser
---

# [​](#zalo-personal-plugin) Zalo Personal (plugin)

Zalo Personal support for Clawdbot via a plugin, using `zca-cli` to automate a normal Zalo user account.
> **Warning:** Unofficial automation may lead to account suspension/ban. Use at your own risk.

## [​](#naming) Naming

Channel id is `zalouser` to make it explicit this automates a **personal Zalo user account** (unofficial). We keep `zalo` reserved for a potential future official Zalo API integration.

## [​](#where-it-runs) Where it runs

This plugin runs **inside the Gateway process**.
If you use a remote Gateway, install/configure it on the **machine running the Gateway**, then restart the Gateway.

## [​](#install) Install

### [​](#option-a:-install-from-npm) Option A: install from npm

Copy

```
clawdbot plugins install @clawdbot/zalouser
```

Restart the Gateway afterwards.

### [​](#option-b:-install-from-a-local-folder-dev) Option B: install from a local folder (dev)

Copy

```
clawdbot plugins install ./extensions/zalouser
cd ./extensions/zalouser && pnpm install
```

Restart the Gateway afterwards.

## [​](#prerequisite:-zca-cli) Prerequisite: zca-cli

The Gateway machine must have `zca` on `PATH`:

Copy

```
zca --version
```

## [​](#config) Config

Channel config lives under `channels.zalouser` (not `plugins.entries.*`):

Copy

```
{
  channels: {
    zalouser: {
      enabled: true,
      dmPolicy: "pairing"
    }
  }
}
```

## [​](#cli) CLI

Copy

```
clawdbot channels login --channel zalouser
clawdbot channels logout --channel zalouser
clawdbot channels status --probe
clawdbot message send --channel zalouser --target <threadId> --message "Hello from Clawdbot"
clawdbot directory peers list --channel zalouser --query "name"
```

## [​](#agent-tool) Agent tool

Tool name: `zalouser`
Actions: `send`, `image`, `link`, `friends`, `groups`, `me`, `status`