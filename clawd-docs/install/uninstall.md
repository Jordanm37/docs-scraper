---
title: Uninstall - Clawdbot
url: https://docs.clawd.bot/install/uninstall
---

# [​](#uninstall) Uninstall

Two paths:

* **Easy path** if `clawdbot` is still installed.
* **Manual service removal** if the CLI is gone but the service is still running.

## [​](#easy-path-cli-still-installed) Easy path (CLI still installed)

Recommended: use the built-in uninstaller:

Copy

```
clawdbot uninstall
```

Non-interactive (automation / npx):

Copy

```
clawdbot uninstall --all --yes --non-interactive
npx -y clawdbot uninstall --all --yes --non-interactive
```

Manual steps (same result):

1. Stop the gateway service:

Copy

```
clawdbot gateway stop
```

2. Uninstall the gateway service (launchd/systemd/schtasks):

Copy

```
clawdbot gateway uninstall
```

3. Delete state + config:

Copy

```
rm -rf "${CLAWDBOT_STATE_DIR:-$HOME/.clawdbot}"
```

If you set `CLAWDBOT_CONFIG_PATH` to a custom location outside the state dir, delete that file too.

4. Delete your workspace (optional, removes agent files):

Copy

```
rm -rf ~/clawd
```

5. Remove the CLI install (pick the one you used):

Copy

```
npm rm -g clawdbot
pnpm remove -g clawdbot
bun remove -g clawdbot
```

6. If you installed the macOS app:

Copy

```
rm -rf /Applications/Clawdbot.app
```

Notes:

* If you used profiles (`--profile` / `CLAWDBOT_PROFILE`), repeat step 3 for each state dir (defaults are `~/.clawdbot-<profile>`).
* In remote mode, the state dir lives on the **gateway host**, so run steps 1-4 there too.

## [​](#manual-service-removal-cli-not-installed) Manual service removal (CLI not installed)

Use this if the gateway service keeps running but `clawdbot` is missing.

### [​](#macos-launchd) macOS (launchd)

Default label is `com.clawdbot.gateway` (or `com.clawdbot.<profile>`):

Copy

```
launchctl bootout gui/$UID/com.clawdbot.gateway
rm -f ~/Library/LaunchAgents/com.clawdbot.gateway.plist
```

If you used a profile, replace the label and plist name with `com.clawdbot.<profile>`.

### [​](#linux-systemd-user-unit) Linux (systemd user unit)

Default unit name is `clawdbot-gateway.service` (or `clawdbot-gateway-<profile>.service`):

Copy

```
systemctl --user disable --now clawdbot-gateway.service
rm -f ~/.config/systemd/user/clawdbot-gateway.service
systemctl --user daemon-reload
```

### [​](#windows-scheduled-task) Windows (Scheduled Task)

Default task name is `Clawdbot Gateway` (or `Clawdbot Gateway (<profile>)`).
The task script lives under your state dir.

Copy

```
schtasks /Delete /F /TN "Clawdbot Gateway"
Remove-Item -Force "$env:USERPROFILE\.clawdbot\gateway.cmd"
```

If you used a profile, delete the matching task name and `~\.clawdbot-<profile>\gateway.cmd`.

## [​](#normal-install-vs-source-checkout) Normal install vs source checkout

### [​](#normal-install-install-sh-/-npm-/-pnpm-/-bun) Normal install (install.sh / npm / pnpm / bun)

If you used `https://clawd.bot/install.sh` or `install.ps1`, the CLI was installed with `npm install -g clawdbot@latest`.
Remove it with `npm rm -g clawdbot` (or `pnpm remove -g` / `bun remove -g` if you installed that way).

### [​](#source-checkout-git-clone) Source checkout (git clone)

If you run from a repo checkout (`git clone` + `clawdbot ...` / `bun run clawdbot ...`):

1. Uninstall the gateway service **before** deleting the repo (use the easy path above or manual service removal).
2. Delete the repo directory.
3. Remove state + workspace as shown above.