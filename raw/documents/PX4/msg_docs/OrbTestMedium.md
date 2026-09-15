---
title: "OrbTestMedium (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/OrbTestMedium"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/OrbTestMedium.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# OrbTestMedium (UORB message)

**TOPICS:** orb_test_medium orb_test_medium_multi orb_test_medium_wrap_around orb_test_medium_queue orb_test_medium_queue_poll

## Fields

| Name                                | Type        | Unit [Frame] | Range/Enum | Description                            |
| ----------------------------------- | ----------- | ------------ | ---------- | -------------------------------------- |
| <a id="fld_timestamp"></a>timestamp | `uint64`    |              |            | time since system start (microseconds) |
| <a id="fld_val"></a>val             | `int32`     |              |            |
| <a id="fld_junk"></a>junk           | `uint8[64]` |              |            |

## Constants

| Name                                            | Type    | Value | Description |
| ----------------------------------------------- | ------- | ----- | ----------- |
| <a id="#ORB_QUEUE_LENGTH"></a> ORB_QUEUE_LENGTH | `uint8` | 16    |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/OrbTestMedium.msg)

::: details Click here to see original file

```c
uint64 timestamp		# time since system start (microseconds)

int32 val

uint8[64] junk

uint8 ORB_QUEUE_LENGTH = 16

# TOPICS orb_test_medium orb_test_medium_multi orb_test_medium_wrap_around orb_test_medium_queue orb_test_medium_queue_poll
```

:::
