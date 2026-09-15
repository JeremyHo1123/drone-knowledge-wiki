---
title: "ParameterSetValueResponse (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/ParameterSetValueResponse"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/ParameterSetValueResponse.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# ParameterSetValueResponse (UORB message)

ParameterSetValueResponse : Response to a set value request by either primary or secondary.

**TOPICS:** parameter_set_value_response parameter_remote_set_value_response parameter_primary_set_value_response

## Fields

| Name                                                | Type     | Unit [Frame] | Range/Enum | Description |
| --------------------------------------------------- | -------- | ------------ | ---------- | ----------- |
| <a id="fld_timestamp"></a>timestamp                 | `uint64` |              |            |
| <a id="fld_request_timestamp"></a>request_timestamp | `uint64` |              |            |
| <a id="fld_parameter_index"></a>parameter_index     | `uint16` |              |            |

## Constants

| Name                                            | Type    | Value | Description |
| ----------------------------------------------- | ------- | ----- | ----------- |
| <a id="#ORB_QUEUE_LENGTH"></a> ORB_QUEUE_LENGTH | `uint8` | 4     |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/ParameterSetValueResponse.msg)

::: details Click here to see original file

```c
# ParameterSetValueResponse : Response to a set value request by either primary or secondary

uint64 timestamp
uint64 request_timestamp
uint16 parameter_index

uint8 ORB_QUEUE_LENGTH = 4

# TOPICS parameter_set_value_response parameter_remote_set_value_response parameter_primary_set_value_response
```

:::
