---
title: "NeuralControl (UORB message)"
type: document
doc_set: PX4
doc_version: main
section: msg_docs
source_url: "https://docs.px4.io/main/en/msg_docs/NeuralControl"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "msg_docs/NeuralControl.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/msg-docs
pageClass: is-wide-page
---

# NeuralControl (UORB message)

Neural control.

Debugging topic for the Neural controller, logs the inputs and output vectors of the neural network, and the time it takes to run
Publisher: mc_nn_control
Subscriber: logger

**TOPICS:** neural_control

## Fields

| Name                                            | Type          | Unit [Frame] | Range/Enum | Description                                                            |
| ----------------------------------------------- | ------------- | ------------ | ---------- | ---------------------------------------------------------------------- |
| <a id="fld_timestamp"></a>timestamp             | `uint64`      | us           |            | Time since system start                                                |
| <a id="fld_observation"></a>observation         | `float32[15]` |              |            | Observation vector (pos error (3), att (6d), lin vel (3), ang vel (3)) |
| <a id="fld_network_output"></a>network_output   | `float32[4]`  |              |            | Output from neural network                                             |
| <a id="fld_controller_time"></a>controller_time | `int32`       | us           |            | Time spent from input to output                                        |
| <a id="fld_inference_time"></a>inference_time   | `int32`       | us           |            | Time spent for NN inference                                            |

## Source Message

[Source file (GitHub)](https://github.com/PX4/PX4-Autopilot/blob/main/msg/NeuralControl.msg)

::: details Click here to see original file

```c
# Neural control
#
# Debugging topic for the Neural controller, logs the inputs and output vectors of the neural network, and the time it takes to run
# Publisher: mc_nn_control
# Subscriber: logger

uint64 timestamp # [us] Time since system start

float32[15] observation # Observation vector (pos error (3), att (6d), lin vel (3), ang vel (3))
float32[4] network_output # Output from neural network

int32 controller_time # [us] Time spent from input to output
int32 inference_time # [us] Time spent for NN inference
```

:::
