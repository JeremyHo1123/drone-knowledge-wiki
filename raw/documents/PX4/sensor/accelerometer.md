---
title: "Accelerometer Hardware & Setup"
type: document
doc_set: PX4
doc_version: main
section: sensor
source_url: "https://docs.px4.io/main/en/sensor/accelerometer"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "sensor/accelerometer.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/sensor
---

# Accelerometer Hardware & Setup

PX4 uses accelerometer data for velocity estimation.

You should not need to attach an accelometer as a stand-alone external device:

- Most flight controllers, such as those in the [Pixhawk Series](../flight_controller/pixhawk_series.md), include an accelerometer as part of the flight controller's [Inertial Motion Unit (IMU)](https://en.wikipedia.org/wiki/Inertial_measurement_unit).
- Gyroscopes are present as part of an [external INS, AHRS or INS-enhanced GNSS system](../sensor/inertial_navigation_systems.md).

The accelerometer must be calibrated before first use of the vehicle:

- [Accelerometer Calibration](../config/accelerometer.md)
