---
title: Zalouser - Clawdbot
url: https://docs.clawd.bot/channels/zalouser
---

# [​](#zalo-personal-unofficial) Zalo Personal (unofficial)

Status: experimental. This integration automates a **personal Zalo account** via `zca-cli`.
> **Warning:** This is an unofficial integration and may result in account suspension/ban. Use at your own risk.

## [​](#plugin-required) Plugin required

Zalo Personal ships as a plugin and is not bundled with the core install.

* Install via CLI: `clawdbot plugins install @clawdbot/zalouser`
* Or from a source checkout: `clawdbot plugins install ./extensions/zalouser`
* Details: [Plugins](/plugin)

## [​](#prerequisite:-zca-cli) Prerequisite: zca-cli

The Gateway machine must have the `zca` binary available in `PATH`.

* Verify: `zca --version`
* If missing, install zca-cli (see `extensions/zalouser/README.md` or the upstream zca-cli docs).

## [​](#quick-setup-beginner) Quick setup (beginner)

1. Install the plugin (see above).
2. Login (QR, on the Gateway machine):
   * `clawdbot channels login --channel zalouser`
   * Scan the QR code in the terminal with the Zalo mobile app.
3. Enable the channel:

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

4. Restart the Gateway (or finish onboarding).
5. DM access defaults to pairing; approve the pairing code on first contact.

## [​](#what-it-is) What it is

* Uses `zca listen` to receive inbound messages.
* Uses `zca msg ...` to send replies (text/media/link).
* Designed for “personal account” use cases where Zalo Bot API is not available.

## [​](#naming) Naming

Channel id is `zalouser` to make it explicit this automates a **personal Zalo user account** (unofficial). We keep `zalo` reserved for a potential future official Zalo API integration.

## [​](#finding-ids-directory) Finding IDs (directory)

Use the directory CLI to discover peers/groups and their IDs:

Copy

```
clawdbot directory self --channel zalouser
clawdbot directory peers list --channel zalouser --query "name"
clawdbot directory groups list --channel zalouser --query "work"
```

## [​](#limits) Limits

* Outbound text is chunked to ~2000 characters (Zalo client limits).
* Streaming is blocked by default.

## [​](#access-control-dms) Access control (DMs)

`channels.zalouser.dmPolicy` supports: `pairing | allowlist | open | disabled` (default: `pairing`).
`channels.zalouser.allowFrom` accepts user IDs or names. The wizard resolves names to IDs via `zca friend find` when available.
Approve via:

* `clawdbot pairing list zalouser`
* `clawdbot pairing approve zalouser <code>`

## [​](#group-access-optional) Group access (optional)

* Default: `channels.zalouser.groupPolicy = "open"` (groups allowed). Use `channels.defaults.groupPolicy` to override the default when unset.
* Restrict to an allowlist with:
  + `channels.zalouser.groupPolicy = "allowlist"`
  + `channels.zalouser.groups` (keys are group IDs or names)
* Block all groups: `channels.zalouser.groupPolicy = "disabled"`.
* The configure wizard can prompt for group allowlists.
* On startup, Clawdbot resolves group/user names in allowlists to IDs and logs the mapping; unresolved entries are kept as typed.

Example:

Copy

```
{
  channels: {
    zalouser: {
      groupPolicy: "allowlist",
      groups: {
        "123456789": { allow: true },
        "Work Chat": { allow: true }
      }
    }
  }
}
```

## [​](#multi-account) Multi-account

Accounts map to zca profiles. Example:

Copy

```
{
  channels: {
    zalouser: {
      enabled: true,
      defaultAccount: "default",
      accounts: {
        work: { enabled: true, profile: "work" }
      }
    }
  }
}
```

## [​](#troubleshooting) Troubleshooting

**`zca` not found:**

* Install zca-cli and ensure it’s on `PATH` for the Gateway process.

**Login doesn’t stick:**

* `clawdbot channels status --probe`
* Re-login: `clawdbot channels logout --channel zalouser && clawdbot channels login --channel zalouser`