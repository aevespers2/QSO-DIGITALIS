# Task Chain

## Repository status

QSO-DIGITALIS remains a charter-or-retirement decision. Current `main` contains no approved product charter, accepted schema contract, tested field implementation, Pages publication, package release, or deployment surface.

Historical PR #2 is closed unmerged as a retired implementation/scaffold lineage at exact head `811f51ba983737e16ab5d465fb848aa5999b82d6`. Historical PR #5 is closed unmerged as a preserved interpretation and gluing source lineage at exact head `37b00a30f5b6f3df719e3884f7c1c8e79dd796a8`. Neither historical generation is current authority or current validation evidence.

States: `PROPOSED` · `READY` · `IN PROGRESS` · `BLOCKED` · `REVIEW` · `DONE`

## Product directive

- **Next objective:** complete a documentation-only charter review and explicitly approve, revise, split, migrate, or retire the repository.
- **User outcome:** contributors can identify the repository's proposed role, record identities, boundaries, non-goals, dependencies, gluing obstructions, evidence state, decision criteria, accessibility requirements, and retirement route without mistaking roadmap or historical artifacts for implementation.
- **MVP scope:** project overview, Pages-ready front door, architecture and trust boundaries, repository/contract responsibility map, source-observation interpretation profile, obstruction/gluing register, charter decision packet, retirement and migration guide, accessibility review, onboarding, developer guide, planning controls, and exact-head documentation validation.
- **Priority:** documentation integrity and charter disposition precede schemas, fixtures, materialization, runtime, storage, transport, signing, scheduling, publication, integration, release, or deployment.
- **Success criteria:** documentation is internally consistent and accessible; PR #2 and PR #5 are classified accurately; the profile preserves source/temporal/interpretation/projection/transport/disposition identities; the obstruction register names unresolved owners and required witnesses; one explicit charter or retirement decision is recorded; and any future contract is versioned, hash-bound, non-overlapping, reversible, and independently accepted by each consumer.
- **Non-goals:** literal-consciousness claims, unrestricted shared memory, raw network/credential/package/binary/Git-object transport, implicit trust, autonomous approval, repository writes, payments, settlement, or production infrastructure.

## Active chain

| Priority | Task | Owner | Depends on | Status | Acceptance criteria |
|---|---|---|---|---|---|
| P0 | Establish a complete documentation and decision front door | QSOBuilder | — | IN PROGRESS | README and `docs/` provide overview, architecture, contract boundary, interpretation profile, gluing register, decision packet, retirement/migration guidance, accessibility review, onboarding, developer guidance, planning links, non-goals, evidence states, and exact-head validation. |
| P0.1 | Disposition historical implementation and documentation lineages | Architect / User | P0 | REVIEW | PR #2 remains retired; useful PR #5 interpretation/gluing material is preservation-safely reconstructed with exact source attribution; no historical validation is promoted to the descendant. |
| P0.G | Complete profile and gluing analysis | QSOBuilder / Reviewers | P0 | REVIEW | Distinct record families, pairwise and triple-overlap witnesses, active obstructions, owner vacancies, failure states, correction/revocation propagation, migration, rollback, and accessibility routes are documented and validated. |
| P0.D | Complete decision, retirement, and accessibility evidence | QSOBuilder / Reviewers | P0 | REVIEW | Decision options and required evidence are explicit; consumer/dependency inventory and reversible retirement states exist; source accessibility checks pass; rendered review remains separately blocked. |
| P0.2 | Approve, revise, split, migrate, or retire the QSO-DIGITALIS charter | Architect / User | P0-P0.1-P0.G-P0.D | BLOCKED | Unique purpose, users, record families, source precedence, owners/vacancies, privacy/security/license/retention/accessibility, consumer boundaries, correction/withdrawal, migration, rollback, and retirement are explicit. |
| P1 | Publish a minimum schema-first contract candidate | QSOBuilder | P0.2 approved as active | BLOCKED | Only approved semantics, schemas, canonicalization, namespaces, policies, fixtures, negative cases, migrations, validators, and exact-head evidence are added. |
| P2 | Implement one bounded local reference path | Builder | P1 accepted | PROPOSED | Disposable, credential-free, network-disabled, deterministic local verification passes retention, correction, revocation, replay, tamper, isolation, migration, and rollback tests. |
| P3 | Validate cross-repository consumers | Architect / Builders | P2 | PROPOSED | Exact producer/consumer generations independently validate semantic compatibility and lifecycle propagation; parser success alone is insufficient. |
| P4 | Publish documentation or release artifacts | Release owner | P0.2-P3 and explicit approval | BLOCKED | Publication/release is separately approved, reproducible, accessible, provenance-bound, reversible, and verified after transition. |
| P5 | Retire the repository | Architect | P0.2 retirement decision | BLOCKED | README, repository description, release status, redirects, archives, ownership transfers, consumer migrations, residual-risk register, restoration target, and rollback evidence clearly record retirement. |

## Current composition route

The candidate route is:

`QSO-SEEKER source observation → temporal assessment → QSO-DIGITALIS interpretation/projection → Bridge transport → Repository 1 disposition → runtime/Fabric/interface view`

This route is not accepted. Active obstructions include source/interpretation identity collapse, temporal-owner overlap, generic-envelope conflict, transport/exchange overlap, derived-storage/canonical-state confusion, projection/capability confusion, privacy downgrade, correction divergence, subject-namespace mismatch, canonicalization disagreement, transformation opacity, reason-code drift, replay ambiguity, consumer-purpose mismatch, partial-state collapse, licensing/retention loss, emergency-stop gaps, runtime/Fabric role collision, and historical-lineage substitution.

## Current documentation candidate

**Status:** `IN PROGRESS — DOCUMENTATION ONLY`

Branch `docs/digitalis-charter-front-door` remains the non-default charter candidate. Focused branch `docs/digitalis-profile-gluing-reconciliation` reconstructs the unique interpretation and gluing material from historical PR #5 on the current candidate lineage, updates reader routes and planning controls, and adds fresh deterministic validation requirements. Neither branch approves the charter, revives PR #2 or PR #5 as implementation candidates, accepts schemas, publishes Pages, releases a package, deploys a service, or grants operational authority.

## Architectural hold

Do not run any scaffold materializer with write mode, create runtime/storage/transport authority, publish field envelopes, register consumers, change repository settings, or alter downstream contracts until P0.2 is explicitly approved. `QSO-CONSENT-CAPACITY-LOCK-v1` and human final review remain mandatory.

## FYSA-120 capability map

Applied categories: `CAT-011`, `CAT-012`, `CAT-013`, `CAT-017`, `CAT-018`, `CAT-019`, `CAT-031`, `CAT-040`, and `CAT-052`.

Applied subdivisions include `011-B`, `011-E`, `012-A`, `012-B`, `012-D`, `012-E`, `013-A`, `013-C`, `013-D`, `013-E`, `017-C`, `017-D`, `017-E`, `018-B`, `018-D`, `018-E`, `019-B`, `019-C`, `019-D`, `031-A`, `031-D`, `031-E`, `040-A`, `040-B`, `040-D`, and `040-E`.

Proposed non-authoritative refinements:

- `032-M — authority-separated interpretation, policy-projection, and exchange-envelope documentation with correction-closed compatibility witnesses`;
- `032-N — cross-repository obstruction ledgers, triple-overlap witnesses, and correction-closed gluing paths for evidence systems`.

Taxonomy mapping does not establish competence, appointment, ownership, acceptance, or authority.

## Builder log

Record exact branches and heads, documentation surfaces, validation commands/results, artifacts and expirations, architecture decisions, owner vacancies, security/privacy/license/accessibility review, migrations, rollback evidence, consumer dispositions, retirement links, and follow-ups.

- 2026-07-17 — Classified PR #2 as the first concrete charter candidate; no implementation or release was authorized.
- 2026-07-23 — Retired PR #2 unmerged and preserved PR #5 as a historical interpretation/gluing source; neither historical lineage is current authority.
- 2026-07-23 — Added a decision matrix, required disposition record, consumer-aware retirement sequence, restoration rules, and exact rendered-accessibility review requirements.
- 2026-07-24 — Reconstructed the interpretation profile and obstruction/gluing register from PR #5 on the current non-default candidate with explicit source attribution, distinct identities, compatibility witnesses, correction closure, and no implementation expansion.
