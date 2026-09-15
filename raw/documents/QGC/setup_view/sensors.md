---
title: "Sensors"
type: document
doc_set: QGC
doc_version: Stable_V5.0
section: setup_view
source_url: "https://docs.qgroundcontrol.com/Stable_V5.0/en/qgc-user-guide/setup_view/sensors.html"
upstream_repo: "mavlink/qgroundcontrol"
upstream_path: "setup_view/sensors.md"
upstream_commit: "cb6ee485e0e11c74ed667ca573e7593f770da436"
ingested: 2026-07-28
tags:
  - docs/qgc
  - docs/qgc/setup-view
---

# Sensors

The _Sensor Setup_ section allows you to configure and calibrate the vehicle's compass, gyroscope, accelerometer and any other sensors
(the available sensors will depend on the autopilot firmware and vehicle type).

Available sensors are displayed as a list of buttons beside the sidebar.
Sensors marked with green are already calibrated, while sensors marked with red require calibration prior to flight.
Sensors with no light are simple settings with default values that you may choose not to calibrate.

Click on the button for each sensor to start its calibration sequence.

Flight stack specific instructions are provided in the following topics:

- [Sensors (ArduPilot)](../setup_view/sensors_ardupilot.md)
- [Sensors (PX4)](../setup_view/sensors_px4.md)
