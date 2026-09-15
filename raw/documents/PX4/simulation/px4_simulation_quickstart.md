---
title: "PX4 Simulation QuickStart"
type: document
doc_set: PX4
doc_version: main
section: simulation
source_url: "https://docs.px4.io/main/en/simulation/px4_simulation_quickstart"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "simulation/px4_simulation_quickstart.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/simulation
---

# PX4 Simulation QuickStart

First install [Docker](https://docs.docker.com/get-started/get-docker/) (a free tool that runs containers).

The following command will then run a PX4 quadrotor simulation that you can connect to [QGroundControl](https://qgroundcontrol.com), [MAVSDK](https://mavsdk.mavlink.io/) or [ROS 2](../ros2/user_guide.md) (on Linux, macOS, and Windows):

```sh
docker run --rm -it -p 14550:14550/udp px4io/px4-sitl:latest
```

That's it — open [QGroundControl](https://qgroundcontrol.com) and fly!

::: details Trouble connecting to QGC?
This command is recommended for Linux and can also be used on Windows (with recent docker/WSL2).
It uses a different mechanism for connecting to the host ports, and will often work in rare cases where the other command does not.

```sh
docker run --rm -it --network host px4io/px4-sitl:latest
```

:::

::: tip

To try [other vehicle types](../sim_sih/#supported-vehicle-types), use the `-e` flag to pass the `PX4_SIM_MODEL` environment variable to the `docker run` command:

Plane

```sh
docker run --rm -it -p 14550:14550/udp -e PX4_SIM_MODEL=sihsim_airplane px4io/px4-sitl:latest
```

Standard VTOL

```sh
docker run --rm -it -p 14550:14550/udp -e PX4_SIM_MODEL=sihsim_standard_vtol px4io/px4-sitl:latest
```

Ackermann rover

```sh
docker run --rm -it -p 14550:14550/udp -e PX4_SIM_MODEL=sihsim_rover_ackermann px4io/px4-sitl:latest
```

For more information and options see [Container Images](../simulation/px4_sitl_prebuilt_packages.md#container-images) (in _Pre-built SITL Packages_) and [SIH Simulation](../sim_sih/index.md).

:::
