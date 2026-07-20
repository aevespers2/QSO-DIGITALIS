# Release Plan

## Current Decision

Status: `BLOCKED — CHARTER DISPOSITION, DOCUMENTATION VALIDATION, CONTRACT EVIDENCE, SECURITY, PRIVACY, PROVENANCE, AND APPROVAL REQUIRED`

QSO-DIGITALIS has one concrete draft charter candidate in PR #2 and one Pages-ready documentation candidate. Together they describe a possible bounded Digital Consciousness Field contract for capability-scoped, content-addressed evidence exchange among QSO-SEEKER, QuantumStateObjects, and QSO-FABRIC.

Both candidates remain proposals. No accepted field schemas, deterministic fixtures, tested implementation, downstream acceptance, release artifact, Pages publication, or deployment exists. The scaffold materializer must remain dry-run/inert; generated placeholder files must not be treated as implementation.

## Versioning

- Semantic Versioning begins only after P0 charter approval.
- First possible documentation candidate: `0.0.1-charter.1`.
- First contract candidate: `0.1.0-alpha.1`, only after accepted schemas, policies, canonicalization, fixtures, tests, CI, security, provenance, migration, and rollback evidence exist.
- Envelope, topic, capability, query/response, acknowledgment, revocation, provenance-link, evidence-reference, retention, and replay versions must be explicit and hash-verifiable.
- Incompatible field, authority, retention, revocation, canonicalization, or storage changes require migrations and coordinated downstream fixtures.
- Retirement must not imply runtime capability.

## Release Scope

### Documentation candidate

- Pages-ready project overview and repository responsibility map.
- Architecture, authority, lifecycle, validation, and release-decision diagrams.
- Proposed design-contract families and invariants.
- Charter decision framework and ADR-0001.
- Security, privacy, retention, revocation, limitations, onboarding, operations, incident, recovery, rollback, and retirement guidance.
- Explicit proposal status and non-claims.

### Charter candidate

- Purpose, users, evidence-envelope inputs/outputs, publisher/subscriber capability separation, non-goals, trust/data/privacy/license/retention boundaries, repository relationships, verification strategy, migrations, rollback, and retirement criteria.
- Explicit distinction between architectural naming and literal-consciousness claims.
- Explicit exclusion of raw network responses, credentials, packages, binaries, Git objects, unrestricted shared memory, implicit trust, autonomous approval, repository writes, payments, and production infrastructure.

### Later contract candidate

- Charter-approved schemas and policies for field envelopes, topics, capabilities, queries/responses, acknowledgments, revocations, provenance links, evidence references, sensitivity, purpose limitation, retention, human review, and tamper detection.
- Positive, negative, boundary, revocation, expiry, replay, duplicate, malformed, cross-QSO isolation, and version/hash mismatch fixtures.
- One bounded local in-memory/filesystem reference implementation only after contract acceptance.
- Read-only downstream compatibility with accepted QSO-SEEKER, QuantumStateObjects, and QSO-FABRIC contracts.

### Explicitly excluded

- Running the scaffold materializer with `--write` as evidence of implementation.
- Network transport, credentials, signing authority, persistent multi-user service, schedules, external storage, autonomous decisions, unrestricted shared state, or production deployment.
- Any literal consciousness, awareness, sentience, or independent authority claim.
- Treating a documentation build, schema build, or local reference path as release or deployment approval.

## Selected Candidate Work

Draft PR #2 is selected only as the P0 charter candidate. The Pages work is selected only as a documentation-review candidate. Neither may move to an accepted product or release state without explicit user and Architect disposition, non-overlap analysis, threat/privacy/license/retention review, and a complete lifecycle/rollback decision.

## Acceptance Gates

| Gate | Status | Requirement |
|---|---|---|
| Charter/retirement disposition | REVIEW | Explicitly approve, revise, or reject draft PR #2 and ADR-0001; establish unique scope and authority boundaries. |
| Non-overlap/architecture | FAIL | Distinguish DCF contract ownership from QSO-SEEKER retrieval/canonicalization, QuantumStateObjects runtime, QSO-FABRIC experiment evidence, and portfolio governance. |
| Documentation build | PENDING | Exact-head `mkdocs build --strict` passes with retained logs and artifact identity. |
| Documentation quality | PENDING | Links, Mermaid diagrams, navigation, terminology, accessibility, privacy, license, and claim review pass. |
| Pages publication | BLOCKED | Explicit publication approval, provenance, source/head identity, rollback, and post-publication validation are recorded. |
| Task completion | FAIL | P0 is `DONE`; implementation requires P1-P3 with linked immutable evidence. |
| Schemas/contracts | NO EVIDENCE | Versioned schemas, policies, canonicalization, migrations, fixtures, negative cases, and hashes validate deterministically. |
| Tests/determinism | NO EVIDENCE | Exact-head tests cover canonicalization, capabilities, retention, revocation, replay, tamper, isolation, and version/hash mismatch. |
| Security | NO EVIDENCE | No implicit trust, raw/executable transport, credential path, unrestricted shared memory, autonomous authority, or external mutation exists. |
| Privacy/license/retention | BLOCKED | Data classes, purpose limitation, retention, revocation, public/private boundaries, source terms, and notice/license model require approval. |
| Provenance | PARTIAL | PR and commit identities can be recorded; no accepted release artifacts, reports, checksums, SBOM, attestation, or downstream acceptance exist. |
| Deployment readiness | BLOCKED | No runtime/storage/transport target is authorized; first target must be disposable, local, credential-free, network-disabled, and fixture-only. |
| Approval | PENDING | Separate charter, merge, Pages, release, and deployment approvals are required. |

## Artifact Requirements

### Documentation

- exact source commit and pull request identity;
- strict build log and rendered site artifact;
- artifact checksum and retention record;
- link, diagram, navigation, accessibility, privacy, license, and claim-review report;
- publication and rollback decision.

### Future implementation

- approved charter or retirement notice;
- architecture responsibility/non-overlap map and versioned contract/migration register;
- schemas, policies, fixtures, validators, positive/negative/adversarial/replay/revocation/isolation tests;
- exact-head CI logs, security/privacy/license reports, source artifact, SBOM where applicable, checksums, provenance, downstream compatibility, health/observability, rollback, and post-validation evidence.

## Operations and Rollback

No deployment is authorized. A future first target must be a disposable local in-memory/filesystem verification environment with synthetic non-sensitive records, no credentials, no network, no external repository writes, no generated-code execution, explicit human controls, bounded records/topics/subscriptions/storage/time, and hash-bound evidence.

Roll back documentation on misleading capability claims, broken navigation, inaccessible or privacy-incompatible publication, provenance mismatch, or unauthorized Pages deployment. Roll back a future contract on scope expansion, version/hash mismatch, nondeterminism, data leakage, revocation/retention failure, tamper/isolation failure, credential/network/execution/write capability, or broken downstream acceptance. Preserve evidence, restore the last accepted state, verify no external mutation, and repeat complete validation.

## Unresolved Blockers

- User and Architect disposition of draft PR #2 and the repository charter/retirement decision.
- Non-overlap and ownership decisions across QSO-SEEKER, QuantumStateObjects, QSO-FABRIC, and portfolio governance.
- Exact-head documentation build, links, diagrams, accessibility, privacy, license, artifact, and claim review.
- No accepted schemas, policies, fixtures, tests, CI, security/privacy/license evidence, downstream compatibility, provenance, rollback, or deployment evidence.
- The scaffold materializer remains unauthorized for write/materialization use.

## Release Log

- 2026-07-16 — Reclassified the repository as a charter-or-retirement decision.
- 2026-07-17 — Recorded draft PR #2 as the first bounded Digital Consciousness Field charter candidate and moved P0 to `REVIEW`; no implementation, release, materialization, or deployment was authorized.
- 2026-07-19 — Added a Pages-ready documentation candidate and explicit documentation validation/publication gates; charter, release, and deployment remain blocked.
