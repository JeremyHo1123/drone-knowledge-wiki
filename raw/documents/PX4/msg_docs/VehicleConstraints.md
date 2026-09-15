---
title: "VehicleConstraints (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/VehicleConstraints"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/VehicleConstraints.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# VehicleConstraints (UORB message)

Local setpoint constraints in NED frame. setting something to NaN means that no limit is provided.

**TOPICS:** vehicle_constraints

## Fields

| Name                                      | Type      | Unit [Frame] | Range/Enum | Description                                                                 |
| ----------------------------------------- | --------- | ------------ | ---------- | --------------------------------------------------------------------------- |
| <a id="fld_timestamp"></a>timestamp       | `uint64`  |              |            | time since system start (microseconds)                                      |
| <a id="fld_speed_up"></a>speed_up         | `float32` |              |            | in meters/sec                                                               |
| <a id="fld_speed_down"></a>speed_down     | `float32` |              |            | in meters/sec                                                               |
| <a id="fld_want_takeoff"></a>want_takeoff | `bool`    |              |            | tell the controller to initiate takeoff when idling (ignored during flight) |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/VehicleConstraints.msg)

::: details Click here to see original file

```c
# Local setpoint constraints in NED frame
# setting something to NaN means that no limit is provided

uint64 timestamp # time since system start (microseconds)

float32 speed_up # in meters/sec
float32 speed_down # in meters/sec

bool want_takeoff # tell the controller to initiate takeoff when idling (ignored during flight)
```

:::
