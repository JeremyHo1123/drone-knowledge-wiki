---
title: "HeaterStatus (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/HeaterStatus"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/HeaterStatus.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# HeaterStatus (UORB message)

**TOPICS:** heater_status

## Fields

| Name                                                                                      | Type      | Unit [Frame] | Range/Enum | Description                            |
| ----------------------------------------------------------------------------------------- | --------- | ------------ | ---------- | -------------------------------------- |
| <a id="fld_timestamp"></a>timestamp                                                       | `uint64`  |              |            | time since system start (microseconds) |
| <a id="fld_device_id"></a>device_id                                                       | `uint32`  |              |            |
| <a id="fld_heater_on"></a>heater_on                                                       | `bool`    |              |            |
| <a id="fld_temperature_target_met"></a>temperature_target_met                             | `bool`    |              |            |
| <a id="fld_temperature_activation_threshold_met"></a>temperature_activation_threshold_met | `bool`    |              |            |
| <a id="fld_temperature_sensor"></a>temperature_sensor                                     | `float32` |              |            |
| <a id="fld_temperature_target"></a>temperature_target                                     | `float32` |              |            |
| <a id="fld_controller_period_usec"></a>controller_period_usec                             | `uint32`  |              |            |
| <a id="fld_controller_time_on_usec"></a>controller_time_on_usec                           | `uint32`  |              |            |
| <a id="fld_proportional_value"></a>proportional_value                                     | `float32` |              |            |
| <a id="fld_integrator_value"></a>integrator_value                                         | `float32` |              |            |
| <a id="fld_feed_forward_value"></a>feed_forward_value                                     | `float32` |              |            |
| <a id="fld_supply_voltage"></a>supply_voltage                                             | `float32` |              |            | Supply voltage (V)                     |
| <a id="fld_heater_current"></a>heater_current                                             | `float32` |              |            | Heater current (A)                     |
| <a id="fld_nominal_multiplier"></a>nominal_multiplier                                     | `float32` |              |            |
| <a id="fld_mode"></a>mode                                                                 | `uint8`   |              |            |
| <a id="fld_temperature_source"></a>temperature_source                                     | `uint8`   |              |            |

## Constants

| Name                                                            | Type    | Value | Description |
| --------------------------------------------------------------- | ------- | ----- | ----------- |
| <a id="#MODE_GPIO"></a> MODE_GPIO                               | `uint8` | 1     |
| <a id="#MODE_PX4IO"></a> MODE_PX4IO                             | `uint8` | 2     |
| <a id="#TEMPERATURE_SOURCE_IMU"></a> TEMPERATURE_SOURCE_IMU     | `uint8` | 0     |
| <a id="#TEMPERATURE_SOURCE_HYGRO"></a> TEMPERATURE_SOURCE_HYGRO | `uint8` | 1     |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/HeaterStatus.msg)

::: details Click here to see original file

```c
uint64 timestamp	# time since system start (microseconds)

uint32 device_id

bool heater_on
bool temperature_target_met
bool temperature_activation_threshold_met

float32 temperature_sensor
float32 temperature_target

uint32 controller_period_usec
uint32 controller_time_on_usec

float32 proportional_value
float32 integrator_value
float32 feed_forward_value

float32 supply_voltage		# Supply voltage (V)
float32 heater_current		# Heater current (A)
float32 nominal_multiplier

uint8 MODE_GPIO  = 1
uint8 MODE_PX4IO = 2
uint8 mode

uint8 TEMPERATURE_SOURCE_IMU   = 0
uint8 TEMPERATURE_SOURCE_HYGRO = 1
uint8 temperature_source
```

:::
