---
title: "Pattern"
type: document
doc_set: QGC
doc_version: Stable_V5.0
section: plan_view
source_url: "https://docs.qgroundcontrol.com/Stable_V5.0/en/qgc-user-guide/plan_view/pattern.html"
upstream_repo: "mavlink/qgroundcontrol"
upstream_path: "plan_view/pattern.md"
upstream_commit: "cb6ee485e0e11c74ed667ca573e7593f770da436"
ingested: 2026-07-28
tags:
  - docs/qgc
  - docs/qgc/plan-view
---

# Pattern

The _Pattern tools_ (in the [PlanView](../plan_view/plan_view.md) _Plan Tools_) allow you to specify complex flight patterns using a simple graphical UI.
The available pattern tools depend on the vehicle (and support for the vehicle-type in the flight stack).

![Pattern Tool (Plan Tools)](https://raw.githubusercontent.com/mavlink/qgroundcontrol/Stable_V5.0/docs/assets/plan/pattern/pattern_tool.jpg)

| Pattern                                                         | Description                                                                                                                                                                                        | Vehicles          |
| --------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| [Survey](../plan_view/pattern_survey.md)                         | Create a grid flight pattern over a polygonal area. <br />You can specify the polygon as well as the specifications for the grid and camera settings appropriate for creating geotagged images.    | All               |
| [Structure Scan](../plan_view/pattern_structure_scan_v2.md)      | Create a grid flight pattern that captures images over vertical surfaces (polygonal or circular). <br />These are typically used for the visual inspection or creation of 3D models of structures. | MultiCopter, VTOL |
| [Corridor Scan](../plan_view/pattern_corridor_scan.md)           | Create a flight pattern which follows a poly-line (for example, to survey a road).                                                                                                                 | All               |
| [Fixed Wing Landing](../plan_view/pattern_fixed_wing_landing.md) | Add a landing pattern for fixed wing vehicles to a mission.                                                                                                                                        | Fixed Wing        |
