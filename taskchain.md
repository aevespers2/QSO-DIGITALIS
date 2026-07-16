# Task Chain

## Repository status
This repository currently has no evidence-backed charter or implementation surface beyond coordination files. Builders must not infer its purpose from the name.

States: `PROPOSED` · `READY` · `IN PROGRESS` · `BLOCKED` · `REVIEW` · `DONE`

| Priority | Task | Owner | Depends on | Status | Acceptance criteria |
|---|---|---|---|---|---|
| P0 | Approve the QSO-DIGITALIS repository charter | Architect | User decision | BLOCKED | `README.md` defines purpose, users, inputs, outputs, non-goals, trust boundary, relation to the other QSO repositories, data classification, license, and verification strategy. |
| P1 | Create the minimum schema-first skeleton | QSOBuilder | P0 | PROPOSED | Only charter-approved directories, schemas, fixtures, tests, and CI are added; no autonomous execution, credentials, unrestricted network access, or production settlement is introduced. |
| P2 | Publish a versioned integration contract | Builder | P1 | PROPOSED | Consumers can validate inputs/outputs by schema version and hash without importing repository code. |

## Architectural hold
No implementation task is `READY` until P0 is approved.

## Builder Log
Record approvals, commits, validation commands/results, hashes, risks, and follow-ups.
