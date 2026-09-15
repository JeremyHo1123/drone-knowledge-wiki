---
title: "VehicleAcceleration (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/VehicleAcceleration"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/VehicleAcceleration.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# VehicleAcceleration (UORB message)

**TOPICS:** vehicle_acceleration

## Fields

| Name                                              | Type         | Unit [Frame] | Range/Enum | Description                                                                             |
| ------------------------------------------------- | ------------ | ------------ | ---------- | --------------------------------------------------------------------------------------- |
| <a id="fld_timestamp"></a>timestamp               | `uint64`     |              |            | time since system start (microseconds)                                                  |
| <a id="fld_timestamp_sample"></a>timestamp_sample | `uint64`     |              |            | the timestamp of the raw data (microseconds)                                            |
| <a id="fld_xyz"></a>xyz                           | `float32[3]` |              |            | Bias corrected acceleration (including gravity) in the FRD body frame XYZ-axis in m/s^2 |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/VehicleAcceleration.msg)

::: details Click here to see original file

```c
uint64 timestamp		# time since system start (microseconds)

uint64 timestamp_sample		# the timestamp of the raw data (microseconds)

float32[3] xyz			# Bias corrected acceleration (including gravity) in the FRD body frame XYZ-axis in m/s^2
```

:::
