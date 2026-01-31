---
title: Vps - Clawdbot
url: https://docs.clawd.bot/vps
---

# [​](#vps-hosting) VPS hosting

This hub links to the supported VPS/hosting guides and explains how cloud
deployments work at a high level.

## [​](#pick-a-provider) Pick a provider

* **Railway** (one‑click + browser setup): [Railway](/railway)
* **Fly.io**: [Fly.io](/platforms/fly)
* **Hetzner (Docker)**: [Hetzner](/platforms/hetzner)
* **exe.dev** (VM + HTTPS proxy): [exe.dev](/platforms/exe-dev)
* **AWS (EC2/Lightsail/free tier)**: works well too. Video guide:
  <https://x.com/techfrenAJ/status/2014934471095812547>

## [​](#how-cloud-setups-work) How cloud setups work

* The **Gateway runs on the VPS** and owns state + workspace.
* You connect from your laptop/phone via the **Control UI** or **Tailscale/SSH**.
* Treat the VPS as the source of truth and **back up** the state + workspace.

Remote access: [Gateway remote](/gateway/remote)  
Platforms hub: [Platforms](/platforms)

## [​](#using-nodes-with-a-vps) Using nodes with a VPS

You can keep the Gateway in the cloud and pair **nodes** on your local devices
(Mac/iOS/Android/headless). Nodes provide local screen/camera/canvas and `system.run`
capabilities while the Gateway stays in the cloud.
Docs: [Nodes](/nodes), [Nodes CLI](/cli/nodes)