---
title: "PowerButtonState (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/PowerButtonState"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/PowerButtonState.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# PowerButtonState (UORB message)

power button state notification message.

**TOPICS:** power_button_state

## Fields

| Name                                | Type     | Unit [Frame] | Range/Enum | Description                            |
| ----------------------------------- | -------- | ------------ | ---------- | -------------------------------------- |
| <a id="fld_timestamp"></a>timestamp | `uint64` |              |            | time since system start (microseconds) |
| <a id="fld_event"></a>event         | `uint8`  |              |            | one of PWR*BUTTON_STATE*\*             |

## Constants

| Name                                                                              | Type    | Value | Description                                                             |
| --------------------------------------------------------------------------------- | ------- | ----- | ----------------------------------------------------------------------- |
| <a id="#PWR_BUTTON_STATE_IDEL"></a> PWR_BUTTON_STATE_IDEL                         | `uint8` | 0     | Button went up without meeting shutdown button down time (delete event) |
| <a id="#PWR_BUTTON_STATE_DOWN"></a> PWR_BUTTON_STATE_DOWN                         | `uint8` | 1     | Button went Down                                                        |
| <a id="#PWR_BUTTON_STATE_UP"></a> PWR_BUTTON_STATE_UP                             | `uint8` | 2     | Button went Up                                                          |
| <a id="#PWR_BUTTON_STATE_REQUEST_SHUTDOWN"></a> PWR_BUTTON_STATE_REQUEST_SHUTDOWN | `uint8` | 3     | Button went Up after meeting shutdown button down time                  |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/PowerButtonState.msg)

::: details Click here to see original file

```c
# power button state notification message

uint64 timestamp			    # time since system start (microseconds)

uint8 PWR_BUTTON_STATE_IDEL = 0             # Button went up without meeting shutdown button down time (delete event)
uint8 PWR_BUTTON_STATE_DOWN = 1             # Button went Down
uint8 PWR_BUTTON_STATE_UP = 2               # Button went Up
uint8 PWR_BUTTON_STATE_REQUEST_SHUTDOWN = 3 # Button went Up after meeting shutdown button down time

uint8 event                                 # one of PWR_BUTTON_STATE_*
```

:::
