# Third-party notices

This repository bundles documentation from three open-source projects in `raw/documents/`, plus one web clipping in `raw/articles/`. That material is **not** covered by this repository's MIT licence, or by the CC BY 4.0 licence of the wiki text. It stays under the licence its authors chose, as listed below.

All material was captured on 2026-07-28.

## Changes made to the bundled documentation

The documents were converted so they can be searched and linked offline. Across the three doc sets:

- a YAML frontmatter block was added to every file (title, doc set, version, section, source URL, upstream path and commit, capture date, tags);
- shared fragments pulled in with VitePress `<!--@include: ...-->` directives were expanded in place, where the upstream used them;
- relative image and media links were rewritten as absolute `raw.githubusercontent.com` URLs;
- pages with no content of their own (navigation-only indexes, redirect stubs, generated search and index pages) were left out; they are listed with reasons in `docs-map/dropped.json`.

Apart from these conversions, the wording of the documentation was not changed.

## PX4 Autopilot User Guide

| | |
| --- | --- |
| Location | `raw/documents/PX4/` (961 pages) |
| Source | [PX4/PX4-Autopilot `docs/`](https://github.com/PX4/PX4-Autopilot/tree/9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55/docs), branch `main`, commit `9467506bff09ffe2b4ca5e509c12f9f9b9a1eb55` |
| Website | https://docs.px4.io/main/en/ |
| Authors | PX4 documentation contributors |
| Licence | Creative Commons Attribution 4.0 International ([CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)); full text in [`LICENSES/CC-BY-4.0.txt`](LICENSES/CC-BY-4.0.txt) |
| Changes | As listed above |

## QGroundControl User Guide

| | |
| --- | --- |
| Location | `raw/documents/QGC/` (73 pages) |
| Source | [mavlink/qgroundcontrol `docs/`](https://github.com/mavlink/qgroundcontrol/tree/cb6ee485e0e11c74ed667ca573e7593f770da436/docs), branch `Stable_V5.0`, commit `cb6ee485e0e11c74ed667ca573e7593f770da436` |
| Website | https://docs.qgroundcontrol.com/Stable_V5.0/en/qgc-user-guide/ |
| Authors | QGroundControl project contributors |
| Licence | The QGroundControl repository is dual-licensed under the Apache License 2.0 and the GNU General Public License v3, and recipients may choose either ([licence information](https://github.com/mavlink/qgroundcontrol/blob/master/.github/COPYING.md)). This repository redistributes the QGroundControl documentation under the **Apache License 2.0**; full text in [`LICENSES/Apache-2.0-QGroundControl.txt`](LICENSES/Apache-2.0-QGroundControl.txt) |
| Changes | As listed above |

## MAVSDK-Python API reference

| | |
| --- | --- |
| Location | `raw/documents/MAVSDK/` (41 pages) |
| Source | The published API reference for MAVSDK-Python 3.17.2 at http://mavsdk-python-docs.s3-website.eu-central-1.amazonaws.com/, generated from [mavlink/MAVSDK-Python](https://github.com/mavlink/MAVSDK-Python) |
| Copyright | Copyright (c) 2020, MAVSDK Development Team |
| Licence | BSD 3-Clause License; full text in [`LICENSES/BSD-3-Clause-MAVSDK-Python.txt`](LICENSES/BSD-3-Clause-MAVSDK-Python.txt) |
| Changes | Converted from the published HTML to Markdown, in addition to the changes listed above |

## Web clipping

| | |
| --- | --- |
| Location | `raw/articles/2026-07-28-px4-user-guide-home-clipping.md` |
| Source | The home page of the PX4 Autopilot User Guide, https://docs.px4.io/main/en/ |
| Authors | PX4 documentation contributors |
| Licence | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); full text in [`LICENSES/CC-BY-4.0.txt`](LICENSES/CC-BY-4.0.txt). The page credits two icons separately under CC BY 3.0 (Smashicons and Magnific, via flaticon.com); the clipping contains only that credit text, not the icons |
| Changes | Saved as Markdown with a short frontmatter block |

## Trademarks

PX4 trademarks are held by the Dronecode Foundation. QGroundControl, MAVLink and MAVSDK are names of their respective projects. They are used here only to identify the documentation. This repository is an independent project and is not affiliated with or endorsed by any of them.
