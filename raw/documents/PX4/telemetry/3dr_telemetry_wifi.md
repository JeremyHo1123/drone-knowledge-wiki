---
title: "3DR WiFi Telemetry (Discontinued)"
type: document
doc_set: PX4
doc_version: main
section: telemetry
source_url: "https://docs.px4.io/main/en/telemetry/3dr_telemetry_wifi"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "telemetry/3dr_telemetry_wifi.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/telemetry
---

# 3DR WiFi Telemetry (Discontinued)

::: info
This product is no longer manufactured or available from 3DR.
:::

The _3DR WiFi Telemetry Radio_ is supported by PX4.
Simply connect it to the flight controller's `TELEM1` port to create a WiFi "hotspot" for the vehicle with the details below:

```sh
essid: APM_PIX
password: 12345678
```

Connect your ground control station to the above WiFi SSID.
After connecting the vehicle should automatically be detected and connect to _QGroundControl_.

![3DR Wifi Telemetry Radio 1](https://raw.githubusercontent.com/PX4/PX4-Autopilot/main/docs/assets/hardware/telemetry/3dr_telemetry_wifi_1.jpg)
![3DR Wifi Telemetry Radio 2](https://raw.githubusercontent.com/PX4/PX4-Autopilot/main/docs/assets/hardware/telemetry/3dr_telemetry_wifi_2.jpg)
