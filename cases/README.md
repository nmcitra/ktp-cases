# Case sets

One directory per case set. Each holds:

- `cases.yaml` — the cases, with `suite`, `version`, a `status` block, `principle`, `no_trivial_pass`, and the list under `cases`.
- `README.md` — what the set tests, which RFC section and KTP release, the workflow it runs under, a coverage table, and the status label stated in prose.

## Adding a case set

1. One PR. The set's `suite` matches its directory name.
2. The status block is required. A new set enters as `proposed` if the requirement is not yet in a KTP release, or `specified` if it is. Neither says anyone has run it.
3. The set states, in its own text, why an implementation that denies everything and one that allows everything both fail.
4. Every pass condition reads the world through an observer that is not the implementation under test.
5. `scripts/check-cases.py` is green.
6. `PROVENANCE.md` gets a row.

## Publishing a run

One PR. It names the case-set tag, the implementation by public repository and tag, the harness, and the result of every case. It moves the label to `tested`. It moves the label to `independently reproduced` only if the PR states which of the Commons `EVIDENCE-MODEL.md` independence tests were checked, and the party running it fails none of them.

## Notation

`setup`, `actions`, `observe` and `pass` are semantic test notation, as in the RFC series' `specifications/conformance/*.json`. They are not wire fields, decision enums or protocol objects. A harness maps them onto its implementation's interfaces.
