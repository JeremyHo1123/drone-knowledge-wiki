---
title: "ActuatorServosTrim (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/ActuatorServosTrim"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/ActuatorServosTrim.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# ActuatorServosTrim (UORB message)

Servo trims, added as offset to servo outputs.

**TOPICS:** actuator_servos_trim

## Fields

| Name                                | Type          | Unit [Frame] | Range/Enum | Description                            |
| ----------------------------------- | ------------- | ------------ | ---------- | -------------------------------------- |
| <a id="fld_timestamp"></a>timestamp | `uint64`      |              |            | time since system start (microseconds) |
| <a id="fld_trim"></a>trim           | `float32[15]` |              |            | range: [-1, 1]                         |

## Constants

| Name                                    | Type    | Value | Description |
| --------------------------------------- | ------- | ----- | ----------- |
| <a id="#NUM_CONTROLS"></a> NUM_CONTROLS | `uint8` | 15    |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/ActuatorServosTrim.msg)

::: details Click here to see original file

```c
# Servo trims, added as offset to servo outputs
uint64 timestamp			# time since system start (microseconds)

uint8 NUM_CONTROLS = 15
float32[15] trim    # range: [-1, 1]
```

:::
