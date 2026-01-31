---
title: Browser - Clawdbot
url: https://docs.clawd.bot/cli/browser
---

# [​](#clawdbot-browser) `clawdbot browser`

Manage Clawdbot’s browser control server and run browser actions (tabs, snapshots, screenshots, navigation, clicks, typing).
Related:

* Browser tool + API: [Browser tool](/tools/browser)
* Chrome extension relay: [Chrome extension](/tools/chrome-extension)

## [​](#common-flags) Common flags

* `--url <controlUrl>`: override `browser.controlUrl` for this command invocation.
* `--browser-profile <name>`: choose a browser profile (default comes from config).
* `--json`: machine-readable output (where supported).

## [​](#quick-start-local) Quick start (local)

Copy

```
clawdbot browser --browser-profile chrome tabs
clawdbot browser --browser-profile clawd start
clawdbot browser --browser-profile clawd open https://example.com
clawdbot browser --browser-profile clawd snapshot
```

## [​](#profiles) Profiles

Profiles are named browser routing configs. In practice:

* `clawd`: launches/attaches to a dedicated Clawdbot-managed Chrome instance (isolated user data dir).
* `chrome`: controls your existing Chrome tab(s) via the Chrome extension relay.

Copy

```
clawdbot browser profiles
clawdbot browser create-profile --name work --color "#FF5A36"
clawdbot browser delete-profile --name work
```

Use a specific profile:

Copy

```
clawdbot browser --browser-profile work tabs
```

## [​](#tabs) Tabs

Copy

```
clawdbot browser tabs
clawdbot browser open https://docs.clawd.bot
clawdbot browser focus <targetId>
clawdbot browser close <targetId>
```

## [​](#snapshot-/-screenshot-/-actions) Snapshot / screenshot / actions

Snapshot:

Copy

```
clawdbot browser snapshot
```

Screenshot:

Copy

```
clawdbot browser screenshot
```

Navigate/click/type (ref-based UI automation):

Copy

```
clawdbot browser navigate https://example.com
clawdbot browser click <ref>
clawdbot browser type <ref> "hello"
```

## [​](#chrome-extension-relay-attach-via-toolbar-button) Chrome extension relay (attach via toolbar button)

This mode lets the agent control an existing Chrome tab that you attach manually (it does not auto-attach).
Install the unpacked extension to a stable path:

Copy

```
clawdbot browser extension install
clawdbot browser extension path
```

Then Chrome → `chrome://extensions` → enable “Developer mode” → “Load unpacked” → select the printed folder.
Full guide: [Chrome extension](/tools/chrome-extension)

## [​](#remote-browser-control-clawdbot-browser-serve) Remote browser control (`clawdbot browser serve`)

If the Gateway runs on a different machine than the browser, run a standalone browser control server on the machine that runs Chrome:

Copy

```
clawdbot browser serve --bind 127.0.0.1 --port 18791 --token <token>
```

Then point the Gateway at it using `browser.controlUrl` + `browser.controlToken` (or `CLAWDBOT_BROWSER_CONTROL_TOKEN`).
Security + TLS best-practices: [Browser tool](/tools/browser), [Tailscale](/gateway/tailscale), [Security](/gateway/security)