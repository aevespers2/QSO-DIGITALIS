# Contract and Repository Boundaries

## Purpose

This document prevents QSO-DIGITALIS from becoming an ambiguous catch-all between source collection, runtime state, experiment evidence, and portfolio governance.

## Proposed record families

The following names are descriptive placeholders only. They are not accepted namespaces or schemas.

| Candidate family | Minimum meaning | Must not imply |
|---|---|---|
| Evidence reference | Immutable pointer to a source-bound record or artifact | Ownership of the source or truth of its content |
| Exchange envelope | Versioned policy and provenance wrapper | Executable payload or unrestricted transport |
| Consumer disposition | Consumer-specific accept, reject, hold, migrate, or withdraw status | Portfolio-wide semantic acceptance |
| Correction reference | Exact link from superseded state to corrected state | Deletion of historical evidence |
| Withdrawal reference | Exact record that current use is prohibited or unsupported | Guaranteed erasure from uncontrolled copies |
| Propagation receipt | Evidence that a controlled consumer processed a lifecycle update | Correct interpretation or successful remediation |
| Migration record | Source and target generations, mapping, omissions, and evidence | Automatic compatibility |
| Rollback record | Restoration target, coverage, validation, and residual risks | Permission to restore stale or revoked authority |

## Repository ownership matrix

| Concern | Primary candidate owner | QSO-DIGITALIS posture |
|---|---|---|
| Source discovery and retrieval | QSO-SEEKER | Reference only; do not duplicate collection authority |
| Source canonicalization tuple | Source repository / QSO-SEEKER | Preserve exact tuple and transformations |
| Runtime-local event and report semantics | QuantumStateObjects | Consume read-only generations only after compatibility review |
| Experiment orchestration and aggregate evidence | QSO-FABRIC | Reference experiment evidence without becoming the experiment authority |
| Public portfolio documentation | qso-field.github.io | Remain subordinate to repository-local accepted sources |
| Architecture and governance decisions | Explicitly appointed decision process | Prepare evidence; never infer acceptance from CI or mergeability |
| Exchange-envelope proposal | QSO-DIGITALIS, if chartered | Remain schema-first, inert, and non-operational |

## Contract acceptance tuple

A future compatibility claim must bind at least:

```text
producer repository and commit
+ source path and blob identity
+ schema identifier and digest
+ semantic profile identifier and digest
+ canonicalization profile and digest
+ namespace and record role
+ fixture generation and digest
+ consumer repository and commit
+ consumer implementation identity
+ correction and withdrawal watermarks
+ migration and rollback generation
+ exact-head evidence
```

Any missing element keeps the relationship `PROPOSED` or `BLOCKED`.

## Gluing conditions

Two locally valid components compose only when their shared boundary agrees on:

- record identity and aggregation level;
- canonical bytes and hashing;
- ordering, duplicate, replay, retry, and conflict semantics;
- correction, revocation, withdrawal, retention, and supersession;
- consumer reachability and acknowledgment;
- migration path and rollback target;
- responsibility and custody without self-authorization.

A pairwise match is insufficient when a third component interprets the same field differently. Triple-overlap witnesses are required for SEEKER → DIGITALIS → QuantumStateObjects/FABRIC paths before portfolio composition can be claimed.

## Current obstruction register

| Obstruction | Status | Closure required |
|---|---|---|
| PR #2 is stale and non-mergeable | OPEN | Preserve useful documentation, supersede stale implementation-bearing changes, and validate a current branch |
| Repository charter is unapproved | BLOCKED | Explicit approve, revise, or retire decision |
| Event-ledger/runtime-report role collision | BLOCKED | Role-specific namespaces, schemas, and ownership |
| Consumer registry absent | BLOCKED | Exact consumer identities, purposes, generations, and lifecycle behavior |
| Correction/withdrawal propagation unproven | BLOCKED | Controlled-route fixtures and receipts |
| License, retention, privacy, and security ownership absent | BLOCKED | Named owners or explicit vacancies and independent review |
| Rollback drill absent | BLOCKED | Synthetic restoration and stale-state rejection evidence |

## Authority boundary

This registry is a documentation aid. It does not assign ownership, accept a contract, register a consumer, authorize implementation, approve a release, publish Pages, or activate any service.
