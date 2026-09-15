---
title: "CUAV HV PM (High-Voltage Power Module)"
type: document
doc_set: PX4
doc_version: main
section: power_module
source_url: "https://docs.px4.io/main/en/power_module/cuav_hv_pm"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "power_module/cuav_hv_pm.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/power-module
---

# CUAV HV PM (High-Voltage Power Module)

The CUAV<sup>&reg;</sup> _HV_PM_ power module is a "high voltage" power module independently developed by CUAV.

:::tip
The _HV_PM_ is included in the CUAV V5+/V5 nano kit, but is also be sold separately.
There are different cables depending on the flight controller (Pixhack v3, V5+/V5 nano, Pixhawk).
It can be used with other flight controllers, but you may need to modify the cable pin.
:::

## Specifications

- **Higher voltage input:** 10V-60V (3s~14s battery)
- **Accurate battery monitor:**
  - **Voltage detection accuracy:** +-0.1v;
  - **Current detection accuracy:** +-0.2A
- **BEC (5v) max current:** 5A
- **Max (detection) current:** 60A
- **Max output current (ESC/MOTOR PORT):** 60A

## Where to Buy

[CUAV aliexpress store](https://www.aliexpress.com/item/32841805115.html?spm=2114.12010615.8148356.1.64165998hPvTKQ)

## Pinouts

![HV PM](https://raw.githubusercontent.com/PX4/PX4-Autopilot/main/docs/assets/hardware/power_module/cuav_hv/hv_pm.jpg)

## Enable HV PM

[Battery Estimation Tuning](../config/battery.md) describes how to configure the battery and power module.

The key configuration settings for `HV_PM` are:

- **Voltage divider:** 18
- **Amps per volt:** 24 A/V
