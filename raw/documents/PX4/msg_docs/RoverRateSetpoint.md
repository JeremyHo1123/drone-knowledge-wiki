---
title: "RoverRateSetpoint (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/RoverRateSetpoint"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/RoverRateSetpoint.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# RoverRateSetpoint (UORB message)

Rover Rate setpoint.

**TOPICS:** rover_rate_setpoint

## Fields

| Name                                                | Type      | Unit [Frame] | Range/Enum   | Description             |
| --------------------------------------------------- | --------- | ------------ | ------------ | ----------------------- |
| <a id="fld_timestamp"></a>timestamp                 | `uint64`  | us           |              | Time since system start |
| <a id="fld_yaw_rate_setpoint"></a>yaw_rate_setpoint | `float32` | rad/s [NED]  | [-inf : inf] | Yaw rate setpoint       |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/RoverRateSetpoint.msg)

::: details Click here to see original file

```c
# Rover Rate setpoint

uint64 timestamp           # [us] Time since system start
float32 yaw_rate_setpoint  # [rad/s] [@range -inf, inf] [@frame NED] Yaw rate setpoint
```

:::
