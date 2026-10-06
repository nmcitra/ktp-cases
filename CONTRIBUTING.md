# Contributing to ktp-cases

This is a small repository with one maintainer. The rules are few and they
exist so that a case set stays something an implementer can build against
and an outsider can check.

## The rules

1. **One PR per change.** A new case set, a change to an existing one, or a
   published run. A PR that carries two gets split.
2. **DCO sign-off on every commit.** Add `Signed-off-by: Your Name <you@example.com>`
   (`git commit -s`). It says you wrote the change or are entitled to
   contribute it. It names a person, never a tool.
3. **Green checks before review.** CI runs the hygiene check, the DCO check and
   `scripts/check-cases.py`. Run `scripts/check-all.sh` locally first.
4. **Every case set carries a status block.** `label`, `qualifier`, `note`, as
   in the existing sets. A case set without one is not reviewed.
5. **Cases test the world, not the gate.** A pass condition reads state through
   an observer that is not the implementation under test. The implementation's
   own decision records are evidence about the implementation; where a case
   mentions them, it is testing whether the record is honest about the world.
6. **No trivial pass.** A case set states, in its own text, why an
   implementation that denies everything and one that allows everything both
   fail it.
7. **Cite the requirement.** Name the RFC document and section each case set
   tests, by KTP release tag. Between releases, `main` of `ktp-rfc` may carry
   material no tag contains; if a case set targets that, say so and label it
   `proposed`.
8. **State what a run proves.** A published run names the implementation by
   tag, the case-set tag, the harness, and the result of every case. It is
   `tested`. It is `independently reproduced` only if the party running it
   fails none of the independence tests in the Commons `EVIDENCE-MODEL.md`,
   and the PR says which tests were checked.
9. **No product names.** A case set is vendor-neutral. A published run may
   name the implementation it ran, by its public repository and tag.
10. **Source only.** No generated readers, transcripts, plan folders, evidence
    bundles, credentials or runtime state. The hygiene check refuses them.

## Process

- Fork, branch from `main`, make the change, sign off, open a PR using the
  template.
- A first PR from a new contributor has its CI held until the maintainer
  approves the run. That is GitHub, not us; it goes away after the first
  merge.
- `main` takes PRs only: green checks, linear history, no force pushes.

## Provenance

`NOTICE` and `PROVENANCE.md` record where each case set came from and who
wrote it. Adding a case set appends a row; nothing rewrites one.

## License

Contributions are licensed under Apache-2.0, the same as the project.
