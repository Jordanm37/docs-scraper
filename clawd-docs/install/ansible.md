---
title: Ansible - Clawdbot
url: https://docs.clawd.bot/install/ansible
---

# [​](#ansible-installation) Ansible Installation

The recommended way to deploy Clawdbot to production servers is via **[clawdbot-ansible](https://github.com/clawdbot/clawdbot-ansible)** — an automated installer with security-first architecture.

## [​](#quick-start) Quick Start

One-command install:

Copy

```
curl -fsSL https://raw.githubusercontent.com/clawdbot/clawdbot-ansible/main/install.sh | bash
```

> **📦 Full guide: [github.com/clawdbot/clawdbot-ansible](https://github.com/clawdbot/clawdbot-ansible)**
> The clawdbot-ansible repo is the source of truth for Ansible deployment. This page is a quick overview.

## [​](#what-you-get) What You Get

* 🔒 **Firewall-first security**: UFW + Docker isolation (only SSH + Tailscale accessible)
* 🔐 **Tailscale VPN**: Secure remote access without exposing services publicly
* 🐳 **Docker**: Isolated sandbox containers, localhost-only bindings
* 🛡️ **Defense in depth**: 4-layer security architecture
* 🚀 **One-command setup**: Complete deployment in minutes
* 🔧 **Systemd integration**: Auto-start on boot with hardening

## [​](#requirements) Requirements

* **OS**: Debian 11+ or Ubuntu 20.04+
* **Access**: Root or sudo privileges
* **Network**: Internet connection for package installation
* **Ansible**: 2.14+ (installed automatically by quick-start script)

## [​](#what-gets-installed) What Gets Installed

The Ansible playbook installs and configures:

1. **Tailscale** (mesh VPN for secure remote access)
2. **UFW firewall** (SSH + Tailscale ports only)
3. **Docker CE + Compose V2** (for agent sandboxes)
4. **Node.js 22.x + pnpm** (runtime dependencies)
5. **Clawdbot** (host-based, not containerized)
6. **Systemd service** (auto-start with security hardening)

Note: The gateway runs **directly on the host** (not in Docker), but agent sandboxes use Docker for isolation. See [Sandboxing](/gateway/sandboxing) for details.

## [​](#post-install-setup) Post-Install Setup

After installation completes, switch to the clawdbot user:

Copy

```
sudo -i -u clawdbot
```

The post-install script will guide you through:

1. **Onboarding wizard**: Configure Clawdbot settings
2. **Provider login**: Connect WhatsApp/Telegram/Discord/Signal
3. **Gateway testing**: Verify the installation
4. **Tailscale setup**: Connect to your VPN mesh

### [​](#quick-commands) Quick commands

Copy

```
# Check service status
sudo systemctl status clawdbot

# View live logs
sudo journalctl -u clawdbot -f

# Restart gateway
sudo systemctl restart clawdbot

# Provider login (run as clawdbot user)
sudo -i -u clawdbot
clawdbot channels login
```

## [​](#security-architecture) Security Architecture

### [​](#4-layer-defense) 4-Layer Defense

1. **Firewall (UFW)**: Only SSH (22) + Tailscale (41641/udp) exposed publicly
2. **VPN (Tailscale)**: Gateway accessible only via VPN mesh
3. **Docker Isolation**: DOCKER-USER iptables chain prevents external port exposure
4. **Systemd Hardening**: NoNewPrivileges, PrivateTmp, unprivileged user

### [​](#verification) Verification

Test external attack surface:

Copy

```
nmap -p- YOUR_SERVER_IP
```

Should show **only port 22** (SSH) open. All other services (gateway, Docker) are locked down.

### [​](#docker-availability) Docker Availability

Docker is installed for **agent sandboxes** (isolated tool execution), not for running the gateway itself. The gateway binds to localhost only and is accessible via Tailscale VPN.
See [Multi-Agent Sandbox & Tools](/multi-agent-sandbox-tools) for sandbox configuration.

## [​](#manual-installation) Manual Installation

If you prefer manual control over the automation:

Copy

```
# 1. Install prerequisites
sudo apt update && sudo apt install -y ansible git

# 2. Clone repository
git clone https://github.com/clawdbot/clawdbot-ansible.git
cd clawdbot-ansible

# 3. Install Ansible collections
ansible-galaxy collection install -r requirements.yml

# 4. Run playbook
./run-playbook.sh

# Or run directly (then manually execute /tmp/clawdbot-setup.sh after)
# ansible-playbook playbook.yml --ask-become-pass
```

## [​](#updating-clawdbot) Updating Clawdbot

The Ansible installer sets up Clawdbot for manual updates. See [Updating](/install/updating) for the standard update flow.
To re-run the Ansible playbook (e.g., for configuration changes):

Copy

```
cd clawdbot-ansible
./run-playbook.sh
```

Note: This is idempotent and safe to run multiple times.

## [​](#troubleshooting) Troubleshooting

### [​](#firewall-blocks-my-connection) Firewall blocks my connection

If you’re locked out:

* Ensure you can access via Tailscale VPN first
* SSH access (port 22) is always allowed
* The gateway is **only** accessible via Tailscale by design

### [​](#service-won’t-start) Service won’t start

Copy

```
# Check logs
sudo journalctl -u clawdbot -n 100

# Verify permissions
sudo ls -la /opt/clawdbot

# Test manual start
sudo -i -u clawdbot
cd ~/clawdbot
pnpm start
```

### [​](#docker-sandbox-issues) Docker sandbox issues

Copy

```
# Verify Docker is running
sudo systemctl status docker

# Check sandbox image
sudo docker images | grep clawdbot-sandbox

# Build sandbox image if missing
cd /opt/clawdbot/clawdbot
sudo -u clawdbot ./scripts/sandbox-setup.sh
```

### [​](#provider-login-fails) Provider login fails

Make sure you’re running as the `clawdbot` user:

Copy

```
sudo -i -u clawdbot
clawdbot channels login
```

## [​](#advanced-configuration) Advanced Configuration

For detailed security architecture and troubleshooting:

* [Security Architecture](https://github.com/clawdbot/clawdbot-ansible/blob/main/docs/security.md)
* [Technical Details](https://github.com/clawdbot/clawdbot-ansible/blob/main/docs/architecture.md)
* [Troubleshooting Guide](https://github.com/clawdbot/clawdbot-ansible/blob/main/docs/troubleshooting.md)

## [​](#related) Related

* [clawdbot-ansible](https://github.com/clawdbot/clawdbot-ansible) — full deployment guide
* [Docker](/install/docker) — containerized gateway setup
* [Sandboxing](/gateway/sandboxing) — agent sandbox configuration
* [Multi-Agent Sandbox & Tools](/multi-agent-sandbox-tools) — per-agent isolation