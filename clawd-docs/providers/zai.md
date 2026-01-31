---
title: Zai - Clawdbot
url: https://docs.clawd.bot/providers/zai
---

# [​](#z-ai) Z.AI

Z.AI is the API platform for **GLM** models. It provides REST APIs for GLM and uses API keys
for authentication. Create your API key in the Z.AI console. Clawdbot uses the `zai` provider
with a Z.AI API key.

## [​](#cli-setup) CLI setup

Copy

```
clawdbot onboard --auth-choice zai-api-key
# or non-interactive
clawdbot onboard --zai-api-key "$ZAI_API_KEY"
```

## [​](#config-snippet) Config snippet

Copy

```
{
  env: { ZAI_API_KEY: "sk-..." },
  agents: { defaults: { model: { primary: "zai/glm-4.7" } } }
}
```

## [​](#notes) Notes

* GLM models are available as `zai/<model>` (example: `zai/glm-4.7`).
* See </providers/glm> for the model family overview.
* Z.AI uses Bearer auth with your API key.