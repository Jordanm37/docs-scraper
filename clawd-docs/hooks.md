---
title: Hooks - Clawdbot
url: https://docs.clawd.bot/hooks
---

# [​](#hooks) Hooks

Hooks provide an extensible event-driven system for automating actions in response to agent commands and events. Hooks are automatically discovered from directories and can be managed via CLI commands, similar to how skills work in Clawdbot.

## [​](#getting-oriented) Getting Oriented

Hooks are small scripts that run when something happens. There are two kinds:

* **Hooks** (this page): run inside the Gateway when agent events fire, like `/new`, `/reset`, `/stop`, or lifecycle events.
* **Webhooks**: external HTTP webhooks that let other systems trigger work in Clawdbot. See [Webhook Hooks](/automation/webhook) or use `clawdbot webhooks` for Gmail helper commands.

Hooks can also be bundled inside plugins; see [Plugins](/plugin#plugin-hooks).
Common uses:

* Save a memory snapshot when you reset a session
* Keep an audit trail of commands for troubleshooting or compliance
* Trigger follow-up automation when a session starts or ends
* Write files into the agent workspace or call external APIs when events fire

If you can write a small TypeScript function, you can write a hook. Hooks are discovered automatically, and you enable or disable them via the CLI.

## [​](#overview) Overview

The hooks system allows you to:

* Save session context to memory when `/new` is issued
* Log all commands for auditing
* Trigger custom automations on agent lifecycle events
* Extend Clawdbot’s behavior without modifying core code

## [​](#getting-started) Getting Started

### [​](#bundled-hooks) Bundled Hooks

Clawdbot ships with four bundled hooks that are automatically discovered:

* **💾 session-memory**: Saves session context to your agent workspace (default `~/clawd/memory/`) when you issue `/new`
* **📝 command-logger**: Logs all command events to `~/.clawdbot/logs/commands.log`
* **🚀 boot-md**: Runs `BOOT.md` when the gateway starts (requires internal hooks enabled)
* **😈 soul-evil**: Swaps injected `SOUL.md` content with `SOUL_EVIL.md` during a purge window or by random chance

List available hooks:

Copy

```
clawdbot hooks list
```

Enable a hook:

Copy

```
clawdbot hooks enable session-memory
```

Check hook status:

Copy

```
clawdbot hooks check
```

Get detailed information:

Copy

```
clawdbot hooks info session-memory
```

### [​](#onboarding) Onboarding

During onboarding (`clawdbot onboard`), you’ll be prompted to enable recommended hooks. The wizard automatically discovers eligible hooks and presents them for selection.

## [​](#hook-discovery) Hook Discovery

Hooks are automatically discovered from three directories (in order of precedence):

1. **Workspace hooks**: `<workspace>/hooks/` (per-agent, highest precedence)
2. **Managed hooks**: `~/.clawdbot/hooks/` (user-installed, shared across workspaces)
3. **Bundled hooks**: `<clawdbot>/dist/hooks/bundled/` (shipped with Clawdbot)

Managed hook directories can be either a **single hook** or a **hook pack** (package directory).
Each hook is a directory containing:

Copy

```
my-hook/
├── HOOK.md          # Metadata + documentation
└── handler.ts       # Handler implementation
```

## [​](#hook-packs-npm/archives) Hook Packs (npm/archives)

Hook packs are standard npm packages that export one or more hooks via `clawdbot.hooks` in
`package.json`. Install them with:

Copy

```
clawdbot hooks install <path-or-spec>
```

Example `package.json`:

Copy

```
{
  "name": "@acme/my-hooks",
  "version": "0.1.0",
  "clawdbot": {
    "hooks": ["./hooks/my-hook", "./hooks/other-hook"]
  }
}
```

Each entry points to a hook directory containing `HOOK.md` and `handler.ts` (or `index.ts`).
Hook packs can ship dependencies; they will be installed under `~/.clawdbot/hooks/<id>`.

## [​](#hook-structure) Hook Structure

### [​](#hook-md-format) HOOK.md Format

The `HOOK.md` file contains metadata in YAML frontmatter plus Markdown documentation:

Copy

```
---
name: my-hook
description: "Short description of what this hook does"
homepage: https://docs.clawd.bot/hooks#my-hook
metadata: {"clawdbot":{"emoji":"🔗","events":["command:new"],"requires":{"bins":["node"]}}}
---

# My Hook

Detailed documentation goes here...

## What It Does

- Listens for `/new` commands
- Performs some action
- Logs the result

## Requirements

- Node.js must be installed

## Configuration

No configuration needed.
```

### [​](#metadata-fields) Metadata Fields

The `metadata.clawdbot` object supports:

* **`emoji`**: Display emoji for CLI (e.g., `"💾"`)
* **`events`**: Array of events to listen for (e.g., `["command:new", "command:reset"]`)
* **`export`**: Named export to use (defaults to `"default"`)
* **`homepage`**: Documentation URL
* **`requires`**: Optional requirements
  + **`bins`**: Required binaries on PATH (e.g., `["git", "node"]`)
  + **`anyBins`**: At least one of these binaries must be present
  + **`env`**: Required environment variables
  + **`config`**: Required config paths (e.g., `["workspace.dir"]`)
  + **`os`**: Required platforms (e.g., `["darwin", "linux"]`)
* **`always`**: Bypass eligibility checks (boolean)
* **`install`**: Installation methods (for bundled hooks: `[{"id":"bundled","kind":"bundled"}]`)

### [​](#handler-implementation) Handler Implementation

The `handler.ts` file exports a `HookHandler` function:

Copy

```
import type { HookHandler } from '../../src/hooks/hooks.js';

const myHandler: HookHandler = async (event) => {
  // Only trigger on 'new' command
  if (event.type !== 'command' || event.action !== 'new') {
    return;
  }

  console.log(`[my-hook] New command triggered`);
  console.log(`  Session: ${event.sessionKey}`);
  console.log(`  Timestamp: ${event.timestamp.toISOString()}`);

  // Your custom logic here

  // Optionally send message to user
  event.messages.push('✨ My hook executed!');
};

export default myHandler;
```

#### [​](#event-context) Event Context

Each event includes:

Copy

```
{
  type: 'command' | 'session' | 'agent' | 'gateway',
  action: string,              // e.g., 'new', 'reset', 'stop'
  sessionKey: string,          // Session identifier
  timestamp: Date,             // When the event occurred
  messages: string[],          // Push messages here to send to user
  context: {
    sessionEntry?: SessionEntry,
    sessionId?: string,
    sessionFile?: string,
    commandSource?: string,    // e.g., 'whatsapp', 'telegram'
    senderId?: string,
    workspaceDir?: string,
    bootstrapFiles?: WorkspaceBootstrapFile[],
    cfg?: ClawdbotConfig
  }
}
```

## [​](#event-types) Event Types

### [​](#command-events) Command Events

Triggered when agent commands are issued:

* **`command`**: All command events (general listener)
* **`command:new`**: When `/new` command is issued
* **`command:reset`**: When `/reset` command is issued
* **`command:stop`**: When `/stop` command is issued

### [​](#agent-events) Agent Events

* **`agent:bootstrap`**: Before workspace bootstrap files are injected (hooks may mutate `context.bootstrapFiles`)

### [​](#gateway-events) Gateway Events

Triggered when the gateway starts:

* **`gateway:startup`**: After channels start and hooks are loaded

### [​](#tool-result-hooks-plugin-api) Tool Result Hooks (Plugin API)

These hooks are not event-stream listeners; they let plugins synchronously adjust tool results before Clawdbot persists them.

* **`tool_result_persist`**: transform tool results before they are written to the session transcript. Must be synchronous; return the updated tool result payload or `undefined` to keep it as-is. See [Agent Loop](/concepts/agent-loop).

### [​](#future-events) Future Events

Planned event types:

* **`session:start`**: When a new session begins
* **`session:end`**: When a session ends
* **`agent:error`**: When an agent encounters an error
* **`message:sent`**: When a message is sent
* **`message:received`**: When a message is received

## [​](#creating-custom-hooks) Creating Custom Hooks

### [​](#1-choose-location) 1. Choose Location

* **Workspace hooks** (`<workspace>/hooks/`): Per-agent, highest precedence
* **Managed hooks** (`~/.clawdbot/hooks/`): Shared across workspaces

### [​](#2-create-directory-structure) 2. Create Directory Structure

Copy

```
mkdir -p ~/.clawdbot/hooks/my-hook
cd ~/.clawdbot/hooks/my-hook
```

### [​](#3-create-hook-md) 3. Create HOOK.md

Copy

```
---
name: my-hook
description: "Does something useful"
metadata: {"clawdbot":{"emoji":"🎯","events":["command:new"]}}
---

# My Custom Hook

This hook does something useful when you issue `/new`.
```

### [​](#4-create-handler-ts) 4. Create handler.ts

Copy

```
import type { HookHandler } from '../../src/hooks/hooks.js';

const handler: HookHandler = async (event) => {
  if (event.type !== 'command' || event.action !== 'new') {
    return;
  }

  console.log('[my-hook] Running!');
  // Your logic here
};

export default handler;
```

### [​](#5-enable-and-test) 5. Enable and Test

Copy

```
# Verify hook is discovered
clawdbot hooks list

# Enable it
clawdbot hooks enable my-hook

# Restart your gateway process (menu bar app restart on macOS, or restart your dev process)

# Trigger the event
# Send /new via your messaging channel
```

## [​](#configuration) Configuration

### [​](#new-config-format-recommended) New Config Format (Recommended)

Copy

```
{
  "hooks": {
    "internal": {
      "enabled": true,
      "entries": {
        "session-memory": { "enabled": true },
        "command-logger": { "enabled": false }
      }
    }
  }
}
```

### [​](#per-hook-configuration) Per-Hook Configuration

Hooks can have custom configuration:

Copy

```
{
  "hooks": {
    "internal": {
      "enabled": true,
      "entries": {
        "my-hook": {
          "enabled": true,
          "env": {
            "MY_CUSTOM_VAR": "value"
          }
        }
      }
    }
  }
}
```

### [​](#extra-directories) Extra Directories

Load hooks from additional directories:

Copy

```
{
  "hooks": {
    "internal": {
      "enabled": true,
      "load": {
        "extraDirs": ["/path/to/more/hooks"]
      }
    }
  }
}
```

### [​](#legacy-config-format-still-supported) Legacy Config Format (Still Supported)

The old config format still works for backwards compatibility:

Copy

```
{
  "hooks": {
    "internal": {
      "enabled": true,
      "handlers": [
        {
          "event": "command:new",
          "module": "./hooks/handlers/my-handler.ts",
          "export": "default"
        }
      ]
    }
  }
}
```

**Migration**: Use the new discovery-based system for new hooks. Legacy handlers are loaded after directory-based hooks.

## [​](#cli-commands) CLI Commands

### [​](#list-hooks) List Hooks

Copy

```
# List all hooks
clawdbot hooks list

# Show only eligible hooks
clawdbot hooks list --eligible

# Verbose output (show missing requirements)
clawdbot hooks list --verbose

# JSON output
clawdbot hooks list --json
```

### [​](#hook-information) Hook Information

Copy

```
# Show detailed info about a hook
clawdbot hooks info session-memory

# JSON output
clawdbot hooks info session-memory --json
```

### [​](#check-eligibility) Check Eligibility

Copy

```
# Show eligibility summary
clawdbot hooks check

# JSON output
clawdbot hooks check --json
```

### [​](#enable/disable) Enable/Disable

Copy

```
# Enable a hook
clawdbot hooks enable session-memory

# Disable a hook
clawdbot hooks disable command-logger
```

## [​](#bundled-hooks-2) Bundled Hooks

### [​](#session-memory) session-memory

Saves session context to memory when you issue `/new`.
**Events**: `command:new`
**Requirements**: `workspace.dir` must be configured
**Output**: `<workspace>/memory/YYYY-MM-DD-slug.md` (defaults to `~/clawd`)
**What it does**:

1. Uses the pre-reset session entry to locate the correct transcript
2. Extracts the last 15 lines of conversation
3. Uses LLM to generate a descriptive filename slug
4. Saves session metadata to a dated memory file

**Example output**:

Copy

```
# Session: 2026-01-16 14:30:00 UTC

- **Session Key**: agent:main:main
- **Session ID**: abc123def456
- **Source**: telegram
```

**Filename examples**:

* `2026-01-16-vendor-pitch.md`
* `2026-01-16-api-design.md`
* `2026-01-16-1430.md` (fallback timestamp if slug generation fails)

**Enable**:

Copy

```
clawdbot hooks enable session-memory
```

### [​](#command-logger) command-logger

Logs all command events to a centralized audit file.
**Events**: `command`
**Requirements**: None
**Output**: `~/.clawdbot/logs/commands.log`
**What it does**:

1. Captures event details (command action, timestamp, session key, sender ID, source)
2. Appends to log file in JSONL format
3. Runs silently in the background

**Example log entries**:

Copy

```
{"timestamp":"2026-01-16T14:30:00.000Z","action":"new","sessionKey":"agent:main:main","senderId":"+1234567890","source":"telegram"}
{"timestamp":"2026-01-16T15:45:22.000Z","action":"stop","sessionKey":"agent:main:main","senderId":"[email protected]","source":"whatsapp"}
```

**View logs**:

Copy

```
# View recent commands
tail -n 20 ~/.clawdbot/logs/commands.log

# Pretty-print with jq
cat ~/.clawdbot/logs/commands.log | jq .

# Filter by action
grep '"action":"new"' ~/.clawdbot/logs/commands.log | jq .
```

**Enable**:

Copy

```
clawdbot hooks enable command-logger
```

### [​](#soul-evil) soul-evil

Swaps injected `SOUL.md` content with `SOUL_EVIL.md` during a purge window or by random chance.
**Events**: `agent:bootstrap`
**Docs**: [SOUL Evil Hook](/hooks/soul-evil)
**Output**: No files written; swaps happen in-memory only.
**Enable**:

Copy

```
clawdbot hooks enable soul-evil
```

**Config**:

Copy

```
{
  "hooks": {
    "internal": {
      "enabled": true,
      "entries": {
        "soul-evil": {
          "enabled": true,
          "file": "SOUL_EVIL.md",
          "chance": 0.1,
          "purge": { "at": "21:00", "duration": "15m" }
        }
      }
    }
  }
}
```

### [​](#boot-md) boot-md

Runs `BOOT.md` when the gateway starts (after channels start).
Internal hooks must be enabled for this to run.
**Events**: `gateway:startup`
**Requirements**: `workspace.dir` must be configured
**What it does**:

1. Reads `BOOT.md` from your workspace
2. Runs the instructions via the agent runner
3. Sends any requested outbound messages via the message tool

**Enable**:

Copy

```
clawdbot hooks enable boot-md
```

## [​](#best-practices) Best Practices

### [​](#keep-handlers-fast) Keep Handlers Fast

Hooks run during command processing. Keep them lightweight:

Copy

```
// ✓ Good - async work, returns immediately
const handler: HookHandler = async (event) => {
  void processInBackground(event); // Fire and forget
};

// ✗ Bad - blocks command processing
const handler: HookHandler = async (event) => {
  await slowDatabaseQuery(event);
  await evenSlowerAPICall(event);
};
```

### [​](#handle-errors-gracefully) Handle Errors Gracefully

Always wrap risky operations:

Copy

```
const handler: HookHandler = async (event) => {
  try {
    await riskyOperation(event);
  } catch (err) {
    console.error('[my-handler] Failed:', err instanceof Error ? err.message : String(err));
    // Don't throw - let other handlers run
  }
};
```

### [​](#filter-events-early) Filter Events Early

Return early if the event isn’t relevant:

Copy

```
const handler: HookHandler = async (event) => {
  // Only handle 'new' commands
  if (event.type !== 'command' || event.action !== 'new') {
    return;
  }

  // Your logic here
};
```

### [​](#use-specific-event-keys) Use Specific Event Keys

Specify exact events in metadata when possible:

Copy

```
metadata: {"clawdbot":{"events":["command:new"]}}  # Specific
```

Rather than:

Copy

```
metadata: {"clawdbot":{"events":["command"]}}      # General - more overhead
```

## [​](#debugging) Debugging

### [​](#enable-hook-logging) Enable Hook Logging

The gateway logs hook loading at startup:

Copy

```
Registered hook: session-memory -> command:new
Registered hook: command-logger -> command
Registered hook: boot-md -> gateway:startup
```

### [​](#check-discovery) Check Discovery

List all discovered hooks:

Copy

```
clawdbot hooks list --verbose
```

### [​](#check-registration) Check Registration

In your handler, log when it’s called:

Copy

```
const handler: HookHandler = async (event) => {
  console.log('[my-handler] Triggered:', event.type, event.action);
  // Your logic
};
```

### [​](#verify-eligibility) Verify Eligibility

Check why a hook isn’t eligible:

Copy

```
clawdbot hooks info my-hook
```

Look for missing requirements in the output.

## [​](#testing) Testing

### [​](#gateway-logs) Gateway Logs

Monitor gateway logs to see hook execution:

Copy

```
# macOS
./scripts/clawlog.sh -f

# Other platforms
tail -f ~/.clawdbot/gateway.log
```

### [​](#test-hooks-directly) Test Hooks Directly

Test your handlers in isolation:

Copy

```
import { test } from 'vitest';
import { createHookEvent } from './src/hooks/hooks.js';
import myHandler from './hooks/my-hook/handler.js';

test('my handler works', async () => {
  const event = createHookEvent('command', 'new', 'test-session', {
    foo: 'bar'
  });

  await myHandler(event);

  // Assert side effects
});
```

## [​](#architecture) Architecture

### [​](#core-components) Core Components

* **`src/hooks/types.ts`**: Type definitions
* **`src/hooks/workspace.ts`**: Directory scanning and loading
* **`src/hooks/frontmatter.ts`**: HOOK.md metadata parsing
* **`src/hooks/config.ts`**: Eligibility checking
* **`src/hooks/hooks-status.ts`**: Status reporting
* **`src/hooks/loader.ts`**: Dynamic module loader
* **`src/cli/hooks-cli.ts`**: CLI commands
* **`src/gateway/server-startup.ts`**: Loads hooks at gateway start
* **`src/auto-reply/reply/commands-core.ts`**: Triggers command events

### [​](#discovery-flow) Discovery Flow

Copy

```
Gateway startup
    ↓
Scan directories (workspace → managed → bundled)
    ↓
Parse HOOK.md files
    ↓
Check eligibility (bins, env, config, os)
    ↓
Load handlers from eligible hooks
    ↓
Register handlers for events
```

### [​](#event-flow) Event Flow

Copy

```
User sends /new
    ↓
Command validation
    ↓
Create hook event
    ↓
Trigger hook (all registered handlers)
    ↓
Command processing continues
    ↓
Session reset
```

## [​](#troubleshooting) Troubleshooting

### [​](#hook-not-discovered) Hook Not Discovered

1. Check directory structure:

   Copy

   ```
   ls -la ~/.clawdbot/hooks/my-hook/
   # Should show: HOOK.md, handler.ts
   ```
2. Verify HOOK.md format:

   Copy

   ```
   cat ~/.clawdbot/hooks/my-hook/HOOK.md
   # Should have YAML frontmatter with name and metadata
   ```
3. List all discovered hooks:

   Copy

   ```
   clawdbot hooks list
   ```

### [​](#hook-not-eligible) Hook Not Eligible

Check requirements:

Copy

```
clawdbot hooks info my-hook
```

Look for missing:

* Binaries (check PATH)
* Environment variables
* Config values
* OS compatibility

### [​](#hook-not-executing) Hook Not Executing

1. Verify hook is enabled:

   Copy

   ```
   clawdbot hooks list
   # Should show ✓ next to enabled hooks
   ```
2. Restart your gateway process so hooks reload.
3. Check gateway logs for errors:

   Copy

   ```
   ./scripts/clawlog.sh | grep hook
   ```

### [​](#handler-errors) Handler Errors

Check for TypeScript/import errors:

Copy

```
# Test import directly
node -e "import('./path/to/handler.ts').then(console.log)"
```

## [​](#migration-guide) Migration Guide

### [​](#from-legacy-config-to-discovery) From Legacy Config to Discovery

**Before**:

Copy

```
{
  "hooks": {
    "internal": {
      "enabled": true,
      "handlers": [
        {
          "event": "command:new",
          "module": "./hooks/handlers/my-handler.ts"
        }
      ]
    }
  }
}
```

**After**:

1. Create hook directory:

   Copy

   ```
   mkdir -p ~/.clawdbot/hooks/my-hook
   mv ./hooks/handlers/my-handler.ts ~/.clawdbot/hooks/my-hook/handler.ts
   ```
2. Create HOOK.md:

   Copy

   ```
   ---
   name: my-hook
   description: "My custom hook"
   metadata: {"clawdbot":{"emoji":"🎯","events":["command:new"]}}
   ---

   # My Hook

   Does something useful.
   ```
3. Update config:

   Copy

   ```
   {
     "hooks": {
       "internal": {
         "enabled": true,
         "entries": {
           "my-hook": { "enabled": true }
         }
       }
     }
   }
   ```
4. Verify and restart your gateway process:

   Copy

   ```
   clawdbot hooks list
   # Should show: 🎯 my-hook ✓
   ```

**Benefits of migration**:

* Automatic discovery
* CLI management
* Eligibility checking
* Better documentation
* Consistent structure

## [​](#see-also) See Also

* [CLI Reference: hooks](/cli/hooks)
* [Bundled Hooks README](https://github.com/clawdbot/clawdbot/tree/main/src/hooks/bundled)
* [Webhook Hooks](/automation/webhook)
* [Configuration](/gateway/configuration#hooks)