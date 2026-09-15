---
title: "Integration Testing for the PX4 ROS 2 Interface Library"
type: document
doc_set: PX4
doc_version: main
section: test_and_ci
source_url: "https://docs.px4.io/main/en/test_and_ci/integration_testing_px4_ros2_interface"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "test_and_ci/integration_testing_px4_ros2_interface.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/test-and-ci
---

# Integration Testing for the PX4 ROS 2 Interface Library

This topic outlines the integration tests for the [PX4 ROS 2 Interface Library](../ros2/px4_ros2_interface_lib.md).

These test that mode registration, failsafes, and mode replacement, work as expected.

## CI Testing

When opening a pull request to PX4, CI runs the library integration tests.

## Running Tests Locally

The tests can also be run locally from PX4:

```sh
./test/ros_test_runner.py
```

And to run only a single case:

```sh
./test/ros_test_runner.py --verbose --case <case>
```

You can list the available test cases with:

```sh
./test/ros_test_runner.py --list-cases
```
