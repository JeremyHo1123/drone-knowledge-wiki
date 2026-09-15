---
title: "EstimatorSelectorStatus (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/EstimatorSelectorStatus"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/EstimatorSelectorStatus.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# EstimatorSelectorStatus (UORB message)

**TOPICS:** estimator_selector_status

## Fields

| Name                                                            | Type         | Unit [Frame] | Range/Enum | Description                            |
| --------------------------------------------------------------- | ------------ | ------------ | ---------- | -------------------------------------- |
| <a id="fld_timestamp"></a>timestamp                             | `uint64`     |              |            | time since system start (microseconds) |
| <a id="fld_primary_instance"></a>primary_instance               | `uint8`      |              |            |
| <a id="fld_instances_available"></a>instances_available         | `uint8`      |              |            |
| <a id="fld_instance_changed_count"></a>instance_changed_count   | `uint32`     |              |            |
| <a id="fld_last_instance_change"></a>last_instance_change       | `uint64`     |              |            |
| <a id="fld_accel_device_id"></a>accel_device_id                 | `uint32`     |              |            |
| <a id="fld_baro_device_id"></a>baro_device_id                   | `uint32`     |              |            |
| <a id="fld_gyro_device_id"></a>gyro_device_id                   | `uint32`     |              |            |
| <a id="fld_mag_device_id"></a>mag_device_id                     | `uint32`     |              |            |
| <a id="fld_combined_test_ratio"></a>combined_test_ratio         | `float32[9]` |              |            |
| <a id="fld_relative_test_ratio"></a>relative_test_ratio         | `float32[9]` |              |            |
| <a id="fld_healthy"></a>healthy                                 | `bool[9]`    |              |            |
| <a id="fld_accumulated_gyro_error"></a>accumulated_gyro_error   | `float32[4]` |              |            |
| <a id="fld_accumulated_accel_error"></a>accumulated_accel_error | `float32[4]` |              |            |
| <a id="fld_gyro_fault_detected"></a>gyro_fault_detected         | `bool`       |              |            |
| <a id="fld_accel_fault_detected"></a>accel_fault_detected       | `bool`       |              |            |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/EstimatorSelectorStatus.msg)

::: details Click here to see original file

```c
uint64 timestamp		# time since system start (microseconds)

uint8 primary_instance

uint8 instances_available

uint32 instance_changed_count
uint64 last_instance_change

uint32 accel_device_id
uint32 baro_device_id
uint32 gyro_device_id
uint32 mag_device_id

float32[9] combined_test_ratio
float32[9] relative_test_ratio
bool[9] healthy

float32[4] accumulated_gyro_error
float32[4] accumulated_accel_error
bool gyro_fault_detected
bool accel_fault_detected
```

:::
