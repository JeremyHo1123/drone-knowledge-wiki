---
title: "VehicleThrustSetpoint (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/VehicleThrustSetpoint"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/VehicleThrustSetpoint.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# VehicleThrustSetpoint (UORB message)

Vehicle thrust setpoint.

This is the thrust setpoint provided by the controller and fed into the control allocator.

**TOPICS:** vehicle_thrust_setpoint vehicle_thrust_setpoint_virtual_fw vehicle_thrust_setpoint_virtual_mc

## Fields

| Name                                              | Type         | Unit [Frame] | Range/Enum | Description                                                                                        |
| ------------------------------------------------- | ------------ | ------------ | ---------- | -------------------------------------------------------------------------------------------------- |
| <a id="fld_timestamp"></a>timestamp               | `uint64`     | us           |            | Time since system start                                                                            |
| <a id="fld_timestamp_sample"></a>timestamp_sample | `uint64`     | us           |            | Timestamp of the data sample on which this message is based                                        |
| <a id="fld_xyz"></a>xyz                           | `float32[3]` |              | [-1 : 1]   | Thrust setpoint along X, Y, Z body axis. If set to NAN the motors affecting this axis are stopped. |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/VehicleThrustSetpoint.msg)

::: details Click here to see original file

```c
# Vehicle thrust setpoint
#
# This is the thrust setpoint provided by the controller and fed into the control allocator.

uint64 timestamp        # [us] Time since system start
uint64 timestamp_sample # [us] Timestamp of the data sample on which this message is based

float32[3] xyz          # [-] [@range -1, 1] Thrust setpoint along X, Y, Z body axis. If set to NAN the motors affecting this axis are stopped.

# TOPICS vehicle_thrust_setpoint
# TOPICS vehicle_thrust_setpoint_virtual_fw vehicle_thrust_setpoint_virtual_mc
```

:::
