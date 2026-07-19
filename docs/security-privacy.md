# Security and privacy

## Security posture

The repository currently contains no accepted field runtime. The security model therefore defines requirements and prohibited authority for the charter candidate rather than claiming implemented controls.

## Threat model

A future contract must address:

- malformed or ambiguous records;
- duplicate keys and canonicalization differences;
- stale, altered, or substituted content hashes;
- unknown or downgraded schema and policy versions;
- forged, expired, over-broad, or replayed capabilities;
- cross-topic and cross-QSO data exposure;
- retention, expiry, or revocation bypass;
- provenance truncation or misleading ancestry;
- oversized records and resource exhaustion;
- secret, raw, executable, or unsupported payload insertion;
- misleading use of contract acceptance as conclusion approval.

## Required controls

- strict parsing with duplicate-key rejection;
- deterministic canonicalization and hashing;
- fail-closed version and policy resolution;
- least-privilege, operation-specific capabilities;
- purpose, sensitivity, source-class, retention, and experiment-scope filtering;
- explicit expiry and revocation evaluation on every access;
- bounded record, collection, depth, time, and replay limits;
- immutable decision and provenance identities;
- non-executable payload rules;
- no credentials or raw source responses in field records;
- stable rejection classes that avoid cross-scope disclosure;
- independently reproducible fixtures and exact-head evidence.

## Privacy principles

### Minimization

Exchange references and only the metadata necessary to validate scope and provenance. Do not copy full source material merely for convenience.

### Purpose limitation

Every request must state an accepted purpose. A capability valid for one purpose must not be reused for another by inference.

### Sensitivity boundaries

Record classes and sensitivity labels must be explicit. A consumer receives only the lowest-detail view required for the approved purpose.

### Retention and deletion

Availability, historical decision evidence, and deletion obligations must be separately defined. Retention must not be indefinite by default.

### Revocation

Revocation blocks future eligible use according to an explicit effective time and policy. Historical records must not be used as a hidden path to continue access.

## Logging and observability

Permitted operational evidence may include:

- exact source, schema, policy, and configuration hashes;
- actor and capability identifiers that are safe to retain;
- topic, purpose, decision class, expiry, and revocation status;
- bounded error codes;
- ledger heads and artifact checksums;
- cleanup and rollback results.

Logs must not contain secrets, raw credentials, raw source responses, executable content, or unrelated record bodies.

## Incident triggers

Stop validation or access and preserve evidence when any of the following occurs:

- a version or hash mismatch;
- nondeterministic results from identical accepted inputs;
- cross-scope disclosure;
- retention or revocation failure;
- unexpected network, credential, execution, or repository-write capability;
- provenance discontinuity or tamper evidence;
- authority expansion beyond contract conformance;
- misleading runtime or consciousness claims.

## Consent Capacity Lock

The repository-wide `QSO-CONSENT-CAPACITY-LOCK-v1` policy remains binding. This documentation does not weaken, bypass, or reinterpret that control. Any future consent-sensitive feature must require explicit consent, capacity to consent, and fail-closed behavior under the global system lock.

## Security non-claims

A documented requirement is not evidence that a control exists. Security acceptance requires implementation, adversarial fixtures, exact-head CI, retained reports, provenance, review, and separate approval.
