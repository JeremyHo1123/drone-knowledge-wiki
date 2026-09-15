---
title: "TaskStackInfo (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/TaskStackInfo"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/TaskStackInfo.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# TaskStackInfo (UORB message)

stack information for a single running process.

**TOPICS:** task_stack_info

## Fields

| Name                                  | Type       | Unit [Frame] | Range/Enum | Description                            |
| ------------------------------------- | ---------- | ------------ | ---------- | -------------------------------------- |
| <a id="fld_timestamp"></a>timestamp   | `uint64`   |              |            | time since system start (microseconds) |
| <a id="fld_stack_free"></a>stack_free | `uint16`   |              |            |
| <a id="fld_task_name"></a>task_name   | `char[24]` |              |            |

## Constants

| Name                                            | Type    | Value | Description |
| ----------------------------------------------- | ------- | ----- | ----------- |
| <a id="#ORB_QUEUE_LENGTH"></a> ORB_QUEUE_LENGTH | `uint8` | 2     |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/TaskStackInfo.msg)

::: details Click here to see original file

```c
# stack information for a single running process

uint64 timestamp		# time since system start (microseconds)

uint16 stack_free
char[24] task_name

uint8 ORB_QUEUE_LENGTH = 2
```

:::
