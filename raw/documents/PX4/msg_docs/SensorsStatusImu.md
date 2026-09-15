---
title: "SensorsStatusImu (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/SensorsStatusImu"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/SensorsStatusImu.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# SensorsStatusImu (UORB message)

Sensor check metrics. This will be zero for a sensor that's primary or unpopulated.

**TOPICS:** sensors_status_imu

## Fields

| Name                                                                | Type         | Unit [Frame] | Range/Enum | Description                                                                    |
| ------------------------------------------------------------------- | ------------ | ------------ | ---------- | ------------------------------------------------------------------------------ |
| <a id="fld_timestamp"></a>timestamp                                 | `uint64`     |              |            | time since system start (microseconds)                                         |
| <a id="fld_accel_device_id_primary"></a>accel_device_id_primary     | `uint32`     |              |            | current primary accel device id for reference                                  |
| <a id="fld_accel_device_ids"></a>accel_device_ids                   | `uint32[4]`  |              |            |
| <a id="fld_accel_inconsistency_m_s_s"></a>accel_inconsistency_m_s_s | `float32[4]` |              |            | magnitude of acceleration difference between IMU instance and mean in m/s^2.   |
| <a id="fld_accel_healthy"></a>accel_healthy                         | `bool[4]`    |              |            |
| <a id="fld_accel_priority"></a>accel_priority                       | `uint8[4]`   |              |            |
| <a id="fld_gyro_device_id_primary"></a>gyro_device_id_primary       | `uint32`     |              |            | current primary gyro device id for reference                                   |
| <a id="fld_gyro_device_ids"></a>gyro_device_ids                     | `uint32[4]`  |              |            |
| <a id="fld_gyro_inconsistency_rad_s"></a>gyro_inconsistency_rad_s   | `float32[4]` |              |            | magnitude of angular rate difference between IMU instance and mean in (rad/s). |
| <a id="fld_gyro_healthy"></a>gyro_healthy                           | `bool[4]`    |              |            |
| <a id="fld_gyro_priority"></a>gyro_priority                         | `uint8[4]`   |              |            |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/SensorsStatusImu.msg)

::: details Click here to see original file

```c
#
# Sensor check metrics. This will be zero for a sensor that's primary or unpopulated.
#
uint64 timestamp # time since system start (microseconds)

uint32 accel_device_id_primary       # current primary accel device id for reference

uint32[4] accel_device_ids
float32[4] accel_inconsistency_m_s_s # magnitude of acceleration difference between IMU instance and mean in m/s^2.
bool[4] accel_healthy
uint8[4] accel_priority

uint32 gyro_device_id_primary       # current primary gyro device id for reference

uint32[4] gyro_device_ids
float32[4] gyro_inconsistency_rad_s # magnitude of angular rate difference between IMU instance and mean in (rad/s).
bool[4] gyro_healthy
uint8[4] gyro_priority
```

:::
