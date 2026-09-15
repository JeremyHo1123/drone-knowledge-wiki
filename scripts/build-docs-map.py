#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Generate the documentation index layer (docs-map/*.md) from docs-map/manifest.json.

The index layer is for routing: a question first lands on the right doc set and
section, then Grep finds the exact passage in raw/documents/. The index holds no
knowledge content and is entirely machine-generated — re-run this script after
changing docs-map/manifest.json or docs-map/dropped.json.

Usage:
    python scripts/build-docs-map.py
"""
import json
import os
import sys
from collections import defaultdict
from datetime import date

sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANIFEST = os.path.join(ROOT, "docs-map", "manifest.json")
DROPPED = os.path.join(ROOT, "docs-map", "dropped.json")

SET_META = {
    "PX4": {
        "slug": "px4",
        "desc": "PX4 Autopilot User and Developer Guide (flight controller firmware: architecture, "
                "flight modes, parameters, simulation, assembly and tuning)",
        "site": "https://docs.px4.io/main/en/",
        "version": "main (development branch)",
    },
    "QGC": {
        "slug": "qgc",
        "desc": "QGroundControl User Guide (ground station: plan, fly, setup and analyze views)",
        "site": "https://docs.qgroundcontrol.com/Stable_V5.0/en/qgc-user-guide/",
        "version": "Stable_V5.0",
    },
    "MAVSDK": {
        "slug": "mavsdk",
        "desc": "MAVSDK-Python API reference (Python library for controlling drones from offboard programs)",
        "site": "http://mavsdk-python-docs.s3-website.eu-central-1.amazonaws.com/",
        "version": "MAVSDK-Python 3.17.2",
    },
}

# Section descriptions; sections not listed get a prettified folder name
SECTION_HINT = {
    "PX4": {
        "getting_started": "Getting started: basic concepts, first flight, sensor orientation",
        "config": "Standard configuration: firmware, airframe, sensor calibration, radio, safety",
        "advanced_config": "Advanced configuration: parameters, EKF tuning, ESC calibration, Ethernet",
        "flight_modes": "Flight modes (common)",
        "flight_modes_mc": "Flight modes: multicopter",
        "flight_modes_fw": "Flight modes: fixed-wing",
        "flight_modes_vtol": "Flight modes: VTOL",
        "flight_modes_rover": "Drive modes: rover",
        "flight_stack": "Flight stack: controller architecture and algorithms",
        "concept": "Core concepts: system architecture, flight tasks, control allocation",
        "modules": "Module and command reference (shell commands, module descriptions)",
        "msg_docs": "uORB message reference",
        "mavlink": "MAVLink interface and messages",
        "ros": "ROS 1 integration",
        "ros2": "ROS 2 / uXRCE-DDS integration",
        "middleware": "Middleware: uORB, uXRCE-DDS, module communication",
        "simulation": "Simulation: SITL/HITL overview",
        "dev_setup": "Development environment setup and building",
        "development": "Development guide",
        "computer_vision": "Computer vision: VIO, obstacle avoidance, optical flow",
        "advanced": "Advanced topics: offboard control, gimbals, neural network control",
        "companion_computer": "Companion computers (Jetson, Raspberry Pi and others)",
        "flight_controller": "Flight controller hardware",
        "peripherals": "Peripherals",
        "sensor": "Sensors",
        "gps_compass": "GPS / compass / RTK",
        "telemetry": "Telemetry links",
        "log": "Flight logs and analysis",
        "debug": "Debugging tools",
        "sim_gazebo_gz": "Gazebo (new) simulation",
        "sim_gazebo_classic": "Gazebo Classic simulation",
        "robotics": "Robotics integration",
        "airframes": "Airframe reference and configuration files",
        "actuators": "Actuator setup",
        "payloads": "Payloads and delivery",
    },
    "QGC": {
        "getting_started": "Getting started: download, install, quick start",
        "setup_view": "Setup view: firmware, airframe, sensors, radio, flight modes, safety",
        "plan_view": "Plan view: missions, geofences, rally points, survey patterns",
        "fly_view": "Fly view: HUD, instrument panel, video streaming, toolbar",
        "analyze_view": "Analyze view: log download, MAVLink console and inspector, geotagging",
        "settings_view": "Application settings",
        "viewer_3d": "3D viewer",
        "custom_actions": "Custom actions",
        "troubleshooting": "Troubleshooting",
        "support": "Support and reporting",
        "releases": "Release notes",
        "root": "Home page",
    },
    "MAVSDK": {
        "plugins": "Plugin API: one file per plugin (Action, Telemetry, Mission, Offboard…)",
        "root": "Core: the System connection object, API overview, Jetson Nano installation",
    },
}


def pretty(section):
    return section.replace("_", " ").replace("-", " ").title()


def main():
    man = json.load(open(MANIFEST, encoding="utf-8"))
    drop = json.load(open(DROPPED, encoding="utf-8")) if os.path.exists(DROPPED) else []
    today = date.today().isoformat()

    by_set = defaultdict(lambda: defaultdict(list))
    for r in man:
        by_set[r["doc_set"]][r["section"]].append(r)
    drop_by_set = defaultdict(list)
    for r in drop:
        drop_by_set[r["doc_set"]].append(r)

    overview = []
    for label in ("PX4", "QGC", "MAVSDK"):
        meta = SET_META[label]
        secs = by_set[label]
        total = sum(len(v) for v in secs.values())
        hints = SECTION_HINT.get(label, {})
        # Large doc sets get one page list per section, so no single file gets too big
        split = total > 150

        out = [
            "---",
            f'title: "{label} documentation index"',
            "type: docs-index",
            f"doc_set: {label}",
            f"doc_version: {meta['version']}",
            f"generated: {today}",
            "tags:",
            f"  - docs/{meta['slug']}",
            "  - docs/index",
            "---",
            "",
            f"# {label} documentation index",
            "",
            f"{meta['desc']}",
            "",
            f"- Official site: {meta['site']}",
            f"- Version: {meta['version']}",
            f"- Local documents: **{total}** pages in `raw/documents/{label}/`",
            f"- Generated: {today} (by `scripts/build-docs-map.py`; don't edit this file by hand — "
            "edit `docs-map/manifest.json` or `docs-map/dropped.json` and re-run the script)",
            "",
            "> [!tip] How to use this index",
            "> Find the right section here first, then Grep `raw/documents/"
            f"{label}/<section>/` for the exact passage. The index lists titles only, no content.",
            "",
            "## Sections",
            "",
            "| Section | Pages | Description |",
            "| --- | ---: | --- |",
        ]
        for sec in sorted(secs, key=lambda s: (s == "root", s)):
            note = hints.get(sec, pretty(sec))
            link = (f"[{sec}]({meta['slug']}/{sec}.md)" if split
                    else f"[{sec}](#{sec.replace('_', '-')})")
            out.append(f"| {link} | {len(secs[sec])} | {note} |")
        out.append("")

        if split:
            secdir = os.path.join(ROOT, "docs-map", meta["slug"])
            os.makedirs(secdir, exist_ok=True)
            for old in os.listdir(secdir):
                if old.endswith(".md"):
                    os.remove(os.path.join(secdir, old))
            out.append(f"The full page list of each section is in `docs-map/{meta['slug']}/<section>.md` "
                       "(the Section column above links to it).")
            out.append("")
            for sec in secs:
                sout = [
                    "---",
                    f'title: "{label} / {sec}"',
                    "type: docs-index",
                    f"doc_set: {label}",
                    f"section: {sec}",
                    f"generated: {today}",
                    "tags:",
                    f"  - docs/{meta['slug']}",
                    "  - docs/index",
                    "---",
                    "",
                    f"# {label} / {sec}",
                    "",
                    f"{hints.get(sec, pretty(sec))} ({len(secs[sec])} pages)"
                    f" — back to the [{label} index](../{meta['slug']}.md)",
                    "",
                ]
                for r in sorted(secs[sec], key=lambda x: x["path"]):
                    rel = r["path"][len("raw/documents/"):]
                    sout.append(f"- [{r['title']}](../../raw/documents/{rel})"
                                f" · [official page]({r['url']})")
                sout.append("")
                open(os.path.join(secdir, f"{sec}.md"), "w",
                     encoding="utf-8", newline="\n").write("\n".join(sout))
        else:
            out.append("## Pages by section")
            out.append("")
            for sec in sorted(secs, key=lambda s: (s == "root", s)):
                out.append(f"### {sec}")
                out.append("")
                out.append(f"{hints.get(sec, pretty(sec))} ({len(secs[sec])} pages)")
                out.append("")
                for r in sorted(secs[sec], key=lambda x: x["path"]):
                    rel = r["path"][len("raw/documents/"):]
                    out.append(f"- [{r['title']}](../raw/documents/{rel})"
                               f" · [official page]({r['url']})")
                out.append("")

        dl = drop_by_set[label]
        if dl:
            out.append("## Upstream pages intentionally left out")
            out.append("")
            out.append(f"The {len(dl)} upstream pages below are not in `raw/documents/` because they have "
                       "no real content: a title only, only links to other pages, or redirect and index "
                       "artefacts generated by the site. Their content lives in the pages they point to, "
                       "so no knowledge is lost.")
            out.append("")
            out.append("| Upstream path | Reason |")
            out.append("| --- | --- |")
            for r in sorted(dl, key=lambda x: x["upstream_path"]):
                out.append(f"| `{r['upstream_path']}` | {r['reason']} |")
            out.append("")

        path = os.path.join(ROOT, "docs-map", f"{meta['slug']}.md")
        open(path, "w", encoding="utf-8", newline="\n").write("\n".join(out))
        print(f"  {path}  ({total} pages / {len(secs)} sections)")
        overview.append((label, meta, total, len(secs)))

    # docs-map/index.md ----------------------------------------------------
    grand = sum(o[2] for o in overview)
    idx = [
        "---",
        'title: "Documentation layer"',
        "type: docs-index",
        f"generated: {today}",
        "tags:",
        "  - docs/index",
        "---",
        "",
        "# Documentation layer",
        "",
        f"`raw/documents/` holds **{grand}** pages of official documentation. This layer is a "
        "machine-generated routing table with no knowledge content — interpretation goes in `wiki/`, "
        "the original text stays in `raw/`.",
        "",
        "| Doc set | Pages | Sections | Covers | Index |",
        "| --- | ---: | ---: | --- | --- |",
    ]
    for label, meta, total, nsec in overview:
        idx.append(f"| **{label}** | {total} | {nsec} | {meta['desc']} | "
                   f"[{meta['slug']}.md]({meta['slug']}.md) |")
    idx += [
        "",
        "## Files",
        "",
        "- `glossary.md` — Chinese–English glossary. The documents are English only, so Chinese search "
        "terms get zero hits: **for a technical question asked in Chinese, translate the key terms with it "
        "before you Grep**. Generated by `scripts/build-glossary.py`.",
        "- `manifest.json` — path, title, section, official URL and size of every document. For scripts "
        "and batch lookups; about 300 KB, so search it instead of reading it whole.",
        "- `dropped.json` — upstream pages intentionally left out, with reasons, so a coverage check can "
        "tell \"dropped on purpose\" from \"missing\".",
        "- `coverage-report.md` — the page-by-page coverage check run when the snapshot was captured "
        "(a static record).",
        "",
        "## Regenerating",
        "",
        "The snapshot in `raw/documents/` was produced by a conversion pipeline that is not part of this "
        "repository. The index files in this folder can be rebuilt from `manifest.json` and `dropped.json`:",
        "",
        "```bash",
        "python scripts/build-docs-map.py",
        "python scripts/build-glossary.py",
        "```",
        "",
    ]
    p = os.path.join(ROOT, "docs-map", "index.md")
    open(p, "w", encoding="utf-8", newline="\n").write("\n".join(idx))
    print(f"  {p}")


if __name__ == "__main__":
    main()
