---
title: "SiK Radio"
type: document
doc_set: PX4
doc_version: main
section: telemetry
source_url: "https://docs.px4.io/main/en/telemetry/sik_radio"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "telemetry/sik_radio.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/telemetry
---

# SiK Radio

[SiK radio](https://github.com/LorenzMeier/SiK) is a collection of firmware and tools for telemetry radios.

PX4 is protocol-compatible with radios that use _SiK_.
SiK Radios often come with appropriate connectors/cables allowing them to be directly connected to [Pixhawk Series](../flight_controller/pixhawk_series.md) controllers
(in some cases you may need to obtain an appropriate cable/connector).
Typically you will need a pair of devices - one for the vehicle and one for the ground station.

Hardware for the SiK radio can be obtained from various manufacturers/stores in variants that support different range and form factors.

![SiK Radio](https://raw.githubusercontent.com/PX4/PX4-Autopilot/main/docs/assets/hardware/telemetry/holybro_sik_radio.jpg)

## Vendors

- [Holybro Telemetry Radio](../telemetry/holybro_sik_radio.md)
- [HolyBro SiK Long Range](../telemetry/holybro_sik_longrange.md)
- [RFD900 Telemetry Radio](../telemetry/rfd900_telemetry.md)
- [ThunderFly TFSIK01 Telemetry Radio](../telemetry/tfsik_telemetry.md)
- <del>_HKPilot Telemetry Radio_</del> (Discontinued)
- <del>_3DR Telemetry Radio_</del> (Discontinued)

## Setup/Configuration

The ground station-based radio is connected via USB (essentially plug-n-play).

The vehicle-based radio is connected to the flight-controller's `TELEM1` port, and typically requires no further configuration.

## Firmware Update

Hardware sourced from most [vendors](#vendors) should come pre-configured with the latest firmware.
You may need to update older hardware with new firmware, for example to gain support for MAVLink 2.

You can update the radio firmware using _QGroundControl_: [QGroundControl User Guide > Loading Firmware](https://docs.qgroundcontrol.com/master/en/qgc-user-guide/setup_view/firmware.html).

## Advanced Setup/Configuration

The Development section has [additional information](../data_links/sik_radio.md) about building firmware and AT-command based configuration.
This should not be required by non-developers.
