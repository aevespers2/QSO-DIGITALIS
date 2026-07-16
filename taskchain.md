# Task Chain

## Repository status

This repository has no evidence-backed charter or implementation surface beyond coordination files. Builders must not infer its purpose from the name.

States: `PROPOSED` · `READY` · `IN PROGRESS` · `BLOCKED` · `REVIEW` · `DONE`

## Product directive

- **Next objective:** Approve a unique repository charter or retire/archive QSO-DIGITALIS before implementation begins.
- **User outcome:** Portfolio contributors can determine whether this repository owns a necessary capability, how it differs from QSO-GENOMES, QSO-SEEKER, QSO-FABRIC, QuantumStateObjects, QSO-STUDIO, and QSO-PAYMENTS, and which contracts it may publish.
- **MVP scope:** documentation-only decision containing purpose, users, inputs, outputs, non-goals, trust boundary, data classification, privacy/license model, upstream/downstream relationships, verification strategy, and retirement criteria.
- **Priority:** Charter or retirement decision is the only active priority.
- **Success criteria:** the approved charter names a non-overlapping user problem and stable contract boundary, or the repository is explicitly retired; no implementation task is opened without that evidence.
- **Non-goals:** inferring a digital-identity, digital-twin, runtime, wallet, or autonomous-agent product from the repository name; adding credentials, networking, execution, settlement, or duplicated schemas before approval.
- **Release rationale:** A documentation-only charter can preserve a valid product slot, while retirement prevents duplicate ownership and misleading public scope.

## Active chain

| Priority | Task | Owner | Depends on | Status | Acceptance criteria |
|---|---|---|---|---|---|
| P0 | Approve or retire the QSO-DIGITALIS repository charter | Architect | User decision | BLOCKED | Purpose, users, inputs/outputs, non-goals, trust/data/privacy/license boundaries, repository relationships, verification plan, and retirement criteria are approved. |
| P1 | Create the minimum schema-first skeleton | QSOBuilder | P0 approved as active | PROPOSED | Only charter-approved directories, schemas, fixtures, tests, and CI are added; no autonomous execution, credentials, unrestricted network access, or settlement is introduced. |
| P2 | Publish a versioned integration contract | Builder | P1 | PROPOSED | Consumers validate inputs/outputs by schema version and hash without importing repository code. |
| P3 | Archive the repository | Architect | P0 retirement decision | BLOCKED | README, repository description, and release state clearly record retirement and point to the owning repositories. |

## Architectural hold

No implementation task is `READY` until P0 is approved. Retirement is a valid product outcome.

## Builder Log

Record approvals, decisions, commits, validation commands/results, hashes, risks, retirement links, and follow-ups.