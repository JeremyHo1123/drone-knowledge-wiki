---
title: "Fixed-wing Vehicle Configuration"
type: document
doc_set: PX4
doc_version: main
section: config_fw
source_url: "https://docs.px4.io/main/en/config_fw/"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "config_fw/index.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/config-fw
---

# Fixed-wing Vehicle Configuration

Fixed-wing configuration and calibration follows the same high level steps as other frames: selection of firmware, configuration of the frame including actuator/motor geometry and output mappings, sensor configuration and calibration, configuration of safety and other features, and finally tuning.

::: info
This topic is the recommended entry point when performing first-time configuration and calibration of a new fixed-wing frame.
:::

The main steps are:

- [Standard Configuration](../config/index.md)
- [Autotune](../config/autotune_fw.md) - PID Tuning

  ::: info
  Autotune simplifies the manual process described in: [Fixed-wing Rate/Attitude Controller Tuning Guide](../config_fw/pid_tuning_guide_fixedwing.md).
  :::

- [Fixed-wing Altitude/Position Controller Tuning Guide](../config_fw/position_tuning_guide_fixedwing.md)
- [Fixed-wing Trimming Guide](../config_fw/trimming_guide_fixedwing.md)
- [Fixed-Wing Airspeed Scale Handling](../config_fw/airspeed_scale_handling.md)
