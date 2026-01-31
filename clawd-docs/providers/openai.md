---
title: Openai - Clawdbot
url: https://docs.clawd.bot/providers/openai
---

# [​](#openai) OpenAI

OpenAI provides developer APIs for GPT models. Codex supports **ChatGPT sign-in** for subscription
access or **API key** sign-in for usage-based access. Codex cloud requires ChatGPT sign-in, while
the Codex CLI supports either sign-in method. The Codex CLI caches login details in
`~/.codex/auth.json` (or your OS credential store), which Clawdbot can reuse.

## [​](#option-a:-openai-api-key-openai-platform) Option A: OpenAI API key (OpenAI Platform)

**Best for:** direct API access and usage-based billing.
Get your API key from the OpenAI dashboard.

### [​](#cli-setup) CLI setup

Copy

```
clawdbot onboard --auth-choice openai-api-key
# or non-interactive
clawdbot onboard --openai-api-key "$OPENAI_API_KEY"
```

### [​](#config-snippet) Config snippet

Copy

```
{
  env: { OPENAI_API_KEY: "sk-..." },
  agents: { defaults: { model: { primary: "openai/gpt-5.2" } } }
}
```

## [​](#option-b:-openai-code-codex-subscription) Option B: OpenAI Code (Codex) subscription

**Best for:** using ChatGPT/Codex subscription access instead of an API key.
Codex cloud requires ChatGPT sign-in, while the Codex CLI supports ChatGPT or API key sign-in.
Clawdbot can reuse your **Codex CLI** login (`~/.codex/auth.json`) or run the OAuth flow.

### [​](#cli-setup-2) CLI setup

Copy

```
# Reuse existing Codex CLI login
clawdbot onboard --auth-choice codex-cli

# Or run Codex OAuth in the wizard
clawdbot onboard --auth-choice openai-codex
```

### [​](#config-snippet-2) Config snippet

Copy

```
{
  agents: { defaults: { model: { primary: "openai-codex/gpt-5.2" } } }
}
```

## [​](#notes) Notes

* Model refs always use `provider/model` (see </concepts/models>).
* Auth details + reuse rules are in </concepts/oauth>.