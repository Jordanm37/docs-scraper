---
title: Date time - Clawdbot
url: https://docs.clawd.bot/date-time
---

# [​](#date-&-time) Date & Time

Clawdbot defaults to **host-local time for transport timestamps** and **user timezone only in the system prompt**.
Provider timestamps are preserved so tools keep their native semantics (current time is available via `session_status`).

## [​](#message-envelopes-local-by-default) Message envelopes (local by default)

Inbound messages are wrapped with a timestamp (minute precision):

Copy

```
[Provider ... 2026-01-05 16:26 PST] message text
```

This envelope timestamp is **host-local by default**, regardless of the provider timezone.
You can override this behavior:

Copy

```
{
  agents: {
    defaults: {
      envelopeTimezone: "local", // "utc" | "local" | "user" | IANA timezone
      envelopeTimestamp: "on", // "on" | "off"
      envelopeElapsed: "on" // "on" | "off"
    }
  }
}
```

* `envelopeTimezone: "utc"` uses UTC.
* `envelopeTimezone: "local"` uses the host timezone.
* `envelopeTimezone: "user"` uses `agents.defaults.userTimezone` (falls back to host timezone).
* Use an explicit IANA timezone (e.g., `"America/Chicago"`) for a fixed zone.
* `envelopeTimestamp: "off"` removes absolute timestamps from envelope headers.
* `envelopeElapsed: "off"` removes elapsed time suffixes (the `+2m` style).

### [​](#examples) Examples

**Local (default):**

Copy

```
[WhatsApp +1555 2026-01-18 00:19 PST] hello
```

**User timezone:**

Copy

```
[WhatsApp +1555 2026-01-18 00:19 CST] hello
```

**Elapsed time enabled:**

Copy

```
[WhatsApp +1555 +30s 2026-01-18T05:19Z] follow-up
```

## [​](#system-prompt:-current-date-&-time) System prompt: Current Date & Time

If the user timezone is known, the system prompt includes a dedicated
**Current Date & Time** section with the **time zone only** (no clock/time format)
to keep prompt caching stable:

Copy

```
Time zone: America/Chicago
```

When the agent needs the current time, use the `session_status` tool; the status
card includes a timestamp line.

## [​](#system-event-lines-local-by-default) System event lines (local by default)

Queued system events inserted into agent context are prefixed with a timestamp using the
same timezone selection as message envelopes (default: host-local).

Copy

```
System: [2026-01-12 12:19:17 PST] Model switched.
```

### [​](#configure-user-timezone-+-format) Configure user timezone + format

Copy

```
{
  agents: {
    defaults: {
      userTimezone: "America/Chicago",
      timeFormat: "auto" // auto | 12 | 24
    }
  }
}
```

* `userTimezone` sets the **user-local timezone** for prompt context.
* `timeFormat` controls **12h/24h display** in the prompt. `auto` follows OS prefs.

## [​](#time-format-detection-auto) Time format detection (auto)

When `timeFormat: "auto"`, Clawdbot inspects the OS preference (macOS/Windows)
and falls back to locale formatting. The detected value is **cached per process**
to avoid repeated system calls.

## [​](#tool-payloads-+-connectors-raw-provider-time-+-normalized-fields) Tool payloads + connectors (raw provider time + normalized fields)

Channel tools return **provider-native timestamps** and add normalized fields for consistency:

* `timestampMs`: epoch milliseconds (UTC)
* `timestampUtc`: ISO 8601 UTC string

Raw provider fields are preserved so nothing is lost.

* Slack: epoch-like strings from the API
* Discord: UTC ISO timestamps
* Telegram/WhatsApp: provider-specific numeric/ISO timestamps

If you need local time, convert it downstream using the known timezone.

## [​](#related-docs) Related docs

* [System Prompt](/concepts/system-prompt)
* [Timezones](/concepts/timezone)
* [Messages](/concepts/messages)