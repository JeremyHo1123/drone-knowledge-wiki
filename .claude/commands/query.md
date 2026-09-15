---
description: Answer conceptual or research questions from the knowledge base, and fold answers worth keeping back into the wiki
argument-hint: A question in natural language (any language)
---

This command handles **conceptual, research, comparison and overview** questions. Purely operational / parameter / API questions go to `/docs-query` (it has a retrieval path optimized for 1,000+ official documents). If unsure: when the question contains a concrete parameter name, API name or QGC screen name → `/docs-query`; when it asks "how does it work / why / which method is better / what approaches exist" → this command.

The goal is to **make good use of the existing wiki first, go into `raw/` only when needed**, and fold the answer back into the wiki when it is worth keeping — **preferably by integrating it into a proper concept / topic / howto page, and only when necessary as a `wiki/queries/` page**.

## Steps

### 1. Parse the intent

- **Definition** ("What is VIO?", "How does control allocation work?") → concept page
- **Entity** ("Who maintains EKF2?", "Pixhawk 6X specs?") → entity page
- **Comparison** ("EKF2 vs. other attitude estimators", "MAVSDK vs. MAVROS") → several concept/entity pages; consider producing a comparison page
- **Topic overview** ("What are the approaches to autonomous obstacle avoidance?") → topic page + related concepts
- **Paper detail** ("What was the experimental setup in paper X?") → summary page; read the original in `raw/papers/` if that isn't enough
- **Cross-source follow-up** ("Does PX4 support this paper's method?") → **the most valuable question type in this knowledge base**; needs both the paper summary and the documentation, see step 4
- **Cross-source consistency** ("Do these two papers agree?") → several summaries, back to the originals when needed

For vague questions ("tell me about offboard"), first fill in a reasonable concrete version ("the offboard mechanism, its entry conditions, and how to run it with MAVSDK") and briefly state your interpretation before answering.

### 2. Locate with index.md

Always read `index.md` first — it is the wiki's table of contents and finds the 3–8 most relevant pages with the fewest tokens.

- Keyword match: proper nouns, method names and author names in the question
- Tag match: `uav/*` (what problem) and `stack/*` (which software) narrow down the sub-field
- If the index isn't enough, Grep `wiki/` for keywords (titles and first paragraphs first, not the full text)

### 3. Read the relevant wiki pages

Read in order of relevance and **don't read every candidate at once**: start with the 1–2 most central pages and stop when you have enough.

- Watch for `status: stale` — check whether the page says what replaced it
- Watch for `has_conflict: "yes"` — the answer must disclose it
- Watch for `doc_version_checked` — if it doesn't match the current documentation version, the technical details may be outdated

### 4. Go back to raw/ when needed

Read the original sources when:

- the user asks for exact numbers, formulas or quotations
- the wiki is too abstract to answer the specific detail
- a wiki claim needs verifying (the user doubts it)
- a cross-source follow-up requires the originals to judge whether there is a real contradiction

**Standard procedure for "paper method vs. actual implementation" questions** — this knowledge base's signature capability; do all three steps:

1. Read `wiki/summaries/` or `raw/papers/` to understand what the paper claims and what it assumes
2. Following steps 2–3 of `/docs-query`, look in `raw/documents/` for **what PX4/MAVSDK actually provides** (is there a matching mode, parameter or API?)
3. State the **gap** explicitly: already in mainline / needs an add-on or a companion computer / research prototype only / no counterpart at all. Write the gap as a `## Research–implementation gap` section on the page, not as a contradiction

When reading PDFs in `raw/papers/`, target passages with `pages:` (check the companion metadata `.md` for the structure first) instead of scanning the whole document.

### 5. Compose the answer

- **Markdown** (default): definitions, entities, paper details
- **Comparison table**: comparisons; typical columns are "method / core idea / strengths / limitations / counterpart in the PX4 ecosystem"
- **Step list**: when the answer has an operational part

Rules:

- **Cite sources**: attach a `[[wiki/...]]` or `[[raw/...]]` wikilink to every key claim
- **Disclose uncertainty**: if the knowledge base doesn't cover something, say "not documented in this wiki" — **never make it up**
- **Disclose contradictions**: when a page has `has_conflict: "yes"`, summarize both sides; don't hide the dispute or silently pick one side
- **Disclose staleness**: warn when a page is `status: stale` or its `updated:` date is old

### 6. Fold back into the wiki: integrate rather than archive

**Core principle: synthesized knowledge should live in exactly one place — if it can be integrated into a proper page, don't create a separate query-result page.** A query-result is a "derived snapshot": it duplicates existing pages and silently goes stale when they are updated. It is **the exception, not the default**. Decide in this order:

1. **Default: answer in the conversation and save nothing.** Most questions are lookups, and the answer already lives in an existing page.
2. **If the answer is a new synthesis worth keeping** (new, reusable, not yet captured by any page): **fold it into the most relevant existing concept / topic / howto page**, and update `updated:` and — if you read new sources — `sources:`.
3. **Only if the synthesis has "no home"** (it spans too many topics and has no single owning page), create a standalone `wiki/queries/` page as a "snapshot awaiting integration", linking all the proper pages it drew on.
4. **Never let a query-result become a copy of a page**: if it only restates → don't save it; if it improves that page → edit the page itself.

Whichever route you take, **ask the user before changing or creating anything**.

If you do create a query-result page: `wiki/queries/YYYY-MM-DD-slug.md`

```yaml
---
title: The core question answered
type: query-result
sources:
  - "[[wiki/concepts/xxx]]"
  - "[[raw/papers/yyy]]"
  - "[[raw/documents/PX4/zzz]]"
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags:
  - uav/subcategory
status: active
# doc_version_checked:  ← required when raw/documents/ is cited
#   - "PX4 main@9467506"
# has_conflict: "yes"   ← only when disclosing an unresolved contradiction; omit otherwise
---
```

Structure: `## Question` → `## Answer` → `## Related pages`. After saving, add an entry under the matching category in `index.md` in the form `- [[wiki/queries/...]] — one-sentence summary`, then run `scripts/check-integrity.py`.

### 7. Long-term integration (reminder only, never automatic)

When `wiki/queries/` has accumulated several related query-results that could be distilled into a proper page, **remind** the user at the end of the answer, but don't change existing proper pages on your own.

---

## Output format

Before starting, briefly report your interpretation of the question and which pages you plan to read (so the user can stop you).
After answering: offer to save when appropriate, and point out blind spots in the wiki when you find them.

## Notes

- Reply in the user's language; keep proper nouns, parameter names and API names in their original form
- Never invent information that isn't in the knowledge base; say so when unsure
- Read PDFs in chunks with `pages:`, never the whole document
- Use full-path wikilinks `[[wiki/path/page]]` / `[[raw/path/file]]`; bare wikilinks are forbidden
