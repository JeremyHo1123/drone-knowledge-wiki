---
title: "Airspeed (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/Airspeed"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/Airspeed.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# Airspeed (UORB message)

Airspeed data from sensors.

This is published by airspeed sensor drivers, CAN airspeed sensors, simulators.
It is subscribed by the airspeed selector module, which validates the data from multiple sensors and passes on a single estimation to the EKF, controllers and telemetry providers.

**TOPICS:** airspeed

## Fields

| Name                                                          | Type      | Unit [Frame] | Range/Enum | Description                      |
| ------------------------------------------------------------- | --------- | ------------ | ---------- | -------------------------------- |
| <a id="fld_timestamp"></a>timestamp                           | `uint64`  | us           |            | Time since system start          |
| <a id="fld_timestamp_sample"></a>timestamp_sample             | `uint64`  | us           |            | Timestamp of the raw data        |
| <a id="fld_indicated_airspeed_m_s"></a>indicated_airspeed_m_s | `float32` | m/s          |            | Indicated airspeed               |
| <a id="fld_true_airspeed_m_s"></a>true_airspeed_m_s           | `float32` | m/s          |            | True airspeed                    |
| <a id="fld_confidence"></a>confidence                         | `float32` |              | [0 : 1]    | Confidence value for this sensor |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/Airspeed.msg)

::: details Click here to see original file

```c
# Airspeed data from sensors
#
# This is published by airspeed sensor drivers, CAN airspeed sensors, simulators.
# It is subscribed by the airspeed selector module, which validates the data from multiple sensors and passes on a single estimation to the EKF, controllers and telemetry providers.

uint64 timestamp                 # [us] Time since system start
uint64 timestamp_sample          # [us] Timestamp of the raw data
float32 indicated_airspeed_m_s   # [m/s] Indicated airspeed
float32 true_airspeed_m_s        # [m/s] True airspeed
float32 confidence               # [@range 0,1] Confidence value for this sensor
```

:::
