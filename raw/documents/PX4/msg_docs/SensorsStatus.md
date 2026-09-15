---
title: "SensorsStatus (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/SensorsStatus"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/SensorsStatus.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# SensorsStatus (UORB message)

Sensor check metrics. This will be zero for a sensor that's primary or unpopulated.

**TOPICS:** sensors_status_baro sensors_status_mag

## Fields

| Name                                                | Type         | Unit [Frame] | Range/Enum | Description                                              |
| --------------------------------------------------- | ------------ | ------------ | ---------- | -------------------------------------------------------- |
| <a id="fld_timestamp"></a>timestamp                 | `uint64`     |              |            | time since system start (microseconds)                   |
| <a id="fld_device_id_primary"></a>device_id_primary | `uint32`     |              |            | current primary device id for reference                  |
| <a id="fld_device_ids"></a>device_ids               | `uint32[4]`  |              |            |
| <a id="fld_inconsistency"></a>inconsistency         | `float32[4]` |              |            | magnitude of difference between sensor instance and mean |
| <a id="fld_healthy"></a>healthy                     | `bool[4]`    |              |            | sensor healthy                                           |
| <a id="fld_priority"></a>priority                   | `uint8[4]`   |              |            |
| <a id="fld_enabled"></a>enabled                     | `bool[4]`    |              |            |
| <a id="fld_external"></a>external                   | `bool[4]`    |              |            |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/SensorsStatus.msg)

::: details Click here to see original file

```c
#
# Sensor check metrics. This will be zero for a sensor that's primary or unpopulated.
#
uint64 timestamp # time since system start (microseconds)

uint32 device_id_primary       # current primary device id for reference

uint32[4] device_ids
float32[4] inconsistency       # magnitude of difference between sensor instance and mean
bool[4] healthy                # sensor healthy
uint8[4] priority
bool[4] enabled
bool[4] external

# TOPICS sensors_status_baro sensors_status_mag
```

:::
