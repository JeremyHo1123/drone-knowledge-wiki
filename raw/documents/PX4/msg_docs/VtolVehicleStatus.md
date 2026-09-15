---
title: "VtolVehicleStatus (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/VtolVehicleStatus"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/VtolVehicleStatus.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# VtolVehicleStatus (UORB message)

VEHICLE_VTOL_STATE, should match 1:1 MAVLinks's MAV_VTOL_STATE.

**TOPICS:** vtol_vehicle_status

## Fields

| Name                                                                | Type     | Unit [Frame] | Range/Enum | Description                                                           |
| ------------------------------------------------------------------- | -------- | ------------ | ---------- | --------------------------------------------------------------------- |
| <a id="fld_timestamp"></a>timestamp                                 | `uint64` |              |            | time since system start (microseconds)                                |
| <a id="fld_vehicle_vtol_state"></a>vehicle_vtol_state               | `uint8`  |              |            | current state of the vtol, see VEHICLE_VTOL_STATE                     |
| <a id="fld_fixed_wing_system_failure"></a>fixed_wing_system_failure | `bool`   |              |            | vehicle in fixed-wing system failure failsafe mode (after quad-chute) |

## Constants

| Name                                                                                  | Type     | Value | Description |
| ------------------------------------------------------------------------------------- | -------- | ----- | ----------- |
| <a id="#MESSAGE_VERSION"></a> MESSAGE_VERSION                                         | `uint32` | 0     |
| <a id="#VEHICLE_VTOL_STATE_UNDEFINED"></a> VEHICLE_VTOL_STATE_UNDEFINED               | `uint8`  | 0     |
| <a id="#VEHICLE_VTOL_STATE_TRANSITION_TO_FW"></a> VEHICLE_VTOL_STATE_TRANSITION_TO_FW | `uint8`  | 1     |
| <a id="#VEHICLE_VTOL_STATE_TRANSITION_TO_MC"></a> VEHICLE_VTOL_STATE_TRANSITION_TO_MC | `uint8`  | 2     |
| <a id="#VEHICLE_VTOL_STATE_MC"></a> VEHICLE_VTOL_STATE_MC                             | `uint8`  | 3     |
| <a id="#VEHICLE_VTOL_STATE_FW"></a> VEHICLE_VTOL_STATE_FW                             | `uint8`  | 4     |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/versioned/VtolVehicleStatus.msg)

::: details Click here to see original file

```c
# VEHICLE_VTOL_STATE, should match 1:1 MAVLinks's MAV_VTOL_STATE

uint32 MESSAGE_VERSION = 0

uint8 VEHICLE_VTOL_STATE_UNDEFINED = 0
uint8 VEHICLE_VTOL_STATE_TRANSITION_TO_FW = 1
uint8 VEHICLE_VTOL_STATE_TRANSITION_TO_MC = 2
uint8 VEHICLE_VTOL_STATE_MC = 3
uint8 VEHICLE_VTOL_STATE_FW = 4

uint64 timestamp			# time since system start (microseconds)

uint8 vehicle_vtol_state		# current state of the vtol, see VEHICLE_VTOL_STATE

bool fixed_wing_system_failure		# vehicle in fixed-wing system failure failsafe mode (after quad-chute)
```

:::
