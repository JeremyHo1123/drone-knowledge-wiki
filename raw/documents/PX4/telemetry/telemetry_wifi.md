---
title: "WiFi Telemetry Radio"
type: document
doc_set: PX4
doc_version: main
section: telemetry
source_url: "https://docs.px4.io/main/en/telemetry/telemetry_wifi"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "telemetry/telemetry_wifi.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/telemetry
---

# WiFi Telemetry Radio

WiFi telemetry enables MAVLink communication between a WiFi radio on a vehicle and a GCS.  
WiFi typically offers shorter range than a normal telemetry radio, but supports higher data rates, and makes it easier to support FPV/video feeds.
Usually only a single radio unit for the vehicle is needed (assuming the ground station already has WiFi).

PX4 supports telemetry via UDP and Wifi. It broadcasts a heartbeat to port 14550 on 255.255.255.255 until it receives the first heartbeat from a ground control station, at which point it will only send data to this ground control station.

Compatible WiFi Telemetry modules include:

- [ESP8266 WiFi Module](../telemetry/esp8266_wifi_module.md)
- [ESP32 WiFi Module](../telemetry/esp32_wifi_module.md)
- [3DR Telemetry Wifi](../telemetry/3dr_telemetry_wifi.md) (Discontinued)
