---
title: Take Off and Land with MAVSDK-Python (Minimal Runnable Example)
type: howto
sources:
  - "[[raw/documents/MAVSDK/system]]"
  - "[[raw/documents/MAVSDK/plugins/action]]"
  - "[[raw/documents/MAVSDK/plugins/telemetry]]"
  - "[[raw/documents/PX4/simulation/index]]"
created: 2026-07-28
updated: 2026-09-15
tags:
  - uav/autonomy
  - stack/mavsdk
  - stack/px4
status: active
doc_version_checked:
  - "MAVSDK 3.17.2@2026-07-28"
  - "PX4 main@9467506"
---

# Take Off and Land with MAVSDK-Python (Minimal Runnable Example)

The shortest path to running the "control a drone from code" chain end to end: connect → wait for health → arm → take off → land. Once this works, moving on to [[wiki/concepts/offboard-control]] makes sense — most offboard failures are really unmet preconditions from this stage.

**Run it in simulation first; don't make a real vehicle your first attempt.** PX4 SITL setup is described in [[raw/documents/PX4/simulation/index]].

## Prerequisites

- PX4 SITL is running, or a real vehicle is connected over a telemetry link
- MAVSDK-Python is installed (notes for installing on a companion computer: [[raw/documents/MAVSDK/jetson-nano-install]])
- Connection address: the SITL default is `udpin://0.0.0.0:14540`, which is also the default of `System.connect()`

## Steps

### 1. Create a System and connect

`System` is the proxy object for all plugins. If `mavsdk_server_address` is not given, a local `mavsdk_server` instance is started automatically.

```python
import asyncio
from mavsdk import System

async def run():
    drone = System()
    await drone.connect(system_address="udpin://0.0.0.0:14540")
```

Supported address formats (see [[raw/documents/MAVSDK/system]]):

| Format | Use |
| --- | --- |
| `serial:///path/to/dev[:baudrate]` | Directly to the flight controller's serial port / USB |
| `udpin://bind_host:bind_port` | Wait for the other side to connect (SITL default) |
| `udpout://dest_host:dest_port` | Connect out actively |
| `tcpin://` / `tcpout://` | TCP versions |

### 2. Wait for the connection and health (**do not skip**)

A connection does not mean the vehicle is ready to fly. The `Health` object from `Telemetry.health()` has seven boolean fields; before takeoff, at least confirm that the position estimate is usable:

- `is_gyrometer_calibration_ok` / `is_accelerometer_calibration_ok` / `is_magnetometer_calibration_ok`
- `is_local_position_ok` — the local position estimate is good enough for position control modes
- `is_global_position_ok` — the global position estimate is good enough for position control modes
- `is_home_position_ok` — the home position has been initialized
- `is_armable` — the system can be armed

```python
    async for state in drone.core.connection_state():
        if state.is_connected:
            break

    async for health in drone.telemetry.health():
        if health.is_global_position_ok and health.is_home_position_ok:
            break
```

**Skipping this is the most common beginner mistake**: calling `arm()` right after connecting, while the flight controller is still waiting for the EKF to converge, so the command is rejected.

### 3. Set the takeoff altitude (optional)

```python
    await drone.action.set_takeoff_altitude(5.0)   # metres above the takeoff point
```

### 4. Arm and take off

```python
    await drone.action.arm()
    await drone.action.takeoff()
    await asyncio.sleep(10)
```

`Action.takeoff()` switches the vehicle to a position control mode, climbs to the configured takeoff altitude and hovers. **The vehicle must be armed before it can take off** — the order cannot be reversed.

`Action.arm()` starts the motors spinning at idle: make sure people are clear before doing this on a real vehicle. `arm_force()` exists for bypassing failed safety checks, but the docs mark it clearly as **for bench testing only, never for normal flight**.

### 5. Land

```python
    await drone.action.land()

asyncio.run(run())
```

## Verification

- QGC's fly view should show the mode change and the altitude change — [[raw/documents/QGC/fly_view/fly_view]]
- From code, subscribe to `drone.telemetry.position()` and `drone.telemetry.armed()` to confirm the state
- All `Action` methods raise `ActionError` on failure, with the reason in the exception message — **catch and inspect it; don't let it fail silently**

## Common failures

| Symptom | Cause | Fix |
| --- | --- | --- |
| `arm()` raises ActionError | Preflight checks failed (position estimate not converged, calibration incomplete) | Wait for the corresponding `health()` fields to become True; details in [[raw/documents/PX4/advanced_config/prearm_arm_disarm]] |
| No telemetry after connecting | Wrong address or port; SITL not running | Check `udpin://0.0.0.0:14540`; test the same link with QGC |
| `takeoff()` does nothing | Not armed | Call `arm()` first |
| A real vehicle arms and immediately disarms | A failsafe triggered | See [[raw/documents/PX4/config/safety]] |

## Safety notes

Before running any automation script on a real vehicle for the first time, make sure failsafes, the geofence and RC takeover are configured and tested. PX4's warnings about automated control are in [[raw/documents/PX4/flight_modes/offboard]].

## Related pages

- [[wiki/concepts/offboard-control]] — the next step: sending custom setpoints
- [[wiki/topics/drone-software-stack]] — where this code sits on the control chain
