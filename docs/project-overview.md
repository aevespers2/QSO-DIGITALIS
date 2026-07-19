# Project overview

## Why this repository exists

The QSO portfolio needs an explicit decision about whether a shared evidence-exchange contract is necessary between retrieval, local QSO execution, and experiment evidence assembly. QSO-DIGITALIS is the place where that decision is being evaluated.

The repository is not yet a product. Its current deliverable is an approved, non-overlapping charter or a clear retirement record.

## Problem statement

Without a bounded exchange contract, portfolio components may drift toward incompatible assumptions about:

- how evidence references are identified and versioned;
- which component may publish, discover, read, acknowledge, or revoke a record;
- how purpose, sensitivity, retention, and experiment scope constrain access;
- how provenance links survive replay and downstream use;
- what happens when a schema, hash, capability, or policy does not match.

A separate repository is justified only if it owns these contracts without duplicating retrieval, runtime, experiment, governance, or deployment responsibilities.

## Proposed users

The charter candidate is intended for:

- maintainers defining portfolio contracts;
- QSO-SEEKER developers publishing sanitized evidence references;
- QuantumStateObjects developers consuming read-only scoped views;
- QSO-FABRIC developers recording evidence use in experiment bundles;
- reviewers validating security, privacy, retention, provenance, and compatibility.

It is not intended as an end-user application, a general event bus, a shared-memory layer, or a production messaging service.

## Proposed inputs and outputs

### Inputs

- canonical evidence identifiers and hashes;
- accepted schema and policy versions;
- publisher identity and capability claims;
- topic, purpose, sensitivity, retention, and experiment metadata;
- acknowledgments, revocations, and provenance links.

### Outputs

- validated immutable envelopes or references;
- deterministic acceptance or rejection results;
- capability-scoped read views;
- replayable policy and provenance decisions;
- bounded audit records suitable for downstream evidence bundles.

No raw network response, credential, executable payload, package, binary, archive, or Git object belongs in the proposed contract.

## Success criteria

QSO-DIGITALIS succeeds at the charter stage only when reviewers can answer all of the following:

1. Is the capability necessary?
2. Is its authority unique and narrower than neighboring repositories?
3. Are inputs, outputs, non-goals, and prohibited capabilities explicit?
4. Are security, privacy, retention, revocation, provenance, migration, and rollback requirements testable?
5. Can downstream consumers bind to an exact version and hash?
6. Is retirement defined if the repository is redundant?

## Current phase

The active chain remains P0 charter disposition. Draft PR #2 is a candidate, not an accepted specification. Schema, implementation, integration, release, and deployment work remain blocked until the charter is explicitly approved.
