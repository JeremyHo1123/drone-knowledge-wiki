---
title: "OpenDroneIdBasicId (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/OpenDroneIdBasicId"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/OpenDroneIdBasicId.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# OpenDroneIdBasicId (UORB message)

**TOPICS:** open_drone_id_basic_id

## Fields

| Name                                | Type        | Unit [Frame] | Range/Enum | Description                                                                                                              |
| ----------------------------------- | ----------- | ------------ | ---------- | ------------------------------------------------------------------------------------------------------------------------ |
| <a id="fld_timestamp"></a>timestamp | `uint64`    |              |            |
| <a id="fld_id_or_mac"></a>id_or_mac | `uint8[20]` |              |            | Only used for drone ID data received from other UAs, no null termination, null filled if shorter                         |
| <a id="fld_id_type"></a>id_type     | `uint8`     |              |            | MAV_ODID_ID_TYPE: indicates the format for the uas_id field                                                              |
| <a id="fld_ua_type"></a>ua_type     | `uint8`     |              |            | MAV_ODID_UA_TYPE: indicates the type of UA (Unmanned Aircraft)                                                           |
| <a id="fld_uas_id"></a>uas_id       | `uint8[20]` |              |            | UAS (Unmanned Aircraft System) ID following the format specified by id_type, no null termination, null filled if shorter |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/OpenDroneIdBasicId.msg)

::: details Click here to see original file

```c
uint64 timestamp
uint8[20] id_or_mac	# Only used for drone ID data received from other UAs, no null termination, null filled if shorter
uint8 id_type		# MAV_ODID_ID_TYPE: indicates the format for the uas_id field
uint8 ua_type		# MAV_ODID_UA_TYPE: indicates the type of UA (Unmanned Aircraft)
uint8[20] uas_id	# UAS (Unmanned Aircraft System) ID following the format specified by id_type, no null termination, null filled if shorter
```

:::
