---
title: "Modules Reference: Transponder (Driver)"
type: document
doc_set: PX4
doc_version: main
section: modules
source_url: "https://docs.px4.io/main/en/modules/modules_driver_transponder"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "modules/modules_driver_transponder.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/modules
---

# Modules Reference: Transponder (Driver)

## sagetech_mxs

Source: [drivers/transponder/sagetech_mxs](https://github.com/PX4/PX4-Autopilot/tree/main/src/drivers/transponder/sagetech_mxs)

    ### Description

    This driver integrates the Sagetech MXS Certified Transponder to send and receive ADSB messages and traffic.

    ### Examples

    Attempt to start driver on a specified serial device.
    $ sagetech_mxs start -d /dev/ttyS1
    Stop driver
    $ sagetech_mxs stop
    Set Flight ID (8 char max)
    $ sagetech_mxs flight_id MXS12345
    Set MXS Operating Mode
    $ sagetech_mxs opmode off/on/stby/alt
    $ sagetech_mxs opmode 0/1/2/3
    Set the Squawk Code
    $ sagetech_mxs squawk 1200

### Usage {#sagetech_mxs_usage}

```
sagetech_mxs <command> [arguments...]
 Commands:
   start         Start driver
     -d <val>    Serial device

   stop          Stop driver

   flightid      Set Flight ID (8 char max)

   ident         Set the IDENT bit in ADSB-Out messages

   opmode        Set the MXS operating mode. ('off', 'on', 'stby', 'alt', or
                 numerical [0-3])

   squawk        Set the Squawk Code. [0-7777] Octal (no digit larger than 7)
```
