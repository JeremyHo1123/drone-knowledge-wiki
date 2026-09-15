---
title: "Sanitizers"
type: document
doc_set: PX4
doc_version: main
section: test_and_ci
source_url: "https://docs.px4.io/main/en/test_and_ci/sanitizers"
upstream_repo: "PX4/PX4-Autopilot"
upstream_path: "test_and_ci/sanitizers.md"
upstream_commit: "9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55"
ingested: 2026-07-28
tags:
  - docs/px4
  - docs/px4/test-and-ci
---

# Sanitizers

[Sanitizers](https://github.com/google/sanitizers) are compiler-instrumentation tools that detect whole classes of bugs at runtime. PX4 can build [SITL](../simulation/index.md) with them to catch problems that are otherwise hard to reproduce:

- **AddressSanitizer (ASan)** — out-of-bounds accesses, use-after-free, memory leaks.
- **ThreadSanitizer (TSan)** — data races and lock-order inversions.
- **MemorySanitizer (MSan)** — reads of uninitialized memory (Clang only).
- **UndefinedBehaviorSanitizer (UBSan)** — undefined behaviour (signed overflow, misaligned access, …).

:::info
Sanitizers are only available for POSIX/SITL builds, where the host compiler instruments the code. They are not used on the NuttX flight-controller targets.
:::

## Building and running

Set the matching environment variable when building SITL. It selects the corresponding `CMAKE_BUILD_TYPE`:

| Variable    | Sanitizer                  |
| ----------- | -------------------------- |
| `PX4_ASAN`  | AddressSanitizer           |
| `PX4_TSAN`  | ThreadSanitizer            |
| `PX4_MSAN`  | MemorySanitizer            |
| `PX4_UBSAN` | UndefinedBehaviorSanitizer |

For example, to build and run SITL under ThreadSanitizer:

```sh
PX4_TSAN=1 make px4_sitl_default
```

To build and run the unit and integration test suite under a sanitizer:

```sh
PX4_TSAN=1 make tests
```

:::warning
A sanitizer is a distinct `CMAKE_BUILD_TYPE`, so switching to or from one rebuilds from scratch. Sanitized binaries are larger and run several times slower (ASan/TSan roughly 2–5×), and lockstep timing changes, so expect tests to take longer.
:::

## Linux: ASLR fix

On recent Linux kernels the default address-space-layout randomization entropy is too high for the sanitizer runtimes' shadow-memory mapping, and the process aborts at startup with e.g.:

```
FATAL: ThreadSanitizer: unexpected memory mapping 0x... - 0x...
```

Lower the mmap randomization (needed for both ASan and TSan), once per boot:

```sh
sudo sysctl vm.mmap_rnd_bits=28
```

To make it persistent across reboots:

```sh
echo 'vm.mmap_rnd_bits=28' | sudo tee /etc/sysctl.d/99-sanitizers.conf
```

If `28` still fails on your kernel, try `26`.

## ThreadSanitizer suppressions

Running SITL with the Gazebo bridge under TSan reports many data races inside the third-party simulation transport (ZeroMQ and gz-transport) and the PX4↔Gazebo bridge glue. None of this is in the flight code path or the SIH-based CI, and it can't be fixed here, so it is filtered with a suppressions file at `test/sitl_tsan.supp`:

```sh
TSAN_OPTIONS="suppressions=$PWD/test/sitl_tsan.supp" PX4_TSAN=1 make px4_sitl_default gz_x500
```

:::warning
Only add third-party / simulation symbols to the suppressions file — never flight-code symbols. A race detector is only useful at zero reports; suppressing your own code blinds it to real bugs.
:::
