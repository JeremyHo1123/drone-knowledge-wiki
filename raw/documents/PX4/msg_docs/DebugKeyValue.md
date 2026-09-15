---
title: "DebugKeyValue (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/DebugKeyValue"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/DebugKeyValue.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# DebugKeyValue (UORB message)

**TOPICS:** debug_key_value

## Fields

| Name                                | Type       | Unit [Frame] | Range/Enum | Description                            |
| ----------------------------------- | ---------- | ------------ | ---------- | -------------------------------------- |
| <a id="fld_timestamp"></a>timestamp | `uint64`   |              |            | time since system start (microseconds) |
| <a id="fld_key"></a>key             | `char[10]` |              |            | max. 10 characters as key / name       |
| <a id="fld_value"></a>value         | `float32`  |              |            | the value to send as debug output      |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/DebugKeyValue.msg)

::: details Click here to see original file

```c
uint64 timestamp		# time since system start (microseconds)
char[10] key			# max. 10 characters as key / name
float32 value			# the value to send as debug output
```

:::
