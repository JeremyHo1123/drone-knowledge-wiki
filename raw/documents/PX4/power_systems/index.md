---
title: "Power Systems"
type: document
doc_set: PX4
doc_version: main
section: power_systems
source_url: "https://docs.px4.io/main/en/power_systems/"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "power_systems/index.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/power-systems
---

# Power Systems

UAVs require a regulated power supply for the flight controller, along with separate power for the motors, servos, and any other peripherals.
The power is usually supplied from a battery (or batteries), though generators and other systems can be used.

Power modules are commonly used to "split off" a regulated power supply for the flight controller and also measure the battery voltage and total current consumed by the vehicle.
PX4 can use this information to infer the remaining battery capacity and provide low-power warnings and other failsafe behaviour.

A Power Distribution Board (PDB) may be used to simplify the wiring for splitting the output of the battery to the flight controller, motors, and other peripherals.
PDBs will sometimes include a power module, ESCs for motors, and a battery elimination circuit (BEC) for powering servos.

PX4 can also receive more comprehensive battery/power-supply information as MAVLink telemetry instead of using a power module.
Batteries that can _supply_ MAVLink information are sometimes referred to as "Smart Batteries" (this definition is open for debate).

- [Power Modules/PDB](../power_module/index.md)
- [Smart/MAVLink Batteries](../smart_batteries/index.md)
