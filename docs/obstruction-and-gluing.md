# Obstruction and Gluing Analysis

## Status

**Documentation and contract-analysis candidate only.** This ledger identifies where QSO-DIGITALIS cannot yet compose safely with the A.L.I.S.T.A.I.R.E. repository portfolio. It does not approve draft PR #2, establish a schema package, create a field runtime or store, authorize transport, issue capabilities, accept evidence as true, or make any record canonical.

## Method

Treat each repository as a local section with a bounded responsibility and each versioned contract as a gluing map. Pairwise compatibility is necessary but not sufficient: a path is accepted only when shared fixtures show that identities, hashes, policy, authority, correction, revocation, and recovery agree on every relevant triple overlap.

This is an engineering compatibility method, not a claim that a complete mathematical homology computation has been performed.

## Candidate Digitalis boundary

The lowest-coupling candidate is:

> QSO-DIGITALIS defines non-executing, content-addressed interpretation, policy-projection, and exchange-envelope profiles for accepted evidence. It preserves source identity and lineage, references separately governed temporal assessments, declares every transformation, and creates purpose-limited consumer views.

Under this candidate:

- QSO-SEEKER owns retrieval, sanitization, source attribution, and inert source-observation records;
- a designated temporal authority owns clock identity, ordering, freshness, uncertainty, and replay assessment;
- QSO-DIGITALIS owns only interpretation references, policy projections, and its profile-specific exchange envelope;
- Bridge owns separately approved admission and transport semantics and delivery receipts;
- Repository `1` owns candidate quarantine, capability, canonical disposition, correction, revocation, checkpoint, and recovery authority;
- QuantumStateObjects and QSO-FABRIC consume exact accepted versions and hashes under separate capabilities;
- QSO-STUDIO and AionUi present distinct states without becoming authority.

## Active obstruction ledger

| ID | Obstruction | Failure mode | Lowest-coupling repair candidate |
|---|---|---|---|
| O-DIG-01 | Source and interpretation identity collapse | Derived claims can appear to be source evidence | Separate typed IDs, domain-separated hashes, immutable source references, explicit UI labels |
| O-DIG-02 | Temporal authority overlap | Digitalis freshness or replay decisions can conflict with temporal-invariants or Repository `1` | Accept temporal assessments as typed external inputs under one designated owner |
| O-DIG-03 | Generic envelope ownership conflict | Digitalis, Seeker, Bridge, QSO-GENOMES, QSO-FABRIC, and Repository `1` can define incompatible envelope rules | Designate a neutral envelope/profile registry; Digitalis owns only its profile |
| O-DIG-04 | Transport and exchange overlap | “Field exchange” can be read as generic network or service authority | Digitalis emits inert envelopes; Bridge owns approved transport profiles |
| O-DIG-05 | Derived store versus canonical state | A content-addressed Digitalis cache can be mistaken for Repository `1` canonical state | Identify any Digitalis store as non-authoritative derived-artifact storage only |
| O-DIG-06 | Projection mistaken for capability | A purpose-limited view can be interpreted as authority to act | Carry explicit non-authority declarations; use separate Repository `1` capabilities |
| O-DIG-07 | Privacy downgrade | Redaction, aggregation, or derivation can reveal protected facts or weaken source restrictions | Most-restrictive-policy inheritance, inference review, deterministic redaction fixtures |
| O-DIG-08 | Correction and cache divergence | Revoked or corrected records can remain active in caches, runtimes, experiments, or interfaces | One versioned propagation contract with bounded invalidation evidence |
| O-DIG-09 | Consciousness terminology ambiguity | The repository name can imply awareness, personhood, or independent authority | Preserve only as an architectural label with explicit non-claims, or rename at P0 |
| O-DIG-10 | Subject namespace mismatch | Seeker, temporal, Digitalis, Bridge, Repository `1`, and consumers can bind the same record to different subjects | Designate typed subject namespaces and crosswalk ownership; reject ambiguous aliases |
| O-DIG-11 | Canonicalization and digest disagreement | Equal-looking records can hash differently or unequal records can be treated as equal | One canonicalization registry, domain tags, exact profile versions, golden vectors |
| O-DIG-12 | Transformation opacity | Normalization, aggregation, redaction, derivation, or repackaging can be undeclared | Field-level transformation declarations and fail-closed replay fixtures |
| O-DIG-13 | Vocabulary and reason-code drift | Completion, confidence, rejection, and uncertainty meanings can diverge across consumers | Versioned shared vocabularies and explicit mappings; never coerce `UNKNOWN` to success |
| O-DIG-14 | Freshness and replay-domain ambiguity | A valid hash can be stale, duplicated, or replayed in a different route | Bind clock source, uncertainty, replay domain, nonce or sequence, and expiry policy |
| O-DIG-15 | Capability and consumer mismatch | A valid projection can be used by the wrong consumer or for the wrong purpose | Bind consumer, purpose, sensitivity, action class, expiry, and exact artifact digest |
| O-DIG-16 | Partial-state collapse | One global success flag can hide unsupported or incomplete evidence groups | Per-claim completion, evidence availability, temporal state, limitations, and reason codes |
| O-DIG-17 | Source-license and retention loss | Derived artifacts can outlive or exceed source terms | Preserve source license, retention start, expiry, legal hold, deletion/tombstone, and disclosure constraints |
| O-DIG-18 | Emergency-stop and recovery gap | Frozen evidence can continue to be projected, transported, admitted, or consumed | Portfolio stop token, independent revocation, cache freeze, explicit recovery and bounded replay |

## Pairwise gluing contracts

### QSO-SEEKER → QSO-DIGITALIS

Required witnesses:

- accepted source profile, producer identity, canonical bytes, and digest;
- malformed, unsupported-version, wrong-producer, and wrong-record-type rejection;
- partial and unsupported collection preservation;
- hostile-input metadata and source-license preservation;
- correction, supersession, and revocation linkage;
- no source mutation during interpretation.

### Temporal authority → QSO-DIGITALIS

Required witnesses:

- accepted clock identity, freshness, uncertainty, ordering, and replay assessment;
- stale or mismatched assessment rejection;
- conflicting clock-source handling;
- duplicate versus replay distinction;
- no silent timestamp replacement or policy override.

### QSO-DIGITALIS → Bridge

Required witnesses:

- exact profile and envelope version acceptance;
- canonical byte and lineage verification;
- undeclared-transformation rejection;
- privacy downgrade, wrong route, wrong consumer, expiry, and revocation rejection;
- transport transformation remains distinct from interpretation.

### Bridge → Repository `1`

Required witnesses:

- delivery receipt never equals canonical acceptance;
- duplicate delivery deduplication;
- partial-delivery, retry, and rollback semantics;
- subject, policy, lineage, and transformation verification;
- correction and revocation propagation.

### Repository `1` → consumers

Required witnesses:

- exact disposition, capability, consumer, purpose, version, and hash binding;
- expired or revoked capability rejection;
- consumption receipt without canonical self-promotion;
- cache invalidation and re-evaluation after correction or revocation;
- interface display cannot create authority.

## Required triple-overlap witnesses

1. **Seeker → temporal authority → Digitalis** — source, subject, clock, freshness, replay, and limitation identities remain coherent.
2. **Seeker → Digitalis → Bridge** — source bytes and lineage stay verifiable while every derived and transport transformation is declared.
3. **Digitalis → Bridge → Repository `1`** — transport success remains distinct from quarantine admission and canonical disposition.
4. **Digitalis → Repository `1` → QuantumStateObjects** — a capability-scoped runtime view binds the exact accepted envelope, policy, consumer, and expiry.
5. **Digitalis → Repository `1` → QSO-FABRIC** — experiment evidence references accepted records without converting experiment outcomes into source truth.
6. **Correction authority → Digitalis → Bridge/Repository `1`** — corrections and revocations invalidate projections, caches, receipts, and dispositions consistently.
7. **Repository `1` → QSO-STUDIO/AionUi → human review** — interfaces preserve source, interpretation, projection, transport, disposition, and approval as separate states.
8. **Emergency stop → Digitalis → downstream caches** — frozen records cannot be newly projected, transported, admitted, or consumed before explicit recovery.

## Acceptance evidence

A gluing edge is not accepted until it has:

- one named contract and profile owner;
- immutable schema/profile versions and canonicalization identifiers;
- positive, negative, malformed, unsupported-version, wrong-subject, stale, replay, privacy, partial-state, correction, revocation, freeze, and rollback fixtures;
- identical golden vectors in every participating repository;
- exact-head CI results and retained hashes;
- migration and retirement rules;
- named privacy, incident, emergency-stop, recovery, and release owners.

## Required architectural decisions

P0 must explicitly decide:

1. whether QSO-DIGITALIS is active as the interpretation/projection profile owner, split into a neutral contract package, renamed, or retired;
2. the generic envelope and profile-registry owner;
3. source, subject/device, temporal, interpretation, projection, transport, disposition, and consumer namespaces;
4. canonical serialization, domain-separated hashing, signing, clock, replay, vocabulary, and reason-code ownership;
5. whether Digitalis may own a local derived-artifact cache or only schemas and profiles;
6. privacy, source-license, retention, correction, revocation, cache invalidation, freeze, and recovery authority;
7. the exact Seeker → temporal/Digitalis → Bridge → Repository `1` route;
8. migration, incident, emergency-stop, rollback, release, deployment, and retirement ownership.

## Scope boundary

This ledger adds documentation only. It does not approve draft PR #2, materialize its scaffold, establish schemas, create or mutate records, fetch external data, transport artifacts, store private data, sign content, issue credentials or capabilities, publish Pages, release a package, or deploy a service.
