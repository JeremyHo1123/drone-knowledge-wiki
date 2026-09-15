---
title: "Pixhawk Autopilot Bus & Carriers"
type: document
doc_set: PX4
doc_version: main
section: flight_controller
source_url: "https://docs.px4.io/main/en/flight_controller/pixhawk_autopilot_bus"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "flight_controller/pixhawk_autopilot_bus.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/flight-controller
---

# Pixhawk Autopilot Bus & Carriers

The [Pixhawk Autopilot Bus (PAB) Standard](https://github.com/pixhawk/Pixhawk-Standards/blob/master/DS-010%20Pixhawk%20Autopilot%20Bus%20Standard.pdf) provides a standard interface design that allows any compliant Pixhawk flight controller to be used "plug-and-play" with any compliant base board.

This modularity makes it easier to integrate flight controllers into different system-on-module designs.
For example, the PAB means that you can use the same flight controller hardware on a more compact board with fewer outputs, or on a board that integrates with a companion computer, and so on.

The following carriers and flight controllers are PAB-compliant, and can therefore be used interchangeably.

::: info
The "Mechanical Design" section of the standard provides specific recommendations for mechanical compatibility between vendors.
The flight controllers and baseports listed here are expected to be compliant with all recommendations.
:::

## PAB Compatible Carriers

- [ARK Electronics Pixhawk Autopilot Bus Carrier](../flight_controller/ark_pab.md)
- [Holybro Pixhawk Standard Baseboard](https://holybro.com/products/pixhawk-baseboards)
- [Holybro Pixhawk Mini Baseboard](https://holybro.com/products/pixhawk-baseboards)
- [Holybro Pixhawk RPi CM4 Baseboard](../companion_computer/holybro_pixhawk_rpi_cm4_baseboard.md) (Integrated Companion/Flight Controller Board)

## PAB Compatible Flight Controllers

- [ARK Electronics ARKV6X](../flight_controller/ark_v6x.md)
- [ARK Electronics ARKV6S](../flight_controller/ark_v6s.md)
- [Holybro Pixhawk 5X (FMUv5X)](../flight_controller/pixhawk5x.md)
- [Holybro Pixhawk 6X (FMUv6X)](../flight_controller/pixhawk6x.md)
- [CUAV Pixhawk V6X (FMUv6X)](../flight_controller/cuav_pixhawk_v6x.md)
