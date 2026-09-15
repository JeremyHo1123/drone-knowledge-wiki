---
title: "EscEepromRead (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/EscEepromRead"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/EscEepromRead.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# EscEepromRead (UORB message)

**TOPICS:** esc_eeprom_read

## Fields

| Name                                | Type        | Unit [Frame] | Range/Enum | Description                                          |
| ----------------------------------- | ----------- | ------------ | ---------- | ---------------------------------------------------- |
| <a id="fld_timestamp"></a>timestamp | `uint64`    | us           |            | Time since system start                              |
| <a id="fld_firmware"></a>firmware   | `uint8`     |              |            | ESC firmware type (see ESC_FIRMWARE enum in MAVLink) |
| <a id="fld_index"></a>index         | `uint8`     |              |            | Index of the ESC (0 = ESC1, 1 = ESC2, etc.)          |
| <a id="fld_length"></a>length       | `uint16`    |              |            | Length of valid data                                 |
| <a id="fld_data"></a>data           | `uint8[48]` |              |            | Raw ESC EEPROM data                                  |

## Constants

| Name                                            | Type    | Value | Description                      |
| ----------------------------------------------- | ------- | ----- | -------------------------------- |
| <a id="#ORB_QUEUE_LENGTH"></a> ORB_QUEUE_LENGTH | `uint8` | 8     | To support 8 queued up responses |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/EscEepromRead.msg)

::: details Click here to see original file

```c
uint64 timestamp # [us] Time since system start
uint8 firmware # [-] ESC firmware type (see ESC_FIRMWARE enum in MAVLink)
uint8 index # [-] Index of the ESC (0 = ESC1, 1 = ESC2, etc.)
uint16 length # [-] Length of valid data
uint8[48] data # [-] Raw ESC EEPROM data

uint8 ORB_QUEUE_LENGTH = 8 # To support 8 queued up responses
```

:::
