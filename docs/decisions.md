# Decisions and open questions

## Decision status

The repository is at **P0: approve, revise, or retire the charter**. Draft PR #2 is the first concrete architecture/scaffold candidate, but no field contract or implementation authority has been accepted.

## Decision 0001 — Charter before implementation

**Status:** accepted repository policy

No schemas, runtime, transport, storage, signing, external integration, or deployment may be treated as authorized until the repository has a unique, bounded charter. A roadmap or materializer cannot satisfy this gate.

## Decision 0002 — Architectural naming is not a consciousness claim

**Status:** accepted clarification

“Digital Consciousness Field” is a proposed architecture name for evidence exchange. It does not establish literal consciousness, awareness, sentience, personhood, legal status, or independent agency.

## Decision 0003 — Evidence-only authority

**Status:** proposed for P0 approval

The candidate contract may govern inert evidence references, policy metadata, capability-scoped access, lifecycle events, and audit evidence. It may not grant execution, credentials, repository writes, payments, release, deployment, or physical-world authority.

## Decision 0004 — Schema and fixtures precede a reference path

**Status:** proposed for P0 approval

If the repository remains active, schemas, canonicalization rules, policies, migrations, and positive/negative fixtures must be accepted before any local reference implementation. The first path must be disposable, synthetic, credential-free, network-disabled, and bounded.

## Decision 0005 — Consent-capacity control remains binding

**Status:** accepted repository control

`QSO-CONSENT-CAPACITY-LOCK-v1` applies across repository files and interfaces. Candidate designs must fail closed when consent or capacity is missing, ambiguous, withdrawn, expired, coerced, mismatched, or unverifiable, and require fresh human review before resumption.

## P0 questions requiring architectural disposition

### Unique ownership

- Is QSO-DIGITALIS the canonical owner of the exchange contract, or does an accepted contract already exist in another repository?
- Does the repository own only envelope and lifecycle semantics, or also deterministic canonicalization of evidence records?
- Which repository owns the vocabulary for topic, source class, purpose, sensitivity, and experiment scope?

### Relationship boundaries

- What exact artifact does QSO-SEEKER publish: complete canonical record, reference, or both?
- Does QuantumStateObjects resolve records directly through a local adapter or only receive pre-resolved bounded views?
- Which exchange events become part of the QSO-FABRIC experiment ledger?
- Where does Bridge begin when external verification or publication is separately approved?

### Identity and capability

- Which canonical identity system issues publisher and subscriber identifiers?
- Which component grants, signs, revokes, and audits capabilities?
- Are grants local configuration records, signed artifacts, or both?
- How are delegation, expiry, clock authority, and emergency revocation handled?

### Data governance

- What data classes are permitted?
- Who approves source terms, purpose, sensitivity, retention, redaction, and deletion behavior?
- How are restricted records kept out of public repositories, Pages, logs, CI artifacts, and pull-request discussions?
- What correction, revocation, and downstream propagation obligations apply?

### Contract lifecycle

- What is the canonical serialization and digest suite?
- Which changes are compatible, and which require a new major version?
- How long must old consumers remain supported?
- How are tombstones, supersession, and provenance preserved across migration?

### Operational authority

- Which repository or service owns autonomous task prioritization, branch and pull-request preparation, verification orchestration, merging, release, deployment, rollback, and incident response?
- What human final approvals remain mandatory?
- What emergency stop mechanism invalidates pending capabilities across consumers?

## Approval record requirements

A P0 disposition should record:

- decision date and reviewers;
- active, revise, or retire outcome;
- concise purpose and user outcome;
- canonical owner and maintainers;
- inputs, outputs, authority, and explicit non-goals;
- upstream and downstream contracts;
- data, privacy, source-license, retention, and consent boundaries;
- versioning, migration, rollback, and retirement rules;
- first allowed implementation target, if active;
- evidence links and exact commit identities.

## Retirement record requirements

If retired, update the repository description and README, close or supersede architecture candidates, preserve the decision history, identify the successor contract, prevent scaffold materialization from being mistaken for implementation, and record migration guidance in `taskchain.md`, `release.md`, and `changelog.md`.
