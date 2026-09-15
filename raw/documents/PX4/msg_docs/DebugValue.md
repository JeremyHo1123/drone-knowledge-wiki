---
title: "DebugValue (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/DebugValue"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/DebugValue.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# DebugValue (UORB message)

**TOPICS:** debug_value

## Fields

| Name                                | Type      | Unit [Frame] | Range/Enum | Description                            |
| ----------------------------------- | --------- | ------------ | ---------- | -------------------------------------- |
| <a id="fld_timestamp"></a>timestamp | `uint64`  |              |            | time since system start (microseconds) |
| <a id="fld_ind"></a>ind             | `int8`    |              |            | index of debug variable                |
| <a id="fld_value"></a>value         | `float32` |              |            | the value to send as debug output      |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/DebugValue.msg)

::: details Click here to see original file

```c
uint64 timestamp	# time since system start (microseconds)
int8 ind                # index of debug variable
float32 value           # the value to send as debug output
```

:::
