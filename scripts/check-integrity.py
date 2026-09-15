#!/usr/bin/env python
"""Mechanical integrity check for the wiki (the machine-verifiable part of a wiki lint).

Usage:
    python scripts/check-integrity.py [--vault PATH]

Checks:
    3   Source integrity    — frontmatter `sources:` point to files that exist
    6   Index sync          — index.md entries point to existing pages; wiki pages
                              missing from index.md are warned
    7   Frontmatter         — required keys, valid type/status values,
                              has_conflict may only be the string "yes"
    7d  Doc version pins    — pages citing raw/documents/ should have a
                              well-formed doc_version_checked
    8a  Empty / stub        — very short bodies are warned (heuristic; read to confirm)
    8b  Unresolved links    — path-style wikilink targets exist; bare wikilinks are
                              always an error
    8c  Misplaced phantoms  — non-whitelisted .md files in the vault root; 0-byte .md
                              files next to a .base of the same name
    9   Typed relations     — superseded_by / supersedes / builds_on links are valid,
                              stale status and superseded_by go together, both
                              directions agree
    10  Documentation layer — docs-map/manifest.json matches the files in
                              raw/documents/; every document has the required
                              frontmatter keys; index page counts match the manifest

Prints a report grouped into ERROR and WARN. Exits 1 if there is any ERROR, else 0.
Semantic judgement (missing cross-references, possible contradictions, confirming
stubs) is left to the reader or the LLM.
"""
import argparse
import json
import os
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

try:
    import yaml
except ImportError:
    print("[FATAL] PyYAML is required: pip install pyyaml")
    sys.exit(2)

REQUIRED_KEYS = ["title", "type", "sources", "created", "updated", "tags", "status"]
VALID_TYPES = {"entity", "concept", "topic", "howto", "comparison",
               "synthesis", "query-result", "summary"}
VALID_STATUS = {"draft", "active", "stale"}
ROOT_MD_WHITELIST = {"CLAUDE.md", "index.md", "README.md", "THIRD_PARTY_NOTICES.md",
                     "log.md", "pending-pages.md"}
EXCLUDE_DIRS = {".obsidian", ".git", ".trash", "node_modules"}
LINK_EXTS = {".md", ".base", ".pdf", ".canvas", ".png", ".jpg", ".jpeg",
             ".webp", ".svg", ".json"}

# Frontmatter keys every document in raw/documents/ must have
DOC_REQUIRED = ["title", "type", "doc_set", "doc_version", "section",
                "source_url", "upstream_path", "ingested", "tags"]
# `<doc_set> <version>@<commit>`. MAVSDK has no commit to pin (its docs were
# captured from the website), so a capture date YYYY-MM-DD is also accepted.
DOC_VERSION_RE = re.compile(
    r"^(PX4|QGC|MAVSDK)\s+\S+@([0-9a-f]{7,40}|\d{4}-\d{2}-\d{2})$")

WIKILINK_RE = re.compile(r"\[\[([^\[\]]+?)\]\]")
FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n?", re.DOTALL)
CODE_FENCE_RE = re.compile(r"^```.*?^```", re.DOTALL | re.MULTILINE)
INLINE_CODE_RE = re.compile(r"`[^`\n]+`")
HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)


def strip_noise(text):
    """Remove code fences, inline code and HTML comments — [[...]] inside them are examples, not links."""
    return INLINE_CODE_RE.sub("", CODE_FENCE_RE.sub("", HTML_COMMENT_RE.sub("", text)))


def read_md(path):
    return path.read_text(encoding="utf-8-sig")


def parse_link_target(inner):
    """Get the target from [[...]]: drop the alias (including a table-escaped \\|) and any #heading."""
    target = re.split(r"\\?\|", inner, maxsplit=1)[0]
    target = target.split("#", 1)[0]
    return target.strip().rstrip("\\").strip()


def normalize_yaml_links(value):
    """Flatten a frontmatter wikilink field into a list of strings."""
    out, unquoted = [], False

    def walk(v):
        nonlocal unquoted
        if v is None:
            return
        if isinstance(v, str):
            out.append(v)
        elif isinstance(v, list):
            if v and all(isinstance(i, list) for i in v):
                unquoted = True
            for i in v:
                walk(i)
        else:
            out.append(str(v))

    walk(value)
    return out, unquoted


def extract_link_from_str(s):
    m = WIKILINK_RE.search(s)
    return parse_link_target(m.group(1)) if m else s.strip()


class Report:
    def __init__(self):
        self.errors, self.warns = [], []

    def error(self, category, path, msg):
        self.errors.append((category, path, msg))

    def warn(self, category, path, msg):
        self.warns.append((category, path, msg))


def build_inventory(vault):
    inv, basenames = {}, {}
    for root, dirs, files in os.walk(vault):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        for f in files:
            rel = (Path(root) / f).relative_to(vault).as_posix()
            inv[rel.lower()] = rel
            basenames.setdefault(Path(f).stem.lower(), []).append(rel)
    return inv, basenames


def resolve_target(target, inv):
    t = target.lower()
    if Path(t).suffix in LINK_EXTS:
        return t in inv
    return f"{t}.md" in inv or f"{t}.base" in inv


def strip_body(text):
    body = FRONTMATTER_RE.sub("", text, count=1)
    return re.sub(r"^# .*\n?", "", body, count=1, flags=re.MULTILINE)


def collapse_wikilinks(text):
    """[[a/b|label]] → label, [[a/b]] → b, so link paths don't inflate the character count."""
    def repl(m):
        parts = re.split(r"\\?\|", m.group(1), maxsplit=1)
        if len(parts) == 2:
            return parts[1]
        return Path(parts[0].split("#", 1)[0]).name
    return WIKILINK_RE.sub(repl, text)


# ---------------------------------------------------------------------------
# 10. Documentation layer
# ---------------------------------------------------------------------------
def check_docs_layer(vault, rep):
    docs_root = vault / "raw" / "documents"
    manifest_p = vault / "docs-map" / "manifest.json"
    if not docs_root.is_dir():
        rep.warn("docs layer", "raw/documents", "directory does not exist (no documentation imported)")
        return 0
    if not manifest_p.exists():
        rep.error("docs layer", "docs-map/manifest.json", "manifest does not exist")
        return 0

    try:
        man = json.loads(manifest_p.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        rep.error("docs layer", "docs-map/manifest.json", f"JSON parse error: {e}")
        return 0

    on_disk = {p.relative_to(vault).as_posix()
               for p in docs_root.rglob("*.md")}
    in_manifest = {r["path"] for r in man}

    for miss in sorted(in_manifest - on_disk)[:20]:
        rep.error("docs layer", miss, "listed in the manifest but the file does not exist")
    for extra in sorted(on_disk - in_manifest)[:20]:
        rep.error("docs layer", extra, "file exists but is not in the manifest")

    # Check the frontmatter of every document
    for rel in sorted(on_disk):
        p = vault / rel
        try:
            text = p.read_text(encoding="utf-8-sig")
        except Exception as e:                                   # noqa: BLE001
            rep.error("docs layer", rel, f"cannot read: {e}")
            continue
        m = FRONTMATTER_RE.match(text)
        if not m:
            rep.error("docs layer", rel, "missing frontmatter")
            continue
        try:
            fm = yaml.safe_load(m.group(1)) or {}
        except yaml.YAMLError as e:
            rep.error("docs layer", rel, f"frontmatter YAML parse error: {e}")
            continue
        if fm.get("type") != "document":
            rep.error("docs layer", rel, f"type should be document (found {fm.get('type')!r})")
        for k in DOC_REQUIRED:
            if k not in fm or fm[k] in (None, ""):
                rep.error("docs layer", rel, f"missing required key {k}")
                break

    # Do the index pages report the same counts as the manifest?
    per_set = {}
    for r in man:
        per_set[r["doc_set"]] = per_set.get(r["doc_set"], 0) + 1
    for label, slug in (("PX4", "px4"), ("QGC", "qgc"), ("MAVSDK", "mavsdk")):
        idx = vault / "docs-map" / f"{slug}.md"
        if label in per_set and not idx.exists():
            rep.error("docs layer", f"docs-map/{slug}.md",
                      "index does not exist — run scripts/build-docs-map.py")
        elif idx.exists():
            txt = idx.read_text(encoding="utf-8-sig")
            m = re.search(r"Local documents: \*\*(\d+)\*\*", txt)
            if m and int(m.group(1)) != per_set.get(label, 0):
                rep.error("docs layer", f"docs-map/{slug}.md",
                          f"index claims {m.group(1)} pages, manifest has "
                          f"{per_set.get(label, 0)} (run scripts/build-docs-map.py)")
    return len(on_disk)


# ---------------------------------------------------------------------------
def check(vault):
    rep = Report()
    inv, basenames = build_inventory(vault)
    wiki_pages = sorted((vault / "wiki").rglob("*.md")) if (vault / "wiki").is_dir() else []

    relations = {}

    for page in wiki_pages:
        rel = page.relative_to(vault).as_posix()
        try:
            text = read_md(page)
        except Exception as e:                                   # noqa: BLE001
            rep.error("read", rel, f"cannot read: {e}")
            continue

        # --- 7. Frontmatter ---
        m = FRONTMATTER_RE.match(text)
        if not m:
            rep.error("frontmatter", rel, "missing YAML frontmatter")
            fm = {}
        else:
            try:
                fm = yaml.safe_load(m.group(1)) or {}
                if not isinstance(fm, dict):
                    rep.error("frontmatter", rel, "frontmatter is not a key-value mapping")
                    fm = {}
            except yaml.YAMLError as e:
                rep.error("frontmatter", rel, f"YAML parse error: {e}")
                fm = {}

        if fm:
            for key in REQUIRED_KEYS:
                if key not in fm or fm[key] is None:
                    rep.error("frontmatter", rel, f"missing required key {key}")
            if "type" in fm and fm["type"] not in VALID_TYPES:
                rep.error("frontmatter", rel, f"invalid type: {fm['type']!r}")
            if "status" in fm and fm["status"] not in VALID_STATUS:
                rep.error("frontmatter", rel, f"invalid status: {fm['status']!r}")
            if "has_conflict" in fm and fm["has_conflict"] != "yes":
                rep.error("frontmatter", rel,
                          f'has_conflict may only be the string "yes" (found {fm["has_conflict"]!r}; '
                          "remove the whole line when there is no conflict)")

            # --- 3. Source integrity ---
            sources, unquoted = normalize_yaml_links(fm.get("sources"))
            if unquoted:
                rep.warn("frontmatter", rel, "wikilinks in sources are not quoted")
            cites_docs = False
            for s in sources:
                target = extract_link_from_str(s)
                if target.lower().startswith("raw/documents/"):
                    cites_docs = True
                if target and not resolve_target(target, inv):
                    rep.error("source links", rel, f"sources points to a missing file: [[{target}]]")

            # --- 7d. Doc version pins ---
            dvc, _ = normalize_yaml_links(fm.get("doc_version_checked"))
            if cites_docs and not dvc:
                rep.warn("doc version", rel,
                         "sources cite raw/documents/ but doc_version_checked is missing "
                         "(no way to tell whether this page is stale after the docs change)")
            for v in dvc:
                if not DOC_VERSION_RE.match(v.strip()):
                    rep.error("doc version", rel,
                              f"malformed doc_version_checked: {v!r} "
                              "(expected `<PX4|QGC|MAVSDK> <version>@<commit>`)")

            # --- 9. Typed relations ---
            rels = {}
            for key in ("superseded_by", "supersedes", "builds_on"):
                if key in fm:
                    links, unq = normalize_yaml_links(fm[key])
                    if unq:
                        rep.warn("frontmatter", rel, f"wikilinks in {key} are not quoted")
                    targets = [extract_link_from_str(x) for x in links]
                    rels[key] = targets
                    for t in targets:
                        if t == rel.removesuffix(".md"):
                            rep.error("typed relations", rel, f"{key} points to the page itself")
                        elif not resolve_target(t, inv):
                            rep.error("typed relations", rel,
                                      f"{key} points to a missing page: [[{t}]]")
            relations[rel] = rels

            status = fm.get("status")
            if status == "stale" and "superseded_by" not in fm:
                rep.error("typed relations", rel,
                          "status: stale but superseded_by is missing (CLAUDE.md requires both)")
            if "superseded_by" in fm and status != "stale":
                rep.warn("typed relations", rel,
                         f"has superseded_by but status is {status!r} (should be stale)")

        # --- 8b. Wikilink resolution ---
        body = strip_body(text)
        for lm in WIKILINK_RE.finditer(strip_noise(body)):
            target = parse_link_target(lm.group(1))
            if not target:
                continue
            if "/" not in target:
                cand = basenames.get(target.lower())
                hint = (f"(a file with this name exists: {cand[0]} — use a path-style link)" if cand
                        else "(no file with this name — use plain text)")
                rep.error("bare wikilink", rel, f"[[{target}]] bare wikilinks are not allowed {hint}")
            elif not resolve_target(target, inv):
                rep.error("broken link", rel, f"[[{target}]] target does not exist")
            elif target.lower().startswith("bases/") and not target.lower().endswith(".base"):
                rep.error("broken link", rel,
                          f"[[{target}]] links to bases/ must include the .base extension")

        # --- 8a. Empty / stub scan ---
        collapsed = collapse_wikilinks(body)
        nonempty = [ln for ln in collapsed.splitlines() if ln.strip()]
        content_len = len("".join(ln.strip() for ln in nonempty))
        if len(nonempty) < 3 or content_len < 250:
            rep.warn("stub", rel,
                     f"body looks very short ({len(nonempty)} non-empty lines, {content_len} characters) "
                     "— read it to confirm; short is not the same as empty")

    # --- 9. Both directions agree ---
    for rel, rels in relations.items():
        self_target = rel.removesuffix(".md")
        for t in rels.get("superseded_by", []):
            other = relations.get(inv.get(f"{t}.md".lower(), f"{t}.md"), {})
            if self_target not in other.get("supersedes", []):
                rep.warn("typed relations", rel,
                         f"superseded_by points to [[{t}]], but that page's supersedes does not list this page")
        for t in rels.get("supersedes", []):
            other = relations.get(inv.get(f"{t}.md".lower(), f"{t}.md"), {})
            if self_target not in other.get("superseded_by", []):
                rep.warn("typed relations", rel,
                         f"supersedes points to [[{t}]], but that page's superseded_by does not list this page")

    # --- 8c. Misplaced phantoms ---
    for f in vault.glob("*.md"):
        if f.name not in ROOT_MD_WHITELIST:
            rep.error("phantom", f.name,
                      "non-whitelisted .md in the vault root (probably created by clicking a graph phantom)")
    bases_dir = vault / "bases"
    if bases_dir.is_dir():
        for f in bases_dir.glob("*.md"):
            if (bases_dir / f"{f.stem}.base").exists() and f.stat().st_size == 0:
                rep.error("phantom", f"bases/{f.name}",
                          "0-byte .md with the same name as a .base (caused by [[bases/x]] without the extension)")

    # --- 6. Index sync ---
    index_path = vault / "index.md"
    if index_path.exists():
        index_text = strip_noise(read_md(index_path))
        indexed = set()
        for lm in WIKILINK_RE.finditer(index_text):
            target = parse_link_target(lm.group(1))
            if not target:
                continue
            if target.lower().startswith("wiki/"):
                indexed.add(target.lower())
            if not resolve_target(target, inv):
                rep.error("index sync", "index.md", f"[[{target}]] target does not exist")
        for page in wiki_pages:
            rel_noext = page.relative_to(vault).as_posix().removesuffix(".md").lower()
            if rel_noext not in indexed:
                rep.warn("index sync", page.relative_to(vault).as_posix(),
                         "not listed in index.md")
    else:
        rep.error("index sync", "index.md", "index.md does not exist")

    n_docs = check_docs_layer(vault, rep)
    return rep, len(wiki_pages), n_docs


def main():
    parser = argparse.ArgumentParser(description="Mechanical integrity check for the wiki")
    parser.add_argument("--vault", default=None)
    args = parser.parse_args()

    vault = Path(args.vault) if args.vault else Path(__file__).resolve().parent.parent
    if not (vault / "CLAUDE.md").exists():
        print(f"[FATAL] no CLAUDE.md under {vault}; pass the vault root with --vault")
        sys.exit(2)

    rep, n_pages, n_docs = check(vault)

    print("=== Wiki integrity check ===")
    print(f"vault: {vault}")
    print(f"wiki pages scanned: {n_pages} | documents: {n_docs}\n")

    for label, items in (("ERROR", rep.errors), ("WARN", rep.warns)):
        if items:
            print(f"--- {label} ({len(items)}) ---")
            by_cat = {}
            for cat, path, msg in items:
                by_cat.setdefault(cat, []).append((path, msg))
            for cat in sorted(by_cat):
                print(f"[{cat}]")
                for path, msg in by_cat[cat][:60]:
                    print(f"  {path}: {msg}")
                if len(by_cat[cat]) > 60:
                    print(f"  … {len(by_cat[cat]) - 60} more of the same kind")
            print()

    print(f"Summary: {len(rep.errors)} errors, {len(rep.warns)} warnings, "
          f"{n_pages} wiki pages / {n_docs} documents scanned")
    sys.exit(1 if rep.errors else 0)


if __name__ == "__main__":
    main()
