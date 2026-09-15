---
title: "PositionSetpointTriplet (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/PositionSetpointTriplet"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/PositionSetpointTriplet.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# PositionSetpointTriplet (UORB message)

Global position setpoint triplet in WGS84 coordinates. This are the three next waypoints (or just the next two or one).

**TOPICS:** position_setpoint_triplet

## Fields

| Name                                | Type               | Unit [Frame] | Range/Enum | Description                            |
| ----------------------------------- | ------------------ | ------------ | ---------- | -------------------------------------- |
| <a id="fld_timestamp"></a>timestamp | `uint64`           |              |            | time since system start (microseconds) |
| <a id="fld_previous"></a>previous   | `PositionSetpoint` |              |            |
| <a id="fld_current"></a>current     | `PositionSetpoint` |              |            |
| <a id="fld_next"></a>next           | `PositionSetpoint` |              |            |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/PositionSetpointTriplet.msg)

::: details Click here to see original file

```c
# Global position setpoint triplet in WGS84 coordinates.
# This are the three next waypoints (or just the next two or one).

uint64 timestamp		# time since system start (microseconds)

PositionSetpoint previous
PositionSetpoint current
PositionSetpoint next
```

:::
