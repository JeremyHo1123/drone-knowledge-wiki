---
title: "SensorSelection (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/SensorSelection"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/SensorSelection.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# SensorSelection (UORB message)

Sensor ID's for the voted sensors output on the sensor_combined topic. Will be updated on startup of the sensor module and when sensor selection changes.

**TOPICS:** sensor_selection

## Fields

| Name                                            | Type     | Unit [Frame] | Range/Enum | Description                                      |
| ----------------------------------------------- | -------- | ------------ | ---------- | ------------------------------------------------ |
| <a id="fld_timestamp"></a>timestamp             | `uint64` |              |            | time since system start (microseconds)           |
| <a id="fld_accel_device_id"></a>accel_device_id | `uint32` |              |            | unique device ID for the selected accelerometers |
| <a id="fld_gyro_device_id"></a>gyro_device_id   | `uint32` |              |            | unique device ID for the selected rate gyros     |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/SensorSelection.msg)

::: details Click here to see original file

```c
#
# Sensor ID's for the voted sensors output on the sensor_combined topic.
# Will be updated on startup of the sensor module and when sensor selection changes
#
uint64 timestamp		# time since system start (microseconds)
uint32 accel_device_id		# unique device ID for the selected accelerometers
uint32 gyro_device_id		# unique device ID for the selected rate gyros
```

:::
