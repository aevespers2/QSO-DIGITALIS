# Release Plan

## Current decision

Status: `BLOCKED — CHARTER DISPOSITION, CONTRACT OWNERSHIP, GLUING EVIDENCE, SECURITY, PRIVACY, PROVENANCE, DOWNSTREAM ACCEPTANCE, AND APPROVAL REQUIRED`

QSO-DIGITALIS has two active draft candidates:

- **PR #2** proposes a bounded Digital Consciousness Field architecture, roadmap manifest, and deterministic scaffold materializer.
- **PR #5** proposes a Pages-ready documentation, architecture, design, onboarding, security, operations, source-observation interpretation/profile, obstruction/gluing, and exact-head documentation-evidence baseline.

Both are pre-release review artifacts. PR #2 does not contain accepted schemas, fixtures, validators, tests, CI evidence, security/privacy/source-license review, migration proof, downstream acceptance, provenance, rollback evidence, or deployment approval. PR #5 does not approve PR #2, materialize its scaffold, establish schemas or runtime capability, authorize transport or storage, or make the interpretation profile authoritative.

## Lowest-coupling candidate

The current documentation recommends, but does not approve, the following bounded role:

> QSO-DIGITALIS defines a non-executing, content-addressed interpretation, policy-projection, and exchange-envelope profile for accepted evidence. It preserves source identity and lineage, references external temporal assessments, declares transformations, and creates purpose-limited consumer views. It does not retrieve sources, validate truth, issue operational capabilities, transport artifacts, own canonical operational state, execute runtimes, approve experiments, publish externally, or deploy services.

P0 may approve, revise, decompose, transfer, or reject this candidate. Retirement remains valid.

## Versioning

- Semantic Versioning begins only after P0 charter approval.
- First possible documentation candidate: `0.0.1-charter.2`.
- First profile/contract candidate: `0.1.0-alpha.1`, only after accepted ownership, schemas, policies, canonicalization, domain-separated digest scopes, fixtures, validators, tests, CI, security, provenance, migration, correction/revocation, rollback, and downstream evidence exist.
- Source-reference, temporal-reference, interpretation, projection, exchange-envelope, lineage, correction, revocation, freeze, recovery, and canonicalization versions must be explicit and hash-verifiable.
- Source record, temporal assessment, interpretation, projection, transport artifact, delivery receipt, Repository `1` disposition, and consumer receipt identities must not alias one another.
- Incompatible identity, vocabulary, canonicalization, digest scope, transformation, purpose, sensitivity, retention, privacy, correction, revocation, transport, disposition, migration, or cache-invalidation changes require coordinated version changes and downstream fixtures.
- Documentation or retirement versions must not imply runtime capability.

## Release scope

### Documentation candidate

- Current repository state and claim boundary.
- A.L.I.S.T.A.I.R.E. portfolio role and non-overlap map.
- Candidate interpretation/projection/exchange role and explicit authority exclusions.
- Record-identity separation, lifecycle, trust boundaries, transformations, digest scopes, privacy inheritance, correction/revocation, freeze/recovery, obstruction ledger, pairwise maps, and triple-overlap witnesses.
- GitHub Pages source and strict exact-head build evidence.
- Alignment with `taskchain.md`, `release.md`, `changelog.md`, and `punchlist.md`.

### Charter candidate

- Purpose, users, source/reference inputs, interpretation/projection outputs, exchange envelopes, identity and capability ownership, non-goals, trust/data/privacy/source-license/retention/consent boundaries, repository relationships, verification, migration, correction, revocation, freeze, rollback, incident response, recovery, and retirement criteria.
- Explicit distinction between architectural naming and literal-consciousness claims.
- Explicit exclusion of source retrieval, independent temporal truth, raw network responses, credentials, packages, binaries, Git objects, unrestricted shared memory, implicit trust, operational capability issuance, autonomous approval, Repository `1` canonical-state ownership, runtime execution, repository writes, payments, production infrastructure, and physical-world authority.

### Later profile/contract candidate

- Charter-approved schemas and policies for typed source/temporal references, interpretations, projections, exchange envelopes, lineage, transformations, confidence/uncertainty, completion states, sensitivity, purpose limitation, source-license inheritance, retention, consent-capacity binding, correction, supersession, revocation, freeze, recovery, canonicalization, and tamper detection.
- Positive, negative, malformed, oversized, boundary, wrong-producer, wrong-subject, stale, replay, duplicate, privacy-downgrade, undeclared-transformation, revocation, expiry, tamper, isolation, and version/hash mismatch fixtures.
- Pairwise compatibility with QSO-SEEKER, temporal authority, Bridge, Repository `1`, QuantumStateObjects, QSO-FABRIC, QSO-STUDIO, and AionUi.
- Eight triple-overlap witness groups demonstrating stable gluing across source, time, interpretation, transport, disposition, consumption, correction, and emergency stop.
- One bounded local in-memory/filesystem reference path only after contract acceptance.

### Explicitly excluded from early candidates

- Running the PR #2 scaffold materializer with `--write` as evidence of implementation.
- Network transport, credentials, signing authority, persistent multi-user service, schedules, external storage, autonomous decisions, unrestricted shared state, repository mutation, release, or deployment.
- Treating a policy projection as an operational capability.
- Treating transport or display success as truth, authorization, or canonical acceptance.
- Any literal consciousness, awareness, sentience, personhood, or independent-authority claim.

## Material obstructions

1. Source, temporal, interpretation, projection, envelope, transport, receipt, disposition, and consumption identities can collapse.
2. Digitalis temporal calculations can conflict with the designated temporal authority.
3. Multiple repositories claim generic envelope, registry, serialization, canonicalization, and migration ownership.
4. Draft field language can overlap Bridge transport responsibility.
5. Content-addressed derived artifacts can be mistaken for Repository `1` canonical state.
6. A projection can be mistaken for permission to act.
7. Redaction, aggregation, or derivation can weaken privacy or source restrictions.
8. Corrections and revocations can diverge across projections, transport caches, Repository `1`, runtimes, experiments, and interfaces.
9. “Digital Consciousness Field” can imply unsupported consciousness or autonomous-authority claims.

## Selected candidate work

Draft PR #5 is selected only as the documentation candidate. Draft PR #2 remains the P0 charter/scaffold candidate. The interpretation profile is a review artifact within PR #5. No schema package, implementation, integration, release, publication, or deployment candidate is selected.

## Acceptance gates

| Gate | Status | Requirement |
|---|---|---|
| Documentation | REVIEW | PR #5 builds strictly against its exact submitted head, passes the consent-capacity lock, retains a rendered artifact and evidence manifest, includes the interpretation/gluing profile, and contains no misleading capability claims. |
| Charter/retirement disposition | REVIEW | Explicitly approve, revise, decompose, transfer, or reject PR #2 and PR #5; establish unique scope and authority boundaries. |
| Neutral ownership | FAIL | Designate the generic envelope/profile registry, canonicalization interface, namespaces, signing/key custody if any, and migration authority. |
| Non-overlap/architecture | FAIL | Distinguish Digitalis interpretation/projection ownership from QSO-SEEKER source retrieval, temporal authority, Bridge transport, Repository `1` disposition/capabilities, QuantumStateObjects runtime, QSO-FABRIC experiments, and interface display. |
| Task completion | FAIL | P0 is `DONE`; implementation requires P1-P4 with linked immutable evidence. |
| Schemas/contracts | NO EVIDENCE | Versioned schemas, policies, canonicalization, digest scopes, migrations, fixtures, negative cases, validators, and hashes validate deterministically. |
| Pairwise gluing | NO EVIDENCE | Seeker→Digitalis, temporal→Digitalis, Digitalis→Bridge, Bridge→Repository `1`, and Repository `1`→consumer fixtures pass identically at pinned versions. |
| Triple-overlap gluing | NO EVIDENCE | Eight source/time/interpretation/transport/disposition/consumption/correction/freeze witnesses commute or fail closed. |
| Tests/determinism | NO EVIDENCE | Exact-head tests cover canonicalization, transformations, identity, purpose, sensitivity, privacy inheritance, retention, correction, revocation, replay, tamper, isolation, limits, cleanup, and version/hash mismatch. |
| Security | PARTIAL | Immutable consent-capacity policy and CI lock exist; no accepted profile threat model, implementation tests, dependency evidence, or external security review exists. |
| Privacy/source license/retention | BLOCKED | Data classes, lawful purpose, source terms, minimization, redaction, inference risk, retention, correction, revocation, deletion/tombstone, logging, public/private boundaries, and notice model require approval. |
| Provenance | PARTIAL | PR/head identities and documentation evidence exist; no accepted contract artifacts, SBOM, attestation, downstream acceptance, correction/revocation replay, or rollback rehearsal exists. |
| Integration | NO EVIDENCE | Every named producer, transport, authority, consumer, and interface accepts one exact profile version/hash and fails closed on mismatch. |
| Deployment readiness | BLOCKED | No runtime/storage/transport target is authorized; a first verification target must be disposable, local, credential-free, network-disabled, synthetic, bounded, and incapable of external writes. |
| Release approval | PENDING | A separate human release approval is required after all prior gates pass. |
| Deployment approval | PENDING | A separate operator, target, credentials owner, monitoring, incident, emergency-stop, rollback, support, and human approval record is required. |

## Artifact requirements

### Documentation

- exact source commit;
- pinned documentation dependencies;
- strict build log;
- rendered site;
- generated-site manifest with file hashes;
- consent-capacity lock result;
- pull-request disposition.

### Future profile and implementation

- approved charter or retirement/transfer notice;
- architecture responsibility and non-overlap map;
- versioned namespace, vocabulary, profile, canonicalization, digest-scope, and migration register;
- schemas, policies, fixtures, validators, positive/negative/adversarial/replay/revocation/privacy/transformation/isolation/limit tests;
- pairwise and triple-overlap compatibility results;
- exact-head CI logs;
- security, privacy, source-license, retention, consent, correction, revocation, and recovery review;
- source artifact, dependency inventory, SBOM where applicable, checksums, and provenance;
- downstream compatibility, health, observability, rollback, emergency-stop, cache-invalidation, and post-validation evidence.

## Deployment readiness, health, observability, rollback, and post-validation

No deployment is authorized. A future first target must be a disposable local in-memory/filesystem verification environment with synthetic non-sensitive records, no credentials, no network, no external repository writes, no generated-code execution, explicit human controls, bounded records/profiles/lineage/cache/time, and hash-bound evidence.

Health requires exact source/configuration/schema/policy/profile identity, deterministic content hashes, distinct record identities, declared transformations, accepted temporal references, strict purpose/sensitivity/privacy/retention filtering, valid lineage, correction/revocation propagation, replay/tamper/isolation checks, visible fail-closed errors, and no denied authority. Observability must record non-secret source/configuration identities, profile and transformation decisions, rejections, correction/revocation/freeze events, limits, health/cleanup/post-validation, and artifact hashes without private payloads or secrets.

Roll back on scope or authority expansion, identity collapse, version/hash mismatch, nondeterminism, data leakage, privacy downgrade, undeclared transformation, correction/revocation failure, cache divergence, tamper/isolation failure, credential/network/execution/write capability, or misleading consciousness/runtime claims. Preserve evidence, freeze the candidate path, restore the previous accepted profile state, verify no external mutation, invalidate derived caches, and re-run the complete fixture suite. There is no automatic unlock.

## Unresolved blockers

- User and Architect disposition of PR #2 and PR #5 and the repository charter/transfer/retirement decision.
- Neutral envelope/profile registry, identity namespace, canonicalization, hashing/signing, vocabulary, data-governance, migration, correction, revocation, cache-invalidation, and emergency-stop ownership.
- Exact Seeker → temporal/Digitalis → Bridge → Repository `1` → consumer route.
- No accepted schemas, policies, canonicalization, fixtures, validators, tests, downstream compatibility, release provenance, correction/revocation replay, rollback rehearsal, or deployment evidence.
- The scaffold materializer remains unauthorized for write/materialization use.

## Release log

- 2026-07-16 — Reclassified the repository as a charter-or-retirement decision.
- 2026-07-17 — Recorded draft PR #2 as the first bounded DCF charter candidate and moved P0 to `REVIEW`; no implementation, release, materialization, or deployment was authorized.
- 2026-07-20 — Recorded draft PR #5 as the documentation-only Pages and architecture candidate; added exact-head documentation evidence requirements without advancing implementation stages.
- 2026-07-21 — Added the source-observation interpretation and exchange profile, identity separation, nine material obstructions, pairwise gluing maps, and eight triple-overlap witnesses. No schema, runtime, storage, transport, capability, release, publication, or deployment was approved.
