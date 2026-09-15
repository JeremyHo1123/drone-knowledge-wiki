---
title: "MessageFormatResponse (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/MessageFormatResponse"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/MessageFormatResponse.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# MessageFormatResponse (UORB message)

**TOPICS:** message_format_response

## Fields

| Name                                              | Type       | Unit [Frame] | Range/Enum | Description                                                                                                      |
| ------------------------------------------------- | ---------- | ------------ | ---------- | ---------------------------------------------------------------------------------------------------------------- |
| <a id="fld_timestamp"></a>timestamp               | `uint64`   |              |            | time since system start (microseconds)                                                                           |
| <a id="fld_protocol_version"></a>protocol_version | `uint16`   |              |            | Must be set to LATEST_PROTOCOL_VERSION. Do not change this field, it must be the first field after the timestamp |
| <a id="fld_topic_name"></a>topic_name             | `char[50]` |              |            | E.g. /fmu/in/vehicle_command                                                                                     |
| <a id="fld_success"></a>success                   | `bool`     |              |            |
| <a id="fld_message_hash"></a>message_hash         | `uint32`   |              |            | hash over all message fields                                                                                     |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/MessageFormatResponse.msg)

::: details Click here to see original file

```c
uint64 timestamp # time since system start (microseconds)

# Response from PX4 with the format of a message

uint16 protocol_version           # Must be set to LATEST_PROTOCOL_VERSION. Do not change this field, it must be the first field after the timestamp

char[50] topic_name  # E.g. /fmu/in/vehicle_command

bool success
uint32 message_hash # hash over all message fields
```

:::
