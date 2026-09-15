---
title: "LandingGear (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/LandingGear"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/LandingGear.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# LandingGear (UORB message)

**TOPICS:** landing_gear

## Fields

| Name                                      | Type     | Unit [Frame] | Range/Enum | Description                            |
| ----------------------------------------- | -------- | ------------ | ---------- | -------------------------------------- |
| <a id="fld_timestamp"></a>timestamp       | `uint64` |              |            | time since system start (microseconds) |
| <a id="fld_landing_gear"></a>landing_gear | `int8`   |              |            |

## Constants

| Name                              | Type   | Value | Description            |
| --------------------------------- | ------ | ----- | ---------------------- |
| <a id="#GEAR_UP"></a> GEAR_UP     | `int8` | 1     | landing gear up        |
| <a id="#GEAR_DOWN"></a> GEAR_DOWN | `int8` | -1    | landing gear down      |
| <a id="#GEAR_KEEP"></a> GEAR_KEEP | `int8` | 0     | keep the current state |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/LandingGear.msg)

::: details Click here to see original file

```c
uint64 timestamp # time since system start (microseconds)

int8 GEAR_UP = 1 # landing gear up
int8 GEAR_DOWN = -1 # landing gear down
int8 GEAR_KEEP = 0 # keep the current state

int8 landing_gear
```

:::
