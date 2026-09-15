---
title: "Console Logging"
type: document
doc_set: QGC
doc_version: Stable_V5.0
section: settings_view
source_url: "https://docs.qgroundcontrol.com/Stable_V5.0/en/qgc-user-guide/settings_view/console_logging.html"
upstream_repo: "mavlink/qgroundcontrol"
upstream_path: "settings_view/console_logging.md"
upstream_commit: "cb6ee485e0e11c74ed667ca573e7593f770da436"
ingested: 2026-07-28
tags:
  - docs/qgc
  - docs/qgc/settings-view
---

# Console Logging

The _Console_ can be helpful tool for diagnosing _QGroundControl_ problems. It can be found in **SettingsView > Console**.

![Console logging](https://raw.githubusercontent.com/mavlink/qgroundcontrol/Stable_V5.0/docs/assets/support/console.jpg)

Click the **Set Logging** button to enable/disable logging information displayed by _QGroundControl_.

## Common Logging Options

The most commmonly used logging options are listed below.

| Option(s)                                                                           | Description                                                                                    |
| ----------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `LinkManagerLog`, `MultiVehicleManagerLog`                                          | Debug connection problems.                                                                     |
| `LinkManagerVerboseLog`                                                             | Debug serial ports not being detected. Very noisy continuous output of available serial ports. |
| `FirmwareUpgradeLog`                                                                | Debug firmware flash issues.                                                                   |
| `ParameterManagerLog`                                                               | Debug parameter load problems.                                                                 |
| `ParameterManagerDebugCacheFailureLog`                                              | Debug parameter cache crc misses.                                                              |
| `PlanManagerLog`, `MissionManagerLog`, `GeoFenceManagerLog`, `RallyPointManagerLog` | Debug Plan upload/download issues.                                                             |
| `RadioComponentControllerLog`                                                       | Debug Radio calibration issues.                                                                |

## Logging from the Command Line

An alternate mechanism for logging is using the `--logging` command line option. This is handy if you are trying to get logs from a situation where _QGroundControl_ crashes.

How you do this and where the traces are output vary by OS:

- Windows

  - You must open a command prompt, change directory to the **qgroundcontrol.exe** location, and run it from there:

    ```sh
    cd "\Program Files (x86)\qgroundcontrol"
    qgroundcontrol --logging:full
    ```

  - When _QGroundControl_ starts you should see a separate console window open which will have the log output

- OSX

  - You must run _QGroundControl_ from Terminal. The Terminal app is located in Applications/Utilities. Once Terminal is open paste the following into it:

    ```sh
    cd /Applications/qgroundcontrol.app/Contents/MacOS/
    ./qgroundcontrol --logging:full
    ```

  - Log traces will output to the Terminal window.

- Linux

  ```sh
  ./qgroundcontrol-start.sh --logging:full
  ```

  - Log traces will output to the shell you are running from.
