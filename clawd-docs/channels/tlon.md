---
title: Tlon - Clawdbot
url: https://docs.clawd.bot/channels/tlon
---

# [​](#tlon-plugin) Tlon (plugin)

Tlon is a decentralized messenger built on Urbit. Clawdbot connects to your Urbit ship and can
respond to DMs and group chat messages. Group replies require an @ mention by default and can
be further restricted via allowlists.
Status: supported via plugin. DMs, group mentions, thread replies, and text-only media fallback
(URL appended to caption). Reactions, polls, and native media uploads are not supported.

## [​](#plugin-required) Plugin required

Tlon ships as a plugin and is not bundled with the core install.
Install via CLI (npm registry):

Copy

```
clawdbot plugins install @clawdbot/tlon
```

Local checkout (when running from a git repo):

Copy

```
clawdbot plugins install ./extensions/tlon
```

Details: [Plugins](/plugin)

## [​](#setup) Setup

1. Install the Tlon plugin.
2. Gather your ship URL and login code.
3. Configure `channels.tlon`.
4. Restart the gateway.
5. DM the bot or mention it in a group channel.

Minimal config (single account):

Copy

```
{
  channels: {
    tlon: {
      enabled: true,
      ship: "~sampel-palnet",
      url: "https://your-ship-host",
      code: "lidlut-tabwed-pillex-ridrup"
    }
  }
}
```

## [​](#group-channels) Group channels

Auto-discovery is enabled by default. You can also pin channels manually:

Copy

```
{
  channels: {
    tlon: {
      groupChannels: [
        "chat/~host-ship/general",
        "chat/~host-ship/support"
      ]
    }
  }
}
```

Disable auto-discovery:

Copy

```
{
  channels: {
    tlon: {
      autoDiscoverChannels: false
    }
  }
}
```

## [​](#access-control) Access control

DM allowlist (empty = allow all):

Copy

```
{
  channels: {
    tlon: {
      dmAllowlist: ["~zod", "~nec"]
    }
  }
}
```

Group authorization (restricted by default):

Copy

```
{
  channels: {
    tlon: {
      defaultAuthorizedShips: ["~zod"],
      authorization: {
        channelRules: {
          "chat/~host-ship/general": {
            mode: "restricted",
            allowedShips: ["~zod", "~nec"]
          },
          "chat/~host-ship/announcements": {
            mode: "open"
          }
        }
      }
    }
  }
}
```

## [​](#delivery-targets-cli/cron) Delivery targets (CLI/cron)

Use these with `clawdbot message send` or cron delivery:

* DM: `~sampel-palnet` or `dm/~sampel-palnet`
* Group: `chat/~host-ship/channel` or `group:~host-ship/channel`

## [​](#notes) Notes

* Group replies require a mention (e.g. `~your-bot-ship`) to respond.
* Thread replies: if the inbound message is in a thread, Clawdbot replies in-thread.
* Media: `sendMedia` falls back to text + URL (no native upload).