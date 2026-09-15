---
title: "RtlTimeEstimate (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/RtlTimeEstimate"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/RtlTimeEstimate.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# RtlTimeEstimate (UORB message)

**TOPICS:** rtl_time_estimate

## Fields

| Name                                                  | Type      | Unit [Frame] | Range/Enum | Description                                                                                   |
| ----------------------------------------------------- | --------- | ------------ | ---------- | --------------------------------------------------------------------------------------------- |
| <a id="fld_timestamp"></a>timestamp                   | `uint64`  |              |            | time since system start (microseconds)                                                        |
| <a id="fld_valid"></a>valid                           | `bool`    |              |            | Flag indicating whether the time estiamtes are valid                                          |
| <a id="fld_time_estimate"></a>time_estimate           | `float32` | s            |            | Estimated time for RTL                                                                        |
| <a id="fld_safe_time_estimate"></a>safe_time_estimate | `float32` | s            |            | Same as time_estimate, but with safety factor and safety margin included (factor\*t + margin) |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/RtlTimeEstimate.msg)

::: details Click here to see original file

```c
uint64 timestamp # time since system start (microseconds)

bool valid			# Flag indicating whether the time estiamtes are valid
float32 time_estimate		# [s] Estimated time for RTL
float32 safe_time_estimate	# [s] Same as time_estimate, but with safety factor and safety margin included (factor*t + margin)
```

:::
