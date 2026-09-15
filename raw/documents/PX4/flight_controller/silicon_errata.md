---
title: "Silicon Errata"
type: document
doc_set: PX4
doc_version: main
section: flight_controller
source_url: "https://docs.px4.io/main/en/flight_controller/silicon_errata"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "flight_controller/silicon_errata.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/flight-controller
---

# Silicon Errata

This page lists known issues with silicon (hardware) errata of 3rd-party parts (micro controller, sensors, etc.) used on the Pixhawk board series. Depending on the type of silicon error, these cannot be fixed in software and might impose specific limitations.

## FMUv2 / Pixhawk Silicon Errata

### STM32F427VIT6 (errata)

Flash Bank 2 and full speed USB device exclusive.

Silicon revisions up to rev 2 (revision 3 is the first not affected) can produce errors / data corruption when accessing the 2nd flash bank while there is activity on PA12, which is one of the USB data lines. There is no workaround / software fix for this, except to not use the flash bank #2.
Since USB is needed to program the device, Pixhawk revisions built with silicon revisions < rev 3 can only use up to 1MB of the 2MB flash of the microprocessor.

::: tip
The errata is fixed in later versions, but this may not be detected if you are using an older bootloader.
See [Firmware > FMUv2 Bootloader Update](../config/firmware.md#bootloader) for more information.
:::

## FMUv1 / Pixhawk Silicon Errata

No known issues.
