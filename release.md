# Release Plan

## Current decision

Status: `BLOCKED — DRAFT PR #2 CHARTER DISPOSITION, CONTRACT EVIDENCE, SECURITY, PRIVACY, PROVENANCE, AND APPROVAL REQUIRED`

QSO-DIGITALIS has one concrete draft charter candidate in PR #2. The pull request proposes a bounded Digital Consciousness Field architecture, a public project overview, a roadmap manifest, and a deterministic scaffold materializer for capability-scoped, content-addressed evidence exchange among QSO-SEEKER, QuantumStateObjects, and QSO-FABRIC.

The candidate is documentation and scaffold only. It does not contain accepted field schemas, deterministic fixtures, tests, CI evidence, security/privacy/license review, migration/compatibility proof, downstream consumer acceptance, provenance, rollback evidence, or deployment approval. The materializer must remain dry-run/inert; generated placeholder files must not be treated as implementation.

The current immutable head must be read from PR #2 before validation. This release plan does not hard-code a moving branch SHA.

## Versioning

- Semantic Versioning begins only after P0 charter approval.
- First possible documentation candidate: `0.0.1-charter.1`.
- First contract candidate: `0.1.0-alpha.1`, only after accepted schemas, policies, fixtures, tests, CI, security, provenance, and rollback evidence exist.
- Envelope, topic, capability, query/response, acknowledgment, revocation, provenance-link, evidence-reference, retention, and replay versions must be explicit and hash-verifiable.
- Incompatible field, authority, retention, revocation, canonicalization, or storage changes require migrations and coordinated downstream fixtures.
- Retirement must not imply runtime capability.

## Release scope

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

## Selected candidate work

Draft PR #2 is selected only as the P0 charter candidate. It may move from `REVIEW` to an accepted charter only after explicit user and Architect disposition, non-overlap analysis, threat/privacy/license/retention review, and a complete lifecycle/rollback decision. No implementation or release candidate is selected.

## Acceptance gates

| Gate | Status | Requirement |
|---|---|---|
| Charter/retirement disposition | REVIEW | Explicitly approve, revise, or reject draft PR #2; establish unique scope and authority boundaries. |
| Non-overlap/architecture | FAIL | Distinguish DCF contract ownership from QSO-SEEKER retrieval/canonicalization, QuantumStateObjects runtime, QSO-FABRIC experiment evidence, Repository `0` governance proposals, and Repository `1` capability authority. |
| Task completion | FAIL | P0 is `DONE`; implementation requires P1-P3 with linked immutable evidence. |
| Schemas/contracts | NO EVIDENCE | Versioned schemas, policies, migrations, fixtures, negative cases, and hashes validate deterministically. |
| Tests/determinism | NO EVIDENCE | Exact-head tests cover canonicalization, capabilities, retention, revocation, replay, tamper, isolation, and version/hash mismatch. |
| Security | NO EVIDENCE | No implicit trust, raw/executable transport, credential path, unrestricted shared memory, autonomous authority, or external mutation exists. |
| Documentation | PARTIAL | Public overview and draft architecture exist; approved charter, operations, limitations, compatibility, and recovery do not. |
| Privacy/license/retention | BLOCKED | Data classes, purpose limitation, retention, revocation, public/private boundaries, source terms, and notice/license model require approval. |
| Provenance | PARTIAL | PR identity and candidate documents exist; no exact-head artifacts, reports, checksums, SBOM, attestation, or downstream acceptance exist. |
| Deployment readiness | BLOCKED | No runtime/storage/transport target is authorized; first target must be disposable, local, credential-free, network-disabled, and fixture-only. |
| Approval | PENDING | Separate charter, merge, release, and deployment approvals are required. |

## Artifact requirements

- Approved charter or retirement notice in source and rendered form.
- Architecture responsibility/non-overlap map and versioned contract/migration register.
- For implementation: schemas, policies, fixtures, validators, positive/negative/adversarial/replay/revocation/isolation tests, exact-head CI logs, security/privacy/license reports, source artifact, SBOM where applicable, checksums, provenance, downstream compatibility, health/observability, rollback, and post-validation evidence.

## Deployment readiness, health, observability, rollback, and post-validation

No deployment is authorized. A future first target must be a disposable local in-memory/filesystem verification environment with synthetic non-sensitive records, no credentials, no network, no external repository writes, no generated-code execution, explicit human controls, bounded records/topics/subscriptions/storage/time, and hash-bound evidence.

Health requires exact source/configuration/schema identity, deterministic content hashes, strict capability and purpose/sensitivity filtering, accepted retention/revocation behavior, valid provenance chains, replay/tamper/isolation checks, visible fail-closed errors, and no denied authority. Observability must record non-secret source/configuration identities, envelope/topic/capability decisions, rejections, provenance/revocation/retention events, limits, ledger heads, health/cleanup/post-validation, and artifact hashes.

Roll back on scope or authority expansion, version/hash mismatch, nondeterminism, data leakage, revocation/retention failure, tamper/isolation failure, credential/network/execution/write capability, or misleading consciousness/runtime claims. Preserve evidence, disable materialization/runtime, restore the previous accepted contract state, verify no external mutation, and re-run the complete fixture suite.

## Unresolved blockers

- User and Architect disposition of draft PR #2 and the repository charter/retirement decision.
- Non-overlap and ownership decisions across QSO-SEEKER, QuantumStateObjects, QSO-FABRIC, Repository `0`, and Repository `1`.
- No accepted schemas, policies, fixtures, tests, CI, security/privacy/license evidence, downstream compatibility, provenance, rollback, or deployment evidence.
- The scaffold materializer remains unauthorized for write/materialization use.

## Release log

- 2026-07-20 — Expanded draft PR #2 with a bounded public README and aligned task/release coordination; no implementation, materialization, release, or deployment was authorized.
- 2026-07-17 — Recorded draft PR #2 as the first bounded Digital Consciousness Field charter candidate and moved P0 to `REVIEW`.
- 2026-07-16 — Reclassified the repository as a charter-or-retirement decision.
