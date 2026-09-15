---
title: "ArmingCheckRequestV0 (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/ArmingCheckRequestV0"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/ArmingCheckRequestV0.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# ArmingCheckRequestV0 (UORB message)

Arming check request.

Broadcast message to request arming checks be reported by all registered components, such as external ROS 2 navigation modes.
All registered components should respond with an ArmingCheckReply message that indicates their current mode requirements, and any arming failure information.
The request is sent regularly, even while armed, so that the FMU always knows the current arming state for external modes, and can forward it to ground stations.

The reply will include the published request_id, allowing correlation of all arming check information for a particular request.
The reply will also include the registration_id for each external component, provided to it during the registration process (RegisterExtComponentReply).

**TOPICS:** arming_check_request_v0

## Fields

| Name                                  | Type     | Unit [Frame] | Range/Enum | Description                                                                       |
| ------------------------------------- | -------- | ------------ | ---------- | --------------------------------------------------------------------------------- |
| <a id="fld_timestamp"></a>timestamp   | `uint64` | us           |            | Time since system start.                                                          |
| <a id="fld_request_id"></a>request_id | `uint8`  |              |            | Id of this request. Allows correlation with associated ArmingCheckReply messages. |

## Constants

| Name                                          | Type     | Value | Description |
| --------------------------------------------- | -------- | ----- | ----------- |
| <a id="#MESSAGE_VERSION"></a> MESSAGE_VERSION | `uint32` | 0     |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/px4_msgs_old/msg/ArmingCheckRequestV0.msg)

::: details Click here to see original file

```c
# Arming check request.
#
# Broadcast message to request arming checks be reported by all registered components, such as external ROS 2 navigation modes.
# All registered components should respond with an ArmingCheckReply message that indicates their current mode requirements, and any arming failure information.
# The request is sent regularly, even while armed, so that the FMU always knows the current arming state for external modes, and can forward it to ground stations.
#
# The reply will include the published request_id, allowing correlation of all arming check information for a particular request.
# The reply will also include the registration_id for each external component, provided to it during the registration process (RegisterExtComponentReply).

uint32 MESSAGE_VERSION = 0

uint64 timestamp  # [us] Time since system start.

uint8 request_id  # Id of this request. Allows correlation with associated ArmingCheckReply messages.
```

:::
