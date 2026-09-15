---
title: "UnregisterExtComponent (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/UnregisterExtComponent"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/UnregisterExtComponent.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# UnregisterExtComponent (UORB message)

**TOPICS:** unregister_ext_component

## Fields

| Name                                              | Type       | Unit [Frame] | Range/Enum | Description                                         |
| ------------------------------------------------- | ---------- | ------------ | ---------- | --------------------------------------------------- |
| <a id="fld_timestamp"></a>timestamp               | `uint64`   |              |            | time since system start (microseconds)              |
| <a id="fld_name"></a>name                         | `char[25]` |              |            | either the mode name, or component name             |
| <a id="fld_arming_check_id"></a>arming_check_id   | `int8`     |              |            | arming check registration ID (-1 if not registered) |
| <a id="fld_mode_id"></a>mode_id                   | `int8`     |              |            | assigned mode ID (-1 if not registered)             |
| <a id="fld_mode_executor_id"></a>mode_executor_id | `int8`     |              |            | assigned mode executor ID (-1 if not registered)    |

## Constants

| Name                                          | Type     | Value | Description |
| --------------------------------------------- | -------- | ----- | ----------- |
| <a id="#MESSAGE_VERSION"></a> MESSAGE_VERSION | `uint32` | 0     |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/versioned/UnregisterExtComponent.msg)

::: details Click here to see original file

```c
uint32 MESSAGE_VERSION = 0

uint64 timestamp # time since system start (microseconds)

char[25] name                      # either the mode name, or component name

int8 arming_check_id      # arming check registration ID (-1 if not registered)
int8 mode_id              # assigned mode ID (-1 if not registered)
int8 mode_executor_id     # assigned mode executor ID (-1 if not registered)
```

:::
