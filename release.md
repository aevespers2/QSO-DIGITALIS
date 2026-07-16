# Release Plan

## Current Decision

Status: `BLOCKED — CHARTER OR RETIREMENT APPROVAL REQUIRED`

QSO-DIGITALIS has no evidence-backed product charter or implementation surface beyond coordination files. P0 is blocked on a user decision, no implementation task is authorized, all quality evidence is absent, and candidate head `f00b0dfacd672baa5cb3b723e97210bc2efcfe07` has no tests, security checks, documentation artifact, provenance, or repository-specific acceptance evidence.

## Versioning

- Scheme: Semantic Versioning only after an active charter is approved.
- First possible documentation candidate: `0.0.1-charter.1`.
- First implementation candidate: `0.1.0-alpha.1`, only after a schema-first skeleton and versioned integration contract pass.
- A retirement outcome must not imply any runtime capability.

## Release Scope

### Charter candidate
- Purpose, users, inputs/outputs, non-goals, trust boundary, data classification, privacy/license model, repository relationships, verification strategy, and retirement criteria.

### Later implementation candidate
- Charter-approved declarative schemas, fixtures, tests, CI, versioned/hash-verifiable integration contract, and no autonomous execution, credentials, unrestricted networking, settlement, or self-modification.

## Selected Completed Work

None. Coordination files and changelog entries are not a releasable charter or implementation.

## Planned Changelog Entries

- `Documentation`: approved charter or retirement notice.
- `Added`: schema-first skeleton and versioned contract only after approval.
- `Security`: verified absence of prohibited authority and credential/network/settlement paths.
- `Release`: rendered charter or implementation artifacts, checksums, provenance, and approval.

## Acceptance Gates

| Gate | Status | Requirement |
|---|---|---|
| Charter/retirement approval | BLOCKED | Approve a unique non-overlapping purpose or retire the repository. |
| Task completion | FAIL | P0 is `DONE`; implementation requires P1-P2 `DONE`. |
| Tests/contracts | NO EVIDENCE | Schemas, references, fixtures, negative cases, and hashes validate deterministically. |
| Security | NO EVIDENCE | Prohibited capabilities are absent and independently checked. |
| Documentation | FAIL | Approved charter, boundaries, and verification strategy are absent. |
| Provenance | NO EVIDENCE | Decision record, commit, commands, versions, artifacts, hashes, and attestations are retained. |
| Approval | PENDING | Separate release approval after applicable gates pass. |

## Artifact Requirements

- Approved charter or retirement notice in source and rendered form.
- For implementation: schemas, fixtures, validation/test reports, security report, source/package artifact, SBOM where applicable, checksums, provenance, and rollback evidence.

## Rollback Criteria

Withdraw a charter candidate if its scope is ambiguous, overlaps another repository, or leaves data/authority boundaries unresolved. Roll back implementation if it exceeds the charter, introduces prohibited capability, fails independent contract validation, or produces non-reproducible hashes. Preserve failed-candidate evidence and restore the prior verified state.

## Unresolved Blockers

- Approval is required to activate or retire QSO-DIGITALIS and to select its privacy/license/data-classification model.
- No implementation task is authorized until P0 is approved.
- No schemas, fixtures, tests, CI, security evidence, documentation artifact, provenance, or rollback evidence exists.

## Release Log

- 2026-07-16: Reclassified the candidate as a charter-or-retirement decision; no release-ready work selected.