---
title: "DistanceSensorModeChangeRequest (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/DistanceSensorModeChangeRequest"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/DistanceSensorModeChangeRequest.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# DistanceSensorModeChangeRequest (UORB message)

**TOPICS:** distance_sensor_mode_change_request

## Fields

| Name                                          | Type     | Unit [Frame] | Range/Enum | Description                                   |
| --------------------------------------------- | -------- | ------------ | ---------- | --------------------------------------------- |
| <a id="fld_timestamp"></a>timestamp           | `uint64` |              |            | time since system start (microseconds)        |
| <a id="fld_request_on_off"></a>request_on_off | `uint8`  |              |            | request to disable/enable the distance sensor |

## Constants

| Name                                  | Type    | Value | Description |
| ------------------------------------- | ------- | ----- | ----------- |
| <a id="#REQUEST_OFF"></a> REQUEST_OFF | `uint8` | 0     |
| <a id="#REQUEST_ON"></a> REQUEST_ON   | `uint8` | 1     |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/DistanceSensorModeChangeRequest.msg)

::: details Click here to see original file

```c
uint64 timestamp		# time since system start (microseconds)

uint8 request_on_off 			# request to disable/enable the distance sensor
uint8 REQUEST_OFF = 0
uint8 REQUEST_ON  = 1
```

:::
