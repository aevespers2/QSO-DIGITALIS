# Charter decision

## Decision required

Reviewers must choose one of three outcomes:

1. **Approve a bounded field-contract charter.** QSO-DIGITALIS becomes the owner of versioned evidence-exchange envelopes and related capability, policy, retention, revocation, and provenance contracts.
2. **Revise the candidate.** The repository remains on architectural hold while overlap, authority, data, legal, or operational concerns are corrected.
3. **Retire the repository.** Responsibility is transferred to an existing repository or determined unnecessary, and QSO-DIGITALIS becomes a provenance-preserving redirect or archive.

No default outcome is implied by the repository name or by the existence of scaffold files.

## Approval checklist

### Purpose and users

- The problem cannot be solved more cleanly inside an existing repository.
- Intended maintainers, publishers, consumers, reviewers, and operators are named.
- End-user expectations are not implied where no application exists.

### Non-overlap

- QSO-SEEKER retains retrieval, source isolation, sanitization, and canonical evidence production.
- QuantumStateObjects retains local QSO state and execution.
- QSO-FABRIC retains experiment assembly and evidence-use recording.
- Portfolio governance remains outside this repository.
- QSO-DIGITALIS owns only the approved exchange contracts.

### Authority

- Conformance decisions are distinct from conclusion or action approval.
- Publisher and consumer capabilities are explicit and separable.
- No repository writes, credentials, network retrieval, execution, payments, or deployment control are introduced.

### Data governance

- Data classes, minimization, public/private boundaries, purpose limits, retention, expiry, revocation, and deletion obligations are approved.
- Raw source material and secrets are excluded.
- Historical evidence retention is justified and bounded.

### Engineering evidence

- Canonicalization and hashing are specified.
- Positive, negative, boundary, replay, revocation, isolation, migration, and rollback fixtures exist.
- Exact-head CI and artifact provenance are retained.
- Downstream consumers accept an exact contract version and hash.

### Operations

- The first environment is local, disposable, credential-free, network-disabled, and synthetic-data-only.
- Limits, observability, incident response, recovery, cleanup, and rollback are testable.
- Separate approvals exist for charter, merge, release, and deployment.

## Decision record

An approval or retirement record should include:

- decision date and decision makers;
- selected outcome and rationale;
- canonical repository role;
- accepted non-goals and prohibited capabilities;
- relationships to neighboring repositories;
- license and support ownership;
- approved data classes and retention model;
- required verification evidence;
- migration, rollback, and retirement conditions;
- exact commit, PR, and artifact identities.

## Current recommendation

Draft PR #2 is sufficiently concrete to review as the leading charter candidate, but not to merge as implementation. The architecture is plausible only if it remains an inert, schema-first exchange contract and the non-overlap, privacy, retention, license, provenance, and downstream acceptance gates are explicitly approved.
