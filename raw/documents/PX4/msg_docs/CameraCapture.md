---
title: "CameraCapture (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/CameraCapture"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/CameraCapture.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# CameraCapture (UORB message)

**TOPICS:** camera_capture

## Fields

| Name                                            | Type         | Unit [Frame] | Range/Enum | Description                                                                                              |
| ----------------------------------------------- | ------------ | ------------ | ---------- | -------------------------------------------------------------------------------------------------------- |
| <a id="fld_timestamp"></a>timestamp             | `uint64`     |              |            | time since system start (microseconds)                                                                   |
| <a id="fld_timestamp_utc"></a>timestamp_utc     | `uint64`     |              |            | Capture time in UTC / GPS time                                                                           |
| <a id="fld_seq"></a>seq                         | `uint32`     |              |            | Image sequence number                                                                                    |
| <a id="fld_lat"></a>lat                         | `float64`    |              |            | Latitude in degrees (WGS84)                                                                              |
| <a id="fld_lon"></a>lon                         | `float64`    |              |            | Longitude in degrees (WGS84)                                                                             |
| <a id="fld_alt"></a>alt                         | `float32`    |              |            | Altitude (AMSL)                                                                                          |
| <a id="fld_ground_distance"></a>ground_distance | `float32`    |              |            | Altitude above ground (meters)                                                                           |
| <a id="fld_q"></a>q                             | `float32[4]` |              |            | Attitude of the camera relative to NED earth-fixed frame when using a gimbal, otherwise vehicle attitude |
| <a id="fld_result"></a>result                   | `int8`       |              |            | 1 for success, 0 for failure, -1 if camera does not provide feedback                                     |
| <a id="fld_report"></a>report                   | `bool`       |              |            | Report this capture to the ground station (CAMERA_IMAGE_CAPTURED); it is always logged regardless        |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/CameraCapture.msg)

::: details Click here to see original file

```c
uint64 timestamp		# time since system start (microseconds)
uint64 timestamp_utc		# Capture time in UTC / GPS time
uint32 seq					# Image sequence number
float64 lat					# Latitude in degrees (WGS84)
float64 lon					# Longitude in degrees (WGS84)
float32 alt					# Altitude (AMSL)
float32 ground_distance			# Altitude above ground (meters)
float32[4] q					# Attitude of the camera relative to NED earth-fixed frame when using a gimbal, otherwise vehicle attitude
int8 result					# 1 for success, 0 for failure, -1 if camera does not provide feedback
bool report					# Report this capture to the ground station (CAMERA_IMAGE_CAPTURED); it is always logged regardless
```

:::
