# QSOBuilder Punch List

## Architectural hold

No Builder implementation is authorized until the repository charter in `taskchain.md` P0 is approved. Documentation, inventory, contract proposals, fixtures, and evidence preservation may proceed; schema activation, storage, transport, signing, external integration, release, and deployment remain blocked.

## P0 — Charter and portfolio boundary

- [x] Document the current repository state and non-capabilities.
- [x] Add a Pages-ready architecture, security, onboarding, operations, and release-evidence baseline.
- [x] Define a candidate source-observation interpretation and policy-projection profile without approving it.
- [x] Separate source record, temporal assessment, interpretation, projection, exchange envelope, transport artifact, delivery receipt, Repository `1` disposition, and consumer receipt identities.
- [ ] Approve, revise, split, or retire the Digital Consciousness Field charter.
- [ ] Decide whether “Digital Consciousness Field” remains the product name or only a historical architectural label.
- [ ] Decide whether QSO-DIGITALIS owns schemas/profiles only, a local derived-artifact cache, a bounded reference implementation, or no active capability.
- [ ] Assign the neutral envelope and profile-registry owner.
- [ ] Approve the exact QSO-SEEKER → temporal/Digitalis → Bridge → Repository `1` route.
- [ ] Approve explicit non-overlap with QSO-SEEKER, temporal invariants, Bridge, Repository `1`, QuantumStateObjects, QSO-FABRIC, QSO-STUDIO, and AionUi.

## P1 — Identity, vocabulary, and canonicalization

- [ ] Assign namespaces and owners for source, subject/device, temporal assessment, interpretation, projection, envelope, transport, receipt, disposition, and consumption identities.
- [ ] Select canonical serialization and domain-separated hashing interfaces.
- [ ] Decide whether signatures are required and assign signing/key-custody ownership.
- [ ] Define versioned completion states: `COMPLETE`, `PARTIAL`, `UNSUPPORTED`, `UNKNOWN`, `STALE`, `REVOKED`, and `FROZEN`.
- [ ] Define confidence, uncertainty, transformation, reason-code, correction, supersession, and revocation vocabularies.
- [ ] Define digest scopes for each record class and the lineage graph.
- [ ] Define deterministic profile migration, compatibility, deprecation, and cache-invalidation rules.

## P2 — Record and policy contracts

- [ ] Specify interpretation records that reference immutable source records without mutation.
- [ ] Specify purpose-, sensitivity-, retention-, consent-, and consumer-limited projections.
- [ ] Specify inert exchange envelopes with typed references and non-authority declarations.
- [ ] Require field-level declaration of copied, normalized, redacted, aggregated, and derived outputs.
- [ ] Preserve the most restrictive source, privacy, license, retention, consent, and disclosure constraint.
- [ ] Define correction, supersession, revocation, freeze, recovery, and tombstone propagation.
- [ ] Define no-secret/public-projection requirements for Pages, logs, artifacts, URLs, and identifiers.
- [ ] Define bounded record, lineage, cache, time, and resource limits.

## P3 — Pairwise gluing fixtures

- [ ] QSO-SEEKER → Digitalis accepted source profile, wrong-producer rejection, partial/unsupported preservation, hostile-input metadata, source-license inheritance, correction, and revocation.
- [ ] Temporal authority → Digitalis accepted clock/freshness, stale rejection, conflicting clocks, replay distinction, uncertainty preservation, and no timestamp substitution.
- [ ] Digitalis → Bridge accepted version/hash, undeclared-transformation rejection, privacy-downgrade rejection, wrong route/consumer, expiry/revocation, and lineage mismatch.
- [ ] Bridge → Repository `1` delivery-versus-acceptance separation, duplicate delivery, partial delivery/retry, correction/revocation propagation, and transport transformation verification.
- [ ] Repository `1` → consumer exact disposition/capability binding, wrong consumer/purpose/version/hash, expiry/revocation, receipt evidence, and cache invalidation.

## P4 — Triple-overlap witnesses

- [ ] Seeker → temporal authority → Digitalis preserves source, subject, clock, freshness, replay, and limitations.
- [ ] Seeker → Digitalis → Bridge preserves source bytes and declares every derivation or transport transformation.
- [ ] Digitalis → Bridge → Repository `1` keeps transport success distinct from quarantine and canonical disposition.
- [ ] Digitalis → Repository `1` → QuantumStateObjects binds an exact accepted view and non-transferable capability.
- [ ] Digitalis → Repository `1` → QSO-FABRIC preserves evidence references without converting experiment results into source truth.
- [ ] Correction authority → Digitalis → Bridge/Repository `1` invalidates projections, caches, receipts, and dispositions.
- [ ] Repository `1` → QSO-STUDIO/AionUi → human review displays source, interpretation, projection, transport, and disposition separately.
- [ ] Emergency stop → Digitalis → downstream caches prevents new projection, transport, admission, or consumption until explicit recovery.

## P5 — Security, privacy, operations, and recovery

- [ ] Assign privacy, source-license, retention, consent, disclosure, correction, revocation, incident, emergency-stop, recovery, and rollback owners.
- [ ] Threat-model identity collapse, interpretation overwrite, temporal disagreement, privacy downgrade, replay, lineage substitution, cache divergence, capability confusion, and misleading consciousness claims.
- [ ] Define local/offline verification with synthetic non-sensitive fixtures and no credentials or network.
- [ ] Define health and observability without logging private payloads or secrets.
- [ ] Define freeze conditions and an independently controlled no-automatic-unlock recovery path.
- [ ] Exercise correction/revocation propagation and bounded cache invalidation.
- [ ] Exercise a portfolio-wide emergency stop and ordered restart.

## P6 — Release and retirement

- [ ] Reconcile PR #2 and the documentation candidate at one immutable review head.
- [ ] Retain strict exact-head documentation and consent-capacity evidence.
- [ ] Produce accepted schema/profile artifacts, validators, fixtures, compatibility manifests, checksums, migrations, and rollback evidence before any contract release.
- [ ] Obtain read-only downstream replay evidence from every accepted consumer.
- [ ] Obtain security, privacy, source-license, retention, provenance, and release approval.
- [ ] If retired, publish the successor contract, migration map, archive notice, and rollback/disposition record.

## Quality gates

- [ ] No credentials, unrestricted networking, autonomous execution, direct settlement, implicit capability grant, or self-modifying behavior.
- [ ] Every integration is versioned, hash-verifiable, independently testable, and fail-closed.
- [ ] Transport or display success is never represented as truth, authority, or canonical acceptance.
- [ ] Derived interpretations and projections never overwrite source evidence.
- [ ] Unknown or unsupported state is never represented as secure, complete, fresh, or accepted.
- [ ] Claims remain limited to implemented and verified capabilities.
