---
title: "EstimatorAidSource3d (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/EstimatorAidSource3d"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/EstimatorAidSource3d.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# EstimatorAidSource3d (UORB message)

**TOPICS:** estimator_aid_src_ev_vel estimator_aid_src_gnss_vel estimator_aid_src_gravity estimator_aid_src_mag

## Fields

| Name                                                      | Type         | Unit [Frame] | Range/Enum | Description                                  |
| --------------------------------------------------------- | ------------ | ------------ | ---------- | -------------------------------------------- |
| <a id="fld_timestamp"></a>timestamp                       | `uint64`     |              |            | time since system start (microseconds)       |
| <a id="fld_timestamp_sample"></a>timestamp_sample         | `uint64`     |              |            | the timestamp of the raw data (microseconds) |
| <a id="fld_estimator_instance"></a>estimator_instance     | `uint8`      |              |            |
| <a id="fld_device_id"></a>device_id                       | `uint32`     |              |            |
| <a id="fld_time_last_fuse"></a>time_last_fuse             | `uint64`     |              |            |
| <a id="fld_observation"></a>observation                   | `float32[3]` |              |            |
| <a id="fld_observation_variance"></a>observation_variance | `float32[3]` |              |            |
| <a id="fld_innovation"></a>innovation                     | `float32[3]` |              |            |
| <a id="fld_innovation_filtered"></a>innovation_filtered   | `float32[3]` |              |            |
| <a id="fld_innovation_variance"></a>innovation_variance   | `float32[3]` |              |            |
| <a id="fld_test_ratio"></a>test_ratio                     | `float32[3]` |              |            | normalized innovation squared                |
| <a id="fld_test_ratio_filtered"></a>test_ratio_filtered   | `float32[3]` |              |            | signed filtered test ratio                   |
| <a id="fld_innovation_rejected"></a>innovation_rejected   | `bool`       |              |            | true if the observation has been rejected    |
| <a id="fld_fused"></a>fused                               | `bool`       |              |            | true if the sample was successfully fused    |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/EstimatorAidSource3d.msg)

::: details Click here to see original file

```c
uint64 timestamp                # time since system start (microseconds)
uint64 timestamp_sample         # the timestamp of the raw data (microseconds)

uint8 estimator_instance

uint32 device_id

uint64 time_last_fuse

float32[3] observation
float32[3] observation_variance

float32[3] innovation
float32[3] innovation_filtered

float32[3] innovation_variance

float32[3] test_ratio           # normalized innovation squared
float32[3] test_ratio_filtered  # signed filtered test ratio

bool innovation_rejected        # true if the observation has been rejected
bool fused                      # true if the sample was successfully fused

# TOPICS estimator_aid_src_ev_vel estimator_aid_src_gnss_vel estimator_aid_src_gravity estimator_aid_src_mag
```

:::
