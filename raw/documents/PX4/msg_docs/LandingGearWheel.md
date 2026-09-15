---
title: "LandingGearWheel (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/LandingGearWheel"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/LandingGearWheel.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# LandingGearWheel (UORB message)

**TOPICS:** landing_gear_wheel

## Fields

| Name                                                                | Type      | Unit [Frame] | Range/Enum | Description                                              |
| ------------------------------------------------------------------- | --------- | ------------ | ---------- | -------------------------------------------------------- |
| <a id="fld_timestamp"></a>timestamp                                 | `uint64`  |              |            | time since system start (microseconds)                   |
| <a id="fld_normalized_wheel_setpoint"></a>normalized_wheel_setpoint | `float32` |              |            | negative is turning left, positive turning right [-1, 1] |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/LandingGearWheel.msg)

::: details Click here to see original file

```c
uint64 timestamp # time since system start (microseconds)

float32 normalized_wheel_setpoint	# negative is turning left, positive turning right [-1, 1]
```

:::
