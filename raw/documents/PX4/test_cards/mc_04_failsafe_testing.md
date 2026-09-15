---
title: "Test MC_04 - Failsafe Testing"
type: document
doc_set: PX4
doc_version: main
section: test_cards
source_url: "https://docs.px4.io/main/en/test_cards/mc_04_failsafe_testing"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "test_cards/mc_04_failsafe_testing.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/test-cards
---

# Test MC_04 - Failsafe Testing

## Objective

Test RC loss, data link loss, and low battery failsafes.

## Preflight

- Verify RC Loss action is Return to Land
- Verify Data Link Loss action is Return to Land and the timeout is 10 seconds
- Verify Battery failsafe
  - Action is Return to Land
  - Battery Warn Level is 25%
  - Battery Failsafe Level is 20%
  - Battery Emergency Level is 15%

## Flight Tests

❏ RC loss

&nbsp;&nbsp;&nbsp;&nbsp;❏ Take off in Altitude mode

&nbsp;&nbsp;&nbsp;&nbsp;❏ Move at least 20 meters away home position

&nbsp;&nbsp;&nbsp;&nbsp;❏Turn off RC and check the vehicle returns to home position, wait for the descent and turn on the RC and take over.

❏ Datalink Loss

&nbsp;&nbsp;&nbsp;&nbsp;❏ Disconnect telemetry, vehicle should return to home position after 10 seconds, wait for the descent and reconnect the telemetry radio

❏ Battery Failsafe

&nbsp;&nbsp;&nbsp;&nbsp;❏ Confirm the warning message is received in QGC

&nbsp;&nbsp;&nbsp;&nbsp;❏ Confirm the vehicle returns to land on failsafe level

&nbsp;&nbsp;&nbsp;&nbsp;❏ Confirm the vehicle lands on emergency land level
