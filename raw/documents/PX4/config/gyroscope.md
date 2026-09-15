---
title: "Gyroscope Calibration"
type: document
doc_set: PX4
doc_version: main
section: config
source_url: "https://docs.px4.io/main/en/config/gyroscope"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "config/gyroscope.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/config
---

# Gyroscope Calibration

_QGroundControl_ will guide you to place the vehicle on a flat surface and keep it still.

## Performing the Calibration

The calibration steps are:

1. Start _QGroundControl_ and connect the vehicle.
1. Select **"Q" icon > Vehicle Setup > Sensors** (sidebar) to open _Sensor Setup_.
1. Click the **Gyroscope** sensor button.

   ![Select Gyroscope calibration PX4](https://raw.githubusercontent.com/PX4/PX4-Autopilot/main/docs/assets/qgc/setup/sensor/gyroscope_calibrate_px4.png)

1. Place the vehicle on a surface and leave it still.
1. Click **Ok** to start the calibration.

   The bar at the top shows the progress:

   ![Gyro calibration in progress on PX4](https://raw.githubusercontent.com/PX4/PX4-Autopilot/main/docs/assets/qgc/setup/sensor/gyroscope_calibrate_progress_px4.png)

1. When finished, _QGroundControl_ will display a progress bar _Calibration complete_
   ![Gyro calibration complete on PX4](https://raw.githubusercontent.com/PX4/PX4-Autopilot/main/docs/assets/qgc/setup/sensor/gyroscope_calibrate_complete_px4.png)

::: info
If you move the vehicle _QGroundControl_ will automatically restart the gyroscope calibration.
:::

## Further Information

- [QGroundControl User Guide > Gyroscope](https://docs.qgroundcontrol.com/master/en/qgc-user-guide/setup_view/sensors_px4.html#gyroscope)
