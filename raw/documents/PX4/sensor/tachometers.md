---
title: "Tachometers (Revolution Counters)"
type: document
doc_set: PX4
doc_version: main
section: sensor
source_url: "https://docs.px4.io/main/en/sensor/tachometers"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "sensor/tachometers.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/sensor
---

# Tachometers (Revolution Counters)

Tachometers (also known as [revolution-counter sensors](https://en.wikipedia.org/wiki/Tachometer#In_automobiles,_trucks,_tractors_and_aircraft)) can be used to measure the rate of rotation turning vehicle parts like rotors, engines, or wheels.

::: info
Currently PX4 just logs RPM data: it is not used for state estimation or control.
:::

This section lists the tachometer sensors supported by PX4 (linked to more detailed documentation).
More detailed setup and configuration information is provided in the topics linked below (and sidebar).

![TFRPM01A](https://raw.githubusercontent.com/PX4/PX4-Autopilot/main/docs/assets/hardware/sensors/tfrpm/tfrpm01_electronics.jpg)

## Supported Hardware

- [ThunderFly TFRPM01 Tachometer](../sensor/thunderfly_tachometer.md)
