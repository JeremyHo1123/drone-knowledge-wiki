---
title: "UlogStreamAck (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/UlogStreamAck"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/UlogStreamAck.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# UlogStreamAck (UORB message)

Ack a previously sent ulog_stream message that had. the NEED_ACK flag set.

**TOPICS:** ulog_stream_ack

## Fields

| Name                                      | Type     | Unit [Frame] | Range/Enum | Description                            |
| ----------------------------------------- | -------- | ------------ | ---------- | -------------------------------------- |
| <a id="fld_timestamp"></a>timestamp       | `uint64` |              |            | time since system start (microseconds) |
| <a id="fld_msg_sequence"></a>msg_sequence | `uint16` |              |            |

## Constants

| Name                                      | Type    | Value | Description                                                                      |
| ----------------------------------------- | ------- | ----- | -------------------------------------------------------------------------------- |
| <a id="#ACK_TIMEOUT"></a> ACK_TIMEOUT     | `int32` | 50    | timeout waiting for an ack until we retry to send the message [ms]               |
| <a id="#ACK_MAX_TRIES"></a> ACK_MAX_TRIES | `int32` | 50    | maximum amount of tries to (re-)send a message, each time waiting ACK_TIMEOUT ms |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/UlogStreamAck.msg)

::: details Click here to see original file

```c
# Ack a previously sent ulog_stream message that had
# the NEED_ACK flag set

uint64 timestamp		# time since system start (microseconds)
int32 ACK_TIMEOUT = 50		# timeout waiting for an ack until we retry to send the message [ms]
int32 ACK_MAX_TRIES = 50	# maximum amount of tries to (re-)send a message, each time waiting ACK_TIMEOUT ms

uint16 msg_sequence
```

:::
