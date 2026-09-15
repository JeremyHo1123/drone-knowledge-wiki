---
title: "PpsCapture (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/PpsCapture"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/PpsCapture.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# PpsCapture (UORB message)

**TOPICS:** pps_capture

## Fields

| Name                                        | Type     | Unit [Frame] | Range/Enum | Description                                                 |
| ------------------------------------------- | -------- | ------------ | ---------- | ----------------------------------------------------------- |
| <a id="fld_timestamp"></a>timestamp         | `uint64` |              |            | time since system start (microseconds) at PPS capture event |
| <a id="fld_rtc_timestamp"></a>rtc_timestamp | `uint64` |              |            | Corrected GPS UTC timestamp at PPS capture event            |
| <a id="fld_"></a>                           | `uint8`  |              |            | Increments when PPS dt < 50ms                               |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/PpsCapture.msg)

::: details Click here to see original file

```c
uint64 timestamp			  # time since system start (microseconds) at PPS capture event
uint64 rtc_timestamp		# Corrected GPS UTC timestamp at PPS capture event
uint8  pps_rate_exceeded_counter # Increments when PPS dt < 50ms
```

:::
