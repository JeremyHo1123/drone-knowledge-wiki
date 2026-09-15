---
title: "ActuatorControlsStatus (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/ActuatorControlsStatus"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/ActuatorControlsStatus.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# ActuatorControlsStatus (UORB message)

**TOPICS:** actuator_controls_status_0 actuator_controls_status_1

## Fields

| Name                                        | Type         | Unit [Frame] | Range/Enum | Description                            |
| ------------------------------------------- | ------------ | ------------ | ---------- | -------------------------------------- |
| <a id="fld_timestamp"></a>timestamp         | `uint64`     |              |            | time since system start (microseconds) |
| <a id="fld_control_power"></a>control_power | `float32[3]` |              |            |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/ActuatorControlsStatus.msg)

::: details Click here to see original file

```c
uint64 timestamp			# time since system start (microseconds)

float32[3] control_power

# TOPICS actuator_controls_status_0 actuator_controls_status_1
```

:::
