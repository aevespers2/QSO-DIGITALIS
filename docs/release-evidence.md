# Release evidence

QSO-DIGITALIS has no approved runtime release. This page turns `release.md` into a reviewable evidence map so that documentation, contract acceptance, implementation, release, and deployment cannot be conflated.

## Stage model

| Stage | Meaning | Current status |
|---|---|---|
| Documentation candidate | Accurate rendered description of repository state and candidate architecture | In progress |
| Charter candidate | Unique purpose, ownership, authority, boundaries, and retirement criteria | Draft PR #2 under review |
| Contract candidate | Accepted schemas, policies, canonicalization, fixtures, migrations, and validators | Blocked by P0 |
| Reference implementation candidate | One bounded local in-memory/filesystem conformance path | Blocked by P0 and P1 |
| Integration candidate | Exact-version/hash acceptance by SEEKER, QuantumStateObjects, and FABRIC | Blocked by P2 |
| Release candidate | Complete source, test, security, privacy, provenance, compatibility, and rollback evidence | Not selected |
| Deployment candidate | Separately approved target and operational authority | Not authorized |

## Documentation evidence

A documentation milestone requires:

- strict MkDocs build from the submitted source head;
- generated-site boundary validation;
- no secrets or restricted data in sources or artifacts;
- current/proposed capability separation;
- alignment with `taskchain.md`, `release.md`, `changelog.md`, and `punchlist.md`;
- successful consent-capacity lock;
- retained build artifact and digest where workflow support exists.

Documentation success does not pass P0 or authorize implementation.

## P0 charter evidence

- approved purpose and user outcome;
- canonical owner and relationship map;
- explicit inputs, outputs, authority, and non-goals;
- data, privacy, source-license, retention, revocation, and consent boundaries;
- identity and capability issuer decisions;
- versioning, migration, rollback, and retirement policy;
- approved first implementation profile or retirement plan;
- exact decision and commit identities.

## P1 contract evidence

- versioned schemas and policy records;
- deterministic canonicalization specification;
- positive, negative, malformed, oversized, boundary, expiry, revocation, replay, duplicate, tamper, and isolation fixtures;
- validator source and deterministic test results;
- schema and policy digests;
- compatibility and migration fixtures;
- threat, privacy, source-license, retention, and logging reviews;
- exact-head CI evidence and retained artifacts.

## P2 reference-path evidence

- local, disposable, synthetic, network-disabled, credential-free profile;
- confined filesystem and path-escape tests;
- resource and time limits;
- deterministic content store and tombstone behavior;
- capability, purpose, sensitivity, retention, revocation, replay, and provenance tests;
- cleanup and no-external-mutation evidence;
- complete rollback rehearsal.

## P3 integration evidence

Each consumer must bind to exact contract and policy versions and hashes.

### QSO-SEEKER

- publishes only accepted inert records;
- preserves source and canonicalization provenance;
- excludes raw responses, secrets, executable content, and unapproved source classes;
- rejects version and hash mismatches.

### QuantumStateObjects

- receives only capability-scoped, purpose-bound views;
- treats evidence as input, not instruction or authority;
- records exact references used;
- fails closed on expiry, revocation, mismatch, or unavailable provenance.

### QSO-FABRIC

- records reference-use evidence in the experiment ledger;
- preserves contract, policy, and record digests;
- does not promote conclusions solely because evidence was available;
- rejects incompatible or unverified bundles.

## Release candidate artifact set

A future release candidate should include:

- source archive bound to an exact commit;
- contract, schema, policy, fixture, and canonicalization manifests;
- test reports and coverage appropriate to the accepted scope;
- security, privacy, source-license, retention, and threat-review records;
- dependency inventory and SBOM where applicable;
- artifact checksums and provenance statement;
- migration and compatibility report;
- downstream acceptance evidence;
- operations, incident, rollback, and post-validation records;
- explicit release approval.

## Deployment gate

Deployment remains a separate decision. A release candidate cannot create its own target, credentials, public endpoint, schedule, or administrative authority. The deployment record must identify the operator, target, data boundary, credentials owner, monitoring, incident responder, emergency stop, rollback owner, support period, and human approval.

## Failure and rollback

Any failed gate leaves later stages blocked. Do not weaken tests, reclassify warnings, omit incompatible consumers, or relabel scaffold output as implementation. Preserve evidence, restore the last accepted state, correct the candidate, and repeat all affected gates against one immutable source head.
