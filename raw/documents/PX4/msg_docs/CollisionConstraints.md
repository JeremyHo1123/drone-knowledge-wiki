---
title: "CollisionConstraints (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/CollisionConstraints"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/CollisionConstraints.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# CollisionConstraints (UORB message)

Local setpoint constraints in NED frame. setting something to NaN means that no limit is provided.

**TOPICS:** collision_constraints

## Fields

| Name                                                | Type         | Unit [Frame] | Range/Enum | Description                            |
| --------------------------------------------------- | ------------ | ------------ | ---------- | -------------------------------------- |
| <a id="fld_timestamp"></a>timestamp                 | `uint64`     |              |            | time since system start (microseconds) |
| <a id="fld_original_setpoint"></a>original_setpoint | `float32[2]` |              |            | velocities demanded                    |
| <a id="fld_adapted_setpoint"></a>adapted_setpoint   | `float32[2]` |              |            | velocities allowed                     |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/CollisionConstraints.msg)

::: details Click here to see original file

```c
# Local setpoint constraints in NED frame
# setting something to NaN means that no limit is provided

uint64 timestamp	# time since system start (microseconds)

float32[2] original_setpoint   # velocities demanded
float32[2] adapted_setpoint    # velocities allowed
```

:::
