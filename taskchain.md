# Task Chain

## Repository status

QSO-DIGITALIS has one draft charter candidate, PR #2, but no approved product charter, accepted schema contract, tested implementation, or deployment surface. The expanded README, architecture document, roadmap manifest, and scaffold materializer are proposal evidence only and must not be presented as implemented field capability.

States: `PROPOSED` · `READY` · `IN PROGRESS` · `BLOCKED` · `REVIEW` · `DONE`

## Product directive

- **Next objective:** Review draft PR #2 as a documentation/architecture charter candidate and either approve a unique bounded Digital Consciousness Field role, request bounded correction, or retire/archive the repository.
- **User outcome:** Portfolio contributors can determine whether QSO-DIGITALIS owns a necessary capability-scoped, content-addressed evidence-exchange contract; how it differs from QSO-SEEKER retrieval/canonicalization, QuantumStateObjects local runtime, QSO-FABRIC experiment evidence, Repository `0` proposal generation, and Repository `1` canonical-state/capability authority; and what authority it explicitly lacks.
- **MVP scope:** documentation-only decision covering purpose, users, field-envelope inputs/outputs, non-goals, trust/data/privacy/license/retention boundaries, publisher/subscriber capability separation, repository relationships, verification strategy, migration/rollback, and retirement criteria.
- **Priority:** Charter disposition is the only active priority. No scaffold materialization, field runtime, transport, storage, signing, schedule, or cross-repository integration is authorized before P0 approval.
- **Success criteria:** an approved charter establishes a non-overlapping stable contract and explicit evidence-only authority boundary, or the repository is retired; downstream repositories accept the contract by version/hash; no implementation task is opened solely because roadmap files or generated placeholders exist.
- **Non-goals:** literal-consciousness claims, raw network/credential/archive/package/binary/Git-object transport, unrestricted shared memory, implicit QSO trust, autonomous approval, repository writes, payments, settlement, or production infrastructure.
- **Release rationale:** draft PR #2 creates a plausible bounded charter and public overview, but its scaffold plan and materializer are proposal artifacts and require architecture, security, privacy, retention, legal/license, provenance, and downstream-consumer review.

## Active chain

| Priority | Task | Owner | Depends on | Status | Acceptance criteria |
|---|---|---|---|---|---|
| P0 | Approve, revise, or retire the QSO-DIGITALIS charter | Architect / User | — | REVIEW | Draft PR #2 receives explicit disposition; purpose, users, envelopes, capabilities, trust/data/privacy/license/retention boundaries, non-overlap, verification, migration, rollback, and retirement criteria are approved. |
| P1 | Publish the minimum schema-first contract candidate | QSOBuilder | P0 approved as active | BLOCKED | Only charter-approved schemas, policies, fixtures, negative cases, migrations, tests, and exact-head CI are added; roadmap placeholders do not count as implementation. |
| P2 | Implement one bounded local in-memory/filesystem reference path | Builder | P1 accepted | PROPOSED | Deterministic content addressing, capability scope, topic/purpose filtering, retention, revocation, replay, tamper detection, and provenance pass without credentials/network or implicit trust. |
| P3 | Validate cross-repository consumers | Architect / Builders | P2 | PROPOSED | QSO-SEEKER publishes only accepted inert records; QuantumStateObjects consumes read-only hash-fixed views; QSO-FABRIC records accesses in append-only evidence; all fail closed on version/hash mismatch. |
| P4 | Archive the repository | Architect | P0 retirement decision | BLOCKED | README, description, release state, and migration links clearly record retirement and ownership transfer. |

## Draft charter candidate — PR #2

**Status:** `REVIEW — DRAFT ARCHITECTURE/SCAFFOLD ONLY; USER AND ARCHITECT APPROVAL REQUIRED`

PR #2 is open and draft. Its current immutable head must be read from the pull request before review or validation; coordination documents do not hard-code a moving branch SHA. The candidate proposes a bounded Digital Consciousness Field architecture, a public project overview, a roadmap manifest, and a deterministic scaffold materializer. It explicitly excludes arbitrary code execution, raw credentials/packages/binaries/Git objects, unrestricted shared memory, implicit trust, self-issued capabilities, autonomous approval, and literal-consciousness claims. It does not include accepted schemas, fixtures, tests, CI evidence, security review, downstream compatibility, provenance, rollback evidence, or deployment approval.

## Architectural hold

Do not run the materializer with `--write`, create runtime/storage/transport authority, publish field envelopes, or change downstream contracts until P0 is explicitly approved. Any future implementation must remain content-addressed, capability-scoped, purpose-limited, retention/revocation aware, human-reviewed, non-executing, and independently testable by version/hash.

## Builder log

Record approvals, decisions, PR/head identities, validation commands/results, schema and artifact hashes, threat/privacy/license review, migrations, rollback evidence, downstream consumer results, retirement links, and follow-ups.

- 2026-07-20 — Expanded PR #2 with a bounded public README, repository relationship matrix, proposed evidence-flow diagram, explicit trust boundary, non-capabilities, and review path. No implementation or authority was added.
- 2026-07-17 — Classified draft PR #2 as the first concrete charter candidate. P0 moved from `BLOCKED` to `REVIEW`; no implementation, materialization, release, or deployment was authorized.
