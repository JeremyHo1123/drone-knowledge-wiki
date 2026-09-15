---
title: "Sensor/Topic Debugging using the Listener Command"
type: document
doc_set: PX4
doc_version: main
section: debug
source_url: "https://docs.px4.io/main/en/debug/sensor_uorb_topic_debugging"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "debug/sensor_uorb_topic_debugging.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/debug
---

# Sensor/Topic Debugging using the Listener Command

The uORB is an asynchronous `publish()` / `subscribe()` messaging API used for
inter-thread/inter-process communication. The `listener` command can be used from the _QGroundControl MAVLink Console_ to inspect topic (message) values, including the current values published by sensors.

:::tip
This is a powerful debugging tool because it can be used even when QGC is connected over a wireless link (e.g. when the vehicle is flying).
:::

::: info
The `listener` command is also available through the [System Console](../debug/system_console.md) and the [MAVLink Shell](../debug/mavlink_shell.md).
:::

:::tip
To check what topics are available at what rate, just use the `uorb top` command.
:::

The image below demonstrates _QGroundControl_ being used to get the value of the acceleration sensor.

![QGC MAVLink Console](https://raw.githubusercontent.com/PX4/PX4-Autopilot/main/docs/assets/gcs/qgc_mavlink_console_listener_command.png)

For more information about how to determine what topics are available and how to call `listener` see: [uORB Messaging > Listing Topics and Listening in](../middleware/uorb.md#listing-topics-and-listening-in).
