---
title: PX4 and ROS 2 Integration (uXRCE-DDS)
type: concept
sources:
  - "[[raw/documents/PX4/middleware/uxrce_dds]]"
  - "[[raw/documents/PX4/ros2/index]]"
  - "[[raw/documents/PX4/ros2/px4_ros2_control_interface]]"
  - "[[raw/documents/PX4/middleware/dds_topics]]"
created: 2026-07-28
updated: 2026-09-15
tags:
  - uav/comms
  - uav/autonomy
  - stack/px4
  - stack/ros2
status: active
doc_version_checked:
  - "PX4 main@9467506"
---

# PX4 and ROS 2 Integration (uXRCE-DDS)

PX4 uses the uXRCE-DDS middleware so that uORB messages ([[wiki/concepts/uorb-messaging]]) **can be published and subscribed on a companion computer as if they were ROS 2 topics**. This gives fast, reliable integration between PX4 and ROS 2, and it is currently the mainline path for building advanced autonomy features.

> uXRCE-DDS replaced the Fast-RTPS Bridge of v1.13 starting with **PX4 v1.14**. Material about Fast-RTPS describes the old architecture.

The implementation is based on eProsima Micro XRCE-DDS.

## Architecture: client + agent

```
Flight controller (PX4)              Companion computer
uxrce_dds_client  <— serial or UDP —>  Micro XRCE-DDS Agent  <->  DDS / ROS 2 network
```

- The **client** runs on PX4; it publishes a **predefined** set of uORB topics to the global DDS data space and subscribes from it
- The **agent** runs on the companion computer and acts as a proxy for the client in the DDS/ROS 2 network
- Data flows in both directions between them

**The key word is "predefined"**: not every uORB topic appears on the ROS 2 side. The bridged topics are listed in [[raw/documents/PX4/middleware/dds_topics]]; adding a topic requires changing the configuration.

## Three levels of ROS 2 integration (picking the wrong one wastes effort)

| Level | What you write | When to use |
| --- | --- | --- |
| **Read/write uORB topics directly** | Subscribe to `VehicleOdometry` and similar, publish `TrajectorySetpoint` + `OffboardControlMode` | Lowest level and most flexible, but you handle all timing and safety yourself |
| **PX4 ROS 2 Interface Library** | A higher-level, safer API | PX4's **recommended alternative** for offboard control |
| **PX4 ROS 2 Control Interface** | An **external flight mode** | Custom mode logic; see [[wiki/concepts/flight-modes]] |

The official docs put a **warning-level** notice on ROS 2 offboard control through the lowest-level path and explicitly recommend considering the Interface Library first (see [[wiki/concepts/offboard-control]]).

## Maturity

- **uXRCE-DDS itself**: the mainline solution since v1.14; stable
- **PX4 ROS 2 Control Interface (external modes)**: introduced in v1.15, **still experimental**, with limitations and expected to keep changing

Factor the latter's change risk into long-term projects, or when citing related papers.

## Message versioning

uORB messages that are exposed to ROS 2 and must stay compatible across ROS and PX4 versions **need to be versioned** (placed in `msg/versioned/`). This is how PX4 keeps internal refactoring from breaking the ROS 2 side; details in [[wiki/concepts/uorb-messaging]].

## Trade-offs versus MAVSDK

| | uXRCE-DDS / ROS 2 | MAVSDK |
| --- | --- | --- |
| Access level | uORB topics, close to the flight controller internals | MAVLink, abstracted |
| Bandwidth and latency | High rate, low latency | Limited by the MAVLink message set and rates |
| Ecosystem | Full ROS 2 toolchain and libraries | Lightweight, simple API |
| Best for | High-rate state, custom control laws, computer-vision integration | Mission-level commands, telemetry subscriptions, quick prototypes |

See the layering in [[wiki/topics/drone-software-stack]].

## Related pages

- [[wiki/concepts/uorb-messaging]] — what is being bridged
- [[wiki/concepts/offboard-control]] — setpoints and liveness signals on the ROS 2 path
- [[wiki/concepts/flight-modes]] — external vs. internal modes
- [[wiki/concepts/visual-inertial-odometry]] — a typical companion-computer application
