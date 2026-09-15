---
title: "Maintenance Notes"
type: document
doc_set: PX4
doc_version: main
section: test_and_ci
source_url: "https://docs.px4.io/main/en/test_and_ci/maintenance"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "test_and_ci/maintenance.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/test-and-ci
---

# Maintenance Notes

This picks and describes some tools to help analyze the state of the codebase and support its maintenance.

## Analyze churn

The amount of churn, so the number of changes done to a file can be an indicator which files/parts might need refactoring.

To find churn metrics a tool such as [Churn](https://github.com/danmayer/churn) can be used:

```sh
gem install churn
```

An example output as of `v1.6.0-rc2` would be:

```sh
cd src/PX4-Autopilot
churn --start_date "6 months ago"
**********************************************************************
* Revision Changes
**********************************************************************
Files
+------------------------------------------+
| file                                     |
+------------------------------------------+
| src/modules/navigator/mission.cpp        |
| src/modules/navigator/navigator_main.cpp |
| src/modules/navigator/rtl.cpp            |
+------------------------------------------+



**********************************************************************
* Project Churn
**********************************************************************

Files
+---------------------------------------------------------------------------+---------------+
| file_path                                                                 | times_changed |
+---------------------------------------------------------------------------+---------------+
| src/modules/mc_pos_control/mc_pos_control_main.cpp                        | 107           |
| src/modules/commander/commander.cpp                                       | 67            |
| ROMFS/px4fmu_common/init.d/rcS                                            | 52            |
| Makefile                                                                  | 49            |
| src/drivers/px4fmu/fmu.cpp                                                | 47            |
| ROMFS/px4fmu_common/init.d/rc.sensors                                     | 40            |
| src/drivers/boards/aerofc-v1/board_config.h                               | 31            |
| src/modules/logger/logger.cpp                                             | 29            |
| src/modules/navigator/navigator_main.cpp                                  | 28            |
```
