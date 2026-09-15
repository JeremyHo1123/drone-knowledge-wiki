---
title: "ROS 1 (Deprecated)"
type: document
doc_set: PX4
doc_version: main
section: ros
source_url: "https://docs.px4.io/main/en/ros/ros1"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "ros/ros1.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/ros
---

# ROS 1 (Deprecated)

::: warning
The PX4 development team recommend that users migrate to [ROS 2](../ros2/index.md) (i.e. skip this section)!

ROS 1 is now "discommended" as the last LTS version is approaching end of life.
ROS 2 has much deeper integration with PX4, enabling lower-latency communication with access to PX4 internal messaging.
:::

[ROS (1)](https://www.ros.org/) is a general purpose robotics library that can be used with PX4 for drone application development.

This version of ROS uses the [MAVROS](../ros/mavros_installation.md) package to communicate with PX4 over MAVLink (MAVROS bridges ROS topics to MAVLink and PX4 conventions).

## Topics

- [ROS/MAVROS Installation Guide](../ros/mavros_installation.md): Setup a PX4 development environment with ROS 1 and MAVROS.
- [ROS/MAVROS Offboard Example (C++)](../ros/mavros_offboard_cpp.md): Tutorial showing the main concepts related to writing a C++ MAVROS/ROS node.
- [ROS MAVROS Sending Custom Messages](../ros/mavros_custom_messages.md)
- [ROS with Gazebo Classic Simulation](../simulation/ros_interface.md)
- [Gazebo Classic OctoMap Models with ROS](../sim_gazebo_classic/octomap.md)
- [ROS Installation on RPi](../ros/raspberrypi_installation.md)
- [External Position Estimation (Vision/Motion based)](../ros/external_position_estimation.md)

## Further Information

- [XTDrone](https://github.com/robin-shaun/XTDrone/blob/master/README.en.md) - ROS + PX4 simulation environment for computer vision.
  The [XTDrone Manual](https://www.yuque.com/xtdrone/manual_en) has everything you need to get started!
- [Prometheus Autonomous Drone Project](https://github.com/amov-lab/Prometheus/blob/master/README_EN.md) - Prometheus is a ROS 1 based, BSD-3 licensed collection of autonomous drone software packages from [AMOVLab](https://github.com/amov-lab), which provides a full set of solutions for the intelligent and autonomous flight of drones, such as mapping, localization, planning, control, and target detection, fully integrated with the [Gazebo Classic](../sim_gazebo_classic/index.md) Simulator.
