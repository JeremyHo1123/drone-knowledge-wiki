---
title: "Lanbao PSK-CM8JL65-CC5 ToF Infrared Distance Measuring Sensor (Discontinued)"
type: document
doc_set: PX4
doc_version: main
section: sensor
source_url: "https://docs.px4.io/main/en/sensor/cm8jl65_ir_distance_sensor"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "sensor/cm8jl65_ir_distance_sensor.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/sensor
---

# Lanbao PSK-CM8JL65-CC5 ToF Infrared Distance Measuring Sensor (Discontinued)

<Badge type="info" text="Discontinued" />

:::warning
This product has been discontinued and is no longer commercially available.
:::

The [Lanbao PSK-CM8JL65-CC5](https://www.seeedstudio.com/PSK-CM8JL65-CC5-Infrared-Distance-Measuring-Sensor-p-4028.html) is a very small IR distance sensor with a 0.17m-8m range and millimeter resolution.
It must be connected to a UART/serial bus.

- Dimensions: 38 mm x 18mm x 7mm
- Weight: ≤10g

![PSK-CM8JL65-CC5 ToF IR Distance Sensor - Hero image](https://raw.githubusercontent.com/PX4/PX4-Autopilot/main/docs/assets/hardware/sensors/cm8jl65/psk_cm8jl65_hero.jpg)

## Hardware Setup

PSK-CM8JL65-CC5 can be connected to any unused _serial port_, e.g.: `TELEM2`, `TELEM3`, `GPS2` etc.

The pinouts are labeled on the bottom of the sensor:

![PSK-CM8JL65-CC5 ToF IR Distance Sensor - Pinout connections](https://raw.githubusercontent.com/PX4/PX4-Autopilot/main/docs/assets/hardware/sensors/cm8jl65/psk-cm8jl65-cc5-02.jpg)

## Parameter Setup

[Configure the serial port](../peripherals/serial_configuration.md) on which the lidar will run using [SENS_CM8JL65_CFG](../advanced_config/parameter_reference.md#SENS_CM8JL65_CFG).

::: info
If the configuration parameter is not available in _QGroundControl_ then you may need to [add the driver to the firmware](../peripherals/serial_configuration.md#parameter_not_in_firmware):

```plain
distance_sensor/cm8jl65
```

:::

In order to use the sensor for _collision prevention_ you will further need to set the parameters [SENS_CM8JL65_R_0](../advanced_config/parameter_reference.md#SENS_CM8JL65_R_0) and [CP_DIST](../advanced_config/parameter_reference.md#CP_DIST).
For more information see: [Collision Prevention](../computer_vision/collision_prevention.md#rangefinder).
