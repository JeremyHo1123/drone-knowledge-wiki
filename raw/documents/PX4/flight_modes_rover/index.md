---
title: "Drive Modes"
type: document
doc_set: PX4
doc_version: main
section: flight_modes_rover
source_url: "https://docs.px4.io/main/en/flight_modes_rover/"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "flight_modes_rover/index.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/flight-modes-rover
---

# Drive Modes

Flight modes (or more accurately "Drive modes" for ground vehicles) provide autopilot support to make it easier to manually drive the vehicle or to execute autonomous missions.

This section outlines all supported drive modes for [Rovers](../frames_rover/index.md).

For information on mapping RC control switches to specific modes see: [Basic Configuration > Flight Modes](../config/flight_mode.md).

::: warning
Selecting any other mode than those listed below will either stop the rover or can lead to undefined behaviour.
:::

## Manual Modes

| Mode                                    | Description                                                                                                                                                                      |
| --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Manual](manual.md#manual-mode)         | No autopilot support. User is responsible for keeping the rover on the desired course and maintaining speed and rate of turn.                                                    |
| [Acro](manual.md#acro-mode)             | + Maintains the yaw rate (feels more like driving a car than manual mode). <br>+ Allows maximum yaw rate to be limited (protects against roll over).                             |
| [Stabilized](manual.md#stabilized-mode) | + Maintains the yaw (significantly better at holding a straight line).                                                                                                           |
| [Position](manual.md#position-mode)     | + Maintains the course (best mode for driving a straight line).<br>+ Maintains speed against disturbances, e.g. when driving up a hill.<br>+ Allows maximum speed to be limited. |

## Auto Modes

| Mode                            | Description                                                             |
| ------------------------------- | ----------------------------------------------------------------------- |
| [Mission](auto.md#mission-mode) | Automatic mode that causes the vehicle to execute a predefined mission. |
| [Return](auto.md#return-mode)   | Automatic mode that returns the vehicle to the launch position.         |
