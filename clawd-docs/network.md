---
title: Network - Clawdbot
url: https://docs.clawd.bot/network
---

# [​](#network-hub) Network hub

This hub links the core docs for how Clawdbot connects, pairs, and secures
devices across localhost, LAN, and tailnet.

## [​](#core-model) Core model

* [Gateway architecture](/concepts/architecture)
* [Gateway protocol](/gateway/protocol)
* [Gateway runbook](/gateway)
* [Web surfaces + bind modes](/web)

## [​](#pairing-+-identity) Pairing + identity

* [Pairing overview (DM + nodes)](/start/pairing)
* [Gateway-owned node pairing](/gateway/pairing)
* [Devices CLI (pairing + token rotation)](/cli/devices)
* [Pairing CLI (DM approvals)](/cli/pairing)

Local trust:

* Local connections (loopback or the gateway host’s own tailnet address) can be
  auto‑approved for pairing to keep same‑host UX smooth.
* Non‑local tailnet/LAN clients still require explicit pairing approval.

## [​](#discovery-+-transports) Discovery + transports

* [Discovery & transports](/gateway/discovery)
* [Bonjour / mDNS](/gateway/bonjour)
* [Remote access (SSH)](/gateway/remote)
* [Tailscale](/gateway/tailscale)

## [​](#nodes-+-transports) Nodes + transports

* [Nodes overview](/nodes)
* [Bridge protocol (legacy nodes)](/gateway/bridge-protocol)
* [Node runbook: iOS](/platforms/ios)
* [Node runbook: Android](/platforms/android)

## [​](#security) Security

* [Security overview](/gateway/security)
* [Gateway config reference](/gateway/configuration)
* [Troubleshooting](/gateway/troubleshooting)
* [Doctor](/gateway/doctor)