---
title: "Custom Mavlink Action"
type: document
doc_set: QGC
doc_version: Stable_V5.0
section: custom_actions
source_url: "https://docs.qgroundcontrol.com/Stable_V5.0/en/qgc-user-guide/custom_actions/custom_actions.html"
upstream_repo: "mavlink/qgroundcontrol"
upstream_path: "custom_actions/custom_actions.md"
upstream_commit: "cb6ee485e0e11c74ed667ca573e7593f770da436"
ingested: 2026-07-28
tags:
  - docs/qgc
  - docs/qgc/custom-actions
---

# Custom Mavlink Action

Both the Fly View and Joysticks support the ability execute arbitrary mavlink commands to the active vehicle. In the Fly View these will show up in the Toolstrip Action list. With Joysticks you can assign then to button presses.

## Mavlink Actions File

The actions available are defined in a JSON file. The format of that file is as follows:

```
{
    "version":    1,
    "fileType":   "MavlinkActions",
    "actions": [
        {
            "label":        "First Mavlink Command",
            "description":  "This is the first command",
            "mavCmd":       10,
            "compId":       100,
            "param1":       1,
            "param2":       2,
            ...
        },
        {
            "label":        "Second Mavlink Command",
            "description":  "This is the second command",
            "mavCmd":       20,
            ...
        }
    ]
}
```

Fields:

* actions (required) - An array of json objects, one for each command
* label (required) - The user visible short description for the command. This is used as the button text for the Fly View - Actions command list. For Joysticks, this is the command you select from the dropdown. For Joysticks, make sure your name doesn't conflict with the built in names.
* description (required) - This is a longer description of the command used in the Fly View - Action list. This is not used by joysticks.
* mavCmd (required) - The command id of the mavlink command you want to send.
* compId (options) - The component id for where you want to send the command to. If not specified `MAV_COMP_ID_AUTOPILOT1` is used.
* param1 thru param7 (optional) - The parameters for the command. Parameters which are not specified will default to 0.0

Mavlink action files should be located in the MavlinkActions directory of the QGC save location. For example on Linux that would be `~/Documents/QGroundControl/MavlinkActions` or `~/Documents/QGroundControl Daily/MavlinkActions`. The Fly View and Joysticks can each have there own custom actions file.

When you start up QGC it will load these files if they exist and make the commands available for use.
