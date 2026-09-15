---
title: "VehicleAngularVelocity (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/VehicleAngularVelocity"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/VehicleAngularVelocity.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# VehicleAngularVelocity (UORB message)

**TOPICS:** vehicle_angular_velocity vehicle_angular_velocity_groundtruth

## Fields

| Name                                              | Type         | Unit [Frame] | Range/Enum | Description                                                                |
| ------------------------------------------------- | ------------ | ------------ | ---------- | -------------------------------------------------------------------------- |
| <a id="fld_timestamp"></a>timestamp               | `uint64`     |              |            | time since system start (microseconds)                                     |
| <a id="fld_timestamp_sample"></a>timestamp_sample | `uint64`     |              |            | timestamp of the data sample on which this message is based (microseconds) |
| <a id="fld_xyz"></a>xyz                           | `float32[3]` |              |            | Bias corrected angular velocity about the FRD body frame XYZ-axis in rad/s |
| <a id="fld_xyz_derivative"></a>xyz_derivative     | `float32[3]` |              |            | angular acceleration about the FRD body frame XYZ-axis in rad/s^2          |

## Constants

| Name                                          | Type     | Value | Description |
| --------------------------------------------- | -------- | ----- | ----------- |
| <a id="#MESSAGE_VERSION"></a> MESSAGE_VERSION | `uint32` | 0     |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/versioned/VehicleAngularVelocity.msg)

::: details Click here to see original file

```c
uint32 MESSAGE_VERSION = 0

uint64 timestamp          # time since system start (microseconds)
uint64 timestamp_sample   # timestamp of the data sample on which this message is based (microseconds)

float32[3] xyz		  # Bias corrected angular velocity about the FRD body frame XYZ-axis in rad/s

float32[3] xyz_derivative # angular acceleration about the FRD body frame XYZ-axis in rad/s^2

# TOPICS vehicle_angular_velocity vehicle_angular_velocity_groundtruth
```

:::
