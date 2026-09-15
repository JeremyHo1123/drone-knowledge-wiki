---
title: "LeddarOne Lidar"
type: document
doc_set: PX4
doc_version: main
section: sensor
source_url: "https://docs.px4.io/main/en/sensor/leddar_one"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "sensor/leddar_one.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/sensor
---

# LeddarOne Lidar

[LeddarOne](https://leddartech.com/solutions/leddarone/) is small Lidar module with a narrow, yet diffuse beam that offers excellent overall detection range and performance, in a robust, reliable, cost-effective package.
It has a sensing range from 1cm to 40m and needs to be connected to a UART/serial bus.

<img src="https://raw.githubusercontent.com/PX4/PX4-Autopilot/main/docs/assets/hardware/sensors/leddar_one.jpg" alt="LeddarOne Lidar rangefinder" width="200px" />

## Hardware Setup

LeddarOne can be connected to any unused _serial port_ (UART), e.g.: TELEM2, TELEM3, GPS2 etc.

Build a cable following your board and pinout and LeddarOne pinout (shown below). You only will need to connect 5V, TX, RX and GND pins.

| Pin | LeddarOne |
| --- | --------- |
| 1   | GND       |
| 2   | -         |
| 3   | VCC       |
| 4   | RX        |
| 5   | TX        |
| 6   | -         |

## Parameter Setup

[Configure the serial port](../peripherals/serial_configuration.md) on which the lidar will run using [SENS_LEDDAR1_CFG](../advanced_config/parameter_reference.md#SENS_LEDDAR1_CFG).
There is no need to set the baud rate for the port, as this is configured by the driver.

::: info
If the configuration parameter is not available in _QGroundControl_ then you may need to [add the driver to the firmware](../peripherals/serial_configuration.md#parameter_not_in_firmware):

```plain
CONFIG_DRIVERS_DISTANCE_SENSOR_LEDDAR_ONE=y
```

:::

## Further Information

- [LeddarOne Spec sheet](https://leddartech.com/download/specsheet-leddarone-single-element-sensor-module/pdf_file.pdf)
