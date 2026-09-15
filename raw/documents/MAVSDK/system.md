---
title: "System"
type: document
doc_set: MAVSDK
doc_version: MAVSDK-Python 3.17.2
section: root
source_url: "http://mavsdk-python-docs.s3-website.eu-central-1.amazonaws.com/system.html"
upstream_repo: "mavlink/MAVSDK-Python"
upstream_path: "system.md"
ingested: 2026-07-28
tags:
  - docs/mavsdk
  - docs/mavsdk/root
---

# System

class mavsdk.system.System(*mavsdk_server_address=None*, *port=50051*, *sysid=245*, *compid=190*)
:   Bases: `object`

    Instantiate a System object, that will serve as a proxy to
    all the MAVSDK plugins.

    Parameters:
    :   * **mavsdk_server_address** (*str*) – Address of a running mavsdk_server instance. If None,
          an instance of mavsdk_server will be automatically
          started (on localhost).
        * **port** (*int*) – Port of the running mavsdk_server instance specified by
          mavsdk_server_address.
        * **sysid** (*int*) – MAVLink system ID of the mavsdk_server (1..255).
        * **compid** (*int*) – MAVLink component ID of the mavsdk_server (1..255).

    property action: [Action](plugins/action.md#mavsdk.action.Action)

    property action_server: [ActionServer](plugins/action_server.md#mavsdk.action_server.ActionServer)

    property arm_authorizer_server: [ArmAuthorizerServer](plugins/arm_authorizer_server.md#mavsdk.arm_authorizer_server.ArmAuthorizerServer)

    property calibration: [Calibration](plugins/calibration.md#mavsdk.calibration.Calibration)

    property camera: [Camera](plugins/camera.md#mavsdk.camera.Camera)

    property camera_server: [CameraServer](plugins/camera_server.md#mavsdk.camera_server.CameraServer)

    property component_metadata: [ComponentMetadata](plugins/component_metadata.md#mavsdk.component_metadata.ComponentMetadata)

    property component_metadata_server: [ComponentMetadataServer](plugins/component_metadata_server.md#mavsdk.component_metadata_server.ComponentMetadataServer)

    async connect(*system_address=None*)
    :   Connect the System object to a remote system.

        Parameters:
        :   **system_address** (*str*) –

            The address of the remote system. If None, it will
            default to udpin://0.0.0.0:14540. Supported URL formats:

            > * Serial: serial:///path/to/serial/dev[:baudrate]
            > * UDP in: udpin://bind_host:bind_port
            > * UDP out: udpout://dest_host:dest_port
            > * TCP in: tcpin://bind_host:bind_port
            > * TCP out: tcpout://dest_host:dest_port

    property core: [Core](plugins/core.md#mavsdk.core.Core)

    static error_uninitialized(*plugin_name: str*) → str

    property events: [Events](plugins/events.md#mavsdk.events.Events)

    property failure: [Failure](plugins/failure.md#mavsdk.failure.Failure)

    property follow_me: [FollowMe](plugins/follow_me.md#mavsdk.follow_me.FollowMe)

    property ftp: [Ftp](plugins/ftp.md#mavsdk.ftp.Ftp)

    property ftp_server: [FtpServer](plugins/ftp_server.md#mavsdk.ftp_server.FtpServer)

    property geofence: [Geofence](plugins/geofence.md#mavsdk.geofence.Geofence)

    property gimbal: [Gimbal](plugins/gimbal.md#mavsdk.gimbal.Gimbal)

    property gripper: [Gripper](plugins/gripper.md#mavsdk.gripper.Gripper)

    property info: [Info](plugins/info.md#mavsdk.info.Info)

    property log_files: [LogFiles](plugins/log_files.md#mavsdk.log_files.LogFiles)

    property log_streaming: [LogStreaming](plugins/log_streaming.md#mavsdk.log_streaming.LogStreaming)

    property manual_control: [ManualControl](plugins/manual_control.md#mavsdk.manual_control.ManualControl)

    property mavlink_direct: [MavlinkDirect](plugins/mavlink_direct.md#mavsdk.mavlink_direct.MavlinkDirect)

    property mission: [Mission](plugins/mission.md#mavsdk.mission.Mission)

    property mission_raw: [MissionRaw](plugins/mission_raw.md#mavsdk.mission_raw.MissionRaw)

    property mission_raw_server: [MissionRawServer](plugins/mission_raw_server.md#mavsdk.mission_raw_server.MissionRawServer)

    property mocap: [Mocap](plugins/mocap.md#mavsdk.mocap.Mocap)

    property offboard: [Offboard](plugins/offboard.md#mavsdk.offboard.Offboard)

    property param: [Param](plugins/param.md#mavsdk.param.Param)

    property param_server: [ParamServer](plugins/param_server.md#mavsdk.param_server.ParamServer)

    property rtk: [Rtk](plugins/rtk.md#mavsdk.rtk.Rtk)

    property server_utility: [ServerUtility](plugins/server_utility.md#mavsdk.server_utility.ServerUtility)

    property shell: [Shell](plugins/shell.md#mavsdk.shell.Shell)

    property telemetry: [Telemetry](plugins/telemetry.md#mavsdk.telemetry.Telemetry)

    property telemetry_server: [TelemetryServer](plugins/telemetry_server.md#mavsdk.telemetry_server.TelemetryServer)

    property tracking_server: [TrackingServer](plugins/tracking_server.md#mavsdk.tracking_server.TrackingServer)

    property transponder: [Transponder](plugins/transponder.md#mavsdk.transponder.Transponder)

    property tune: [Tune](plugins/tune.md#mavsdk.tune.Tune)

    property winch: [Winch](plugins/winch.md#mavsdk.winch.Winch)
