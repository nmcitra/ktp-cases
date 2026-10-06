# Versioning

Tags are the version. `main` is where the case sets live.

## Tags

Bare, numeric, semantic: `vMAJOR.MINOR.PATCH`. **A published tag is never moved or deleted.** A mistake in a tagged case set is fixed by a new tag that says so.

Before `v1.0.0`, minors may restructure: `0.y.z` means no case set has yet been run. **`v1.0.0` is reserved for the first tag at which a case set carries a published run** and says so in its release notes.

## What a tag carries

A GitHub Release with notes stating which case sets it contains, the status label of each, which KTP release each tests, and what the tag does not prove.

## Pinning

A KTP release cites this repository by tag, never by branch. An implementation that publishes a run names the case-set tag it ran. Between tags, `main` may carry material no tag contains; a run against `main` names the exact commit and is labelled accordingly.

## Case-set versions

Each `cases.yaml` carries its own `version`. Adding a case is a minor bump of the set; changing a pass condition is a major bump of the set, because every published run against the old condition stops being evidence for the new one.
