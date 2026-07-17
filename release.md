# Release Plan

## Current Decision

Status: `BLOCKED — DRAFT PR #2 CHARTER DISPOSITION, CONTRACT EVIDENCE, SECURITY, PRIVACY, PROVENANCE, AND APPROVAL REQUIRED`

QSO-DIGITALIS now has one concrete draft charter candidate in PR #2. The pull request is open, draft, mergeable, and currently points to head `46dea012b63e4652bf845d344128797cda804d16`. It proposes a bounded Digital Consciousness Field architecture, a roadmap manifest, and a deterministic scaffold materializer for capability-scoped, content-addressed evidence exchange among QSO-SEEKER, QuantumStateObjects, and QSO-FABRIC.

The candidate is architecture/scaffold only. It does not contain accepted field schemas, deterministic fixtures, tests, CI evidence, security/privacy/license review, migration/compatibility proof, downstream consumer acceptance, provenance, rollback evidence, or deployment approval. The materializer must remain dry-run/inert; generated placeholder files must not be treated as implementation.

## Versioning

- Semantic Versioning begins only after P0 charter approval.
- First possible documentation candidate: `0.0.1-charter.1`.
- First contract candidate: `0.1.0-alpha.1`, only after accepted schemas, policies, fixtures, tests, CI, security, provenance, and rollback evidence exist.
- Envelope, topic, capability, query/response, acknowledgment, revocation, provenance-link, evidence-reference, retention, and replay versions must be explicit and hash-verifiable.
- Incompatible field, authority, retention, revocation, canonicalization, or storage changes require migrations and coordinated downstream fixtures.
- Retirement must not imply runtime capability.

## Release Scope

### Charter candidate

- Purpose, users, evidence-envelope inputs/outputs, publisher/subscriber capability separation, non-goals, trust/data/privacy/license/retention boundaries, repository relationships, verification strategy, migrations, rollback, and retirement criteria.
- Explicit distinction between architectural naming and literal-consciousness claims.
- Explicit exclusion of raw network responses, credentials, packages, binaries, Git objects, unrestricted shared memory, implicit trust, autonomous approval, repository writes, payments, and production infrastructure.

### Later contract candidate

- Charter-approved schemas and policies for field envelopes, topics, capabilities, queries/responses, acknowledgments, revocations, provenance links, evidence references, sensitivity, purpose limitation, retention, human review, and tamper detection.
- Positive, negative, boundary, revocation, expiry, replay, duplicate, malformed, cross-QSO isolation, and version/hash mismatch fixtures.
- One bounded local in-memory/filesystem reference implementation only after contract acceptance.
- Read-only downstream compatibility with accepted QSO-SEEKER, QuantumStateObjects, and QSO-FABRIC contracts.

### Explicitly excluded from the first candidate

- Running the scaffold materializer with `--write` as evidence of implementation.
- Network transport, credentials, signing authority, persistent multi-user service, schedules, external storage, autonomous decisions, unrestricted shared state, or production deployment.
- Any literal consciousness, awareness, sentience, or independent authority claim.

## Selected Candidate Work

Draft PR #2 is selected only as the P0 charter candidate. It may move from `REVIEW` to an accepted charter only after explicit user and Architect disposition, non-overlap analysis, threat/privacy/license/retention review, and a complete lifecycle/rollback decision. No implementation or release candidate is selected.

## Planned Changelog Entries

- `Documentation`: approved DCF charter or retirement notice, repository responsibility map, trust/privacy/retention/license boundaries, and downstream contract roles.
- `Added`: accepted field schemas, policies, deterministic fixtures, validators, and bounded local reference path only after approval.
- `Security`: capability separation, purpose/sensitivity filtering, retention/revocation, tamper detection, cross-QSO isolation, non-executable records, least privilege, and fail-closed version/hash checks.
- `Release`: source artifacts, reports, SBOM where applicable, checksums, provenance, migrations, rollback evidence, downstream acceptance, and approval.

## Acceptance Gates

| Gate | Status | Requirement |
|---|---|---|
| Charter/retirement disposition | REVIEW | Explicitly approve, revise, or reject draft PR #2; establish unique scope and authority boundaries. |
| Non-overlap/architecture | FAIL | Distinguish DCF contract ownership from QSO-SEEKER retrieval/canonicalization, QuantumStateObjects runtime, QSO-FABRIC experiment evidence, and Repository `0` governance proposals. |
| Task completion | FAIL | P0 is `DONE`; implementation requires P1-P3 with linked immutable evidence. |
| Schemas/contracts | NO EVIDENCE | Versioned schemas, policies, migrations, fixtures, negative cases, and hashes validate deterministically. |
| Tests/determinism | NO EVIDENCE | Exact-head tests cover canonicalization, capabilities, retention, revocation, replay, tamper, isolation, and version/hash mismatch. |
| Security | NO EVIDENCE | No implicit trust, raw/executable transport, credential path, unrestricted shared memory, autonomous authority, or external mutation exists. |
| Documentation | PARTIAL | Draft architecture and roadmap exist; approved charter, operations, limitations, compatibility, and recovery do not. |
| Privacy/license/retention | BLOCKED | Data classes, purpose limitation, retention, revocation, public/private boundaries, source terms, and notice/license model require approval. |
| Provenance | PARTIAL | PR and head identity are recorded; no exact-head artifacts, reports, checksums, SBOM, attestation, or downstream acceptance exist. |
| Deployment readiness | BLOCKED | No runtime/storage/transport target is authorized; first target must be disposable, local, credential-free, network-disabled, and fixture-only. |
| Approval | PENDING | Separate charter, merge, release, and deployment approvals are required. |

## Artifact Requirements

- Approved charter or retirement notice in source and rendered form.
- Architecture responsibility/non-overlap map and versioned contract/migration register.
- For implementation: schemas, policies, fixtures, validators, positive/negative/adversarial/replay/revocation/isolation tests, exact-head CI logs, security/privacy/license reports, source artifact, SBOM where applicable, checksums, provenance, downstream compatibility, health/observability, rollback, and post-validation evidence.

## Deployment Readiness, Health, Observability, Rollback, and Post-Validation

No deployment is authorized. A future first target must be a disposable local in-memory/filesystem verification environment with synthetic non-sensitive records, no credentials, no network, no external repository writes, no generated-code execution, explicit human controls, bounded records/topics/subscriptions/storage/time, and hash-bound evidence.

Health requires exact source/configuration/schema identity, deterministic content hashes, strict capability and purpose/sensitivity filtering, accepted retention/revocation behavior, valid provenance chains, replay/tamper/isolation checks, visible fail-closed errors, and no denied authority. Observability must record non-secret source/configuration identities, envelope/topic/capability decisions, rejections, provenance/revocation/retention events, limits, ledger heads, health/cleanup/post-validation, and artifact hashes. Roll back on scope/authority expansion, version/hash mismatch, nondeterminism, data leakage, revocation/retention failure, tamper/isolation failure, credential/network/execution/write capability, or misleading consciousness/runtime claims; preserve evidence, disable materialization/runtime, restore the previous accepted contract state, verify no external mutation, and re-run the complete fixture suite. Post-validation repeats deterministic replay and revocation, verifies final hashes and cleanup, confirms disablement, archives evidence, and returns the environment to a known clean state.

## Unresolved Blockers

- User and Architect disposition of draft PR #2 and the repository charter/retirement decision.
- Non-overlap and ownership decisions across QSO-SEEKER, QuantumStateObjects, QSO-FABRIC, and Repository `0` governance proposals.
- No accepted schemas, policies, fixtures, tests, CI, security/privacy/license evidence, downstream compatibility, provenance, rollback, or deployment evidence.
- The scaffold materializer remains unauthorized for write/materialization use.

## Release Log

- 2026-07-16 — Reclassified the repository as a charter-or-retirement decision.
- 2026-07-17 — Recorded draft PR #2 as the first bounded Digital Consciousness Field charter candidate and moved P0 to `REVIEW`; no implementation, release, materialization, or deployment was authorized.
