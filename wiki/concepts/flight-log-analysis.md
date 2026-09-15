---
title: Flight Log Analysis
type: concept
sources:
  - "[[raw/documents/PX4/log/flight_log_analysis]]"
  - "[[raw/documents/PX4/log/flight_review]]"
  - "[[raw/documents/PX4/log/plotjuggler_log_analysis]]"
  - "[[raw/documents/QGC/analyze_view/log_download]]"
created: 2026-07-28
updated: 2026-09-15
tags:
  - uav/safety
  - uav/flight-control
  - stack/px4
  - stack/qgc
status: active
doc_version_checked:
  - "PX4 main@9467506"
  - "QGC Stable_V5.0@cb6ee48"
---

# Flight Log Analysis

After an incident (or after tuning), this is the only thing that can tell you clearly "what actually happened". PX4 uses the **ULog** format, and what it records are essentially the topics of [[wiki/concepts/uorb-messaging]].

## Structured analysis: establish context before looking at plots

The official order is worth following — **ask these four questions before you start plotting**:

1. **If analysing a failure: did the log capture the crash, or did it stop in mid-air?**
2. **Did the controllers track their references?** The simplest check is to **compare the attitude roll/pitch rates with their setpoints**
3. **Do the sensor data look plausible? Is vibration too high?** The official threshold: **more than 2–3 m/s² peak-to-peak counts as strong vibration**
4. If the root cause is not specific to your vehicle, report it on the PX4 issue tracker with the log attached (a video helps)

Point 2 is the standard way to verify tuning; see [[wiki/concepts/pid-tuning]].

## Log stops in mid-air: rule out power loss first

A log that ends abruptly in the air has two main causes: **power loss**, or an **operating-system hard fault**.

**STM32-based flight controllers write hard faults to the root of the SD card**, with file names such as `fault_2017_04_03_00_26_05.log`. **When a log stops abruptly, first check the SD card root for such a file** — if there is one, it was a software fault; only if there isn't should you investigate power.

This one triage rule saves a lot of guesswork.

## Tools

| Tool | Best for |
| --- | --- |
| **Flight Review** (logs.px4.io) | Web-based, best for most users. Upload a log to share an interactive report with others. Batch uploads with `upload_log.py` |
| **PlotJuggler** | Desktop tool for detailed time-series comparison; see [[raw/documents/PX4/log/plotjuggler_log_analysis]] |
| **QGC Log Download** | Downloads logs from the vehicle; see [[raw/documents/QGC/analyze_view/log_download]] |

## Related pages

- [[wiki/concepts/pid-tuning]] — using logs to assess rate and attitude tracking
- [[wiki/concepts/ekf2]] — estimation quality is also diagnosed from logs
- [[wiki/concepts/uorb-messaging]] — logs contain uORB topics
- [[wiki/concepts/failsafe]] — checking whether a failsafe triggered as expected
