---
title: "VteBiasInitStatus (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/VteBiasInitStatus"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/VteBiasInitStatus.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# VteBiasInitStatus (UORB message)

Diagnostics for the initial GNSS/vision bias averaging phase in the Vision Target Estimator.

Published by: vision_target_estimator (VTEPosition) while the bias low-pass filter is running.
Subscribed by: logger only, to verify that the bias settles before the estimator starts fusing vision.

**TOPICS:** vte_bias_init_status

## Fields

| Name                                        | Type         | Unit [Frame] | Range/Enum | Description                     |
| ------------------------------------------- | ------------ | ------------ | ---------- | ------------------------------- |
| <a id="fld_timestamp"></a>timestamp         | `uint64`     | us           |            | Time since system start         |
| <a id="fld_raw_bias"></a>raw_bias           | `float32[3]` | m [NED]      |            | Current GNSS-vision bias sample |
| <a id="fld_filtered_bias"></a>filtered_bias | `float32[3]` | m [NED]      |            | Low-pass filtered bias sample   |
| <a id="fld_delta_norm"></a>delta_norm       | `float32`    | m            |            | norm(raw_bias_k - raw_bias_k-1) |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/VteBiasInitStatus.msg)

::: details Click here to see original file

```c
# Diagnostics for the initial GNSS/vision bias averaging phase in the Vision Target Estimator.
#
# Published by: vision_target_estimator (VTEPosition) while the bias low-pass filter is running.
# Subscribed by: logger only, to verify that the bias settles before the estimator starts fusing vision.

uint64 timestamp # [us] Time since system start

float32[3] raw_bias # [m] [@frame NED] Current GNSS-vision bias sample
float32[3] filtered_bias # [m] [@frame NED] Low-pass filtered bias sample
float32 delta_norm # [m] norm(raw_bias_k - raw_bias_k-1)
```

:::
