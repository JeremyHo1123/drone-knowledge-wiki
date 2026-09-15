---
title: "Plan View - Rally Points"
type: document
doc_set: QGC
doc_version: Stable_V5.0
section: plan_view
source_url: "https://docs.qgroundcontrol.com/Stable_V5.0/en/qgc-user-guide/plan_view/plan_rally_points.html"
upstream_repo: "mavlink/qgroundcontrol"
upstream_path: "plan_view/plan_rally_points.md"
upstream_commit: "cb6ee485e0e11c74ed667ca573e7593f770da436"
ingested: 2026-07-28
tags:
  - docs/qgc
  - docs/qgc/plan-view
---

# Plan View - Rally Points

Rally Points are alternative landing or loiter locations.
They are typically used to provide a safer or more convenient (e.g. closer) destination than the home position in Return/RTL mode.

::: info
Rally Points are only supported by ArduPilot on Rover 3.6 and Copter 3.7 (or higher).
PX4 support is planned in PX4 v1.10 timeframes.
It also requires usage of a Daily build or Stable 3.6 (once available).
_QGroundControl_ will not display the Rally Point options if they are not supported by the connected vehicle.
:::

![Rally Points](https://raw.githubusercontent.com/mavlink/qgroundcontrol/Stable_V5.0/docs/assets/plan/rally/rally_points_overview.jpg)

## Rally Point Usage

To create Rally Points:

1. Navigate to the Plan View
1. Select the _Rally_ radio button above the Mission Command List
1. Click the map wherever you want rally points.
   - An **R** marker is added for each
   - the currently active marker has a different colour (green) and can be edited using the _Rally Point_ panel.
1. Make any rally point active by selecting it on the map:
   - Move the active rally point by either dragging it on the map or editing the position in the panel.
   - Delete the active rally point by selecting the menu option on the _Rally Point_ panel
     ![Delete Rally Point](https://raw.githubusercontent.com/mavlink/qgroundcontrol/Stable_V5.0/docs/assets/plan/rally/rally_points_delete.jpg)

## Upload Rally Points

Rally points are uploaded in the same way as a mission, using **File** in the [Plan tools](../plan_view/plan_view.md).

## Remaining tools

The rest of the tools work exactly as they do while editing a Mission.
