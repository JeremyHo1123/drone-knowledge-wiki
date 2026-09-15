---
title: "Plan View - GeoFence"
type: document
doc_set: QGC
doc_version: Stable_V5.0
section: plan_view
source_url: "https://docs.qgroundcontrol.com/Stable_V5.0/en/qgc-user-guide/plan_view/plan_geofence.html"
upstream_repo: "mavlink/qgroundcontrol"
upstream_path: "plan_view/plan_geofence.md"
upstream_commit: "cb6ee485e0e11c74ed667ca573e7593f770da436"
ingested: 2026-07-28
tags:
  - docs/qgc
  - docs/qgc/plan-view
---

# Plan View - GeoFence

GeoFences allow you to create virtual regions within which the vehicle can fly, or in which it is _not allowed_ to fly.
You can also configure the action taken if you fly outside permitted areas.

![Geofence overview](https://raw.githubusercontent.com/mavlink/qgroundcontrol/Stable_V5.0/docs/assets/plan/geofence/geofence_overview.jpg)

::: info
**ArduPilot users:** GeoFence support is only supported by Rover 3.6 and Copter 3.7 or higher. It also requires usage of a Daily build or Stable 3.6 (once available).
_QGroundControl_ will not display the GeoFence options if they are not supported by the connected vehicle.
:::

## Create a Geofence

To create a GeoFence:

1. Navigate to the Plan View
1. Select the _Geofence_ radio button above the Mission Command List

   ![Select geofence radio button](https://raw.githubusercontent.com/mavlink/qgroundcontrol/Stable_V5.0/docs/assets/plan/geofence/geofence_select.jpg)

1. Insert a circular or polygon region by pressing the **Circular Fence** or **Polygon Fence** button, respectively.
   A new region will be added to the map and to the associated list of fences below the buttons.

:::tip
You can create multiple regions by pressing the buttons multiple times, allowing complex geofence definitions to be created.
:::

- Circular region:

  ![Circular Geofence](https://raw.githubusercontent.com/mavlink/qgroundcontrol/Stable_V5.0/docs/assets/plan/geofence/geofence_circular.jpg)

  - Move the region by dragging the central dot on the map
  - Resize the circle by dragging the dot on the edge of the circle (or you can change the radius value in the fence panel).

- Polygon region:

  ![Polygon Geofence](https://raw.githubusercontent.com/mavlink/qgroundcontrol/Stable_V5.0/docs/assets/plan/geofence/geofence_polygon.jpg)

  - Move the vertices by dragging the filled dots
  - Create new vertices by clicking the "unfilled" dots on the lines between the filled vertices.

1. By default new regions are created as _inclusion_ zones (vehicles must stay within the region).
   Change them to exclusion zones (where the vehicle can't travel) by unchecking the associated _Inclusion_ checkbox in the fence panel.

## Edit/Delete a GeoFence

You can select a geofence region to edit by selecting its _Edit_ radio button in the GeoFence panel.
You can then edit the region on the map as described in the previous section.

Regions can be deleted by pressing the associated **Del** button.

## Upload a GeoFence

The GeoFence is uploaded in the same way as a mission, using **File** in the [Plan tools](../plan_view/plan_view.md).

## Remaining tools

The rest of the tools work exactly as they do while editing a Mission.
