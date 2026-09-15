---
title: "MAVSDK-Python API reference"
type: document
doc_set: MAVSDK
doc_version: MAVSDK-Python 3.17.2
section: root
source_url: "http://mavsdk-python-docs.s3-website.eu-central-1.amazonaws.com/index.html"
upstream_repo: "mavlink/MAVSDK-Python"
upstream_path: "index.md"
ingested: 2026-07-28
tags:
  - docs/mavsdk
  - docs/mavsdk/root
---

# MAVSDK-Python API reference

Contents:

* [System](system.md)
  + [`System`](system.md#mavsdk.system.System)
* [Plugins](plugins/index.md)
  + [Action](plugins/action.md)
  + [ActionServer](plugins/action_server.md)
  + [ArmAuthorizerServer](plugins/arm_authorizer_server.md)
  + [Calibration](plugins/calibration.md)
  + [Camera](plugins/camera.md)
  + [CameraServer](plugins/camera_server.md)
  + [ComponentMetadata](plugins/component_metadata.md)
  + [ComponentMetadataServer](plugins/component_metadata_server.md)
  + [Core](plugins/core.md)
  + [Failure](plugins/failure.md)
  + [FollowMe](plugins/follow_me.md)
  + [Ftp](plugins/ftp.md)
  + [FtpServer](plugins/ftp_server.md)
  + [Geofence](plugins/geofence.md)
  + [Gimbal](plugins/gimbal.md)
  + [Gripper](plugins/gripper.md)
  + [Info](plugins/info.md)
  + [LogFiles](plugins/log_files.md)
  + [LogStreaming](plugins/log_streaming.md)
  + [ManualControl](plugins/manual_control.md)
  + [Mission](plugins/mission.md)
  + [MissionRaw](plugins/mission_raw.md)
  + [MissionRawServer](plugins/mission_raw_server.md)
  + [Mocap](plugins/mocap.md)
  + [Offboard](plugins/offboard.md)
  + [Param](plugins/param.md)
  + [ParamServer](plugins/param_server.md)
  + [Rtk](plugins/rtk.md)
  + [ServerUtility](plugins/server_utility.md)
  + [Shell](plugins/shell.md)
  + [Telemetry](plugins/telemetry.md)
  + [TelemetryServer](plugins/telemetry_server.md)
  + [TrackingServer](plugins/tracking_server.md)
  + [Transponder](plugins/transponder.md)
  + [Tune](plugins/tune.md)
  + [Winch](plugins/winch.md)
  + [Events](plugins/events.md)
  + [MavlinkDirect](plugins/mavlink_direct.md)
* [Jetson Nano Install](jetson-nano-install.md)
  + [Ubuntu 18.04](jetson-nano-install.md#ubuntu-18-04)
  + [Ubuntu 20.04](jetson-nano-install.md#ubuntu-20-04)

## Important Notes

* Python 3.7+ is required.
* You may need to run `pip3` instead of `pip` and `python3` instead of `python`, depending of your system defaults.
* Auterion has a _Getting started with MAVSDK-Python: <https://auterion.com/getting-started-with-mavsdk-python/> guide if you’re a beginner and not sure where to start.

## Install using pip from PyPi

To install simply run:

```
python -m pip install --upgrade mavsdk
```

The package contains `mavsdk_server` already (previously called “backend”), which is started automatically when connecting (e.g. `await drone.connect()`). Have a look at the examples to see it used in practice. It will be something like:

```
python
from mavsdk import System
...
drone = System()
await drone.connect(system_address="udpin://0.0.0.0:14540")
```

Note: `System()` takes two named parameters: `mavsdk_server_address` and `port`. When left empty, they default to `None` and `50051`, respectively, and `mavsdk_server -p 50051` is run by `await drone.connect()`. If `mavsdk_server_address` is set (e.g. to “localhost”), then `await drone.connect()` will not start the embedded `mavsdk_server` and will try to connect to a server running at this address. This is useful for platforms where `mavsdk_server` does not come embedded, for debugging purposes, and for running `mavsdk_server` in a place different than where the MAVSDK-Python script is run.

For specific platforms, check the detailed install instructions:

* [Jetson Nano Install](jetson-nano-install.md#jetson-nano-install)

## Run the examples

Once the package has been installed, the examples can be run:

```
examples/takeoff_and_land.py
```

The examples assume that the embedded `mavsdk_server` binary can be run. In some cases (e.g. on Raspberry Pi), it may be necessary to run `mavsdk_server` manually, and therefore to set `mavsdk_server_address='localhost'` as described above.

## Debug connection issues

MAVSDK-Python automatically captures and displays important messages from `mavsdk_server`. Error and warning messages are shown by default, while informational messages can be enabled for more detailed debugging.

**For basic debugging (recommended):**

```
import logging
logging.basicConfig(level=logging.INFO)
```

This will show connection attempts, version information, and any errors or warnings from `mavsdk_server`.

**For detailed debugging:**

```
import logging
logging.basicConfig(level=logging.DEBUG)
```

This shows all messages including internal debug information.

**For server-only messages:**

You can also control just the `mavsdk_server` output:

```
import logging
logging.basicConfig(level=logging.WARNING)  # Hide most messages
logging.getLogger('mavsdk_server').setLevel(logging.INFO)  # Show server info
```

**To disable server messages completely:**

```
import logging
logging.getLogger('mavsdk_server').setLevel(logging.CRITICAL)  # Hide all server output
```

**Common error messages:**

If you see error messages like these, they indicate connection string issues:

```
ERROR:mavsdk_server:Unknown protocol (cli_arg.cpp:62)
ERROR:mavsdk_server:Connection failed: Invalid connection URL
```

Check that your connection string follows the correct format (e.g. `udpin://0.0.0.0:14540`).

**Running mavsdk_server separately:**

In order to get more debugging information, it is possible to run the mavsdk_server binary separately.

For this case, let’s assume the example was like this:

```
drone = System()
await drone.connect(system_address="udpin://0.0.0.0:14540")
```

The mavsdk_server binary is installed using `pip`. If installed with `python -m pip install --upgrade mavsdk` it is usually (at least for Linux) to be found in `~/.local/lib/python3.10/site-packages/mavsdk/bin/` (of course depending on the Python version used).

It can then be run in a separate console with the `system_address` as an argument:

```
~/.local/lib/python3.10/site-packages/mavsdk/bin/mavsdk_server udpin://0.0.0.0:14540
```

Without an autopilot connecting, the output will look something like:

```
[02:36:31|Info ] MAVSDK version: v1.4.16 (mavsdk_impl.cpp:28)
[02:36:31|Info ] Waiting to discover system on udpin://0.0.0.0:14540... (connection_initiator.h:20)
```

Once an autopilot is discovered, something like this should be printed:

```
[02:38:12|Info ] MAVSDK version: v1.4.16 (mavsdk_impl.cpp:28)
[02:38:12|Info ] Waiting to discover system on udpin://0.0.0.0:14540... (connection_initiator.h:20)
[02:39:01|Info ] New system on: 127.0.0.1:14580 (with sysid: 1) (udp_connection.cpp:194)
[02:39:01|Debug] New: System ID: 1 Comp ID: 1 (mavsdk_impl.cpp:484)
[02:39:01|Debug] Component Autopilot (1) added. (system_impl.cpp:355)
[02:39:02|Debug] Discovered 1 component(s) (system_impl.cpp:523)
[02:39:02|Info ] System discovered (connection_initiator.h:63)
[02:39:02|Info ] Server started (grpc_server.cpp:52)
[02:39:02|Info ] Server set to listen on 0.0.0.0:50051 (grpc_server.cpp:53)
```

This would look promising, and the example can now be run against this server, however, without `system_address`:

```
drone = System()
await drone.connect()
```

# Indices and tables

* [Index](genindex.md)
* [Module Index](py-modindex.md)
* [Search Page](search.md)

### Table of Contents

* MAVSDK-Python API reference
  + [Important Notes](#important-notes)
  + [Install using pip from PyPi](#install-using-pip-from-pypi)
  + [Run the examples](#run-the-examples)
  + [Debug connection issues](#debug-connection-issues)
* [Indices and tables](#indices-and-tables)

#### Next topic

[System](system.md)

### This Page

* [Show Source](_sources/index.rst.txt)

### Quick search
