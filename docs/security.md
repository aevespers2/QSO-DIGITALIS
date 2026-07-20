# Security and privacy

QSO-DIGITALIS is a contract-stage repository. Security claims are therefore limited to controls that are present on `main` and requirements that a future candidate must satisfy.

## Present control

The repository contains the immutable policy `QSO-CONSENT-CAPACITY-LOCK-v1` and a pull-request workflow that scans supported text files for prohibited bypass language and requires consent-sensitive content to be bound to the lock. The control requires explicit, informed, freely given, specific, current, revocable consent and capacity to consent; ambiguous or invalid states fail closed and require human review.

This documentation does not modify that policy or broaden the repository's authority.

## Protected assets

- evidence content and canonical digests;
- source, transformation, envelope, and use provenance;
- publisher and subscriber identities;
- capability grants and policy decisions;
- purpose, sensitivity, retention, revocation, and review metadata;
- negative decisions, tombstones, and incident evidence;
- schema, policy, canonicalization, validator, and migration identities;
- private source terms and personal or confidential data that must not enter public artifacts.

## Threat model

| Threat | Required response |
|---|---|
| Malformed or oversized records | Deterministic limits, schema rejection, bounded diagnostics |
| Content substitution | Verify canonical digest, schema digest, and provenance chain before access |
| Publisher impersonation | Explicit verifiable identity and publisher capability; no display-name trust |
| Capability confusion | Separate operations, deny by default, prohibit implicit or transitive grants |
| Purpose or sensitivity crossing | Compute the intersection of record, policy, consumer, and experiment constraints |
| Replay outside policy | Bind nonce or event identity, time, contract version, and replay rules |
| Revoked or expired access | Enforce revocation and expiry before discovery and resolution; preserve tombstones |
| Cross-QSO leakage | Isolate views by subject, purpose, source class, sensitivity, and experiment |
| Provenance truncation | Reject broken or unverifiable chains; never promote an orphaned reference |
| Executable or secret-bearing payload | Reject prohibited media classes, active content, credentials, tokens, and private keys |
| Path escape in local adapters | Resolve against a confined root, reject links and traversal, enforce byte and file limits |
| Policy downgrade | Bind exact policy digests and require explicit migration and review |
| Misleading capability claim | Keep generated placeholders, roadmaps, and diagrams labeled as proposal evidence |

## Data classification

A future contract must define at least:

- **Public:** intentionally publishable metadata and records with verified source terms.
- **Portfolio-internal:** architecture, test fixtures, and non-secret operational evidence not approved for public publication.
- **Restricted:** personal, confidential, licensed, legally constrained, or security-relevant records available only to explicitly approved consumers.
- **Prohibited:** credentials, session material, private keys, raw authentication artifacts, executable packages, binaries, unrestricted archives, or records lacking a lawful and approved purpose.

Public GitHub Pages content must contain only public documentation and synthetic examples. It must not become a data plane, record store, administrative console, or source of secrets.

## Privacy requirements

Before accepting any implementation candidate, reviewers must approve:

1. data classes and permitted sources;
2. lawful and documented purpose for each flow;
3. minimization and redaction rules;
4. source-license and notice obligations;
5. retention, deletion eligibility, legal hold, and tombstone behavior;
6. access, correction, revocation, and incident procedures;
7. public/private artifact boundaries;
8. logging fields and secret-exclusion tests;
9. downstream propagation and deletion semantics;
10. evidence proving that rejected records do not leak through diagnostics.

## Least privilege

- The first reference path must have no network access, credentials, external repository writes, or deployment authority.
- Publishers cannot read merely because they can publish.
- Discovery cannot resolve content unless a separate read capability is valid.
- Consumers cannot revoke, administer policy, or delegate unless separately authorized.
- Administrative changes require a different approval path from ordinary evidence use.
- UI and documentation surfaces remain read-only.
- Release and deployment credentials remain outside the exchange boundary.

## Logging and evidence

Operational evidence should include only non-secret identifiers, contract and policy digests, decision codes, bounded timing, record counts, limit events, revocation and retention transitions, and artifact hashes. It should never log credentials, raw restricted records, full private paths, or unnecessary personal data.

## Security stop conditions

Stop and preserve evidence when a candidate exhibits:

- unknown or mismatched source, schema, policy, or artifact identity;
- nondeterministic canonicalization or validation;
- purpose, sensitivity, retention, revocation, or isolation failure;
- secret or restricted-data exposure;
- implicit trust, capability escalation, or unauthorized delegation;
- network, execution, repository-write, release, payment, or deployment capability outside approved scope;
- inability to restore a previous accepted contract state;
- conflict with `QSO-CONSENT-CAPACITY-LOCK-v1`.

Restart requires a corrected candidate, exact-head evidence, a fresh security and privacy review, and explicit approval. Automatic unlock is not permitted by the repository policy.
