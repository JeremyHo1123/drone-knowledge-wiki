---
title: "FigureEightStatus (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/FigureEightStatus"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/FigureEightStatus.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# FigureEightStatus (UORB message)

**TOPICS:** figure_eight_status

## Fields

| Name                                      | Type      | Unit [Frame] | Range/Enum | Description                                                                                                                                     |
| ----------------------------------------- | --------- | ------------ | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| <a id="fld_timestamp"></a>timestamp       | `uint64`  |              |            | time since system start (microseconds)                                                                                                          |
| <a id="fld_major_radius"></a>major_radius | `float32` |              |            | Major axis radius of the figure eight [m]. Positive values orbit clockwise, negative values orbit counter-clockwise.                            |
| <a id="fld_minor_radius"></a>minor_radius | `float32` |              |            | Minor axis radius of the figure eight [m].                                                                                                      |
| <a id="fld_orientation"></a>orientation   | `float32` |              |            | Orientation of the major axis of the figure eight [rad].                                                                                        |
| <a id="fld_frame"></a>frame               | `uint8`   |              |            | The coordinate system of the fields: x, y, z.                                                                                                   |
| <a id="fld_x"></a>x                       | `int32`   |              |            | X coordinate of center point. Coordinate system depends on frame field: local = x position in meters _ 1e4, global = latitude in degrees _ 1e7. |
| <a id="fld_y"></a>y                       | `int32`   |              |            | Y coordinate of center point. Coordinate system depends on frame field: local = y position in meters _ 1e4, global = latitude in degrees _ 1e7. |
| <a id="fld_z"></a>z                       | `float32` |              |            | Altitude of center point. Coordinate system depends on frame field.                                                                             |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/FigureEightStatus.msg)

::: details Click here to see original file

```c
uint64 timestamp # time since system start (microseconds)
float32 major_radius 	# Major axis radius of the figure eight [m]. Positive values orbit clockwise, negative values orbit counter-clockwise.
float32 minor_radius 	# Minor axis radius of the figure eight [m].
float32 orientation 	# Orientation of the major axis of the figure eight [rad].
uint8 frame      # The coordinate system of the fields: x, y, z.
int32 x          # X coordinate of center point. Coordinate system depends on frame field: local = x position in meters * 1e4, global = latitude in degrees * 1e7.
int32 y        	 # Y coordinate of center point. Coordinate system depends on frame field: local = y position in meters * 1e4, global = latitude in degrees * 1e7.
float32 z        # Altitude of center point. Coordinate system depends on frame field.
```

:::
