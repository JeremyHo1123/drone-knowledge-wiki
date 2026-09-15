---
title: "GimbalControls (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/GimbalControls"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/GimbalControls.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# GimbalControls (UORB message)

**TOPICS:** gimbal_controls

## Fields

| Name                                              | Type         | Unit [Frame] | Range/Enum | Description                                                                                                                      |
| ------------------------------------------------- | ------------ | ------------ | ---------- | -------------------------------------------------------------------------------------------------------------------------------- |
| <a id="fld_timestamp"></a>timestamp               | `uint64`     |              |            | time since system start (microseconds)                                                                                           |
| <a id="fld_timestamp_sample"></a>timestamp_sample | `uint64`     |              |            | the timestamp the data this control response is based on was sampled                                                             |
| <a id="fld_control"></a>control                   | `float32[3]` |              |            | Normalized output. 1 means maximum positive position. -1 maximum negative position. 0 means no deflection. NaN maps to disarmed. |

## Constants

| Name                                  | Type    | Value | Description |
| ------------------------------------- | ------- | ----- | ----------- |
| <a id="#INDEX_ROLL"></a> INDEX_ROLL   | `uint8` | 0     |
| <a id="#INDEX_PITCH"></a> INDEX_PITCH | `uint8` | 1     |
| <a id="#INDEX_YAW"></a> INDEX_YAW     | `uint8` | 2     |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/GimbalControls.msg)

::: details Click here to see original file

```c
uint64 timestamp			# time since system start (microseconds)
uint8 INDEX_ROLL = 0
uint8 INDEX_PITCH = 1
uint8 INDEX_YAW = 2

uint64 timestamp_sample	    # the timestamp the data this control response is based on was sampled
float32[3] control	# Normalized output. 1 means maximum positive position. -1 maximum negative position. 0 means no deflection. NaN maps to disarmed.
```

:::
