---
title: Cron - Clawdbot
url: https://docs.clawd.bot/cli/cron
---

# [​](#clawdbot-cron) `clawdbot cron`

Manage cron jobs for the Gateway scheduler.
Related:

* Cron jobs: [Cron jobs](/automation/cron-jobs)

Tip: run `clawdbot cron --help` for the full command surface.

## [​](#common-edits) Common edits

Update delivery settings without changing the message:

Copy

```
clawdbot cron edit <job-id> --deliver --channel telegram --to "123456789"
```

Disable delivery for an isolated job:

Copy

```
clawdbot cron edit <job-id> --no-deliver
```