---
title: "FollowTarget (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/FollowTarget"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/FollowTarget.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# FollowTarget (UORB message)

**TOPICS:** follow_target

## Fields

| Name                                | Type      | Unit [Frame] | Range/Enum | Description                            |
| ----------------------------------- | --------- | ------------ | ---------- | -------------------------------------- |
| <a id="fld_timestamp"></a>timestamp | `uint64`  |              |            | time since system start (microseconds) |
| <a id="fld_lat"></a>lat             | `float64` |              |            | target position (deg \* 1e7)           |
| <a id="fld_lon"></a>lon             | `float64` |              |            | target position (deg \* 1e7)           |
| <a id="fld_alt"></a>alt             | `float32` |              |            | target position                        |
| <a id="fld_vy"></a>vy               | `float32` |              |            | target vel in y                        |
| <a id="fld_vx"></a>vx               | `float32` |              |            | target vel in x                        |
| <a id="fld_vz"></a>vz               | `float32` |              |            | target vel in z                        |
| <a id="fld_est_cap"></a>est_cap     | `uint8`   |              |            | target reporting capabilities          |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/FollowTarget.msg)

::: details Click here to see original file

```c
uint64 timestamp  # time since system start (microseconds)

float64 lat       # target position (deg * 1e7)
float64 lon       # target position (deg * 1e7)
float32 alt       # target position

float32 vy        # target vel in y
float32 vx        # target vel in x
float32 vz        # target vel in z

uint8 est_cap     # target reporting capabilities
```

:::
