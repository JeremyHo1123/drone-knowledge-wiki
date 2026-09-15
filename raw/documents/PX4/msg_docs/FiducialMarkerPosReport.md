---
title: "FiducialMarkerPosReport (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/FiducialMarkerPosReport"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/FiducialMarkerPosReport.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# FiducialMarkerPosReport (UORB message)

Relative position of a precision-landing target detected by a vision pipeline (e.g. an ArUco marker).

Published by: vision pipelines (on-board or off-board over MAVLink TARGET_RELATIVE), decoded in mavlink_receiver.
Subscribed by: vision_target_estimator (VTEPosition).

The measurement is expressed in an arbitrary sensor frame; the quaternion q rotates it into the NED earth frame.

**TOPICS:** fiducial_marker_pos_report

## Fields

| Name                                              | Type         | Unit [Frame] | Range/Enum | Description                                                              |
| ------------------------------------------------- | ------------ | ------------ | ---------- | ------------------------------------------------------------------------ |
| <a id="fld_timestamp"></a>timestamp               | `uint64`     | us           |            | Time since system start                                                  |
| <a id="fld_timestamp_sample"></a>timestamp_sample | `uint64`     | us           |            | Timestamp of the raw observation                                         |
| <a id="fld_rel_pos"></a>rel_pos                   | `float32[3]` | m            |            | Target position relative to vehicle, expressed in the frame defined by q |
| <a id="fld_cov_rel_pos"></a>cov_rel_pos           | `float32[3]` | m^2          |            | Target position variance, expressed in the frame defined by q            |
| <a id="fld_q"></a>q                               | `float32[4]` |              |            | Quaternion rotation from the rel_pos frame to the NED earth frame        |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/FiducialMarkerPosReport.msg)

::: details Click here to see original file

```c
# Relative position of a precision-landing target detected by a vision pipeline (e.g. an ArUco marker).
#
# Published by: vision pipelines (on-board or off-board over MAVLink TARGET_RELATIVE), decoded in mavlink_receiver.
# Subscribed by: vision_target_estimator (VTEPosition).
#
# The measurement is expressed in an arbitrary sensor frame; the quaternion q rotates it into the NED earth frame.

uint64 timestamp # [us] Time since system start
uint64 timestamp_sample # [us] Timestamp of the raw observation

float32[3] rel_pos # [m] Target position relative to vehicle, expressed in the frame defined by q
float32[3] cov_rel_pos # [m^2] Target position variance, expressed in the frame defined by q

float32[4] q # [-] Quaternion rotation from the rel_pos frame to the NED earth frame
```

:::
