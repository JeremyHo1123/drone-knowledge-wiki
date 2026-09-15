---
title: "RoverSpeedSetpoint (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/RoverSpeedSetpoint"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/RoverSpeedSetpoint.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# RoverSpeedSetpoint (UORB message)

Rover Speed Setpoint.

**TOPICS:** rover_speed_setpoint

## Fields

| Name                                      | Type      | Unit [Frame] | Range/Enum                          | Description                                                                    |
| ----------------------------------------- | --------- | ------------ | ----------------------------------- | ------------------------------------------------------------------------------ |
| <a id="fld_timestamp"></a>timestamp       | `uint64`  | us           |                                     | Time since system start                                                        |
| <a id="fld_speed_body_x"></a>speed_body_x | `float32` | m/s [Body]   | [-inf (Backwards) : inf (Forwards)] | Speed setpoint in body x direction                                             |
| <a id="fld_speed_body_y"></a>speed_body_y | `float32` | m/s [Body]   | [-inf (Left) : inf (Right)]         | Mecanum only: Speed setpoint in body y direction (Invalid: NaN If not mecanum) |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/RoverSpeedSetpoint.msg)

::: details Click here to see original file

```c
# Rover Speed Setpoint

uint64 timestamp      # [us] Time since system start
float32 speed_body_x  # [m/s] [@range -inf (Backwards), inf (Forwards)] [@frame Body] Speed setpoint in body x direction
float32 speed_body_y  # [m/s] [@range -inf (Left), inf (Right)] [@frame Body] [@invalid NaN If not mecanum] Mecanum only: Speed setpoint in body y direction
```

:::
