# Contract design

This page records the **candidate contract shape** that P0 review must either approve, revise, or reject. It does not establish an accepted schema and must not be used as a production interoperability promise.

## Design objective

A conforming exchange should let a publisher expose an already accepted evidence record to a precisely scoped subscriber without transferring execution authority, hidden mutable state, credentials, or implicit trust.

## Candidate envelope

A future `field-envelope` should carry only the minimum information required to verify and govern an evidence reference.

| Field group | Candidate contents | Invariant |
|---|---|---|
| Identity | envelope identifier, publisher identifier, issuer class | Explicit and verifiable; never inferred from display names |
| Contract | schema name, semantic version, schema digest | Unknown versions or digest mismatch fail closed |
| Evidence | canonical record digest, media type, byte length, evidence-reference identifier | Content is immutable under the digest |
| Provenance | source-record link, canonicalization record, prior envelope links | Every link is hash-bound and independently traversable |
| Scope | topic, approved purpose, source class, experiment identifier | Access outside the intersection is denied |
| Sensitivity | classification, disclosure constraints, redaction profile | Subscriber receives no broader view than authorized |
| Time | issued time, not-before time, expiry, retention class | Expired or not-yet-valid records are unavailable |
| Capabilities | permitted operations and optional delegation constraints | Operations are explicit and non-transitive by default |
| Review | review status and evidence reference | Review metadata cannot substitute for required approval |
| Revocation | revocation endpoint or tombstone reference | Revocation remains observable and replay-safe |

## Capability model

Capabilities should be separate, least-privilege grants:

- `publish` — submit an envelope candidate;
- `discover` — enumerate authorized references without reading content;
- `subscribe` — receive bounded change notifications for an approved topic and purpose;
- `read` — resolve a specific authorized evidence reference;
- `acknowledge` — record receipt or processing state without modifying the source record;
- `revoke` — issue a valid revocation for a record the caller is authorized to revoke;
- `administer-policy` — maintain contract policy, separately approved and never implied by ordinary use.

No capability implies another. Delegation, if ever supported, must be narrower than the delegator's authority, time-bounded, purpose-bound, revocable, and fully auditable.

## Candidate record family

| Record | Purpose |
|---|---|
| Field envelope | Bind identity, evidence digest, policy, scope, and lifecycle metadata |
| Evidence reference | Resolve a canonical inert record by content address |
| Topic definition | Define vocabulary, permitted publishers, subscriber classes, and policy defaults |
| Capability grant | Express operation, resource, purpose, constraints, issuer, subject, and expiry |
| Query | Request references under explicit filters and limits |
| Response | Return bounded references plus contract and policy evidence |
| Acknowledgment | Record receipt, rejection, or processing evidence without mutating the record |
| Revocation | Withdraw authority or availability while preserving an auditable tombstone |
| Provenance link | Connect source, transformation, envelope, access, and experiment evidence |
| Retention event | Record expiry, deletion eligibility, legal hold, or tombstone transition |

## Canonicalization and hashing

Contract acceptance requires one deterministic canonicalization specification per serialized record type. It must define:

- character encoding and Unicode normalization;
- object-key ordering and number representation;
- treatment of absent, null, empty, and default values;
- timestamp format and precision;
- content type and compression rules;
- digest algorithm identifier and domain-separation prefix;
- maximum size and nesting depth;
- behavior for duplicate keys, unknown fields, and unsupported versions.

A digest is meaningful only when the exact canonicalization procedure and schema digest are also bound into verification evidence.

## Fail-closed rules

A conforming validator rejects at least:

- malformed or oversized records;
- unknown schema versions or mismatched schema digests;
- invalid publisher identity or missing capability;
- purpose, topic, source-class, sensitivity, or experiment mismatch;
- expired, revoked, not-yet-valid, or retention-ineligible records;
- content digest mismatch, provenance break, substitution, or replay outside policy;
- ambiguous migration state;
- requests that would expose executable content, secrets, or external-write authority.

## Versioning and migration

Compatible additions require explicit defaults and fixtures proving old consumers remain safe. Any change to canonicalization, identity, capability meaning, purpose enforcement, sensitivity, retention, revocation, provenance, or digest behavior is incompatible unless a reviewed migration proves both old and new states.

Every downstream evidence bundle should record:

1. contract name and semantic version;
2. schema digests;
3. policy digests;
4. canonicalization identifier;
5. evidence-reference digests;
6. migration identifiers, if any;
7. validation result and exact validator source identity.

## Acceptance evidence

The contract is not accepted until schemas, policies, fixtures, validators, deterministic tests, negative cases, migration tests, exact-head CI evidence, security/privacy/license review, downstream compatibility results, and rollback procedures are all linked from the release record.
