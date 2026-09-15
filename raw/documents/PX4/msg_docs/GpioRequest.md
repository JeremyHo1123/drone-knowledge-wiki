---
title: "GpioRequest (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/GpioRequest"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/GpioRequest.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# GpioRequest (UORB message)

Request GPIO mask to be read.

**TOPICS:** gpio_request

## Fields

| Name                                | Type     | Unit [Frame] | Range/Enum | Description                            |
| ----------------------------------- | -------- | ------------ | ---------- | -------------------------------------- |
| <a id="fld_timestamp"></a>timestamp | `uint64` |              |            | time since system start (microseconds) |
| <a id="fld_device_id"></a>device_id | `uint32` |              |            | Device id                              |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/GpioRequest.msg)

::: details Click here to see original file

```c
# Request GPIO mask to be read

uint64 timestamp			# time since system start (microseconds)
uint32 device_id			# Device id
```

:::
