---
title: "Setting up a Developer Environment (Toolchain)"
type: document
doc_set: PX4
doc_version: main
section: dev_setup
source_url: "https://docs.px4.io/main/en/dev_setup/dev_env"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "dev_setup/dev_env.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/dev-setup
---

# Setting up a Developer Environment (Toolchain)

::: tip
You only need a toolchain if you want to **modify and build** PX4 from source.
If you just want to run PX4 simulation without changing the code, use a pre-built [Docker container or .deb package](../simulation/px4_sitl_prebuilt_packages.md) instead.
:::

The _supported platforms_ for PX4 development are:

- [Ubuntu Linux (24.04/22.04)](../dev_setup/dev_env_linux_ubuntu.md)
- [Windows (10/11)](../dev_setup/dev_env_windows_wsl.md) — via WSL2
- [macOS](../dev_setup/dev_env_mac.md)

## Supported Targets

The table below shows what PX4 targets you can build on each OS.

| Target                                                                                                                                 | Linux (Ubuntu) | macOS | Windows |
| -------------------------------------------------------------------------------------------------------------------------------------- | :------------: | :---: | :-----: |
| **NuttX based hardware:** [Pixhawk Series](../flight_controller/pixhawk_series.md), [Crazyflie](../flight_controller/autopilot_discontinued.md) |       ✓        |   ✓   |    ✓    |
| **Linux-based hardware:** [Raspberry Pi 2/3](../flight_controller/raspberry_pi_navio2.md)                                              |       ✓        |       |         |
| **Simulation:** [Gazebo SITL](../sim_gazebo_gz/index.md)                                                                               |       ✓        |   ✓   |    ✓    |
| **Simulation:** ROS 2 with Gazebo                                                                                                      |       ✓        |       |    ✓    |
| **Simulation:** [Gazebo Classic SITL](../sim_gazebo_classic/index.md)                                                                  |                |   ✓   |    ✓    |
| **Simulation:** [ROS with Gazebo Classic](../simulation/ros_interface.md)                                                              |                |       |    ✓    |

Experienced Docker users can also build with the containers used by our continuous integration system: [Docker Containers](../test_and_ci/docker.md)

## Next Steps

Once you have finished setting up one of the command-line toolchains above:

- Install [VSCode](../dev_setup/vscode.md) (if you prefer using an IDE to the command line).
- Install the [QGroundControl Daily Build](../dev_setup/qgc_daily_build.md)
- Continue to [Building PX4 Software](../dev_setup/building_px4.md).
