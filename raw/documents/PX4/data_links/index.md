---
title: "Data Links"
type: document
doc_set: PX4
doc_version: main
section: data_links
source_url: "https://docs.px4.io/main/en/data_links/"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "data_links/index.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/data-links
---

# Data Links

Data links are radio channels that are used to communicate vehicle telemetry (position, velocity, battery status, and so on) from the flight controller to ground control stations (and to some RC systems), and commands from ground stations to the vehicle.
These links are usually created using different radios than those used for manual RC control of the vehicle.
PX4 uses the [MAVLink](https://mavlink.io/en/) protocol for communicating serial data over the radio channel.

This section provides information about various radio systems that you can use, and how to configure them for use with PX4.

- [MAVLink Telemetry (OSD/GCS)](../peripherals/mavlink_peripherals.md) — Configuring autopilot outputs for telemetry
- [Telemetry Radios](../telemetry/index.md) — Popular protocols and radio systems for data links
- [FrSky Telemetry](../peripherals/frsky_telemetry.md) — Telemetry on your (FRSky) RC Receiver
- [TBS Crossfire (CRSF) Telemetry](../telemetry/crsf_telemetry.md) — Telemetry on your (TBS Crossfire) RC Receiver
- [Satellite Comms (Iridium/RockBlock)](../advanced_features/satcom_roadblock.md) — High-latency comms via satellite

## See Also

- [Safety Configuration > Data Link Loss Failsafe](../config/safety.md#data-link-loss-failsafe)
