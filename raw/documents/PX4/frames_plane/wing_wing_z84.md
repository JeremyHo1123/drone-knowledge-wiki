---
title: "Wing Wing Z-84 Pixracer Build"
type: document
doc_set: PX4
doc_version: main
section: frames_plane
source_url: "https://docs.px4.io/main/en/frames_plane/wing_wing_z84"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "frames_plane/wing_wing_z84.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/frames-plane
---

# Wing Wing Z-84 Pixracer Build

The Wing Wing Z-84 is a flying wing frame.
It is small, rugged and just large enough to host a [Pixracer](../flight_controller/pixracer.md).

Key information:

- **Frame:** Wing Wing Z-84
- **Flight controller:** Pixracer (Discontinued)

![Wing Wing Z-84 build](https://raw.githubusercontent.com/PX4/PX4-Autopilot/main/docs/assets/airframes/fw/wing_wing/wing_wing_build11.jpg)

## Parts List

### Z-84 Plug n' Fly (PNF/PNP) or Kit

- [Banggood](https://www.banggood.com/Zeta-Wing-Wing-Z-84-Z84-EPO-845mm-Wingspan-Flying-Wing-PNP-p-973125.html?akmClientCountry=America&)

:::tip
PNF (or "PNP") versions include motor, propeller and electronic speed controller.
The "kit" version does not include these components, which must be purchased separately.
:::

### Electronic Speed Controller (ESC)

Any small (>=12A) ESC will do:

- [Lumenier Regler 30A BLHeli_S ESC OPTO](https://www.getfpv.com/lumenier-30a-blheli-s-esc-opto-2-4s.html) (GetFPV)

### Autopilot and Essential Components

- [Pixracer](../flight_controller/pixracer.md) kit (including GPS and power module)
- FrSky D4R-II receiver or equivalent (jumpered to PPM sum output according to its manual)
- _Mini telemetry set_ for Holybro pix32
- _Digital airspeed sensor_ for Holybro pix32 / Pixfalcon
- 1800 mAh 2S LiPo Battery - e.g. Team Orion 1800mAh 7.4V 50C 2S1P with XT 60 plug.

### Recommended spare parts

- 1 cm diameter O-ring for prop saver ([Hobbyking](https://hobbyking.com/en_us/wing-wing-z-84-o-ring-10pcs.html))
- 125x110 mm propellers ([Hobbyking](https://hobbyking.com/en_us/gws-ep-propeller-dd-5043-125x110mm-green-6pcs-set.html))

## Wiring

Wire the servos and motors as shown.
Use the `MAIN` outputs (not the ones labeled with AUX).
The motor controller needs to have an in-built BEC, as the autopilot is not powering the servo rail.

| Port   | Connection                  |
| ------ | --------------------------- |
| RC IN  | PPM or S.BUS / S.BUS2 input |
| MAIN 1 | Left Aileron                |
| MAIN 2 | Right Aileron               |
| MAIN 3 | Empty                       |
| MAIN 4 | Motor 1                     |

## Build Log

The images below give a rough idea about the assembly process, which is simple and can be done with a hot glue gun.

![wing wing build01](https://raw.githubusercontent.com/PX4/PX4-Autopilot/main/docs/assets/airframes/fw/wing_wing/wing_wing_build01.jpg)
![wing wing build02](https://raw.githubusercontent.com/PX4/PX4-Autopilot/main/docs/assets/airframes/fw/wing_wing/wing_wing_build02.jpg)
![wing wing build03](https://raw.githubusercontent.com/PX4/PX4-Autopilot/main/docs/assets/airframes/fw/wing_wing/wing_wing_build03.jpg)
![wing wing build04](https://raw.githubusercontent.com/PX4/PX4-Autopilot/main/docs/assets/airframes/fw/wing_wing/wing_wing_build04.jpg)
![wing wing build09](https://raw.githubusercontent.com/PX4/PX4-Autopilot/main/docs/assets/airframes/fw/wing_wing/wing_wing_build09.jpg)
![Wing Wing Z-84 build](https://raw.githubusercontent.com/PX4/PX4-Autopilot/main/docs/assets/airframes/fw/wing_wing/wing_wing_build11.jpg)

## PX4 Configuration

### Airframe Configuration

Select **Flying Wing > Generic Flying Wing** in the QGroundControl [Airframe Configuration](../config/airframe.md):

![QGC - select firmware for West Wing](https://raw.githubusercontent.com/PX4/PX4-Autopilot/main/docs/assets/airframes/fw/wing_wing/qgc_firmware_flying_wing_west_wing.png)

### Actuator Mapping

Set up the [Actuator Configuration](../config/actuators.md) to match the wiring for the ailerons and throttle as [indicated above](#wiring).

![QGC - set the actuators](https://raw.githubusercontent.com/PX4/PX4-Autopilot/main/docs/assets/airframes/fw/wing_wing/qgc_actuator_config.png)

### Other Configuration

Perform all the the other [Basic Configuration](../config/index.md), including [Autotuning](../config/autotune_fw.md).

Advanced tuning is optional - see [Fixed-wing Vehicle Configuration](../config_fw/index.md).
