---
title: The Drone Software Stack (PX4 / MAVLink / QGC / MAVSDK)
type: topic
sources:
  - "[[raw/documents/PX4/getting_started/px4_basic_concepts]]"
  - "[[raw/documents/PX4/concept/architecture]]"
  - "[[raw/documents/PX4/mavlink/index]]"
  - "[[raw/documents/MAVSDK/system]]"
  - "[[raw/documents/QGC/getting_started/quick_start]]"
created: 2026-07-28
updated: 2026-09-15
tags:
  - uav/comms
  - stack/px4
  - stack/qgc
  - stack/mavsdk
  - stack/mavlink
status: active
doc_version_checked:
  - "PX4 main@9467506"
  - "QGC Stable_V5.0@cb6ee48"
---

# The Drone Software Stack (PX4 / MAVLink / QGC / MAVSDK)

The three sets of official documentation in this wiki are not three independent subjects; they are **three positions on the same control chain**. Knowing who sits at which layer, and who talks to whom, is a prerequisite for everything else — much of the confusion over "where is this feature actually configured" comes down to mixing up the layers.

## Layers

| Layer | Role | Runs on | Docs in this wiki |
| --- | --- | --- | --- |
| **Flight controller firmware** | PX4 Autopilot: estimates state, runs the control loops, drives actuators, executes failsafes | Flight controller board (Pixhawk and others), hard real-time | [[docs-map/px4\|PX4 index]] (961 pages) |
| **Communication protocol** | MAVLink: the format and semantics of every message between the flight controller and the outside world | On top of serial / UDP / TCP | [[raw/documents/PX4/mavlink/index]] |
| **Ground station** | QGroundControl: the human interface — setup, calibration, mission planning, flight monitoring, log download | Laptop / tablet | [[docs-map/qgc\|QGC index]] (73 pages) |
| **Programmatic control** | MAVSDK: commands and telemetry subscriptions from code (this wiki holds the Python version) | Companion computer or ground computer | [[docs-map/mavsdk\|MAVSDK index]] (41 pages) |

Key fact: **QGC and MAVSDK are two parallel MAVLink clients, not an upper and a lower layer.** Both talk to PX4 over MAVLink and their capabilities overlap heavily — one is made for people, the other for programs. That is why many operations "can be clicked in QGC and also called from MAVSDK".

## Which layer a decision belongs to

To work out where to look for any feature, ask three questions:

1. **Is it something the vehicle must be able to do by itself?** (attitude stabilization, position hold, failsafes, mode switching logic) → PX4, usually in the form of a **parameter**. Example: `COM_OF_LOSS_T` decides how long an offboard signal interruption may last before it counts as lost.
2. **Is it something a person needs to see or click?** (calibration, mission planning, video streaming, log download) → QGC.
3. **Does it need automation or your own algorithms?** (deciding where to fly from sensor results, running custom control laws) → MAVSDK or ROS 2.

The third category is where people trip up most: **whether the program can issue a command depends on whether PX4 is in a mode that allows it and whether its preconditions are met**. MAVSDK call failures are usually not API misuse but the wrong flight controller state. Details in [[wiki/concepts/offboard-control]].

## MAVSDK architecture notes

MAVSDK-Python is not a pure Python implementation — the `System` object is a gRPC proxy for `mavsdk_server` (the C++ core). If no existing server address is given when `System()` is created, one is started locally. The default connection address is `udpin://0.0.0.0:14540` (PX4 SITL's default offboard port), and five formats are supported: `serial://`, `udpin://`, `udpout://`, `tcpin://` and `tcpout://`.

Functionality is split into **plugins**, each a property of `System`: `system.action`, `system.telemetry`, `system.offboard`, `system.mission`, … Of this wiki's 41 MAVSDK pages, 39 are the API references of individual plugins. All methods are `async`, and telemetry methods return async generators.

## Watch out for version gaps

This wiki's PX4 docs track `main` (the development branch), and QGC tracks `Stable_V5.0`. This means **the behaviour described in the PX4 docs may be ahead of the stable firmware on your vehicle**. Any answer involving "does this parameter exist" or "how does this mode behave" has to account for that gap; when needed, check [[raw/documents/PX4/releases/index]] for the release that introduced a feature.

## Related pages

- [[wiki/concepts/offboard-control]] — the entry mode for programmatic control, and where the three layers interact most
- [[wiki/howto/mavsdk-takeoff-and-land]] — a minimal example that runs the whole chain once
