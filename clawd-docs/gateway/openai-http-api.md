---
title: Openai http api - Clawdbot
url: https://docs.clawd.bot/gateway/openai-http-api
---

# [​](#openai-chat-completions-http) OpenAI Chat Completions (HTTP)

Clawdbot’s Gateway can serve a small OpenAI-compatible Chat Completions endpoint.
This endpoint is **disabled by default**. Enable it in config first.

* `POST /v1/chat/completions`
* Same port as the Gateway (WS + HTTP multiplex): `http://<gateway-host>:<port>/v1/chat/completions`

Under the hood, requests are executed as a normal Gateway agent run (same codepath as `clawdbot agent`), so routing/permissions/config match your Gateway.

## [​](#authentication) Authentication

Uses the Gateway auth configuration. Send a bearer token:

* `Authorization: Bearer <token>`

Notes:

* When `gateway.auth.mode="token"`, use `gateway.auth.token` (or `CLAWDBOT_GATEWAY_TOKEN`).
* When `gateway.auth.mode="password"`, use `gateway.auth.password` (or `CLAWDBOT_GATEWAY_PASSWORD`).

## [​](#choosing-an-agent) Choosing an agent

No custom headers required: encode the agent id in the OpenAI `model` field:

* `model: "clawdbot:<agentId>"` (example: `"clawdbot:main"`, `"clawdbot:beta"`)
* `model: "agent:<agentId>"` (alias)

Or target a specific Clawdbot agent by header:

* `x-clawdbot-agent-id: <agentId>` (default: `main`)

Advanced:

* `x-clawdbot-session-key: <sessionKey>` to fully control session routing.

## [​](#enabling-the-endpoint) Enabling the endpoint

Set `gateway.http.endpoints.chatCompletions.enabled` to `true`:

Copy

```
{
  gateway: {
    http: {
      endpoints: {
        chatCompletions: { enabled: true }
      }
    }
  }
}
```

## [​](#disabling-the-endpoint) Disabling the endpoint

Set `gateway.http.endpoints.chatCompletions.enabled` to `false`:

Copy

```
{
  gateway: {
    http: {
      endpoints: {
        chatCompletions: { enabled: false }
      }
    }
  }
}
```

## [​](#session-behavior) Session behavior

By default the endpoint is **stateless per request** (a new session key is generated each call).
If the request includes an OpenAI `user` string, the Gateway derives a stable session key from it, so repeated calls can share an agent session.

## [​](#streaming-sse) Streaming (SSE)

Set `stream: true` to receive Server-Sent Events (SSE):

* `Content-Type: text/event-stream`
* Each event line is `data: <json>`
* Stream ends with `data: [DONE]`

## [​](#examples) Examples

Non-streaming:

Copy

```
curl -sS http://127.0.0.1:18789/v1/chat/completions \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -H 'Content-Type: application/json' \
  -H 'x-clawdbot-agent-id: main' \
  -d '{
    "model": "clawdbot",
    "messages": [{"role":"user","content":"hi"}]
  }'
```

Streaming:

Copy

```
curl -N http://127.0.0.1:18789/v1/chat/completions \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -H 'Content-Type: application/json' \
  -H 'x-clawdbot-agent-id: main' \
  -d '{
    "model": "clawdbot",
    "stream": true,
    "messages": [{"role":"user","content":"hi"}]
  }'
```