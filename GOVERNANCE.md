# Governance

How this repository is run, who does what, and when the arrangement is reviewed.

## Roles

| Role | Who | What it means |
|---|---|---|
| **Maintainer and owner of record** | Chris Perkins | Reviews and merges contributions, cuts releases, speaks for the repository in the Open Trust Commons. The only owner. |
| **Host** | Chris Perkins | Controls the GitHub account the repository lives under, keeps the protection rules and CI running, approves first-time contributors' CI runs. |
| **Contributor** | Anyone | Proposes case sets, corrections and published runs by DCO-signed pull request. |

One owner, by design. A conformance repository is a yardstick, and a yardstick with several hands on it is not yet a yardstick. The arrangement is revisited when the first independent reproduction exists; see below.

## How the maintainer changes

By the maintainer's own commit naming a successor, or, if the maintainer is unreachable, by the inactivity rule below.

## Inactivity

If no maintainer commit, review or release lands for **180 days**, the repository's Commons state becomes `UNMAINTAINED` on that day, by the calendar and not by anyone's hand. The repository stays public and forkable. A returning maintainer clears it with one commit.

## Independence, stated plainly

The maintainer is the author of the specification these cases test. That disqualifies the maintainer from supplying independent evidence about it. So does contributing to it. "Independent" here means what the Open Trust Commons means: a party who fails none of `EVIDENCE-MODEL.md`'s tests (no shared founders or funders, no advisory or reciprocal-review relationship, no employment or contractor status, no code contributed, no commercial dependency, no substantial prior collaboration) running a published case set against a tagged implementation and publishing the run. Until such a run exists, every case set here is at most `tested`, `independent_validation` in `otcs.yaml` is 0, and the number is the honest one.

## Co-maintainers

None now. The question reopens on the day the first `independently reproduced` label lands, because that is the first day a second hand on the yardstick would be something other than the author's.

## Review of this arrangement

Reviewed on **2026-12-10**. On that day the maintainer confirms, in this file, that the arrangement still serves the protocol, or reopens the question. Nothing here is permanent by default; a review date that passes without a line added here is itself a finding.

## Changing this file

By PR, one review, like everything else.
