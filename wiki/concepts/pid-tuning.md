---
title: PX4 Tuning (PID and Autotune)
type: concept
sources:
  - "[[raw/documents/PX4/config_mc/pid_tuning_guide_multicopter]]"
  - "[[raw/documents/PX4/config/autotune_mc]]"
  - "[[raw/documents/PX4/config_fw/pid_tuning_guide_fixedwing]]"
  - "[[raw/documents/QGC/setup_view/tuning_px4]]"
created: 2026-07-28
updated: 2026-09-15
tags:
  - uav/flight-control
  - stack/px4
  - stack/qgc
status: active
doc_version_checked:
  - "PX4 main@9467506"
  - "QGC Stable_V5.0@cb6ee48"
---

# PX4 Tuning (PID and Autotune)

What you tune are the gains in the cascaded architecture described in [[wiki/topics/px4-flight-stack]]. **The order of preference is clear: autotune first, manual tuning only if that is not enough.**

## Try autotune first

Autotune tunes the **rate and attitude controllers** automatically — the docs call these "the most important controllers for stable and responsive flight; other tuning is more optional". Tune once, unless the vehicle has been modified.

**But it runs in flight**, and the docs attach a warning:

- The vehicle must already fly well enough to tolerate moderate disturbances
- **Stay close, watch the whole time, and be ready to abort** — switching flight modes aborts it (fixed-wing aircraft can also use a dedicated autotune switch)
- Verify flight quality after tuning

Autotune only covers the region **around the hover thrust point**. Tune manually if you see non-linearities or oscillations at high thrust, want to understand what airmode does, or want a deeper grasp of basic tuning principles.

## Iron rules of manual tuning

The general rules from the docs — each one learned the hard way:

- **Default gains are deliberately low for safety. Without raising them you will not get a good control response** — don't assume the defaults should fly well
- **Always raise gains very slowly**; large gains cause dangerous oscillation. Typically 20–30 % per step, then 5–10 % for the final adjustments
- **Land before changing parameters.** Then increase throttle slowly and watch for oscillation
- Tune around the hover thrust point, and use the thrust curve parameter to handle thrust non-linearity
- You can temporarily enable high-rate logging (`SDLOG_PROFILE`) to assess rate and attitude tracking from logs; turn it off afterwards
- **Always disable `MC_AIRMODE` while tuning** (official warning)

## Inside out

### 1. Rate controller (innermost, most important)

Three independent PIDs control the body rates (roll / pitch / yaw).

> How well it is tuned affects **all** flight modes. A poorly tuned rate controller shows up in Position mode as "twitches" or oscillation — the vehicle cannot hover perfectly still.

In a single "mixed" implementation, PX4 supports two **mathematically equivalent** PID forms: **Parallel** and **Standard**. Select one by setting the proportional gain of the other form to 1 (set **K**=1 for parallel, **P**=1 for standard).

### 2. Attitude controller (next layer out, much easier)

Only three parameters: `MC_ROLL_P`, `MC_PITCH_P`, `MC_YAW_P`.

> The attitude controller is much easier to tune. In fact, most of the time the defaults do not need to be changed at all.

If you do tune it, fly in **Stabilized mode** and raise the P gain step by step; oscillation or overshoot means it is too high. The maximum rate per axis can also be set: `MC_ROLLRATE_MAX`, `MC_PITCHRATE_MAX`, `MC_YAWRATE_MAX`.

## Airmode and mixer saturation (worth understanding on its own)

The rate controller outputs torque for three axes plus a scalar thrust, and mixing turns them into individual motor thrusts (see [[wiki/concepts/control-allocation]]). **With low thrust and a large torque command, some motor's command comes out negative** (or above 100 %) — this is mixer saturation, and it is physically impossible to execute.

PX4 offers two solutions:

| | Airmode off | Airmode on |
| --- | --- | --- |
| Approach | **Reduce** the torque commands until no motor command is negative | **Increase** overall thrust until no motor command is negative |
| Cost | No attitude correction at all at zero thrust — **so this mode always needs a minimum thrust** | Total thrust goes up |
| Benefit | Zero throttle never causes an unexpected climb | **Attitude/rate tracking works correctly at low or even zero throttle**; better flight performance overall |
| Risk | — | The vehicle may "keep climbing with the throttle at zero". A well-tuned vehicle won't, but **it can happen when an excessive P gain causes strong oscillation** |

This trade-off explains why airmode must be off while tuning: leaving it on masks the symptoms of gains that are too high.

## Related pages

- [[wiki/topics/px4-flight-stack]] — the controller layers and their gain parameters
- [[wiki/concepts/control-allocation]] — where mixing and saturation happen
- [[wiki/concepts/px4-parameters]] — looking up `MC_` / `MPC_` / `FW_` parameters
- [[wiki/concepts/flight-log-analysis]] — assessing tracking quality from logs
