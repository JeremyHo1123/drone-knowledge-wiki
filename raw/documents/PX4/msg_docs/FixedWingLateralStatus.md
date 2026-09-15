---
title: "FixedWingLateralStatus (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/FixedWingLateralStatus"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/FixedWingLateralStatus.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# FixedWingLateralStatus (UORB message)

Fixed Wing Lateral Status message. Published by the fw_lateral_longitudinal_control module to report the resultant lateral setpoint.

**TOPICS:** fixed_wing_lateral_status

## Fields

| Name                                                                        | Type      | Unit [Frame] | Range/Enum | Description                                                                  |
| --------------------------------------------------------------------------- | --------- | ------------ | ---------- | ---------------------------------------------------------------------------- |
| <a id="fld_timestamp"></a>timestamp                                         | `uint64`  |              |            | time since system start (microseconds)                                       |
| <a id="fld_lateral_acceleration_setpoint"></a>lateral_acceleration_setpoint | `float32` | FRD          |            | resultant lateral acceleration setpoint                                      |
| <a id="fld_can_run_factor"></a>can_run_factor                               | `float32` | norm         | [0 : 1]    | estimate of certainty of the correct functionality of the npfg roll setpoint |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/FixedWingLateralStatus.msg)

::: details Click here to see original file

```c
# Fixed Wing Lateral Status message
# Published by the fw_lateral_longitudinal_control module to report the resultant lateral setpoint

uint64 timestamp                         # time since system start (microseconds)

float32 lateral_acceleration_setpoint    # [m/s^2] [FRD] resultant lateral acceleration setpoint
float32 can_run_factor 	 	         # [norm] [@range 0, 1] estimate of certainty of the correct functionality of the npfg roll setpoint
```

:::
