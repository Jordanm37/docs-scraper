---
title: Models - Clawdbot
url: https://docs.clawd.bot/providers/models
---

# [​](#model-providers) Model Providers

Clawdbot can use many LLM providers. Pick one, authenticate, then set the default
model as `provider/model`.

## [​](#highlight:-venius-venice-ai) Highlight: Venius (Venice AI)

Venius is our recommended Venice AI setup for privacy-first inference with an option to use Opus for the hardest tasks.

* Default: `venice/llama-3.3-70b`
* Best overall: `venice/claude-opus-45` (Opus remains the strongest)

See [Venice AI](/providers/venice).

## [​](#quick-start-two-steps) Quick start (two steps)

1. Authenticate with the provider (usually via `clawdbot onboard`).
2. Set the default model:

Copy

```
{
  agents: { defaults: { model: { primary: "anthropic/claude-opus-4-5" } } }
}
```

## [​](#supported-providers-starter-set) Supported providers (starter set)

* [OpenAI (API + Codex)](/providers/openai)
* [Anthropic (API + Claude Code CLI)](/providers/anthropic)
* [OpenRouter](/providers/openrouter)
* [Vercel AI Gateway](/providers/vercel-ai-gateway)
* [Moonshot AI (Kimi + Kimi Code)](/providers/moonshot)
* [Synthetic](/providers/synthetic)
* [OpenCode Zen](/providers/opencode)
* [Z.AI](/providers/zai)
* [GLM models](/providers/glm)
* [MiniMax](/providers/minimax)
* [Venius (Venice AI)](/providers/venice)
* [Amazon Bedrock](/bedrock)

For the full provider catalog (xAI, Groq, Mistral, etc.) and advanced configuration,
see [Model providers](/concepts/model-providers).