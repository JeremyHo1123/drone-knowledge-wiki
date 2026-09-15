---
title: "Modules Reference: Adc (Driver)"
type: document
doc_set: PX4
doc_version: main
section: modules
source_url: "https://docs.px4.io/main/en/modules/modules_driver_adc"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "modules/modules_driver_adc.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/modules
---

# Modules Reference: Adc (Driver)

## ADS7128

Source: [drivers/adc/ads7128](https://github.com/PX4/PX4-Autopilot/tree/main/src/drivers/adc/ads7128)

### Usage {#ADS7128_usage}

```
ADS7128 <command> [arguments...]
 Commands:
   start
     [-I]        Internal I2C bus(es)
     [-X]        External I2C bus(es)
     [-b <val>]  board-specific bus (default=all) (external SPI: n-th bus
                 (default=1))
     [-f <val>]  bus frequency in kHz
     [-q]        quiet startup (no message if no device found)
     [-a <val>]  I2C address
                 default: 16

   stop

   status        print status info
```

## TLA2528

Source: [drivers/adc/tla2528](https://github.com/PX4/PX4-Autopilot/tree/main/src/drivers/adc/tla2528)

### Usage {#TLA2528_usage}

```
TLA2528 <command> [arguments...]
 Commands:
   start
     [-I]        Internal I2C bus(es)
     [-X]        External I2C bus(es)
     [-b <val>]  board-specific bus (default=all) (external SPI: n-th bus
                 (default=1))
     [-f <val>]  bus frequency in kHz
     [-q]        quiet startup (no message if no device found)

   stop

   status        print status info
```

## adc

Source: [drivers/adc/board_adc](https://github.com/PX4/PX4-Autopilot/tree/main/src/drivers/adc/board_adc)

### Description

ADC driver.

### Usage {#adc_usage}

```
adc <command> [arguments...]
 Commands:
   start

   test
     [-n]        Do not publish ADC report, only system power

   stop

   status        print status info
```

## ads1115

Source: [drivers/adc/ads1115](https://github.com/PX4/PX4-Autopilot/tree/main/src/drivers/adc/ads1115)

### Description

Driver to enable an external [ADS1115](https://www.adafruit.com/product/1085) ADC connected via I2C.

The driver is included by default in firmware for boards that do not have an internal analog to digital converter,
such as [PilotPi](../flight_controller/raspberry_pi_pilotpi.md) or [CUAV Nora](../flight_controller/cuav_nora.md)
(search for `CONFIG_DRIVERS_ADC_ADS1115` in board configuration files).

It is enabled/disabled using the
[ADC_ADS1115_EN](../advanced_config/parameter_reference.md#ADC_ADS1115_EN)
parameter, and is disabled by default.
If enabled, internal ADCs are not used.

### Usage {#ads1115_usage}

```
ads1115 <command> [arguments...]
 Commands:
   start
     [-I]        Internal I2C bus(es)
     [-X]        External I2C bus(es)
     [-b <val>]  board-specific bus (default=all) (external SPI: n-th bus
                 (default=1))
     [-f <val>]  bus frequency in kHz
     [-q]        quiet startup (no message if no device found)
     [-a <val>]  I2C address
                 default: 72

   stop

   status        print status info
```

## ads7953

Source: [drivers/adc/ads7953](https://github.com/PX4/PX4-Autopilot/tree/main/src/drivers/adc/ads7953)

### Usage {#ads7953_usage}

```
ads7953 <command> [arguments...]
 Commands:
   start
     [-s]        Internal SPI bus(es)
     [-S]        External SPI bus(es)
     [-b <val>]  board-specific bus (default=all) (external SPI: n-th bus
                 (default=1))
     [-c <val>]  chip-select pin (for internal SPI) or index (for external SPI)
     [-m <val>]  SPI mode
     [-f <val>]  bus frequency in kHz
     [-q]        quiet startup (no message if no device found)

   stop

   status        print status info
```
