---
title: "Holybro Micro Power Module (PM06)"
type: document
doc_set: PX4
doc_version: main
section: power_module
source_url: "https://docs.px4.io/main/en/power_module/holybro_pm06_pixhawk4mini_power_module"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "power_module/holybro_pm06_pixhawk4mini_power_module.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/power-module
---

# Holybro Micro Power Module (PM06)

This power module has integrated power distribution board and provides regulated power for a flight controller and ESCs, and sends information to the autopilot about the battery’s voltage and current draw.

![PM06](https://raw.githubusercontent.com/PX4/PX4-Autopilot/main/docs/assets/hardware/power_module/holybro_pm06_14s/pm06v2_pm06v2-14s.jpg)

## Specifications

- **PCB Current:** 120A continued
- **UBEC Current:** 3A Max
- **Power input:** 2S~10S (standard version)
- **Power input:** 2S~14S (14S version)
- **Power output:** DC 5.1V~5.3V
- **Voltage Divider:** 18.182
- **Amperes per Volt:** 36.364

## Mechanical Specifications

- **Dimensions:** 35x35x5mm
- **Mounting hole:** 30.5mm\*30.5mm
- **Weight:** 24g

## Where to Buy

[PM06 V2 Power Module](https://holybro.com/collections/power-modules-pdbs/products/micro-power-module-pm06-v2)

## Wiring/Connections

![pm06_pin_map](https://raw.githubusercontent.com/PX4/PX4-Autopilot/main/docs/assets/hardware/power_module/holybro_pm06/pm06_pin_map.jpg)

This image shows the wiring and connections for the [Pixhawk 4 Mini](https://docs.px4.io/v1.16/en/assembly/quick_start_pixhawk4_mini#power) (discontinued).

![Pixhawk 4 - Power Management Board](https://raw.githubusercontent.com/PX4/PX4-Autopilot/main/docs/assets/hardware/power_module/holybro_pm06/pixhawk4mini_power_management.png)
