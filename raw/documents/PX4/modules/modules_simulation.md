---
title: "Modules Reference: Simulation"
type: document
doc_set: PX4
doc_version: main
section: modules
source_url: "https://docs.px4.io/main/en/modules/modules_simulation"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "modules/modules_simulation.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/modules
---

# Modules Reference: Simulation

## simulator_sih

Source: [modules/simulation/simulator_sih](https://github.com/PX4/PX4-Autopilot/tree/main/src/modules/simulation/simulator_sih)

### Description

This module provides a simulator for quadrotors and fixed-wings running fully
inside the hardware autopilot.

This simulator subscribes to "actuator_outputs" which are the actuator pwm
signals given by the control allocation module.

This simulator publishes the sensors signals corrupted with realistic noise
in order to incorporate the state estimator in the loop.

### Implementation

The simulator implements the equations of motion using matrix algebra.
Quaternion representation is used for the attitude.
Forward Euler is used for integration.
Most of the variables are declared global in the .hpp file to avoid stack overflow.

### Usage {#simulator_sih_usage}

```
simulator_sih <command> [arguments...]
 Commands:
   start

   stop

   status        print status info
```
