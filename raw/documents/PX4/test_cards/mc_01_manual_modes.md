---
title: "Test MC_01 - Manual Modes"
type: document
doc_set: PX4
doc_version: main
section: test_cards
source_url: "https://docs.px4.io/main/en/test_cards/mc_01_manual_modes"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "test_cards/mc_01_manual_modes.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/test-cards
---

# Test MC_01 - Manual Modes

## Objective

To test that manual flight modes work as expected

## Preflight

Ensure that the drone can go into Stabilized, Altitude, Position mode while still on the ground

## Flight Tests

❏ Stabilized

&nbsp;&nbsp;&nbsp;&nbsp;❏ Pitch/Roll/Yaw response 1:1

&nbsp;&nbsp;&nbsp;&nbsp;❏ Throttle response 1:1

❏ Altitude

&nbsp;&nbsp;&nbsp;&nbsp;❏ Vertical position should hold current value with stick centered

&nbsp;&nbsp;&nbsp;&nbsp;❏ Pitch/Roll/Yaw response 1:1

&nbsp;&nbsp;&nbsp;&nbsp;❏ Throttle response set to Climbs/Descend rate

❏ Position

&nbsp;&nbsp;&nbsp;&nbsp;❏ Horizontal position should hold current value with stick centered

&nbsp;&nbsp;&nbsp;&nbsp;❏ Vertical position should hold current value with stick centered

&nbsp;&nbsp;&nbsp;&nbsp;❏ Throttle response set to Climbs/Descend rate

&nbsp;&nbsp;&nbsp;&nbsp;❏ Pitch/Roll/Yaw response set to Pitch/Roll/Yaw rates

❏ Landing

&nbsp;&nbsp;&nbsp;&nbsp;❏ Land in Position mode with the throttle below 40%

&nbsp;&nbsp;&nbsp;&nbsp;❏ Upon touching ground, copter should disarm automatically within 2 seconds (disarm time set by parameter: [COM_DISARM_LAND](../advanced_config/parameter_reference.md#COM_DISARM_LAND))

## Expected Results

- Take-off should be smooth as throttle is raised
- No oscillations should present in any of the above flight modes
- Upon landing, copter should not bounce on the ground
