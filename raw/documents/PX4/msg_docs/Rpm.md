---
title: "Rpm (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/Rpm"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/Rpm.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# Rpm (UORB message)

**TOPICS:** rpm

## Fields

| Name                                      | Type      | Unit [Frame] | Range/Enum | Description                            |
| ----------------------------------------- | --------- | ------------ | ---------- | -------------------------------------- |
| <a id="fld_timestamp"></a>timestamp       | `uint64`  |              |            | time since system start (microseconds) |
| <a id="fld_rpm_estimate"></a>rpm_estimate | `float32` |              |            | filtered revolutions per minute        |
| <a id="fld_rpm_raw"></a>rpm_raw           | `float32` |              |            |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/Rpm.msg)

::: details Click here to see original file

```c
uint64 timestamp # time since system start (microseconds)

# rpm values of 0.0 mean within a timeout there is no movement measured
float32 rpm_estimate # filtered revolutions per minute
float32 rpm_raw
```

:::
