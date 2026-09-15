---
title: "Gripper (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/Gripper"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/Gripper.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# Gripper (UORB message)

# Used to command an actuation in the gripper, which is mapped to a specific output in the control allocation module.

**TOPICS:** gripper

## Fields

| Name                                | Type     | Unit [Frame] | Range/Enum | Description                     |
| ----------------------------------- | -------- | ------------ | ---------- | ------------------------------- |
| <a id="fld_timestamp"></a>timestamp | `uint64` |              |            |
| <a id="fld_command"></a>command     | `int8`   |              |            | Commanded state for the gripper |

## Constants

| Name                                          | Type   | Value | Description |
| --------------------------------------------- | ------ | ----- | ----------- |
| <a id="#COMMAND_GRAB"></a> COMMAND_GRAB       | `int8` | 0     |
| <a id="#COMMAND_RELEASE"></a> COMMAND_RELEASE | `int8` | 1     |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/Gripper.msg)

::: details Click here to see original file

```c
## Used to command an actuation in the gripper, which is mapped to a specific output in the control allocation module

uint64 timestamp

int8 command		# Commanded state for the gripper
int8 COMMAND_GRAB = 0
int8 COMMAND_RELEASE = 1
```

:::
