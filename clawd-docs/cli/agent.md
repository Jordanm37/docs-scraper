---
title: Agent - Clawdbot
url: https://docs.clawd.bot/cli/agent
---

# [​](#clawdbot-agent) `clawdbot agent`

Run an agent turn via the Gateway (use `--local` for embedded).
Use `--agent <id>` to target a configured agent directly.
Related:

* Agent send tool: [Agent send](/tools/agent-send)

## [​](#examples) Examples

Copy

```
clawdbot agent --to +15555550123 --message "status update" --deliver
clawdbot agent --agent ops --message "Summarize logs"
clawdbot agent --session-id 1234 --message "Summarize inbox" --thinking medium
clawdbot agent --agent ops --message "Generate report" --deliver --reply-channel slack --reply-to "#reports"
```