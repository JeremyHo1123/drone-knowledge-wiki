---
title: "Modules Reference: Optical Flow (Driver)"
type: document
doc_set: PX4
doc_version: main
section: modules
source_url: "https://docs.px4.io/main/en/modules/modules_driver_optical_flow"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "modules/modules_driver_optical_flow.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/modules
---

# Modules Reference: Optical Flow (Driver)

## thoneflow

Source: [drivers/optical_flow/thoneflow](https://github.com/PX4/PX4-Autopilot/tree/main/src/drivers/optical_flow/thoneflow)

### Description

Serial bus driver for the ThoneFlow-3901U optical flow sensor.

Most boards are configured to enable/start the driver on a specified UART using the SENS_TFLOW_CFG parameter.

Setup/usage information: https://docs.px4.io/main/en/sensor/pmw3901.html#thone-thoneflow-3901u

### Examples

Attempt to start driver on a specified serial device.

```
thoneflow start -d /dev/ttyS1
```

Stop driver

```
thoneflow stop
```

### Usage {#thoneflow_usage}

```
thoneflow <command> [arguments...]
 Commands:
   start         Start driver
     -d <val>    Serial device

   stop          Stop driver

   info          Print driver information
```
