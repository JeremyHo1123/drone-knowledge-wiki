---
title: "GeoTag Images (Analyze View)"
type: document
doc_set: QGC
doc_version: Stable_V5.0
section: analyze_view
source_url: "https://docs.qgroundcontrol.com/Stable_V5.0/en/qgc-user-guide/analyze_view/geotag_images.html"
upstream_repo: "mavlink/qgroundcontrol"
upstream_path: "analyze_view/geotag_images.md"
upstream_commit: "cb6ee485e0e11c74ed667ca573e7593f770da436"
ingested: 2026-07-28
tags:
  - docs/qgc
  - docs/qgc/analyze-view
---

# GeoTag Images (Analyze View)

The _GeoTag Images_ screen (**Analyze > GeoTag Images**) allows you to geotag images from a survey mission using information in the flight log.

::: info
This feature only works with _PX4_ flight stack logs.
ArduPilot is not supported.
:::

![Analyze View GeoTag Images](https://raw.githubusercontent.com/mavlink/qgroundcontrol/Stable_V5.0/docs/assets/analyze/geotag_images.jpg)

Select the log file, image directory and (optionally) output directory for geotagged images using the buttons provided.
Click **Start Tagging** to generate the geotagged images.
