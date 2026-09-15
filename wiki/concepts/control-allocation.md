---
title: Control Allocation (Mixing)
type: concept
sources:
  - "[[raw/documents/PX4/concept/control_allocation]]"
  - "[[raw/documents/PX4/config/actuators]]"
  - "[[raw/documents/PX4/config/airframe]]"
created: 2026-07-28
updated: 2026-09-15
tags:
  - uav/flight-control
  - uav/hardware
  - stack/px4
  - stack/qgc
status: active
doc_version_checked:
  - "PX4 main@9467506"
---

# Control Allocation (Mixing)

The layer that translates the **torque and thrust commands** output by the core controllers into **individual motor and servo commands**. How that translation works depends on the vehicle's physical geometry:

- For a plane with one servo per aileron, "roll right" means one servo deflects up and the other down
- For a multicopter, "yaw right" means changing the speed of **all** motors

**PX4 deliberately separates this logic from the attitude/rate controllers**, so the core controllers need no special cases for each vehicle geometry — which is why all vehicle types can share one code base (see [[wiki/topics/px4-flight-stack]]).

Besides the geometric translation, it also abstracts the mapping of "output functions → physical output pins", so **almost any motor or servo can be assigned to almost any physical output**.

> Control allocation replaced the legacy mixing approach used in PX4 v1.13 and earlier. If you find material about mixer files or geometry files, it refers to v1.13.

## What the `control_allocator` module does

- Handles different geometries based on configuration parameters
- Performs the mixing
- **Handles motor failures**
- Publishes the motor and servo control signals
- **Publishes servo trims separately**, so they can be added as an offset during actuator testing (the test sliders in QGC)

Upstream it receives torque and thrust setpoints from the rate controller; downstream are the output drivers (which handle hardware initialization and updates).

## Two-stage setup

| Stage | What | Where |
| --- | --- | --- |
| **1. Select the airframe** | Loads the approximate geometry and default parameters from the airframe configuration (`CA_AIRFRAME`, `CA_ROTOR_COUNT`, the per-rotor `CA_ROTOR*_*`) | QGC → Basic Configuration → **Airframe** |
| **2. Adjust geometry and output mapping** | Sets the exact geometry and output pins for your actual vehicle and flight controller hardware | QGC → Basic Configuration → **Actuators** |

**Selecting an airframe does not finish the setup.** The airframe configuration only provides defaults for that type; the actual motor positions, spin directions and output pins must be confirmed on the Actuators screen. This is the step that most often goes wrong on self-built vehicles, and the symptom is "flips over on takeoff".

Parameters with the `CA_` prefix belong to control allocation; see [[wiki/concepts/px4-parameters]] for how to look them up.

## Related pages

- [[wiki/topics/px4-flight-stack]] — where control allocation sits in the data flow
- [[wiki/concepts/pid-tuning]] — tuning the upstream controllers; `MC_AIRMODE` concerns mixer saturation
- [[wiki/concepts/px4-parameters]] — the `CA_` parameter family
