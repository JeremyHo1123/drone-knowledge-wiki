---
title: "TiltrotorExtraControls (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/TiltrotorExtraControls"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/TiltrotorExtraControls.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# TiltrotorExtraControls (UORB message)

**TOPICS:** tiltrotor_extra_controls

## Fields

| Name                                                                                        | Type      | Unit [Frame] | Range/Enum | Description                                                                     |
| ------------------------------------------------------------------------------------------- | --------- | ------------ | ---------- | ------------------------------------------------------------------------------- |
| <a id="fld_timestamp"></a>timestamp                                                         | `uint64`  |              |            | time since system start (microseconds)                                          |
| <a id="fld_collective_tilt_normalized_setpoint"></a>collective_tilt_normalized_setpoint     | `float32` |              |            | Collective tilt angle of motors of tiltrotor, 0: vertical, 1: horizontal [0, 1] |
| <a id="fld_collective_thrust_normalized_setpoint"></a>collective_thrust_normalized_setpoint | `float32` |              |            | Collective thrust setpoint [0, 1]                                               |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/TiltrotorExtraControls.msg)

::: details Click here to see original file

```c
uint64 timestamp # time since system start (microseconds)

float32 collective_tilt_normalized_setpoint	# Collective tilt angle of motors of tiltrotor, 0: vertical, 1: horizontal [0, 1]
float32 collective_thrust_normalized_setpoint 	# Collective thrust setpoint [0, 1]
```

:::
