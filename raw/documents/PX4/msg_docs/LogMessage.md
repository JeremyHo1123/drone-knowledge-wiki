---
title: "LogMessage (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/LogMessage"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/LogMessage.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# LogMessage (UORB message)

A logging message, output with PX4_WARN, PX4_ERR, PX4_INFO.

**TOPICS:** log_message

## Fields

| Name                                | Type        | Unit [Frame] | Range/Enum | Description                                              |
| ----------------------------------- | ----------- | ------------ | ---------- | -------------------------------------------------------- |
| <a id="fld_timestamp"></a>timestamp | `uint64`    |              |            | time since system start (microseconds)                   |
| <a id="fld_severity"></a>severity   | `uint8`     |              |            | log level (same as in the linux kernel, starting with 0) |
| <a id="fld_text"></a>text           | `char[127]` |              |            |

## Constants

| Name                                            | Type    | Value | Description |
| ----------------------------------------------- | ------- | ----- | ----------- |
| <a id="#ORB_QUEUE_LENGTH"></a> ORB_QUEUE_LENGTH | `uint8` | 4     |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/LogMessage.msg)

::: details Click here to see original file

```c
# A logging message, output with PX4_WARN, PX4_ERR, PX4_INFO

uint64 timestamp		# time since system start (microseconds)

uint8 severity # log level (same as in the linux kernel, starting with 0)
char[127] text

uint8 ORB_QUEUE_LENGTH = 4
```

:::
