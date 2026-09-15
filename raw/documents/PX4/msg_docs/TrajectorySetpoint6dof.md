---
title: "TrajectorySetpoint6dof (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/TrajectorySetpoint6dof"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/TrajectorySetpoint6dof.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# TrajectorySetpoint6dof (UORB message)

Trajectory setpoint in NED frame. Input to position controller.

**TOPICS:** trajectory_setpoint6dof

## Fields

| Name                                              | Type         | Unit [Frame] | Range/Enum | Description                            |
| ------------------------------------------------- | ------------ | ------------ | ---------- | -------------------------------------- |
| <a id="fld_timestamp"></a>timestamp               | `uint64`     |              |            | time since system start (microseconds) |
| <a id="fld_position"></a>position                 | `float32[3]` |              |            | in meters                              |
| <a id="fld_velocity"></a>velocity                 | `float32[3]` |              |            | in meters/second                       |
| <a id="fld_acceleration"></a>acceleration         | `float32[3]` |              |            | in meters/second^2                     |
| <a id="fld_jerk"></a>jerk                         | `float32[3]` |              |            | in meters/second^3 (for logging only)  |
| <a id="fld_quaternion"></a>quaternion             | `float32[4]` |              |            | unit quaternion                        |
| <a id="fld_angular_velocity"></a>angular_velocity | `float32[3]` |              |            | angular velocity in radians/second     |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/TrajectorySetpoint6dof.msg)

::: details Click here to see original file

```c
# Trajectory setpoint in NED frame
# Input to position controller.

uint64 timestamp # time since system start (microseconds)

# NED local world frame
float32[3] position               # in meters
float32[3] velocity               # in meters/second
float32[3] acceleration           # in meters/second^2
float32[3] jerk                   # in meters/second^3 (for logging only)

float32[4] quaternion             # unit quaternion
float32[3] angular_velocity       # angular velocity in radians/second
```

:::
