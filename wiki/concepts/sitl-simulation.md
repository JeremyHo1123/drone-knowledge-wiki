---
title: PX4 Simulation (SITL / HITL)
type: concept
sources:
  - "[[raw/documents/PX4/simulation/index]]"
  - "[[raw/documents/PX4/simulation/hitl]]"
  - "[[raw/documents/PX4/simulation/px4_simulation_quickstart]]"
  - "[[raw/documents/PX4/sim_gazebo_gz/index]]"
  - "[[raw/documents/PX4/sim_sih/index]]"
created: 2026-07-28
updated: 2026-09-15
tags:
  - uav/simulation
  - stack/px4
status: active
doc_version_checked:
  - "PX4 main@9467506"
---

# PX4 Simulation (SITL / HITL)

A simulator lets the PX4 flight code control a computer-modelled vehicle. **You interact with it just as you would with a real vehicle** — through QGroundControl, an offboard API, or an RC transmitter/joystick. It is the foundation of every "get it working in simulation first" recommendation in this wiki.

| | SITL (Software In the Loop) | HITL (Hardware In the Loop) |
| --- | --- | --- |
| The flight stack runs on | A computer (the same machine or another one on the network) | A **real flight controller board** (running simulation firmware) |
| Purpose | Development and fast iteration | Verifying real hardware timing and compute load |

> Simulation is a quick, easy and, **most importantly, safe** way to test changes to PX4 code before attempting to fly in the real world. It is also a good way to start with PX4 when you don't have a vehicle yet.

## Which simulator

The core development team supports three; **Gazebo is the default choice for new projects**:

| Simulator | Positioning |
| --- | --- |
| **Gazebo** (formerly Gazebo Ignition) | Replaces Gazebo Classic. More advanced rendering, physics and sensor models. **The only Gazebo version available from Ubuntu 22.04 onwards**. Good for testing obstacle avoidance and computer vision; supports multi-vehicle simulation; commonly paired with ROS |
| **SIH** | Lightweight and headless; physics runs inside PX4 as a C++ module (**no external dependencies**). Headless by default for the fastest iteration; supports uXRCE-DDS for ROS 2. **Can also run on real flight controller hardware** (`SYS_HITL=2`) |
| **Gazebo Classic** | **Demoted to community support and no longer recommended as the default**. Keep using it if an old workflow does not yet run on the new Gazebo, but the core team no longer maintains it |

### Gazebo vs. SIH

| Aspect | Gazebo | SIH |
| --- | --- | --- |
| Default mode | GUI with 3D rendering | Headless (fastest iteration) |
| Physics engine | External (gz-physics) | Internal (C++ module over uORB) |
| External dependencies | Gazebo packages, rendering libraries | None |
| Simulated sensors | Camera, LiDAR, depth, IMU, GPS, barometer, magnetometer | IMU, GPS, barometer, magnetometer, airspeed |
| Vehicle types | Quad, VTOL, Plane, Rover | Quad, Hex, Plane, Tailsitter, Standard VTOL, Rover |

**The rule of thumb is clear**: if you need vision sensors (camera/LiDAR/depth), use Gazebo; if you only verify control, mission or failsafe logic, SIH is much faster and needs nothing extra installed.

If you **don't want to set up a build environment**, prebuilt packages and containers are available ([[raw/documents/PX4/simulation/px4_sitl_prebuilt_packages]]).

## Three things to finish in simulation first

1. **Verify combined failsafe behaviour** — the state-machine simulation in [[raw/documents/PX4/config/safety_simulation]]; see [[wiki/concepts/failsafe]]
2. **Get programmatic control working** — MAVSDK's default connection address `udpin://0.0.0.0:14540` is the SITL port; see [[wiki/howto/mavsdk-takeoff-and-land]]
3. **Watch the uORB data flow** — the SITL `pxh>` shell supports `uorb top` and `listener` too; see [[wiki/concepts/uorb-messaging]]

## Related pages

- [[wiki/concepts/failsafe]] — verifying failsafes in simulation
- [[wiki/howto/mavsdk-takeoff-and-land]] — the first thing to run in simulation
- [[wiki/concepts/ros2-px4-bridge]] — SIH also supports uXRCE-DDS
- [[wiki/concepts/flight-log-analysis]] — simulations produce logs too
