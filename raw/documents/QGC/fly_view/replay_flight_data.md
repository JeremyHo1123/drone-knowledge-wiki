---
title: "Replay Flight Data"
type: document
doc_set: QGC
doc_version: Stable_V5.0
section: fly_view
source_url: "https://docs.qgroundcontrol.com/Stable_V5.0/en/qgc-user-guide/fly_view/replay_flight_data.html"
upstream_repo: "mavlink/qgroundcontrol"
upstream_path: "fly_view/replay_flight_data.md"
upstream_commit: "cb6ee485e0e11c74ed667ca573e7593f770da436"
ingested: 2026-07-28
tags:
  - docs/qgc
  - docs/qgc/fly-view
---

# Replay Flight Data

::: warning
This feature is intended primarily for **autopilot developers**/**vehicle creators**.
It is only supported on desktop builds (Windows, Linux, Mac OS).
:::

The _Replay Flight Data_ feature allows users to replay a telemetry log, enabling review of past or problematic flights.
The flight can be started, paused, stopped, restarted etc.

::: info
_QGroundControl_ treats flight replay like an active connection.
When you pause/stop playing, the ground station will report "Communication Lost" and wait for disconnection or for more messages.
:::

To replay a flight:

1. Disconnect any active connections.
1. Select **Application Settings > General > Fly View**
1. Check **Show Telemetry Log Replay Status Bar** to toggle the flight replay bar at the bottom of the screen.

   ![Toggle Flight Replay](https://raw.githubusercontent.com/mavlink/qgroundcontrol/Stable_V5.0/docs/assets/fly/flight_replay/flight_replay_toggle.jpg)

1. Select the **Load Telemetry Log** button in the bar to display a _file selection_ dialog.
   - Choose a log file to replay from the available telemetry logs.
   - _QGroundControl_ will immediately start playing the log.
1. When a log is loaded you can use the:
   - **Pause/Play** button to pause and restart playing.
   - _Slider_ to drag to a new position in the log.
   - _Rate_ selector to choose the playback speed.
1. To stop replay (i.e. to load a new file to replay), first pause the flight, and then select **Disconnect** (when it appears).
   After disconnecting, the **Load Telemetry Log** button will be displayed.

:::tip
You can inspect the running replay in more detail using the [MAVLink Inspector](../analyze_view/mavlink_inspector.md).
:::
