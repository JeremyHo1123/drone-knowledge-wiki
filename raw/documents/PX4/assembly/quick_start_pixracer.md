---
title: "Pixracer Wiring Quick Start"
type: document
doc_set: PX4
doc_version: main
section: assembly
source_url: "https://docs.px4.io/main/en/assembly/quick_start_pixracer"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "assembly/quick_start_pixracer.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/assembly
---

# Pixracer Wiring Quick Start

:::warning
PX4 does not manufacture this (or any) autopilot.
Contact the [manufacturer](https://store.mrobotics.io/) for hardware support or compliance issues.
:::

:::warning
Under construction
:::

This quick start guide shows how to power the [Pixracer](../flight_controller/pixracer.md) flight controller and connect its most important peripherals.

<img src="https://raw.githubusercontent.com/PX4/PX4-Autopilot/main/docs/assets/flight_controller/pixracer/pixracer_hero_grey.jpg" width="300px" title="pixracer + 8266 grey" />

## Wiring Guides/Assembly

![Grau pixracer double](https://raw.githubusercontent.com/PX4/PX4-Autopilot/main/docs/assets/flight_controller/pixracer/grau_pixracer_double.jpg)

### Main Setup

![Grau setup pixracer top](https://raw.githubusercontent.com/PX4/PX4-Autopilot/main/docs/assets/flight_controller/pixracer/grau_setup_pixracer_top.jpg)

![Grau setup pixracer bottom](https://raw.githubusercontent.com/PX4/PX4-Autopilot/main/docs/assets/flight_controller/pixracer/grau_setup_pixracer_bottom.jpg)

### Radio/Remote Control

A remote control (RC) radio system is required if you want to _manually_ control your vehicle (PX4 does not require a radio system for autonomous flight modes).

You will need to [select a compatible transmitter/receiver](../getting_started/rc_transmitter_receiver.md) and then _bind_ them so that they communicate (read the instructions that come with your specific transmitter/receiver).

The instructions below show how to connect the different types of receivers:

- FrSky receivers connect via the port shown, and can use the provided I/O Connector.

  ![Grau b Pixracer FrSkyS.Port Connection](https://raw.githubusercontent.com/PX4/PX4-Autopilot/main/docs/assets/flight_controller/pixracer/grau_b_pixracer_frskys.port_connection.jpg)

  ![Pixracer FrSkyS.Port Connection](https://raw.githubusercontent.com/PX4/PX4-Autopilot/main/docs/assets/flight_controller/pixracer/pixracer_FrSkyTelemetry.jpg)

- PPM-SUM and S.BUS receivers connect to the **RCIN** port.

  ![Radio Connection](https://raw.githubusercontent.com/PX4/PX4-Autopilot/main/docs/assets/flight_controller/pixracer/grau_setup_pixracer_radio.jpg)

- PPM and PWM receivers that have an _individual wire for each channel_ must connect to the **RCIN** port _via a PPM encoder_ [like this one](https://www.getfpv.com/radios/radio-accessories/holybro-ppm-encoder-module.html) (PPM-Sum receivers use a single signal wire for all channels).

### Power Module (ACSP4)

![Grau ACSP4 2 roh](https://raw.githubusercontent.com/PX4/PX4-Autopilot/main/docs/assets/flight_controller/pixracer/grau_acsp4_2_roh.jpg)

### External Telemetry

Pixracer has inbuilt WiFi, but also supports telemetry via external Wi-Fi or radio telemetry modules connected to the `TELEM1` or `TELEM2` ports.
This is shown in the wiring diagram below.

![Pixracer external telemetry options](https://raw.githubusercontent.com/PX4/PX4-Autopilot/main/docs/assets/flight_controller/pixracer/pixracer_top_telemetry.jpg)

::: info
The `TELEM2` port must be configured as a second MAVLink instance using the [MAV_2_CONFIG](../advanced_config/parameter_reference.md#MAV_2_CONFIG) parameter.
For more information see [MAVLink Peripherals > MAVLink Instances](../peripherals/mavlink_peripherals.md#mavlink-instances) (and [Serial Port Configuration](../peripherals/serial_configuration.md)).
:::
