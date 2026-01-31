---
title: Onboard - Clawdbot
url: https://docs.clawd.bot/cli/onboard
---

# [​](#clawdbot-onboard) `clawdbot onboard`

Interactive onboarding wizard (local or remote Gateway setup).
Related:

* Wizard guide: [Onboarding](/start/onboarding)

## [​](#examples) Examples

Copy

```
clawdbot onboard
clawdbot onboard --flow quickstart
clawdbot onboard --flow manual
clawdbot onboard --mode remote --remote-url ws://gateway-host:18789
```

Flow notes:

* `quickstart`: minimal prompts, auto-generates a gateway token.
* `manual`: full prompts for port/bind/auth (alias of `advanced`).