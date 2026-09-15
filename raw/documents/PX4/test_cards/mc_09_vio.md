---
title: "Test MC_09 - VIO (Visual-Inertial Odometry)"
type: document
doc_set: PX4
doc_version: main
section: test_cards
source_url: "https://docs.px4.io/main/en/test_cards/mc_09_vio"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "test_cards/mc_09_vio.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/test-cards
---

# Test MC_09 - VIO (Visual-Inertial Odometry)

## Objective

Test that external vision (VIO) works as expected

## Preflight

Disconnect all GPS / compasses and ensure vehicle is using VIO for navigation

Ensure that the drone can go into [Altitude](../flight_modes_mc/altitude.md) / [Position](../flight_modes_mc/position.md) mode while still on the ground

Ensure there are no other sources of positioning besides VIO:

- [EKF2_OF_CTRL](../advanced_config/parameter_reference.md#EKF2_OF_CTRL): `0`
- [EKF2_GPS_CTRL](../advanced_config/parameter_reference.md#EKF2_GPS_CTRL): `0`
- [EKF2_EV_CTRL](../advanced_config/parameter_reference.md#EKF2_EV_CTRL): `15`
- [SYS_HAS_MAG](../advanced_config/parameter_reference.md#SYS_HAS_MAG): `0`

## Flight Tests

❏ [Altitude mode](../flight_modes_mc/altitude.md)

&nbsp;&nbsp;&nbsp;&nbsp;❏ Vertical position should hold current value with stick centered

&nbsp;&nbsp;&nbsp;&nbsp;❏ Pitch/Roll/Yaw response 1:1

&nbsp;&nbsp;&nbsp;&nbsp;❏ Throttle response set to climb/descent rate

❏ [Position mode](../flight_modes_mc/position.md)

&nbsp;&nbsp;&nbsp;&nbsp;❏ Horizontal position should hold current value with stick centered

&nbsp;&nbsp;&nbsp;&nbsp;❏ Vertical position should hold current value with stick centered

&nbsp;&nbsp;&nbsp;&nbsp;❏ Throttle response set to climb/descent rate

&nbsp;&nbsp;&nbsp;&nbsp;❏ Pitch/Roll/Yaw response set to pitch/roll/yaw rates

## Landing

❏ Land in either Position or Altitude mode with the throttle below 40%

❏ Upon touching ground, copter should disarm automatically within 2 seconds (default: see [COM_DISARM_LAND](../advanced_config/parameter_reference.md#COM_DISARM_LAND))

## Expected Results

- Take-off should be smooth as throttle is raised
- Drone should hold altitude in Altitude mode without wandering
- Drone should hold position within 1 meter in Position mode without pilot moving sticks
- No oscillations should present in any of the above flight modes
- Upon landing, copter should not bounce on the ground
