---
title: "Autotuning (VTOL)"
type: document
doc_set: PX4
doc_version: main
section: config
source_url: "https://docs.px4.io/main/en/config/autotune_vtol"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "config/autotune_vtol.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/config
---

# Autotuning (VTOL)

Auto-tuning automates the process of tuning the PX4 rate and attitude PID controllers, which are the most important controllers for stable and responsive flight (other tuning is more "optional").

Tuning only needs to be done once, and is recommended unless you're using a vehicle that has already been tuned by the manufacturer (and not modified since).

Hybrid VTOL fixed-wing vehicles ("VTOL") must be tuned following the multicopter instructions in MC mode and then the fixed-wing instructions in FW mode:

- [Auto-tune (Multicopter)](../config/autotune_mc.md)
- [Auto-tune (Fixed-wing)](../config/autotune_fw.md)
