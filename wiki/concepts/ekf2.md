---
title: EKF2 State Estimator
type: concept
sources:
  - "[[raw/documents/PX4/advanced_config/tuning_the_ecl_ekf]]"
  - "[[raw/documents/PX4/flight_stack/controller_diagrams]]"
  - "[[raw/documents/PX4/advanced_config/parameter_reference]]"
created: 2026-07-28
updated: 2026-09-15
tags:
  - uav/state-estimation
  - stack/px4
status: active
doc_version_checked:
  - "PX4 main@9467506"
---

# EKF2 State Estimator

PX4's navigation filter: an Extended Kalman Filter that fuses sensor measurements to produce the vehicle state needed by the control loops. **It sets the upper bound on control quality for the entire flight stack** — if the estimate is wrong, no controller can save you. That is why debugging "it doesn't fly steadily" always starts with the estimator, and only then the controllers.

## States it estimates

| State | Unit |
| --- | --- |
| Quaternion (rotation from the NED navigation frame to the XYZ body frame) | — |
| Velocity at the IMU (North / East / Down) | m/s |
| Position at the IMU (latitude rad, longitude rad, altitude m) | — |
| IMU gyro bias X/Y/Z | rad/s |
| IMU accelerometer bias X/Y/Z | m/s² |
| Earth magnetic field components N/E/D | gauss |
| Body-frame magnetic field bias X/Y/Z | gauss |
| Wind velocity N/E | m/s |
| Terrain height | m |

**Gyro and accelerometer biases are estimated states, not calibration constants** — which is why the estimate improves after the vehicle has sat still and warmed up for a while.

## Three design choices (they determine how it behaves and how to tune it)

### 1. Error-state formulation

An error-state formulation is used for numerical stability, which matters especially for rotation uncertainty (rotation uncertainty lives in the tangent space of SO(3): a 3D vector rather than a 4D quaternion). The covariance update uses the **Joseph stabilized form**, which improves numerical stability and allows conditional updates of independent states. The algebra for covariance prediction and the measurement Jacobians is generated symbolically with **SymForce**.

### 2. Delayed fusion time horizon

**This is the key to understanding EKF2 parameters.** Each sensor has a different delay relative to the IMU, so the EKF **runs at a point in the past**: each sensor's data goes into a FIFO buffer, and the EKF takes it out at the correct time.

- Per-sensor delay compensation is controlled by the `EKF2_*_DELAY` parameters
- The delay of the fusion time horizon and the buffer length are set by `EKF2_DELAY_MAX`, **which must be at least as large as the longest `EKF2_*_DELAY`**
- A complementary filter then propagates the state from the fusion time horizon to the current time, with time constants set by `EKF2_TAU_VEL` and `EKF2_TAU_POS`
- **Reducing the fusion time horizon delay reduces the errors introduced by the complementary filter's forward prediction**

### 3. The IMU is used only for prediction

IMU data is **not used as an observation** in the EKF derivation; it is only used for state prediction (propagation). Observations come from GNSS, magnetometer, barometer, vision, optical flow and so on.

## Details of the position output

- Position is estimated as latitude/longitude/altitude, and INS integration is done on the WGS84 ellipsoid; the position uncertainty, however, is defined in a **local navigation frame** (NED, metres) at the current position
- Before output to the control loops, position and velocity are **corrected for the offset between the IMU and the body frame origin**, set with `EKF2_IMU_POS_X/Y/Z` — **fill these in whenever the IMU is not at the centre of gravity**
- Besides the global position, the filter produces a local position estimate (NED metres) using an **azimuthal equidistant projection**. The projection origin is set automatically when global position measurements are fused, or can be set manually
- **Without any global position information only the local position is available**, and INS integration uses a spherical Earth model instead

## Single vs. multiple instances

**A single EKF instance runs by default**: sensor selection and failover happen before the data reaches the EKF. This protects against a limited set of sensor faults (such as data loss), but **not against a sensor that keeps reporting inaccurate data** — that exceeds what the EKF and the control loops can compensate for. Consider multiple instances only when you need stronger fault tolerance.

## Related pages

- [[wiki/topics/px4-flight-stack]] — where EKF2 sits in the data flow
- [[wiki/concepts/visual-inertial-odometry]] — the position source fed to EKF2 without GNSS
- [[wiki/concepts/rtk-gnss]] — centimetre-level position measurements
- [[wiki/concepts/px4-parameters]] — how to look up `EKF2_` parameters
- [[wiki/concepts/flight-log-analysis]] — estimation quality is diagnosed from flight logs
