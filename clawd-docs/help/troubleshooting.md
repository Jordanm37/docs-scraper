---
title: Troubleshooting - Clawdbot
url: https://docs.clawd.bot/help/troubleshooting
---

# [​](#troubleshooting) Troubleshooting

## [​](#first-60-seconds) First 60 seconds

Run these in order:

Copy

```
clawdbot status
clawdbot status --all
clawdbot gateway probe
clawdbot logs --follow
clawdbot doctor
```

If the gateway is reachable, deep probes:

Copy

```
clawdbot status --deep
```

## [​](#common-“it-broke”-cases) Common “it broke” cases

### [​](#clawdbot:-command-not-found) `clawdbot: command not found`

Almost always a Node/npm PATH issue. Start here:

* [Install (Node/npm PATH sanity)](/install#nodejs--npm-path-sanity)

### [​](#installer-fails-or-you-need-full-logs) Installer fails (or you need full logs)

Re-run the installer in verbose mode to see the full trace and npm output:

Copy

```
curl -fsSL https://clawd.bot/install.sh | bash -s -- --verbose
```

For beta installs:

Copy

```
curl -fsSL https://clawd.bot/install.sh | bash -s -- --beta --verbose
```

You can also set `CLAWDBOT_VERBOSE=1` instead of the flag.

### [​](#gateway-“unauthorized”,-can’t-connect,-or-keeps-reconnecting) Gateway “unauthorized”, can’t connect, or keeps reconnecting

* [Gateway troubleshooting](/gateway/troubleshooting)
* [Gateway authentication](/gateway/authentication)

### [​](#control-ui-fails-on-http-device-identity-required) Control UI fails on HTTP (device identity required)

* [Gateway troubleshooting](/gateway/troubleshooting)
* [Control UI](/web/control-ui#insecure-http)

### [​](#docs-clawd-bot-shows-an-ssl-error-comcast/xfinity) `docs.clawd.bot` shows an SSL error (Comcast/Xfinity)

Some Comcast/Xfinity connections block `docs.clawd.bot` via Xfinity Advanced Security.
Disable Advanced Security or add `docs.clawd.bot` to the allowlist, then retry.

* Xfinity Advanced Security help: <https://www.xfinity.com/support/articles/using-xfinity-xfi-advanced-security>
* Quick sanity checks: try a mobile hotspot or VPN to confirm it’s ISP-level filtering

### [​](#service-says-running,-but-rpc-probe-fails) Service says running, but RPC probe fails

* [Gateway troubleshooting](/gateway/troubleshooting)
* [Background process / service](/gateway/background-process)

### [​](#model/auth-failures-rate-limit,-billing,-“all-models-failed”) Model/auth failures (rate limit, billing, “all models failed”)

* [Models](/cli/models)
* [OAuth / auth concepts](/concepts/oauth)

### [​](#/model-says-model-not-allowed) `/model` says `model not allowed`

This usually means `agents.defaults.models` is configured as an allowlist. When it’s non-empty,
only those provider/model keys can be selected.

* Check the allowlist: `clawdbot config get agents.defaults.models`
* Add the model you want (or clear the allowlist) and retry `/model`
* Use `/models` to browse the allowed providers/models

### [​](#when-filing-an-issue) When filing an issue

Paste a safe report:

Copy

```
clawdbot status --all
```

If you can, include the relevant log tail from `clawdbot logs --follow`.