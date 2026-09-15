---
title: "RadioStatus (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/RadioStatus"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/RadioStatus.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# RadioStatus (UORB message)

**TOPICS:** radio_status

## Fields

| Name                                      | Type     | Unit [Frame] | Range/Enum | Description                               |
| ----------------------------------------- | -------- | ------------ | ---------- | ----------------------------------------- |
| <a id="fld_timestamp"></a>timestamp       | `uint64` |              |            | time since system start (microseconds)    |
| <a id="fld_rssi"></a>rssi                 | `uint8`  |              |            | local signal strength                     |
| <a id="fld_remote_rssi"></a>remote_rssi   | `uint8`  |              |            | remote signal strength                    |
| <a id="fld_txbuf"></a>txbuf               | `uint8`  |              |            | how full the tx buffer is as a percentage |
| <a id="fld_noise"></a>noise               | `uint8`  |              |            | background noise level                    |
| <a id="fld_remote_noise"></a>remote_noise | `uint8`  |              |            | remote background noise level             |
| <a id="fld_rxerrors"></a>rxerrors         | `uint16` |              |            | receive errors                            |
| <a id="fld_fix"></a>fix                   | `uint16` |              |            | count of error corrected packets          |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/RadioStatus.msg)

::: details Click here to see original file

```c
uint64 timestamp	# time since system start (microseconds)

uint8 rssi				# local signal strength
uint8 remote_rssi			# remote signal strength

uint8 txbuf				# how full the tx buffer is as a percentage
uint8 noise				# background noise level

uint8 remote_noise			# remote background noise level
uint16 rxerrors				# receive errors

uint16 fix				# count of error corrected packets
```

:::
