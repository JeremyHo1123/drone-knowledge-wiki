---
title: "PX4 SD Card Layout"
type: document
doc_set: PX4
doc_version: main
section: concept
source_url: "https://docs.px4.io/main/en/concept/sd_card_layout"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "concept/sd_card_layout.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/concept
---

# PX4 SD Card Layout

The PX4 SD Card is used for storing configuration files, flight logs, mission information etc.

:::tip
The SD card should be FAT32 formatted for use with PX4 (this is the default for SD cards).
We recommend that you reformat cards that are using a different file system.
:::

The directory structure/layout is shown below.

| Directory/File(s)       | Description                                                                              |
| ----------------------- | ---------------------------------------------------------------------------------------- |
| `/etc/`                 | Extra config. See [System Startup > Replacing the System Startup][replace system start]. |
| `/log/`                 | Full [flight logs](../dev_log/logging.md)                                                |
| `/mission_log/`         | Reduced flight logs                                                                      |
| `/fw/`                  | [DroneCAN](../dronecan/index.md) firmware                                                |
| `/uavcan.db/`           | DroneCAN DNA server DB + logs                                                            |
| `/params`               | Parameters (if not in FRAM/FLASH)                                                        |
| `/dataman`              | Mission storage file                                                                     |
| `/fault_<datetime>.txt` | Hardfault files                                                                          |
| `/bootlog.txt`          | Boot log file                                                                            |

[replace system start]: ../concept/system_startup.md#replacing-the-system-startup
