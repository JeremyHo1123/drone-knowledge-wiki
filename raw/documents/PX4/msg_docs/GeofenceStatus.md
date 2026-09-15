---
title: "GeofenceStatus (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/GeofenceStatus"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/GeofenceStatus.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# GeofenceStatus (UORB message)

**TOPICS:** geofence_status

## Fields

| Name                                    | Type     | Unit [Frame] | Range/Enum | Description                            |
| --------------------------------------- | -------- | ------------ | ---------- | -------------------------------------- |
| <a id="fld_timestamp"></a>timestamp     | `uint64` |              |            | time since system start (microseconds) |
| <a id="fld_geofence_id"></a>geofence_id | `uint32` |              |            | loaded geofence id                     |
| <a id="fld_status"></a>status           | `uint8`  |              |            | Current geofence status                |

## Constants

| Name                                              | Type    | Value | Description |
| ------------------------------------------------- | ------- | ----- | ----------- |
| <a id="#GF_STATUS_LOADING"></a> GF_STATUS_LOADING | `uint8` | 0     |
| <a id="#GF_STATUS_READY"></a> GF_STATUS_READY     | `uint8` | 1     |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/GeofenceStatus.msg)

::: details Click here to see original file

```c
uint64 timestamp                        # time since system start (microseconds)

uint32 geofence_id 			# loaded geofence id
uint8 status 				# Current geofence status

uint8 GF_STATUS_LOADING = 0
uint8 GF_STATUS_READY = 1
```

:::
