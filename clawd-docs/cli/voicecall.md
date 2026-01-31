---
title: Voicecall - Clawdbot
url: https://docs.clawd.bot/cli/voicecall
---

# [​](#clawdbot-voicecall) `clawdbot voicecall`

`voicecall` is a plugin-provided command. It only appears if the voice-call plugin is installed and enabled.
Primary doc:

* Voice-call plugin: [Voice Call](/plugins/voice-call)

## [​](#common-commands) Common commands

Copy

```
clawdbot voicecall status --call-id <id>
clawdbot voicecall call --to "+15555550123" --message "Hello" --mode notify
clawdbot voicecall continue --call-id <id> --message "Any questions?"
clawdbot voicecall end --call-id <id>
```

## [​](#exposing-webhooks-tailscale) Exposing webhooks (Tailscale)

Copy

```
clawdbot voicecall expose --mode serve
clawdbot voicecall expose --mode funnel
clawdbot voicecall unexpose
```

Security note: only expose the webhook endpoint to networks you trust. Prefer Tailscale Serve over Funnel when possible.