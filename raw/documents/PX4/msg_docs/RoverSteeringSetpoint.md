---
title: "RoverSteeringSetpoint (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/RoverSteeringSetpoint"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/RoverSteeringSetpoint.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# RoverSteeringSetpoint (UORB message)

Rover Steering setpoint.

**TOPICS:** rover_steering_setpoint

## Fields

| Name                                                                      | Type      | Unit [Frame] | Range/Enum              | Description                                                                                                               |
| ------------------------------------------------------------------------- | --------- | ------------ | ----------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| <a id="fld_timestamp"></a>timestamp                                       | `uint64`  | us           |                         | Time since system start                                                                                                   |
| <a id="fld_normalized_steering_setpoint"></a>normalized_steering_setpoint | `float32` | [Body]       | [-1 (Left) : 1 (Right)] | Ackermann: Normalized steering angle, Differential/Mecanum: Normalized speed difference between the left and right wheels |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/RoverSteeringSetpoint.msg)

::: details Click here to see original file

```c
# Rover Steering setpoint

uint64 timestamp                      # [us] Time since system start
float32 normalized_steering_setpoint  # [-] [@range -1 (Left), 1 (Right)] [@frame Body] Ackermann: Normalized steering angle, Differential/Mecanum: Normalized speed difference between the left and right wheels
```

:::
