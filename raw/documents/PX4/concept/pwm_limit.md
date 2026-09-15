---
title: "PWM_limit State Machine"
type: document
doc_set: PX4
doc_version: main
section: concept
source_url: "https://docs.px4.io/main/en/concept/pwm_limit"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "concept/pwm_limit.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/concept
---

# PWM_limit State Machine

The`PWM_limit State Machine` controls PWM outputs as a function of pre-armed and armed inputs.
Provides a delay between assertion of "armed" and a ramp-up of throttle on assertion of the armed signal.

## Quick Summary

**Inputs**

- armed: asserted to enable dangerous behaviors such as spinning propellers
- pre-armed: asserted to enable benign behaviors such as moving control surfaces
- this input overrides the current state
- assertion of pre-armed immediately forces behavior of state ON, regardless of current state
- deassertion of pre-armed reverts behavior to current state

**States**

- INIT and OFF
  - pwm outputs set to disarmed values.
- RAMP
  - pwm outputs ramp from disarmed values to min values.
- ON
  - pwm outputs set according to control values.

## State Transition Diagram

<img src="https://raw.githubusercontent.com/PX4/PX4-Autopilot/main/docs/assets/diagrams/pwm_limit_state_diagram.svg" alt="PWM Limit state machine diagram" class="diagram-invert">
