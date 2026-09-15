---
title: "CanInterfaceStatus (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/CanInterfaceStatus"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/CanInterfaceStatus.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# CanInterfaceStatus (UORB message)

**TOPICS:** can_interface_status

## Fields

| Name                                | Type     | Unit [Frame] | Range/Enum | Description                            |
| ----------------------------------- | -------- | ------------ | ---------- | -------------------------------------- |
| <a id="fld_timestamp"></a>timestamp | `uint64` |              |            | time since system start (microseconds) |
| <a id="fld_interface"></a>interface | `uint8`  |              |            |
| <a id="fld_io_errors"></a>io_errors | `uint64` |              |            |
| <a id="fld_frames_tx"></a>frames_tx | `uint64` |              |            |
| <a id="fld_frames_rx"></a>frames_rx | `uint64` |              |            |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/CanInterfaceStatus.msg)

::: details Click here to see original file

```c
uint64 timestamp		# time since system start (microseconds)
uint8 interface

uint64 io_errors
uint64 frames_tx
uint64 frames_rx
```

:::
