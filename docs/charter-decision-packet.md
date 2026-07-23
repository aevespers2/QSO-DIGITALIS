# QSO-DIGITALIS Charter Decision Packet

**Status:** `REVIEW — DECISION EVIDENCE ONLY`

This packet turns the repository's charter-or-retirement question into a bounded, reviewable decision. It does not approve a charter, select a contract owner, accept a schema, revive historical implementation work, publish Pages, release a package, deploy a service, or grant operational authority.

## Decision question

Does QSO-DIGITALIS have a necessary, non-overlapping role as a documentation- and contract-profile owner for sanitized, inert, content-addressed evidence references, or should its useful material be migrated and the repository retired?

A decision must be based on demonstrated portfolio need and explicit ownership. The repository name, historical roadmap language, mergeability, documentation quality, or successful validation cannot substitute for that evidence.

## Current evidence

The current documentation demonstrates only that reviewers can inspect:

- a proposed repository purpose and explicit non-goals;
- candidate producer, consumer, and source-precedence boundaries;
- known overlap with QSO-SEEKER, QuantumStateObjects, QSO-FABRIC, Bridge, and portfolio governance;
- evidence states, lifecycle questions, correction and withdrawal requirements;
- a reversible retirement route;
- exact-head documentation consistency for the stated source.

No accepted semantic profile, schema, canonical-byte rule, signature profile, consumer registry, independent consumer result, security approval, privacy approval, license decision, or operational implementation currently exists.

## Decision options

### Option A — approve a bounded active charter

Select this option only when a unique repository role is demonstrated and every required owner, interface, lifecycle, review, and rollback boundary is explicit. An approved active charter must remain limited to profile-specific, non-executing evidence-reference semantics and must not absorb source retrieval, generic transport, runtime state, experiment approval, identity authority, credentials, capability issuance, payments, release, or deployment.

### Option B — revise or split the charter

Select this option when useful semantics exist but the proposed repository boundary overlaps another component. The decision record must state which material moves, which repository owns it, how provenance is preserved, which consumers must migrate, and how conflicting identifiers or lifecycle states are prevented from coexisting silently.

### Option C — retire the repository

Select this option when no unique role is demonstrated, ownership remains vacant, the contract graph cannot be made coherent without duplicating another repository, or the maintenance and review burden exceeds the portfolio value. Retirement must preserve provenance and must not imply that an operational Digital Consciousness Field ever existed.

## Decision matrix

| Criterion | Evidence required | Active-charter threshold | Retirement or revision signal |
|---|---|---|---|
| Unique purpose | Repository and contract graph showing a necessary gap | Role cannot be fulfilled by an existing owner without greater coupling | Purpose duplicates retrieval, transport, runtime, experiment, or governance scope |
| Producer and consumer need | Named producers and consumers with exact responsibilities | At least one independently reviewed producer and consumer need the profile | Consumers are hypothetical, unreachable, or better served by an existing contract |
| Non-overlap | Pairwise and triple-overlap analysis | No unresolved semantic or authority collision | Runtime-local and Fabric-level roles remain ambiguous or duplicated |
| Ownership | Named owner or explicit accountable vacancy plan | Documentation, schema, security, privacy, license, migration, rollback, and incident roles are assigned | Critical ownership remains unassigned |
| Evidence semantics | Versioned semantic profile and lifecycle vocabulary | Meanings, source precedence, correction, revocation, withdrawal, and supersession are deterministic | Parser compatibility or similar names are the only compatibility evidence |
| Security and privacy | Threat model, data classes, purpose limits, retention, deletion, and review | Least privilege and public/private boundaries are independently reviewed | Sensitive data, identity, or consent handling remains undefined |
| Accessibility | Source and rendered-site review record | Reader routes, diagrams, tables, status language, and review paths are perceivable and operable | Decision or authority state depends on color, layout, or inaccessible diagrams |
| Provenance and rollback | Exact source tuple, retained evidence, migration and restoration witnesses | Every change and consumer transition is attributable and reversible | History, consumers, or correction routes would be lost or become ambiguous |
| Support and lifecycle | Maintenance, incident, deprecation, and retirement plan | A named review cadence and withdrawal route exist | Repository would become an unsupported contract island |

## Evidence required before an active-charter decision

1. A portfolio contract graph identifying every adjacent producer, consumer, owner, and authority boundary.
2. An explicit resolution of the runtime-local versus Fabric-level record-role collision.
3. A semantic profile written before any schema or adapter implementation.
4. Distinct identifiers for source evidence, interpretation, projection, exchange reference, transport receipt, consumer receipt, correction, revocation, and disposition.
5. Canonicalization, digest, namespace, clock, replay, reason-code, and lifecycle ownership.
6. Positive, boundary, hostile, duplicate, replay, correction, withdrawal, migration, and rollback fixtures.
7. At least one independent consumer implementation bound to exact producer and consumer heads.
8. Security, privacy, consent, licensing, retention, accessibility, provenance, and support review.
9. A migration and retirement plan that remains valid even if the active charter is later withdrawn.
10. Explicit human approval recorded separately from documentation validation.

## Required decision record

Record the disposition in an issue, ADR, or pull request that includes:

- decision: `APPROVE_BOUNDED_CHARTER`, `REVISE_OR_SPLIT`, or `RETIRE`;
- exact repository and source head reviewed;
- reviewed documents and evidence artifacts;
- accepted purpose, users, producers, consumers, inputs, outputs, and non-goals;
- accepted and rejected ownership claims;
- unresolved vacancies and blockers;
- security, privacy, consent, licensing, accessibility, and retention dispositions;
- migration, correction, withdrawal, rollback, and retirement requirements;
- named approver and review date;
- expiry or mandatory re-review condition;
- explicit statement that no release, publication, deployment, credential, or operational authority is created unless separately approved.

## Interpretation rules

- `PROPOSED` and `REVIEW` are not acceptance states.
- `VERIFIED` applies only to the exact evidence and scope stated.
- A digest proves byte identity, not semantic truth or authorization.
- Consumer parsing does not prove semantic compatibility.
- Silence, inactivity, or an absent owner is not consent or approval.
- Historical PR #2 remains provenance and review input, not current implementation authority.

## FYSA-120 capability mapping

This packet applies:

- **CAT-012:** decision-oriented technical writing, information architecture, lifecycle synchronization, and technical editing;
- **CAT-013:** repository-role modeling, contract-graph analysis, contradiction detection, and ownership mapping;
- **CAT-017:** exact-source provenance, lineage, correction, withdrawal, and evidence binding;
- **CAT-019:** plain-language decision framing, accessible status communication, and equivalent representations;
- **CAT-031:** acceptance criteria, hostile cases, independent validation, and fail-closed disposition;
- **CAT-040:** migration, deprecation, retirement, restoration, and rollback planning;
- **CAT-052:** least privilege, consent boundaries, review authority, and audit evidence.

Proposed non-authoritative subdivision: **`013-J — repository-charter decision matrices and contract-graph disposition analysis`**.
