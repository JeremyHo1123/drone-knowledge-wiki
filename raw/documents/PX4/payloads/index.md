---
title: "Payloads and Cameras"
type: document
doc_set: PX4
doc_version: main
section: payloads
source_url: "https://docs.px4.io/main/en/payloads/"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "payloads/index.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/payloads
---

# Payloads and Cameras

Payloads are equipment carried by the vehicle to meet user or mission objectives.
PX4 supports a wide range of vehicle payloads, including cameras of various types, cargo, instrumentation, and so on.

Payloads are connected to [Flight Controller outputs](../getting_started/px4_basic_concepts.md#outputs-motors-servos-actuators), and can be triggered automatically in missions, manually from an RC Controller or Joystick, or from a Ground Station (via MAVLink/MAVSDK commands).

- [Payload Use Cases](../payloads/use_cases.md)
- [Package Delivery Mission](../flying/package_delivery_mission.md)
- [Generic Actuator Control](../payloads/generic_actuator_control.md)
- [Camera](../camera/index.md)
- [Gimbal \(Mount\) Configuration](../advanced/gimbal_control.md)
- [Grippers](../peripherals/gripper.md)
