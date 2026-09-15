---
title: "NavigatorStatus (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/NavigatorStatus"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/NavigatorStatus.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# NavigatorStatus (UORB message)

Current status of a Navigator mode. The possible values of nav_state are defined in the VehicleStatus msg.

**TOPICS:** navigator_status

## Fields

| Name                                | Type     | Unit [Frame] | Range/Enum | Description                            |
| ----------------------------------- | -------- | ------------ | ---------- | -------------------------------------- |
| <a id="fld_timestamp"></a>timestamp | `uint64` |              |            | time since system start (microseconds) |
| <a id="fld_nav_state"></a>nav_state | `uint8`  |              |            | Source mode (values in VehicleStatus)  |
| <a id="fld_failure"></a>failure     | `uint8`  |              |            | Navigator failure enum                 |

## Constants

| Name                                    | Type    | Value | Description                                         |
| --------------------------------------- | ------- | ----- | --------------------------------------------------- |
| <a id="#FAILURE_NONE"></a> FAILURE_NONE | `uint8` | 0     |
| <a id="#FAILURE_HAGL"></a> FAILURE_HAGL | `uint8` | 1     | Target altitude exceeds maximum height above ground |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/NavigatorStatus.msg)

::: details Click here to see original file

```c
# Current status of a Navigator mode
# The possible values of nav_state are defined in the VehicleStatus msg.
uint64 timestamp  # time since system start (microseconds)

uint8 nav_state   # Source mode (values in VehicleStatus)
uint8 failure     # Navigator failure enum

uint8 FAILURE_NONE = 0
uint8 FAILURE_HAGL = 1 # Target altitude exceeds maximum height above ground
```

:::
