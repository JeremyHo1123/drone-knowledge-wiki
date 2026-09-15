---
title: "Documentation coverage report"
type: report
generated: 2026-07-28
---

# Documentation coverage report

A static record of the page-by-page coverage check run when the documentation snapshot was captured (2026-07-28). The verification script is not part of this repository; the numbers below describe the snapshot that ships here.

Method: fetch the full list of pages from each official website (PX4 through its official `sitemap.xml`; QGC and MAVSDK have no sitemap, so their sites were crawled breadth-first from the home page, following every internal link — this also finds pages that are only reachable from sub-pages), then compare that list page by page with `docs-map/manifest.json`. The number of missing pages must be 0.

### PX4 — PASS

- Reference list: official sitemap.xml (4,191 entries in total, 1,050 after keeping English pages only)
- Pages online: **1050**
- Stored locally: **960**
- Dropped on purpose (navigation-only pages / redirect stubs): **90**
- Missing: **0**
- Coverage ((stored + dropped on purpose) ÷ pages online): **100.0%**

Present locally but not in the online list (usually a difference in how the site indexes itself):

  - https://docs.px4.io/main/en

### QGC — PASS

- Reference list: breadth-first crawl from the home page (75 pages visited)
- Pages online: **75**
- Stored locally: **73**
- Dropped on purpose (navigation-only pages / redirect stubs): **2**
- Missing: **0**
- Coverage ((stored + dropped on purpose) ÷ pages online): **100.0%**

### MAVSDK — PASS

- Reference list: breadth-first crawl from the home page (45 pages visited)
- Pages online: **45**
- Stored locally: **41**
- Dropped on purpose (navigation-only pages / redirect stubs): **4**
- Missing: **0**
- Coverage ((stored + dropped on purpose) ÷ pages online): **100.0%**

### Content spot check (vocabulary coverage)

**40** local documents were picked at random. For each, the visible text of the official online page was fetched, and the check measured what share of the words in the local copy really appear in the online original. This verifies that the content was stored completely, not only that the file exists. A word-set comparison is used instead of sentence-by-sentence matching, because sentence matching is flooded with false alarms from layout differences (permalink symbols, definition lists, VitePress container rendering).

- Average vocabulary coverage: **97.4%**
- At or above the 90% threshold: **39/40**
- Skipped (too few comparable words, or the fetch failed): **0**

Below the threshold:

  - `raw/documents/PX4/assembly/assembly_fw.md` — 89.2% (619 words); examples of words not found online: accurately, alone, altitude., assist, breaks, buildings, capable, case

> Coverage below 100% **does not mean content is missing**. Known, expected gaps: (1) after VitePress `<!--@include:-->` shared fragments are expanded, the local file contains the multicopter, fixed-wing and VTOL variants together, while the online page renders only one of them with `v-if` — the local copy has **more** than the online page, not less; (2) tables and code blocks are rendered with different markup online; (3) the upstream page was updated after the capture. Real content loss shows up as much lower coverage (<70%) with whole paragraphs missing.
