---
title: "HoverThrustEstimate (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/HoverThrustEstimate"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/HoverThrustEstimate.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# HoverThrustEstimate (UORB message)

**TOPICS:** hover_thrust_estimate

## Fields

| Name                                                          | Type      | Unit [Frame] | Range/Enum | Description                                                             |
| ------------------------------------------------------------- | --------- | ------------ | ---------- | ----------------------------------------------------------------------- |
| <a id="fld_timestamp"></a>timestamp                           | `uint64`  |              |            | time since system start (microseconds)                                  |
| <a id="fld_timestamp_sample"></a>timestamp_sample             | `uint64`  |              |            | time of corresponding sensor data last used for this estimate           |
| <a id="fld_hover_thrust"></a>hover_thrust                     | `float32` |              |            | estimated hover thrust [0.1, 0.9]                                       |
| <a id="fld_hover_thrust_var"></a>hover_thrust_var             | `float32` |              |            | estimated hover thrust variance                                         |
| <a id="fld_accel_innov"></a>accel_innov                       | `float32` |              |            | innovation of the last acceleration fusion                              |
| <a id="fld_accel_innov_var"></a>accel_innov_var               | `float32` |              |            | innovation variance of the last acceleration fusion                     |
| <a id="fld_accel_innov_test_ratio"></a>accel_innov_test_ratio | `float32` |              |            | normalized innovation squared test ratio                                |
| <a id="fld_accel_noise_var"></a>accel_noise_var               | `float32` |              |            | vertical acceleration noise variance estimated form innovation residual |
| <a id="fld_valid"></a>valid                                   | `bool`    |              |            |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/HoverThrustEstimate.msg)

::: details Click here to see original file

```c
uint64 timestamp                # time since system start (microseconds)
uint64 timestamp_sample         # time of corresponding sensor data last used for this estimate

float32 hover_thrust		# estimated hover thrust [0.1, 0.9]
float32 hover_thrust_var	# estimated hover thrust variance

float32 accel_innov		# innovation of the last acceleration fusion
float32 accel_innov_var		# innovation variance of the last acceleration fusion
float32 accel_innov_test_ratio	# normalized innovation squared test ratio

float32 accel_noise_var		# vertical acceleration noise variance estimated form innovation residual

bool valid
```

:::
