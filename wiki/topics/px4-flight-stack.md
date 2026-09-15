---
title: PX4 System Architecture and Flight Stack
type: topic
sources:
  - "[[raw/documents/PX4/concept/architecture]]"
  - "[[raw/documents/PX4/flight_stack/controller_diagrams]]"
  - "[[raw/documents/PX4/middleware/index]]"
created: 2026-07-28
updated: 2026-09-15
tags:
  - uav/flight-control
  - stack/px4
status: active
doc_version_checked:
  - "PX4 main@9467506"
---

# PX4 System Architecture and Flight Stack

PX4 has two main layers: the **flight stack** (estimation and flight control) and the **middleware** (a general robotics layer: drivers, communication, simulation). All vehicle types — multicopters, fixed-wing aircraft, VTOL, helicopters, rovers and boats — **share a single code base**; the differences are absorbed by configuration and control allocation, not by separate firmware branches.

Understanding this layering tells you which knob to turn for a given problem: a bad estimate is the estimator's business, jitter is the rate controller's, and a motor spinning the wrong way is control allocation's.

## Reactive design and uORB

The whole system is **reactive**: functionality is split into replaceable modules, and modules communicate asynchronously **only through the uORB publish/subscribe message bus**, never by calling each other directly. Three practical consequences:

- Modules can be started and stopped individually **at runtime** (`<module_name> start/stop` in the shell; `top` shows what is running)
- Update rates are set by the **publishing driver**: most IMU drivers sample at 1 kHz, integrate and publish at 250 Hz; modules such as `navigator` that don't need high rates run much slower
- To observe the actual system behaviour, `uorb top` shows each topic's update rate live

Details in [[wiki/concepts/uorb-messaging]].

## Flight stack data flow

From sensors to motors in one line:

```
Sensors / RC input
   ↓
Estimator (EKF2) — one or more sensor inputs → vehicle state
   ↓
Navigator / flight mode — generates setpoints
   ↓
Position controller → Velocity controller → Attitude controller → Rate controller
   ↓
Control allocation (mixing) — torque/thrust → individual motor and servo commands
   ↓
Output drivers (PWM / DShot / DroneCAN …)
```

The official definitions of the three roles are precise and worth remembering as written:

- **Estimator**: takes one or more sensor inputs and combines them into the vehicle state (e.g. computing attitude from IMU data)
- **Controller**: takes a setpoint and a measurement or estimate, and outputs a correction that moves the process towards the setpoint. For example, the position controller takes a position setpoint, uses the current estimated position as the process variable, and outputs **attitude and thrust setpoints**
- **Mixer** (now called control allocation): translates force/torque commands such as "turn right" into individual motor commands while making sure limits are not exceeded. The translation depends on the vehicle geometry — the arrangement of the motors relative to the centre of gravity, the moments of inertia, and so on

## The multicopter controllers are cascaded

A standard cascaded control structure, from the outside in: position → velocity → attitude → rate, mixing P and PID controllers. Practical points:

- **The outer (position) loop is bypassed depending on the mode** — it is active only while holding position or when a velocity of zero is requested on an axis. This is why changing position gains has no noticeable effect in manual modes
- The velocity controller outputs an **acceleration** command and does **not saturate** it; saturation happens later, when it is converted into a thrust setpoint, together with the maximum tilt angle
- The acceleration → thrust/attitude conversion has a priority: the vertical thrust `thrust_z` is computed first and saturated with `MPC_THR_MAX`, and the horizontal thrust then gets `(MPC_THR_MAX² − thrust_z²)^0.5`. **Vertical takes priority over horizontal** — a deliberate trade-off, since losing altitude is more serious than drifting off course
- The attitude controller uses quaternions; the rate controller is a K-PID with limited integral authority to prevent wind-up

Fixed-wing aircraft take an entirely different route: **TECS (Total Energy Control System)** controls true airspeed and altitude together and outputs throttle and pitch setpoints to the attitude controller. So **poor airspeed or altitude tracking is often rooted in a badly tuned pitch loop**, not in TECS itself.

The gain parameters of each layer and the tuning order are in [[wiki/concepts/pid-tuning]]; the complete block diagrams are in [[raw/documents/PX4/flight_stack/controller_diagrams]].

## Middleware

Mainly embedded sensor drivers, external communication (companion computers, ground stations) and the uORB bus itself. **The simulation layer is also part of the middleware** — which is why the same flight code can run as SITL on a desktop and control a simulated vehicle; see [[wiki/concepts/sitl-simulation]].

## Runtime environment

PX4 runs on any operating system that provides a POSIX API (Linux, macOS, NuttX, QuRT) and needs some form of real-time scheduling (such as FIFO). Communication between modules is based on **shared memory**.

## Related pages

- [[wiki/concepts/uorb-messaging]] — how modules communicate
- [[wiki/concepts/control-allocation]] — how torque commands become motor commands
- [[wiki/concepts/ekf2]] — where the state comes from
- [[wiki/concepts/flight-modes]] — where the setpoints come from
- [[wiki/concepts/px4-parameters]] — the entry point to every knob
- [[wiki/topics/drone-software-stack]] — one layer further out: how PX4 relates to QGC and MAVSDK
