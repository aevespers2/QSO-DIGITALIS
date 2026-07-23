# Task Chain

## Repository status

QSO-DIGITALIS remains a charter-or-retirement decision. Current `main` contains no approved product charter, accepted schema contract, tested field implementation, Pages publication, package release, or deployment surface.

Historical PR #2 proposed a bounded Digital Consciousness Field architecture plus scaffold materialization. It is now stale relative to `main` and non-mergeable. Its useful charter questions remain review inputs; its implementation-bearing changes are not current authority.

States: `PROPOSED` · `READY` · `IN PROGRESS` · `BLOCKED` · `REVIEW` · `DONE`

## Product directive

- **Next objective:** complete a documentation-only charter review and explicitly approve, revise, or retire the repository.
- **User outcome:** contributors can identify the repository's proposed role, boundaries, non-goals, dependencies, risks, evidence state, and retirement route without mistaking roadmap or scaffold artifacts for implementation.
- **MVP scope:** project overview, Pages-ready front door, architecture and trust boundaries, repository/contract responsibility map, onboarding, developer guide, planning controls, exact-head documentation validation, and a decision packet.
- **Priority:** documentation integrity and charter disposition precede schemas, fixtures, materialization, runtime, storage, transport, signing, scheduling, publication, or integration.
- **Success criteria:** the documentation is internally consistent and accessible; PR #2 is classified as historical/stale; one explicit charter or retirement decision is recorded; any future contract is versioned, hash-bound, non-overlapping, reversible, and accepted by each consumer independently.
- **Non-goals:** literal-consciousness claims, unrestricted shared memory, raw network/credential/package/binary/Git-object transport, implicit trust, autonomous approval, repository writes, payments, settlement, or production infrastructure.

## Active chain

| Priority | Task | Owner | Depends on | Status | Acceptance criteria |
|---|---|---|---|---|---|
| P0 | Establish a complete documentation and decision front door | QSOBuilder | — | IN PROGRESS | README and `docs/` provide overview, architecture, contract boundary, onboarding, developer guidance, accessible diagrams, planning links, non-goals, evidence states, and exact-head validation. |
| P0.1 | Disposition historical PR #2 | Architect / User | P0 | REVIEW | Useful charter material is preserved; stale implementation-bearing changes are superseded, revised, or rejected without history rewriting. |
| P0.2 | Approve, revise, or retire the QSO-DIGITALIS charter | Architect / User | P0-P0.1 | BLOCKED | Unique purpose, users, record families, source precedence, owners/vacancies, privacy/security/license/retention, consumer boundaries, correction/withdrawal, migration, rollback, and retirement are explicit. |
| P1 | Publish a minimum schema-first contract candidate | QSOBuilder | P0.2 approved as active | BLOCKED | Only approved schemas, canonicalization, namespaces, policies, fixtures, negative cases, migrations, validators, and exact-head evidence are added. |
| P2 | Implement one bounded local reference path | Builder | P1 accepted | PROPOSED | Disposable, credential-free, network-disabled, deterministic local verification passes retention, correction, revocation, replay, tamper, isolation, migration, and rollback tests. |
| P3 | Validate cross-repository consumers | Architect / Builders | P2 | PROPOSED | Exact consumer generations independently validate semantic compatibility and lifecycle propagation; parser success alone is insufficient. |
| P4 | Publish documentation or release artifacts | Release owner | P0.2-P3 and explicit approval | BLOCKED | Publication/release is separately approved, reproducible, accessible, provenance-bound, reversible, and verified after transition. |
| P5 | Retire the repository | Architect | P0.2 retirement decision | BLOCKED | README, repository description, release status, redirects, archives, ownership transfers, consumer migrations, and rollback evidence clearly record retirement. |

## Current documentation candidate

**Status:** `IN PROGRESS — DOCUMENTATION ONLY`

Branch `docs/digitalis-charter-front-door` prepares the missing reader routes and deterministic documentation checks. It does not approve the Digital Consciousness Field charter, merge historical PR #2, accept schemas, run a scaffold materializer, publish Pages, release a package, deploy a service, or grant operational authority.

## Architectural hold

Do not run any scaffold materializer with write mode, create runtime/storage/transport authority, publish field envelopes, register consumers, or alter downstream contracts until P0.2 is explicitly approved. `QSO-CONSENT-CAPACITY-LOCK-v1` and human final review remain mandatory.

## Builder log

Record exact branches and heads, documentation surfaces, validation commands/results, artifacts and expirations, architecture decisions, owner vacancies, security/privacy/license/accessibility review, migrations, rollback evidence, consumer dispositions, retirement links, and follow-ups.

- 2026-07-17 — Classified PR #2 as the first concrete charter candidate; no implementation or release was authorized.
- 2026-07-23 — Reclassified PR #2 as stale and non-mergeable relative to current `main`; began a current documentation-only front door without changing implementation scope.
