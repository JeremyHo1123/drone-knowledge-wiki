---
title: "Camera Setup"
type: document
doc_set: QGC
doc_version: Stable_V5.0
section: setup_view
source_url: "https://docs.qgroundcontrol.com/Stable_V5.0/en/qgc-user-guide/setup_view/camera.html"
upstream_repo: "mavlink/qgroundcontrol"
upstream_path: "setup_view/camera.md"
upstream_commit: "cb6ee485e0e11c74ed667ca573e7593f770da436"
ingested: 2026-07-28
tags:
  - docs/qgc
  - docs/qgc/setup-view
---

# Camera Setup

The details of the page differ if you are using PX4 firmware or ArduPilot firmware.

## ArduPilot Camera Setup

![](https://raw.githubusercontent.com/mavlink/qgroundcontrol/Stable_V5.0/docs/assets/setup/ardupilot_camera.jpg)

## PX4 Camera Setup

![PX4 Camera setup](https://raw.githubusercontent.com/mavlink/qgroundcontrol/Stable_V5.0/docs/assets/setup/px4_camera.jpg)

For more information see [Camera](http://docs.px4.io/main/en/peripherals/camera.html) (PX4 User Guide).

::: info
The camera settings section is not available by default for FMUv2-based flight controllers (e.g. 3DR Pixhawk) because the camera module is not automatically included in firmware.
For more information see [this topic](http://docs.px4.io/main/en/advanced_config/parameters.html#parameter-not-in-firmware).
:::
