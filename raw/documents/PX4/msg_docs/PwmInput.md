---
title: "PwmInput (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/PwmInput"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/PwmInput.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# PwmInput (UORB message)

**TOPICS:** pwm_input

## Fields

| Name                                    | Type     | Unit [Frame] | Range/Enum | Description                                  |
| --------------------------------------- | -------- | ------------ | ---------- | -------------------------------------------- |
| <a id="fld_timestamp"></a>timestamp     | `uint64` |              |            | Time since system start (microseconds)       |
| <a id="fld_error_count"></a>error_count | `uint64` |              |            | Timer overcapture error flag (AUX5 or MAIN5) |
| <a id="fld_pulse_width"></a>pulse_width | `uint32` |              |            | Pulse width, timer counts (microseconds)     |
| <a id="fld_period"></a>period           | `uint32` |              |            | Period, timer counts (microseconds)          |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/PwmInput.msg)

::: details Click here to see original file

```c
uint64 timestamp   # Time since system start (microseconds)
uint64 error_count # Timer overcapture error flag (AUX5 or MAIN5)
uint32 pulse_width # Pulse width, timer counts (microseconds)
uint32 period      # Period, timer counts (microseconds)
```

:::
