---
title: "Gazebo Classic Vehicles"
type: document
doc_set: PX4
doc_version: main
section: sim_gazebo_classic
source_url: "https://docs.px4.io/main/en/sim_gazebo_classic/vehicles"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "sim_gazebo_classic/vehicles.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/sim-gazebo-classic
---

# Gazebo Classic Vehicles

This topic lists/displays the vehicles supported by the PX4 [Gazebo Classic](../sim_gazebo_classic/index.md) simulation and the `make` commands required to run them (the commands are run from a terminal in the **PX4-Autopilot** directory).

Supported vehicle types include: mutirotors, VTOL, VTOL Tailsitter, Plane, Rover, Submarine/UUV.

::: info
The [Gazebo Classic](../sim_gazebo_classic/index.md) page shows how to install Gazebo Classic, how to enable video and load custom maps, and many other configuration options.
:::

## Multicopter

### Quadrotor (Default)

```sh
make px4_sitl gazebo-classic
```

### Quadrotor with Optical Flow

```sh
make px4_sitl gazebo-classic_iris_opt_flow
```

### Quadrotor with Depth Camera

These models have a depth camera attached, modelled on the Intel® RealSense™ D455.

_Forward-facing depth camera:_

```sh
make px4_sitl gazebo-classic_iris_depth_camera
```

_Downward-facing depth camera:_

```sh
make px4_sitl gazebo-classic_iris_downward_depth_camera
```

### 3DR Solo (Quadrotor)

```sh
make px4_sitl gazebo-classic_solo
```

![3DR Solo in Gazebo Classic](https://raw.githubusercontent.com/PX4/PX4-Autopilot/main/docs/assets/simulation/gazebo_classic/vehicles/solo.png)

### Typhoon H480 (Hexrotor)

```sh
make px4_sitl gazebo-classic_typhoon_h480
```

![Typhoon H480 in Gazebo Classic](https://raw.githubusercontent.com/PX4/PX4-Autopilot/main/docs/assets/simulation/gazebo_classic/vehicles/typhoon.jpg)

::: info
This target also supports [video streaming simulation](../sim_gazebo_classic/index.md#video-streaming).
:::

<a id="fixed_wing"></a>

## Plane/Fixed-wing

### Standard Plane

```sh
make px4_sitl gazebo-classic_plane
```

![Plane in Gazebo Classic](https://raw.githubusercontent.com/PX4/PX4-Autopilot/main/docs/assets/simulation/gazebo_classic/vehicles/plane.png)

#### Standard Plane with Catapult Launch

```sh
make px4_sitl gazebo-classic_plane_catapult
```

This model simulates hand/catapult launch, which can be used for [fixed-wing takeoff](../flight_modes_fw/takeoff.md) in position mode, takeoff mode, or missions.

The plane will automatically be launched as soon as the vehicle is armed.

## VTOL

### Standard VTOL

```sh
make px4_sitl gazebo-classic_standard_vtol
```

![Standard VTOL in Gazebo Classic](https://raw.githubusercontent.com/PX4/PX4-Autopilot/main/docs/assets/simulation/gazebo_classic/vehicles/standard_vtol.png)

### Tailsitter VTOL

```sh
make px4_sitl gazebo-classic_tailsitter
```

![Tailsitter VTOL in Gazebo Classic](https://raw.githubusercontent.com/PX4/PX4-Autopilot/main/docs/assets/simulation/gazebo_classic/vehicles/tailsitter.png)

## Unmanned Underwater Vehicle (UUV/Submarine)

### HippoCampus TUHH UUV

```sh
make px4_sitl gazebo-classic_uuv_hippocampus
```

![Submarine/UUV](https://raw.githubusercontent.com/PX4/PX4-Autopilot/main/docs/assets/simulation/gazebo_classic/vehicles/hippocampus.png)

## Unmanned Surface Vehicle (USV/Boat)

<a id="usv_boat"></a>

### Boat (USV)

```sh
make px4_sitl gazebo-classic_boat
```

![Boat/USV](https://raw.githubusercontent.com/PX4/PX4-Autopilot/main/docs/assets/simulation/gazebo_classic/vehicles/boat.png)

<a id="airship"></a>

## Airship

### Cloudship

```sh
make px4_sitl gazebo-classic_cloudship
```

![Airship](https://raw.githubusercontent.com/PX4/PX4-Autopilot/main/docs/assets/simulation/gazebo_classic/vehicles/airship.png)
