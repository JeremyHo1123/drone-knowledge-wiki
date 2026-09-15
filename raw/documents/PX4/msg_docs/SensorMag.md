---
title: "SensorMag (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/SensorMag"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/SensorMag.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# SensorMag (UORB message)

**TOPICS:** sensor_mag

## Fields

| Name                                              | Type      | Unit [Frame] | Range/Enum | Description                                                               |
| ------------------------------------------------- | --------- | ------------ | ---------- | ------------------------------------------------------------------------- |
| <a id="fld_timestamp"></a>timestamp               | `uint64`  |              |            | time since system start (microseconds)                                    |
| <a id="fld_timestamp_sample"></a>timestamp_sample | `uint64`  |              |            |
| <a id="fld_device_id"></a>device_id               | `uint32`  |              |            | unique device ID for the sensor that does not change between power cycles |
| <a id="fld_x"></a>x                               | `float32` | Gauss        |            | magnetic field in the FRD board frame X-axis                              |
| <a id="fld_y"></a>y                               | `float32` | Gauss        |            | magnetic field in the FRD board frame Y-axis                              |
| <a id="fld_z"></a>z                               | `float32` | Gauss        |            | magnetic field in the FRD board frame Z-axis                              |
| <a id="fld_temperature"></a>temperature           | `float32` | °C           |            | Temperature.                                                              |
| <a id="fld_error_count"></a>error_count           | `uint32`  |              |            |

## Constants

| Name                                            | Type    | Value | Description |
| ----------------------------------------------- | ------- | ----- | ----------- |
| <a id="#ORB_QUEUE_LENGTH"></a> ORB_QUEUE_LENGTH | `uint8` | 4     |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/SensorMag.msg)

::: details Click here to see original file

```c
uint64 timestamp          # time since system start (microseconds)
uint64 timestamp_sample

uint32 device_id          # unique device ID for the sensor that does not change between power cycles

float32 x                 # [Gauss] magnetic field in the FRD board frame X-axis
float32 y                 # [Gauss] magnetic field in the FRD board frame Y-axis
float32 z                 # [Gauss] magnetic field in the FRD board frame Z-axis

float32 temperature       # [°C] Temperature.

uint32 error_count

uint8 ORB_QUEUE_LENGTH = 4
```

:::
