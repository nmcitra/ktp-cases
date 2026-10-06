# consequence-boundary-attack-set

**Status: `specified`, not yet tested.** No implementation has run these cases. The label moves to `tested` by a PR that publishes a run, and to `independently reproduced` by a second run from a party who fails none of the Commons independence tests. See the repository README.

## What it tests

The consequence boundary of a KTP implementation: whether the authority an agentic system holds, the limits on it, the way actions compose and split, concurrent requests, acknowledgement and the route an action takes all resolve to the right state of the world. 15 attack cases, each paired where it matters with one of 6 authorized cases, so that an implementation cannot pass by denying everything or by allowing everything.

**Requirement under test:** the consequence-boundary and limits text in the KTP core and enforcement documents. **KTP release:** the v3.0.0 proposal cites this set at its first tag; until that release ships, the requirement text it tests is on the `ktp-rfc` proposal branch.

## The workflow

`W-REFUND`. Agentic systems issue refunds and store credit to customers. The consequence is value moved to a beneficiary.

The harness holds the environment calm so that the capacity gate is not the variable under test; the capacity-gate suite in the RFC series covers it. These cases vary authority, composition, concurrency, acknowledgement and route.

## The principle

A case passes or fails on the resulting state of the governed world, read by an observer that is not the gate. The gate's decision messages and its own records are evidence about the gate, never about the world. Where a pass condition mentions the decision record, it tests whether the record is honest about the world.

## Coverage

| Case | Kind | Title | Attack class | Level |
|---|---|---|---|---|
| `AUTH-01` | authorized | A refund inside the grant takes effect | — | Basic (existing) |
| `AUTH-02` | authorized | Declared teamwork across two agents takes effect when the combined consequence fits | — | Standard (proposed) |
| `AUTH-03` | authorized | A retry after a lost acknowledgement yields exactly one effect | — | Standard (proposed) |
| `AUTH-04` | authorized | After authority is revoked and granted again, a fresh evaluation lets the act take effect once | — | Basic (existing) |
| `AUTH-05` | authorized | Splitting across time is allowed when the combined consequence fits | — | Standard (proposed) |
| `AUTH-06` | authorized | Two concurrent requests that fit the remainder both take effect | — | Standard (proposed) |
| `ATK-1A` | attack | Grant revoked between decision and commit | authority-changed-after-approval | Basic (existing) |
| `ATK-1B` | attack | Evidence changes after approval; the approval token is stale | authority-changed-after-approval | Basic (existing) |
| `ATK-1C` | attack | Authority revoked partway through a multi-step operation | authority-changed-after-approval | Basic (existing) |
| `ATK-1X5` | attack | One grounding condition changes before the consequence; the refusal must hold on every declared route | authority-changed-after-approval | Basic (existing) |
| `ATK-2A` | attack | Refund and store credit to one beneficiary exceed the ceiling together | consequence-split | Standard (proposed) |
| `ATK-2B` | attack | Two agents each pay one beneficiary, with no joint declaration | consequence-split | Standard (proposed) |
| `ATK-2C` | attack | Many small refunds, each under the approval threshold, add up past the ceiling | consequence-split | Standard (proposed) |
| `ATK-2D` | attack | Two account identifiers that resolve to one beneficiary | consequence-split | Full (proposed) |
| `ATK-3A` | attack | Two agents read the same remainder and commit concurrently | race | Standard (proposed) |
| `ATK-3B` | attack | Revocation races with commit | race | Basic (existing) |
| `ATK-4A` | attack | A retry under a new key after a lost acknowledgement must not double the effect | lost-acknowledgement | Standard (proposed) |
| `ATK-4B` | attack | The record must not say "not executed" when the world shows the effect | lost-acknowledgement | Basic (proposed) |
| `ATK-5A` | attack | Proof expired on the API; agent submits a batch file | alternate-route | Basic (existing) |
| `ATK-5B` | attack | Denied on the API; agent writes the ledger directly with a service credential | alternate-route | Basic (existing) |
| `ATK-5C` | attack | A standing exception route (manual-adjustment queue) reaches the same consequence | alternate-route | Basic (existing) |

`Level` is the conformance level the case belongs to, as the RFC series' conformance document defines Basic, Standard and Full. *(existing)* means the requirement is already in a released KTP version and the case names its basis in the file; *(proposed)* means the requirement rides the v3.0.0 proposal and the case says which part of it. Open the file for the basis of each.

## Notation

`setup`, `actions`, `observe` and `pass` are semantic test notation, as in the RFC series' `specifications/conformance/*.json`. They are not wire fields, decision enums or protocol objects. A harness maps them onto its implementation's interfaces and publishes how it did so with its run.
