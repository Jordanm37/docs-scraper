---
title: Health - Clawdbot
url: https://docs.clawd.bot/cli/health
---

# [​](#clawdbot-health) `clawdbot health`

Fetch health from the running Gateway.

Copy

```
clawdbot health
clawdbot health --json
clawdbot health --verbose
```

Notes:

* `--verbose` runs live probes and prints per-account timings when multiple accounts are configured.
* Output includes per-agent session stores when multiple agents are configured.