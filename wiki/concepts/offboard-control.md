---
title: Offboard Control
type: concept
sources:
  - "[[raw/documents/PX4/flight_modes/offboard]]"
  - "[[raw/documents/MAVSDK/plugins/offboard]]"
  - "[[raw/documents/PX4/ros2/index]]"
created: 2026-07-28
updated: 2026-09-15
tags:
  - uav/flight-control
  - uav/autonomy
  - stack/px4
  - stack/mavsdk
status: active
doc_version_checked:
  - "PX4 main@9467506"
---

# Offboard Control

Offboard is a PX4 flight mode in which the vehicle no longer decides where to go from its own mission or manual input, but **follows setpoints sent from a source outside the flight controller** — position, velocity, acceleration, attitude, attitude rate, or thrust/torque. It is the standard entry point for connecting your own algorithms (vision, planning or learned controllers on a companion computer) to a real vehicle, and a mandatory stop on this wiki's "paper method → actually flying" path.

## Mechanism: the setpoint stream is the "proof of life"

The most commonly misunderstood point about offboard: **the external controller must stream messages continuously, and the stream itself is the proof of life**. It is not "send one command and the flight controller remembers it".

- Over MAVLink (including MAVSDK): the setpoint message plays **both** roles, "I'm alive" and "target value". To hold the vehicle in place, you must keep sending a setpoint for the current position.
- Over ROS 2: the roles are separated — `OffboardControlMode` is published continuously to signal liveness, and the actual target is published to the corresponding uORB topic (such as `TrajectorySetpoint`), which only needs to be sent once.

If the stream stops for longer than the `COM_OF_LOSS_T` timeout, PX4 leaves offboard and performs the failsafe action set in `COM_OBL_RC_ACT` (which depends on whether RC is available).

## Entry conditions (most failures happen here)

1. **A position or attitude source must be available first** — GPS, optical flow, VIO or motion capture, depending on the setpoint type you send.
2. **The setpoint stream must already be running before you switch into offboard (or arm in offboard).** Switching the mode first and only then starting to send is rejected.
3. **Manual control is disabled in offboard**, except for the ability to change modes. With no RC at all, set `COM_RC_IN_MODE` to `4: Disable manual control`.
4. Offboard supports only a limited set of MAVLink commands. **Takeoff, landing and return are more reliable in their dedicated modes** — don't force them into offboard.

## Pitfalls with frames and setpoint types

PX4 **does not support every** combination of frames and fields that the MAVLink specification allows, and support differs by vehicle type. Before choosing a setpoint type, check the support matrix in the corresponding section of [[raw/documents/PX4/flight_modes/offboard]] — this is the most common reason for "I followed the MAVLink docs and nothing happens".

## Mapping in the PX4 ecosystem

| Aspect | Mapping |
| --- | --- |
| PX4 parameters | `COM_OF_LOSS_T` (offboard signal timeout), `COM_OBL_RC_ACT` (action after loss), `COM_RC_IN_MODE` (whether manual control is disabled) |
| PX4 docs | [[raw/documents/PX4/flight_modes/offboard]]; controller architecture in [[raw/documents/PX4/flight_stack/controller_diagrams]] |
| MAVSDK API | `system.offboard`: `start()` / `stop()` / `is_active()`; setpoints via `set_position_ned()`, `set_velocity_ned()`, `set_velocity_body()`, `set_position_global()`, `set_attitude()`, `set_attitude_rate()`, `set_acceleration_ned()`, `set_position_velocity_ned()`, `set_position_velocity_acceleration_ned()`, `set_actuator_control()` — [[raw/documents/MAVSDK/plugins/offboard]] |
| ROS 2 path | uXRCE-DDS or a direct Zenoh connection — [[raw/documents/PX4/ros2/index]] |

**With MAVSDK, at least one setpoint must be sent before `Offboard.start()`**, otherwise PX4 refuses to enter the mode — the "stream before mode switch" rule above, expressed at the API level.

## Safety

The official PX4 documentation puts a **warning-level** notice on ROS 2 offboard control: using it safely requires a good understanding of the PX4 controller architecture, and the safer alternative interface [[raw/documents/PX4/ros2/px4_ros2_interface_lib]] should be considered first. Before testing on a real vehicle, make sure failsafes and a geofence are configured.

## Related pages

- [[wiki/topics/drone-software-stack]] — offboard is where the three layers interact most
- [[wiki/howto/mavsdk-takeoff-and-land]] — get the basic connection and Action working first, then move on to offboard
