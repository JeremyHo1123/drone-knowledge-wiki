---
title: "RaccoonLab Power Connectors and Management Units"
type: document
doc_set: PX4
doc_version: main
section: dronecan
source_url: "https://docs.px4.io/main/en/dronecan/raccoonlab_power"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "dronecan/raccoonlab_power.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/dronecan
---

# RaccoonLab Power Connectors and Management Units

## CAN Power Connectors

CAN power connectors are designed for light unmanned aerial (UAV) and other vehicles for providing power over CAN using [CAN power cables](https://docs.raccoonlab.co/guide/pmu/wires.html).

There are two types of devices:

1. `CAN-MUX` devices provide power from XT30 connector to CAN.
   There are 2 variation of this type of the device with different number of connectors.
2. `Power connector node` is designed to pass current (up to 60A) to power load and CAN, measure voltage and current on load.
   It behaves as Cyphal/DroneCAN node.

Please refer to the RaccoonLab docs [CAN Power Connectors](https://docs.raccoonlab.co/guide/pmu/power/) page.

**Connection example diagram**

Here are the examples:

- The first shows how to use both external high voltage power and 5V CAN power for different nodes with MUX.
  The [NODE](raccoonlab_nodes.md) (the large one in the left diagram) is connected to a high-voltage power source (here 30 V).
  In this case, the [uNODE](raccoonlab_nodes.md) (smaller one on the left schematic) is powered directly from the autopilot.
- The second example shows how to connect multiple [uNODEs](raccoonlab_nodes.md) that are powered by the autopilot (5V).
  If these nodes are powered from a separate DCDC, that DCDC should also be connected to one of these connectors.

![RaccoonLab CAN Power Connector Example Diagram](https://raw.githubusercontent.com/PX4/PX4-Autopilot/main/docs/assets/hardware/power_module/raccoonlab_can/raccoonlab_power_connector_example.png)

## Power Management Unit

![raccoonlab pmu ](https://raw.githubusercontent.com/PX4/PX4-Autopilot/main/docs/assets/hardware/power_module/raccoonlab_can/raccoonlab_pmu.jpg)

This board monitors the battery (voltage and current) and allows control over charging, source and load using he DroneCAN interface.
It might be useful for applications where you need to control the power of the drone including the board computer and charging process.

Please refer to the RaccoonLab docs [Power & Connectivity](https://docs.raccoonlab.co/guide/pmu/) page.

## Where to Buy

[RaccoonLab Store](https://raccoonlab.co/store)

[Cyphal store](https://cyphal.store/search?q=raccoonlab)
