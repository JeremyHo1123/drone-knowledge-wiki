---
title: "CSV Logging"
type: document
doc_set: QGC
doc_version: Stable_V5.0
section: settings_view
source_url: "https://docs.qgroundcontrol.com/Stable_V5.0/en/qgc-user-guide/settings_view/csv.html"
upstream_repo: "mavlink/qgroundcontrol"
upstream_path: "settings_view/csv.md"
upstream_commit: "cb6ee485e0e11c74ed667ca573e7593f770da436"
ingested: 2026-07-28
tags:
  - docs/qgc
  - docs/qgc/settings-view
---

# CSV Logging

![Csv checkbox](https://raw.githubusercontent.com/mavlink/qgroundcontrol/Stable_V5.0/docs/assets/settings/general/csv.jpg)

When checked, a CSV (comma-separated value) telemetry file will be created along with the usual **.tlog** telemetry file.
The file is only created if **Save log after each flight** is enabled, and is recorded for the same duration.

This CSV file contains the most relevant vehicle telemetry data available for quick analysis such as GPS position, attitude, battery status, and others.
It is populated at 1 Hz and while it is not as detailed as the telemetry log, it is a lot easier to work with and quicker to extract data out of.

The file can be opened by common spreadsheet software, including: Microsoft Excel, Google Sheets, LibreOffice Calc or OpenOffice Calc.
