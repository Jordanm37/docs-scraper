---
title: Clawdhub - Clawdbot
url: https://docs.clawd.bot/tools/clawdhub
---

# [​](#clawdhub) ClawdHub

ClawdHub is the **public skill registry for Clawdbot**. It is a free service: all skills are public, open, and visible to everyone for sharing and reuse. A skill is just a folder with a `SKILL.md` file (plus supporting text files). You can browse skills in the web app or use the CLI to search, install, update, and publish skills.
Site: [clawdhub.com](https://clawdhub.com)

## [​](#who-this-is-for-beginner-friendly) Who this is for (beginner-friendly)

If you want to add new capabilities to your Clawdbot agent, ClawdHub is the easiest way to find and install skills. You do not need to know how the backend works. You can:

* Search for skills by plain language.
* Install a skill into your workspace.
* Update skills later with one command.
* Back up your own skills by publishing them.

## [​](#quick-start-non-technical) Quick start (non-technical)

1. Install the CLI (see next section).
2. Search for something you need:
   * `clawdhub search "calendar"`
3. Install a skill:
   * `clawdhub install <skill-slug>`
4. Start a new Clawdbot session so it picks up the new skill.

## [​](#install-the-cli) Install the CLI

Pick one:

Copy

```
npm i -g clawdhub
```

Copy

```
pnpm add -g clawdhub
```

## [​](#how-it-fits-into-clawdbot) How it fits into Clawdbot

By default, the CLI installs skills into `./skills` under your current working directory. If a Clawdbot workspace is configured, `clawdhub` falls back to that workspace unless you override `--workdir` (or `CLAWDHUB_WORKDIR`). Clawdbot loads workspace skills from `<workspace>/skills` and will pick them up in the **next** session. If you already use `~/.clawdbot/skills` or bundled skills, workspace skills take precedence.
For more detail on how skills are loaded, shared, and gated, see
[Skills](/tools/skills).

## [​](#what-the-service-provides-features) What the service provides (features)

* **Public browsing** of skills and their `SKILL.md` content.
* **Search** powered by embeddings (vector search), not just keywords.
* **Versioning** with semver, changelogs, and tags (including `latest`).
* **Downloads** as a zip per version.
* **Stars and comments** for community feedback.
* **Moderation** hooks for approvals and audits.
* **CLI-friendly API** for automation and scripting.

## [​](#cli-commands-and-parameters) CLI commands and parameters

Global options (apply to all commands):

* `--workdir <dir>`: Working directory (default: current dir; falls back to Clawdbot workspace).
* `--dir <dir>`: Skills directory, relative to workdir (default: `skills`).
* `--site <url>`: Site base URL (browser login).
* `--registry <url>`: Registry API base URL.
* `--no-input`: Disable prompts (non-interactive).
* `-V, --cli-version`: Print CLI version.

Auth:

* `clawdhub login` (browser flow) or `clawdhub login --token <token>`
* `clawdhub logout`
* `clawdhub whoami`

Options:

* `--token <token>`: Paste an API token.
* `--label <label>`: Label stored for browser login tokens (default: `CLI token`).
* `--no-browser`: Do not open a browser (requires `--token`).

Search:

* `clawdhub search "query"`
* `--limit <n>`: Max results.

Install:

* `clawdhub install <slug>`
* `--version <version>`: Install a specific version.
* `--force`: Overwrite if the folder already exists.

Update:

* `clawdhub update <slug>`
* `clawdhub update --all`
* `--version <version>`: Update to a specific version (single slug only).
* `--force`: Overwrite when local files do not match any published version.

List:

* `clawdhub list` (reads `.clawdhub/lock.json`)

Publish:

* `clawdhub publish <path>`
* `--slug <slug>`: Skill slug.
* `--name <name>`: Display name.
* `--version <version>`: Semver version.
* `--changelog <text>`: Changelog text (can be empty).
* `--tags <tags>`: Comma-separated tags (default: `latest`).

Delete/undelete (owner/admin only):

* `clawdhub delete <slug> --yes`
* `clawdhub undelete <slug> --yes`

Sync (scan local skills + publish new/updated):

* `clawdhub sync`
* `--root <dir...>`: Extra scan roots.
* `--all`: Upload everything without prompts.
* `--dry-run`: Show what would be uploaded.
* `--bump <type>`: `patch|minor|major` for updates (default: `patch`).
* `--changelog <text>`: Changelog for non-interactive updates.
* `--tags <tags>`: Comma-separated tags (default: `latest`).
* `--concurrency <n>`: Registry checks (default: 4).

## [​](#common-workflows-for-agents) Common workflows for agents

### [​](#search-for-skills) Search for skills

Copy

```
clawdhub search "postgres backups"
```

### [​](#download-new-skills) Download new skills

Copy

```
clawdhub install my-skill-pack
```

### [​](#update-installed-skills) Update installed skills

Copy

```
clawdhub update --all
```

### [​](#back-up-your-skills-publish-or-sync) Back up your skills (publish or sync)

For a single skill folder:

Copy

```
clawdhub publish ./my-skill --slug my-skill --name "My Skill" --version 1.0.0 --tags latest
```

To scan and back up many skills at once:

Copy

```
clawdhub sync --all
```

## [​](#advanced-details-technical) Advanced details (technical)

### [​](#versioning-and-tags) Versioning and tags

* Each publish creates a new **semver** `SkillVersion`.
* Tags (like `latest`) point to a version; moving tags lets you roll back.
* Changelogs are attached per version and can be empty when syncing or publishing updates.

### [​](#local-changes-vs-registry-versions) Local changes vs registry versions

Updates compare the local skill contents to registry versions using a content hash. If local files do not match any published version, the CLI asks before overwriting (or requires `--force` in non-interactive runs).

### [​](#sync-scanning-and-fallback-roots) Sync scanning and fallback roots

`clawdhub sync` scans your current workdir first. If no skills are found, it falls back to known legacy locations (for example `~/clawdbot/skills` and `~/.clawdbot/skills`). This is designed to find older skill installs without extra flags.

### [​](#storage-and-lockfile) Storage and lockfile

* Installed skills are recorded in `.clawdhub/lock.json` under your workdir.
* Auth tokens are stored in the ClawdHub CLI config file (override via `CLAWDHUB_CONFIG_PATH`).

### [​](#telemetry-install-counts) Telemetry (install counts)

When you run `clawdhub sync` while logged in, the CLI sends a minimal snapshot to compute install counts. You can disable this entirely:

Copy

```
export CLAWDHUB_DISABLE_TELEMETRY=1
```

## [​](#environment-variables) Environment variables

* `CLAWDHUB_SITE`: Override the site URL.
* `CLAWDHUB_REGISTRY`: Override the registry API URL.
* `CLAWDHUB_CONFIG_PATH`: Override where the CLI stores the token/config.
* `CLAWDHUB_WORKDIR`: Override the default workdir.
* `CLAWDHUB_DISABLE_TELEMETRY=1`: Disable telemetry on `sync`.