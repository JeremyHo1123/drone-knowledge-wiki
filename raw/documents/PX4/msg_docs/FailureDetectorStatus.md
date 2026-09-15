---
title: "FailureDetectorStatus (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/FailureDetectorStatus"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/FailureDetectorStatus.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# FailureDetectorStatus (UORB message)

**TOPICS:** failure_detector_status

## Fields

| Name                                                          | Type      | Unit [Frame] | Range/Enum | Description                                                     |
| ------------------------------------------------------------- | --------- | ------------ | ---------- | --------------------------------------------------------------- |
| <a id="fld_timestamp"></a>timestamp                           | `uint64`  |              |            | time since system start (microseconds)                          |
| <a id="fld_fd_roll"></a>fd_roll                               | `bool`    |              |            |
| <a id="fld_fd_pitch"></a>fd_pitch                             | `bool`    |              |            |
| <a id="fld_fd_alt"></a>fd_alt                                 | `bool`    |              |            |
| <a id="fld_fd_ext"></a>fd_ext                                 | `bool`    |              |            |
| <a id="fld_fd_arm_escs"></a>fd_arm_escs                       | `bool`    |              |            |
| <a id="fld_fd_battery"></a>fd_battery                         | `bool`    |              |            |
| <a id="fld_fd_imbalanced_prop"></a>fd_imbalanced_prop         | `bool`    |              |            |
| <a id="fld_fd_motor"></a>fd_motor                             | `bool`    |              |            |
| <a id="fld_imbalanced_prop_metric"></a>imbalanced_prop_metric | `float32` |              |            | Metric of the imbalanced propeller check (low-passed)           |
| <a id="fld_motor_failure_mask"></a>motor_failure_mask         | `uint16`  |              |            | Bit-mask with motor indices, indicating critical motor failures |
| <a id="fld_motor_stop_mask"></a>motor_stop_mask               | `uint16`  |              |            | Bitmaks of motors stopped by failure injection                  |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/FailureDetectorStatus.msg)

::: details Click here to see original file

```c
uint64 timestamp                    # time since system start (microseconds)

# FailureDetector status
bool fd_roll
bool fd_pitch
bool fd_alt
bool fd_ext
bool fd_arm_escs
bool fd_battery
bool fd_imbalanced_prop
bool fd_motor

float32 imbalanced_prop_metric      # Metric of the imbalanced propeller check (low-passed)
uint16 motor_failure_mask           # Bit-mask with motor indices, indicating critical motor failures
uint16 motor_stop_mask              # Bitmaks of motors stopped by failure injection
```

:::
