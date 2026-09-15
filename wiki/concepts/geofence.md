---
title: Geofence
type: concept
sources:
  - "[[raw/documents/PX4/flying/geofence]]"
  - "[[raw/documents/PX4/config/safety]]"
  - "[[raw/documents/QGC/plan_view/plan_geofence]]"
  - "[[raw/documents/MAVSDK/plugins/geofence]]"
created: 2026-07-28
updated: 2026-09-15
tags:
  - uav/safety
  - stack/px4
  - stack/qgc
  - stack/mavsdk
status: active
doc_version_checked:
  - "PX4 main@9467506"
  - "QGC Stable_V5.0@cb6ee48"
---

# Geofence

A virtual boundary that defines **where the vehicle may go**. It is used to avoid flying out of RC range and to stay out of unsafe or restricted airspace.

**Key fact: the geofence is active in all modes, including missions and manual flight.** This runs against many people's intuition — it is not only the automatic modes that are restricted.

## Two independent mechanisms

PX4 provides two, **with different purposes and complexity, and they can be used together**:

| Mechanism | Shape | Where to configure |
| --- | --- | --- |
| **Failsafe Geofence** | A **single cylinder** centred on home (maximum radius + maximum altitude) | QGC Safety page / `GF_` parameters |
| **Geofence Plan** | Multiple circular and polygonal regions, each set as **inclusion (must stay inside)** or **exclusion (must not enter)** | QGC Plan View, planned together with the mission and rally points |

The failsafe geofence includes the "action on breach" — it can be just a warning, but **more commonly it is an immediate Return to a safe location**. The action ladder and the "more severe of several simultaneous failsafes wins" rule are in [[wiki/concepts/failsafe]].

## Planning complex fences in QGC

Procedure (details in [[raw/documents/QGC/plan_view/plan_geofence]]):

1. **Plan View** → set Plan Type to **Fence** to open the GeoFence Editor
2. Click **Polygon Fence** or **Circular Fence** to add a basic fence
3. Adjust shape and position on the map — the centre marker moves the whole fence; the marker on a circular fence's edge changes its radius
4. Set each fence individually as inclusion or exclusion

Fences, the mission and rally points ([[raw/documents/QGC/plan_view/plan_rally_points]]) are three parts of the same Plan and are uploaded to the vehicle together.

## Programmatic access

MAVSDK's `Geofence` plugin can upload fence polygons; see [[raw/documents/MAVSDK/plugins/geofence]]. Useful for automated testing or for adjusting the flight area dynamically.

## Related pages

- [[wiki/concepts/failsafe]] — the action on breach belongs to the failsafe action ladder
- [[wiki/concepts/mission-planning]] — fences and missions are the same Plan in QGC
