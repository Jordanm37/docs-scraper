---
title: Getting started - Clawdbot
url: https://docs.clawd.bot/start/getting-started
---

# [​](#getting-started) Getting Started

Goal: go from **zero** → **first working chat** (with sane defaults) as quickly as possible.
Recommended path: use the **CLI onboarding wizard** (`clawdbot onboard`). It sets up:

* model/auth (OAuth recommended)
* gateway settings
* channels (WhatsApp/Telegram/Discord/Mattermost (plugin)/…)
* pairing defaults (secure DMs)
* workspace bootstrap + skills
* optional background service

If you want the deeper reference pages, jump to: [Wizard](/start/wizard), [Setup](/start/setup), [Pairing](/start/pairing), [Security](/gateway/security).
Sandboxing note: `agents.defaults.sandbox.mode: "non-main"` uses `session.mainKey` (default `"main"`),
so group/channel sessions are sandboxed. If you want the main agent to always
run on host, set an explicit per-agent override:

Copy

```
{
  "routing": {
    "agents": {
      "main": {
        "workspace": "~/clawd",
        "sandbox": { "mode": "off" }
      }
    }
  }
}
```

## [​](#0-prereqs) 0) Prereqs

* Node `>=22`
* `pnpm` (optional; recommended if you build from source)
* **Recommended:** Brave Search API key for web search. Easiest path:
  `clawdbot configure --section web` (stores `tools.web.search.apiKey`).
  See [Web tools](/tools/web).

macOS: if you plan to build the apps, install Xcode / CLT. For the CLI + gateway only, Node is enough.
Windows: use **WSL2** (Ubuntu recommended). WSL2 is strongly recommended; native Windows is untested, more problematic, and has poorer tool compatibility. Install WSL2 first, then run the Linux steps inside WSL. See [Windows (WSL2)](/platforms/windows).

## [​](#1-install-the-cli-recommended) 1) Install the CLI (recommended)

Copy

```
curl -fsSL https://clawd.bot/install.sh | bash
```

Installer options (install method, non-interactive, from GitHub): [Install](/install).
Windows (PowerShell):

Copy

```
iwr -useb https://clawd.bot/install.ps1 | iex
```

Alternative (global install):

Copy

```
npm install -g clawdbot@latest
```

Copy

```
pnpm add -g clawdbot@latest
```

## [​](#2-run-the-onboarding-wizard-and-install-the-service) 2) Run the onboarding wizard (and install the service)

Copy

```
clawdbot onboard --install-daemon
```

What you’ll choose:

* **Local vs Remote** gateway
* **Auth**: OpenAI Code (Codex) subscription (OAuth) or API keys. For Anthropic we recommend an API key; `claude setup-token` is also supported.
* **Providers**: WhatsApp QR login, Telegram/Discord bot tokens, Mattermost plugin tokens, etc.
* **Daemon**: background install (launchd/systemd; WSL2 uses systemd)
  + **Runtime**: Node (recommended; required for WhatsApp/Telegram). Bun is **not recommended**.
* **Gateway token**: the wizard generates one by default (even on loopback) and stores it in `gateway.auth.token`.

Wizard doc: [Wizard](/start/wizard)

### [​](#auth:-where-it-lives-important) Auth: where it lives (important)

* **Recommended Anthropic path:** set an API key (wizard can store it for service use). `claude setup-token` is also supported if you want to reuse Claude Code credentials.
* OAuth credentials (legacy import): `~/.clawdbot/credentials/oauth.json`
* Auth profiles (OAuth + API keys): `~/.clawdbot/agents/<agentId>/agent/auth-profiles.json`

Headless/server tip: do OAuth on a normal machine first, then copy `oauth.json` to the gateway host.

## [​](#3-start-the-gateway) 3) Start the Gateway

If you installed the service during onboarding, the Gateway should already be running:

Copy

```
clawdbot gateway status
```

Manual run (foreground):

Copy

```
clawdbot gateway --port 18789 --verbose
```

Dashboard (local loopback): `http://127.0.0.1:18789/`
If a token is configured, paste it into the Control UI settings (stored as `connect.params.auth.token`).
⚠️ **Bun warning (WhatsApp + Telegram):** Bun has known issues with these
channels. If you use WhatsApp or Telegram, run the Gateway with **Node**.

## [​](#3-5-quick-verify-2-min) 3.5) Quick verify (2 min)

Copy

```
clawdbot status
clawdbot health
```

## [​](#4-pair-+-connect-your-first-chat-surface) 4) Pair + connect your first chat surface

### [​](#whatsapp-qr-login) WhatsApp (QR login)

Copy

```
clawdbot channels login
```

Scan via WhatsApp → Settings → Linked Devices.
WhatsApp doc: [WhatsApp](/channels/whatsapp)

### [​](#telegram-/-discord-/-others) Telegram / Discord / others

The wizard can write tokens/config for you. If you prefer manual config, start with:

* Telegram: [Telegram](/channels/telegram)
* Discord: [Discord](/channels/discord)
* Mattermost (plugin): [Mattermost](/channels/mattermost)

**Telegram DM tip:** your first DM returns a pairing code. Approve it (see next step) or the bot won’t respond.

## [​](#5-dm-safety-pairing-approvals) 5) DM safety (pairing approvals)

Default posture: unknown DMs get a short code and messages are not processed until approved.
If your first DM gets no reply, approve the pairing:

Copy

```
clawdbot pairing list whatsapp
clawdbot pairing approve whatsapp <code>
```

Pairing doc: [Pairing](/start/pairing)

## [​](#from-source-development) From source (development)

If you’re hacking on Clawdbot itself, run from source:

Copy

```
git clone https://github.com/clawdbot/clawdbot.git
cd clawdbot
pnpm install
pnpm ui:build # auto-installs UI deps on first run
pnpm build
clawdbot onboard --install-daemon
```

If you don’t have a global install yet, run the onboarding step via `pnpm clawdbot ...` from the repo.
Gateway (from this repo):

Copy

```
node dist/entry.js gateway --port 18789 --verbose
```

## [​](#7-verify-end-to-end) 7) Verify end-to-end

In a new terminal, send a test message:

Copy

```
clawdbot message send --target +15555550123 --message "Hello from Clawdbot"
```

If `clawdbot health` shows “no auth configured”, go back to the wizard and set OAuth/key auth — the agent won’t be able to respond without it.
Tip: `clawdbot status --all` is the best pasteable, read-only debug report.
Health probes: `clawdbot health` (or `clawdbot status --deep`) asks the running gateway for a health snapshot.

## [​](#next-steps-optional,-but-great) Next steps (optional, but great)

* macOS menu bar app + voice wake: [macOS app](/platforms/macos)
* iOS/Android nodes (Canvas/camera/voice): [Nodes](/nodes)
* Remote access (SSH tunnel / Tailscale Serve): [Remote access](/gateway/remote) and [Tailscale](/gateway/tailscale)
* Always-on / VPN setups: [Remote access](/gateway/remote), [exe.dev](/platforms/exe-dev), [Hetzner](/platforms/hetzner), [macOS remote](/platforms/mac/remote)