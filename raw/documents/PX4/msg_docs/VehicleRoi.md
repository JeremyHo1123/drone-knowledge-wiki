---
title: "VehicleRoi (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/VehicleRoi"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/VehicleRoi.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# VehicleRoi (UORB message)

Vehicle Region Of Interest (ROI).

**TOPICS:** vehicle_roi

## Fields

| Name                                      | Type      | Unit [Frame] | Range/Enum | Description                            |
| ----------------------------------------- | --------- | ------------ | ---------- | -------------------------------------- |
| <a id="fld_timestamp"></a>timestamp       | `uint64`  |              |            | time since system start (microseconds) |
| <a id="fld_mode"></a>mode                 | `uint8`   |              |            | ROI mode (see above)                   |
| <a id="fld_lat"></a>lat                   | `float64` |              |            | Latitude to point to                   |
| <a id="fld_lon"></a>lon                   | `float64` |              |            | Longitude to point to                  |
| <a id="fld_alt"></a>alt                   | `float32` |              |            | Altitude to point to                   |
| <a id="fld_roll_offset"></a>roll_offset   | `float32` |              |            | angle offset in rad                    |
| <a id="fld_pitch_offset"></a>pitch_offset | `float32` |              |            | angle offset in rad                    |
| <a id="fld_yaw_offset"></a>yaw_offset     | `float32` |              |            | angle offset in rad                    |

## Constants

| Name                                    | Type    | Value | Description                                    |
| --------------------------------------- | ------- | ----- | ---------------------------------------------- |
| <a id="#ROI_NONE"></a> ROI_NONE         | `uint8` | 0     | No region of interest                          |
| <a id="#ROI_WPNEXT"></a> ROI_WPNEXT     | `uint8` | 1     | Point toward next MISSION with optional offset |
| <a id="#ROI_WPINDEX"></a> ROI_WPINDEX   | `uint8` | 2     | Point toward given MISSION                     |
| <a id="#ROI_LOCATION"></a> ROI_LOCATION | `uint8` | 3     | Point toward fixed location                    |
| <a id="#ROI_TARGET"></a> ROI_TARGET     | `uint8` | 4     | Point toward target                            |
| <a id="#ROI_ENUM_END"></a> ROI_ENUM_END | `uint8` | 5     |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/VehicleRoi.msg)

::: details Click here to see original file

```c
# Vehicle Region Of Interest (ROI)

uint64 timestamp			# time since system start (microseconds)

uint8 ROI_NONE = 0			# No region of interest
uint8 ROI_WPNEXT = 1			# Point toward next MISSION with optional offset
uint8 ROI_WPINDEX = 2			# Point toward given MISSION
uint8 ROI_LOCATION = 3			# Point toward fixed location
uint8 ROI_TARGET = 4			# Point toward target
uint8 ROI_ENUM_END = 5

uint8 mode          # ROI mode (see above)

float64 lat			    # Latitude to point to
float64 lon			    # Longitude to point to
float32 alt			    # Altitude to point to

# additional angle offsets to next waypoint (only used with ROI_WPNEXT)
float32 roll_offset		# angle offset in rad
float32 pitch_offset		# angle offset in rad
float32 yaw_offset		# angle offset in rad
```

:::
