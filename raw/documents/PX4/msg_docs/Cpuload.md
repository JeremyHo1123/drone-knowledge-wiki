---
title: "Cpuload (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/Cpuload"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/Cpuload.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# Cpuload (UORB message)

**TOPICS:** cpuload

## Fields

| Name                                | Type      | Unit [Frame] | Range/Enum | Description                            |
| ----------------------------------- | --------- | ------------ | ---------- | -------------------------------------- |
| <a id="fld_timestamp"></a>timestamp | `uint64`  |              |            | time since system start (microseconds) |
| <a id="fld_load"></a>load           | `float32` |              |            | processor load from 0 to 1             |
| <a id="fld_ram_usage"></a>ram_usage | `float32` |              |            | RAM usage from 0 to 1                  |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/Cpuload.msg)

::: details Click here to see original file

```c
uint64 timestamp		# time since system start (microseconds)
float32 load                    # processor load from 0 to 1
float32 ram_usage		# RAM usage from 0 to 1
```

:::
