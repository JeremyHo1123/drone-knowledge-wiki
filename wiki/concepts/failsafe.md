---
title: Failsafe
type: concept
sources:
  - "[[raw/documents/PX4/config/safety]]"
  - "[[raw/documents/PX4/config/safety_simulation]]"
  - "[[raw/documents/PX4/advanced_config/flight_termination]]"
  - "[[raw/documents/QGC/setup_view/safety]]"
created: 2026-07-28
updated: 2026-09-15
tags:
  - uav/safety
  - stack/px4
  - stack/qgc
status: active
doc_version_checked:
  - "PX4 main@9467506"
  - "QGC Stable_V5.0@cb6ee48"
---

# Failsafe

A failsafe defines "under which conditions something counts as going wrong, and what the vehicle should do on its own when it does". **This is the one setting you cannot skip before real flights** — every form of automated control (missions, offboard, companion computers) rests on the assumption that the vehicle ends up safe when control is lost.

## The action ladder (increasing severity)

When triggered, **most failsafes by default first enter Hold for `COM_FAIL_ACT_T` seconds**, and then perform the configured action. This delay is deliberately left for the operator to react and take over — switching modes from the RC or the ground station overrides it. **Note: stick movement does not trigger a takeover during failsafe hold**; you must switch modes.

| Action | Behaviour |
| --- | --- |
| None/Disabled | The failsafe is ignored |
| Warning | Only a warning message is sent to the ground station |
| Hold mode | Multicopters hover, fixed-wing aircraft loiter; VTOL depends on its current configuration |
| Return mode | Enters Return mode; behaviour follows the Return settings |
| Land mode | Lands in place; a VTOL transitions to multicopter configuration first |
| Disarm | **Stops the motors immediately** (the vehicle falls if it is airborne) |
| Flight termination | Turns off all controllers and sets all PWM outputs to their failsafe values (`PWM_MAIN_FAILn` / `PWM_AUX_FAILn`), which can deploy a parachute or landing gear; a fixed-wing aircraft may glide to safety |

**When several failsafes trigger at once, the more severe action is taken.** For example, if RC loss is set to Return and GPS loss to Land and both happen together, Land is executed.

## Where to configure it

- **Mainly**: the QGC **Vehicle Setup → Safety** page — battery, RC loss and the other key items, plus the trigger actions for Return and Land
- **Everything else**: parameters only, mostly with the `COM_` prefix (see [[wiki/concepts/px4-parameters]])

## Test it in simulation, not on a real vehicle

PX4 provides a **Failsafe State Machine Simulation** ([[raw/documents/PX4/config/safety_simulation]]) that shows "what actually happens when various failsafe combinations trigger" without flying. It is particularly useful for understanding the "more severe action wins" rule above — combined behaviour is not intuitive, and guessing is unreliable.

For complete testing in simulation, see [[wiki/concepts/sitl-simulation]].

## Relation to programmatic control

When running offboard or companion-computer control, the failsafe is your safety net, and it has dedicated triggers:

- `COM_OF_LOSS_T` — how long the offboard setpoint stream may be interrupted before it counts as lost
- `COM_OBL_RC_ACT` — the action after offboard loss (depends on whether RC is available)

Details in [[wiki/concepts/offboard-control]]. **Check these two parameters before writing automation scripts**; otherwise the vehicle's behaviour when your program crashes is undefined.

## Related pages

- [[wiki/concepts/geofence]] — the failsafe for spatial boundaries
- [[wiki/concepts/offboard-control]] — loss handling for programmatic control
- [[wiki/concepts/flight-modes]] — Hold / Return / Land are themselves flight modes
- [[wiki/concepts/sitl-simulation]] — verifying failsafe combinations in simulation
