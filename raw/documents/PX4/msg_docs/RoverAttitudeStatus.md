---
title: "RoverAttitudeStatus (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/RoverAttitudeStatus"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/RoverAttitudeStatus.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# RoverAttitudeStatus (UORB message)

Rover Attitude Status.

**TOPICS:** rover_attitude_status

## Fields

| Name                                                        | Type      | Unit [Frame] | Range/Enum | Description                                             |
| ----------------------------------------------------------- | --------- | ------------ | ---------- | ------------------------------------------------------- |
| <a id="fld_timestamp"></a>timestamp                         | `uint64`  | us           |            | Time since system start                                 |
| <a id="fld_measured_yaw"></a>measured_yaw                   | `float32` | rad [NED]    | [-pi : pi] | Measured yaw                                            |
| <a id="fld_adjusted_yaw_setpoint"></a>adjusted_yaw_setpoint | `float32` | rad [NED]    | [-pi : pi] | Yaw setpoint that is being tracked (Applied slew rates) |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/RoverAttitudeStatus.msg)

::: details Click here to see original file

```c
# Rover Attitude Status

uint64 timestamp               # [us] Time since system start
float32 measured_yaw           # [rad] [@range -pi, pi] [@frame NED]Measured yaw
float32 adjusted_yaw_setpoint  # [rad] [@range -pi, pi] [@frame NED] Yaw setpoint that is being tracked (Applied slew rates)
```

:::
