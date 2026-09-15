---
title: "ActuatorMotors (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/ActuatorMotors"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/ActuatorMotors.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# ActuatorMotors (UORB message)

Motor control message.

Normalised thrust setpoint for up to 12 motors.
Published by the vehicle's allocation and consumed by the ESC protocol drivers e.g. PWM, DSHOT, UAVCAN.

**TOPICS:** actuator_motors

## Fields

| Name                                              | Type          | Unit [Frame] | Range/Enum | Description                                                                                                                                                            |
| ------------------------------------------------- | ------------- | ------------ | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <a id="fld_timestamp"></a>timestamp               | `uint64`      | us           |            | Time since system start                                                                                                                                                |
| <a id="fld_timestamp_sample"></a>timestamp_sample | `uint64`      | us           |            | Sampling timestamp of the data this control response is based on                                                                                                       |
| <a id="fld_reversible_flags"></a>reversible_flags | `uint16`      |              |            | Bitset indicating which motors are configured to be reversible                                                                                                         |
| <a id="fld_control"></a>control                   | `float32[12]` |              | [-1 : 1]   | Normalized thrust. Where 1 means maximum positive thrust, -1 maximum negative (if not supported by the output, <0 maps to NaN). NaN maps to disarmed (stop the motors) |

## Constants

| Name                                                            | Type     | Value | Description                       |
| --------------------------------------------------------------- | -------- | ----- | --------------------------------- |
| <a id="#MESSAGE_VERSION"></a> MESSAGE_VERSION                   | `uint32` | 0     |
| <a id="#ACTUATOR_FUNCTION_MOTOR1"></a> ACTUATOR_FUNCTION_MOTOR1 | `uint8`  | 101   | output_functions.yaml Motor.start |
| <a id="#NUM_CONTROLS"></a> NUM_CONTROLS                         | `uint8`  | 12    | output_functions.yaml Motor.count |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/versioned/ActuatorMotors.msg)

::: details Click here to see original file

```c
# Motor control message
#
# Normalised thrust setpoint for up to 12 motors.
# Published by the vehicle's allocation and consumed by the ESC protocol drivers e.g. PWM, DSHOT, UAVCAN.

uint32 MESSAGE_VERSION = 0

uint64 timestamp # [us] Time since system start
uint64 timestamp_sample # [us] Sampling timestamp of the data this control response is based on

uint16 reversible_flags # [-] Bitset indicating which motors are configured to be reversible

uint8 ACTUATOR_FUNCTION_MOTOR1 = 101 # output_functions.yaml Motor.start

uint8 NUM_CONTROLS = 12 # output_functions.yaml Motor.count
float32[12] control # [@range -1, 1] Normalized thrust. Where 1 means maximum positive thrust, -1 maximum negative (if not supported by the output, <0 maps to NaN). NaN maps to disarmed (stop the motors)
```

:::
