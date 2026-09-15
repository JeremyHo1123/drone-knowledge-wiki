---
title: "ModeCompleted (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/ModeCompleted"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/ModeCompleted.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# ModeCompleted (UORB message)

Mode completion result, published by an active mode. The possible values of nav_state are defined in the VehicleStatus msg. Note that this is not always published (e.g. when a user switches modes or on. failsafe activation).

**TOPICS:** mode_completed

## Fields

| Name                                | Type     | Unit [Frame] | Range/Enum | Description                            |
| ----------------------------------- | -------- | ------------ | ---------- | -------------------------------------- |
| <a id="fld_timestamp"></a>timestamp | `uint64` |              |            | time since system start (microseconds) |
| <a id="fld_result"></a>result       | `uint8`  |              |            | One of RESULT\_\*                      |
| <a id="fld_nav_state"></a>nav_state | `uint8`  |              |            | Source mode (values in VehicleStatus)  |

## Constants

| Name                                                    | Type     | Value | Description                 |
| ------------------------------------------------------- | -------- | ----- | --------------------------- |
| <a id="#MESSAGE_VERSION"></a> MESSAGE_VERSION           | `uint32` | 0     |
| <a id="#RESULT_SUCCESS"></a> RESULT_SUCCESS             | `uint8`  | 0     |
| <a id="#RESULT_FAILURE_OTHER"></a> RESULT_FAILURE_OTHER | `uint8`  | 100   | Mode failed (generic error) |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/versioned/ModeCompleted.msg)

::: details Click here to see original file

```c
# Mode completion result, published by an active mode.
# The possible values of nav_state are defined in the VehicleStatus msg.
# Note that this is not always published (e.g. when a user switches modes or on
# failsafe activation)

uint32 MESSAGE_VERSION = 0

uint64 timestamp				 # time since system start (microseconds)


uint8 RESULT_SUCCESS = 0
# [1-99]: reserved
uint8 RESULT_FAILURE_OTHER = 100 # Mode failed (generic error)

uint8 result                     # One of RESULT_*

uint8 nav_state                  # Source mode (values in VehicleStatus)
```

:::
