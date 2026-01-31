---
title: Directory - Clawdbot
url: https://docs.clawd.bot/cli/directory
---

# [​](#clawdbot-directory) `clawdbot directory`

Directory lookups for channels that support it (contacts/peers, groups, and “me”).

## [​](#common-flags) Common flags

* `--channel <name>`: channel id/alias (required when multiple channels are configured; auto when only one is configured)
* `--account <id>`: account id (default: channel default)
* `--json`: output JSON

## [​](#notes) Notes

* `directory` is meant to help you find IDs you can paste into other commands (especially `clawdbot message send --target ...`).
* For many channels, results are config-backed (allowlists / configured groups) rather than a live provider directory.
* Default output is `id` (and sometimes `name`) separated by a tab; use `--json` for scripting.

## [​](#using-results-with-message-send) Using results with `message send`

Copy

```
clawdbot directory peers list --channel slack --query "U0"
clawdbot message send --channel slack --target user:U012ABCDEF --message "hello"
```

## [​](#id-formats-by-channel) ID formats (by channel)

* WhatsApp: `+15551234567` (DM), `[email protected]` (group)
* Telegram: `@username` or numeric chat id; groups are numeric ids
* Slack: `user:U…` and `channel:C…`
* Discord: `user:<id>` and `channel:<id>`
* Matrix (plugin): `user:@user:server`, `room:!roomId:server`, or `#alias:server`
* Microsoft Teams (plugin): `user:<id>` and `conversation:<id>`
* Zalo (plugin): user id (Bot API)
* Zalo Personal / `zalouser` (plugin): thread id (DM/group) from `zca` (`me`, `friend list`, `group list`)

## [​](#self-“me”) Self (“me”)

Copy

```
clawdbot directory self --channel zalouser
```

## [​](#peers-contacts/users) Peers (contacts/users)

Copy

```
clawdbot directory peers list --channel zalouser
clawdbot directory peers list --channel zalouser --query "name"
clawdbot directory peers list --channel zalouser --limit 50
```

## [​](#groups) Groups

Copy

```
clawdbot directory groups list --channel zalouser
clawdbot directory groups list --channel zalouser --query "work"
clawdbot directory groups members --channel zalouser --group-id <id>
```