---
title: "Platform Testing and Continuous Integration"
type: document
doc_set: PX4
doc_version: main
section: test_and_ci
source_url: "https://docs.px4.io/main/en/test_and_ci/"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "test_and_ci/index.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/test-and-ci
---

# Platform Testing and Continuous Integration

PX4 is extensively tested using unit and integration tests run via continuous integration.
Live flight testing is also performed by the development team and the broader community.

Test topics include:

- [Test Flights](../test_and_ci/test_flights.md) - How to make test flights (e.g. to [test PRs](../contribute/code.md#pull-requests))
- [Hardware Bench Testing (px4bench)](../test_and_ci/bench_testing.md) - Automated verification on real flight-controller hardware: release qualification, hardware-in-the-loop flight testing, and production end-of-line checks
- [Unit Tests](../test_and_ci/unit_tests.md)
- [Sanitizers](../test_and_ci/sanitizers.md) - Build SITL with ASan/TSan to catch memory errors and data races
- [Continuous Integration (CI)](../test_and_ci/continous_integration.md)
- [Integration Testing](../test_and_ci/integration_testing.md)
  - [MAVSDK Integration Testing](../test_and_ci/integration_testing_mavsdk.md)
  - [PX4 ROS2 Interface Library Integration Testing](../test_and_ci/integration_testing_px4_ros2_interface.md)
- [Docker](../test_and_ci/docker.md)
- [Maintenance](../test_and_ci/maintenance.md)
