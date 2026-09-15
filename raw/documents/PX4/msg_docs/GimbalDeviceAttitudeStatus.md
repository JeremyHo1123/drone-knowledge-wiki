---
title: "GimbalDeviceAttitudeStatus (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/GimbalDeviceAttitudeStatus"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/GimbalDeviceAttitudeStatus.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# GimbalDeviceAttitudeStatus (UORB message)

**TOPICS:** gimbal_device_attitude_status

## Fields

| Name                                                        | Type         | Unit [Frame] | Range/Enum | Description                            |
| ----------------------------------------------------------- | ------------ | ------------ | ---------- | -------------------------------------- |
| <a id="fld_timestamp"></a>timestamp                         | `uint64`     |              |            | time since system start (microseconds) |
| <a id="fld_target_system"></a>target_system                 | `uint8`      |              |            |
| <a id="fld_target_component"></a>target_component           | `uint8`      |              |            |
| <a id="fld_device_flags"></a>device_flags                   | `uint16`     |              |            |
| <a id="fld_q"></a>q                                         | `float32[4]` |              |            |
| <a id="fld_angular_velocity_x"></a>angular_velocity_x       | `float32`    |              |            |
| <a id="fld_angular_velocity_y"></a>angular_velocity_y       | `float32`    |              |            |
| <a id="fld_angular_velocity_z"></a>angular_velocity_z       | `float32`    |              |            |
| <a id="fld_failure_flags"></a>failure_flags                 | `uint32`     |              |            |
| <a id="fld_delta_yaw"></a>delta_yaw                         | `float32`    |              |            |
| <a id="fld_delta_yaw_velocity"></a>delta_yaw_velocity       | `float32`    |              |            |
| <a id="fld_gimbal_device_id"></a>gimbal_device_id           | `uint8`      |              |            |
| <a id="fld_received_from_mavlink"></a>received_from_mavlink | `bool`       |              |            |

## Constants

| Name                                                                              | Type     | Value | Description |
| --------------------------------------------------------------------------------- | -------- | ----- | ----------- |
| <a id="#DEVICE_FLAGS_RETRACT"></a> DEVICE_FLAGS_RETRACT                           | `uint16` | 1     |
| <a id="#DEVICE_FLAGS_NEUTRAL"></a> DEVICE_FLAGS_NEUTRAL                           | `uint16` | 2     |
| <a id="#DEVICE_FLAGS_ROLL_LOCK"></a> DEVICE_FLAGS_ROLL_LOCK                       | `uint16` | 4     |
| <a id="#DEVICE_FLAGS_PITCH_LOCK"></a> DEVICE_FLAGS_PITCH_LOCK                     | `uint16` | 8     |
| <a id="#DEVICE_FLAGS_YAW_LOCK"></a> DEVICE_FLAGS_YAW_LOCK                         | `uint16` | 16    |
| <a id="#DEVICE_FLAGS_YAW_IN_VEHICLE_FRAME"></a> DEVICE_FLAGS_YAW_IN_VEHICLE_FRAME | `uint16` | 32    |
| <a id="#DEVICE_FLAGS_YAW_IN_EARTH_FRAME"></a> DEVICE_FLAGS_YAW_IN_EARTH_FRAME     | `uint16` | 64    |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/GimbalDeviceAttitudeStatus.msg)

::: details Click here to see original file

```c
uint64 timestamp						# time since system start (microseconds)

uint8 target_system
uint8 target_component
uint16 device_flags

uint16 DEVICE_FLAGS_RETRACT = 1
uint16 DEVICE_FLAGS_NEUTRAL = 2
uint16 DEVICE_FLAGS_ROLL_LOCK = 4
uint16 DEVICE_FLAGS_PITCH_LOCK = 8
uint16 DEVICE_FLAGS_YAW_LOCK = 16
uint16 DEVICE_FLAGS_YAW_IN_VEHICLE_FRAME = 32
uint16 DEVICE_FLAGS_YAW_IN_EARTH_FRAME = 64


float32[4] q
float32 angular_velocity_x
float32 angular_velocity_y
float32 angular_velocity_z

uint32 failure_flags
float32 delta_yaw
float32 delta_yaw_velocity
uint8 gimbal_device_id

bool received_from_mavlink
```

:::
