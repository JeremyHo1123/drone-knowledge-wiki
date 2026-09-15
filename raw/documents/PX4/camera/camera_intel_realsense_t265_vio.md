---
title: "Intel® RealSense™ Tracking Camera T265 (VIO)"
type: document
doc_set: PX4
doc_version: main
section: camera
source_url: "https://docs.px4.io/main/en/camera/camera_intel_realsense_t265_vio"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "camera/camera_intel_realsense_t265_vio.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/camera
---

# Intel® RealSense™ Tracking Camera T265 (VIO)

:::tip
This camera is discontinued.
:::

The _Intel® RealSense™ Tracking Camera T265_ provides odometry information that can be used for [VIO](../computer_vision/visual_inertial_odometry.md), augmenting or replacing other positioning systems on PX4.

It is used in the [Visual Inertial Odometry (VIO) > Suggested Setup](../computer_vision/visual_inertial_odometry.md#suggested-setup).

![Intel® RealSense™ Tracking Camera T265 - Angled Image](https://raw.githubusercontent.com/PX4/PX4-Autopilot/main/docs/assets/peripherals/camera_vio/t265_intel_realsense_tracking_camera_photo_angle.jpg)

## Where to Buy

No longer available.

## Setup Instructions

At a high level:

- The [`realsense-ros` wrapper](https://github.com/realsenseai/realsense-ros) provided by Intel should be used to extract the raw data from the camera.
- The camera should be mounted with lenses facing down (default).
  Be sure to specify the camera orientation by publishing the static transform between the `base_link` and `camera_pose_frame` in a ROS launch file, for example:

  ```xml
  <node pkg="tf" type="static_transform_publisher" name="tf_baseLink_cameraPose"
      args="0 0 0 0 1.5708 0 base_link camera_pose_frame 1000"/>
  ```

  This is a static transform that links the camera ROS frame `camera_pose_frame` to the MAVROS drone frame `base_link`.
  - the first three `args` specify _translation_ x,y,z in metres from the center of the flight controller to the camera.
    For example, if the camera is 10cm in front of the controller and 4cm up, the first three numbers would be : [0.1, 0, 0.04,...]
  - the next three `args` specify rotation in radians (yaw, pitch, roll).
    So `[... 0, 1.5708, 0]` means pitch down by 90° (facing the ground). Facing straight forward would be [... 0 0 0].

- The camera is sensitive to high-frequency vibrations!
  It should be soft-mounted with, for example, vibration isolation foam.
