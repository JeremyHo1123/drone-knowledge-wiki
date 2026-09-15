---
title: "OpenDroneIdArmStatus (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/OpenDroneIdArmStatus"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/OpenDroneIdArmStatus.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# OpenDroneIdArmStatus (UORB message)

**TOPICS:** open_drone_id_arm_status

## Fields

| Name                                | Type       | Unit [Frame] | Range/Enum | Description |
| ----------------------------------- | ---------- | ------------ | ---------- | ----------- |
| <a id="fld_timestamp"></a>timestamp | `uint64`   |              |            |
| <a id="fld_status"></a>status       | `uint8`    |              |            |
| <a id="fld_error"></a>error         | `char[50]` |              |            |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/OpenDroneIdArmStatus.msg)

::: details Click here to see original file

```c
uint64 timestamp
uint8 status
char[50] error
```

:::
