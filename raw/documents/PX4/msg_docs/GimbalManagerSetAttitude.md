---
title: "GimbalManagerSetAttitude (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/GimbalManagerSetAttitude"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/GimbalManagerSetAttitude.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# GimbalManagerSetAttitude (UORB message)

**TOPICS:** gimbal_manager_set_attitude

## Fields

| Name                                                  | Type         | Unit [Frame] | Range/Enum | Description                            |
| ----------------------------------------------------- | ------------ | ------------ | ---------- | -------------------------------------- |
| <a id="fld_timestamp"></a>timestamp                   | `uint64`     |              |            | time since system start (microseconds) |
| <a id="fld_origin_sysid"></a>origin_sysid             | `uint8`      |              |            |
| <a id="fld_origin_compid"></a>origin_compid           | `uint8`      |              |            |
| <a id="fld_target_system"></a>target_system           | `uint8`      |              |            |
| <a id="fld_target_component"></a>target_component     | `uint8`      |              |            |
| <a id="fld_flags"></a>flags                           | `uint32`     |              |            |
| <a id="fld_gimbal_device_id"></a>gimbal_device_id     | `uint8`      |              |            |
| <a id="fld_q"></a>q                                   | `float32[4]` |              |            |
| <a id="fld_angular_velocity_x"></a>angular_velocity_x | `float32`    |              |            |
| <a id="fld_angular_velocity_y"></a>angular_velocity_y | `float32`    |              |            |
| <a id="fld_angular_velocity_z"></a>angular_velocity_z | `float32`    |              |            |

## Constants

| Name                                                                          | Type     | Value | Description |
| ----------------------------------------------------------------------------- | -------- | ----- | ----------- |
| <a id="#GIMBAL_MANAGER_FLAGS_RETRACT"></a> GIMBAL_MANAGER_FLAGS_RETRACT       | `uint32` | 1     |
| <a id="#GIMBAL_MANAGER_FLAGS_NEUTRAL"></a> GIMBAL_MANAGER_FLAGS_NEUTRAL       | `uint32` | 2     |
| <a id="#GIMBAL_MANAGER_FLAGS_ROLL_LOCK"></a> GIMBAL_MANAGER_FLAGS_ROLL_LOCK   | `uint32` | 4     |
| <a id="#GIMBAL_MANAGER_FLAGS_PITCH_LOCK"></a> GIMBAL_MANAGER_FLAGS_PITCH_LOCK | `uint32` | 8     |
| <a id="#GIMBAL_MANAGER_FLAGS_YAW_LOCK"></a> GIMBAL_MANAGER_FLAGS_YAW_LOCK     | `uint32` | 16    |
| <a id="#ORB_QUEUE_LENGTH"></a> ORB_QUEUE_LENGTH                               | `uint8`  | 2     |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/GimbalManagerSetAttitude.msg)

::: details Click here to see original file

```c
uint64 timestamp						# time since system start (microseconds)

uint8 origin_sysid
uint8 origin_compid

uint8 target_system
uint8 target_component

uint32 GIMBAL_MANAGER_FLAGS_RETRACT = 1
uint32 GIMBAL_MANAGER_FLAGS_NEUTRAL = 2
uint32 GIMBAL_MANAGER_FLAGS_ROLL_LOCK = 4
uint32 GIMBAL_MANAGER_FLAGS_PITCH_LOCK = 8
uint32 GIMBAL_MANAGER_FLAGS_YAW_LOCK = 16

uint32 flags
uint8 gimbal_device_id

float32[4] q

float32 angular_velocity_x
float32 angular_velocity_y
float32 angular_velocity_z

uint8 ORB_QUEUE_LENGTH = 2
```

:::
