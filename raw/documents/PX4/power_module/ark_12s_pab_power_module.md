---
title: "ARK 12S PAB Power Module"
type: document
doc_set: PX4
doc_version: main
section: power_module
source_url: "https://docs.px4.io/main/en/power_module/ark_12s_pab_power_module"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "power_module/ark_12s_pab_power_module.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/power-module
---

# ARK 12S PAB Power Module

The [ARK 12S PAB Power Module](https://arkelectron.gitbook.io/ark-documentation/power/ark-12s-pab-power-module) is a 5V 6A power supply and digital power monitor designed for use with Pixhawk Autopilot Bus Carrier boards.

![ARK 12S PAB Power Module](https://raw.githubusercontent.com/PX4/PX4-Autopilot/main/docs/assets/hardware/power_module/ark_power_modules//ark_12s_pab_power_module.jpg)

## Where to Buy

Order this module from:

- [ARK Electronics](https://arkelectron.com/product/ark-12s-pab-power-module/) (US)

## Hardware Specifications

- **TI INA238 Digital Power Monitor**
  - 0.0001 Ohm Shunt
  - I2C Interface

- **5.2V 6A Step-Down Regulator**
  - 66V Maximum Input Voltage
  - 10V Minimum Input Voltage at 6A Out
  - Output Over-Current Protection

- **Connections**
  - Solder Pads Battery Input
  - Solder Pads Battery Output
  - 6 Pin Molex CLIK-Mate Output
    - [Matches ARK PAB Carrier Power Pinout](https://arkelectron.gitbook.io/ark-documentation/flight-controllers/ark-pixhawk-autopilot-bus-carrier/pinout)

- **Other**
  - USA Built
  - Includes 6 Pin Molex CLIK-Mate Cable

- **Additional Information**
  - Weight: 15.5 g
  - Dimensions: 3.7 cm x 2.2 cm x 1.3 cm

## PX4 Setup

- Disable the `SENS_EN_INA226` parameter if it is enabled.
- Enable the `SENS_EN_INA238` parameter.
- Reboot the flight controller.
- Set the `INA238_SHUNT` parameter to 0.0001.
- Reboot the flight controller.

## See Also

- [ARK 12S PAB Power Module Documentation](https://arkelectron.gitbook.io/ark-documentation/power/ark-12s-pab-power-module) (ARK Docs)
