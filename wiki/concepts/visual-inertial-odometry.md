---
title: Visual-Inertial Odometry (VIO)
type: concept
sources:
  - "[[raw/documents/PX4/computer_vision/visual_inertial_odometry]]"
  - "[[raw/documents/PX4/computer_vision/index]]"
  - "[[raw/documents/PX4/advanced_config/tuning_the_ecl_ekf]]"
created: 2026-07-28
updated: 2026-09-15
tags:
  - uav/state-estimation
  - uav/perception
  - stack/px4
  - stack/ros2
status: active
doc_version_checked:
  - "PX4 main@9467506"
---

# Visual-Inertial Odometry (VIO)

Estimates the vehicle's 3D pose (position + orientation) and velocity relative to a **local starting point** from camera images, using inertial measurements from the IMU to correct the errors caused by degraded image quality during fast motion. It is mainly used **where GPS is unavailable or unreliable** — indoors, under bridges, in urban canyons.

VIO is the most typical example of this wiki's "research ↔ implementation" gap: academia has a large body of VIO/VI-SLAM methods and benchmarks, but **the PX4 side only defines an interface; it does not do VIO itself**.

## What PX4 actually provides

In one sentence: **PX4 only fuses; it does not compute.**

> PX4 does not care about the source of the messages, as long as they arrive through the appropriate MAVLink interface.

That means:

- The VIO algorithm runs on a **companion computer**, not on the flight controller
- The companion computer sends its pose estimate to PX4 as `ODOMETRY` or `VISION_POSITION_ESTIMATE` MAVLink messages
- PX4's [[wiki/concepts/ekf2]] fuses it as one of its observations
- The docs **recommend** ROS + MAVROS as the pipeline, but this is a suggested route, not a hard requirement

This split decides where your effort goes: **algorithm choice and accuracy are the paper's business; PX4's business is only "is the interface right, is EKF2 tuned correctly, is the delay compensation accurate".**

## Recommended setup from the docs

- **Camera**: an off-the-shelf tracking camera; the docs' example is the Intel RealSense T265
- **Mounting**: facing down if possible (the default); **the camera is extremely sensitive to vibration, so soft-mount it** (e.g. with anti-vibration foam)
- **Companion computer**: install and configure MAVROS, and run a ROS node that reads the camera and publishes VIO odometry through MAVROS
- **PX4**: tune the EKF2 estimator parameters as documented

### The ROS node's three responsibilities

1. Interface with the chosen camera/sensor hardware (the implementation depends on the camera)
2. Produce odometry messages with the position estimate, of type `nav_msgs/Odometry`, published to `/mavros/odometry/out`
3. Publish system status messages, of type `mavros_msgs/CompanionProcessStatus`, to `/mavros/companion_process/status`, with component ID `MAV_COMP_ID_VISUAL_INERTIAL_ODOMETRY` (197)

## Verification (before the first flight)

Use QGC's **MAVLink Inspector** ([[raw/documents/QGC/analyze_view/mavlink_inspector]]) to confirm that:

- `ODOMETRY` or `VISION_POSITION_ESTIMATE` messages are being received, or
- a `HEARTBEAT` with component id 197 is being received

The docs use an exclamation mark for "verify that the VIO setup is correct before the first flight" — **with VIO, estimation errors are equivalent to losing position control**.

## Research–implementation gap

- **Papers claim**: VIO/VI-SLAM can reach centimetre-level relative positioning accuracy, with many open-source implementations
- **PX4 today**: the mainline only provides the MAVLink fusion interface and EKF2 support for vision measurements; **no VIO algorithm is built in**
- **Nature of the gap**: needs a companion computer plus your own selection and integration. Algorithm quality, time synchronization and delay compensation (`EKF2_*_DELAY`) are entirely the user's responsibility

When a paper is added to the wiki, the deciding questions for whether its method can run on a vehicle are: **does it output a pose format that PX4 can consume, and is its delay measurable and compensable?**

## Related pages

- [[wiki/concepts/ekf2]] — VIO is one observation source for it; the delay compensation parameters live there
- [[wiki/concepts/collision-prevention]] — the same "companion computer provides, PX4 consumes" pattern
- [[wiki/concepts/ros2-px4-bridge]] — a newer integration path than MAVROS
