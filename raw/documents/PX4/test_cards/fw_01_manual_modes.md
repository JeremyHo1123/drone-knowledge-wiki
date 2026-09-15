---
title: "Test FW_01 - Manual Modes"
type: document
doc_set: PX4
doc_version: main
section: test_cards
source_url: "https://docs.px4.io/main/en/test_cards/fw_01_manual_modes"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "test_cards/fw_01_manual_modes.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/test-cards
---

# Test FW_01 - Manual Modes

## Objective

To test that manual flight modes work as expected for fixed wing vehicles.

## Preflight

Ensure that the vehicle can go into Stabilized, Altitude, and Position mode while still on the ground.

## Flight Tests

❏ Stabilized

&nbsp;&nbsp;&nbsp;&nbsp;❏ Wings level with stick centered

&nbsp;&nbsp;&nbsp;&nbsp;❏ Pitch/Roll response with correct bank angle limits

&nbsp;&nbsp;&nbsp;&nbsp;❏ Yaw coordination

&nbsp;&nbsp;&nbsp;&nbsp;❏ Throttle response 1:1

❏ Altitude

&nbsp;&nbsp;&nbsp;&nbsp;❏ Altitude should hold current value with stick centered

&nbsp;&nbsp;&nbsp;&nbsp;❏ Pitch input controls climb/descend rate

&nbsp;&nbsp;&nbsp;&nbsp;❏ Throttle automatically managed to maintain airspeed

&nbsp;&nbsp;&nbsp;&nbsp;❏ Roll/Yaw respond correctly to stick movement

❏ Position

&nbsp;&nbsp;&nbsp;&nbsp;❏ Vehicle should hold current heading and loiter with stick centered

&nbsp;&nbsp;&nbsp;&nbsp;❏ Altitude should hold current value

&nbsp;&nbsp;&nbsp;&nbsp;❏ Roll input commands heading change

## Expected Results

- Takeoff should be smooth (hand launch or runway)
- No oscillations should be present in any of the above flight modes
- Vehicle should maintain stable flight throughout all mode transitions
- Landing approach should be stable and controllable
