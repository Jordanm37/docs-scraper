---
title: Index - Clawdbot
url: https://docs.clawd.bot/install
---

# [​](#install) Install

Use the installer unless you have a reason not to. It sets up the CLI and runs onboarding.

## [​](#quick-install-recommended) Quick install (recommended)

Copy

```
curl -fsSL https://clawd.bot/install.sh | bash
```

Windows (PowerShell):

Copy

```
iwr -useb https://clawd.bot/install.ps1 | iex
```

Next step (if you skipped onboarding):

Copy

```
clawdbot onboard --install-daemon
```

## [​](#system-requirements) System requirements

* **Node >=22**
* macOS, Linux, or Windows via WSL2
* `pnpm` only if you build from source

## [​](#choose-your-install-path) Choose your install path

### [​](#1-installer-script-recommended) 1) Installer script (recommended)

Installs `clawdbot` globally via npm and runs onboarding.

Copy

```
curl -fsSL https://clawd.bot/install.sh | bash
```

Installer flags:

Copy

```
curl -fsSL https://clawd.bot/install.sh | bash -s -- --help
```

Details: [Installer internals](/install/installer).
Non-interactive (skip onboarding):

Copy

```
curl -fsSL https://clawd.bot/install.sh | bash -s -- --no-onboard
```

### [​](#2-global-install-manual) 2) Global install (manual)

If you already have Node:

Copy

```
npm install -g clawdbot@latest
```

If you have libvips installed globally (common on macOS via Homebrew) and `sharp` fails to install, force prebuilt binaries:

Copy

```
SHARP_IGNORE_GLOBAL_LIBVIPS=1 npm install -g clawdbot@latest
```

If you see `sharp: Please add node-gyp to your dependencies`, either install build tooling (macOS: Xcode CLT + `npm install -g node-gyp`) or use the `SHARP_IGNORE_GLOBAL_LIBVIPS=1` workaround above to skip the native build.
Or:

Copy

```
pnpm add -g clawdbot@latest
```

Then:

Copy

```
clawdbot onboard --install-daemon
```

### [​](#3-from-source-contributors/dev) 3) From source (contributors/dev)

Copy

```
git clone https://github.com/clawdbot/clawdbot.git
cd clawdbot
pnpm install
pnpm ui:build # auto-installs UI deps on first run
pnpm build
clawdbot onboard --install-daemon
```

Tip: if you don’t have a global install yet, run repo commands via `pnpm clawdbot ...`.

### [​](#4-other-install-options) 4) Other install options

* Docker: [Docker](/install/docker)
* Nix: [Nix](/install/nix)
* Ansible: [Ansible](/install/ansible)
* Bun (CLI only): [Bun](/install/bun)

## [​](#after-install) After install

* Run onboarding: `clawdbot onboard --install-daemon`
* Quick check: `clawdbot doctor`
* Check gateway health: `clawdbot status` + `clawdbot health`
* Open the dashboard: `clawdbot dashboard`

## [​](#install-method:-npm-vs-git-installer) Install method: npm vs git (installer)

The installer supports two methods:

* `npm` (default): `npm install -g clawdbot@latest`
* `git`: clone/build from GitHub and run from a source checkout

### [​](#cli-flags) CLI flags

Copy

```
# Explicit npm
curl -fsSL https://clawd.bot/install.sh | bash -s -- --install-method npm

# Install from GitHub (source checkout)
curl -fsSL https://clawd.bot/install.sh | bash -s -- --install-method git
```

Common flags:

* `--install-method npm|git`
* `--git-dir <path>` (default: `~/clawdbot`)
* `--no-git-update` (skip `git pull` when using an existing checkout)
* `--no-prompt` (disable prompts; required in CI/automation)
* `--dry-run` (print what would happen; make no changes)
* `--no-onboard` (skip onboarding)

### [​](#environment-variables) Environment variables

Equivalent env vars (useful for automation):

* `CLAWDBOT_INSTALL_METHOD=git|npm`
* `CLAWDBOT_GIT_DIR=...`
* `CLAWDBOT_GIT_UPDATE=0|1`
* `CLAWDBOT_NO_PROMPT=1`
* `CLAWDBOT_DRY_RUN=1`
* `CLAWDBOT_NO_ONBOARD=1`
* `SHARP_IGNORE_GLOBAL_LIBVIPS=0|1` (default: `1`; avoids `sharp` building against system libvips)

## [​](#troubleshooting:-clawdbot-not-found-path) Troubleshooting: `clawdbot` not found (PATH)

Quick diagnosis:

Copy

```
node -v
npm -v
npm prefix -g
echo "$PATH"
```

If `$(npm prefix -g)/bin` (macOS/Linux) or `$(npm prefix -g)` (Windows) is **not** present inside `echo "$PATH"`, your shell can’t find global npm binaries (including `clawdbot`).
Fix: add it to your shell startup file (zsh: `~/.zshrc`, bash: `~/.bashrc`):

Copy

```
# macOS / Linux
export PATH="$(npm prefix -g)/bin:$PATH"
```

On Windows, add the output of `npm prefix -g` to your PATH.
Then open a new terminal (or `rehash` in zsh / `hash -r` in bash).

## [​](#update-/-uninstall) Update / uninstall

* Updates: [Updating](/install/updating)
* Uninstall: [Uninstall](/install/uninstall)