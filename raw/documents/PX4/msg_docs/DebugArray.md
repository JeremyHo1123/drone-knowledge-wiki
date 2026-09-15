---
title: "DebugArray (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/DebugArray"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/DebugArray.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# DebugArray (UORB message)

**TOPICS:** debug_array

## Fields

| Name                                | Type          | Unit [Frame] | Range/Enum | Description                                                   |
| ----------------------------------- | ------------- | ------------ | ---------- | ------------------------------------------------------------- |
| <a id="fld_timestamp"></a>timestamp | `uint64`      |              |            | time since system start (microseconds)                        |
| <a id="fld_id"></a>id               | `uint16`      |              |            | unique ID of debug array, used to discriminate between arrays |
| <a id="fld_name"></a>name           | `char[10]`    |              |            | name of the debug array (max. 10 characters)                  |
| <a id="fld_data"></a>data           | `float32[58]` |              |            | data                                                          |

## Constants

| Name                                | Type    | Value | Description |
| ----------------------------------- | ------- | ----- | ----------- |
| <a id="#ARRAY_SIZE"></a> ARRAY_SIZE | `uint8` | 58    |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/DebugArray.msg)

::: details Click here to see original file

```c
uint8 ARRAY_SIZE = 58
uint64 timestamp            # time since system start (microseconds)
uint16 id                   # unique ID of debug array, used to discriminate between arrays
char[10] name               # name of the debug array (max. 10 characters)
float32[58] data            # data
```

:::
