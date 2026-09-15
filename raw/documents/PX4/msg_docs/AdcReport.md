---
title: "AdcReport (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/AdcReport"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/AdcReport.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# AdcReport (UORB message)

ADC raw data.

Communicates raw data from an analog-to-digital converter (ADC) to other modules, such as battery status.

**TOPICS:** adc_report

## Fields

| Name                                  | Type        | Unit [Frame] | Range/Enum | Description                                                                          |
| ------------------------------------- | ----------- | ------------ | ---------- | ------------------------------------------------------------------------------------ |
| <a id="fld_timestamp"></a>timestamp   | `uint64`    | us           |            | Time since system start                                                              |
| <a id="fld_device_id"></a>device_id   | `uint32`    |              |            | unique device ID for the sensor that does not change between power cycles            |
| <a id="fld_channel_id"></a>channel_id | `int16[16]` |              |            | ADC channel IDs, negative for non-existent, TODO: should be kept same as array index |
| <a id="fld_raw_data"></a>raw_data     | `int32[16]` |              |            | ADC channel raw value, accept negative value, valid if channel ID is positive        |
| <a id="fld_resolution"></a>resolution | `uint32`    |              |            | ADC channel resolution                                                               |
| <a id="fld_v_ref"></a>v_ref           | `float32`   | V            |            | ADC channel voltage reference, use to calculate LSB voltage(lsb=scale/resolution)    |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/AdcReport.msg)

::: details Click here to see original file

```c
# ADC raw data.
#
# Communicates raw data from an analog-to-digital converter (ADC) to other modules, such as battery status.

uint64 timestamp      # [us] Time since system start
uint32 device_id      # [-] unique device ID for the sensor that does not change between power cycles
int16[16] channel_id  # [-] ADC channel IDs, negative for non-existent, TODO: should be kept same as array index
int32[16] raw_data    # [-] ADC channel raw value, accept negative value, valid if channel ID is positive
uint32 resolution     # [-] ADC channel resolution
float32 v_ref         # [V] ADC channel voltage reference, use to calculate LSB voltage(lsb=scale/resolution)
```

:::
