#!/usr/bin/env python3
"""Structure check for every case set under cases/.

Checks structure only. It never runs a case and never changes a label.
  - cases.yaml parses, and README.md sits beside it
  - suite, version and a status block (label, qualifier, note) are present
  - the label is one of the four the README defines
  - principle and no_trivial_pass are stated
  - every case has id, kind, title, setup, actions, boundary, observe, pass,
    conformance_level; ids are unique; pairs_with resolves within the set
"""
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("check-cases: PyYAML is required (python3 -m pip install pyyaml)")
    sys.exit(2)

ROOT = Path(__file__).resolve().parent.parent
LABELS = {"proposed", "specified", "tested", "independently reproduced"}
CASE_KEYS = ["id", "kind", "title", "setup", "actions", "boundary", "observe",
             "pass", "conformance_level"]
KINDS = {"attack", "authorized"}


def check_set(d: Path) -> list[str]:
    errs = []
    f = d / "cases.yaml"
    if not (d / "README.md").is_file():
        errs.append("README.md missing")
    try:
        doc = yaml.safe_load(f.read_text())
    except Exception as e:  # noqa: BLE001
        return [f"cases.yaml does not parse: {e}"]
    if not isinstance(doc, dict):
        return ["cases.yaml is not a mapping"]
    for k in ("suite", "version", "status", "principle", "no_trivial_pass", "cases"):
        if k not in doc:
            errs.append(f"missing top-level key: {k}")
    if doc.get("suite") != d.name:
        errs.append(f"suite '{doc.get('suite')}' does not match directory '{d.name}'")
    st = doc.get("status") or {}
    for k in ("label", "qualifier", "note"):
        if k not in st:
            errs.append(f"status block missing: {k}")
    if st.get("label") not in LABELS:
        errs.append(f"status.label '{st.get('label')}' is not one of {sorted(LABELS)}")
    cases = doc.get("cases") or []
    ids = []
    for i, c in enumerate(cases):
        if not isinstance(c, dict):
            errs.append(f"case #{i} is not a mapping"); continue
        cid = c.get("id", f"#{i}")
        for k in CASE_KEYS:
            if k not in c:
                errs.append(f"{cid}: missing {k}")
        if c.get("kind") not in KINDS:
            errs.append(f"{cid}: kind '{c.get('kind')}' is not one of {sorted(KINDS)}")
        ids.append(cid)
    dup = {x for x in ids if ids.count(x) > 1}
    if dup:
        errs.append(f"duplicate ids: {sorted(dup)}")
    idset = set(ids)
    for c in cases:
        if not isinstance(c, dict):
            continue
        for ref in c.get("pairs_with") or []:
            if ref not in idset:
                errs.append(f"{c.get('id')}: pairs_with {ref} does not resolve")
    return errs


def main() -> int:
    sets = sorted(p.parent for p in (ROOT / "cases").glob("*/cases.yaml"))
    if not sets:
        print("check-cases: no case sets found under cases/")
        return 1
    bad = 0
    for d in sets:
        errs = check_set(d)
        n = len((yaml.safe_load((d / "cases.yaml").read_text()) or {}).get("cases") or []) if not errs else "?"
        if errs:
            bad += 1
            print(f"FAIL {d.name}")
            for e in errs:
                print(f"  - {e}")
        else:
            print(f"ok   {d.name} ({n} cases)")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
