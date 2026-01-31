---
title: Glm - Clawdbot
url: https://docs.clawd.bot/providers/glm
---

# [​](#glm-models) GLM models

GLM is a **model family** (not a company) available through the Z.AI platform. In Clawdbot, GLM
models are accessed via the `zai` provider and model IDs like `zai/glm-4.7`.

## [​](#cli-setup) CLI setup

Copy

```
clawdbot onboard --auth-choice zai-api-key
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

* GLM versions and availability can change; check Z.AI’s docs for the latest.
* Example model IDs include `glm-4.7` and `glm-4.6`.
* For provider details, see </providers/zai>.