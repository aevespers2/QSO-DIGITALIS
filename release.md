# Release Plan

## Current decision

Status: `BLOCKED — DOCUMENTATION CANDIDATE IN REVIEW; CHARTER, CONTRACT, SECURITY, PRIVACY, LICENSE, PROVENANCE, MIGRATION, ROLLBACK, AND APPROVAL REQUIRED`

QSO-DIGITALIS has no eligible runtime or package release. Current work is limited to a Pages-ready documentation source and exact-head documentation validation that clarify the charter-or-retirement decision.

Historical PR #2 proposed a bounded Digital Consciousness Field architecture and scaffold materializer. It is stale relative to current `main`, currently non-mergeable, and must not be treated as a current release or implementation candidate.

## Versioning

- No SemVer release begins before explicit charter approval.
- A documentation snapshot could later use `0.0.1-docs.1` only after publication approval and resulting-state verification.
- A contract candidate could later use `0.1.0-alpha.1` only after accepted semantics, schemas, canonicalization, namespaces, fixtures, validators, security/privacy/license review, consumer evidence, migration, and rollback exist.
- Mutable version aliases are prohibited for compatibility claims.
- Retirement documentation must not imply that a runtime ever existed.

## Current documentation scope

- project overview and reader routes;
- architecture and trust boundaries;
- accessible diagram plus equivalent prose;
- repository and contract responsibility map;
- safe onboarding and developer guidance;
- planning, release, punch-list, and changelog alignment;
- deterministic link, structure, evidence-state, authority-boundary, and planning validation;
- retained exact-head evidence.

## Explicitly excluded

- approving the Digital Consciousness Field charter;
- merging or reviving stale PR #2 implementation-bearing changes;
- running a scaffold materializer with write mode;
- accepting namespaces, schemas, semantic profiles, adapters, or consumers;
- network transport, credentials, signing, persistent storage, scheduling, repository writes, payments, settlement, autonomous decisions, or production infrastructure;
- Pages publication, package release, deployment, or operational use;
- literal consciousness, sentience, awareness, or independent-authority claims.

## Release gates

| Gate | Status | Requirement |
|---|---|---|
| Documentation structure | REVIEW | Required reader routes, headings, planning files, links, diagram prose, and authority notices pass at the final exact head. |
| Charter/retirement disposition | BLOCKED | Explicitly approve, revise, or retire the repository and disposition stale PR #2. |
| Non-overlap architecture | BLOCKED | Distinguish source retrieval, exchange metadata, runtime-local state, experiment evidence, portfolio documentation, and governance. |
| Contract semantics | NO EVIDENCE | Accepted semantic profiles, schemas, canonicalization, namespaces, reason codes, fixtures, and lifecycle rules exist. |
| Consumer compatibility | NO EVIDENCE | Exact producer/consumer tuples and independent semantic witnesses pass, including triple-overlap cases. |
| Security and privacy | BLOCKED | Threat model, data classes, purpose limits, least privilege, retention, correction, withdrawal, and independent review are approved. |
| Accessibility | REVIEW | Documentation uses descriptive routes and equivalent prose; a rendered-site review remains required before publication. |
| Licensing | BLOCKED | Repository, documentation, examples, schemas, and dependencies have an approved license and attribution plan. |
| Provenance | PARTIAL | Source history is preserved; final exact-head workflow and retained-artifact evidence are still required. |
| Migration and rollback | BLOCKED | Stale-candidate supersession, consumer migration, repository retirement, redirect/archive, and restoration paths are proven reversible. |
| Publication | BLOCKED | Separate Pages approval, source settings, build evidence, and resulting public-state verification are required. |
| Release and deployment | BLOCKED | Separate explicit approvals are required after every preceding gate passes. |

## Required evidence

For the documentation milestone:

- exact submitted head;
- deterministic validator and hostile-regression results;
- internal-link and required-route report;
- source hashes for documentation, planning files, validator, tests, and workflow;
- clean-tree evidence;
- retained artifact with expiration;
- pull-request disposition and resulting-head verification if merged.

For any future contract or implementation milestone:

- accepted semantic and schema manifests;
- canonical byte and digest profiles;
- positive and hostile fixtures;
- independent consumers;
- security, privacy, licensing, accessibility, and retention reviews;
- migration, correction, withdrawal, and rollback witnesses;
- source artifacts, checksums, SBOM where applicable, provenance, and approval.

## Rollback and withdrawal

Roll back a documentation candidate when it broadens scope, hides an unresolved vacancy or conflict, loses source provenance, introduces broken routes, lacks accessible alternatives, or represents CI as approval. Restore the prior supported documentation state or mark the candidate withdrawn; do not restore stale implementation claims.

A future contract rollback must preserve historical identity while preventing unsupported consumers, revoked access, withdrawn claims, expired evidence, or incompatible generations from becoming current again.

## Unresolved blockers

- explicit charter or retirement decision;
- disposition of stale PR #2;
- runtime-local versus Fabric-level record-role collision;
- namespace, schema, semantic, documentation, security, privacy, licensing, retention, migration, and rollback ownership;
- accepted consumer registry and compatibility evidence;
- correction/withdrawal propagation and rollback drill;
- publication, release, and deployment approval.

## Release log

- 2026-07-16 — Reclassified the repository as a charter-or-retirement decision.
- 2026-07-17 — Recorded PR #2 as the first charter candidate without authorizing implementation.
- 2026-07-23 — Classified PR #2 as stale/non-mergeable and began a current documentation-only front door; publication and implementation remain blocked.
