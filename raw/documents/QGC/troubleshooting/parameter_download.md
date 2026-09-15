---
title: "Parameter Download failures"
type: document
doc_set: QGC
doc_version: Stable_V5.0
section: troubleshooting
source_url: "https://docs.qgroundcontrol.com/Stable_V5.0/en/qgc-user-guide/troubleshooting/parameter_download.html"
upstream_repo: "mavlink/qgroundcontrol"
upstream_path: "troubleshooting/parameter_download.md"
upstream_commit: "cb6ee485e0e11c74ed667ca573e7593f770da436"
ingested: 2026-07-28
tags:
  - docs/qgc
  - docs/qgc/troubleshooting
---

# Parameter Download failures

The majority of parameter download failures are caused by a communication link which is noisy and has a high loss rate.
Although the parameter protocol has retry logic for such a case it will eventually give up.
At which point you will get an error stating that QGC was unable to retrieve the full set or parameters.

Although you can still fly the vehicle in this state it is not recommended.
Also the vehicle setup pages will not be available.

You can see the loss rate for your link from the [Settings View > MAVLink](../settings_view/mavlink.md) page.
Even a loss rate in the high single digits can lead to intermittent failures of the plan protocols.
Higher loss rates could leads to 100% failure.

There is also the more remote possibility of either firmware or QGC bugs.
To see the details of the back and forth message traffic of the protocol you can turn on [Console Logging](../settings_view/console_logging.md) for the Parameter Protocol.
