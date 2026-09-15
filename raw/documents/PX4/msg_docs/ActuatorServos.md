---
title: "ActuatorServos (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/ActuatorServos"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/ActuatorServos.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# ActuatorServos (UORB message)

Servo control message.

Normalised output setpoint for up to 15 servos.
Published by the vehicle's allocation and consumed by the actuator output drivers.

**TOPICS:** actuator_servos

## Fields

| Name                                              | Type          | Unit [Frame] | Range/Enum | Description                                                                                                                                                |
| ------------------------------------------------- | ------------- | ------------ | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <a id="fld_timestamp"></a>timestamp               | `uint64`      | us           |            | Time since system start                                                                                                                                    |
| <a id="fld_timestamp_sample"></a>timestamp_sample | `uint64`      | us           |            | Sampling timestamp of the data this control response is based on                                                                                           |
| <a id="fld_control"></a>control                   | `float32[15]` |              | [-1 : 1]   | Normalized output. 1 means maximum positive position. -1 maximum negative position (if not supported by the output, <0 maps to NaN). NaN maps to disarmed. |

## Constants

| Name                                          | Type     | Value | Description |
| --------------------------------------------- | -------- | ----- | ----------- |
| <a id="#MESSAGE_VERSION"></a> MESSAGE_VERSION | `uint32` | 1     |
| <a id="#NUM_CONTROLS"></a> NUM_CONTROLS       | `uint8`  | 15    |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/versioned/ActuatorServos.msg)

::: details Click here to see original file

```c
# Servo control message
#
# Normalised output setpoint for up to 15 servos.
# Published by the vehicle's allocation and consumed by the actuator output drivers.

uint32 MESSAGE_VERSION = 1

uint64 timestamp # [us] Time since system start
uint64 timestamp_sample # [us] Sampling timestamp of the data this control response is based on

uint8 NUM_CONTROLS = 15
float32[15] control # [-] [@range -1, 1] Normalized output. 1 means maximum positive position. -1 maximum negative position (if not supported by the output, <0 maps to NaN). NaN maps to disarmed.
```

:::
