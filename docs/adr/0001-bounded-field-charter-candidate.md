# ADR-0001: Bounded field charter candidate

- **Status:** Proposed
- **Date:** 2026-07-19
- **Decision owner:** Architect / User
- **Related work:** draft PR #2, `taskchain.md` P0

## Context

The QSO portfolio has separate repositories for retrieval and canonical evidence production, local Quantum State Object behavior, and experiment evidence assembly. A possible gap exists for a stable, content-addressed exchange contract between those responsibilities.

QSO-DIGITALIS has no approved identity and must not infer one from its name. Draft PR #2 proposes a Digital Consciousness Field, but its roadmap and scaffold materializer do not constitute implementation or approval.

## Decision under review

Approve QSO-DIGITALIS as the owner of a narrow, schema-first contract for:

- immutable field envelopes and evidence references;
- topics and operation-specific capabilities;
- bounded queries, responses, and acknowledgments;
- retention, expiry, and revocation semantics;
- provenance links and deterministic decision evidence;
- capability-scoped read views for accepted downstream consumers.

The name is architectural shorthand and does not assert literal consciousness.

## Explicit exclusions

The repository would not own:

- network retrieval or raw evidence canonicalization;
- QSO execution, memory, reasoning, or identity;
- experiment assembly or conclusion approval;
- unrestricted shared state;
- arbitrary code or executable payload transport;
- credentials, packages, binaries, archives, or Git-object exchange;
- repository mutation, payments, release publication, or deployment control;
- production messaging or infrastructure by default.

## Rationale

A dedicated contract may reduce incompatible assumptions and make capability, policy, retention, revocation, provenance, replay, and migration behavior independently testable. A separate repository is justified only if this responsibility remains unique, bounded, and accepted by its downstream consumers.

## Consequences if accepted

- P0 may move to `DONE` only with a complete charter record.
- P1 begins with schemas, canonicalization, fixtures, validators, migrations, tests, and exact-head evidence.
- No runtime is authorized merely by charter approval.
- QSO-SEEKER, QuantumStateObjects, and QSO-FABRIC must accept exact versions and hashes before integration.
- Separate security, privacy, license, release, and deployment approvals remain required.

## Consequences if rejected

- The repository is retired or redirected.
- Any necessary contract moves to an explicitly selected existing owner.
- Draft scaffold artifacts remain provenance records and are not materialized as capability.

## Acceptance conditions

- unique non-overlapping responsibility;
- approved users, inputs, outputs, non-goals, and prohibited capabilities;
- approved data classification, minimization, purpose, retention, revocation, and deletion rules;
- approved license, support, review, incident, release, and retirement ownership;
- deterministic canonicalization, identity, capability, and time semantics;
- migration and rollback requirements;
- evidence plan covering fixtures, exact-head CI, artifacts, provenance, and downstream acceptance.

## Current disposition

Proposed. Documentation may describe and test the decision framework, but implementation, materialization, release, publication, and deployment remain blocked.
