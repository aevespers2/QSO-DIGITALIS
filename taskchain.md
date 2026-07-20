# Task Chain

## Repository status

QSO-DIGITALIS has one draft charter candidate, PR #2, but no approved product charter, accepted schema contract, tested implementation, or deployment surface. A Pages-ready documentation candidate now clarifies the proposal, responsibility boundaries, design requirements, decision process, onboarding, limitations, and recovery posture without authorizing implementation.

States: `PROPOSED` · `READY` · `IN PROGRESS` · `BLOCKED` · `REVIEW` · `DONE`

## Product directive

- **Next objective:** Review draft PR #2 together with the documentation candidate and either approve a unique bounded Digital Consciousness Field role, request bounded correction, or retire/archive the repository.
- **User outcome:** Portfolio contributors can determine whether QSO-DIGITALIS owns a necessary capability-scoped, content-addressed evidence-exchange contract; how it differs from QSO-SEEKER retrieval/canonicalization, QuantumStateObjects local runtime, and QSO-FABRIC experiment evidence; and what authority it explicitly lacks.
- **MVP scope:** documentation-only disposition covering purpose, users, field-envelope inputs/outputs, non-goals, trust/data/privacy/license/retention boundaries, publisher/subscriber capability separation, repository relationships, verification strategy, migration/rollback, operations, and retirement criteria.
- **Priority:** Charter disposition is the only active priority. No scaffold materialization, field runtime, transport, storage, signing, schedule, or cross-repository integration is authorized before P0 approval.
- **Success criteria:** an approved charter establishes a non-overlapping stable contract and explicit evidence-only authority boundary, or the repository is retired; downstream repositories accept the contract by exact version/hash; no implementation task is opened solely because roadmap or documentation files exist.
- **Non-goals:** literal-consciousness claims, raw network/credential/archive/package/binary/Git-object transport, unrestricted shared memory, implicit QSO trust, autonomous approval, repository writes, payments, settlement, or production infrastructure.
- **Release rationale:** draft PR #2 creates a plausible bounded charter, and the documentation candidate makes its review surface explicit. Both remain proposals requiring architecture, security, privacy, retention, legal/license, provenance, accessibility, operations, and downstream-consumer review.

## Active chain

| Priority | Task | Owner | Depends on | Status | Acceptance criteria |
|---|---|---|---|---|---|
| P0 | Approve, revise, or retire the QSO-DIGITALIS charter | Architect / User | — | REVIEW | Draft PR #2 and ADR-0001 receive explicit disposition; purpose, users, envelopes, capabilities, trust/data/privacy/license/retention boundaries, non-overlap, verification, migration, rollback, operations, and retirement criteria are approved. |
| P0-DOC | Validate the Pages documentation candidate | Documentation reviewer | — | REVIEW | `mkdocs build --strict`, links, diagrams, accessibility, privacy, license, terminology, exact-head provenance, and claim review pass; publication remains separately approved. |
| P1 | Publish the minimum schema-first contract candidate | QSOBuilder | P0 approved as active | BLOCKED | Only charter-approved schemas, policies, canonicalization, fixtures, negative cases, migrations, tests, and exact-head CI are added; roadmap placeholders do not count as implementation. |
| P2 | Implement one bounded local in-memory/filesystem reference path | Builder | P1 accepted | PROPOSED | Deterministic content addressing, capability scope, topic/purpose filtering, retention, revocation, replay, tamper detection, and provenance pass without credentials/network or implicit trust. |
| P3 | Validate cross-repository consumers | Architect / Builders | P2 | PROPOSED | QSO-SEEKER publishes only accepted inert records; QuantumStateObjects consumes read-only hash-fixed views; QSO-FABRIC records accesses in append-only evidence; all fail closed on version/hash mismatch. |
| P4 | Archive the repository | Architect | P0 retirement decision | BLOCKED | README, description, release state, and migration links clearly record retirement and ownership transfer. |

## Draft charter candidate — PR #2

**Status:** `REVIEW — DRAFT ARCHITECTURE/SCAFFOLD ONLY; USER AND ARCHITECT APPROVAL REQUIRED`

PR #2 proposes a bounded Digital Consciousness Field architecture, a roadmap manifest, and a deterministic scaffold materializer. It explicitly excludes arbitrary code execution, raw credentials/packages/binaries/Git objects, unrestricted shared memory, implicit trust, and literal-consciousness claims. It does not include accepted schemas, fixtures, tests, CI evidence, security review, downstream compatibility, provenance, rollback evidence, or deployment approval.

## Documentation candidate

**Status:** `REVIEW — DOCUMENTATION ONLY; NO PAGES PUBLICATION OR CAPABILITY AUTHORIZED`

The Pages candidate adds a project overview, architecture and authority diagrams, proposed design contracts, charter-decision framework, security/privacy requirements, limitations, onboarding, operations/recovery guidance, and ADR-0001. It is intended to make P0 review complete and testable, not to resolve P0 by implication.

## Architectural hold

Do not run the materializer with `--write`, create runtime/storage/transport authority, publish field envelopes, or change downstream contracts until P0 is explicitly approved. Any future implementation must remain content-addressed, capability-scoped, purpose-limited, retention/revocation aware, human-reviewed, non-executing, and independently testable by exact version/hash.

## Builder Log

Record approvals, decisions, PR/head identities, validation commands/results, schema and artifact hashes, threat/privacy/license review, migrations, rollback evidence, downstream consumer results, retirement links, and follow-ups.

- 2026-07-17 — Classified draft PR #2 as the first concrete charter candidate. P0 moved from `BLOCKED` to `REVIEW`; no implementation, materialization, release, or deployment was authorized.
- 2026-07-19 — Added a Pages-ready documentation candidate aligned with the architectural hold. P0 remains `REVIEW`; documentation validation and explicit charter disposition are still required.
