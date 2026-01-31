---
title: Setup - Clawdbot
url: https://docs.clawd.bot/start/setup
---

# [​](#setup) Setup

Last updated: 2026-01-01

## [​](#tl;dr) TL;DR

* **Tailoring lives outside the repo:** `~/clawd` (workspace) + `~/.clawdbot/clawdbot.json` (config).
* **Stable workflow:** install the macOS app; let it run the bundled Gateway.
* **Bleeding edge workflow:** run the Gateway yourself via `pnpm gateway:watch`, then let the macOS app attach in Local mode.

## [​](#prereqs-from-source) Prereqs (from source)

* Node `>=22`
* `pnpm`
* Docker (optional; only for containerized setup/e2e — see [Docker](/install/docker))

## [​](#tailoring-strategy-so-updates-don’t-hurt) Tailoring strategy (so updates don’t hurt)

If you want “100% tailored to me” *and* easy updates, keep your customization in:

* **Config:** `~/.clawdbot/clawdbot.json` (JSON/JSON5-ish)
* **Workspace:** `~/clawd` (skills, prompts, memories; make it a private git repo)

Bootstrap once:

Copy

```
clawdbot setup
```

From inside this repo, use the local CLI entry:

Copy

```
clawdbot setup
```

If you don’t have a global install yet, run it via `pnpm clawdbot setup`.

## [​](#stable-workflow-macos-app-first) Stable workflow (macOS app first)

1. Install + launch **Clawdbot.app** (menu bar).
2. Complete the onboarding/permissions checklist (TCC prompts).
3. Ensure Gateway is **Local** and running (the app manages it).
4. Link surfaces (example: WhatsApp):

Copy

```
clawdbot channels login
```

5. Sanity check:

Copy

```
clawdbot health
```

If onboarding is not available in your build:

* Run `clawdbot setup`, then `clawdbot channels login`, then start the Gateway manually (`clawdbot gateway`).

## [​](#bleeding-edge-workflow-gateway-in-a-terminal) Bleeding edge workflow (Gateway in a terminal)

Goal: work on the TypeScript Gateway, get hot reload, keep the macOS app UI attached.

### [​](#0-optional-run-the-macos-app-from-source-too) 0) (Optional) Run the macOS app from source too

If you also want the macOS app on the bleeding edge:

Copy

```
./scripts/restart-mac.sh
```

### [​](#1-start-the-dev-gateway) 1) Start the dev Gateway

Copy

```
pnpm install
pnpm gateway:watch
```

`gateway:watch` runs the gateway in watch mode and reloads on TypeScript changes.

### [​](#2-point-the-macos-app-at-your-running-gateway) 2) Point the macOS app at your running Gateway

In **Clawdbot.app**:

* Connection Mode: **Local**
  The app will attach to the running gateway on the configured port.

### [​](#3-verify) 3) Verify

* In-app Gateway status should read **“Using existing gateway …”**
* Or via CLI:

Copy

```
clawdbot health
```

### [​](#common-footguns) Common footguns

* **Wrong port:** Gateway WS defaults to `ws://127.0.0.1:18789`; keep app + CLI on the same port.
* **Where state lives:**
  + Credentials: `~/.clawdbot/credentials/`
  + Sessions: `~/.clawdbot/agents/<agentId>/sessions/`
  + Logs: `/tmp/clawdbot/`

## [​](#updating-without-wrecking-your-setup) Updating (without wrecking your setup)

* Keep `~/clawd` and `~/.clawdbot/` as “your stuff”; don’t put personal prompts/config into the `clawdbot` repo.
* Updating source: `git pull` + `pnpm install` (when lockfile changed) + keep using `pnpm gateway:watch`.

## [​](#linux-systemd-user-service) Linux (systemd user service)

Linux installs use a systemd **user** service. By default, systemd stops user
services on logout/idle, which kills the Gateway. Onboarding attempts to enable
lingering for you (may prompt for sudo). If it’s still off, run:

Copy

```
sudo loginctl enable-linger $USER
```

For always-on or multi-user servers, consider a **system** service instead of a
user service (no lingering needed). See [Gateway runbook](/gateway) for the systemd notes.

## [​](#related-docs) Related docs

* [Gateway runbook](/gateway) (flags, supervision, ports)
* [Gateway configuration](/gateway/configuration) (config schema + examples)
* [Discord](/channels/discord) and [Telegram](/channels/telegram) (reply tags + replyToMode settings)
* [Clawdbot assistant setup](/start/clawd)
* [macOS app](/platforms/macos) (gateway lifecycle)