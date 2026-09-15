---
title: "MAVLink Console (Analyze View)"
type: document
doc_set: QGC
doc_version: Stable_V5.0
section: analyze_view
source_url: "https://docs.qgroundcontrol.com/Stable_V5.0/en/qgc-user-guide/analyze_view/mavlink_console.html"
upstream_repo: "mavlink/qgroundcontrol"
upstream_path: "analyze_view/mavlink_console.md"
upstream_commit: "cb6ee485e0e11c74ed667ca573e7593f770da436"
ingested: 2026-07-28
tags:
  - docs/qgc
  - docs/qgc/analyze-view
---

# MAVLink Console (Analyze View)

The MAVLink Console (**Analyze > Mavlink Console**) allows you to connect to the PX4 [System Console](https://docs.px4.io/main/en/debug/system_console.html) and send commands.

::: info
The console only works when connected to _hardware_ running the _PX4_ flight stack.
PX4 SITL and ArduPilot are not supported.
:::

::: tip
This is a very useful feature for developers as it allows deep access to the system. In particular, if you are connected via Wifi, you can have this same level of access while the vehicle is flying.
:::

![Analyze View MAVLink Console](https://raw.githubusercontent.com/mavlink/qgroundcontrol/Stable_V5.0/docs/assets/analyze/mavlink_console.jpg)

The view does not display any output except in response to commands.
Once the vehicle is connected, you can enter commands in the bar provided (for a full list of available commands enter: `?`).

Command output is displayed in the view above the command bar.
Click **Show Latest** to jump to the bottom of the command output.
