---
title: Openrouter - Clawdbot
url: https://docs.clawd.bot/providers/openrouter
---

# [​](#openrouter) OpenRouter

OpenRouter provides a **unified API** that routes requests to many models behind a single
endpoint and API key. It is OpenAI-compatible, so most OpenAI SDKs work by switching the base URL.

## [​](#cli-setup) CLI setup

Copy

```
clawdbot onboard --auth-choice apiKey --token-provider openrouter --token "$OPENROUTER_API_KEY"
```

## [​](#config-snippet) Config snippet

Copy

```
{
  env: { OPENROUTER_API_KEY: "sk-or-..." },
  agents: {
    defaults: {
      model: { primary: "openrouter/anthropic/claude-sonnet-4-5" }
    }
  }
}
```

## [​](#notes) Notes

* Model refs are `openrouter/<provider>/<model>`.
* For more model/provider options, see </concepts/model-providers>.
* OpenRouter uses a Bearer token with your API key under the hood.