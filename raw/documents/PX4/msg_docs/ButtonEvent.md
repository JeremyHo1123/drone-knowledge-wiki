---
title: "ButtonEvent (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/ButtonEvent"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/ButtonEvent.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# ButtonEvent (UORB message)

**TOPICS:** button_event safety_button

## Fields

| Name                                | Type     | Unit [Frame] | Range/Enum | Description                            |
| ----------------------------------- | -------- | ------------ | ---------- | -------------------------------------- |
| <a id="fld_timestamp"></a>timestamp | `uint64` |              |            | time since system start (microseconds) |
| <a id="fld_triggered"></a>triggered | `bool`   |              |            | Set to true if the event is triggered  |

## Constants

| Name                                            | Type    | Value | Description |
| ----------------------------------------------- | ------- | ----- | ----------- |
| <a id="#ORB_QUEUE_LENGTH"></a> ORB_QUEUE_LENGTH | `uint8` | 2     |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/ButtonEvent.msg)

::: details Click here to see original file

```c
uint64 timestamp			# time since system start (microseconds)
bool triggered				# Set to true if the event is triggered

# TOPICS button_event safety_button

uint8 ORB_QUEUE_LENGTH = 2
```

:::
