---
title: "Modules Reference: Rpm Sensor (Driver)"
type: document
doc_set: PX4
doc_version: main
section: modules
source_url: "https://docs.px4.io/main/en/modules/modules_driver_rpm_sensor"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "modules/modules_driver_rpm_sensor.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/modules
---

# Modules Reference: Rpm Sensor (Driver)

## pcf8583

Source: [drivers/rpm/pcf8583](https://github.com/PX4/PX4-Autopilot/tree/main/src/drivers/rpm/pcf8583)

### Usage {#pcf8583_usage}

```
pcf8583 <command> [arguments...]
 Commands:
   start
     [-I]        Internal I2C bus(es)
     [-X]        External I2C bus(es)
     [-b <val>]  board-specific bus (default=all) (external SPI: n-th bus
                 (default=1))
     [-f <val>]  bus frequency in kHz
     [-q]        quiet startup (no message if no device found)
     [-a <val>]  I2C address
                 default: 80
     [-k]        if initialization (probing) fails, keep retrying periodically

   stop

   status        print status info
```
