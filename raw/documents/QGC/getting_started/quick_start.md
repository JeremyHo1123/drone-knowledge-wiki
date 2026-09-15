---
title: "QGroundControl Quick Start"
type: document
doc_set: QGC
doc_version: Stable_V5.0
section: getting_started
source_url: "https://docs.qgroundcontrol.com/Stable_V5.0/en/qgc-user-guide/getting_started/quick_start.html"
upstream_repo: "mavlink/qgroundcontrol"
upstream_path: "getting_started/quick_start.md"
upstream_commit: "cb6ee485e0e11c74ed667ca573e7593f770da436"
ingested: 2026-07-28
tags:
  - docs/qgc
  - docs/qgc/getting-started
---

# QGroundControl Quick Start

Getting _QGroundControl_ up and running is quick and easy:

1. [Download and install (Daily 5.0)](../releases/daily_builds.md) the application.
1. Start _QGroundControl_.
1. Attach your vehicle to the ground station device via USB, through a telemetry radio, or over WiFi. _QGroundControl_ should detect your vehicle and connect to it automatically.

That's it! If the vehicle is ready to fly, _QGroundControl_ should display [Fly View](../fly_view/fly_view.md) as shown below (otherwise it will open [Setup View](../setup_view/setup_view.md)).

![](https://raw.githubusercontent.com/mavlink/qgroundcontrol/Stable_V5.0/docs/assets/quickstart/fly_view_connected_vehicle.jpg)

A good way to become familiar with _QGroundControl_ is to start experimenting:

- Use the View Selector to switch between main views:
  - Plan Flight
  - Analyze Tools
  - Vehicle Configuration
  - Application Settings
- Click the _Status Indicators_ on the toolbar to find out the status of the connected vehicle.

While the UI is fairly intuitive, this documentation can also be referenced to find out more.

::: info
Make sure QGC has an internet connection when you connect a new vehicle in order to display map content.
:::
