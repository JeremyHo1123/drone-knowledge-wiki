---
title: "Test MC_03 - Auto Manual Mix"
type: document
doc_set: PX4
doc_version: main
section: test_cards
source_url: "https://docs.px4.io/main/en/test_cards/mc_03_auto_manual_mix"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "test_cards/mc_03_auto_manual_mix.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/test-cards
---

# Test MC_03 - Auto Manual Mix

## Objective

To test switching between various modes

## Preflight

- Takeoff as first waypoint
- Changes in Altitude throughout the mission
- Last waypoint is a NOT RTL, but a normal waypoint
- Duration of 5 to 6 minutes

## Flight Tests

❏ Position + Mission

&nbsp;&nbsp;&nbsp;&nbsp;❏ Arm and take-off in Position mode

&nbsp;&nbsp;&nbsp;&nbsp;❏ Engage Auto

&nbsp;&nbsp;&nbsp;&nbsp;❏ Observe tracking and cornering

&nbsp;&nbsp;&nbsp;&nbsp;❏ Once mission has completed, switch back to Position mode

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;❏ Horizontal position should hold current value with stick centered

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;❏ Vertical position should hold current value with stick centered

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;❏ Throttle response set to Climbs/Descend rate

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;❏ Pitch/Roll/Yaw response set to Pitch/Roll/Yaw rates

&nbsp;&nbsp;&nbsp;&nbsp;❏ Engage RTL

&nbsp;&nbsp;&nbsp;&nbsp;❏ Upon touching ground, copter should disarm automatically within 2 seconds (disarm time set by parameter: COM_DISARM_LAND)

❏ Mission + Controller interruption

&nbsp;&nbsp;&nbsp;&nbsp;❏ Arm and take-off in Position mode

&nbsp;&nbsp;&nbsp;&nbsp;❏ Engage Auto

&nbsp;&nbsp;&nbsp;&nbsp;❏ Observe tracking and cornering

&nbsp;&nbsp;&nbsp;&nbsp;❏ Before the last waypoint mission is reached, move the control sticks and ensure the vehicle goes into Position flight mode

&nbsp;&nbsp;&nbsp;&nbsp;❏ Manually move the drone over the landing zone

&nbsp;&nbsp;&nbsp;&nbsp;❏ Engage Land mode

&nbsp;&nbsp;&nbsp;&nbsp;❏ Upon touching ground, copter should disarm automatically within 2 seconds (disarm time set by parameter: COM_DISARM_LAND)

## Expected Results

- Take-off should be smooth as throttle is raised
- No oscillations should present in any of the above flight modes
- When moving the control sticks the drone goes into Position flight mode
- Upon landing, copter should not bounce on the ground
