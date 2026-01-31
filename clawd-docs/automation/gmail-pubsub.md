---
title: Gmail pubsub - Clawdbot
url: https://docs.clawd.bot/automation/gmail-pubsub
---

# [​](#gmail-pub/sub->-clawdbot) Gmail Pub/Sub -> Clawdbot

Goal: Gmail watch -> Pub/Sub push -> `gog gmail watch serve` -> Clawdbot webhook.

## [​](#prereqs) Prereqs

* `gcloud` installed and logged in ([install guide](https://docs.cloud.google.com/sdk/docs/install-sdk)).
* `gog` (gogcli) installed and authorized for the Gmail account ([gogcli.sh](https://gogcli.sh/)).
* Clawdbot hooks enabled (see [Webhooks](/automation/webhook)).
* `tailscale` logged in ([tailscale.com](https://tailscale.com/)). Supported setup uses Tailscale Funnel for the public HTTPS endpoint.
  Other tunnel services can work, but are DIY/unsupported and require manual wiring.
  Right now, Tailscale is what we support.

Example hook config (enable Gmail preset mapping):

Copy

```
{
  hooks: {
    enabled: true,
    token: "CLAWDBOT_HOOK_TOKEN",
    path: "/hooks",
    presets: ["gmail"]
  }
}
```

To deliver the Gmail summary to a chat surface, override the preset with a mapping
that sets `deliver` + optional `channel`/`to`:

Copy

```
{
  hooks: {
    enabled: true,
    token: "CLAWDBOT_HOOK_TOKEN",
    presets: ["gmail"],
    mappings: [
      {
        match: { path: "gmail" },
        action: "agent",
        wakeMode: "now",
        name: "Gmail",
        sessionKey: "hook:gmail:{{messages[0].id}}",
        messageTemplate:
          "New email from {{messages[0].from}}\nSubject: {{messages[0].subject}}\n{{messages[0].snippet}}\n{{messages[0].body}}",
        model: "openai/gpt-5.2-mini",
        deliver: true,
        channel: "last"
        // to: "+15551234567"
      }
    ]
  }
}
```

If you want a fixed channel, set `channel` + `to`. Otherwise `channel: "last"`
uses the last delivery route (falls back to WhatsApp).
To force a cheaper model for Gmail runs, set `model` in the mapping
(`provider/model` or alias). If you enforce `agents.defaults.models`, include it there.
To set a default model and thinking level specifically for Gmail hooks, add
`hooks.gmail.model` / `hooks.gmail.thinking` in your config:

Copy

```
{
  hooks: {
    gmail: {
      model: "openrouter/meta-llama/llama-3.3-70b-instruct:free",
      thinking: "off"
    }
  }
}
```

Notes:

* Per-hook `model`/`thinking` in the mapping still overrides these defaults.
* Fallback order: `hooks.gmail.model` → `agents.defaults.model.fallbacks` → primary (auth/rate-limit/timeouts).
* If `agents.defaults.models` is set, the Gmail model must be in the allowlist.

To customize payload handling further, add `hooks.mappings` or a JS/TS transform module
under `hooks.transformsDir` (see [Webhooks](/automation/webhook)).

## [​](#wizard-recommended) Wizard (recommended)

Use the Clawdbot helper to wire everything together (installs deps on macOS via brew):

Copy

```
clawdbot webhooks gmail setup \
  --account [email protected]
```

Defaults:

* Uses Tailscale Funnel for the public push endpoint.
* Writes `hooks.gmail` config for `clawdbot webhooks gmail run`.
* Enables the Gmail hook preset (`hooks.presets: ["gmail"]`).

Path note: when `tailscale.mode` is enabled, Clawdbot automatically sets
`hooks.gmail.serve.path` to `/` and keeps the public path at
`hooks.gmail.tailscale.path` (default `/gmail-pubsub`) because Tailscale
strips the set-path prefix before proxying.
If you need the backend to receive the prefixed path, set
`hooks.gmail.tailscale.target` (or `--tailscale-target`) to a full URL like
`http://127.0.0.1:8788/gmail-pubsub` and match `hooks.gmail.serve.path`.
Want a custom endpoint? Use `--push-endpoint <url>` or `--tailscale off`.
Platform note: on macOS the wizard installs `gcloud`, `gogcli`, and `tailscale`
via Homebrew; on Linux install them manually first.
Gateway auto-start (recommended):

* When `hooks.enabled=true` and `hooks.gmail.account` is set, the Gateway starts
  `gog gmail watch serve` on boot and auto-renews the watch.
* Set `CLAWDBOT_SKIP_GMAIL_WATCHER=1` to opt out (useful if you run the daemon yourself).
* Do not run the manual daemon at the same time, or you will hit
  `listen tcp 127.0.0.1:8788: bind: address already in use`.

Manual daemon (starts `gog gmail watch serve` + auto-renew):

Copy

```
clawdbot webhooks gmail run
```

## [​](#one-time-setup) One-time setup

1. Select the GCP project **that owns the OAuth client** used by `gog`.

Copy

```
gcloud auth login
gcloud config set project <project-id>
```

Note: Gmail watch requires the Pub/Sub topic to live in the same project as the OAuth client.

2. Enable APIs:

Copy

```
gcloud services enable gmail.googleapis.com pubsub.googleapis.com
```

3. Create a topic:

Copy

```
gcloud pubsub topics create gog-gmail-watch
```

4. Allow Gmail push to publish:

Copy

```
gcloud pubsub topics add-iam-policy-binding gog-gmail-watch \
  --member=serviceAccount:[email protected] \
  --role=roles/pubsub.publisher
```

## [​](#start-the-watch) Start the watch

Copy

```
gog gmail watch start \
  --account [email protected] \
  --label INBOX \
  --topic projects/<project-id>/topics/gog-gmail-watch
```

Save the `history_id` from the output (for debugging).

## [​](#run-the-push-handler) Run the push handler

Local example (shared token auth):

Copy

```
gog gmail watch serve \
  --account [email protected] \
  --bind 127.0.0.1 \
  --port 8788 \
  --path /gmail-pubsub \
  --token <shared> \
  --hook-url http://127.0.0.1:18789/hooks/gmail \
  --hook-token CLAWDBOT_HOOK_TOKEN \
  --include-body \
  --max-bytes 20000
```

Notes:

* `--token` protects the push endpoint (`x-gog-token` or `?token=`).
* `--hook-url` points to Clawdbot `/hooks/gmail` (mapped; isolated run + summary to main).
* `--include-body` and `--max-bytes` control the body snippet sent to Clawdbot.

Recommended: `clawdbot webhooks gmail run` wraps the same flow and auto-renews the watch.

## [​](#expose-the-handler-advanced,-unsupported) Expose the handler (advanced, unsupported)

If you need a non-Tailscale tunnel, wire it manually and use the public URL in the push
subscription (unsupported, no guardrails):

Copy

```
cloudflared tunnel --url http://127.0.0.1:8788 --no-autoupdate
```

Use the generated URL as the push endpoint:

Copy

```
gcloud pubsub subscriptions create gog-gmail-watch-push \
  --topic gog-gmail-watch \
  --push-endpoint "https://<public-url>/gmail-pubsub?token=<shared>"
```

Production: use a stable HTTPS endpoint and configure Pub/Sub OIDC JWT, then run:

Copy

```
gog gmail watch serve --verify-oidc --oidc-email <svc@...>
```

## [​](#test) Test

Send a message to the watched inbox:

Copy

```
gog gmail send \
  --account [email protected] \
  --to [email protected] \
  --subject "watch test" \
  --body "ping"
```

Check watch state and history:

Copy

```
gog gmail watch status --account [email protected]
gog gmail history --account [email protected] --since <historyId>
```

## [​](#troubleshooting) Troubleshooting

* `Invalid topicName`: project mismatch (topic not in the OAuth client project).
* `User not authorized`: missing `roles/pubsub.publisher` on the topic.
* Empty messages: Gmail push only provides `historyId`; fetch via `gog gmail history`.

## [​](#cleanup) Cleanup

Copy

```
gog gmail watch stop --account [email protected]
gcloud pubsub subscriptions delete gog-gmail-watch-push
gcloud pubsub topics delete gog-gmail-watch
```