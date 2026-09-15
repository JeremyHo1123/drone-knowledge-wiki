---
title: "TelemetryServer"
type: document
doc_set: MAVSDK
doc_version: MAVSDK-Python 3.17.2
section: plugins
source_url: "http://mavsdk-python-docs.s3-website.eu-central-1.amazonaws.com/plugins/telemetry_server.html"
upstream_repo: "mavlink/MAVSDK-Python"
upstream_path: "plugins/telemetry_server.md"
ingested: 2026-07-28
tags:
  - docs/mavsdk
  - docs/mavsdk/plugins
---

# TelemetryServer

class mavsdk.telemetry_server.AccelerationFrd(*forward_m_s2*, *right_m_s2*, *down_m_s2*)
:   Bases: `object`

    AccelerationFrd message type.

    Parameters:
    :   * **forward_m_s2** (*float*) – Acceleration in forward direction in metres per second^2
        * **right_m_s2** (*float*) – Acceleration in right direction in metres per second^2
        * **down_m_s2** (*float*) – Acceleration in down direction in metres per second^2

class mavsdk.telemetry_server.ActuatorControlTarget(*group*, *controls*)
:   Bases: `object`

    Actuator control target type.

    Parameters:
    :   * **group** (*int32_t*) – An actuator control group is e.g. ‘attitude’ for the core flight controls, or ‘gimbal’ for a payload.
        * **controls** (*[**float**]*) – Controls normed from -1 to 1, where 0 is neutral position.

class mavsdk.telemetry_server.ActuatorOutputStatus(*active*, *actuator*)
:   Bases: `object`

    Actuator output status type.

    Parameters:
    :   * **active** (*uint32_t*) – Active outputs
        * **actuator** (*[**float**]*) – Servo/motor output values

class mavsdk.telemetry_server.AngularVelocityBody(*roll_rad_s*, *pitch_rad_s*, *yaw_rad_s*)
:   Bases: `object`

    Angular velocity type.

    Parameters:
    :   * **roll_rad_s** (*float*) – Roll angular velocity
        * **pitch_rad_s** (*float*) – Pitch angular velocity
        * **yaw_rad_s** (*float*) – Yaw angular velocity

class mavsdk.telemetry_server.AngularVelocityFrd(*forward_rad_s*, *right_rad_s*, *down_rad_s*)
:   Bases: `object`

    AngularVelocityFrd message type.

    Parameters:
    :   * **forward_rad_s** (*float*) – Angular velocity in forward direction in radians per second
        * **right_rad_s** (*float*) – Angular velocity in right direction in radians per second
        * **down_rad_s** (*float*) – Angular velocity in Down direction in radians per second

class mavsdk.telemetry_server.Battery(*voltage_v*, *remaining_percent*)
:   Bases: `object`

    Battery type.

    Parameters:
    :   * **voltage_v** (*float*) – Voltage in volts
        * **remaining_percent** (*float*) – Estimated battery remaining (range: 0.0 to 1.0)

class mavsdk.telemetry_server.Covariance(*covariance_matrix*)
:   Bases: `object`

    Covariance type.

    Row-major representation of a 6x6 cross-covariance matrix
    upper right triangle.
    Set first to NaN if unknown.

    Parameters:
    :   **covariance_matrix** (*[**float**]*) – Representation of a covariance matrix.

class mavsdk.telemetry_server.DistanceSensor(*minimum_distance_m*, *maximum_distance_m*, *current_distance_m*)
:   Bases: `object`

    DistanceSensor message type.

    Parameters:
    :   * **minimum_distance_m** (*float*) – Minimum distance the sensor can measure, NaN if unknown.
        * **maximum_distance_m** (*float*) – Maximum distance the sensor can measure, NaN if unknown.
        * **current_distance_m** (*float*) – Current distance reading, NaN if unknown.

class mavsdk.telemetry_server.EulerAngle(*roll_deg*, *pitch_deg*, *yaw_deg*, *timestamp_us*)
:   Bases: `object`

    Euler angle type.

    All rotations and axis systems follow the right-hand rule.
    The Euler angles follow the convention of a 3-2-1 intrinsic Tait-Bryan rotation sequence.

    For more info see <https://en.wikipedia.org/wiki/Euler_angles>

    Parameters:
    :   * **roll_deg** (*float*) – Roll angle in degrees, positive is banking to the right
        * **pitch_deg** (*float*) – Pitch angle in degrees, positive is pitching nose up
        * **yaw_deg** (*float*) – Yaw angle in degrees, positive is clock-wise seen from above
        * **timestamp_us** (*uint64_t*) – Timestamp in microseconds

class mavsdk.telemetry_server.FixType(**values*)
:   Bases: `Enum`

    GPS fix type.

    ## Values

    NO_GPS
    :   No GPS connected

    NO_FIX
    :   No position information, GPS is connected

    FIX_2D
    :   2D position

    FIX_3D
    :   3D position

    FIX_DGPS
    :   DGPS/SBAS aided 3D position

    RTK_FLOAT
    :   RTK float, 3D position

    RTK_FIXED
    :   RTK Fixed, 3D position

    FIX_2D = 2

    FIX_3D = 3

    FIX_DGPS = 4

    NO_FIX = 1

    NO_GPS = 0

    RTK_FIXED = 6

    RTK_FLOAT = 5

class mavsdk.telemetry_server.FixedwingMetrics(*airspeed_m_s*, *throttle_percentage*, *climb_rate_m_s*, *groundspeed_m_s*, *heading_deg*, *absolute_altitude_m*)
:   Bases: `object`

    FixedwingMetrics message type.

    Parameters:
    :   * **airspeed_m_s** (*float*) – Current indicated airspeed (IAS) in metres per second
        * **throttle_percentage** (*float*) – Current throttle setting (0 to 100)
        * **climb_rate_m_s** (*float*) – Current climb rate in metres per second
        * **groundspeed_m_s** (*float*) – Current groundspeed metres per second
        * **heading_deg** (*float*) – Current heading in compass units (0-360, 0=north)
        * **absolute_altitude_m** (*float*) – Current altitude in metres (MSL)

class mavsdk.telemetry_server.GpsInfo(*num_satellites*, *fix_type*)
:   Bases: `object`

    GPS information type.

    Parameters:
    :   * **num_satellites** (*int32_t*) – Number of visible satellites in use
        * **fix_type** ([*FixType*](#mavsdk.telemetry_server.FixType "mavsdk.telemetry_server.FixType")) – Fix type

class mavsdk.telemetry_server.GroundTruth(*latitude_deg*, *longitude_deg*, *absolute_altitude_m*, *timestamp_us*)
:   Bases: `object`

    GroundTruth message type.

    Parameters:
    :   * **latitude_deg** (*double*) – Latitude in degrees (range: -90 to +90)
        * **longitude_deg** (*double*) – Longitude in degrees (range: -180 to 180)
        * **absolute_altitude_m** (*float*) – Altitude AMSL (above mean sea level) in metres
        * **timestamp_us** (*uint64_t*) – Timestamp in microseconds (since system boot)

class mavsdk.telemetry_server.Heading(*heading_deg*)
:   Bases: `object`

    Heading type used for global position

    Parameters:
    :   **heading_deg** (*double*) – Heading in degrees (range: 0 to +360)

class mavsdk.telemetry_server.Imu(*acceleration_frd*, *angular_velocity_frd*, *magnetic_field_frd*, *temperature_degc*, *timestamp_us*)
:   Bases: `object`

    Imu message type.

    Parameters:
    :   * **acceleration_frd** ([*AccelerationFrd*](#mavsdk.telemetry_server.AccelerationFrd "mavsdk.telemetry_server.AccelerationFrd")) – Acceleration
        * **angular_velocity_frd** ([*AngularVelocityFrd*](#mavsdk.telemetry_server.AngularVelocityFrd "mavsdk.telemetry_server.AngularVelocityFrd")) – Angular velocity
        * **magnetic_field_frd** ([*MagneticFieldFrd*](#mavsdk.telemetry_server.MagneticFieldFrd "mavsdk.telemetry_server.MagneticFieldFrd")) – Magnetic field
        * **temperature_degc** (*float*) – Temperature
        * **timestamp_us** (*uint64_t*) – Timestamp in microseconds

class mavsdk.telemetry_server.LandedState(**values*)
:   Bases: `Enum`

    Landed State enumeration.

    ## Values

    UNKNOWN
    :   Landed state is unknown

    ON_GROUND
    :   The vehicle is on the ground

    IN_AIR
    :   The vehicle is in the air

    TAKING_OFF
    :   The vehicle is taking off

    LANDING
    :   The vehicle is landing

    IN_AIR = 2

    LANDING = 4

    ON_GROUND = 1

    TAKING_OFF = 3

    UNKNOWN = 0

class mavsdk.telemetry_server.MagneticFieldFrd(*forward_gauss*, *right_gauss*, *down_gauss*)
:   Bases: `object`

    MagneticFieldFrd message type.

    Parameters:
    :   * **forward_gauss** (*float*) – Magnetic field in forward direction measured in Gauss
        * **right_gauss** (*float*) – Magnetic field in East direction measured in Gauss
        * **down_gauss** (*float*) – Magnetic field in Down direction measured in Gauss

class mavsdk.telemetry_server.Odometry(*time_usec*, *frame_id*, *child_frame_id*, *position_body*, *q*, *velocity_body*, *angular_velocity_body*, *pose_covariance*, *velocity_covariance*)
:   Bases: `object`

    Odometry message type.

    Parameters:
    :   * **time_usec** (*uint64_t*) – Timestamp (0 to use Backend timestamp).
        * **frame_id** ([*MavFrame*](#mavsdk.telemetry_server.Odometry.MavFrame "mavsdk.telemetry_server.Odometry.MavFrame")) – Coordinate frame of reference for the pose data.
        * **child_frame_id** ([*MavFrame*](#mavsdk.telemetry_server.Odometry.MavFrame "mavsdk.telemetry_server.Odometry.MavFrame")) – Coordinate frame of reference for the velocity in free space (twist) data.
        * **position_body** ([*PositionBody*](#mavsdk.telemetry_server.PositionBody "mavsdk.telemetry_server.PositionBody")) – Position.
        * **q** ([*Quaternion*](#mavsdk.telemetry_server.Quaternion "mavsdk.telemetry_server.Quaternion")) – Quaternion components, w, x, y, z (1 0 0 0 is the null-rotation).
        * **velocity_body** ([*VelocityBody*](#mavsdk.telemetry_server.VelocityBody "mavsdk.telemetry_server.VelocityBody")) – Linear velocity (m/s).
        * **angular_velocity_body** ([*AngularVelocityBody*](#mavsdk.telemetry_server.AngularVelocityBody "mavsdk.telemetry_server.AngularVelocityBody")) – Angular velocity (rad/s).
        * **pose_covariance** ([*Covariance*](#mavsdk.telemetry_server.Covariance "mavsdk.telemetry_server.Covariance")) – Pose cross-covariance matrix.
        * **velocity_covariance** ([*Covariance*](#mavsdk.telemetry_server.Covariance "mavsdk.telemetry_server.Covariance")) – Velocity cross-covariance matrix.

    class MavFrame(**values*)
    :   Bases: `Enum`

        Mavlink frame id

        ## Values

        UNDEF
        :   Frame is undefined.

        BODY_NED
        :   Setpoint in body NED frame. This makes sense if all position control is externalized - e.g. useful to command 2 m/s^2 acceleration to the right.

        VISION_NED
        :   Odometry local coordinate frame of data given by a vision estimation system, Z-down (x: north, y: east, z: down).

        ESTIM_NED
        :   Odometry local coordinate frame of data given by an estimator running onboard the vehicle, Z-down (x: north, y: east, z: down).

        BODY_NED = 1

        ESTIM_NED = 3

        UNDEF = 0

        VISION_NED = 2

class mavsdk.telemetry_server.Position(*latitude_deg*, *longitude_deg*, *absolute_altitude_m*, *relative_altitude_m*)
:   Bases: `object`

    Position type in global coordinates.

    Parameters:
    :   * **latitude_deg** (*double*) – Latitude in degrees (range: -90 to +90)
        * **longitude_deg** (*double*) – Longitude in degrees (range: -180 to +180)
        * **absolute_altitude_m** (*float*) – Altitude AMSL (above mean sea level) in metres
        * **relative_altitude_m** (*float*) – Altitude relative to takeoff altitude in metres

class mavsdk.telemetry_server.PositionBody(*x_m*, *y_m*, *z_m*)
:   Bases: `object`

    Position type, represented in the Body (X Y Z) frame

    Parameters:
    :   * **x_m** (*float*) – X Position in metres.
        * **y_m** (*float*) – Y Position in metres.
        * **z_m** (*float*) – Z Position in metres.

class mavsdk.telemetry_server.PositionNed(*north_m*, *east_m*, *down_m*)
:   Bases: `object`

    PositionNed message type.

    Parameters:
    :   * **north_m** (*float*) – Position along north direction in metres
        * **east_m** (*float*) – Position along east direction in metres
        * **down_m** (*float*) – Position along down direction in metres

class mavsdk.telemetry_server.PositionVelocityNed(*position*, *velocity*)
:   Bases: `object`

    PositionVelocityNed message type.

    Parameters:
    :   * **position** ([*PositionNed*](#mavsdk.telemetry_server.PositionNed "mavsdk.telemetry_server.PositionNed")) – Position (NED)
        * **velocity** ([*VelocityNed*](#mavsdk.telemetry_server.VelocityNed "mavsdk.telemetry_server.VelocityNed")) – Velocity (NED)

class mavsdk.telemetry_server.Quaternion(*w*, *x*, *y*, *z*, *timestamp_us*)
:   Bases: `object`

    Quaternion type.

    All rotations and axis systems follow the right-hand rule.
    The Hamilton quaternion product definition is used.
    A zero-rotation quaternion is represented by (1,0,0,0).
    The quaternion could also be written as w + xi + yj + zk.

    For more info see: <https://en.wikipedia.org/wiki/Quaternion>

    Parameters:
    :   * **w** (*float*) – Quaternion entry 0, also denoted as a
        * **x** (*float*) – Quaternion entry 1, also denoted as b
        * **y** (*float*) – Quaternion entry 2, also denoted as c
        * **z** (*float*) – Quaternion entry 3, also denoted as d
        * **timestamp_us** (*uint64_t*) – Timestamp in microseconds

class mavsdk.telemetry_server.RawGps(*timestamp_us*, *latitude_deg*, *longitude_deg*, *absolute_altitude_m*, *hdop*, *vdop*, *velocity_m_s*, *cog_deg*, *altitude_ellipsoid_m*, *horizontal_uncertainty_m*, *vertical_uncertainty_m*, *velocity_uncertainty_m_s*, *heading_uncertainty_deg*, *yaw_deg*)
:   Bases: `object`

    Raw GPS information type.

    Warning: this is an advanced type! If you want the location of the drone, use
    the position instead. This message exposes the raw values of the GNSS sensor.

    Parameters:
    :   * **timestamp_us** (*uint64_t*) – Timestamp in microseconds (UNIX Epoch time or time since system boot, to be inferred)
        * **latitude_deg** (*double*) – Latitude in degrees (WGS84, EGM96 ellipsoid)
        * **longitude_deg** (*double*) – Longitude in degrees (WGS84, EGM96 ellipsoid)
        * **absolute_altitude_m** (*float*) – Altitude AMSL (above mean sea level) in metres
        * **hdop** (*float*) – GPS HDOP horizontal dilution of position (unitless). If unknown, set to NaN
        * **vdop** (*float*) – GPS VDOP vertical dilution of position (unitless). If unknown, set to NaN
        * **velocity_m_s** (*float*) – Ground velocity in metres per second
        * **cog_deg** (*float*) – Course over ground (NOT heading, but direction of movement) in degrees. If unknown, set to NaN
        * **altitude_ellipsoid_m** (*float*) – Altitude in metres (above WGS84, EGM96 ellipsoid)
        * **horizontal_uncertainty_m** (*float*) – Position uncertainty in metres
        * **vertical_uncertainty_m** (*float*) – Altitude uncertainty in metres
        * **velocity_uncertainty_m_s** (*float*) – Velocity uncertainty in metres per second
        * **heading_uncertainty_deg** (*float*) – Heading uncertainty in degrees
        * **yaw_deg** (*float*) – Yaw in earth frame from north.

class mavsdk.telemetry_server.RcStatus(*was_available_once*, *is_available*, *signal_strength_percent*)
:   Bases: `object`

    Remote control status type.

    Parameters:
    :   * **was_available_once** (*bool*) – True if an RC signal has been available once
        * **is_available** (*bool*) – True if the RC signal is available now
        * **signal_strength_percent** (*float*) – Signal strength (range: 0 to 100, NaN if unknown)

class mavsdk.telemetry_server.ScaledPressure(*timestamp_us*, *absolute_pressure_hpa*, *differential_pressure_hpa*, *temperature_deg*, *differential_pressure_temperature_deg*)
:   Bases: `object`

    Scaled Pressure message type.

    Parameters:
    :   * **timestamp_us** (*uint64_t*) – Timestamp (time since system boot)
        * **absolute_pressure_hpa** (*float*) – Absolute pressure in hPa
        * **differential_pressure_hpa** (*float*) – Differential pressure 1 in hPa
        * **temperature_deg** (*float*) – Absolute pressure temperature (in celsius)
        * **differential_pressure_temperature_deg** (*float*) – Differential pressure temperature (in celsius, 0 if not available)

class mavsdk.telemetry_server.StatusText(*type*, *text*)
:   Bases: `object`

    StatusText information type.

    Parameters:
    :   * **type** ([*StatusTextType*](#mavsdk.telemetry_server.StatusTextType "mavsdk.telemetry_server.StatusTextType")) – Message type
        * **text** (*std::string*) – MAVLink status message

class mavsdk.telemetry_server.StatusTextType(**values*)
:   Bases: `Enum`

    Status types.

    ## Values

    DEBUG
    :   Debug

    INFO
    :   Information

    NOTICE
    :   Notice

    WARNING
    :   Warning

    ERROR
    :   Error

    CRITICAL
    :   Critical

    ALERT
    :   Alert

    EMERGENCY
    :   Emergency

    ALERT = 6

    CRITICAL = 5

    DEBUG = 0

    EMERGENCY = 7

    ERROR = 4

    INFO = 1

    NOTICE = 2

    WARNING = 3

class mavsdk.telemetry_server.TelemetryServer(*async_plugin_manager*)
:   Bases: `AsyncBase`

    Allow users to provide vehicle telemetry and state information
    (e.g. battery, GPS, RC connection, flight mode etc.) and set telemetry update rates.

    Generated by dcsdkgen - MAVSDK TelemetryServer API

    name = 'TelemetryServer'

    async publish_attitude(*angle*, *angular_velocity*)
    :   Publish to “attitude” updates.

        Parameters:
        :   * **angle** ([*EulerAngle*](#mavsdk.telemetry_server.EulerAngle "mavsdk.telemetry_server.EulerAngle")) – roll/pitch/yaw body angles
            * **angular_velocity** ([*AngularVelocityBody*](#mavsdk.telemetry_server.AngularVelocityBody "mavsdk.telemetry_server.AngularVelocityBody")) – roll/pitch/yaw angular velocities

        Raises:
        :   [**TelemetryServerError**](#mavsdk.telemetry_server.TelemetryServerError "mavsdk.telemetry_server.TelemetryServerError") – If the request fails. The error contains the reason for the failure.

    async publish_battery(*battery*)
    :   Publish to ‘battery’ updates.

        Parameters:
        :   **battery** ([*Battery*](#mavsdk.telemetry_server.Battery "mavsdk.telemetry_server.Battery")) – The next ‘battery’ state

        Raises:
        :   [**TelemetryServerError**](#mavsdk.telemetry_server.TelemetryServerError "mavsdk.telemetry_server.TelemetryServerError") – If the request fails. The error contains the reason for the failure.

    async publish_distance_sensor(*distance_sensor*)
    :   Publish to “distance sensor” updates.

        Parameters:
        :   **distance_sensor** ([*DistanceSensor*](#mavsdk.telemetry_server.DistanceSensor "mavsdk.telemetry_server.DistanceSensor")) – The next ‘Distance Sensor’ status

        Raises:
        :   [**TelemetryServerError**](#mavsdk.telemetry_server.TelemetryServerError "mavsdk.telemetry_server.TelemetryServerError") – If the request fails. The error contains the reason for the failure.

    async publish_extended_sys_state(*vtol_state*, *landed_state*)
    :   Publish ‘extended sys state’ updates.

        Parameters:
        :   * **vtol_state** ([*VtolState*](#mavsdk.telemetry_server.VtolState "mavsdk.telemetry_server.VtolState"))
            * **landed_state** ([*LandedState*](#mavsdk.telemetry_server.LandedState "mavsdk.telemetry_server.LandedState"))

        Raises:
        :   [**TelemetryServerError**](#mavsdk.telemetry_server.TelemetryServerError "mavsdk.telemetry_server.TelemetryServerError") – If the request fails. The error contains the reason for the failure.

    async publish_ground_truth(*ground_truth*)
    :   Publish to ‘ground truth’ updates.

        Parameters:
        :   **ground_truth** ([*GroundTruth*](#mavsdk.telemetry_server.GroundTruth "mavsdk.telemetry_server.GroundTruth")) – Ground truth position information available in simulation

        Raises:
        :   [**TelemetryServerError**](#mavsdk.telemetry_server.TelemetryServerError "mavsdk.telemetry_server.TelemetryServerError") – If the request fails. The error contains the reason for the failure.

    async publish_home(*home*)
    :   Publish to ‘home position’ updates.

        Parameters:
        :   **home** ([*Position*](#mavsdk.telemetry_server.Position "mavsdk.telemetry_server.Position")) – The next home position

        Raises:
        :   [**TelemetryServerError**](#mavsdk.telemetry_server.TelemetryServerError "mavsdk.telemetry_server.TelemetryServerError") – If the request fails. The error contains the reason for the failure.

    async publish_imu(*imu*)
    :   Publish to ‘IMU’ updates (in SI units in NED body frame).

        Parameters:
        :   **imu** ([*Imu*](#mavsdk.telemetry_server.Imu "mavsdk.telemetry_server.Imu")) – The next IMU status

        Raises:
        :   [**TelemetryServerError**](#mavsdk.telemetry_server.TelemetryServerError "mavsdk.telemetry_server.TelemetryServerError") – If the request fails. The error contains the reason for the failure.

    async publish_odometry(*odometry*)
    :   Publish to ‘odometry’ updates.

        Parameters:
        :   **odometry** ([*Odometry*](#mavsdk.telemetry_server.Odometry "mavsdk.telemetry_server.Odometry")) – The next odometry status

        Raises:
        :   [**TelemetryServerError**](#mavsdk.telemetry_server.TelemetryServerError "mavsdk.telemetry_server.TelemetryServerError") – If the request fails. The error contains the reason for the failure.

    async publish_position(*position*, *velocity_ned*, *heading*)
    :   Publish to ‘position’ updates.

        Parameters:
        :   * **position** ([*Position*](#mavsdk.telemetry_server.Position "mavsdk.telemetry_server.Position")) – The next position
            * **velocity_ned** ([*VelocityNed*](#mavsdk.telemetry_server.VelocityNed "mavsdk.telemetry_server.VelocityNed")) – The next velocity (NED)
            * **heading** ([*Heading*](#mavsdk.telemetry_server.Heading "mavsdk.telemetry_server.Heading")) – Heading (yaw) in degrees

        Raises:
        :   [**TelemetryServerError**](#mavsdk.telemetry_server.TelemetryServerError "mavsdk.telemetry_server.TelemetryServerError") – If the request fails. The error contains the reason for the failure.

    async publish_position_velocity_ned(*position_velocity_ned*)
    :   Publish to ‘position velocity’ updates.

        Parameters:
        :   **position_velocity_ned** ([*PositionVelocityNed*](#mavsdk.telemetry_server.PositionVelocityNed "mavsdk.telemetry_server.PositionVelocityNed")) – The next position and velocity status

        Raises:
        :   [**TelemetryServerError**](#mavsdk.telemetry_server.TelemetryServerError "mavsdk.telemetry_server.TelemetryServerError") – If the request fails. The error contains the reason for the failure.

    async publish_raw_gps(*raw_gps*, *gps_info*)
    :   Publish to ‘Raw GPS’ updates.

        Parameters:
        :   * **raw_gps** ([*RawGps*](#mavsdk.telemetry_server.RawGps "mavsdk.telemetry_server.RawGps")) – The next ‘Raw GPS’ state. Warning: this is an advanced feature, use Position updates to get the location of the drone!
            * **gps_info** ([*GpsInfo*](#mavsdk.telemetry_server.GpsInfo "mavsdk.telemetry_server.GpsInfo")) – The next ‘GPS info’ state

        Raises:
        :   [**TelemetryServerError**](#mavsdk.telemetry_server.TelemetryServerError "mavsdk.telemetry_server.TelemetryServerError") – If the request fails. The error contains the reason for the failure.

    async publish_raw_imu(*imu*)
    :   Publish to ‘Raw IMU’ updates.

        Parameters:
        :   **imu** ([*Imu*](#mavsdk.telemetry_server.Imu "mavsdk.telemetry_server.Imu")) – The next raw IMU status

        Raises:
        :   [**TelemetryServerError**](#mavsdk.telemetry_server.TelemetryServerError "mavsdk.telemetry_server.TelemetryServerError") – If the request fails. The error contains the reason for the failure.

    async publish_scaled_imu(*imu*)
    :   Publish to ‘Scaled IMU’ updates.

        Parameters:
        :   **imu** ([*Imu*](#mavsdk.telemetry_server.Imu "mavsdk.telemetry_server.Imu")) – The next scaled IMU status

        Raises:
        :   [**TelemetryServerError**](#mavsdk.telemetry_server.TelemetryServerError "mavsdk.telemetry_server.TelemetryServerError") – If the request fails. The error contains the reason for the failure.

    async publish_status_text(*status_text*)
    :   Publish to ‘status text’ updates.

        Parameters:
        :   **status_text** ([*StatusText*](#mavsdk.telemetry_server.StatusText "mavsdk.telemetry_server.StatusText")) – The next ‘status text’

        Raises:
        :   [**TelemetryServerError**](#mavsdk.telemetry_server.TelemetryServerError "mavsdk.telemetry_server.TelemetryServerError") – If the request fails. The error contains the reason for the failure.

    async publish_sys_status(*battery*, *rc_receiver_status*, *gyro_status*, *accel_status*, *mag_status*, *gps_status*)
    :   Publish ‘sys status’ updates.

        Parameters:
        :   * **battery** ([*Battery*](#mavsdk.telemetry_server.Battery "mavsdk.telemetry_server.Battery")) – The next ‘battery’ state
            * **rc_receiver_status** (*bool*) – rc receiver status
            * **gyro_status** (*bool*)
            * **accel_status** (*bool*)
            * **mag_status** (*bool*)
            * **gps_status** (*bool*)

        Raises:
        :   [**TelemetryServerError**](#mavsdk.telemetry_server.TelemetryServerError "mavsdk.telemetry_server.TelemetryServerError") – If the request fails. The error contains the reason for the failure.

    async publish_unix_epoch_time(*time_us*)
    :   Publish to ‘unix epoch time’ updates.

        Parameters:
        :   **time_us** (*uint64_t*) – The next ‘unix epoch time’ status

        Raises:
        :   [**TelemetryServerError**](#mavsdk.telemetry_server.TelemetryServerError "mavsdk.telemetry_server.TelemetryServerError") – If the request fails. The error contains the reason for the failure.

    async publish_visual_flight_rules_hud(*fixed_wing_metrics*)
    :   Publish to “Visual Flight Rules HUD” updates.

        Parameters:
        :   **fixed_wing_metrics** ([*FixedwingMetrics*](#mavsdk.telemetry_server.FixedwingMetrics "mavsdk.telemetry_server.FixedwingMetrics"))

        Raises:
        :   [**TelemetryServerError**](#mavsdk.telemetry_server.TelemetryServerError "mavsdk.telemetry_server.TelemetryServerError") – If the request fails. The error contains the reason for the failure.

exception mavsdk.telemetry_server.TelemetryServerError(*result*, *origin*, **params*)
:   Bases: `Exception`

    Raised when a TelemetryServerResult is a fail code

class mavsdk.telemetry_server.TelemetryServerResult(*result*, *result_str*)
:   Bases: `object`

    Result type.

    Parameters:
    :   * **result** ([*Result*](#mavsdk.telemetry_server.TelemetryServerResult.Result "mavsdk.telemetry_server.TelemetryServerResult.Result")) – Result enum value
        * **result_str** (*std::string*) – Human-readable English string describing the result

    class Result(**values*)
    :   Bases: `Enum`

        Possible results returned for telemetry requests.

        ## Values

        UNKNOWN
        :   Unknown result

        SUCCESS
        :   Success: the telemetry command was accepted by the vehicle

        NO_SYSTEM
        :   No system connected

        CONNECTION_ERROR
        :   Connection error

        BUSY
        :   Vehicle is busy

        COMMAND_DENIED
        :   Command refused by vehicle

        TIMEOUT
        :   Request timed out

        UNSUPPORTED
        :   Request not supported

        BUSY = 4

        COMMAND_DENIED = 5

        CONNECTION_ERROR = 3

        NO_SYSTEM = 2

        SUCCESS = 1

        TIMEOUT = 6

        UNKNOWN = 0

        UNSUPPORTED = 7

class mavsdk.telemetry_server.VelocityBody(*x_m_s*, *y_m_s*, *z_m_s*)
:   Bases: `object`

    Velocity type, represented in the Body (X Y Z) frame and in metres/second.

    Parameters:
    :   * **x_m_s** (*float*) – Velocity in X in metres/second
        * **y_m_s** (*float*) – Velocity in Y in metres/second
        * **z_m_s** (*float*) – Velocity in Z in metres/second

class mavsdk.telemetry_server.VelocityNed(*north_m_s*, *east_m_s*, *down_m_s*)
:   Bases: `object`

    VelocityNed message type.

    Parameters:
    :   * **north_m_s** (*float*) – Velocity along north direction in metres per second
        * **east_m_s** (*float*) – Velocity along east direction in metres per second
        * **down_m_s** (*float*) – Velocity along down direction in metres per second

class mavsdk.telemetry_server.VtolState(**values*)
:   Bases: `Enum`

    Maps to MAV_VTOL_STATE

    ## Values

    UNDEFINED
    :   Not VTOL

    TRANSITION_TO_FW
    :   Transitioning to fixed-wing

    TRANSITION_TO_MC
    :   Transitioning to multi-copter

    MC
    :   Multi-copter

    FW
    :   Fixed-wing

    FW = 4

    MC = 3

    TRANSITION_TO_FW = 1

    TRANSITION_TO_MC = 2

    UNDEFINED = 0
