---
title: "Telemetry"
type: document
doc_set: MAVSDK
doc_version: MAVSDK-Python 3.17.2
section: plugins
source_url: "http://mavsdk-python-docs.s3-website.eu-central-1.amazonaws.com/plugins/telemetry.html"
upstream_repo: "mavlink/MAVSDK-Python"
upstream_path: "plugins/telemetry.md"
ingested: 2026-07-28
tags:
  - docs/mavsdk
  - docs/mavsdk/plugins
---

# Telemetry

class mavsdk.telemetry.AccelerationFrd(*forward_m_s2*, *right_m_s2*, *down_m_s2*)
:   Bases: `object`

    AccelerationFrd message type.

    Parameters:
    :   * **forward_m_s2** (*float*) – Acceleration in forward direction in metres per second^2
        * **right_m_s2** (*float*) – Acceleration in right direction in metres per second^2
        * **down_m_s2** (*float*) – Acceleration in down direction in metres per second^2

class mavsdk.telemetry.ActuatorControlTarget(*group*, *controls*)
:   Bases: `object`

    Actuator control target type.

    Parameters:
    :   * **group** (*int32_t*) – An actuator control group is e.g. ‘attitude’ for the core flight controls, or ‘gimbal’ for a payload.
        * **controls** (*[**float**]*) – Controls normed from -1 to 1, where 0 is neutral position.

class mavsdk.telemetry.ActuatorOutputStatus(*active*, *actuator*)
:   Bases: `object`

    Actuator output status type.

    Parameters:
    :   * **active** (*uint32_t*) – Active outputs
        * **actuator** (*[**float**]*) – Servo/motor output values

class mavsdk.telemetry.Altitude(*altitude_monotonic_m*, *altitude_amsl_m*, *altitude_local_m*, *altitude_relative_m*, *altitude_terrain_m*, *bottom_clearance_m*, *timestamp_us*)
:   Bases: `object`

    Altitude message type

    Parameters:
    :   * **altitude_monotonic_m** (*float*) – Altitude in meters is initialized on system boot and monotonic
        * **altitude_amsl_m** (*float*) – Altitude AMSL (above mean sea level) in meters
        * **altitude_local_m** (*float*) – Local altitude in meters
        * **altitude_relative_m** (*float*) – Altitude above home position in meters
        * **altitude_terrain_m** (*float*) – Altitude above terrain in meters
        * **bottom_clearance_m** (*float*) – This is not the altitude, but the clear space below the system according to the fused clearance estimate in meters.
        * **timestamp_us** (*uint64_t*) – Timestamp in microseconds (since system boot)

class mavsdk.telemetry.AngularVelocityBody(*roll_rad_s*, *pitch_rad_s*, *yaw_rad_s*)
:   Bases: `object`

    Angular velocity type.

    Parameters:
    :   * **roll_rad_s** (*float*) – Roll angular velocity
        * **pitch_rad_s** (*float*) – Pitch angular velocity
        * **yaw_rad_s** (*float*) – Yaw angular velocity

class mavsdk.telemetry.AngularVelocityFrd(*forward_rad_s*, *right_rad_s*, *down_rad_s*)
:   Bases: `object`

    AngularVelocityFrd message type.

    Parameters:
    :   * **forward_rad_s** (*float*) – Angular velocity in forward direction in radians per second
        * **right_rad_s** (*float*) – Angular velocity in right direction in radians per second
        * **down_rad_s** (*float*) – Angular velocity in Down direction in radians per second

class mavsdk.telemetry.Battery(*id*, *temperature_degc*, *voltage_v*, *current_battery_a*, *capacity_consumed_ah*, *remaining_percent*, *time_remaining_s*, *battery_function*)
:   Bases: `object`

    Battery type.

    Parameters:
    :   * **id** (*uint32_t*) – Battery ID, for systems with multiple batteries
        * **temperature_degc** (*float*) – Temperature of the battery in degrees Celsius. NAN for unknown temperature
        * **voltage_v** (*float*) – Voltage in volts
        * **current_battery_a** (*float*) – Battery current in Amps, NAN if autopilot does not measure the current
        * **capacity_consumed_ah** (*float*) – Consumed charge in Amp hours, NAN if autopilot does not provide consumption estimate
        * **remaining_percent** (*float*) – Estimated battery remaining (range: 0 to 100)
        * **time_remaining_s** (*float*) – Estimated battery usage time remaining
        * **battery_function** ([*BatteryFunction*](#mavsdk.telemetry.BatteryFunction "mavsdk.telemetry.BatteryFunction")) – Function of the battery

class mavsdk.telemetry.BatteryFunction(**values*)
:   Bases: `Enum`

    Battery function type.

    ## Values

    UNKNOWN
    :   Battery function is unknown

    ALL
    :   Battery supports all flight systems

    PROPULSION
    :   Battery for the propulsion system

    AVIONICS
    :   Avionics battery

    PAYLOAD
    :   Payload battery

    ALL = 1

    AVIONICS = 3

    PAYLOAD = 4

    PROPULSION = 2

    UNKNOWN = 0

class mavsdk.telemetry.Covariance(*covariance_matrix*)
:   Bases: `object`

    Covariance type.

    Row-major representation of a 6x6 cross-covariance matrix
    upper right triangle.
    Set first to NaN if unknown.

    Parameters:
    :   **covariance_matrix** (*[**float**]*) – Representation of a covariance matrix.

class mavsdk.telemetry.DistanceSensor(*minimum_distance_m*, *maximum_distance_m*, *current_distance_m*, *orientation*)
:   Bases: `object`

    DistanceSensor message type.

    Parameters:
    :   * **minimum_distance_m** (*float*) – Minimum distance the sensor can measure, NaN if unknown.
        * **maximum_distance_m** (*float*) – Maximum distance the sensor can measure, NaN if unknown.
        * **current_distance_m** (*float*) – Current distance reading, NaN if unknown.
        * **orientation** ([*EulerAngle*](#mavsdk.telemetry.EulerAngle "mavsdk.telemetry.EulerAngle")) – Sensor Orientation reading.

class mavsdk.telemetry.EulerAngle(*roll_deg*, *pitch_deg*, *yaw_deg*, *timestamp_us*)
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

class mavsdk.telemetry.FixType(**values*)
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

class mavsdk.telemetry.FixedwingMetrics(*airspeed_m_s*, *throttle_percentage*, *climb_rate_m_s*, *groundspeed_m_s*, *heading_deg*, *absolute_altitude_m*)
:   Bases: `object`

    FixedwingMetrics message type.

    Parameters:
    :   * **airspeed_m_s** (*float*) – Current indicated airspeed (IAS) in metres per second
        * **throttle_percentage** (*float*) – Current throttle setting (0 to 100)
        * **climb_rate_m_s** (*float*) – Current climb rate in metres per second
        * **groundspeed_m_s** (*float*) – Current groundspeed metres per second
        * **heading_deg** (*float*) – Current heading in compass units (0-360, 0=north)
        * **absolute_altitude_m** (*float*) – Current altitude in metres (MSL)

class mavsdk.telemetry.FlightMode(**values*)
:   Bases: `Enum`

    Flight modes.

    For more information about flight modes, check out
    <https://docs.px4.io/master/en/config/flight_mode.html>.

    ## Values

    UNKNOWN
    :   Mode not known

    READY
    :   Armed and ready to take off

    TAKEOFF
    :   Taking off

    HOLD
    :   Holding (hovering in place (or circling for fixed-wing vehicles)

    MISSION
    :   In mission

    RETURN_TO_LAUNCH
    :   Returning to launch position (then landing)

    LAND
    :   Landing

    OFFBOARD
    :   In ‘offboard’ mode

    FOLLOW_ME
    :   In ‘follow-me’ mode

    MANUAL
    :   In ‘Manual’ mode

    ALTCTL
    :   In ‘Altitude Control’ mode

    POSCTL
    :   In ‘Position Control’ mode

    ACRO
    :   In ‘Acro’ mode

    STABILIZED
    :   In ‘Stabilize’ mode

    RATTITUDE
    :   In ‘Rattitude’ mode

    ACRO = 12

    ALTCTL = 10

    FOLLOW_ME = 8

    HOLD = 3

    LAND = 6

    MANUAL = 9

    MISSION = 4

    OFFBOARD = 7

    POSCTL = 11

    RATTITUDE = 14

    READY = 1

    RETURN_TO_LAUNCH = 5

    STABILIZED = 13

    TAKEOFF = 2

    UNKNOWN = 0

class mavsdk.telemetry.GpsGlobalOrigin(*latitude_deg*, *longitude_deg*, *altitude_m*)
:   Bases: `object`

    Gps global origin type.

    Parameters:
    :   * **latitude_deg** (*double*) – Latitude of the origin
        * **longitude_deg** (*double*) – Longitude of the origin
        * **altitude_m** (*float*) – Altitude AMSL (above mean sea level) in metres

class mavsdk.telemetry.GpsInfo(*num_satellites*, *fix_type*)
:   Bases: `object`

    GPS information type.

    Parameters:
    :   * **num_satellites** (*int32_t*) – Number of visible satellites in use
        * **fix_type** ([*FixType*](#mavsdk.telemetry.FixType "mavsdk.telemetry.FixType")) – Fix type

class mavsdk.telemetry.GroundTruth(*latitude_deg*, *longitude_deg*, *absolute_altitude_m*, *timestamp_us*)
:   Bases: `object`

    GroundTruth message type.

    Parameters:
    :   * **latitude_deg** (*double*) – Latitude in degrees (range: -90 to +90)
        * **longitude_deg** (*double*) – Longitude in degrees (range: -180 to 180)
        * **absolute_altitude_m** (*float*) – Altitude AMSL (above mean sea level) in metres
        * **timestamp_us** (*uint64_t*) – Timestamp in microseconds (since system boot)

class mavsdk.telemetry.Heading(*heading_deg*)
:   Bases: `object`

    Heading type used for global position

    Parameters:
    :   **heading_deg** (*double*) – Heading in degrees (range: 0 to +360)

class mavsdk.telemetry.Health(*is_gyrometer_calibration_ok*, *is_accelerometer_calibration_ok*, *is_magnetometer_calibration_ok*, *is_local_position_ok*, *is_global_position_ok*, *is_home_position_ok*, *is_armable*)
:   Bases: `object`

    Health type.

    Parameters:
    :   * **is_gyrometer_calibration_ok** (*bool*) – True if the gyrometer is calibrated
        * **is_accelerometer_calibration_ok** (*bool*) – True if the accelerometer is calibrated
        * **is_magnetometer_calibration_ok** (*bool*) – True if the magnetometer is calibrated
        * **is_local_position_ok** (*bool*) – True if the local position estimate is good enough to fly in ‘position control’ mode
        * **is_global_position_ok** (*bool*) – True if the global position estimate is good enough to fly in ‘position control’ mode
        * **is_home_position_ok** (*bool*) – True if the home position has been initialized properly
        * **is_armable** (*bool*) – True if system can be armed

class mavsdk.telemetry.Imu(*acceleration_frd*, *angular_velocity_frd*, *magnetic_field_frd*, *temperature_degc*, *timestamp_us*)
:   Bases: `object`

    Imu message type.

    Parameters:
    :   * **acceleration_frd** ([*AccelerationFrd*](#mavsdk.telemetry.AccelerationFrd "mavsdk.telemetry.AccelerationFrd")) – Acceleration
        * **angular_velocity_frd** ([*AngularVelocityFrd*](#mavsdk.telemetry.AngularVelocityFrd "mavsdk.telemetry.AngularVelocityFrd")) – Angular velocity
        * **magnetic_field_frd** ([*MagneticFieldFrd*](#mavsdk.telemetry.MagneticFieldFrd "mavsdk.telemetry.MagneticFieldFrd")) – Magnetic field
        * **temperature_degc** (*float*) – Temperature
        * **timestamp_us** (*uint64_t*) – Timestamp in microseconds

class mavsdk.telemetry.LandedState(**values*)
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

class mavsdk.telemetry.MagneticFieldFrd(*forward_gauss*, *right_gauss*, *down_gauss*)
:   Bases: `object`

    MagneticFieldFrd message type.

    Parameters:
    :   * **forward_gauss** (*float*) – Magnetic field in forward direction measured in Gauss
        * **right_gauss** (*float*) – Magnetic field in East direction measured in Gauss
        * **down_gauss** (*float*) – Magnetic field in Down direction measured in Gauss

class mavsdk.telemetry.Odometry(*time_usec*, *frame_id*, *child_frame_id*, *position_body*, *q*, *velocity_body*, *angular_velocity_body*, *pose_covariance*, *velocity_covariance*)
:   Bases: `object`

    Odometry message type.

    Parameters:
    :   * **time_usec** (*uint64_t*) – Timestamp (0 to use Backend timestamp).
        * **frame_id** ([*MavFrame*](#mavsdk.telemetry.Odometry.MavFrame "mavsdk.telemetry.Odometry.MavFrame")) – Coordinate frame of reference for the pose data.
        * **child_frame_id** ([*MavFrame*](#mavsdk.telemetry.Odometry.MavFrame "mavsdk.telemetry.Odometry.MavFrame")) – Coordinate frame of reference for the velocity in free space (twist) data.
        * **position_body** ([*PositionBody*](#mavsdk.telemetry.PositionBody "mavsdk.telemetry.PositionBody")) – Position.
        * **q** ([*Quaternion*](#mavsdk.telemetry.Quaternion "mavsdk.telemetry.Quaternion")) – Quaternion components, w, x, y, z (1 0 0 0 is the null-rotation).
        * **velocity_body** ([*VelocityBody*](#mavsdk.telemetry.VelocityBody "mavsdk.telemetry.VelocityBody")) – Linear velocity (m/s).
        * **angular_velocity_body** ([*AngularVelocityBody*](#mavsdk.telemetry.AngularVelocityBody "mavsdk.telemetry.AngularVelocityBody")) – Angular velocity (rad/s).
        * **pose_covariance** ([*Covariance*](#mavsdk.telemetry.Covariance "mavsdk.telemetry.Covariance")) – Pose cross-covariance matrix.
        * **velocity_covariance** ([*Covariance*](#mavsdk.telemetry.Covariance "mavsdk.telemetry.Covariance")) – Velocity cross-covariance matrix.

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

class mavsdk.telemetry.Position(*latitude_deg*, *longitude_deg*, *absolute_altitude_m*, *relative_altitude_m*)
:   Bases: `object`

    Position type in global coordinates.

    Parameters:
    :   * **latitude_deg** (*double*) – Latitude in degrees (range: -90 to +90)
        * **longitude_deg** (*double*) – Longitude in degrees (range: -180 to +180)
        * **absolute_altitude_m** (*float*) – Altitude AMSL (above mean sea level) in metres
        * **relative_altitude_m** (*float*) – Altitude relative to takeoff altitude in metres

class mavsdk.telemetry.PositionBody(*x_m*, *y_m*, *z_m*)
:   Bases: `object`

    Position type, represented in the Body (X Y Z) frame

    Parameters:
    :   * **x_m** (*float*) – X Position in metres.
        * **y_m** (*float*) – Y Position in metres.
        * **z_m** (*float*) – Z Position in metres.

class mavsdk.telemetry.PositionNed(*north_m*, *east_m*, *down_m*)
:   Bases: `object`

    PositionNed message type.

    Parameters:
    :   * **north_m** (*float*) – Position along north direction in metres
        * **east_m** (*float*) – Position along east direction in metres
        * **down_m** (*float*) – Position along down direction in metres

class mavsdk.telemetry.PositionVelocityNed(*position*, *velocity*)
:   Bases: `object`

    PositionVelocityNed message type.

    Parameters:
    :   * **position** ([*PositionNed*](#mavsdk.telemetry.PositionNed "mavsdk.telemetry.PositionNed")) – Position (NED)
        * **velocity** ([*VelocityNed*](#mavsdk.telemetry.VelocityNed "mavsdk.telemetry.VelocityNed")) – Velocity (NED)

class mavsdk.telemetry.Quaternion(*w*, *x*, *y*, *z*, *timestamp_us*)
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

class mavsdk.telemetry.RawGps(*timestamp_us*, *latitude_deg*, *longitude_deg*, *absolute_altitude_m*, *hdop*, *vdop*, *velocity_m_s*, *cog_deg*, *altitude_ellipsoid_m*, *horizontal_uncertainty_m*, *vertical_uncertainty_m*, *velocity_uncertainty_m_s*, *heading_uncertainty_deg*, *yaw_deg*)
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

class mavsdk.telemetry.RcStatus(*was_available_once*, *is_available*, *signal_strength_percent*)
:   Bases: `object`

    Remote control status type.

    Parameters:
    :   * **was_available_once** (*bool*) – True if an RC signal has been available once
        * **is_available** (*bool*) – True if the RC signal is available now
        * **signal_strength_percent** (*float*) – Signal strength (range: 0 to 100, NaN if unknown)

class mavsdk.telemetry.ScaledPressure(*timestamp_us*, *absolute_pressure_hpa*, *differential_pressure_hpa*, *temperature_deg*, *differential_pressure_temperature_deg*)
:   Bases: `object`

    Scaled Pressure message type.

    Parameters:
    :   * **timestamp_us** (*uint64_t*) – Timestamp (time since system boot)
        * **absolute_pressure_hpa** (*float*) – Absolute pressure in hPa
        * **differential_pressure_hpa** (*float*) – Differential pressure 1 in hPa
        * **temperature_deg** (*float*) – Absolute pressure temperature (in celsius)
        * **differential_pressure_temperature_deg** (*float*) – Differential pressure temperature (in celsius, 0 if not available)

class mavsdk.telemetry.StatusText(*type*, *text*)
:   Bases: `object`

    StatusText information type.

    Parameters:
    :   * **type** ([*StatusTextType*](#mavsdk.telemetry.StatusTextType "mavsdk.telemetry.StatusTextType")) – Message type
        * **text** (*std::string*) – MAVLink status message

class mavsdk.telemetry.StatusTextType(**values*)
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

class mavsdk.telemetry.Telemetry(*async_plugin_manager*)
:   Bases: `AsyncBase`

    Allow users to get vehicle telemetry and state information
    (e.g. battery, GPS, RC connection, flight mode etc.) and set telemetry update rates.
    Certain Telemetry Topics such as, Position or Velocity_Ned require GPS Fix before data gets published.

    Generated by dcsdkgen - MAVSDK Telemetry API

    async actuator_control_target()
    :   Subscribe to ‘actuator control target’ updates.

        Yields:
        :   **actuator_control_target** (*ActuatorControlTarget*) – The next actuator control target

    async actuator_output_status()
    :   Subscribe to ‘actuator output status’ updates.

        Yields:
        :   **actuator_output_status** (*ActuatorOutputStatus*) – The next actuator output status

    async altitude()
    :   Subscribe to ‘Altitude’ updates.

        Yields:
        :   **altitude** (*Altitude*) – The next altitude

    async armed()
    :   Subscribe to armed updates.

        Yields:
        :   **is_armed** (*bool*) – The next ‘armed’ state

    async attitude_angular_velocity_body()
    :   Subscribe to ‘attitude’ updates (angular velocity)

        Yields:
        :   **attitude_angular_velocity_body** (*AngularVelocityBody*) – The next angular velocity (rad/s)

    async attitude_euler()
    :   Subscribe to ‘attitude’ updates (Euler).

        Yields:
        :   **attitude_euler** (*EulerAngle*) – The next attitude (Euler)

    async attitude_quaternion()
    :   Subscribe to ‘attitude’ updates (quaternion).

        Yields:
        :   **attitude_quaternion** (*Quaternion*) – The next attitude (quaternion)

    async battery()
    :   Subscribe to ‘battery’ updates.

        Yields:
        :   **battery** (*Battery*) – The next ‘battery’ state

    async distance_sensor()
    :   Subscribe to ‘Distance Sensor’ updates.

        Yields:
        :   **distance_sensor** (*DistanceSensor*) – The next Distance Sensor status

    async fixedwing_metrics()
    :   Subscribe to ‘fixedwing metrics’ updates.

        Yields:
        :   **fixedwing_metrics** (*FixedwingMetrics*) – The next fixedwing metrics

    async flight_mode()
    :   Subscribe to ‘flight mode’ updates.

        Yields:
        :   **flight_mode** (*FlightMode*) – The next flight mode

    async get_gps_global_origin()
    :   Get the GPS location of where the estimator has been initialized.

        Returns:
        :   **gps_global_origin**

        Return type:
        :   [GpsGlobalOrigin](#mavsdk.telemetry.GpsGlobalOrigin "mavsdk.telemetry.GpsGlobalOrigin")

        Raises:
        :   [**TelemetryError**](#mavsdk.telemetry.TelemetryError "mavsdk.telemetry.TelemetryError") – If the request fails. The error contains the reason for the failure.

    async gps_info()
    :   Subscribe to ‘GPS info’ updates.

        Yields:
        :   **gps_info** (*GpsInfo*) – The next ‘GPS info’ state

    async ground_truth()
    :   Subscribe to ‘ground truth’ updates.

        Yields:
        :   **ground_truth** (*GroundTruth*) – Ground truth position information available in simulation

    async heading()
    :   Subscribe to ‘Heading’ updates.

        Yields:
        :   **heading_deg** (*Heading*) – The next heading (yaw) in degrees

    async health()
    :   Subscribe to ‘health’ updates.

        Yields:
        :   **health** (*Health*) – The next ‘health’ state

    async health_all_ok()
    :   Subscribe to ‘HealthAllOk’ updates.

        Yields:
        :   **is_health_all_ok** (*bool*) – The next ‘health all ok’ status

    async home()
    :   Subscribe to ‘home position’ updates.

        Yields:
        :   **home** (*Position*) – The next home position

    async imu()
    :   Subscribe to ‘IMU’ updates (in SI units in NED body frame).

        Yields:
        :   **imu** (*Imu*) – The next IMU status

    async in_air()
    :   Subscribe to in-air updates.

        Yields:
        :   **is_in_air** (*bool*) – The next ‘in-air’ state

    async landed_state()
    :   Subscribe to landed state updates

        Yields:
        :   **landed_state** (*LandedState*) – The next ‘landed’ state

    name = 'Telemetry'

    async odometry()
    :   Subscribe to ‘odometry’ updates.

        Yields:
        :   **odometry** (*Odometry*) – The next odometry status

    async position()
    :   Subscribe to ‘position’ updates.

        Yields:
        :   **position** (*Position*) – The next position

    async position_velocity_ned()
    :   Subscribe to ‘position velocity’ updates.

        Yields:
        :   **position_velocity_ned** (*PositionVelocityNed*) – The next position and velocity status

    async raw_gps()
    :   Subscribe to ‘Raw GPS’ updates.

        Yields:
        :   **raw_gps** (*RawGps*) – The next ‘Raw GPS’ state. Warning: this is an advanced feature, use Position updates to get the location of the drone!

    async raw_imu()
    :   Subscribe to ‘Raw IMU’ updates (note that units are are incorrect and “raw” as provided by the sensor)

        Yields:
        :   **imu** (*Imu*) – The next raw IMU status

    async rc_status()
    :   Subscribe to ‘RC status’ updates.

        Yields:
        :   **rc_status** (*RcStatus*) – The next RC status

    async scaled_imu()
    :   Subscribe to ‘Scaled IMU’ updates.

        Yields:
        :   **imu** (*Imu*) – The next scaled IMU status

    async scaled_pressure()
    :   Subscribe to ‘Scaled Pressure’ updates.

        Yields:
        :   **scaled_pressure** (*ScaledPressure*) – The next Scaled Pressure status

    async set_rate_actuator_control_target(*rate_hz*)
    :   Set rate to ‘actuator control target’ updates.

        Parameters:
        :   **rate_hz** (*double*) – The requested rate (in Hertz)

        Raises:
        :   [**TelemetryError**](#mavsdk.telemetry.TelemetryError "mavsdk.telemetry.TelemetryError") – If the request fails. The error contains the reason for the failure.

    async set_rate_actuator_output_status(*rate_hz*)
    :   Set rate to ‘actuator output status’ updates.

        Parameters:
        :   **rate_hz** (*double*) – The requested rate (in Hertz)

        Raises:
        :   [**TelemetryError**](#mavsdk.telemetry.TelemetryError "mavsdk.telemetry.TelemetryError") – If the request fails. The error contains the reason for the failure.

    async set_rate_altitude(*rate_hz*)
    :   Set rate to ‘Altitude’ updates.

        Parameters:
        :   **rate_hz** (*double*) – The requested rate (in Hertz)

        Raises:
        :   [**TelemetryError**](#mavsdk.telemetry.TelemetryError "mavsdk.telemetry.TelemetryError") – If the request fails. The error contains the reason for the failure.

    async set_rate_attitude_euler(*rate_hz*)
    :   Set rate to ‘attitude quaternion’ updates.

        Parameters:
        :   **rate_hz** (*double*) – The requested rate (in Hertz)

        Raises:
        :   [**TelemetryError**](#mavsdk.telemetry.TelemetryError "mavsdk.telemetry.TelemetryError") – If the request fails. The error contains the reason for the failure.

    async set_rate_attitude_quaternion(*rate_hz*)
    :   Set rate to ‘attitude euler angle’ updates.

        Parameters:
        :   **rate_hz** (*double*) – The requested rate (in Hertz)

        Raises:
        :   [**TelemetryError**](#mavsdk.telemetry.TelemetryError "mavsdk.telemetry.TelemetryError") – If the request fails. The error contains the reason for the failure.

    async set_rate_battery(*rate_hz*)
    :   Set rate to ‘battery’ updates.

        Parameters:
        :   **rate_hz** (*double*) – The requested rate (in Hertz)

        Raises:
        :   [**TelemetryError**](#mavsdk.telemetry.TelemetryError "mavsdk.telemetry.TelemetryError") – If the request fails. The error contains the reason for the failure.

    async set_rate_distance_sensor(*rate_hz*)
    :   Set rate to ‘Distance Sensor’ updates.

        Parameters:
        :   **rate_hz** (*double*) – The requested rate (in Hertz)

        Raises:
        :   [**TelemetryError**](#mavsdk.telemetry.TelemetryError "mavsdk.telemetry.TelemetryError") – If the request fails. The error contains the reason for the failure.

    async set_rate_fixedwing_metrics(*rate_hz*)
    :   Set rate to ‘fixedwing metrics’ updates.

        Parameters:
        :   **rate_hz** (*double*) – The requested rate (in Hertz)

        Raises:
        :   [**TelemetryError**](#mavsdk.telemetry.TelemetryError "mavsdk.telemetry.TelemetryError") – If the request fails. The error contains the reason for the failure.

    async set_rate_gps_info(*rate_hz*)
    :   Set rate to ‘GPS info’ updates.

        Parameters:
        :   **rate_hz** (*double*) – The requested rate (in Hertz)

        Raises:
        :   [**TelemetryError**](#mavsdk.telemetry.TelemetryError "mavsdk.telemetry.TelemetryError") – If the request fails. The error contains the reason for the failure.

    async set_rate_ground_truth(*rate_hz*)
    :   Set rate to ‘ground truth’ updates.

        Parameters:
        :   **rate_hz** (*double*) – The requested rate (in Hertz)

        Raises:
        :   [**TelemetryError**](#mavsdk.telemetry.TelemetryError "mavsdk.telemetry.TelemetryError") – If the request fails. The error contains the reason for the failure.

    async set_rate_health(*rate_hz*)
    :   Set rate to ‘Health’ updates.

        Parameters:
        :   **rate_hz** (*double*) – The requested rate (in Hertz)

        Raises:
        :   [**TelemetryError**](#mavsdk.telemetry.TelemetryError "mavsdk.telemetry.TelemetryError") – If the request fails. The error contains the reason for the failure.

    async set_rate_home(*rate_hz*)
    :   Set rate to ‘home position’ updates.

        Parameters:
        :   **rate_hz** (*double*) – The requested rate (in Hertz)

        Raises:
        :   [**TelemetryError**](#mavsdk.telemetry.TelemetryError "mavsdk.telemetry.TelemetryError") – If the request fails. The error contains the reason for the failure.

    async set_rate_imu(*rate_hz*)
    :   Set rate to ‘IMU’ updates.

        Parameters:
        :   **rate_hz** (*double*) – The requested rate (in Hertz)

        Raises:
        :   [**TelemetryError**](#mavsdk.telemetry.TelemetryError "mavsdk.telemetry.TelemetryError") – If the request fails. The error contains the reason for the failure.

    async set_rate_in_air(*rate_hz*)
    :   Set rate to in-air updates.

        Parameters:
        :   **rate_hz** (*double*) – The requested rate (in Hertz)

        Raises:
        :   [**TelemetryError**](#mavsdk.telemetry.TelemetryError "mavsdk.telemetry.TelemetryError") – If the request fails. The error contains the reason for the failure.

    async set_rate_landed_state(*rate_hz*)
    :   Set rate to landed state updates

        Parameters:
        :   **rate_hz** (*double*) – The requested rate (in Hertz)

        Raises:
        :   [**TelemetryError**](#mavsdk.telemetry.TelemetryError "mavsdk.telemetry.TelemetryError") – If the request fails. The error contains the reason for the failure.

    async set_rate_odometry(*rate_hz*)
    :   Set rate to ‘odometry’ updates.

        Parameters:
        :   **rate_hz** (*double*) – The requested rate (in Hertz)

        Raises:
        :   [**TelemetryError**](#mavsdk.telemetry.TelemetryError "mavsdk.telemetry.TelemetryError") – If the request fails. The error contains the reason for the failure.

    async set_rate_position(*rate_hz*)
    :   Set rate to ‘position’ updates.

        Parameters:
        :   **rate_hz** (*double*) – The requested rate (in Hertz)

        Raises:
        :   [**TelemetryError**](#mavsdk.telemetry.TelemetryError "mavsdk.telemetry.TelemetryError") – If the request fails. The error contains the reason for the failure.

    async set_rate_position_velocity_ned(*rate_hz*)
    :   Set rate to ‘position velocity’ updates.

        Parameters:
        :   **rate_hz** (*double*) – The requested rate (in Hertz)

        Raises:
        :   [**TelemetryError**](#mavsdk.telemetry.TelemetryError "mavsdk.telemetry.TelemetryError") – If the request fails. The error contains the reason for the failure.

    async set_rate_raw_gps(*rate_hz*)
    :   Set rate to ‘Raw GPS’ updates.

        Parameters:
        :   **rate_hz** (*double*) – The requested rate (in Hertz)

        Raises:
        :   [**TelemetryError**](#mavsdk.telemetry.TelemetryError "mavsdk.telemetry.TelemetryError") – If the request fails. The error contains the reason for the failure.

    async set_rate_raw_imu(*rate_hz*)
    :   Set rate to ‘Raw IMU’ updates.

        Parameters:
        :   **rate_hz** (*double*) – The requested rate (in Hertz)

        Raises:
        :   [**TelemetryError**](#mavsdk.telemetry.TelemetryError "mavsdk.telemetry.TelemetryError") – If the request fails. The error contains the reason for the failure.

    async set_rate_rc_status(*rate_hz*)
    :   Set rate to ‘RC status’ updates.

        Parameters:
        :   **rate_hz** (*double*) – The requested rate (in Hertz)

        Raises:
        :   [**TelemetryError**](#mavsdk.telemetry.TelemetryError "mavsdk.telemetry.TelemetryError") – If the request fails. The error contains the reason for the failure.

    async set_rate_scaled_imu(*rate_hz*)
    :   Set rate to ‘Scaled IMU’ updates.

        Parameters:
        :   **rate_hz** (*double*) – The requested rate (in Hertz)

        Raises:
        :   [**TelemetryError**](#mavsdk.telemetry.TelemetryError "mavsdk.telemetry.TelemetryError") – If the request fails. The error contains the reason for the failure.

    async set_rate_unix_epoch_time(*rate_hz*)
    :   Set rate to ‘unix epoch time’ updates.

        Parameters:
        :   **rate_hz** (*double*) – The requested rate (in Hertz)

        Raises:
        :   [**TelemetryError**](#mavsdk.telemetry.TelemetryError "mavsdk.telemetry.TelemetryError") – If the request fails. The error contains the reason for the failure.

    async set_rate_velocity_ned(*rate_hz*)
    :   Set rate of camera attitude updates.
        Set rate to ‘ground speed’ updates (NED).

        Parameters:
        :   **rate_hz** (*double*) – The requested rate (in Hertz)

        Raises:
        :   [**TelemetryError**](#mavsdk.telemetry.TelemetryError "mavsdk.telemetry.TelemetryError") – If the request fails. The error contains the reason for the failure.

    async set_rate_vtol_state(*rate_hz*)
    :   Set rate to VTOL state updates

        Parameters:
        :   **rate_hz** (*double*) – The requested rate (in Hertz)

        Raises:
        :   [**TelemetryError**](#mavsdk.telemetry.TelemetryError "mavsdk.telemetry.TelemetryError") – If the request fails. The error contains the reason for the failure.

    async status_text()
    :   Subscribe to ‘status text’ updates.

        Yields:
        :   **status_text** (*StatusText*) – The next ‘status text’

    async unix_epoch_time()
    :   Subscribe to ‘unix epoch time’ updates.

        Yields:
        :   **time_us** (*uint64_t*) – The next ‘unix epoch time’ status

    async velocity_ned()
    :   Subscribe to ‘ground speed’ updates (NED).

        Yields:
        :   **velocity_ned** (*VelocityNed*) – The next velocity (NED)

    async vtol_state()
    :   subscribe to vtol state Updates

        Yields:
        :   **vtol_state** (*VtolState*) – The next ‘vtol’ state

    async wind()
    :   Subscribe to ‘Wind Estimated’ updates.

        Yields:
        :   **wind** (*Wind*) – The next wind

exception mavsdk.telemetry.TelemetryError(*result*, *origin*, **params*)
:   Bases: `Exception`

    Raised when a TelemetryResult is a fail code

class mavsdk.telemetry.TelemetryResult(*result*, *result_str*)
:   Bases: `object`

    Result type.

    Parameters:
    :   * **result** ([*Result*](#mavsdk.telemetry.TelemetryResult.Result "mavsdk.telemetry.TelemetryResult.Result")) – Result enum value
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

class mavsdk.telemetry.VelocityBody(*x_m_s*, *y_m_s*, *z_m_s*)
:   Bases: `object`

    Velocity type, represented in the Body (X Y Z) frame and in metres/second.

    Parameters:
    :   * **x_m_s** (*float*) – Velocity in X in metres/second
        * **y_m_s** (*float*) – Velocity in Y in metres/second
        * **z_m_s** (*float*) – Velocity in Z in metres/second

class mavsdk.telemetry.VelocityNed(*north_m_s*, *east_m_s*, *down_m_s*)
:   Bases: `object`

    VelocityNed message type.

    Parameters:
    :   * **north_m_s** (*float*) – Velocity along north direction in metres per second
        * **east_m_s** (*float*) – Velocity along east direction in metres per second
        * **down_m_s** (*float*) – Velocity along down direction in metres per second

class mavsdk.telemetry.VtolState(**values*)
:   Bases: `Enum`

    VTOL State enumeration

    ## Values

    UNDEFINED
    :   MAV is not configured as VTOL

    TRANSITION_TO_FW
    :   VTOL is in transition from multicopter to fixed-wing

    TRANSITION_TO_MC
    :   VTOL is in transition from fixed-wing to multicopter

    MC
    :   VTOL is in multicopter state

    FW
    :   VTOL is in fixed-wing state

    FW = 4

    MC = 3

    TRANSITION_TO_FW = 1

    TRANSITION_TO_MC = 2

    UNDEFINED = 0

class mavsdk.telemetry.Wind(*wind_x_ned_m_s*, *wind_y_ned_m_s*, *wind_z_ned_m_s*, *horizontal_variability_stddev_m_s*, *vertical_variability_stddev_m_s*, *wind_altitude_msl_m*, *horizontal_wind_speed_accuracy_m_s*, *vertical_wind_speed_accuracy_m_s*)
:   Bases: `object`

    Wind message type

    Parameters:
    :   * **wind_x_ned_m_s** (*float*) – Wind in North (NED) direction
        * **wind_y_ned_m_s** (*float*) – Wind in East (NED) direction
        * **wind_z_ned_m_s** (*float*) – Wind in down (NED) direction
        * **horizontal_variability_stddev_m_s** (*float*) – Variability of wind in XY, 1-STD estimated from a 1 Hz lowpassed wind estimate
        * **vertical_variability_stddev_m_s** (*float*) – Variability of wind in Z, 1-STD estimated from a 1 Hz lowpassed wind estimate
        * **wind_altitude_msl_m** (*float*) – Altitude (MSL) that this measurement was taken at
        * **horizontal_wind_speed_accuracy_m_s** (*float*) – Horizontal speed 1-STD accuracy
        * **vertical_wind_speed_accuracy_m_s** (*float*) – Vertical speed 1-STD accuracy
