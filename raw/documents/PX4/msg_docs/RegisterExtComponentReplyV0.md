---
title: "RegisterExtComponentReplyV0 (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/RegisterExtComponentReplyV0"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/RegisterExtComponentReplyV0.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# RegisterExtComponentReplyV0 (UORB message)

**TOPICS:** register_ext_component_reply_v0

## Fields

| Name                                                      | Type       | Unit [Frame] | Range/Enum | Description                                  |
| --------------------------------------------------------- | ---------- | ------------ | ---------- | -------------------------------------------- |
| <a id="fld_timestamp"></a>timestamp                       | `uint64`   |              |            | time since system start (microseconds)       |
| <a id="fld_request_id"></a>request_id                     | `uint64`   |              |            | ID from the request                          |
| <a id="fld_name"></a>name                                 | `char[25]` |              |            | name from the request                        |
| <a id="fld_px4_ros2_api_version"></a>px4_ros2_api_version | `uint16`   |              |            |
| <a id="fld_success"></a>success                           | `bool`     |              |            |
| <a id="fld_arming_check_id"></a>arming_check_id           | `int8`     |              |            | arming check registration ID (-1 if invalid) |
| <a id="fld_mode_id"></a>mode_id                           | `int8`     |              |            | assigned mode ID (-1 if invalid)             |
| <a id="fld_mode_executor_id"></a>mode_executor_id         | `int8`     |              |            | assigned mode executor ID (-1 if invalid)    |

## Constants

| Name                                            | Type     | Value | Description |
| ----------------------------------------------- | -------- | ----- | ----------- |
| <a id="#MESSAGE_VERSION"></a> MESSAGE_VERSION   | `uint32` | 0     |
| <a id="#ORB_QUEUE_LENGTH"></a> ORB_QUEUE_LENGTH | `uint8`  | 2     |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/px4_msgs_old/msg/RegisterExtComponentReplyV0.msg)

::: details Click here to see original file

```c
uint32 MESSAGE_VERSION = 0

uint64 timestamp # time since system start (microseconds)

uint64 request_id          # ID from the request
char[25] name              # name from the request

uint16 px4_ros2_api_version

bool success
int8 arming_check_id      # arming check registration ID (-1 if invalid)
int8 mode_id              # assigned mode ID (-1 if invalid)
int8 mode_executor_id     # assigned mode executor ID (-1 if invalid)

uint8 ORB_QUEUE_LENGTH = 2
```

:::
