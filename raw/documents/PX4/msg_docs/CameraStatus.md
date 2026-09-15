---
title: "CameraStatus (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/CameraStatus"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/CameraStatus.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# CameraStatus (UORB message)

**TOPICS:** camera_status

## Fields

| Name                                          | Type     | Unit [Frame] | Range/Enum | Description                                      |
| --------------------------------------------- | -------- | ------------ | ---------- | ------------------------------------------------ |
| <a id="fld_timestamp"></a>timestamp           | `uint64` |              |            | time since system start (microseconds)           |
| <a id="fld_active_sys_id"></a>active_sys_id   | `uint8`  |              |            | mavlink system id of the currently active camera |
| <a id="fld_active_comp_id"></a>active_comp_id | `uint8`  |              |            | mavlink component id of currently active camera  |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/CameraStatus.msg)

::: details Click here to see original file

```c
uint64 timestamp		# time since system start (microseconds)

uint8 active_sys_id		# mavlink system id of the currently active camera
uint8 active_comp_id 	# mavlink component id of currently active camera
```

:::
