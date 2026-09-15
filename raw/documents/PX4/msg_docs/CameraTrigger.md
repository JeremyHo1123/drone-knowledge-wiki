---
title: "CameraTrigger (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/CameraTrigger"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/CameraTrigger.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# CameraTrigger (UORB message)

**TOPICS:** camera_trigger

## Fields

| Name                                        | Type     | Unit [Frame] | Range/Enum | Description                            |
| ------------------------------------------- | -------- | ------------ | ---------- | -------------------------------------- |
| <a id="fld_timestamp"></a>timestamp         | `uint64` |              |            | time since system start (microseconds) |
| <a id="fld_timestamp_utc"></a>timestamp_utc | `uint64` |              |            | UTC timestamp                          |
| <a id="fld_seq"></a>seq                     | `uint32` |              |            | Image sequence number                  |
| <a id="fld_feedback"></a>feedback           | `bool`   |              |            | Trigger feedback from camera           |

## Constants

| Name                                            | Type     | Value | Description |
| ----------------------------------------------- | -------- | ----- | ----------- |
| <a id="#ORB_QUEUE_LENGTH"></a> ORB_QUEUE_LENGTH | `uint32` | 2     |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/CameraTrigger.msg)

::: details Click here to see original file

```c
uint64 timestamp	# time since system start (microseconds)
uint64 timestamp_utc # UTC timestamp

uint32 seq		# Image sequence number
bool feedback	# Trigger feedback from camera

uint32 ORB_QUEUE_LENGTH = 2
```

:::
