---
title: "Telemetry Radio/Modem Integration"
type: document
doc_set: PX4
doc_version: main
section: data_links
source_url: "https://docs.px4.io/main/en/data_links/telemetry"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "data_links/telemetry.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/data-links
---

# Telemetry Radio/Modem Integration

Telemetry Radios can (optionally) be used to provide a wireless MAVLink connection between a ground control station like _QGroundControl_ and a vehicle running PX4.
This section contains topics about advanced use of supported radios and integrating new telemetry systems into PX4.

:::tip
[Peripheral Hardware > Telemetry Radios](../telemetry/index.md) contains information about telemetry radio systems already supported by PX4.
This includes radios that use the _SiK Radio_ firmware and _3DR WiFi Telemetry Radios_.
:::

## Integrating Telemetry Systems

PX4 enables MAVLink-based telemetry via the telemetry port of a Pixhawk-based flight controller.
Provided that a telemetry radio supports MAVLink and provides a UART interface with compatible voltage levels/connector, no further integration is required.

Telemetry systems that communicate using some other protocol will need more extensive integration, potentially covering both software (e.g. device drivers) and hardware (connectors etc.).
While this has been done for specific cases (e.g. [FrSky Telemetry](../peripherals/frsky_telemetry.md) enables sending vehicle status to an RC controller via an FrSky receiver) providing general advice is difficult.
We recommend you start by [discussing with the development team](../contribute/support.md).
