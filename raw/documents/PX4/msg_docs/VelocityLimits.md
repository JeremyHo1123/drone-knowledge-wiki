---
title: "VelocityLimits (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/VelocityLimits"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/VelocityLimits.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# VelocityLimits (UORB message)

Velocity and yaw rate limits for a multicopter position slow mode only.

**TOPICS:** velocity_limits

## Fields

| Name                                                    | Type      | Unit [Frame] | Range/Enum | Description                            |
| ------------------------------------------------------- | --------- | ------------ | ---------- | -------------------------------------- |
| <a id="fld_timestamp"></a>timestamp                     | `uint64`  |              |            | time since system start (microseconds) |
| <a id="fld_horizontal_velocity"></a>horizontal_velocity | `float32` | m/s          |            |
| <a id="fld_vertical_velocity"></a>vertical_velocity     | `float32` | m/s          |            |
| <a id="fld_yaw_rate"></a>yaw_rate                       | `float32` | rad/s        |            |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/VelocityLimits.msg)

::: details Click here to see original file

```c
# Velocity and yaw rate limits for a multicopter position slow mode only

uint64 timestamp # time since system start (microseconds)

# absolute speeds, NAN means use default limit
float32 horizontal_velocity # [m/s]
float32 vertical_velocity # [m/s]
float32 yaw_rate # [rad/s]
```

:::
