---
title: "PositionControllerLandingStatus (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/PositionControllerLandingStatus"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/PositionControllerLandingStatus.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# PositionControllerLandingStatus (UORB message)

**TOPICS:** position_controller_landing_status

## Fields

| Name                                                              | Type      | Unit [Frame] | Range/Enum | Description                                                         |
| ----------------------------------------------------------------- | --------- | ------------ | ---------- | ------------------------------------------------------------------- |
| <a id="fld_timestamp"></a>timestamp                               | `uint64`  | us           |            | time since system start                                             |
| <a id="fld_lateral_touchdown_offset"></a>lateral_touchdown_offset | `float32` | m            |            | lateral touchdown position offset manually commanded during landing |
| <a id="fld_flaring"></a>flaring                                   | `bool`    |              |            | true if the aircraft is flaring                                     |
| <a id="fld_abort_status"></a>abort_status                         | `uint8`   |              |            |

## Constants

| Name                                                          | Type    | Value | Description           |
| ------------------------------------------------------------- | ------- | ----- | --------------------- |
| <a id="#NOT_ABORTED"></a> NOT_ABORTED                         | `uint8` | 0     |
| <a id="#ABORTED_BY_OPERATOR"></a> ABORTED_BY_OPERATOR         | `uint8` | 1     |
| <a id="#TERRAIN_NOT_FOUND"></a> TERRAIN_NOT_FOUND             | `uint8` | 2     | FW_LND_ABORT (1 << 0) |
| <a id="#TERRAIN_TIMEOUT"></a> TERRAIN_TIMEOUT                 | `uint8` | 3     | FW_LND_ABORT (1 << 1) |
| <a id="#UNKNOWN_ABORT_CRITERION"></a> UNKNOWN_ABORT_CRITERION | `uint8` | 4     |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/PositionControllerLandingStatus.msg)

::: details Click here to see original file

```c
uint64 timestamp # [us] time since system start
float32 lateral_touchdown_offset # [m] lateral touchdown position offset manually commanded during landing
bool flaring # true if the aircraft is flaring

# abort status is:
# 0 if not aborted
# >0 if aborted, with the singular abort criterion which triggered the landing abort enumerated by the following abort reasons
uint8 abort_status

# abort reasons
# after the manual operator abort, corresponds to individual bits of param FW_LND_ABORT
uint8 NOT_ABORTED = 0
uint8 ABORTED_BY_OPERATOR = 1
uint8 TERRAIN_NOT_FOUND = 2 # FW_LND_ABORT (1 << 0)
uint8 TERRAIN_TIMEOUT = 3 # FW_LND_ABORT (1 << 1)
uint8 UNKNOWN_ABORT_CRITERION = 4
```

:::
