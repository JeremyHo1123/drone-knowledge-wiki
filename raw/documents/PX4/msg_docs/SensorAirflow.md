---
title: "SensorAirflow (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/SensorAirflow"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/SensorAirflow.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# SensorAirflow (UORB message)

**TOPICS:** sensor_airflow

## Fields

| Name                                | Type      | Unit [Frame] | Range/Enum | Description                                                               |
| ----------------------------------- | --------- | ------------ | ---------- | ------------------------------------------------------------------------- |
| <a id="fld_timestamp"></a>timestamp | `uint64`  |              |            | time since system start (microseconds)                                    |
| <a id="fld_device_id"></a>device_id | `uint32`  |              |            | unique device ID for the sensor that does not change between power cycles |
| <a id="fld_speed"></a>speed         | `float32` |              |            | the speed being reported by the wind / airflow sensor                     |
| <a id="fld_direction"></a>direction | `float32` |              |            | the direction being reported by the wind / airflow sensor                 |
| <a id="fld_status"></a>status       | `uint8`   |              |            | Status code from the sensor                                               |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/SensorAirflow.msg)

::: details Click here to see original file

```c
uint64 timestamp		# time since system start (microseconds)
uint32 device_id                # unique device ID for the sensor that does not change between power cycles
float32 speed			# the speed being reported by the wind / airflow sensor
float32 direction		# the direction being reported by the wind / airflow sensor
uint8 status			# Status code from the sensor
```

:::
