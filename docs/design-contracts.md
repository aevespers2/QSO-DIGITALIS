# Design contracts

This page records requirements for a future schema-first candidate. It does not define an accepted wire format or authorize implementation.

## Contract families

| Contract | Responsibility | Minimum identity |
|---|---|---|
| Field envelope | Bind an immutable evidence reference to policy metadata | envelope version, envelope ID, content hash, publisher ID, created time |
| Topic | Name a bounded evidence category | topic version, topic ID, owner, allowed record classes |
| Capability | Grant one explicit operation within scope | capability version, subject, operation, scope, expiry, issuer |
| Query | Request a bounded read view | query version, requester, purpose, topic, constraints, nonce |
| Response | Return accepted immutable references or a rejection | response version, query ID, decision, record hashes, policy hash |
| Acknowledgment | Record receipt without approval | acknowledgment version, response ID, actor, time, status |
| Revocation | Deny future use under an explicit rule | revocation version, target ID, issuer, reason class, effective time |
| Provenance link | Relate source, transformation, envelope, view, and use | link version, parent hashes, child hash, operation, actor |
| Retention policy | Bound availability and permitted historical evidence | policy version, data class, duration, expiry behavior |

## Common requirements

Every accepted record must:

- use a declared schema version and canonical serialization;
- have a deterministic content hash;
- contain no executable payload;
- bind actor, operation, purpose, scope, and policy identity;
- distinguish creation time from effective and expiry times;
- reject unknown fields when ambiguity would expand authority;
- preserve enough provenance to reproduce the decision;
- avoid secrets and raw source responses;
- support deterministic positive and negative fixtures.

## Capability model

Capabilities are independent. An implementation must not infer one from another.

| Operation | Meaning |
|---|---|
| `publish` | Submit a candidate envelope for validation |
| `discover` | Learn that an eligible topic or record class exists |
| `subscribe` | Register a bounded interest under an explicit lease |
| `read` | Receive an authorized immutable view |
| `acknowledge` | Record receipt or processing status |
| `revoke` | Invalidate future use where policy grants that authority |

A capability must bind to a subject, operation, topic or record scope, purpose, issuer, validity interval, and exact policy version. Wildcard scope is prohibited for the first contract candidate.

## Decision model

Validation produces an explicit result:

- `accepted` — all contract, capability, policy, hash, retention, and provenance checks pass;
- `rejected` — the submission is invalid or not authorized;
- `expired` — the governing lease or retention period has ended;
- `revoked` — an effective revocation prevents use;
- `version_mismatch` — a schema or policy version/hash is unknown or unacceptable.

Errors must be stable enough for testing but must not disclose secret or cross-scope information.

## Canonicalization

A future contract must choose and document one canonical representation. The canonicalization profile must specify:

- character encoding;
- key ordering;
- number and timestamp representation;
- Unicode normalization;
- null and omitted-field semantics;
- duplicate-key rejection;
- unknown-field behavior;
- hash algorithm and multihash or algorithm identifier;
- maximum depth, record size, collection size, and string length.

No hash claim is meaningful until this profile is accepted and fixtures prove cross-implementation consistency.

## Retention and revocation

Retention and revocation are related but distinct:

- retention determines how long a record or decision may remain available;
- expiry ends a lease or time-bound authorization;
- revocation changes future eligibility before ordinary expiry;
- historical evidence records that a decision occurred, subject to approved minimization and deletion rules.

The contract must define conflict resolution, clock assumptions, effective-time ordering, and replay behavior.

## Compatibility and migration

A change is incompatible when it alters canonical bytes, hashes, authority, required fields, decision semantics, retention, revocation, provenance, or consumer interpretation. Incompatible changes require:

1. a new contract version;
2. migration fixtures and expected hashes;
3. explicit consumer acceptance;
4. rollback instructions;
5. a transition window or deliberate hard cutover;
6. preservation of historical decision identity.

## Required fixture classes

- minimal valid records;
- boundary sizes and times;
- malformed and duplicate-key records;
- unknown schema and policy versions;
- altered content with stale hashes;
- missing or excessive capabilities;
- purpose and sensitivity mismatches;
- expired and revoked records;
- replayed requests and duplicate acknowledgments;
- cross-QSO and cross-topic isolation attempts;
- migration and rollback cases.

## Authority rule

A schema or validator may determine contract conformance. It may not approve conclusions, authorize external action, grant repository write access, create payment authority, or silently widen a portfolio component's role.
