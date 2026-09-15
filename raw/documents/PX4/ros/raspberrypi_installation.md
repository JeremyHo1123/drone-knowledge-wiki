---
title: "Raspberry Pi - ROS installation"
type: document
doc_set: PX4
doc_version: main
section: ros
source_url: "https://docs.px4.io/main/en/ros/raspberrypi_installation"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "ros/raspberrypi_installation.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/ros
---

# Raspberry Pi - ROS installation

This is a guide on how to install ROS-indigo on a Raspberry Pi 2 serving as a companion computer for Pixhawk.

## Prerequisites

- A working Raspberry Pi with monitor, keyboard, or configured SSH connection
- This guide assumes that you have Raspbian "JESSIE" installed on your RPi. If not: [install it](https://www.raspberrypi.org/downloads/raspbian/) or [upgrade](https://raspberrypi.stackexchange.com/questions/27858/upgrade-to-raspbian-jessie) your Raspbian Wheezy to Jessie.

## Installation

Follow [this guide](https://wiki.ros.org/ROSberryPi/Installing%20ROS%20Indigo%20on%20Raspberry%20Pi) for the actual installation of ROS Indigo. Note: Install the "ROS-Comm" variant. The Desktop variant is too heavyweight.

### Errors when installing packages

If you want to download packages (e.g. `sudo apt-get install ros-indigo-ros-tutorials`), you might get an error saying: "unable to locate package ros-indigo-ros-tutorials".

If so, proceed as follows:
Go to your catkin workspace (e.g. ~/ros_catkin_ws) and change the name of the packages.

```sh
cd ~/ros_catkin_ws
rosinstall_generator ros_tutorials --rosdistro indigo --deps --wet-only --exclude roslisp --tar > indigo-custom_ros.rosinstall
```

Next, update your workspace with wstool.

```sh
wstool merge -t src indigo-custom_ros.rosinstall
wstool update -t src
```

Next (still in your workspace folder), source and make your files.

```sh
source /opt/ros/indigo/setup.bash
source devel/setup.bash
catkin_make
```
