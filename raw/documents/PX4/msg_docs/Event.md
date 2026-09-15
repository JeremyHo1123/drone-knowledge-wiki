---
title: "Event (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/Event"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/Event.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# Event (UORB message)

Events interface.

**TOPICS:** event

## Fields

| Name                                          | Type        | Unit [Frame] | Range/Enum | Description                                            |
| --------------------------------------------- | ----------- | ------------ | ---------- | ------------------------------------------------------ |
| <a id="fld_timestamp"></a>timestamp           | `uint64`    |              |            | time since system start (microseconds)                 |
| <a id="fld_id"></a>id                         | `uint32`    |              |            | Event ID                                               |
| <a id="fld_event_sequence"></a>event_sequence | `uint16`    |              |            | Event sequence number                                  |
| <a id="fld_arguments"></a>arguments           | `uint8[25]` |              |            | (optional) arguments, depend on event id               |
| <a id="fld_log_levels"></a>log_levels         | `uint8`     |              |            | Log levels: 4 bits MSB: internal, 4 bits LSB: external |

## Constants

| Name                                            | Type     | Value | Description |
| ----------------------------------------------- | -------- | ----- | ----------- |
| <a id="#MESSAGE_VERSION"></a> MESSAGE_VERSION   | `uint32` | 1     |
| <a id="#ORB_QUEUE_LENGTH"></a> ORB_QUEUE_LENGTH | `uint8`  | 16    |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/versioned/Event.msg)

::: details Click here to see original file

```c
# Events interface
uint32 MESSAGE_VERSION = 1

uint64 timestamp			# time since system start (microseconds)

uint32 id                   # Event ID
uint16 event_sequence       # Event sequence number
uint8[25] arguments         # (optional) arguments, depend on event id

uint8 log_levels            # Log levels: 4 bits MSB: internal, 4 bits LSB: external

uint8 ORB_QUEUE_LENGTH = 16
```

:::
