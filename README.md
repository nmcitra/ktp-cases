# ktp-cases — KTP conformance case sets

The published test cases for the [Kinetic Trust Protocol](https://github.com/nmcitra/ktp-rfc): what an implementation has to get right, written as cases an observer can check against the state of the governed world. The requirements live in the RFCs; the cases live here.

**Maintainer:** Chris Perkins. **Host:** Chris Perkins. See `GOVERNANCE.md`.

**Status: EXPERIMENTAL · review by 2026-12-10.**

Publishing a case set makes a requirement `specified`. It tests nothing. A case becomes `tested` when an implementation runs it and publishes the run; `independently reproduced` when a party that fails none of the independence tests runs it too. The maintainer's own runs are never independent.

## What this repository is

- Case sets, one directory each under `cases/`, each with a `cases.yaml` and a `README.md`. A case set is a contract: given a setup and a sequence of actions, an observer that is not the gate reads the resulting state of the world and the case passes or fails on that state.
- The status of every case set, stated in its own file and never inferred from anything else.
- A structure check (`scripts/check-cases.py`) so a case set cannot be merged with duplicate ids, dangling references or missing fields.

## What this repository is not

- The specification. That is [`ktp-rfc`](https://github.com/nmcitra/ktp-rfc). A KTP release cites this repository at a tag; this repository cites the RFC section each case set tests.
- A runner. Nothing here executes a case. An implementation runs the cases with its own harness and publishes the run; a runner, if one is built, is a separate contribution with its own evidence limits.
- A certification. There is no badge, no seal and no "KTP conformant" claim that this repository issues. A published run says what it ran, against what, and what it got.
- The RFC series' own conformance document (`ktp-conformance`, the Conformance Requirements, Levels, Testing and Certification spec) or the nine JSON suites that ship beside it under `specifications/conformance/`. Those stay in `ktp-rfc`. This repository holds case sets written after v2.1.0; where a case file says "ktp-conformance", it means that document, and cites its levels and test ids.

## Status labels

Every case set carries one of these in its `status` block. The qualifier is part of the label.

| Label | Meaning |
|---|---|
| `proposed` | The cases are on a branch or in a PR. The requirement they test is not yet in a KTP release. |
| `specified` | The cases are published here at a tag and the requirement is in a KTP release. **No one has run them.** The qualifier reads `not yet tested`. |
| `tested` | At least one implementation has run the cases and published the run, by PR to this repository, with the implementation's tag and the results. |
| `independently reproduced` | A second party has run them too, and that party fails none of the independence tests in the Open Trust Commons [`EVIDENCE-MODEL.md`](https://github.com/nmcitra/otcs/blob/main/EVIDENCE-MODEL.md): no shared founders or funders, no advisory or reciprocal-review relationship, no employment or contractor status, no code contributed, no commercial dependency, no substantial prior collaboration. |

A label only moves forward by PR, with the evidence attached. It never moves because time passed.

## Case sets

| Directory | Tests | Status |
|---|---|---|
| `cases/consequence-boundary-attack-set/` | The consequence boundary: authority holders, limits, composition, concurrency, acknowledgement and route, under one refund workflow. 21 cases: 15 attack, 6 authorized. | `specified`, not yet tested |

## Running the checks

```sh
bash scripts/check-all.sh
```

Runs what CI runs: hygiene, DCO sign-off on commits not yet on `main`, and the case-set structure check. The structure check needs PyYAML (`python3 -m pip install pyyaml`).

## Contributing

Read [`CONTRIBUTING.md`](CONTRIBUTING.md). Short version: one PR per change, DCO sign-off on every commit, green checks, a status block on every case set, and no claim a run does not support.

## License

Apache-2.0. See `LICENSE` and `NOTICE`.
