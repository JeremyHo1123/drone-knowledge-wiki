---
title: Page title
type: concept
sources:
  - "[[raw/papers/YYYY-MM-DD-slug]]"
  - "[[raw/documents/PX4/section/page]]"
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags:
  - uav/subcategory
  - stack/px4
status: draft
# doc_version_checked:   ← required when citing raw/documents/
#   - "PX4 main@9467506"
# has_conflict: "yes"    ← only when there is an unresolved contradiction
# superseded_by: / supersedes: / builds_on:   ← only when the relationship is explicit
---

# Page title

One paragraph on what this is and why it matters. **The first paragraph must answer "what is this page about" on its own** — don't just write "this page introduces…".

## Core mechanism

The substance. Formulas in LaTeX (`$...$`). Parameter names, API names and commands always stay in their original form.

## Mapping in the PX4 ecosystem

**This section is the point of this knowledge base** — connect the concept to things you can execute:

- PX4 parameter: `PARAM_NAME` — description (see [[raw/documents/PX4/advanced_config/parameter_reference]])
- PX4 documentation: [[raw/documents/PX4/...]]
- MAVSDK API: `Plugin.method()` — [[raw/documents/MAVSDK/plugins/...]]
- QGC location: menu path — [[raw/documents/QGC/...]]

If there is no implementation yet, **say so explicitly** ("no counterpart in the PX4 mainline") and explain what is missing; don't be vague.

## Related pages

- [[wiki/concepts/xxx]] — one sentence on the relation
- [[wiki/howto/yyy]] — one sentence on the relation

<!-- Add this section only for an unresolved contradiction, and set has_conflict: "yes" in the frontmatter
## Disputes and disagreements

- **Side A** ([[source-1]]): claims…
- **Side B** ([[source-2]]): claims…
-->

<!-- Use this section when a paper says something works but implementations haven't caught up (this is not a contradiction; don't set has_conflict)
## Research–implementation gap

- Papers claim: … ([[raw/papers/...]])
- PX4 today: … ([[raw/documents/PX4/...]])
- Nature of the gap: research prototype only / needs a companion computer / needs an add-on module / in mainline but disabled by default
-->
