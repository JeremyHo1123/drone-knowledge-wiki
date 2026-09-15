---
title: "ActuatorOutputs (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/ActuatorOutputs"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/ActuatorOutputs.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# ActuatorOutputs (UORB message)

**TOPICS:** actuator_outputs actuator_outputs_sim actuator_outputs_debug

## Fields

| Name                                | Type          | Unit [Frame] | Range/Enum | Description                            |
| ----------------------------------- | ------------- | ------------ | ---------- | -------------------------------------- |
| <a id="fld_timestamp"></a>timestamp | `uint64`      |              |            | time since system start (microseconds) |
| <a id="fld_noutputs"></a>noutputs   | `uint32`      |              |            | valid outputs                          |
| <a id="fld_output"></a>output       | `float32[16]` |              |            | output data, in natural output units   |

## Constants

| Name                                                                | Type    | Value | Description         |
| ------------------------------------------------------------------- | ------- | ----- | ------------------- |
| <a id="#NUM_ACTUATOR_OUTPUTS"></a> NUM_ACTUATOR_OUTPUTS             | `uint8` | 16    |
| <a id="#NUM_ACTUATOR_OUTPUT_GROUPS"></a> NUM_ACTUATOR_OUTPUT_GROUPS | `uint8` | 4     | for sanity checking |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/ActuatorOutputs.msg)

::: details Click here to see original file

```c
uint64 timestamp				# time since system start (microseconds)
uint8 NUM_ACTUATOR_OUTPUTS		= 16
uint8 NUM_ACTUATOR_OUTPUT_GROUPS	= 4	# for sanity checking
uint32 noutputs				# valid outputs
float32[16] output				# output data, in natural output units

# actuator_outputs_sim is used for SITL, HITL & SIH (with an output range of [-1, 1])
# TOPICS actuator_outputs actuator_outputs_sim actuator_outputs_debug
```

:::
