---
title: Security - Clawdbot
url: https://docs.clawd.bot/cli/security
---

# [​](#clawdbot-security) `clawdbot security`

Security tools (audit + optional fixes).
Related:

* Security guide: [Security](/gateway/security)

## [​](#audit) Audit

Copy

```
clawdbot security audit
clawdbot security audit --deep
clawdbot security audit --fix
```

The audit warns when multiple DM senders share the main session and recommends `session.dmScope="per-channel-peer"` for shared inboxes.
It also warns when small models (`<=300B`) are used without sandboxing and with web/browser tools enabled.