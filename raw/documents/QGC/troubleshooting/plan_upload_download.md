---
title: "Mission Upload/Download failures"
type: document
doc_set: QGC
doc_version: Stable_V5.0
section: troubleshooting
source_url: "https://docs.qgroundcontrol.com/Stable_V5.0/en/qgc-user-guide/troubleshooting/plan_upload_download.html"
upstream_repo: "mavlink/qgroundcontrol"
upstream_path: "troubleshooting/plan_upload_download.md"
upstream_commit: "cb6ee485e0e11c74ed667ca573e7593f770da436"
ingested: 2026-07-28
tags:
  - docs/qgc
  - docs/qgc/troubleshooting
---

# Mission Upload/Download failures

Although the protocol for uploading and download Plans (Mission, GeoFence, Rally Points) to a vehicle includes retry logic it can still fail over a communication link which is running at a high loss rate.

For more information see: [Plan View > Mission (Plan) Upload/Download Failures](../plan_view/plan_view.md#plan_transfer_fail)
