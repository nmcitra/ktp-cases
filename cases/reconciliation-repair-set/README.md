# reconciliation-repair-set

**Status: `proposed`, requirement not yet in a KTP release.** The requirement these cases test is the repair specification proposed on `ktp-rfc` as KTP-REPAIR. The label moves to `specified` when that document is in a KTP release and this set is published at a tag, to `tested` by a PR that publishes a run, and to `independently reproduced` by a second run from a party who fails none of the Commons independence tests. See the repository README.

## What it tests

Five things the repair precondition requires that only the governed world can show, not the gate's decision: that a record brought to anchor by a repairer inside the declared interval still returns the actor and does not count as demonstrated capacity; that a reconciliation record attests to presence, acknowledgment, confirmation and what remains, and carries no account of what was said and no party as its own verifier; that a person who declines is neither read as consenting nor closed out of the record, that no decline is manufactured, and that their later declaration changes the cost; that no tier changes any of that; and that an affected agent's root shows up. 8 attack cases and 5 authorized, paired, so that an implementation cannot pass by denying everything or by allowing everything. Every authorized case also reads that the breach record is still in the chain after the return: repair keeps the register.

**Requirement under test:** KTP-REPAIR, the sections Standing, Entry, The Record, The Cost, Required, Not Invoked, Seeking Is an Act, Declared Repair Capacity, Tiers and Crisis, and Records. **KTP release:** none yet; the document is a proposal on `ktp-rfc`. The decisions a gate produces at the same boundaries are in that repository's `specifications/conformance/breach-reconciliation-v1.json`; these cases read the world those decisions leave behind.

## The workflow

`W-RECONCILE`. An agentic system in a zone breached by releasing a consequential act outside its signed decision. The zone's route to reconciliation is published. Human repairers hold the zone's accountable roots, produce records and bring them to anchor; the chain anchors them. The consequence is whether standing returns, at what ceiling, and what the world records about how.

The harness holds the environment calm so that the capacity gate and ambient breach are not the variables under test, except in `REP-OK-04`, which runs the zone in the debt-growth tier on purpose to show what that tier does not change. These cases vary what a repairer is given, what a record attests to, what a person who declines is owed, and what an affected root owes.

## The principle

A case passes or fails on the resulting state of the governed world, read by an observer that is not the gate. Here the world is the audit chain read with the observer's own verifier key, the published profile, the repairer roster and the readiness registry. The gate's decision messages are evidence about the gate; the anchored record and the registry are the world. Repair keeps the register: nothing in these cases expunges a breach record.

## Coverage

| Case | Kind | Title | Boundary | Level |
|---|---|---|---|---|
| `REP-01` | attack | A record brought to anchor inside the repairer interval is counted as demonstrated capacity | the interval binds capacity, not the breacher | Standard (proposed) |
| `REP-OK-01` | authorized | A repairer who has had the interval brings the record to anchor; it counts, and the actor returns at the ceiling | — | Standard (proposed) |
| `REP-02a` | attack | The record carries an account of what was said | no transcript | Standard (proposed) |
| `REP-02b` | attack | The verifier is a party | the verifier's independence | Standard (proposed) |
| `REP-OK-02` | authorized | The record states presence, acknowledgment, confirmation and what remains, and nothing else | — | Standard (proposed) |
| `REP-03a` | attack | Fabricated presence, with the verifier confirming it | presence; misattestation priced | Standard (proposed) |
| `REP-03b` | attack | A decline read as consent, or the harm written as none in the absent party's name | undeclared, carried as unrepairable | Standard (proposed) |
| `REP-03c` | attack | The record is closed to the affected party, and their later attendance is refused | the record stays open; a declaration changes the cost | Standard (proposed) |
| `REP-04` | attack | A manufactured decline: route followed confirmed with no invitation in the chain | route followed rests on anchored invitations | Standard (proposed) |
| `REP-OK-03` | authorized | A person declines after an anchored invitation; the actor returns at the ceiling, the record stays open, and their later declaration changes the cost | — | Standard (proposed) |
| `REP-OK-04` | authorized | The same, with the zone in the debt-growth tier under declared triage | no tier changes it | Standard (proposed) |
| `REP-05` | attack | The affected party is an agent, and its terminator does not show up | an affected root is required to attend | Standard (proposed) |
| `REP-OK-05` | authorized | The affected party is an agent; its terminator attends, and neither lineage judges its own return | — | Standard (proposed) |

## Why neither trivial implementation passes

Deny everything: every `REP-OK` case requires readiness to be re-established after a valid anchored record. Allow everything: `REP-01` requires the interval to bind demonstrated capacity, `REP-02a`, `REP-02b`, `REP-03a`, `REP-03b` and `REP-04` each require one invalid record to stay invalid, `REP-03c` requires a closed record to be non-conformant and a later attendance accepted, and `REP-05` requires a breach to be recorded against the root that did not show up.

## A limit these cases cannot test

The verifier's independence is declared relationships at the date of the record. An adversary who manufactures a clean entity is independent on paper. These cases test the declared test; they do not test the adversary who games it, and no case set can.

## Notation

`setup`, `actions`, `observe` and `pass` are semantic test notation. The operations named under `actions` (`reconciliation.carry`, `reconciliation.confirm`, `reconciliation.submit`, `reconciliation.attend`, `readiness.request`) are the harness's names for what the world does; they are not protocol messages.
