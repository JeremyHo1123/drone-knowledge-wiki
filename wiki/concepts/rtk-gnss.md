---
title: RTK GNSS (Centimetre-Level Positioning)
type: concept
sources:
  - "[[raw/documents/PX4/gps_compass/rtk_gps]]"
  - "[[raw/documents/PX4/gps_compass/index]]"
  - "[[raw/documents/PX4/advanced_config/gnss_degraded_or_denied_flight]]"
  - "[[raw/documents/MAVSDK/plugins/rtk]]"
created: 2026-07-28
updated: 2026-09-15
tags:
  - uav/state-estimation
  - stack/px4
  - stack/qgc
status: active
doc_version_checked:
  - "PX4 main@9467506"
---

# RTK GNSS (Centimetre-Level Positioning)

Real Time Kinematic GNSS provides **centimetre-level** positioning accuracy, which lets PX4 be used in applications that need precise positioning, such as surveying. Compared with the metre-level error of standard GNSS, this is an order-of-magnitude difference.

## Architecture: always a pair

**RTK needs a pair of devices** — a **base** at the ground station and a **rover** on the vehicle. The base sits at a known position, computes corrections, and sends them to the rover through the ground station and a data link.

The requirements are therefore:

- A **laptop/PC** running QGroundControl (**the Android/iOS versions of QGC do not support RTK**)
- A WiFi or telemetry radio link between the vehicle and the laptop

In principle one base can serve several vehicles/rover modules, but **the docs note that this use case was untested at the time of writing**.

## Hardware connection

How the rover module connects depends on the module and the flight controller: most connect to the flight controller's GPS port like a regular GPS module; **some use the CAN bus (DroneCAN)**.

PX4 supports the u-blox M8P, the u-blox F9P, the Trimble MB-Two and products built on these chips. [[raw/documents/PX4/gps_compass/rtk_gps]] has the full compatibility table, including whether a device uses DroneCAN, outputs yaw, or supports PPK (Post-Processing Kinematic).

## It can also solve compass problems

Some RTK configurations can **output yaw/heading and replace the compass** — a very practical benefit on vehicles with strong magnetic interference (high currents, carbon-fibre frames). Two routes:

- **Dual antennas/dual modules**: e.g. the dual u-blox F9P heading solution
- **GPS outputs yaw directly**: supported natively by some devices

## Relation to EKF2

For [[wiki/concepts/ekf2]], RTK is simply "a more accurate global position measurement". It improves the global position and velocity estimates, but **does not improve attitude estimation** (unless the GPS yaw feature above is used).

Conversely, strategies for degraded or fully denied GNSS are in [[raw/documents/PX4/advanced_config/gnss_degraded_or_denied_flight]]; then you rely on alternative position sources such as [[wiki/concepts/visual-inertial-odometry]].

## Programmatic access

MAVSDK's `Rtk` plugin can send RTCM correction data to the vehicle; see [[raw/documents/MAVSDK/plugins/rtk]] — needed when you run your own base station or use a network NTRIP service.

## Related pages

- [[wiki/concepts/ekf2]] — RTK is a high-accuracy observation fed into it
- [[wiki/concepts/visual-inertial-odometry]] — the alternative when GNSS is denied
