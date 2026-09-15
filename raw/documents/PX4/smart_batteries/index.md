---
title: "Smart Batteries"
type: document
doc_set: PX4
doc_version: main
section: smart_batteries
source_url: "https://docs.px4.io/main/en/smart_batteries/"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "smart_batteries/index.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/smart-batteries
---

# Smart Batteries

Smart Batteries provide more accurate (and often more detailed) information about the state of a battery than an autopilot can estimate for "dumb" batteries.
This allows for more reliable flight planning notification of failure conditions.
The information may include some of: remaining charge, time-to-empty (estimated), cell voltages (rated max/min, current voltage, etc.), temperature, currents, fault information, battery vendor, chemistry, etc.

PX4 supports (at least) following smart batteries:

- [Rotoye Batmon](../smart_batteries/rotoye_batmon.md)

### Further Information

- [Mavlink Battery Protocol](https://mavlink.io/en/services/battery.html)
- [batt_smbus](../modules/modules_driver.md) - PX4 SMBus Battery Driver docs
- [Safety > Low Battery Failsafe](../config/safety.md#battery-level-failsafe).
