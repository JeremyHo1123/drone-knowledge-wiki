---
title: "Flight Modes (VTOL)"
type: document
doc_set: PX4
doc_version: main
section: flight_modes_vtol
source_url: "https://docs.px4.io/main/en/flight_modes_vtol/"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "flight_modes_vtol/index.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/flight-modes-vtol
---

# Flight Modes (VTOL)

Flight modes provide autopilot support to make it easier to manually fly the vehicle, to automate common tasks such as takeoff and landing, to execute autonomous missions, or to defer flight control to an external system.

VTOL vehicles can fly as either a multicopter or a fixed-wing vehicle, and will generally have exactly the same behaviour as the corresponding vehicle type:

VTOL-specific flight mode behaviour is covered in:

- [Land mode](../flight_modes_vtol/land.md): A VTOL flying as a fixed-wing vehicle will transition to MC before landing.
- [Mission mode](../flight_modes_vtol/mission.md): Missions support VTOL-specific mission commands for taking off, landing, and transitioning between vehicle types.
- [Return mode](../flight_modes_vtol/return.md): VTOL vehicles behave slightly differently they return as an MC or FW than the corresponding vehicles.

For other flight modes see the vehicle-specific behaviour:

- [Flight Modes (Multicopter)](../flight_modes_mc/index.md)
- [Flight Modes (Fixed-Wing)](../flight_modes_fw/index.md)

## Further Information

- [Basic Configuration > Flight Modes](../config/flight_mode.md) - How to map RC control switches to specific flight modes
