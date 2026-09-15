---
title: "DebugVect (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/DebugVect"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/DebugVect.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# DebugVect (UORB message)

**TOPICS:** debug_vect

## Fields

| Name                                | Type       | Unit [Frame] | Range/Enum | Description                            |
| ----------------------------------- | ---------- | ------------ | ---------- | -------------------------------------- |
| <a id="fld_timestamp"></a>timestamp | `uint64`   |              |            | time since system start (microseconds) |
| <a id="fld_name"></a>name           | `char[10]` |              |            | max. 10 characters as key / name       |
| <a id="fld_x"></a>x                 | `float32`  |              |            | x value                                |
| <a id="fld_y"></a>y                 | `float32`  |              |            | y value                                |
| <a id="fld_z"></a>z                 | `float32`  |              |            | z value                                |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/DebugVect.msg)

::: details Click here to see original file

```c
uint64 timestamp	# time since system start (microseconds)
char[10] name           # max. 10 characters as key / name
float32 x               # x value
float32 y               # y value
float32 z               # z value
```

:::
