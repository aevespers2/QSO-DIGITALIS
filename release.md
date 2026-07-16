# Release Plan

## Current Decision
Status: `BLOCKED — APPROVAL REQUIRED`

No release is eligible because the repository has no approved charter or evidence-backed implementation surface. P0 is blocked on a user decision, all preparation and quality-gate items are unchecked, and reviewed commit `395f1acbacf7e7c7996d6df14f8023d47f7686a7` has no reported commit-status checks.

## Versioning
- Scheme: Semantic Versioning after charter approval.
- First possible documentation-only candidate: `0.0.1-charter.1`.
- First implementation candidate: `0.1.0-alpha.1`, only after the schema-first skeleton and versioned integration contract are verified.
- No tag may imply runtime capability before P1 and P2 are complete.

## Candidate Scope
### Charter candidate
- Approved purpose, users, inputs, outputs, non-goals, trust boundary, repository relationships, data classification, license, and verification strategy.

### Later implementation candidate
- Charter-approved schema-first directories, fixtures, tests, and CI.
- Versioned, hash-verifiable integration contract.
- No autonomous execution, credentials, unrestricted networking, direct settlement, or self-modifying behavior.

## Selected Completed Work
None. Coordination files and `changelog.md` are not a releaseable charter or implementation.

## Planned Changelog Entries
- `Documentation`: approved repository charter, boundaries, data classification, and verification strategy.
- `Added`: schema-first skeleton, fixtures, tests, and versioned contract after approval.
- `Security`: explicit prohibition and verification of credentials, unrestricted network access, autonomous execution, settlement, and self-modification.

## Acceptance Gates
| Gate | Status | Requirement |
|---|---|---|
| Charter approval | BLOCKED | User approves purpose, users, inputs, outputs, non-goals, trust boundary, relationships, data classification, and license. |
| Task completion | FAIL | P0 is `DONE`; no implementation release until P1 and P2 are `DONE`. |
| Tests/validation | NO EVIDENCE | Schemas, fixtures, negative cases, and hash verification pass deterministically. |
| Security | NO EVIDENCE | Prohibited capabilities are absent and independently checked. |
| Documentation | FAIL | README charter and verification strategy do not yet exist. |
| Provenance | NO EVIDENCE | Approval record, commit, commands, schema/fixture hashes, tool versions, and artifact checksums recorded. |
| Approval | PENDING | Separate release approval after the applicable gates pass. |

## Artifact Requirements
- Approved charter source and rendered documentation for the charter candidate.
- For implementation: schemas, fixtures, test reports, security report, source archive/package, SBOM where applicable, checksums, and provenance manifest.

## Rollback Criteria
Withdraw a charter candidate if its scope is ambiguous or conflicts with another repository. Roll back an implementation candidate if code exceeds the charter, introduces a prohibited capability, cannot validate contracts independently, or produces non-reproducible hashes. Restore the previous verified tag and preserve failed-candidate evidence.

## Unresolved Blockers
- Approval is required for the repository charter and license/data-classification model.
- No implementation task is authorized until P0 is approved.
- No schemas, fixtures, tests, CI, security evidence, documentation, or provenance exist.
- No CI status is attached to the reviewed commit.

## Release Log
- 2026-07-16: Candidate evaluated and held `BLOCKED — APPROVAL REQUIRED`; no completed work selected.