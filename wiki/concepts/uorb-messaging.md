---
title: uORB Messaging
type: concept
sources:
  - "[[raw/documents/PX4/middleware/uorb]]"
  - "[[raw/documents/PX4/concept/architecture]]"
  - "[[raw/documents/PX4/middleware/dds_topics]]"
created: 2026-07-28
updated: 2026-09-15
tags:
  - uav/comms
  - stack/px4
status: active
doc_version_checked:
  - "PX4 main@9467506"
---

# uORB Messaging

uORB is PX4's internal asynchronous `publish()` / `subscribe()` messaging API, used for all inter-thread and inter-process communication. **PX4 modules never call each other directly; they only exchange uORB messages** — this is how the reactive architecture of [[wiki/topics/px4-flight-stack]] is implemented, and why any module can be replaced at runtime.

It is implemented in the `uorb` module, which is started automatically very early in the boot sequence with `uorb start` (many applications depend on it). Communication between modules is based on **shared memory**.

## Why you will need to touch it

Three situations:

1. **Debugging** — you want to know whether a value is actually being computed and how fast it updates. This is the most common use.
2. **Connecting ROS 2** — uXRCE-DDS bridges selected uORB topics into ROS 2 topics; see [[wiki/concepts/ros2-px4-bridge]].
3. **Writing your own module** — you need a new topic to carry your own data.

## Observing it on the flight controller shell

| Command | Purpose |
| --- | --- |
| `uorb top` | Live update rate of each topic — **the first check for whether data is flowing** |
| `ls /obj` | List all topics |
| `listener <topic> <n>` | Print the next n messages of a topic, e.g. `listener sensor_accel 5` |
| `top` | See which modules are running |
| `<module> start` / `stop` | Start or stop individual modules at runtime |

`listener` is available on most boards from FMUv4 onwards; to confirm for a specific board, check `CONFIG_SYSTEMCMDS_TOPIC_LISTENER` in that board's kconfig.

These commands work in the SITL `pxh>` shell as well (`top` is specific to the NuttX shell), so **understand the data flow in simulation first, then move to the real vehicle**.

## Message definitions and naming

- Message definitions are `.msg` files with **CamelCase names**, placed in `msg/` (versioned ones in `msg/versioned/`) and listed in `msg/CMakeLists.txt`
- By default one definition file corresponds to one topic, and the topic name is **the file name in snake_case**: `TopicName.msg` → topic `topic_name`
- C/C++ code is generated automatically; include the snake_case header (`VelocityLimits` → `velocity_limits.h`) and refer to the topic as `ORB_ID(velocity_limits)` in code
- One definition file can also declare several topics with the same structure (multi-topic)

**When to version**: only messages that are exposed to ROS 2 and must stay compatible across ROS and PX4 versions need versioning. This wiki's [[raw/documents/PX4/msg_docs/index]] contains the complete message reference (284 pages, one per message) — grep that directory to find a topic's fields.

## The publisher sets the update rate

Modules run when they "wait for a message update", so **a driver's publishing rate determines the execution rate of the downstream modules**. Most IMU drivers sample at 1 kHz, integrate and publish at 250 Hz; modules such as `navigator` that don't need high rates run much slower. To see the actual rates, use `uorb top` above.

## Related pages

- [[wiki/topics/px4-flight-stack]] — where uORB fits in the overall architecture
- [[wiki/concepts/ros2-px4-bridge]] — how uORB topics become ROS 2 topics
- [[wiki/concepts/flight-log-analysis]] — logs record uORB topics
