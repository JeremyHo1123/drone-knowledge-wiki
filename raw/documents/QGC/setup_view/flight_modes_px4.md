---
title: "PX4 Flight Modes Setup"
type: document
doc_set: QGC
doc_version: Stable_V5.0
section: setup_view
source_url: "https://docs.qgroundcontrol.com/Stable_V5.0/en/qgc-user-guide/setup_view/flight_modes_px4.html"
upstream_repo: "mavlink/qgroundcontrol"
upstream_path: "setup_view/flight_modes_px4.md"
upstream_commit: "cb6ee485e0e11c74ed667ca573e7593f770da436"
ingested: 2026-07-28
tags:
  - docs/qgc
  - docs/qgc/setup-view
---

# PX4 Flight Modes Setup

The _Flight Modes_ section allows you to configure which [flight modes](http://docs.px4.io/main/en/getting_started/flight_modes.html) and other actions are triggered by particular switches/switch positions on your RC transmitter.

::: info
In order to set up flight modes you must already have

- [Configured your radio](../setup_view/radio.md) in order to set flight modes.
- [Setup the RC transmitter](../setup_view/FlightModes.md#transmitter-setup) (Flight Modes > Transmitter Setup)
  :::

To access this section, select the **Gear** icon (Vehicle Setup) in the top toolbar and then **Flight Modes** in the sidebar.

![Flight modes single-channel](https://raw.githubusercontent.com/mavlink/qgroundcontrol/Stable_V5.0/docs/assets/setup/flight_modes/px4_single_channel.jpg)

## Flight Mode Settings

The screen allows you to specify a "mode" channel and select up to 6 flight modes that will be activated based on the value sent on the channel.
You can also assign a small number of channels to trigger particular actions, such as deploying landing gear, or emergency shutdown (kill switch).

The steps are:

1. Turn on your RC transmitter.
1. Select the **Gear** icon (Vehicle Setup) in the top toolbar and then **Flight Modes** in the sidebar.

   ![Flight modes single-channel](https://raw.githubusercontent.com/mavlink/qgroundcontrol/Stable_V5.0/docs/assets/setup/flight_modes/px4_single_channel.jpg)

1. Specify _Flight Mode Settings_:

   - Select the transmitter **Mode channel** (shown as Channel 5 above).
   - Select up to six **Flight Modes** for switch positions encoded in the channel.

     ::: info
     Position mode, return mode and mission mode [are recommended](https://docs.px4.io/main/en/config/flight_mode.html#what-flight-modes-and-switches-should-i-set).
     :::

1. Specify _Switch Settings_:

   - Select the channels that you want to map to specific actions - _Kill switch_, landing gear, etc. (if you have spare switches and channels on your transmitter).

1. Test that the modes are mapped to the right transmitter switches:
   - Check the _Channel Monitor_ to confirm that each switch moves the expected channel.
   - Select each mode switch on your transmitter in turn, and check that the desired flight mode is activated (the text turns yellow on _QGroundControl_ for the active mode).

All values are automatically saved as they are changed.

## See Also

- [PX4 Flight Modes](https://docs.px4.io/en/flight_modes/)
