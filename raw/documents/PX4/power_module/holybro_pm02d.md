---
title: "Holybro PM02D Power Module"
type: document
doc_set: PX4
doc_version: main
section: power_module
source_url: "https://docs.px4.io/main/en/power_module/holybro_pm02d"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "power_module/holybro_pm02d.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/power-module
---

# Holybro PM02D Power Module

The Holybro PM02D digital power module provides regulated power to flight controller and power distribution board, and sends information to the autopilot about battery voltage and current supplied to the flight controller and the motors.

The power module is connected using the I2C protocol.
It is designed for flight controllers based on the Pixhawk FMUv5X and FMUv6X open standard, including the [Pixhawk 5X](../flight_controller/pixhawk5x.md).

::: info
The PM is **NOT** compatible with flight controllers that require an analog power module, including: [Pixhawk 4](../flight_controller/pixhawk4.md), [Durandal](../flight_controller/durandal.md), [Pix32 v5](../flight_controller/holybro_pix32_v5.md), etc.
:::

![PM02D](https://raw.githubusercontent.com/PX4/PX4-Autopilot/main/docs/assets/hardware/power_module/holybro_pm02d/pm02d_hero.jpg)

## Specifications

- **Max input voltage**: 36V
- **Rated current**: 60A
- **Max current**: 120A (<60S)
- **Max current sensing**: 164A
- **Battery supported**: up to 6S battery
- **Communication protocol**: I2C
- **Switching regulator outputs**: 5.2V and 3A max
- **Weight**: 20g
- **IC Used**: TI INA228

## Package Contents

- PM02D board with XT60 connectors
- 6pin 2.00mm pitch CLIK-Mate cable to power flight controller

## Where to Buy

[Order from Holybro Store](https://holybro.com/products/pm02d-power-module)

## Wiring/Connections

![pm02d_pinout](https://raw.githubusercontent.com/PX4/PX4-Autopilot/main/docs/assets/hardware/power_module/holybro_pm02d/pm02d_pinout.png)

Additional wiring and connection information can be found in: [Holybro Pixhawk 5x Wiring Quick Start](../assembly/quick_start_pixhawk5x.md).

## PX4 Configuration

Enable parameter [SENS_EN_INA228](../advanced_config/parameter_reference.md#SENS_EN_INA228)

::: warning
There is an out-of-production low voltage version (6S) of this module with the same name, which uses the TI INA226 IC.
For this module you must instead enable parameter [SENS_EN_INA226](../advanced_config/parameter_reference.md#SENS_EN_INA226).
:::

Note that the current divider and voltage divider should not be set in the [Battery Configuration](../config/battery.md) (the default values are accurate within 5%).

## See Also

- [Digital Power Module (PM) Setup](https://docs.holybro.com/power-module-and-pdb/power-module/digital-power-module-pm-setup#px4-setup) (Manufacturer guide)
