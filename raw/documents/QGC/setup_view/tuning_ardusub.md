---
title: "ArduSub Tuning"
type: document
doc_set: QGC
doc_version: Stable_V5.0
section: setup_view
source_url: "https://docs.qgroundcontrol.com/Stable_V5.0/en/qgc-user-guide/setup_view/tuning_ardusub.html"
upstream_repo: "mavlink/qgroundcontrol"
upstream_path: "setup_view/tuning_ardusub.md"
upstream_commit: "cb6ee485e0e11c74ed667ca573e7593f770da436"
ingested: 2026-07-28
tags:
  - docs/qgc
  - docs/qgc/setup-view
---

# ArduSub Tuning

![ArduSub Tuning Page](https://raw.githubusercontent.com/mavlink/qgroundcontrol/Stable_V5.0/docs/assets/setup/tuning/ardusub.jpg)

## Basic Tuning

This page allows changing the PID controller gains to better suit your vehicle and application. Changing these may help you get a snappier response for more precise movements, or a smoother response for recording cinematic footages. Adjust a parameter by moving the desired slider, or by clicking the increase/decrease buttons. There are three controllers that can be adjusted here:

- [**Attitude Controller Parameters**](https://www.ardusub.com/operators-manual/full-parameter-list.html#atc-parameters) are the parameters for the controller responsible for keeping the vehicle oriented as you want it, assuming your vehicle has ability (enough motors/DOF) to do so.

- **Position Controller Parameters** are the parameters for the controller responsible for positioning the vehicle at a point in 3D space. The **Z** parameters control how the depth control works (eg in [_Depth Hold_](https://www.ardusub.com/operators-manual/flight-modes.html#depth-hold) mode). The **XY** parameters affect how the vehicle controls the horizontal position in [_Position Enabled_](https://www.ardusub.com/operators-manual/flight-modes.html#position-enabled-modes) modes.

- **Waypoint Navigation Parameters** are the parameters for the controller responsible for following waypoints in **Auto** and **Guided** mode.

  ::: warning
  **Guided** and **Auto** modes are currently unsupported and some features are disabled in QGC.
  :::
