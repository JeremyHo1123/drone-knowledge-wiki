---
title: "OpenDroneIdOperatorId (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/OpenDroneIdOperatorId"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/OpenDroneIdOperatorId.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# OpenDroneIdOperatorId (UORB message)

**TOPICS:** open_drone_id_operator_id

## Fields

| Name                                              | Type        | Unit [Frame] | Range/Enum | Description |
| ------------------------------------------------- | ----------- | ------------ | ---------- | ----------- |
| <a id="fld_timestamp"></a>timestamp               | `uint64`    |              |            |
| <a id="fld_id_or_mac"></a>id_or_mac               | `uint8[20]` |              |            |
| <a id="fld_operator_id_type"></a>operator_id_type | `uint8`     |              |            |
| <a id="fld_operator_id"></a>operator_id           | `char[20]`  |              |            |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/OpenDroneIdOperatorId.msg)

::: details Click here to see original file

```c
uint64 timestamp
uint8[20] id_or_mac
uint8 operator_id_type
char[20] operator_id
```

:::
