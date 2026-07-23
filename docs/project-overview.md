# Project Overview

## Purpose

QSO-DIGITALIS is a candidate documentation and contract surface for exchanging **sanitized, inert evidence references** among QSO portfolio components. Its purpose is under review; no runtime capability is implied by the repository name or by the presence of roadmap files.

## Intended readers

- portfolio architects deciding whether the repository should exist;
- maintainers reviewing scope, ownership, migration, and retirement;
- security, privacy, accessibility, legal, licensing, and release reviewers;
- developers preparing schemas, fixtures, or validators after approval;
- downstream consumer maintainers verifying exact versions and digests.

## Problem statement

Evidence can originate in one repository, be interpreted by another, and be summarized by a third. Without a bounded exchange contract, those transitions can lose provenance, merge incompatible meanings, broaden authority, or make correction and withdrawal incomplete.

The unresolved question is whether QSO-DIGITALIS should provide a neutral envelope for those transitions or whether existing repositories should retain the responsibility directly.

## Candidate responsibility

A valid charter may cover:

- immutable envelope identity and content digests;
- source and interpretation provenance;
- sensitivity, purpose, and retention labels;
- publisher and subscriber capability declarations;
- correction, revocation, supersession, tombstone, and withdrawal references;
- evidence-reference acknowledgments and consumer dispositions;
- exact schema and canonicalization versions;
- migration and rollback records.

## Responsibilities retained elsewhere

| Repository | Responsibility that QSO-DIGITALIS must not absorb |
|---|---|
| QSO-SEEKER | Retrieval, source observation, canonical source tuples, and collection policy |
| QuantumStateObjects | Runtime-local state, execution-local records, and local lifecycle semantics |
| QSO-FABRIC | Experiment orchestration, aggregate evidence, collaboration records, and experiment conclusions |
| qso-field.github.io | Portfolio documentation and non-authoritative governance observations |
| ALISTAIRE repositories | Portfolio-level architectural and governance decisions, subject to their own approvals |

## Maturity

`REVIEW`

The repository has planning controls and a stale PR #2 architecture candidate. It does not yet have an approved charter, accepted schema, compatibility proof, production-quality implementation, release candidate, or deployment authority.

## Success condition

One of two outcomes is acceptable:

1. **Approve a bounded charter:** establish a unique contract role, exact ownership, governance, fixtures, compatibility, migration, and rollback requirements.
2. **Retire or repurpose the repository:** preserve provenance and point readers to the repositories that retain each responsibility.

Continuing indefinitely with an ambiguous name and overlapping scope is not a successful outcome.

## Non-goals

- literal consciousness or sentience claims;
- unrestricted shared memory;
- raw network response or executable-content transport;
- credential, key, payment, settlement, or identity authority;
- autonomous acceptance, publication, or repository mutation;
- replacing source repositories or their canonical records;
- treating a digest, acknowledgment, or CI result as semantic truth or approval.

## Authority and consent boundary

`QSO-CONSENT-CAPACITY-LOCK-v1` applies to all repository content and future interfaces. Documentation review cannot waive explicit, informed, current, revocable consent, human final review, privacy constraints, or the repository's non-operational status.
