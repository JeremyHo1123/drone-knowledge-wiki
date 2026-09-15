---
title: "BatteryInfo (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/BatteryInfo"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/BatteryInfo.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# BatteryInfo (UORB message)

Battery information.

Static or near-invariant battery information.
Should be streamed at low rate.

**TOPICS:** battery_info

## Fields

| Name                                        | Type       | Unit [Frame] | Range/Enum | Description                                                                                |
| ------------------------------------------- | ---------- | ------------ | ---------- | ------------------------------------------------------------------------------------------ |
| <a id="fld_timestamp"></a>timestamp         | `uint64`   | us           |            | Time since system start                                                                    |
| <a id="fld_id"></a>id                       | `uint8`    |              |            | Must match the id in the battery_status message for the same battery                       |
| <a id="fld_serial_number"></a>serial_number | `char[32]` |              |            | Serial number of the battery pack in ASCII characters, 0 terminated (Invalid: 0 All bytes) |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/BatteryInfo.msg)

::: details Click here to see original file

```c
# Battery information
#
# Static or near-invariant battery information.
# Should be streamed at low rate.

uint64 timestamp # [us] Time since system start

uint8 id # Must match the id in the battery_status message for the same battery
char[32] serial_number # [@invalid 0 All bytes] Serial number of the battery pack in ASCII characters, 0 terminated
```

:::
