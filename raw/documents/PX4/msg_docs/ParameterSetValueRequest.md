---
title: "ParameterSetValueRequest (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/ParameterSetValueRequest"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/ParameterSetValueRequest.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# ParameterSetValueRequest (UORB message)

ParameterSetValueRequest : Used by a remote or primary to update the value for a parameter at the other end.

**TOPICS:** parameter_set_value_request parameter_remote_set_value_request parameter_primary_set_value_request

## Fields

| Name                                            | Type      | Unit [Frame] | Range/Enum | Description                             |
| ----------------------------------------------- | --------- | ------------ | ---------- | --------------------------------------- |
| <a id="fld_timestamp"></a>timestamp             | `uint64`  |              |            |
| <a id="fld_parameter_index"></a>parameter_index | `uint16`  |              |            |
| <a id="fld_int_value"></a>int_value             | `int32`   |              |            | Optional value for an integer parameter |
| <a id="fld_float_value"></a>float_value         | `float32` |              |            | Optional value for a float parameter    |

## Constants

| Name                                            | Type    | Value | Description |
| ----------------------------------------------- | ------- | ----- | ----------- |
| <a id="#ORB_QUEUE_LENGTH"></a> ORB_QUEUE_LENGTH | `uint8` | 32    |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/ParameterSetValueRequest.msg)

::: details Click here to see original file

```c
# ParameterSetValueRequest : Used by a remote or primary to update the value for a parameter at the other end

uint64 timestamp
uint16 parameter_index

int32 int_value             # Optional value for an integer parameter
float32 float_value         # Optional value for a float parameter

uint8 ORB_QUEUE_LENGTH = 32

# TOPICS parameter_set_value_request parameter_remote_set_value_request parameter_primary_set_value_request
```

:::
