---
title: Flight Mode System
type: concept
sources:
  - "[[raw/documents/PX4/concept/flight_modes]]"
  - "[[raw/documents/PX4/flight_modes/index]]"
  - "[[raw/documents/PX4/config/flight_mode]]"
  - "[[raw/documents/QGC/setup_view/flight_modes_px4]]"
created: 2026-07-28
updated: 2026-09-15
tags:
  - uav/flight-control
  - uav/autonomy
  - stack/px4
  - stack/qgc
status: active
doc_version_checked:
  - "PX4 main@9467506"
  - "QGC Stable_V5.0@cb6ee48"
---

# Flight Mode System

A mode is an operating state that defines "how the autopilot responds to user input and controls vehicle motion". Modes are **loosely** grouped by how much control the autopilot provides:

- **manual** — the pilot controls the vehicle directly
- **assisted** — the autopilot helps (e.g. Position mode holds position)
- **auto** — the autopilot is in charge (missions, return, landing)

Modes are switched from an RC switch or the ground station. Which switch maps to which mode is configured in QGC: [[raw/documents/QGC/setup_view/flight_modes_px4]].

**Not every mode is available or meaningful on every vehicle type, and modes with the same name can behave differently on different vehicles.** That is why the mode documentation is split per vehicle type:

- Multicopter [[raw/documents/PX4/flight_modes_mc/index]]
- Fixed-wing [[raw/documents/PX4/flight_modes_fw/index]]
- VTOL [[raw/documents/PX4/flight_modes_vtol/index]]
- Rover [[raw/documents/PX4/flight_modes_rover/index]]

**When looking up mode behaviour, always go to the directory for your vehicle type**; the generic `flight_modes/` only holds content shared across vehicle types.

## Internal modes vs. external (ROS 2) modes

This is the most significant architectural change in PX4 in recent years, and the fork in the road for "writing your own flight mode". A mode can be implemented as a **PX4 internal mode running on the flight controller**, or as a **PX4 external mode running on a companion computer**. **From the ground station's (MAVLink) point of view, the two are indistinguishable.**

### When you cannot use an external mode

- There is no companion computer on the vehicle
- You need low-level access, strict timing or high update rates — e.g. a multicopter mode that controls the motors directly
- **Safety-critical modes such as Return mode**
- Any situation where ROS cannot be used

**In all other cases external modes should be preferred**, for convincing reasons:

- No need to deal with low-level embedded constraints (such as limited stack size), so they are easier to implement
- The integration API is small, well defined and stable; custom modes on the flight controller, by contrast, often use interfaces considered "internal and subject to change", **which makes them much harder to port across PX4 versions**
- **If a ROS 2 mode process terminates, PX4 falls back to an internal flight mode; if an internal mode terminates, the vehicle is likely to crash**
- They can replace existing modes to provide more advanced functionality — **even safety-critical modes**, because the original mode takes over if the ROS 2 mode fails
- A high-level programming environment, a wealth of Linux/ROS libraries, and far more compute (enough for computer vision)

### Maturity warning

The **PX4 ROS 2 Control Interface** used to build external modes **first appeared in PX4 v1.15 and is still considered experimental**. It has limitations and is expected to keep changing.

**This is a textbook case of the research–implementation gap**: architecturally, external modes are the right way to build custom autonomous behaviour, but the interface itself is still evolving — factor this in when citing related papers or planning long-term projects.

## Relation to offboard

Offboard is **an internal mode**: the external program only sends setpoints and the control laws still run on the flight controller. With an external mode, **the whole mode logic** runs on the companion computer. They are solutions at different levels:

| | Offboard mode | External (ROS 2) mode |
| --- | --- | --- |
| Who decides where to go | External program | External program |
| Who runs the control laws | PX4 | External program (customizable at different levels) |
| What the ground station shows | Offboard mode | A normal flight mode |
| Maturity | Stable | Experimental (v1.15+) |

Details in [[wiki/concepts/offboard-control]] and [[wiki/concepts/ros2-px4-bridge]].

## Related pages

- [[wiki/concepts/offboard-control]] — the most common programmatic control mode
- [[wiki/concepts/ros2-px4-bridge]] — the underlying channel for external modes
- [[wiki/concepts/failsafe]] — the Hold / Return / Land failsafe actions are modes themselves
- [[wiki/concepts/mission-planning]] — where the content of auto modes comes from
