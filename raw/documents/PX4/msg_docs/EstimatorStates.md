---
title: "EstimatorStates (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/EstimatorStates"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/EstimatorStates.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# EstimatorStates (UORB message)

**TOPICS:** estimator_states

## Fields

| Name                                              | Type          | Unit [Frame] | Range/Enum | Description                                  |
| ------------------------------------------------- | ------------- | ------------ | ---------- | -------------------------------------------- |
| <a id="fld_timestamp"></a>timestamp               | `uint64`      |              |            | time since system start (microseconds)       |
| <a id="fld_timestamp_sample"></a>timestamp_sample | `uint64`      |              |            | the timestamp of the raw data (microseconds) |
| <a id="fld_states"></a>states                     | `float32[25]` |              |            | Internal filter states                       |
| <a id="fld_n_states"></a>n_states                 | `uint8`       |              |            | Number of states effectively used            |
| <a id="fld_covariances"></a>covariances           | `float32[24]` |              |            | Diagonal Elements of Covariance Matrix       |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/EstimatorStates.msg)

::: details Click here to see original file

```c
uint64 timestamp		# time since system start (microseconds)
uint64 timestamp_sample         # the timestamp of the raw data (microseconds)

float32[25] states		# Internal filter states
uint8 n_states		# Number of states effectively used

float32[24] covariances	# Diagonal Elements of Covariance Matrix
```

:::
