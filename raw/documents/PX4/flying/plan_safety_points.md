---
title: "Safety Points (Rally Points)"
type: document
doc_set: PX4
doc_version: main
section: flying
source_url: "https://docs.px4.io/main/en/flying/plan_safety_points"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "flying/plan_safety_points.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/flying
---

# Safety Points (Rally Points)

Safety points are alternative [Return Mode](../flight_modes/return.md) destinations/landing points.
When enabled, the vehicle will choose the _closest return destination_ of: home location, mission landing pattern or a _safety point_.

![Safety Points](https://raw.githubusercontent.com/PX4/PX4-Autopilot/main/docs/assets/qgc/plan/rally_point/rally_points.jpg)

## Creating/Defining Safety Points

Safety points are created in _QGroundControl_ (which calls them "Rally Points").

At high level:

1. Open **QGroundControl > Plan View**
1. Select the **Rally** tab/button on the _Plan Editor_ (right of screen).
1. Select the **Rally Point** button on the toolbar (left of screen).
1. Click anywhere on the map to add a rally/safety point.
   - The _Plan Editor_ displays and lets you edit the current rally point (shown as a green **R** on the map).
   - You can select another rally point (shown as a more orange/yellow **R** on the map) to edit it instead.
1. Select the **Upload Required** button to upload the rally points (along with any [mission](../flying/missions.md) and [geofence](../flying/geofence.md)) to the vehicle.

:::tip
More complete documentation can be found in the _QGroundControl User Guide_: [Plan View - Rally Points](https://docs.qgroundcontrol.com/master/en/qgc-user-guide/plan_view/plan_rally_points.html).
:::

## Using Safety Points

Safety points are not enabled by default (there are a number of different [Return Mode Types](../flight_modes/return.md#return_types)).

To enable safety points:

1. [Use the QGroundControl Parameter Editor](../advanced_config/parameters.md) to set parameter: [RTL_TYPE=3](../advanced_config/parameter_reference.md#RTL_TYPE).
