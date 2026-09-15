---
title: "RFD900 Long-Range Telemetry"
type: document
doc_set: PX4
doc_version: main
section: telemetry
source_url: "https://docs.px4.io/main/en/telemetry/rfd900_telemetry"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "telemetry/rfd900_telemetry.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/telemetry
---

# RFD900 Long-Range Telemetry

[RFDesign](https://rfdesign.com.au/) offers _long-range_ [SiK](../telemetry/sik_radio.md)-compatible telemetry radios.
The radios provide reliable connectivity at greater than 5km ranges with normal antennas (and have been reported to achieve much greater ranges).

![RFDesign Long Range Telemetry](https://raw.githubusercontent.com/PX4/PX4-Autopilot/main/docs/assets/hardware/telemetry/jdrones_long_range_uav_telemetry_rf900set02_2.jpg)

The raw modems expose bare pin headers, multiple vendors—along with _RFDesign_ themselves—offer productized versions.
Depending on your region and target deployment, several turn-key solutions and regional bundles are available:

- **Official RFDesign Store:**
  - [RFD900x Modem (915MHz - Americas/APAC)](https://store.rfdesign.com.au/rfd-900x-modem/)
  - [RFD868x Modem (868MHz - Europe)](https://store.rfdesign.com.au/rfd868x-eu-hs-8517-62-00-90/)

- **Productized Enclosures & Bundles:**
  - [Bask Aerospace AeroLink System](https://baskaerospace.com.au/products/aerolink/) (Rugged, weather-resistant base station and drone adapters)
  - [IR-Lock RFD900x TXMOD V2 Bundle](https://irlock.com/products/rfd900-txmod-bundle) (Complete ground-to-air transmitter kit)
