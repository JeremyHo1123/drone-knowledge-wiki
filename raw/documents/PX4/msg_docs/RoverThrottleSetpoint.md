---
title: "RoverThrottleSetpoint (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/RoverThrottleSetpoint"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/RoverThrottleSetpoint.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# RoverThrottleSetpoint (UORB message)

Rover Throttle setpoint.

**TOPICS:** rover_throttle_setpoint

## Fields

| Name                                            | Type      | Unit [Frame] | Range/Enum                      | Description                                                                     |
| ----------------------------------------------- | --------- | ------------ | ------------------------------- | ------------------------------------------------------------------------------- |
| <a id="fld_timestamp"></a>timestamp             | `uint64`  | us           |                                 | Time since system start                                                         |
| <a id="fld_throttle_body_x"></a>throttle_body_x | `float32` | [Body]       | [-1 (Backwards) : 1 (Forwards)] | Throttle setpoint along body X axis                                             |
| <a id="fld_throttle_body_y"></a>throttle_body_y | `float32` | [Body]       | [-1 (Left) : 1 (Right)]         | Mecanum only: Throttle setpoint along body Y axis (Invalid: NaN If not mecanum) |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/RoverThrottleSetpoint.msg)

::: details Click here to see original file

```c
# Rover Throttle setpoint

uint64 timestamp         # [us] Time since system start
float32 throttle_body_x  # [-] [@range -1 (Backwards), 1 (Forwards)] [@frame Body] Throttle setpoint along body X axis
float32 throttle_body_y  # [-] [@range -1 (Left), 1 (Right)] [@frame Body] [@invalid NaN If not mecanum] Mecanum only: Throttle setpoint along body Y axis
```

:::
