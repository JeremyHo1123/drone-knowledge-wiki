---
title: "Holybro PM02 (V3) Power Module"
type: document
doc_set: PX4
doc_version: main
section: power_module
source_url: "https://docs.px4.io/main/en/power_module/holybro_pm02"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "power_module/holybro_pm02.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/power-module
---

# Holybro PM02 (V3) Power Module

This analog power module provides regulated power to flight controller and power distribution board, and sends information to the autopilot about battery voltage and current supplied to the flight controller and the motors.
It is commonly used with [Pixhawk 4](../assembly/quick_start_pixhawk4.md).

::: info
The module can be used with other flight controllers that require an analog power module, including [Durandal](../flight_controller/durandal.md), [Pix32 v5](../flight_controller/holybro_pix32_v5.md), etc
:::

![Holybro PM02](https://raw.githubusercontent.com/PX4/PX4-Autopilot/main/docs/assets/hardware/power_module/holybro_pm02/pm02.jpg)

## Specifications

- **Rated current**: 60A
- **Max current**: 120A (<60 Sec)
- **Max current sensing**: 120A
- **Battery supported**: up to 12S battery
- **Communication protocol**: Analog
- **Switching regulator outputs**: 5.2V and 3A max
- **Weight**: 20g

Voltage and current measurement configured for 3.3V ADC

## Package Contents

- Power Module with XT60 Connector Board
- Electrolytic capacito: 220uF 63V (pre-installed)
- Molex 6 Position Connector 15 cm
- GH 6 Position Connector 15 cm

## Where to Buy

[Order from Holybro Store](https://holybro.com/collections/power-modules-pdbs/products/pm02-v3-12s-power-module)

## Wiring/Connections

Additional wiring and connection information can be found in: [Pixhawk 4 QuickStart](../assembly/quick_start_pixhawk4.md).
