---
title: "ParameterUpdate (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/ParameterUpdate"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/ParameterUpdate.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# ParameterUpdate (UORB message)

This message is used to notify the system about one or more parameter changes.

**TOPICS:** parameter_update

## Fields

| Name                                          | Type     | Unit [Frame] | Range/Enum | Description                              |
| --------------------------------------------- | -------- | ------------ | ---------- | ---------------------------------------- |
| <a id="fld_timestamp"></a>timestamp           | `uint64` |              |            | time since system start (microseconds)   |
| <a id="fld_instance"></a>instance             | `uint32` |              |            | Instance count - constantly incrementing |
| <a id="fld_get_count"></a>get_count           | `uint32` |              |            |
| <a id="fld_set_count"></a>set_count           | `uint32` |              |            |
| <a id="fld_find_count"></a>find_count         | `uint32` |              |            |
| <a id="fld_export_count"></a>export_count     | `uint32` |              |            |
| <a id="fld_active"></a>active                 | `uint16` |              |            |
| <a id="fld_changed"></a>changed               | `uint16` |              |            |
| <a id="fld_custom_default"></a>custom_default | `uint16` |              |            |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/ParameterUpdate.msg)

::: details Click here to see original file

```c
# This message is used to notify the system about one or more parameter changes

uint64 timestamp		# time since system start (microseconds)

uint32 instance		# Instance count - constantly incrementing

uint32 get_count
uint32 set_count
uint32 find_count
uint32 export_count

uint16 active
uint16 changed
uint16 custom_default
```

:::
