---
title: "LateralControlConfiguration (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/LateralControlConfiguration"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/LateralControlConfiguration.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# LateralControlConfiguration (UORB message)

Fixed Wing Lateral Control Configuration message.

Used by the fw_lateral_longitudinal_control module to constrain FixedWingLateralSetpoint messages.

**TOPICS:** lateral_control_configuration

## Fields

| Name                                                | Type      | Unit [Frame] | Range/Enum | Description                                                                  |
| --------------------------------------------------- | --------- | ------------ | ---------- | ---------------------------------------------------------------------------- |
| <a id="fld_timestamp"></a>timestamp                 | `uint64`  | us           |            | Time since system start                                                      |
| <a id="fld_lateral_accel_max"></a>lateral_accel_max | `float32` | m/s^2        |            | Currently maps to a maximum roll angle, accel_max = tan(roll_max) \* GRAVITY |

## Constants

| Name                                          | Type     | Value | Description |
| --------------------------------------------- | -------- | ----- | ----------- |
| <a id="#MESSAGE_VERSION"></a> MESSAGE_VERSION | `uint32` | 0     |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/versioned/LateralControlConfiguration.msg)

::: details Click here to see original file

```c
# Fixed Wing Lateral Control Configuration message
#
# Used by the fw_lateral_longitudinal_control module to constrain FixedWingLateralSetpoint messages.

uint32 MESSAGE_VERSION = 0

uint64 timestamp # [us] Time since system start

float32 lateral_accel_max # [m/s^2] Currently maps to a maximum roll angle, accel_max = tan(roll_max) * GRAVITY
```

:::
