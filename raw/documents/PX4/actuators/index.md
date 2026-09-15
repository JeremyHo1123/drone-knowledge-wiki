---
title: "Actuators"
type: document
doc_set: PX4
doc_version: main
section: actuators
source_url: "https://docs.px4.io/main/en/actuators/"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "actuators/index.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/actuators
---

# Actuators

This section contains topics about the core actuators used for flight control (ESC/motors, and servos), and how they are assigned to the flight controller outputs, configured, and calibrated.

- [Actuator Allocation](../config/actuators.md) — Configure flight controller outputs for specific functions and ESC/servo types.

- [ESCs & Motors](../peripherals/esc_motors.md) — ESCs such as [DShot](../peripherals/dshot.md) (recommended) and DroneCAN.
- [ESC Calibration](../advanced_config/esc_calibration.md) — Calibration for PWM ESC (not required for DShot/CAN ESC/servos).

## See Also

- [Peripherals](../peripherals/index.md) - includes non-core actuators such as grippers, parachutes, etc.
