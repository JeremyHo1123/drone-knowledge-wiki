---
title: "Land Mode (VTOL)"
type: document
doc_set: PX4
doc_version: main
section: flight_modes_vtol
source_url: "https://docs.px4.io/main/en/flight_modes_vtol/land"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "flight_modes_vtol/land.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/flight-modes-vtol
---

# Land Mode (VTOL)

<img src="https://raw.githubusercontent.com/PX4/PX4-Autopilot/main/docs/assets/site/position_fixed.svg" title="Position estimate required (e.g. GPS)" width="30px" />

The _Land_ flight mode causes the vehicle to land at the position where the mode was engaged.
After landing, vehicles will disarm after a short timeout (by default).

A VTOL follows the land mode behavior and parameters of [Fixed-wing](../flight_modes_fw/land.md) when in FW mode, and of [Multicopter](../flight_modes_mc/land.md) when in MC mode.

By default a VTOL in FW mode will transition back to MC just before landing.

## Parameters

The VTOL-specific parameters are:

| Parameter                                                              | Description                                                     |
| ---------------------------------------------------------------------- | --------------------------------------------------------------- |
| [NAV_FORCE_VT](../advanced_config/parameter_reference.md#NAV_FORCE_VT) | Force VTOL to takeoff and land as a multicopter (default: true) |

## See Also

- [Land Mode (MC)](../flight_modes_mc/land.md)
- [Land Mode (FW)](../flight_modes_fw/land.md)
