---
title: "PX4 Autopilot User Guide"
source: "https://docs.px4.io/main/en/"
author:
published:
created: 2026-07-28
description: "PX4 User and Developer Guide"
tags:
  - "clippings"
---
PX4 is an open-source autopilot for drones and autonomous vehicles. It runs on multirotors, fixed-wing, VTOL, helicopters, rovers, and more. This guide covers everything from assembly and configuration to flight operations and development.

WARNING

This guide is for the *development* version of PX4 (`main` branch). Use the **Version** selector to find the current *stable* version.

Documented changes since the stable release are captured in the evolving [release note](https://docs.px4.io/main/en/releases/main).

## Try PX4

No hardware needed. Run PX4 in simulation with a single command using [Docker or a.deb package](https://docs.px4.io/main/en/simulation/px4_simulation_quickstart). Connect [QGroundControl](https://qgroundcontrol.com/), [MAVSDK](https://mavsdk.mavlink.io/), or [ROS 2](https://docs.px4.io/main/en/ros2/) and start flying immediately.

## For Developers

Want to modify PX4 or build from source? Start with the [Development Guide](https://docs.px4.io/main/en/development/development): set up your [dev environment](https://docs.px4.io/main/en/dev_setup/dev_env), [build the code](https://docs.px4.io/main/en/dev_setup/building_px4), and run [SITL simulation](https://docs.px4.io/main/en/simulation/).

## Getting Started

Start with [Basic Concepts](https://docs.px4.io/main/en/getting_started/px4_basic_concepts) for an overview of the flight stack, flight modes, safety features, and supported hardware.

## Developer Kits

The fastest way to get flying hardware for PX4 development. [Official PX4 Developer Kits](https://docs.px4.io/main/en/dev_kits/) ship with the latest stable PX4 pre-installed on current Pixhawk-standard hardware, need no build skills, and are certified by the PX4 team.

## Build a Vehicle

Pick your frame type: [Multicopter](https://docs.px4.io/main/en/frames_multicopter/), [Fixed-Wing](https://docs.px4.io/main/en/frames_plane/), [VTOL](https://docs.px4.io/main/en/frames_vtol/), [Helicopter](https://docs.px4.io/main/en/frames_helicopter/), or [Rover](https://docs.px4.io/main/en/frames_rover/). Each section covers complete vehicles, kits, and DIY builds. For assembly instructions see [Assembling a Multicopter](https://docs.px4.io/main/en/assembly/assembly_mc) or the equivalent for your frame.

## Configure and Tune

Once assembled, follow the configuration guide for your vehicle type (e.g. [Multicopter Configuration](https://docs.px4.io/main/en/config_mc/)). This covers sensor calibration, flight mode setup, and tuning.

## Hardware

The [Hardware Selection & Setup](https://docs.px4.io/main/en/hardware/drone_parts) section covers flight controllers, sensors, telemetry, RC systems, and payloads. See [Payloads](https://docs.px4.io/main/en/payloads/) for camera and delivery integrations.

## Fly

Read [Operations](https://docs.px4.io/main/en/config/operations) to understand safety features and failsafe behavior before your first flight. Then see [Basic Flying (Multicopter)](https://docs.px4.io/main/en/flying/basic_flying_mc) or the equivalent for your frame type.

## Support

Get help on the [discussion forums](https://discuss.px4.io/) or [Discord](https://discord.com/invite/dronecode). See the [Support](https://docs.px4.io/main/en/contribute/support) page for diagnosing problems, reporting bugs, and joining the [weekly dev call](https://docs.px4.io/main/en/contribute/dev_call).

## Contributing

See the [Contributing](https://docs.px4.io/main/en/contribute/) section for code, [documentation](https://docs.px4.io/main/en/contribute/docs), and [translation](https://docs.px4.io/main/en/contribute/translation) guidelines.

## Translations

There are several [translations](https://docs.px4.io/main/en/contribute/translation) of this guide. Use the language selector in the top navigation.

## License

PX4 code is free to use and modify under the terms of the permissive [BSD 3-clause license](https://opensource.org/license/BSD-3-Clause). This documentation is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). For more information see: [Licences](https://docs.px4.io/main/en/contribute/licenses).

## Calendar & Events

The *Dronecode Calendar* shows important community events for platform users and developers. Select the links below to display the calendar in your timezone (and to add it to your own calendar):

- [Switzerland – Zurich](https://calendar.google.com/calendar/embed?src=linuxfoundation.org_g21tvam24m7pm7jhev01bvlqh8%40group.calendar.google.com&ctz=Europe%2FZurich)
- [Pacific Time – Tijuana](https://calendar.google.com/calendar/embed?src=linuxfoundation.org_g21tvam24m7pm7jhev01bvlqh8%40group.calendar.google.com&ctz=America%2FTijuana)
- [Australia – Melbourne/Sydney/Hobart](https://calendar.google.com/calendar/embed?src=linuxfoundation.org_g21tvam24m7pm7jhev01bvlqh8%40group.calendar.google.com&ctz=Australia%2FSydney)

TIP

The calendar default timezone is Central European Time (CET).

<iframe src="https://calendar.google.com/calendar/embed?title=Dronecode%20Calendar&amp;mode=WEEK&amp;height=600&amp;wkst=1&amp;bgcolor=%23FFFFFF&amp;src=linuxfoundation.org_g21tvam24m7pm7jhev01bvlqh8%40group.calendar.google.com&amp;color=%23691426&amp;ctz=Europe%2FZurich" width="800" height="600" frameborder="0"></iframe>

### Icons

The following icons used in this library are licensed separately (as shown below):

*placeholder* icon made by [Smashicons](https://www.flaticon.com/authors/smashicons "Smashicons") from [www.flaticon.com](https://www.flaticon.com/ "Flaticon") is licensed by [CC 3.0 BY](https://creativecommons.org/licenses/by/3.0/ "Creative Commons BY 3.0").

*camera-automatic-mode* icon made by [Magnific (formerly Freepik)](https://www.magnific.com/ "Magnific") from [www.flaticon.com](https://www.flaticon.com/ "Flaticon") is licensed by [CC 3.0 BY](https://creativecommons.org/licenses/by/3.0/ "Creative Commons BY 3.0").

## Governance

The PX4 Autopilot project is hosted by the [Dronecode Foundation](https://dronecode.org/), a [Linux Foundation](https://www.linuxfoundation.org/) Collaborative Project. Dronecode holds all PX4 trademarks and serves as the project's legal guardian, ensuring vendor-neutral stewardship. No single company owns the name or controls the roadmap. The source code is licensed under the [BSD 3-Clause](https://opensource.org/license/BSD-3-Clause) license, so you are free to use, modify, and distribute it in your own projects.

[![Dronecode Logo](https://docs.px4.io/main/assets/dronecode_logo.CuVYaDse.svg)](https://dronecode.org/)

Doc build time: "2026-07-28T11:27:23.119Z"