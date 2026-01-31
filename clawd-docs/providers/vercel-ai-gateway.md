---
title: Vercel AI Gateway - Clawdbot
url: https://docs.clawd.bot/providers/vercel-ai-gateway
---

# [​](#vercel-ai-gateway) Vercel AI Gateway

The [Vercel AI Gateway](https://vercel.com/ai-gateway) provides a unified API to access hundreds of models through a single endpoint.

* Provider: `vercel-ai-gateway`
* Auth: `AI_GATEWAY_API_KEY`
* API: Anthropic Messages compatible

## [​](#quick-start) Quick start

1. Set the API key (recommended: store it for the Gateway):

Copy

```
clawdbot onboard --auth-choice ai-gateway-api-key
```

2. Set a default model:

Copy

```
{
  agents: {
    defaults: {
      model: { primary: "vercel-ai-gateway/anthropic/claude-opus-4.5" }
    }
  }
}
```

## [​](#non-interactive-example) Non-interactive example

Copy

```
clawdbot onboard --non-interactive \
  --mode local \
  --auth-choice ai-gateway-api-key \
  --ai-gateway-api-key "$AI_GATEWAY_API_KEY"
```

## [​](#environment-note) Environment note

If the Gateway runs as a daemon (launchd/systemd), make sure `AI_GATEWAY_API_KEY`
is available to that process (for example, in `~/.clawdbot/.env` or via
`env.shellEnv`).