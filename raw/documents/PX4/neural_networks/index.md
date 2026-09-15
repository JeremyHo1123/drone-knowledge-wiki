---
title: "Neural Network Control"
type: document
doc_set: PX4
doc_version: main
section: neural_networks
source_url: "https://docs.px4.io/main/en/neural_networks/"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "neural_networks/index.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/neural-networks
---

# Neural Network Control

PX4 supports the following mechanisms for using neural networks for multirotor control:

- [MC Neural Networks Control](../neural_networks/mc_neural_network_control.md)<Badge type="warning" text="Experimental" /> — A generic neural network module that you can modify to use different underlying neural network and training models and compile into the firmware.
- [RAPTOR: A Neural Network Module for Adaptive Quadrotor Control](../neural_networks/raptor.md)<Badge type="warning" text="Experimental" /> — An adaptive RL NN module that works well with different Quad configurations without additional training.

Generally you will select the former if you wish to experiment with custom neural network architectures and train them using PyTorch or TensorFlow, and the latter if you want to use a pre-trained neural-network controller that works out-of-the-box (without training for your particular platform) or if you train your own policies using [RLtools](https://rl.tools).

Note that both modules are experimental and provided for experimentation.
The table below provides more detail on the differences.

| Use Case                                                         | [`mc_raptor`](../neural_networks/raptor.md) | [`mc_nn_control`](../neural_networks/mc_neural_network_control.md) |
| ---------------------------------------------------------------- | ------------------------------------------- | ------------------------------------------------------------------ |
| Pre-trained policy that adapts to any quadrotor without training | ✓ RAPTOR                                    | ✘                                                                  |
| Train policy in PyTorch/TF                                       | ✘                                           | ✓ TF Lite                                                          |
| Train policy in RLtools                                          | ✓                                           | ✘                                                                  |
| Use manual control (remote) with NN policy                       | ✘ GPS/MoCap                                 | ✓ Manual attitude commands                                         |
| Load policy checkpoints from SD card                             | ✓ Upload via MAVLink FTP                    | ✘ Compiled into firmware                                           |
| Offboard setpoints                                               | ✓ MAVLink                                   | ✘                                                                  |
| Internal Trajectory Generator                                    | ✓ (Position, Lissajous)                     | ✘                                                                  |
