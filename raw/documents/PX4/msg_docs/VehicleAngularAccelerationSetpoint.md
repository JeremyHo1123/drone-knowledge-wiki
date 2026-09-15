---
title: "VehicleAngularAccelerationSetpoint (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/VehicleAngularAccelerationSetpoint"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/VehicleAngularAccelerationSetpoint.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# VehicleAngularAccelerationSetpoint (UORB message)

**TOPICS:** vehicle_angular_acceleration_setpoint

## Fields

| Name                                              | Type         | Unit [Frame] | Range/Enum | Description                                                                |
| ------------------------------------------------- | ------------ | ------------ | ---------- | -------------------------------------------------------------------------- |
| <a id="fld_timestamp"></a>timestamp               | `uint64`     |              |            | time since system start (microseconds)                                     |
| <a id="fld_timestamp_sample"></a>timestamp_sample | `uint64`     |              |            | timestamp of the data sample on which this message is based (microseconds) |
| <a id="fld_xyz"></a>xyz                           | `float32[3]` |              |            | angular acceleration about X, Y, Z body axis in rad/s^2                    |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/VehicleAngularAccelerationSetpoint.msg)

::: details Click here to see original file

```c
uint64 timestamp         # time since system start (microseconds)
uint64 timestamp_sample  # timestamp of the data sample on which this message is based (microseconds)

float32[3] xyz           # angular acceleration about X, Y, Z body axis in rad/s^2
```

:::
