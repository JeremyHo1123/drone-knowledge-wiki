---
title: "VTOL Configuration"
type: document
doc_set: PX4
doc_version: main
section: config_vtol
source_url: "https://docs.px4.io/main/en/config_vtol/"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "config_vtol/index.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/config-vtol
---

# VTOL Configuration

First perform the [Standard Configuration](../config/index.md).
As part of this you should calibrate the [Airspeed sensor](../config/airspeed.md) (optional, but highly recommended) and [assign a VTOL transition switch](../config/flight_mode.md#what-flight-modes-and-switches-should-i-set) to your RC controller.

Then perform VTOL-specific configuration and tuning:

- [QuadPlane Configuration](../config_vtol/vtol_quad_configuration.md)
- [Back-transition Tuning](../config_vtol/vtol_back_transition_tuning.md)
- [VTOL w/o Airspeed Sensor](../config_vtol/vtol_without_airspeed_sensor.md)
- [VTOL Weather Vane](../config_vtol/vtol_weathervane.md)
- [Ice Shedding](../config_vtol/vtol_ice_shedding.md)
