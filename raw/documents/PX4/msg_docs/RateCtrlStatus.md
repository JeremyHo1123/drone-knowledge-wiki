---
title: "RateCtrlStatus (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/RateCtrlStatus"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/RateCtrlStatus.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# RateCtrlStatus (UORB message)

**TOPICS:** rate_ctrl_status

## Fields

| Name                                              | Type      | Unit [Frame] | Range/Enum | Description                            |
| ------------------------------------------------- | --------- | ------------ | ---------- | -------------------------------------- |
| <a id="fld_timestamp"></a>timestamp               | `uint64`  |              |            | time since system start (microseconds) |
| <a id="fld_rollspeed_integ"></a>rollspeed_integ   | `float32` |              |            |
| <a id="fld_pitchspeed_integ"></a>pitchspeed_integ | `float32` |              |            |
| <a id="fld_yawspeed_integ"></a>yawspeed_integ     | `float32` |              |            |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/RateCtrlStatus.msg)

::: details Click here to see original file

```c
uint64 timestamp		# time since system start (microseconds)

# rate controller integrator status
float32 rollspeed_integ
float32 pitchspeed_integ
float32 yawspeed_integ
```

:::
