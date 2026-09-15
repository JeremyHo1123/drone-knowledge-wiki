---
title: "OrbTestLarge (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/OrbTestLarge"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/OrbTestLarge.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# OrbTestLarge (UORB message)

**TOPICS:** orb_test_large

## Fields

| Name                                | Type         | Unit [Frame] | Range/Enum | Description                            |
| ----------------------------------- | ------------ | ------------ | ---------- | -------------------------------------- |
| <a id="fld_timestamp"></a>timestamp | `uint64`     |              |            | time since system start (microseconds) |
| <a id="fld_val"></a>val             | `int32`      |              |            |
| <a id="fld_junk"></a>junk           | `uint8[512]` |              |            |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/OrbTestLarge.msg)

::: details Click here to see original file

```c
uint64 timestamp		# time since system start (microseconds)

int32 val

uint8[512] junk
```

:::
