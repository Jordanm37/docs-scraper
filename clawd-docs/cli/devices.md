---
title: Devices - Clawdbot
url: https://docs.clawd.bot/cli/devices
---

# [​](#clawdbot-devices) `clawdbot devices`

Manage device pairing requests and device-scoped tokens.

## [​](#commands) Commands

### [​](#clawdbot-devices-list) `clawdbot devices list`

List pending pairing requests and paired devices.

Copy

```
clawdbot devices list
clawdbot devices list --json
```

### [​](#clawdbot-devices-approve-<requestid>) `clawdbot devices approve <requestId>`

Approve a pending device pairing request.

Copy

```
clawdbot devices approve <requestId>
```

### [​](#clawdbot-devices-reject-<requestid>) `clawdbot devices reject <requestId>`

Reject a pending device pairing request.

Copy

```
clawdbot devices reject <requestId>
```

### [​](#clawdbot-devices-rotate-device-<id>-role-<role>-[-scope-<scope->]) `clawdbot devices rotate --device <id> --role <role> [--scope <scope...>]`

Rotate a device token for a specific role (optionally updating scopes).

Copy

```
clawdbot devices rotate --device <deviceId> --role operator --scope operator.read --scope operator.write
```

### [​](#clawdbot-devices-revoke-device-<id>-role-<role>) `clawdbot devices revoke --device <id> --role <role>`

Revoke a device token for a specific role.

Copy

```
clawdbot devices revoke --device <deviceId> --role node
```

## [​](#common-options) Common options

* `--url <url>`: Gateway WebSocket URL (defaults to `gateway.remote.url` when configured).
* `--token <token>`: Gateway token (if required).
* `--password <password>`: Gateway password (password auth).
* `--timeout <ms>`: RPC timeout.
* `--json`: JSON output (recommended for scripting).

## [​](#notes) Notes

* Token rotation returns a new token (sensitive). Treat it like a secret.
* These commands require `operator.pairing` (or `operator.admin`) scope.