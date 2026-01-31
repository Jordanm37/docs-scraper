---
title: Doctor - Clawdbot
url: https://docs.clawd.bot/cli/doctor
---

# [​](#clawdbot-doctor) `clawdbot doctor`

Health checks + quick fixes for the gateway and channels.
Related:

* Troubleshooting: [Troubleshooting](/gateway/troubleshooting)
* Security audit: [Security](/gateway/security)

## [​](#examples) Examples

Copy

```
clawdbot doctor
clawdbot doctor --repair
clawdbot doctor --deep
```

Notes:

* Interactive prompts (like keychain/OAuth fixes) only run when stdin is a TTY and `--non-interactive` is **not** set. Headless runs (cron, Telegram, no terminal) will skip prompts.
* `--fix` (alias for `--repair`) writes a backup to `~/.clawdbot/clawdbot.json.bak` and drops unknown config keys, listing each removal.

## [​](#macos:-launchctl-env-overrides) macOS: `launchctl` env overrides

If you previously ran `launchctl setenv CLAWDBOT_GATEWAY_TOKEN ...` (or `...PASSWORD`), that value overrides your config file and can cause persistent “unauthorized” errors.

Copy

```
launchctl getenv CLAWDBOT_GATEWAY_TOKEN
launchctl getenv CLAWDBOT_GATEWAY_PASSWORD

launchctl unsetenv CLAWDBOT_GATEWAY_TOKEN
launchctl unsetenv CLAWDBOT_GATEWAY_PASSWORD
```