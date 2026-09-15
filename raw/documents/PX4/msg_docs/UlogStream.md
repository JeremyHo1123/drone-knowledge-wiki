---
title: "UlogStream (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/UlogStream"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/UlogStream.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# UlogStream (UORB message)

Message to stream ULog data from the logger. Corresponds to the LOGGING_DATA. mavlink message.

**TOPICS:** ulog_stream

## Fields

| Name                                                      | Type         | Unit [Frame] | Range/Enum | Description                                       |
| --------------------------------------------------------- | ------------ | ------------ | ---------- | ------------------------------------------------- |
| <a id="fld_timestamp"></a>timestamp                       | `uint64`     |              |            | time since system start (microseconds)            |
| <a id="fld_length"></a>length                             | `uint8`      |              |            | length of data                                    |
| <a id="fld_first_message_offset"></a>first_message_offset | `uint8`      |              |            | offset into data where first message starts. This |
| <a id="fld_msg_sequence"></a>msg_sequence                 | `uint16`     |              |            | allows determine drops                            |
| <a id="fld_flags"></a>flags                               | `uint8`      |              |            | see FLAGS\_\*                                     |
| <a id="fld_data"></a>data                                 | `uint8[249]` |              |            | ulog data                                         |

## Constants

| Name                                            | Type    | Value | Description                                                          |
| ----------------------------------------------- | ------- | ----- | -------------------------------------------------------------------- |
| <a id="#FLAGS_NEED_ACK"></a> FLAGS_NEED_ACK     | `uint8` | 1     | if set, this message requires to be acked.                           |
| <a id="#ORB_QUEUE_LENGTH"></a> ORB_QUEUE_LENGTH | `uint8` | 16    | TODO: we might be able to reduce this if mavlink polled on the topic |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/UlogStream.msg)

::: details Click here to see original file

```c
# Message to stream ULog data from the logger. Corresponds to the LOGGING_DATA
# mavlink message

uint64 timestamp		# time since system start (microseconds)

# flags bitmasks
uint8 FLAGS_NEED_ACK = 1	# if set, this message requires to be acked.
				# Acked messages are published synchronous: a
				# publisher waits for an ack before sending the
				# next message

uint8 length			# length of data
uint8 first_message_offset	# offset into data where first message starts. This
				# can be used for recovery, when a previous message got lost
uint16 msg_sequence		# allows determine drops
uint8 flags			# see FLAGS_*
uint8[249] data		# ulog data

uint8 ORB_QUEUE_LENGTH = 16	# TODO: we might be able to reduce this if mavlink polled on the topic
```

:::
