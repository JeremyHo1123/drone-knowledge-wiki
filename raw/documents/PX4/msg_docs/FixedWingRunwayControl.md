---
title: "FixedWingRunwayControl (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/FixedWingRunwayControl"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/FixedWingRunwayControl.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# FixedWingRunwayControl (UORB message)

Auxiliary control fields for fixed-wing runway takeoff/landing.

**TOPICS:** fixed_wing_runway_control

## Fields

| Name                                                                    | Type      | Unit [Frame] | Range/Enum | Description                                                                |
| ----------------------------------------------------------------------- | --------- | ------------ | ---------- | -------------------------------------------------------------------------- |
| <a id="fld_timestamp"></a>timestamp                                     | `uint64`  | us           |            | time since system start                                                    |
| <a id="fld_runway_takeoff_state"></a>runway_takeoff_state               | `uint8`   |              |            | Current state of runway takeoff state machine                              |
| <a id="fld_wheel_steering_enabled"></a>wheel_steering_enabled           | `bool`    |              |            | Flag that enables the wheel steering.                                      |
| <a id="fld_wheel_steering_nudging_rate"></a>wheel_steering_nudging_rate | `float32` | FRD          | [-1 : 1]   | Manual wheel nudging, added to controller output. NAN is interpreted as 0. |

## Constants

| Name                                                          | Type    | Value | Description                                                   |
| ------------------------------------------------------------- | ------- | ----- | ------------------------------------------------------------- |
| <a id="#STATE_THROTTLE_RAMP"></a> STATE_THROTTLE_RAMP         | `uint8` | 0     | ramping up throttle                                           |
| <a id="#STATE_CLAMPED_TO_RUNWAY"></a> STATE_CLAMPED_TO_RUNWAY | `uint8` | 1     | clamped to runway, controlling yaw directly (wheel or rudder) |
| <a id="#STATE_CLIMBOUT"></a> STATE_CLIMBOUT                   | `uint8` | 2     | climbout to safe height before navigation                     |
| <a id="#STATE_FLYING"></a> STATE_FLYING                       | `uint8` | 3     | navigate freely                                               |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/FixedWingRunwayControl.msg)

::: details Click here to see original file

```c
# Auxiliary control fields for fixed-wing runway takeoff/landing

# Passes information from the FixedWingModeManager to the FixedWingAttitudeController (wheel control) and FixedWingLandDetector (takeoff state)

uint64 timestamp # [us] time since system start

uint8 STATE_THROTTLE_RAMP = 0		# ramping up throttle
uint8 STATE_CLAMPED_TO_RUNWAY = 1	# clamped to runway, controlling yaw directly (wheel or rudder)
uint8 STATE_CLIMBOUT = 2		# climbout to safe height before navigation
uint8 STATE_FLYING = 3			# navigate freely

uint8 runway_takeoff_state		# Current state of runway takeoff state machine

bool wheel_steering_enabled		# Flag that enables the wheel steering.
float32 wheel_steering_nudging_rate	# [norm] [@range -1, 1] [FRD] Manual wheel nudging, added to controller output. NAN is interpreted as 0.
```

:::
