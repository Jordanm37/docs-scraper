---
title: Index - Clawdbot
url: https://docs.clawd.bot/web
---

# [​](#web-gateway) Web (Gateway)

The Gateway serves a small **browser Control UI** (Vite + Lit) from the same port as the Gateway WebSocket:

* default: `http://<host>:18789/`
* optional prefix: set `gateway.controlUi.basePath` (e.g. `/clawdbot`)

Capabilities live in [Control UI](/web/control-ui).
This page focuses on bind modes, security, and web-facing surfaces.

## [​](#webhooks) Webhooks

When `hooks.enabled=true`, the Gateway also exposes a small webhook endpoint on the same HTTP server.
See [Gateway configuration](/gateway/configuration) → `hooks` for auth + payloads.

## [​](#config-default-on) Config (default-on)

The Control UI is **enabled by default** when assets are present (`dist/control-ui`).
You can control it via config:

Copy

```
{
  gateway: {
    controlUi: { enabled: true, basePath: "/clawdbot" } // basePath optional
  }
}
```

## [​](#tailscale-access) Tailscale access

### [​](#integrated-serve-recommended) Integrated Serve (recommended)

Keep the Gateway on loopback and let Tailscale Serve proxy it:

Copy

```
{
  gateway: {
    bind: "loopback",
    tailscale: { mode: "serve" }
  }
}
```

Then start the gateway:

Copy

```
clawdbot gateway
```

Open:

* `https://<magicdns>/` (or your configured `gateway.controlUi.basePath`)

### [​](#tailnet-bind-+-token) Tailnet bind + token

Copy

```
{
  gateway: {
    bind: "tailnet",
    controlUi: { enabled: true },
    auth: { mode: "token", token: "your-token" }
  }
}
```

Then start the gateway (token required for non-loopback binds):

Copy

```
clawdbot gateway
```

Open:

* `http://<tailscale-ip>:18789/` (or your configured `gateway.controlUi.basePath`)

### [​](#public-internet-funnel) Public internet (Funnel)

Copy

```
{
  gateway: {
    bind: "loopback",
    tailscale: { mode: "funnel" },
    auth: { mode: "password" } // or CLAWDBOT_GATEWAY_PASSWORD
  }
}
```

## [​](#security-notes) Security notes

* Binding the Gateway to a non-loopback address **requires** auth (`gateway.auth` or `CLAWDBOT_GATEWAY_TOKEN`).
* The wizard generates a gateway token by default (even on loopback).
* The UI sends `connect.params.auth.token` or `connect.params.auth.password`.
* With Serve, Tailscale identity headers can satisfy auth when
  `gateway.auth.allowTailscale` is `true` (no token/password required). Set
  `gateway.auth.allowTailscale: false` to require explicit credentials. See
  [Tailscale](/gateway/tailscale) and [Security](/gateway/security).
* `gateway.tailscale.mode: "funnel"` requires `gateway.auth.mode: "password"` (shared password).

## [​](#building-the-ui) Building the UI

The Gateway serves static files from `dist/control-ui`. Build them with:

Copy

```
pnpm ui:build # auto-installs UI deps on first run
```