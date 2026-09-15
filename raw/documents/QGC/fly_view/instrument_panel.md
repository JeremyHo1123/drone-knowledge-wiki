---
title: "Instrument Panel"
type: document
doc_set: QGC
doc_version: Stable_V5.0
section: fly_view
source_url: "https://docs.qgroundcontrol.com/Stable_V5.0/en/qgc-user-guide/fly_view/instrument_panel.html"
upstream_repo: "mavlink/qgroundcontrol"
upstream_path: "fly_view/instrument_panel.md"
upstream_commit: "cb6ee485e0e11c74ed667ca573e7593f770da436"
ingested: 2026-07-28
tags:
  - docs/qgc
  - docs/qgc/fly-view
---

# Instrument Panel

The instrument panel displays telemetry information about the current vehicle.

![Instrument Panel - for values/telemetry](https://raw.githubusercontent.com/mavlink/qgroundcontrol/Stable_V5.0/docs/assets/fly/instrument_panel/instrument_panel_default_values.png)

The default values include altitude (relative to the home location), horizontal and vertical speed, total flight time, and distance between vehicle and ground station.

You can configure where the information is displayed by:

* Tablets: Press and hold over control
* Desktop: Right click control
* Click to Lock icon to close and save changes

![Instrument Panel - edit tools](https://raw.githubusercontent.com/mavlink/qgroundcontrol/Stable_V5.0/docs/assets/fly/instrument_panel/instrument_panel_tools_edit.png)

You configure what information is display by selecting the edit/pencil icon.
The grid will then display "+" and "-" icons that you can use to add or remove rows and columns (and the pencil icon is replaced by a "lock" icon that you can use to save the settings).

Select a value to launch its "Value Display" editor.
This allows you to change the icon, text, size, units and so on of the current telemetry value.

![Instrument Panel - edit a value](https://raw.githubusercontent.com/mavlink/qgroundcontrol/Stable_V5.0/docs/assets/fly/instrument_panel/instrument_panel_tools_edit_value.png)

The selection list on the top left is used to change the source of the telemetry.
By default this is the vehicle, but you can use the selector to choose a particular sensor type.

![Instrument Panel - value type](https://raw.githubusercontent.com/mavlink/qgroundcontrol/Stable_V5.0/docs/assets/fly/instrument_panel/instrument_panel_edit_value_type.png)

The selection list on the top right is used to select a particular telemetry value for the vehicle or sensor.

![Instrument Panel - value options](https://raw.githubusercontent.com/mavlink/qgroundcontrol/Stable_V5.0/docs/assets/fly/instrument_panel/instrument_panel_edit_value_options.png)
