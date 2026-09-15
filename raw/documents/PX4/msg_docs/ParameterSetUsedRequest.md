---
title: "ParameterSetUsedRequest (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/ParameterSetUsedRequest"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/ParameterSetUsedRequest.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# ParameterSetUsedRequest (UORB message)

ParameterSetUsedRequest : Used by a remote to update the used flag for a parameter on the primary.

**TOPICS:** parameter_set_used_request

## Fields

| Name                                            | Type     | Unit [Frame] | Range/Enum | Description |
| ----------------------------------------------- | -------- | ------------ | ---------- | ----------- |
| <a id="fld_timestamp"></a>timestamp             | `uint64` |              |            |
| <a id="fld_parameter_index"></a>parameter_index | `uint16` |              |            |

## Constants

| Name                                            | Type    | Value | Description |
| ----------------------------------------------- | ------- | ----- | ----------- |
| <a id="#ORB_QUEUE_LENGTH"></a> ORB_QUEUE_LENGTH | `uint8` | 64    |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/ParameterSetUsedRequest.msg)

::: details Click here to see original file

```c
# ParameterSetUsedRequest : Used by a remote to update the used flag for a parameter on the primary

uint64 timestamp
uint16 parameter_index

uint8 ORB_QUEUE_LENGTH = 64
```

:::
