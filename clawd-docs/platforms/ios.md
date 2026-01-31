---
title: Ios - Clawdbot
url: https://docs.clawd.bot/platforms/ios
---

# [​](#ios-app-node) iOS App (Node)

Availability: internal preview. The iOS app is not publicly distributed yet.

## [​](#what-it-does) What it does

* Connects to a Gateway over WebSocket (LAN or tailnet).
* Exposes node capabilities: Canvas, Screen snapshot, Camera capture, Location, Talk mode, Voice wake.
* Receives `node.invoke` commands and reports node status events.

## [​](#requirements) Requirements

* Gateway running on another device (macOS, Linux, or Windows via WSL2).
* Network path:
  + Same LAN via Bonjour, **or**
  + Tailnet via unicast DNS-SD (`clawdbot.internal.`), **or**
  + Manual host/port (fallback).

## [​](#quick-start-pair-+-connect) Quick start (pair + connect)

1. Start the Gateway:

Copy

```
clawdbot gateway --port 18789
```

2. In the iOS app, open Settings and pick a discovered gateway (or enable Manual Host and enter host/port).
3. Approve the pairing request on the gateway host:

Copy

```
clawdbot nodes pending
clawdbot nodes approve <requestId>
```

4. Verify connection:

Copy

```
clawdbot nodes status
clawdbot gateway call node.list --params "{}"
```

## [​](#discovery-paths) Discovery paths

### [​](#bonjour-lan) Bonjour (LAN)

The Gateway advertises `_clawdbot._tcp` on `local.`. The iOS app lists these automatically.

### [​](#tailnet-cross-network) Tailnet (cross-network)

If mDNS is blocked, use a unicast DNS-SD zone (recommended domain: `clawdbot.internal.`) and Tailscale split DNS.
See [Bonjour](/gateway/bonjour) for the CoreDNS example.

### [​](#manual-host/port) Manual host/port

In Settings, enable **Manual Host** and enter the gateway host + port (default `18789`).

## [​](#canvas-+-a2ui) Canvas + A2UI

The iOS node renders a WKWebView canvas. Use `node.invoke` to drive it:

Copy

```
clawdbot nodes invoke --node "iOS Node" --command canvas.navigate --params '{"url":"http://<gateway-host>:18793/__clawdbot__/canvas/"}'
```

Notes:

* The Gateway canvas host serves `/__clawdbot__/canvas/` and `/__clawdbot__/a2ui/`.
* The iOS node auto-navigates to A2UI on connect when a canvas host URL is advertised.
* Return to the built-in scaffold with `canvas.navigate` and `{"url":""}`.

### [​](#canvas-eval-/-snapshot) Canvas eval / snapshot

Copy

```
clawdbot nodes invoke --node "iOS Node" --command canvas.eval --params '{"javaScript":"(() => { const {ctx} = window.__clawdbot; ctx.clearRect(0,0,innerWidth,innerHeight); ctx.lineWidth=6; ctx.strokeStyle=\"#ff2d55\"; ctx.beginPath(); ctx.moveTo(40,40); ctx.lineTo(innerWidth-40, innerHeight-40); ctx.stroke(); return \"ok\"; })()"}'
```

Copy

```
clawdbot nodes invoke --node "iOS Node" --command canvas.snapshot --params '{"maxWidth":900,"format":"jpeg"}'
```

## [​](#voice-wake-+-talk-mode) Voice wake + talk mode

* Voice wake and talk mode are available in Settings.
* iOS may suspend background audio; treat voice features as best-effort when the app is not active.

## [​](#common-errors) Common errors

* `NODE_BACKGROUND_UNAVAILABLE`: bring the iOS app to the foreground (canvas/camera/screen commands require it).
* `A2UI_HOST_NOT_CONFIGURED`: the Gateway did not advertise a canvas host URL; check `canvasHost` in [Gateway configuration](/gateway/configuration).
* Pairing prompt never appears: run `clawdbot nodes pending` and approve manually.
* Reconnect fails after reinstall: the Keychain pairing token was cleared; re-pair the node.

## [​](#related-docs) Related docs

* [Pairing](/gateway/pairing)
* [Discovery](/gateway/discovery)
* [Bonjour](/gateway/bonjour)