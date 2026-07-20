# Release Plan

## Current decision

Status: `BLOCKED — CHARTER DISPOSITION, CONTRACT EVIDENCE, SECURITY, PRIVACY, PROVENANCE, DOWNSTREAM ACCEPTANCE, AND APPROVAL REQUIRED`

QSO-DIGITALIS has two active draft candidates:

- **PR #2** proposes a bounded Digital Consciousness Field architecture, roadmap manifest, and deterministic scaffold materializer at head `46dea012b63e4652bf845d344128797cda804d16`.
- **PR #5** proposes a Pages-ready documentation, architecture, design, onboarding, security, operations, governance, and exact-head documentation-evidence baseline.

Both are pre-release review artifacts. PR #2 does not contain accepted schemas, fixtures, validators, tests, CI evidence, security/privacy/source-license review, migration proof, downstream acceptance, provenance, rollback evidence, or deployment approval. PR #5 does not approve PR #2, materialize its scaffold, or establish runtime capability.

## Versioning

- Semantic Versioning begins only after P0 charter approval.
- First possible documentation candidate: `0.0.1-charter.1`.
- First contract candidate: `0.1.0-alpha.1`, only after accepted schemas, policies, canonicalization, fixtures, validators, tests, CI, security, provenance, migration, rollback, and downstream evidence exist.
- Envelope, topic, capability, query/response, acknowledgment, revocation, provenance-link, evidence-reference, retention, replay, and canonicalization versions must be explicit and hash-verifiable.
- Incompatible field, identity, capability, purpose, sensitivity, retention, revocation, canonicalization, provenance, storage, or migration changes require a new compatible plan and coordinated downstream fixtures.
- Documentation or retirement versions must not imply runtime capability.

## Release scope

### Documentation candidate

- Current repository state and claim boundary.
- A.L.I.S.T.A.I.R.E. portfolio role and non-overlap map.
- Candidate architecture, contract family, lifecycle, trust boundaries, capability separation, canonicalization, failure, migration, security, privacy, consent, operations, rollback, and evidence guidance.
- GitHub Pages source and strict exact-head build evidence.
- Alignment with `taskchain.md`, `release.md`, `changelog.md`, and `punchlist.md`.

### Charter candidate

- Purpose, users, evidence-envelope inputs/outputs, identity and capability ownership, publisher/subscriber separation, non-goals, trust/data/privacy/source-license/retention/consent boundaries, repository relationships, verification, migration, rollback, incident response, and retirement criteria.
- Explicit distinction between architectural naming and literal-consciousness claims.
- Explicit exclusion of raw network responses, credentials, packages, binaries, Git objects, unrestricted shared memory, implicit trust, autonomous approval, repository writes, payments, production infrastructure, and physical-world authority.

### Later contract candidate

- Charter-approved schemas and policies for field envelopes, topics, capabilities, queries/responses, acknowledgments, revocations, provenance links, evidence references, sensitivity, purpose limitation, retention, consent-capacity binding, human review, canonicalization, and tamper detection.
- Positive, negative, malformed, oversized, boundary, revocation, expiry, replay, duplicate, tamper, isolation, and version/hash mismatch fixtures.
- One bounded local in-memory/filesystem reference path only after contract acceptance.
- Read-only downstream compatibility with accepted QSO-SEEKER, QuantumStateObjects, and QSO-FABRIC contracts.

### Explicitly excluded from early candidates

- Running the PR #2 scaffold materializer with `--write` as evidence of implementation.
- Network transport, credentials, signing authority, persistent multi-user service, schedules, external storage, autonomous decisions, unrestricted shared state, repository mutation, release, or deployment.
- Any literal consciousness, awareness, sentience, personhood, or independent-authority claim.

## Selected candidate work

Draft PR #5 is selected only as the documentation candidate. Draft PR #2 remains the P0 charter candidate. No contract, implementation, integration, release, or deployment candidate is selected.

## Planned changelog entries

- `Documentation`: Pages baseline, responsibility map, architecture, diagrams, onboarding, operations, decision register, release-evidence map, and validation workflow.
- `Architecture`: approved DCF charter or retirement notice; accepted ownership and non-overlap decisions.
- `Added`: accepted field schemas, policies, canonicalization, deterministic fixtures, validators, and bounded local reference path only after approval.
- `Security`: consent-capacity binding, capability separation, purpose/sensitivity filtering, retention/revocation, tamper detection, isolation, non-executable records, least privilege, and fail-closed version/hash checks.
- `Release`: source artifacts, reports, SBOM where applicable, checksums, provenance, migrations, rollback evidence, downstream acceptance, and approval.

## Acceptance gates

| Gate | Status | Requirement |
|---|---|---|
| Documentation | REVIEW | PR #5 builds strictly against its exact submitted head, passes the consent-capacity lock, retains a rendered artifact and evidence manifest, and contains no misleading capability claims. |
| Charter/retirement disposition | REVIEW | Explicitly approve, revise, or reject PR #2 and PR #5; establish unique scope and authority boundaries. |
| Non-overlap/architecture | FAIL | Distinguish DCF contract ownership from QSO-SEEKER retrieval/canonicalization, QuantumStateObjects runtime, QSO-FABRIC experiment evidence, Bridge external boundaries, and the A.L.I.S.T.A.I.R.E. development control plane. |
| Task completion | FAIL | P0 is `DONE`; implementation requires P1-P3 with linked immutable evidence. |
| Schemas/contracts | NO EVIDENCE | Versioned schemas, policies, canonicalization, migrations, fixtures, negative cases, validators, and hashes validate deterministically. |
| Tests/determinism | NO EVIDENCE | Exact-head tests cover canonicalization, capabilities, purpose, sensitivity, retention, revocation, replay, tamper, isolation, limits, cleanup, and version/hash mismatch. |
| Security | PARTIAL | Immutable consent-capacity policy and CI lock exist; no accepted field threat model, implementation tests, dependency evidence, or external security review exists. |
| Privacy/source license/retention | BLOCKED | Data classes, lawful purpose, source terms, minimization, redaction, retention, revocation, deletion, logging, public/private boundaries, and notice model require approval. |
| Provenance | PARTIAL | PR/head identities and documentation evidence design exist; no accepted contract artifacts, SBOM, attestation, downstream acceptance, or rollback rehearsal exists. |
| Integration | NO EVIDENCE | SEEKER, QuantumStateObjects, and FABRIC accept one exact contract version/hash and fail closed on mismatch. |
| Deployment readiness | BLOCKED | No runtime/storage/transport target is authorized; a first verification target must be disposable, local, credential-free, network-disabled, synthetic, bounded, and incapable of external writes. |
| Release approval | PENDING | A separate human release approval is required after all prior gates pass. |
| Deployment approval | PENDING | A separate operator, target, credentials, monitoring, incident, rollback, support, and human approval record is required. |

## Artifact requirements

### Documentation

- exact source commit;
- pinned documentation dependencies;
- strict build log;
- rendered site;
- generated-site manifest with file hashes;
- consent-capacity lock result;
- pull-request disposition.

### Future contract and implementation

- approved charter or retirement notice;
- architecture responsibility/non-overlap map;
- versioned contract and migration register;
- schemas, policies, canonicalization, fixtures, validators, positive/negative/adversarial/replay/revocation/isolation/limit tests;
- exact-head CI logs;
- security, privacy, source-license, retention, and consent review;
- source artifact, dependency inventory, SBOM where applicable, checksums, and provenance;
- downstream compatibility, health, observability, rollback, and post-validation evidence.

## Deployment readiness, health, observability, rollback, and post-validation

No deployment is authorized. A future first target must be a disposable local in-memory/filesystem verification environment with synthetic non-sensitive records, no credentials, no network, no external repository writes, no generated-code execution, explicit human controls, bounded records/topics/subscriptions/storage/time, and hash-bound evidence.

Health requires exact source/configuration/schema/policy identity, deterministic content hashes, strict capability and purpose/sensitivity filtering, accepted retention/revocation behavior, valid provenance chains, replay/tamper/isolation checks, visible fail-closed errors, and no denied authority. Observability must record non-secret source/configuration identities, envelope/topic/capability decisions, rejections, provenance/revocation/retention events, limits, ledger heads, health/cleanup/post-validation, and artifact hashes. Roll back on scope or authority expansion, version/hash mismatch, nondeterminism, data leakage, revocation/retention failure, tamper/isolation failure, credential/network/execution/write capability, or misleading consciousness/runtime claims; preserve evidence, disable the candidate path, restore the previous accepted contract state, verify no external mutation, and re-run the complete fixture suite. Post-validation repeats deterministic replay and revocation, verifies final hashes and cleanup, confirms disablement, archives evidence, and returns the environment to a known clean state.

## Unresolved blockers

- User and Architect disposition of PR #2 and PR #5 and the repository charter/retirement decision.
- Contract, identity, capability, vocabulary, data-governance, migration, and emergency-stop ownership across the portfolio.
- No accepted schemas, policies, canonicalization, fixtures, validators, tests, downstream compatibility, release provenance, rollback rehearsal, or deployment evidence.
- The scaffold materializer remains unauthorized for write/materialization use.

## Release log

- 2026-07-16 — Reclassified the repository as a charter-or-retirement decision.
- 2026-07-17 — Recorded draft PR #2 as the first bounded DCF charter candidate and moved P0 to `REVIEW`; no implementation, release, materialization, or deployment was authorized.
- 2026-07-20 — Recorded draft PR #5 as the documentation-only Pages and architecture candidate; added exact-head documentation evidence requirements without advancing P0-P5.
