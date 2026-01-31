---
title: Flags - Clawdbot
url: https://docs.clawd.bot/diagnostics/flags
---

# [​](#diagnostics-flags) Diagnostics Flags

Diagnostics flags let you enable targeted debug logs without turning on verbose logging everywhere. Flags are opt-in and have no effect unless a subsystem checks them.

## [​](#how-it-works) How it works

* Flags are strings (case-insensitive).
* You can enable flags in config or via an env override.
* Wildcards are supported:
  + `telegram.*` matches `telegram.http`
  + `*` enables all flags

## [​](#enable-via-config) Enable via config

Copy

```
{
  "diagnostics": {
    "flags": ["telegram.http"]
  }
}
```

Multiple flags:

Copy

```
{
  "diagnostics": {
    "flags": ["telegram.http", "gateway.*"]
  }
}
```

Restart the gateway after changing flags.

## [​](#env-override-one-off) Env override (one-off)

Copy

```
CLAWDBOT_DIAGNOSTICS=telegram.http,telegram.payload
```

Disable all flags:

Copy

```
CLAWDBOT_DIAGNOSTICS=0
```

## [​](#where-logs-go) Where logs go

Flags emit logs into the standard diagnostics log file. By default:

Copy

```
/tmp/clawdbot/clawdbot-YYYY-MM-DD.log
```

If you set `logging.file`, use that path instead. Logs are JSONL (one JSON object per line). Redaction still applies based on `logging.redactSensitive`.

## [​](#extract-logs) Extract logs

Pick the latest log file:

Copy

```
ls -t /tmp/clawdbot/clawdbot-*.log | head -n 1
```

Filter for Telegram HTTP diagnostics:

Copy

```
rg "telegram http error" /tmp/clawdbot/clawdbot-*.log
```

Or tail while reproducing:

Copy

```
tail -f /tmp/clawdbot/clawdbot-$(date +%F).log | rg "telegram http error"
```

For remote gateways, you can also use `clawdbot logs --follow` (see </cli/logs>).

## [​](#notes) Notes

* If `logging.level` is set higher than `warn`, these logs may be suppressed. Default `info` is fine.
* Flags are safe to leave enabled; they only affect log volume for the specific subsystem.
* Use </logging> to change log destinations, levels, and redaction.