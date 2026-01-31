---
title: Brave search - Clawdbot
url: https://docs.clawd.bot/brave-search
---

# [​](#brave-search-api) Brave Search API

Clawdbot uses Brave Search as the default provider for `web_search`.

## [​](#get-an-api-key) Get an API key

1. Create a Brave Search API account at <https://brave.com/search/api/>
2. In the dashboard, choose the **Data for Search** plan and generate an API key.
3. Store the key in config (recommended) or set `BRAVE_API_KEY` in the Gateway environment.

## [​](#config-example) Config example

Copy

```
{
  tools: {
    web: {
      search: {
        provider: "brave",
        apiKey: "BRAVE_API_KEY_HERE",
        maxResults: 5,
        timeoutSeconds: 30
      }
    }
  }
}
```

## [​](#notes) Notes

* The Data for AI plan is **not** compatible with `web_search`.
* Brave provides a free tier plus paid plans; check the Brave API portal for current limits.

See [Web tools](/tools/web) for the full web\_search configuration.