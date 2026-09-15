---
title: "EstimatorBias (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/EstimatorBias"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/EstimatorBias.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# EstimatorBias (UORB message)

**TOPICS:** estimator_baro_bias estimator_gnss_hgt_bias

## Fields

| Name                                              | Type      | Unit [Frame] | Range/Enum | Description                                                               |
| ------------------------------------------------- | --------- | ------------ | ---------- | ------------------------------------------------------------------------- |
| <a id="fld_timestamp"></a>timestamp               | `uint64`  |              |            | time since system start (microseconds)                                    |
| <a id="fld_timestamp_sample"></a>timestamp_sample | `uint64`  |              |            | the timestamp of the raw data (microseconds)                              |
| <a id="fld_device_id"></a>device_id               | `uint32`  |              |            | unique device ID for the sensor that does not change between power cycles |
| <a id="fld_bias"></a>bias                         | `float32` |              |            | estimated barometric altitude bias (m)                                    |
| <a id="fld_bias_var"></a>bias_var                 | `float32` |              |            | estimated barometric altitude bias variance (m^2)                         |
| <a id="fld_innov"></a>innov                       | `float32` |              |            | innovation of the last measurement fusion (m)                             |
| <a id="fld_innov_var"></a>innov_var               | `float32` |              |            | innovation variance of the last measurement fusion (m^2)                  |
| <a id="fld_innov_test_ratio"></a>innov_test_ratio | `float32` |              |            | normalized innovation squared test ratio                                  |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/EstimatorBias.msg)

::: details Click here to see original file

```c
uint64 timestamp                # time since system start (microseconds)
uint64 timestamp_sample         # the timestamp of the raw data (microseconds)

uint32 device_id		# unique device ID for the sensor that does not change between power cycles
float32 bias			# estimated barometric altitude bias (m)
float32 bias_var		# estimated barometric altitude bias variance (m^2)

float32 innov			# innovation of the last measurement fusion (m)
float32 innov_var		# innovation variance of the last measurement fusion (m^2)
float32 innov_test_ratio	# normalized innovation squared test ratio

# TOPICS estimator_baro_bias estimator_gnss_hgt_bias
```

:::
