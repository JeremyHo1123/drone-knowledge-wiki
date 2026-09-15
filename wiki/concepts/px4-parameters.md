---
title: PX4 Parameter System
type: concept
sources:
  - "[[raw/documents/PX4/advanced_config/parameters]]"
  - "[[raw/documents/PX4/advanced_config/parameter_reference]]"
  - "[[raw/documents/QGC/setup_view/parameters]]"
  - "[[raw/documents/MAVSDK/plugins/param]]"
created: 2026-07-28
updated: 2026-09-15
tags:
  - uav/flight-control
  - stack/px4
  - stack/qgc
  - stack/mavsdk
status: active
doc_version_checked:
  - "PX4 main@9467506"
  - "QGC Stable_V5.0@cb6ee48"
---

# PX4 Parameter System

Parameters are the entry point to almost all tunable behaviour in PX4 — PID gains, speed and tilt limits, failsafe actions, sensor calibration results and serial port function assignments are all parameters. **When you ask "how do I change the behaviour of X", the answer is usually a parameter.**

## Naming convention (it determines how you search)

Parameter names are upper case with underscores, and **the prefix is the module or subsystem**. Knowing the prefix narrows the search from thousands to dozens:

| Prefix | Scope |
| --- | --- |
| `MPC_` | Multicopter position/velocity control (Multicopter Position Control) |
| `MC_` | Multicopter attitude and rate control |
| `FW_` | Fixed-wing control |
| `VT_` | VTOL transitions |
| `EKF2_` | State estimator |
| `COM_` | Commander: mode switching, arming conditions, failsafes |
| `NAV_` | Navigation and mission behaviour |
| `RTL_` | Return |
| `GF_` | Geofence |
| `IMU_` | IMU filtering (notch, low-pass) |
| `SER_` / `MAV_` | Serial port and MAVLink settings |
| `SIM_` | Simulation |

In practice: narrow the range by grepping for the prefix, then find the exact definition in [[raw/documents/PX4/advanced_config/parameter_reference]]. That file is 1.6 MB and contains each parameter's description, type, default, unit and bounds; **it is this wiki's authoritative source for parameter questions**.

```
Grep pattern="MPC_TILTMAX" path="raw/documents/PX4/advanced_config/parameter_reference.md" output_mode="content" -n=true
```

## Three ways to change parameters

| Route | Suited for | Source |
| --- | --- | --- |
| **Dedicated QGC setup screens** | Common items (airframe, sensor calibration, radio, flight modes, safety) | [[raw/documents/PX4/config/index]] |
| **QGC Parameters screen** | Less common parameters, fine adjustments during tuning | [[raw/documents/QGC/setup_view/parameters]] |
| **MAVSDK `Param` plugin** | Programmatic reads and writes, automated testing | [[raw/documents/MAVSDK/plugins/param]] |

The QGC Parameters screen is under **Vehicle Setup → Parameters**. It supports substring search (over names and descriptions), browsing by type and group, and **Show modified only**. Groups named *Component X* at the bottom are DroneCAN peripherals attached to the flight controller — **the peripheral must already be connected when QGC starts** for them to appear.

**The docs warn explicitly: although some parameters can be changed in flight, this is not recommended unless the documentation says so.**

## Three reasons a parameter can't be found

This is the most common confusion, and the docs classify it clearly:

1. **Conditional parameter** — it depends on another parameter that is not enabled yet, so it is hidden. Serial port configuration parameters are the typical case: they depend on which service the port has been assigned (see [[raw/documents/PX4/peripherals/serial_configuration]]).
2. **Not in the firmware** — your PX4 version differs, or the module was not compiled into this build. Every release adds parameters and also removes or renames some.
3. **You remembered the name wrong** — search the descriptions in the parameter reference, not just the names.

**This matters especially for this wiki**: `raw/documents/PX4/` tracks the `main` development branch, so the parameter reference may contain parameters that your stable release does not have yet. If the local docs list a parameter that QGC cannot find, suspect a version gap first, then check [[raw/documents/PX4/releases/index]] for the release that introduced it.

## Related pages

- [[wiki/topics/px4-flight-stack]] — which architectural layer a parameter belongs to
- [[wiki/concepts/pid-tuning]] — how to tune the control gain parameters
- [[wiki/concepts/failsafe]] — failsafe parameters in the `COM_` family
- [[wiki/concepts/ekf2]] — estimator parameters in the `EKF2_` family
