---
title: "Airframe Setup (ArduPilot)"
type: document
doc_set: QGC
doc_version: Stable_V5.0
section: setup_view
source_url: "https://docs.qgroundcontrol.com/Stable_V5.0/en/qgc-user-guide/setup_view/airframe_ardupilot.html"
upstream_repo: "mavlink/qgroundcontrol"
upstream_path: "setup_view/airframe_ardupilot.md"
upstream_commit: "cb6ee485e0e11c74ed667ca573e7593f770da436"
ingested: 2026-07-28
tags:
  - docs/qgc
  - docs/qgc/setup-view
---

# Airframe Setup (ArduPilot)

Airframe Setup is used to select the frame class and type that matches your vehicle

::: info
Airframe Setup is only available on _ArduCopter_ and _ArduSub_ vehicles (it is not shown for _ArduPilot_ Rover or Plane vehicles).
:::

## ArduCopter Airframe Setup

To select the airframe in Copter:

1. First select the **Gear** icon (Vehicle Setup) in the top toolbar and then **Airframe** in the sidebar.

   ![Airframe config](https://raw.githubusercontent.com/mavlink/qgroundcontrol/Stable_V5.0/docs/assets/setup/airframe/arducopter.jpg)

1. Select the broad _Frame Class_ for your vehicle:

   ![Airframe type](https://raw.githubusercontent.com/mavlink/qgroundcontrol/Stable_V5.0/docs/assets/setup/airframe/arducopter_class.jpg)

   ::: info
   You will need to reboot the vehicle for class changes to take effect.
   :::

1. Select the specific _Frame Type_ for your vehicle:

   ![Airframe type](https://raw.githubusercontent.com/mavlink/qgroundcontrol/Stable_V5.0/docs/assets/setup/airframe/arducopter_type.jpg)

## ArduSub Frame Setup {#ardusub}

To select the frame type for Sub:

1. First select the **Gear** icon (Vehicle Setup) in the top toolbar and then **Frame** in the sidebar.
1. Select the frame type that matches your vehicle (selecting a frame applies the selection).
1. Make sure that all **green** thrusters have **clockwise** propellers and all **blue** thrusters have **counter-clockwise** propellers (or vice-versa).

   ![Select airframe type](https://raw.githubusercontent.com/mavlink/qgroundcontrol/Stable_V5.0/docs/assets/setup/airframe_ardusub.jpg)

   - You can also click **Load Vehicle Default Parameters** to load default parameter set for ArduSub.

     ![Load vehicle params](https://raw.githubusercontent.com/mavlink/qgroundcontrol/Stable_V5.0/docs/assets/setup/airframe_ardusub_parameters.jpg)
