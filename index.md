# Drone Knowledge Wiki — Index

The table of contents of this wiki. Schema and conventions are in `CLAUDE.md`; the project overview is in `README.md`.

## How to ask

| Your question looks like | Use |
| --- | --- |
| "How do I configure X", "Which parameter controls Y", "How do I call Z in MAVSDK" | `/docs-query` |
| "How does X work", "What is the difference between A and B", "What approaches exist" | `/query` |

## Official documentation (raw/documents/)

1,075 pages of official documentation, read-only. The routing tables live in `docs-map/`:

- [[docs-map/index|Documentation layer overview]]
- [[docs-map/glossary|Chinese–English glossary]] — the documents are English only; maps about 100 Chinese terms to the official English terms, with real hit counts and main locations
- [[docs-map/px4|PX4 index]] — 961 pages, `main`, flight controller firmware (90 sections, each with its own page list)
- [[docs-map/qgc|QGC index]] — 73 pages, `Stable_V5.0`, ground station
- [[docs-map/mavsdk|MAVSDK index]] — 41 pages, Python 3.17.2, programmatic control
- [[docs-map/coverage-report|Page-by-page coverage report]]

Retrieval path: **question → non-English terms translated into official English (glossary for Chinese) → the doc-set index picks the section → Grep `raw/documents/<set>/<section>/`**. Details in `/docs-query`.

## Topics

- [[wiki/topics/drone-software-stack]] — how PX4 / MAVLink / QGC / MAVSDK divide the work, and which layer to look in for a feature
- [[wiki/topics/px4-flight-stack]] — PX4's internal architecture: the full data flow from sensors to motors, cascaded controllers and uORB

## Concepts

### Flight control and tuning

- [[wiki/concepts/control-allocation]] — how torque/thrust commands become individual motor and servo commands
- [[wiki/concepts/flight-modes]] — the mode system, and the split between internal and external (ROS 2) modes
- [[wiki/concepts/pid-tuning]] — autotune first, the iron rules of manual tuning, airmode and mixer saturation
- [[wiki/concepts/px4-parameters]] — the entry point to all tunable behaviour: naming, three ways to change parameters, three reasons one can't be found

### State estimation and perception

- [[wiki/concepts/collision-prevention]] — reactive collision prevention (not avoidance), and its strict enabling conditions
- [[wiki/concepts/ekf2]] — the navigation filter: estimated states, the delayed fusion time horizon, single vs. multiple instances
- [[wiki/concepts/rtk-gnss]] — centimetre-level positioning, the base/rover pair, and replacing the compass
- [[wiki/concepts/visual-inertial-odometry]] — a position source for GNSS-denied environments; PX4 provides the interface, not the algorithm

### Autonomy and programmatic control

- [[wiki/concepts/mission-planning]] — mission planning, feasibility checks, Mission vs. MissionRaw
- [[wiki/concepts/offboard-control]] — handing control to an external program; the setpoint stream is the proof of life
- [[wiki/concepts/ros2-px4-bridge]] — the uXRCE-DDS architecture and three levels of ROS 2 integration

### Safety and simulation

- [[wiki/concepts/failsafe]] — the action ladder, the more severe action wins, verify in simulation first
- [[wiki/concepts/flight-log-analysis]] — a structured analysis order, and triage when a log stops in mid-air
- [[wiki/concepts/geofence]] — two independent mechanisms, active in all modes
- [[wiki/concepts/sitl-simulation]] — SITL/HITL, and how to choose between Gazebo and SIH

### Communication and middleware

- [[wiki/concepts/uorb-messaging]] — PX4's internal message bus, and watching the data flow from the shell

## Entities (people, organizations, products, systems)

*(no pages yet)*

## How-to (executable procedures)

- [[wiki/howto/mavsdk-takeoff-and-land]] — a minimal runnable example: connect, arm, take off and land with MAVSDK-Python

## Summaries (single-source summaries)

*(no pages yet)*

## Comparisons / Syntheses

*(no pages yet)*

## Queries (saved query results)

*(no pages yet)*

## Bases (dashboard views)

- [[bases/dashboard.base|dashboard]] — all pages, pages needing attention, recent activity
- [[bases/concepts.base|concepts]] — concept pages grouped by tag
- [[bases/entities.base|entities]] — entity pages
- [[bases/howto.base|howto]] — how-to guides, including a "missing documentation version" check
- [[bases/papers.base|papers]] — paper and article summaries
- [[bases/doc-refs.base|doc-refs]] — pages that cite documentation, grouped by the documentation version they rely on
- [[bases/conflicts.base|conflicts]] — unresolved cross-source contradictions
- [[bases/stale-pages.base|stale-pages]] — superseded pages

## Other

- `raw/papers/`, `raw/articles/` — papers and web clippings (this edition ships one PX4 guide clipping)
- `templates/` — page templates
- `scripts/` — integrity check and index generators
