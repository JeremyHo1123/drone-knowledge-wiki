---
title: Collision Prevention
type: concept
sources:
  - "[[raw/documents/PX4/computer_vision/collision_prevention]]"
  - "[[raw/documents/PX4/computer_vision/path_planning_interface]]"
  - "[[raw/documents/PX4/flight_modes_mc/position]]"
created: 2026-07-28
updated: 2026-09-15
tags:
  - uav/perception
  - uav/navigation
  - uav/safety
  - stack/px4
status: active
doc_version_checked:
  - "PX4 main@9467506"
---

# Collision Prevention

Automatically slows the vehicle down and stops it before it hits an obstacle. **Be clear about what it is: collision *prevention*, not obstacle *avoidance*** — it never plans a way around anything; it only refuses to let you fly into it. Actively routing around obstacles requires path planning; see "Difference from obstacle avoidance" below.

## Enabling conditions (stricter than you might expect)

- **Multicopters only** (or a VTOL in multicopter configuration)
- **Position mode only**, and `MPC_POS_MODE` must be set to **Acceleration based**
- Sensor data can come from a companion computer, an off-board rangefinder over MAVLink, a rangefinder connected directly to the flight controller, or any combination of these

## Two side effects that will bite

The official docs call these out explicitly, and you will run into them in practice:

1. **If the sensors' range is too short, the vehicle's maximum speed is limited.** It will not fly fast towards what it cannot see far enough — the unavoidable price of safety.
2. **Movement is blocked in any direction without sensor data.** Without a rear-facing sensor, the vehicle **cannot move backwards at all**.

Hence the docs give two opposite hints: if you want to fly fast, disable it when you don't need it; if you enable it, **make sure every direction you intend to fly is covered by a sensor**.

## How it works

- The closer the vehicle gets to an obstacle, the tighter the speed limit, and the acceleration setpoint is adjusted to exclude trajectories that would lead to a collision
- **To move away from or parallel to an obstacle, the user must actively command a setpoint that does not bring the vehicle closer to it** — it will not pick an escape direction for you
- The algorithm only makes **small adjustments** within a fixed margin on either side of the requested setpoint, when it determines that a "better" setpoint exists in that range
- While it is actively limiting speed, the user is notified through QGC

## Difference from obstacle avoidance / path planning

| | Collision Prevention | Path-planning obstacle avoidance |
| --- | --- | --- |
| Behaviour | Slows down, stops, blocks unsafe directions | Actively routes around obstacles |
| Runs on | Built into PX4 (flight controller) | Companion computer, connected through [[raw/documents/PX4/computer_vision/path_planning_interface]] |
| Mode | Position mode (manual) | Mission / autonomous modes |

**This is also where research and implementation diverge**: obstacle avoidance in academia is mostly a planning problem (generate a collision-free trajectory), while the PX4 mainline only ships a reactive speed limiter. A real planner has to run on a companion computer and plug in through the path planning interface.

## Related pages

- [[wiki/concepts/visual-inertial-odometry]] — the same "companion computer computes, PX4 consumes" pattern
- [[wiki/concepts/flight-modes]] — how Position mode relates to `MPC_POS_MODE`
- [[wiki/concepts/failsafe]] — the last line of defence when collision prevention is not enough
